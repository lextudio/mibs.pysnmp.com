# SNMP MIB module (BETTER-NETWORKS-ETHERNETBOX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BETTER-NETWORKS-ETHERNETBOX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:06 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Betternetworks_ObjectIdentity = ObjectIdentity
betternetworks = _Betternetworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14848)
)
_Ethernetbox_ObjectIdentity = ObjectIdentity
ethernetbox = _Ethernetbox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14848, 2)
)
_EthernetboxObjects_ObjectIdentity = ObjectIdentity
ethernetboxObjects = _EthernetboxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1)
)
_Misc_ObjectIdentity = ObjectIdentity
misc = _Misc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 1)
)
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 1, 1),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("mandatory")
_Location_Type = DisplayString
_Location_Object = MibScalar
location = _Location_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 1, 2),
    _Location_Type()
)
location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    location.setStatus("mandatory")


class _Tempunit_Type(Integer32):
    """Custom type tempunit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Tempunit_Type.__name__ = "Integer32"
_Tempunit_Object = MibScalar
tempunit = _Tempunit_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 1, 3),
    _Tempunit_Type()
)
tempunit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempunit.setStatus("mandatory")


class _Refreshinterval_Type(Integer32):
    """Custom type refreshinterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Refreshinterval_Type.__name__ = "Integer32"
_Refreshinterval_Object = MibScalar
refreshinterval = _Refreshinterval_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 1, 4),
    _Refreshinterval_Type()
)
refreshinterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    refreshinterval.setStatus("mandatory")


class _Numbersensors_Type(Integer32):
    """Custom type numbersensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Numbersensors_Type.__name__ = "Integer32"
_Numbersensors_Object = MibScalar
numbersensors = _Numbersensors_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 1, 5),
    _Numbersensors_Type()
)
numbersensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numbersensors.setStatus("mandatory")
_Address_Type = IpAddress
_Address_Object = MibScalar
address = _Address_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 1, 6),
    _Address_Type()
)
address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    address.setStatus("mandatory")
_Uptime_Type = TimeTicks
_Uptime_Object = MibScalar
uptime = _Uptime_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 1, 7),
    _Uptime_Type()
)
uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uptime.setStatus("mandatory")
_SensorTable_Object = MibTable
sensorTable = _SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 2)
)
if mibBuilder.loadTexts:
    sensorTable.setStatus("mandatory")
_SensorEntry_Object = MibTableRow
sensorEntry = _SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 2, 1)
)
sensorEntry.setIndexNames(
    (0, "BETTER-NETWORKS-ETHERNETBOX-MIB", "sensorindex"),
)
if mibBuilder.loadTexts:
    sensorEntry.setStatus("mandatory")
_Sensorindex_Type = Integer32
_Sensorindex_Object = MibTableColumn
sensorindex = _Sensorindex_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 2, 1, 1),
    _Sensorindex_Type()
)
sensorindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorindex.setStatus("mandatory")
_Name_Type = DisplayString
_Name_Object = MibTableColumn
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 2, 1, 2),
    _Name_Type()
)
name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    name.setStatus("mandatory")
_Sensortype_Type = Integer32
_Sensortype_Object = MibTableColumn
sensortype = _Sensortype_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 2, 1, 3),
    _Sensortype_Type()
)
sensortype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensortype.setStatus("mandatory")
_Valueint_Type = Integer32
_Valueint_Object = MibTableColumn
valueint = _Valueint_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 2, 1, 4),
    _Valueint_Type()
)
valueint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueint.setStatus("mandatory")
_Valueint10_Type = Integer32
_Valueint10_Object = MibTableColumn
valueint10 = _Valueint10_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 2, 1, 5),
    _Valueint10_Type()
)
valueint10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valueint10.setStatus("mandatory")
_Valuestr_Type = DisplayString
_Valuestr_Object = MibTableColumn
valuestr = _Valuestr_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 2, 1, 6),
    _Valuestr_Type()
)
valuestr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valuestr.setStatus("mandatory")
_Valid_Type = Integer32
_Valid_Object = MibTableColumn
valid = _Valid_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 2, 1, 7),
    _Valid_Type()
)
valid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valid.setStatus("mandatory")
_Lowlimit_Type = Integer32
_Lowlimit_Object = MibTableColumn
lowlimit = _Lowlimit_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 2, 1, 8),
    _Lowlimit_Type()
)
lowlimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowlimit.setStatus("mandatory")
_Highlimit_Type = Integer32
_Highlimit_Object = MibTableColumn
highlimit = _Highlimit_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 2, 1, 9),
    _Highlimit_Type()
)
highlimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highlimit.setStatus("mandatory")
_Hysteresis_Type = Integer32
_Hysteresis_Object = MibTableColumn
hysteresis = _Hysteresis_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 2, 1, 10),
    _Hysteresis_Type()
)
hysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hysteresis.setStatus("mandatory")
_Status_Type = Integer32
_Status_Object = MibTableColumn
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 2, 1, 11),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("mandatory")
_InputTable_Object = MibTable
inputTable = _InputTable_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 3)
)
if mibBuilder.loadTexts:
    inputTable.setStatus("mandatory")
_InputEntry_Object = MibTableRow
inputEntry = _InputEntry_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 3, 1)
)
inputEntry.setIndexNames(
    (0, "BETTER-NETWORKS-ETHERNETBOX-MIB", "inputindex"),
)
if mibBuilder.loadTexts:
    inputEntry.setStatus("mandatory")
_Inputindex_Type = Integer32
_Inputindex_Object = MibTableColumn
inputindex = _Inputindex_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 3, 1, 1),
    _Inputindex_Type()
)
inputindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputindex.setStatus("mandatory")
_Inputstatus_Type = Integer32
_Inputstatus_Object = MibTableColumn
inputstatus = _Inputstatus_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 3, 1, 2),
    _Inputstatus_Type()
)
inputstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputstatus.setStatus("mandatory")
_OutputTable_Object = MibTable
outputTable = _OutputTable_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 4)
)
if mibBuilder.loadTexts:
    outputTable.setStatus("mandatory")
_OutputEntry_Object = MibTableRow
outputEntry = _OutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 4, 1)
)
outputEntry.setIndexNames(
    (0, "BETTER-NETWORKS-ETHERNETBOX-MIB", "outputindex"),
)
if mibBuilder.loadTexts:
    outputEntry.setStatus("mandatory")
_Outputindex_Type = Integer32
_Outputindex_Object = MibTableColumn
outputindex = _Outputindex_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 4, 1, 1),
    _Outputindex_Type()
)
outputindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputindex.setStatus("mandatory")
_Outputstatus_Type = Integer32
_Outputstatus_Object = MibTableColumn
outputstatus = _Outputstatus_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 4, 1, 2),
    _Outputstatus_Type()
)
outputstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputstatus.setStatus("mandatory")
_AnalogTable_Object = MibTable
analogTable = _AnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 5)
)
if mibBuilder.loadTexts:
    analogTable.setStatus("mandatory")
_AnalogEntry_Object = MibTableRow
analogEntry = _AnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 5, 1)
)
analogEntry.setIndexNames(
    (0, "BETTER-NETWORKS-ETHERNETBOX-MIB", "analogindex"),
)
if mibBuilder.loadTexts:
    analogEntry.setStatus("mandatory")
_Analogindex_Type = Integer32
_Analogindex_Object = MibTableColumn
analogindex = _Analogindex_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 5, 1, 1),
    _Analogindex_Type()
)
analogindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogindex.setStatus("mandatory")
_Analogname_Type = DisplayString
_Analogname_Object = MibTableColumn
analogname = _Analogname_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 5, 1, 2),
    _Analogname_Type()
)
analogname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analogname.setStatus("mandatory")
_Analogvalueint_Type = Integer32
_Analogvalueint_Object = MibTableColumn
analogvalueint = _Analogvalueint_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 5, 1, 3),
    _Analogvalueint_Type()
)
analogvalueint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogvalueint.setStatus("mandatory")
_Analogvalueint10_Type = Integer32
_Analogvalueint10_Object = MibTableColumn
analogvalueint10 = _Analogvalueint10_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 5, 1, 4),
    _Analogvalueint10_Type()
)
analogvalueint10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogvalueint10.setStatus("mandatory")
_Analogvaluestr_Type = DisplayString
_Analogvaluestr_Object = MibTableColumn
analogvaluestr = _Analogvaluestr_Object(
    (1, 3, 6, 1, 4, 1, 14848, 2, 1, 5, 1, 5),
    _Analogvaluestr_Type()
)
analogvaluestr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analogvaluestr.setStatus("mandatory")

# Managed Objects groups


# Notification objects

sensorstatusChangeToLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 14848, 0, 1)
)
if mibBuilder.loadTexts:
    sensorstatusChangeToLow.setStatus(
        ""
    )

sensorstatusChangeToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 14848, 0, 2)
)
if mibBuilder.loadTexts:
    sensorstatusChangeToNormal.setStatus(
        ""
    )

sensorstatusChangeToHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 14848, 0, 3)
)
if mibBuilder.loadTexts:
    sensorstatusChangeToHigh.setStatus(
        ""
    )

inputlineChangeToLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 14848, 0, 4)
)
if mibBuilder.loadTexts:
    inputlineChangeToLow.setStatus(
        ""
    )

inputlineChangeToHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 14848, 0, 5)
)
if mibBuilder.loadTexts:
    inputlineChangeToHigh.setStatus(
        ""
    )

ethernetboxPowerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14848, 0, 100)
)
if mibBuilder.loadTexts:
    ethernetboxPowerUp.setStatus(
        ""
    )

ethernetboxConfigSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14848, 0, 101)
)
if mibBuilder.loadTexts:
    ethernetboxConfigSaved.setStatus(
        ""
    )

ethernetboxNotificationInputLineChangeToLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 14848, 4)
)
ethernetboxNotificationInputLineChangeToLow.setObjects(
      *(("BETTER-NETWORKS-ETHERNETBOX-MIB", "uptime"),
        ("BETTER-NETWORKS-ETHERNETBOX-MIB", "location"),
        ("BETTER-NETWORKS-ETHERNETBOX-MIB", "address"),
        ("BETTER-NETWORKS-ETHERNETBOX-MIB", "inputindex"),
        ("BETTER-NETWORKS-ETHERNETBOX-MIB", "name"),
        ("BETTER-NETWORKS-ETHERNETBOX-MIB", "sensortype"),
        ("BETTER-NETWORKS-ETHERNETBOX-MIB", "inputstatus"))
)
if mibBuilder.loadTexts:
    ethernetboxNotificationInputLineChangeToLow.setStatus(
        "current"
    )

ethernetboxNotificationInputLineChangeToHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 14848, 5)
)
ethernetboxNotificationInputLineChangeToHigh.setObjects(
      *(("BETTER-NETWORKS-ETHERNETBOX-MIB", "uptime"),
        ("BETTER-NETWORKS-ETHERNETBOX-MIB", "location"),
        ("BETTER-NETWORKS-ETHERNETBOX-MIB", "address"),
        ("BETTER-NETWORKS-ETHERNETBOX-MIB", "inputindex"),
        ("BETTER-NETWORKS-ETHERNETBOX-MIB", "name"),
        ("BETTER-NETWORKS-ETHERNETBOX-MIB", "sensortype"),
        ("BETTER-NETWORKS-ETHERNETBOX-MIB", "inputstatus"))
)
if mibBuilder.loadTexts:
    ethernetboxNotificationInputLineChangeToHigh.setStatus(
        "current"
    )

ethernetboxNotificationPowerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 14848, 100)
)
ethernetboxNotificationPowerUp.setObjects(
      *(("BETTER-NETWORKS-ETHERNETBOX-MIB", "uptime"),
        ("BETTER-NETWORKS-ETHERNETBOX-MIB", "location"),
        ("BETTER-NETWORKS-ETHERNETBOX-MIB", "address"))
)
if mibBuilder.loadTexts:
    ethernetboxNotificationPowerUp.setStatus(
        "current"
    )

ethernetboxNotificationConfigSaved = NotificationType(
    (1, 3, 6, 1, 4, 1, 14848, 101)
)
ethernetboxNotificationConfigSaved.setObjects(
      *(("BETTER-NETWORKS-ETHERNETBOX-MIB", "uptime"),
        ("BETTER-NETWORKS-ETHERNETBOX-MIB", "location"),
        ("BETTER-NETWORKS-ETHERNETBOX-MIB", "address"))
)
if mibBuilder.loadTexts:
    ethernetboxNotificationConfigSaved.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BETTER-NETWORKS-ETHERNETBOX-MIB",
    **{"DisplayString": DisplayString,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "betternetworks": betternetworks,
       "sensorstatusChangeToLow": sensorstatusChangeToLow,
       "sensorstatusChangeToNormal": sensorstatusChangeToNormal,
       "sensorstatusChangeToHigh": sensorstatusChangeToHigh,
       "inputlineChangeToLow": inputlineChangeToLow,
       "inputlineChangeToHigh": inputlineChangeToHigh,
       "ethernetboxPowerUp": ethernetboxPowerUp,
       "ethernetboxConfigSaved": ethernetboxConfigSaved,
       "ethernetbox": ethernetbox,
       "ethernetboxObjects": ethernetboxObjects,
       "misc": misc,
       "version": version,
       "location": location,
       "tempunit": tempunit,
       "refreshinterval": refreshinterval,
       "numbersensors": numbersensors,
       "address": address,
       "uptime": uptime,
       "sensorTable": sensorTable,
       "sensorEntry": sensorEntry,
       "sensorindex": sensorindex,
       "name": name,
       "sensortype": sensortype,
       "valueint": valueint,
       "valueint10": valueint10,
       "valuestr": valuestr,
       "valid": valid,
       "lowlimit": lowlimit,
       "highlimit": highlimit,
       "hysteresis": hysteresis,
       "status": status,
       "inputTable": inputTable,
       "inputEntry": inputEntry,
       "inputindex": inputindex,
       "inputstatus": inputstatus,
       "outputTable": outputTable,
       "outputEntry": outputEntry,
       "outputindex": outputindex,
       "outputstatus": outputstatus,
       "analogTable": analogTable,
       "analogEntry": analogEntry,
       "analogindex": analogindex,
       "analogname": analogname,
       "analogvalueint": analogvalueint,
       "analogvalueint10": analogvalueint10,
       "analogvaluestr": analogvaluestr,
       "ethernetboxNotificationInputLineChangeToLow": ethernetboxNotificationInputLineChangeToLow,
       "ethernetboxNotificationInputLineChangeToHigh": ethernetboxNotificationInputLineChangeToHigh,
       "ethernetboxNotificationPowerUp": ethernetboxNotificationPowerUp,
       "ethernetboxNotificationConfigSaved": ethernetboxNotificationConfigSaved}
)
