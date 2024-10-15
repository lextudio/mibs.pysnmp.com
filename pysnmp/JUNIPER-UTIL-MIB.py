# SNMP MIB module (JUNIPER-UTIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-UTIL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:23 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(jnxUtilMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxUtilMibRoot")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxUtil = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1)
)
jnxUtil.setRevisions(
        ("2007-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxUtilData_ObjectIdentity = ObjectIdentity
jnxUtilData = _JnxUtilData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1)
)
_JnxUtilCounter32Table_Object = MibTable
jnxUtilCounter32Table = _JnxUtilCounter32Table_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxUtilCounter32Table.setStatus("current")
_JnxUtilCounter32Entry_Object = MibTableRow
jnxUtilCounter32Entry = _JnxUtilCounter32Entry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 1, 1)
)
jnxUtilCounter32Entry.setIndexNames(
    (1, "JUNIPER-UTIL-MIB", "jnxUtilCounter32Name"),
)
if mibBuilder.loadTexts:
    jnxUtilCounter32Entry.setStatus("current")


class _JnxUtilCounter32Name_Type(DisplayString):
    """Custom type jnxUtilCounter32Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_JnxUtilCounter32Name_Type.__name__ = "DisplayString"
_JnxUtilCounter32Name_Object = MibTableColumn
jnxUtilCounter32Name = _JnxUtilCounter32Name_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 1, 1, 1),
    _JnxUtilCounter32Name_Type()
)
jnxUtilCounter32Name.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxUtilCounter32Name.setStatus("current")
_JnxUtilCounter32Value_Type = Counter32
_JnxUtilCounter32Value_Object = MibTableColumn
jnxUtilCounter32Value = _JnxUtilCounter32Value_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 1, 1, 2),
    _JnxUtilCounter32Value_Type()
)
jnxUtilCounter32Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUtilCounter32Value.setStatus("current")
_JnxUtilCounter32Time_Type = DateAndTime
_JnxUtilCounter32Time_Object = MibTableColumn
jnxUtilCounter32Time = _JnxUtilCounter32Time_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 1, 1, 3),
    _JnxUtilCounter32Time_Type()
)
jnxUtilCounter32Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUtilCounter32Time.setStatus("current")
_JnxUtilCounter64Table_Object = MibTable
jnxUtilCounter64Table = _JnxUtilCounter64Table_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxUtilCounter64Table.setStatus("current")
_JnxUtilCounter64Entry_Object = MibTableRow
jnxUtilCounter64Entry = _JnxUtilCounter64Entry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 2, 1)
)
jnxUtilCounter64Entry.setIndexNames(
    (1, "JUNIPER-UTIL-MIB", "jnxUtilCounter64Name"),
)
if mibBuilder.loadTexts:
    jnxUtilCounter64Entry.setStatus("current")


class _JnxUtilCounter64Name_Type(DisplayString):
    """Custom type jnxUtilCounter64Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_JnxUtilCounter64Name_Type.__name__ = "DisplayString"
_JnxUtilCounter64Name_Object = MibTableColumn
jnxUtilCounter64Name = _JnxUtilCounter64Name_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 2, 1, 1),
    _JnxUtilCounter64Name_Type()
)
jnxUtilCounter64Name.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxUtilCounter64Name.setStatus("current")
_JnxUtilCounter64Value_Type = Counter64
_JnxUtilCounter64Value_Object = MibTableColumn
jnxUtilCounter64Value = _JnxUtilCounter64Value_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 2, 1, 2),
    _JnxUtilCounter64Value_Type()
)
jnxUtilCounter64Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUtilCounter64Value.setStatus("current")
_JnxUtilCounter64Time_Type = DateAndTime
_JnxUtilCounter64Time_Object = MibTableColumn
jnxUtilCounter64Time = _JnxUtilCounter64Time_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 2, 1, 3),
    _JnxUtilCounter64Time_Type()
)
jnxUtilCounter64Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUtilCounter64Time.setStatus("current")
_JnxUtilIntegerTable_Object = MibTable
jnxUtilIntegerTable = _JnxUtilIntegerTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxUtilIntegerTable.setStatus("current")
_JnxUtilIntegerEntry_Object = MibTableRow
jnxUtilIntegerEntry = _JnxUtilIntegerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 3, 1)
)
jnxUtilIntegerEntry.setIndexNames(
    (1, "JUNIPER-UTIL-MIB", "jnxUtilIntegerName"),
)
if mibBuilder.loadTexts:
    jnxUtilIntegerEntry.setStatus("current")


class _JnxUtilIntegerName_Type(DisplayString):
    """Custom type jnxUtilIntegerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_JnxUtilIntegerName_Type.__name__ = "DisplayString"
_JnxUtilIntegerName_Object = MibTableColumn
jnxUtilIntegerName = _JnxUtilIntegerName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 3, 1, 1),
    _JnxUtilIntegerName_Type()
)
jnxUtilIntegerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxUtilIntegerName.setStatus("current")
_JnxUtilIntegerValue_Type = Integer32
_JnxUtilIntegerValue_Object = MibTableColumn
jnxUtilIntegerValue = _JnxUtilIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 3, 1, 2),
    _JnxUtilIntegerValue_Type()
)
jnxUtilIntegerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUtilIntegerValue.setStatus("current")
_JnxUtilIntegerTime_Type = DateAndTime
_JnxUtilIntegerTime_Object = MibTableColumn
jnxUtilIntegerTime = _JnxUtilIntegerTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 3, 1, 3),
    _JnxUtilIntegerTime_Type()
)
jnxUtilIntegerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUtilIntegerTime.setStatus("current")
_JnxUtilUintTable_Object = MibTable
jnxUtilUintTable = _JnxUtilUintTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxUtilUintTable.setStatus("current")
_JnxUtilUintEntry_Object = MibTableRow
jnxUtilUintEntry = _JnxUtilUintEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 4, 1)
)
jnxUtilUintEntry.setIndexNames(
    (1, "JUNIPER-UTIL-MIB", "jnxUtilUintName"),
)
if mibBuilder.loadTexts:
    jnxUtilUintEntry.setStatus("current")


class _JnxUtilUintName_Type(DisplayString):
    """Custom type jnxUtilUintName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_JnxUtilUintName_Type.__name__ = "DisplayString"
_JnxUtilUintName_Object = MibTableColumn
jnxUtilUintName = _JnxUtilUintName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 4, 1, 1),
    _JnxUtilUintName_Type()
)
jnxUtilUintName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxUtilUintName.setStatus("current")
_JnxUtilUintValue_Type = Unsigned32
_JnxUtilUintValue_Object = MibTableColumn
jnxUtilUintValue = _JnxUtilUintValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 4, 1, 2),
    _JnxUtilUintValue_Type()
)
jnxUtilUintValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUtilUintValue.setStatus("current")
_JnxUtilUintTime_Type = DateAndTime
_JnxUtilUintTime_Object = MibTableColumn
jnxUtilUintTime = _JnxUtilUintTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 4, 1, 3),
    _JnxUtilUintTime_Type()
)
jnxUtilUintTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUtilUintTime.setStatus("current")
_JnxUtilStringTable_Object = MibTable
jnxUtilStringTable = _JnxUtilStringTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 5)
)
if mibBuilder.loadTexts:
    jnxUtilStringTable.setStatus("current")
_JnxUtilStringEntry_Object = MibTableRow
jnxUtilStringEntry = _JnxUtilStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 5, 1)
)
jnxUtilStringEntry.setIndexNames(
    (1, "JUNIPER-UTIL-MIB", "jnxUtilStringName"),
)
if mibBuilder.loadTexts:
    jnxUtilStringEntry.setStatus("current")


class _JnxUtilStringName_Type(DisplayString):
    """Custom type jnxUtilStringName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_JnxUtilStringName_Type.__name__ = "DisplayString"
_JnxUtilStringName_Object = MibTableColumn
jnxUtilStringName = _JnxUtilStringName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 5, 1, 1),
    _JnxUtilStringName_Type()
)
jnxUtilStringName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxUtilStringName.setStatus("current")


class _JnxUtilStringValue_Type(OctetString):
    """Custom type jnxUtilStringValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_JnxUtilStringValue_Type.__name__ = "OctetString"
_JnxUtilStringValue_Object = MibTableColumn
jnxUtilStringValue = _JnxUtilStringValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 5, 1, 2),
    _JnxUtilStringValue_Type()
)
jnxUtilStringValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUtilStringValue.setStatus("current")
_JnxUtilStringTime_Type = DateAndTime
_JnxUtilStringTime_Object = MibTableColumn
jnxUtilStringTime = _JnxUtilStringTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 47, 1, 1, 5, 1, 3),
    _JnxUtilStringTime_Type()
)
jnxUtilStringTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUtilStringTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-UTIL-MIB",
    **{"jnxUtil": jnxUtil,
       "jnxUtilData": jnxUtilData,
       "jnxUtilCounter32Table": jnxUtilCounter32Table,
       "jnxUtilCounter32Entry": jnxUtilCounter32Entry,
       "jnxUtilCounter32Name": jnxUtilCounter32Name,
       "jnxUtilCounter32Value": jnxUtilCounter32Value,
       "jnxUtilCounter32Time": jnxUtilCounter32Time,
       "jnxUtilCounter64Table": jnxUtilCounter64Table,
       "jnxUtilCounter64Entry": jnxUtilCounter64Entry,
       "jnxUtilCounter64Name": jnxUtilCounter64Name,
       "jnxUtilCounter64Value": jnxUtilCounter64Value,
       "jnxUtilCounter64Time": jnxUtilCounter64Time,
       "jnxUtilIntegerTable": jnxUtilIntegerTable,
       "jnxUtilIntegerEntry": jnxUtilIntegerEntry,
       "jnxUtilIntegerName": jnxUtilIntegerName,
       "jnxUtilIntegerValue": jnxUtilIntegerValue,
       "jnxUtilIntegerTime": jnxUtilIntegerTime,
       "jnxUtilUintTable": jnxUtilUintTable,
       "jnxUtilUintEntry": jnxUtilUintEntry,
       "jnxUtilUintName": jnxUtilUintName,
       "jnxUtilUintValue": jnxUtilUintValue,
       "jnxUtilUintTime": jnxUtilUintTime,
       "jnxUtilStringTable": jnxUtilStringTable,
       "jnxUtilStringEntry": jnxUtilStringEntry,
       "jnxUtilStringName": jnxUtilStringName,
       "jnxUtilStringValue": jnxUtilStringValue,
       "jnxUtilStringTime": jnxUtilStringTime}
)
