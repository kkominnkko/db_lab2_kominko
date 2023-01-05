SELECT category.hero_category, COUNT(heroes.category_id) FROM heroes
JOIN category ON category.category_id = heroes.category_id GROUP BY hero_category

SELECT roles.hero_role, COUNT(heroes.role_id) FROM heroes
JOIN roles ON roles.role_id = heroes.role_id GROUP BY hero_role

SELECT hero_name, hero_intelligence FROM heroes
WHERE category_id = 1 ORDER BY hero_intelligence DESC