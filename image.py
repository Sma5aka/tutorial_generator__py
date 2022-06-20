from PIL import Image, ImageDraw, ImageFont
import re

def cut_str(stri, index):
	stri = stri[:index]+'\n'+stri[index:];
	arr = stri.split('\n');
	return arr;

def cut_str2(stri, widths):

	for i in range(len(stri)):
		str_width = 0;
		for k in range(len(stri[i])):
			str_width = str_width + widths[stri[i][k]];
			if str_width > 650:
				stri[i] = cut_str(stri[i], k);
				break;
	return stri;

def in_one_str(arr):
	sentence = "";
	for word in arr:
		if isinstance(word, list):
			word = in_one_str(word);
		sentence += str(word) + "\n";
	return sentence;

def draw_exam(school_names, name_sch, exams, course_projs, course_works, offsets, offset_w_grades, practices, proff, year, num_sem, widths):
	free_space_point = 100;

	main_img = Image.new('RGBA', (1024, 1024));
	main_img.paste(school_names[name_sch], (0,0), school_names[name_sch]);

	second_img = Image.new('RGBA', (1024, 1024));
	second_img.paste(school_names[name_sch], (0,0), school_names[name_sch]);

	if exams != ['']:
		exams = cut_str2(exams, widths);
		n_exams = 0;
		for exam in exams:
			if isinstance(exam, list):
				n_exams += 2;
			else:
				n_exams += 1;

		n = (n_exams * 31 + 15.5 * (n_exams - 1) + 31)-10+31;

		if n-0.5 != int(n):
			n = int(n);

		result = in_one_str(exams);
		result = re.sub("\n\n", '\n', result);

		free_space_point += n+26;

		route = "images\\light\\exam\\"+str(n)+".png";
		for_exams = Image.open(route);

		for_exams_draw = ImageDraw.Draw(for_exams);
		for_exams_draw.text((30,35), result, font=main_font, fill="#163E5A");

		main_img.paste(for_exams, (35,100), for_exams);

	main_img_draw = ImageDraw.Draw(main_img);
	second_img_draw = ImageDraw.Draw(second_img);

	name_of_pic = proff + '-' + year + '-' + num_sem;

	if name_sch == "pi":
		main_img_draw.text((133, 28), name_of_pic, font=header_font, fill="#163E5A");
		second_img_draw.text((133, 28), name_of_pic, font=header_font, fill="#163E5A");
	elif name_sch == "shm" or name_sch == "imo" or name_sch == "shp" or name_sch == "yur":
		main_img_draw.text((150, 28), name_of_pic, font=header_font, fill="#163E5A");
		second_img_draw.text((150, 28), name_of_pic, font=header_font, fill="#163E5A");
	elif name_sch == "imct" or name_sch == "shem":
		main_img_draw.text((190, 28), name_of_pic, font=header_font, fill="#163E5A");
		second_img_draw.text((190, 28), name_of_pic, font=header_font, fill="#163E5A");
	elif name_sch == "inszb" or name_sch == "shign":
		main_img_draw.text((210, 28), name_of_pic, font=header_font, fill="#163E5A");
		second_img_draw.text((210, 28), name_of_pic, font=header_font, fill="#163E5A");
	elif name_sch == "shrmi" or name_sch == "intpm" :
		main_img_draw.text((250, 28), name_of_pic, font=header_font, fill="#163E5A");
		second_img_draw.text((250, 28), name_of_pic, font=header_font, fill="#163E5A");

	draw_another(free_space_point, course_projs, course_works, offsets, offset_w_grades, practices, main_img, second_img, name_of_pic, widths);

	main_img.save(name_of_pic+".png");

	return main_img;
	
def draw_another(start_point, course_proj, course_work, offset, offset_w_grade, practice, main_img, second_img, name_of_pic, widths):
	free_space_start = start_point;
	free_space = 1024 - free_space_start;

	not_posted = {'course_proj': 0, 'course_work':0, 'offset':0, 'offset_w_grade':0, 'practice':0};

	if course_proj == ['']:
		not_posted['course_proj'] = 1;
	if course_work == ['']:
		not_posted['course_work'] = 1;
	if offset == ['']:
		not_posted['offset'] = 1;
	if offset_w_grade == ['']:
		not_posted['offset_w_grade'] = 1;
	if practice == ['']:
		not_posted['practice'] = 1;

	n_course_proj = 0; height_course_proj = 0;
	n_course_work = 0; height_course_work = 0;
	n_offset = 0; height_offset = 0;
	n_offset_w_grade = 0; height_offset_w_grade = 0;
	n_practice = 0; height_practice = 0;

	course_proj_res = "";
	course_work_res = "";
	offset_res = "";
	offset_w_grade_res = "";
	practice_res = "";

	if course_proj != "":
		course_proj = cut_str2(course_proj, widths);

		for proj in course_proj:
			if isinstance(proj, list):
				n_course_proj += 2;
			else:
				n_course_proj += 1;

		height_course_proj = (n_course_proj * 31 + 15.5 * (n_course_proj - 1) + 31)-10+31;

		if height_course_proj-0.5 != int(height_course_proj):
			height_course_proj = int(height_course_proj);
		
		course_proj_res = in_one_str(course_proj);
		course_proj_res = re.sub("\n\n", '\n', course_proj_res);

		for_course_proj = Image.open("images\\light\\course_proj\\"+str(height_course_proj)+".png");

		for_course_proj_draw = ImageDraw.Draw(for_course_proj);
		for_course_proj_draw.text((30,35), course_proj_res, font=main_font, fill="#163E5A");

	if course_work != "":
		course_work = cut_str2(course_work, widths);

		for work in course_work:
			if isinstance(work, list):
				n_course_work += 2;
			else:
				n_course_work += 1;

		height_course_work = (n_course_work * 31 + 15.5 * (n_course_work - 1) + 31)-10+31;

		if height_course_work-0.5 != int(height_course_work):
			height_course_work = int(height_course_work);
		
		course_work_res = in_one_str(course_work);
		course_work_res = re.sub("\n\n", '\n', course_work_res);

		for_course_work = Image.open("images\\light\\course_work\\"+str(height_course_work)+".png");

		for_course_work_draw = ImageDraw.Draw(for_course_work);
		for_course_work_draw.text((30,35), course_work_res, font=main_font, fill="#163E5A");

	if offset != "":
		offset = cut_str2(offset, widths);

		for offs in offset:
			if isinstance(offs, list):
				n_offset += 2;
			else:
				n_offset += 1;

		height_offset = (n_offset * 31 + 15.5 * (n_offset - 1) + 31)-10+31;

		if height_offset-0.5 != int(height_offset):
			height_offset = int(height_offset);
		
		offset_res = in_one_str(offset);
		offset_res = re.sub("\n\n", '\n', offset_res);

		for_offset = Image.open("images\\light\\offset\\"+str(height_offset)+".png");

		for_offset_draw = ImageDraw.Draw(for_offset);
		for_offset_draw.text((30,35), offset_res, font=main_font, fill="#163E5A");

	if offset_w_grade != "":
		offset_w_grade = cut_str2(offset_w_grade, widths);

		for offs in offset_w_grade:
			if isinstance(offs, list):
				n_offset_w_grade += 2;
			else:
				n_offset_w_grade += 1;

		height_offset_w_grade = (n_offset_w_grade * 31 + 15.5 * (n_offset_w_grade - 1) + 31)-10+31;

		if height_offset_w_grade-0.5 != int(height_offset_w_grade):
			height_offset_w_grade = int(height_offset_w_grade);
		
		offset_w_grade_res = in_one_str(offset_w_grade);
		offset_w_grade_res = re.sub("\n\n", '\n', offset_w_grade_res);

		for_offset_w_grade = Image.open("images\\light\\offset_w_grade\\"+str(height_offset_w_grade)+".png");

		for_offset_w_grade_draw = ImageDraw.Draw(for_offset_w_grade);
		for_offset_w_grade_draw.text((30,35), offset_w_grade_res, font=main_font, fill="#163E5A");

	if practice != "":
		practice = cut_str2(practice, widths);

		for praks in practice:
			if isinstance(praks, list):
				n_practice += 2;
			else:
				n_practice += 1;

		height_practice = (n_practice * 31 + 15.5 * (n_practice - 1) + 31)-10+31;

		if height_practice-0.5 != int(height_practice):
			height_practice = int(height_practice);
		
		practice_res = in_one_str(practice);
		practice_res = re.sub("\n\n", '\n', practice_res);

		for_practice = Image.open("images\\light\\practice\\"+str(height_practice)+".png");

		for_practice_draw = ImageDraw.Draw(for_practice);
		for_practice_draw.text((30,35), practice_res, font=main_font, fill="#163E5A");

	free_space_point2 = 100;
	need_second = 0;
	
	if (not_posted['course_proj'] == 0) & (height_course_proj <= free_space):
		main_img.paste(for_course_proj, (35, int(free_space_start)), for_course_proj);
		not_posted['course_proj'] = 1;
		free_space -= height_course_proj + 26;
		free_space_start = 1024 - free_space;
	elif (not_posted['course_proj'] == 0) & (height_course_proj > free_space):
		need_second = 1;
		second_img.paste(for_course_proj, (35, int(free_space_point2)), for_course_proj);
		not_posted['course_proj'] = 1;
		free_space_point2 += height_course_proj+26;
		
	if (not_posted['course_work'] == 0) & (height_course_work <= free_space):
		main_img.paste(for_course_work, (35, int(free_space_start)), for_course_work);
		not_posted['course_work'] = 1;
		free_space -= height_course_work + 26;
		free_space_start = 1024 - free_space;
	elif (not_posted['course_work'] == 0) & (height_course_work > free_space):
		need_second = 1;
		second_img.paste(for_course_work, (35, int(free_space_point2)), for_course_work);
		not_posted['course_work'] = 1;
		free_space_point2 += height_course_work+26;

	if (not_posted['offset'] == 0) & (height_offset <= free_space):
		main_img.paste(for_offset, (35, int(free_space_start)), for_offset);
		not_posted['offset'] = 1;
		free_space -= height_offset + 26;
		free_space_start = 1024 - free_space;
	elif (not_posted['offset'] == 0) & (height_offset > free_space):
		need_second = 1;
		second_img.paste(for_offset, (35, int(free_space_point2)), for_offset);
		not_posted['offset'] = 1;
		free_space_point2 += height_offset+26;

	if (not_posted['offset_w_grade'] == 0) & (height_offset_w_grade <= free_space):
		main_img.paste(for_offset_w_grade, (35, int(free_space_start)), for_offset_w_grade);
		not_posted['offset_w_grade'] = 1;
		free_space -= height_offset_w_grade + 26;
		free_space_start = 1024 - free_space;
	elif (not_posted['offset_w_grade'] == 0) & (height_offset_w_grade > free_space):
		need_second = 1;
		second_img.paste(for_offset_w_grade, (35, int(free_space_point2)), for_offset_w_grade);
		not_posted['offset_w_grade'] = 1;
		free_space_point2 += height_offset_w_grade+26;

	if (not_posted['practice'] == 0) & (height_practice <= free_space):
		main_img.paste(for_practice, (35, int(free_space_start)), for_practice);
		not_posted['practice'] = 1;
		free_space -= height_practice + 26;
		free_space_start = 1024 - free_space;
	elif (not_posted['practice'] == 0) & (height_practice > free_space):
		need_second = 1;
		second_img.paste(for_practice, (35, int(free_space_point2)), for_practice);
		not_posted['practice'] = 1;
		free_space_point2 += height_practice+26;
	#if free_space < 83:
		
	if(need_second == 1):
		second_img.save(name_of_pic+'(2)'+".png");


	return;


main_font = ImageFont.truetype('SF-Pro-Text-Regular.otf', 40);
header_font = ImageFont.truetype('SF-Pro-Text-Bold.otf', 40);

shrmi = Image.open("images\\shrmi.png");
imct = Image.open("images\\imct.png");
imo = Image.open("images\\imo.png");
inszb = Image.open("images\\inszb.png");
intpm = Image.open("images\\intmp.png");
pi = Image.open("images\\pi.png");
shign = Image.open("images\\shign.png");
shm = Image.open("images\\shm.png");
shp = Image.open("images\\shp.png");
shem = Image.open("images\\shem.png");
yur = Image.open("images\\yur.png");

school_imgs = {'shrmi':shrmi, 'imct':imct, 'imo':imo, 'inszb':inszb, 'intpm':intpm, 'pi':pi, 'shign':shign, 'shm':shm, 'shp':shp, 'shem':shem, 'yur':yur};


school_imgs = {'shrmi':shrmi, 'imct':imct, 'imo':imo, 'inszb':inszb, 'intpm':intpm, 'pi':pi, 'shign':shign, 'shm':shm, 'shp':shp, 'shem':shem, 'yur':yur};

eng_widths = {'a':17, 'b':20, 'c':19, 'd':20, 'e':19, 'f':12, 'g':20, 'h':18, 'i':6, 'j':9, 'k':18, 'l':4, 'm':29, 'n':18, 'o':20, 'p':19, 'q':20, 'r':12, 's':17, 't':12, 'u':18, 
'v':20, 'w':29, 'x':19, 'y':20, 'z':17, ' ':6, '.':6, '!':6, '(':9, '?':18, ')':9, '1':12, '2':19, '3':21, '4':22, '5':19, '6':21, '7':20, '8':21, '9':21, '0':21, ',':6, '-':14,
 'A':25, 'B':21, 'C':25, 'D':23, 'E':18, 'F':18, 'G':26, 'H':24, 'I':5, 'J':17, 'K':22, 'L':18, 'M':29, 'N':24, 'O':27, 'P':21, 'Q':27, 'R':21, 'S':22, 'T':23, 'U':23, 'V':25, 'W':36, 'X':24, 'Y':25, 'Z':22}

all_widths = {'a':17, 'b':20, 'c':19, 'd':20, 'e':19, 'f':12, 'g':20, 'h':18, 'i':6, 'j':9, 'k':18, 'l':4, 'm':29, 'n':18, 'o':20, 'p':19, 'q':20, 'r':12, 's':17, 't':12, 'u':18, 
'v':20, 'w':29, 'x':19, 'y':20, 'z':17, ' ':6, '.':6, '!':6, '(':9, '?':18, ')':9, '1':12, '2':19, '3':21, '4':22, '5':19, '6':21, '7':20, '8':21, '9':21, '0':21, ',':6, '-':14,
 'A':25, 'B':21, 'C':25, 'D':23, 'E':18, 'F':18, 'G':26, 'H':24, 'I':5, 'J':17, 'K':22, 'L':18, 'M':29, 'N':24, 'O':27, 'P':21, 'Q':27, 'R':21, 'S':22, 'T':23, 'U':23, 'V':25, 'W':36, 'X':24, 'Y':25, 'Z':22,
'а':18, 'б':20, 'в':17, 'г':14, 'д':24, 'е':19, 'ё':19, 'ж':29, 'з':17, 'и':18, 'й':18, 'к':17, 'л':19, 'м':24, 'н':18, 'о':20, 'п':18, 'р':20, 'с':19, 'т':18, 'у':20, 'ф':26, 'х':19, 'ц':21, 'ч':18, 'ш':27, 'щ':30, 'ъ':22, 'ы':23, 'ь':16, 'э':20, 'ю':27, 'я':17,
'А':25, 'Б':20, 'В':22, 'Г':18, 'Д':29, 'Е':19 'Ё':19, 'Ж':39, 'З':21, 'И':24, 'Й':24, 'К':23, 'Л':25, 'М':29, 'Н':24, 'О':27, 'П':23, 'Р':21, 'С':25, 'Т':22, 'У':23, 'Ф':29, 'Х':24, 'Ц':27, 'Ч':22, 'Ш':32, 'Щ':36, 'Ъ':28, 'Ы':29, 'Ь':21, 'Э':23, 'Ю':32, 'Я':22}

stringg = ['1. abcdefghijklmnopqrstuvwxyz fgsdfg fsg dfgsdfgsedfgds dfgssdf','2. ABCDEFGHIJKLMNOPQRSTUVWXYZ asdsa buiabfidb sdbfibisdf biuaosduffsdfsd','3. Mathematic analysis (LK-18, PR-34)','4.-','5!', '6,','7?','8-','9)','0(','11.']
string1 = ['']
string2 = ['']
string3 = ['']
string4 = ['']
string5 = ['']

shkola = "imct";
napravlenie = "shrmi";
god = "2020";
semestr = "1";
draw_exam(school_imgs, shkola, stringg, string1, string2, string3, string4, string5,napravlenie, god, semestr, all_widths);
