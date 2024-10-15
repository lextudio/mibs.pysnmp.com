# SNMP MIB module (JUNIPER-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-BFD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:50 2024
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

(bfdSessIndex,) = mibBuilder.importSymbols(
    "BFD-STD-MIB",
    "bfdSessIndex")

(jnxBfdMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxBfdMibRoot")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

jnxBfdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1)
)
jnxBfdMib.setRevisions(
        ("2006-10-12 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxBfdNotification_ObjectIdentity = ObjectIdentity
jnxBfdNotification = _JnxBfdNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 0)
)
_JnxBfdObjects_ObjectIdentity = ObjectIdentity
jnxBfdObjects = _JnxBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 1)
)
_JnxBfdSessTable_Object = MibTable
jnxBfdSessTable = _JnxBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxBfdSessTable.setStatus("current")
_JnxBfdSessEntry_Object = MibTableRow
jnxBfdSessEntry = _JnxBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 1, 1, 1)
)
jnxBfdSessEntry.setIndexNames(
    (0, "BFD-STD-MIB", "bfdSessIndex"),
)
if mibBuilder.loadTexts:
    jnxBfdSessEntry.setStatus("current")
_JnxBfdSessThreshTxInterval_Type = Unsigned32
_JnxBfdSessThreshTxInterval_Object = MibTableColumn
jnxBfdSessThreshTxInterval = _JnxBfdSessThreshTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 1, 1, 1, 1),
    _JnxBfdSessThreshTxInterval_Type()
)
jnxBfdSessThreshTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBfdSessThreshTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    jnxBfdSessThreshTxInterval.setUnits("microseconds")
_JnxBfdSessCurrTxInterval_Type = Unsigned32
_JnxBfdSessCurrTxInterval_Object = MibTableColumn
jnxBfdSessCurrTxInterval = _JnxBfdSessCurrTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 1, 1, 1, 2),
    _JnxBfdSessCurrTxInterval_Type()
)
jnxBfdSessCurrTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBfdSessCurrTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    jnxBfdSessCurrTxInterval.setUnits("microseconds")
_JnxBfdSessThreshDectTime_Type = Unsigned32
_JnxBfdSessThreshDectTime_Object = MibTableColumn
jnxBfdSessThreshDectTime = _JnxBfdSessThreshDectTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 1, 1, 1, 3),
    _JnxBfdSessThreshDectTime_Type()
)
jnxBfdSessThreshDectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBfdSessThreshDectTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxBfdSessThreshDectTime.setUnits("microseconds")
_JnxBfdSessCurrDectTime_Type = Unsigned32
_JnxBfdSessCurrDectTime_Object = MibTableColumn
jnxBfdSessCurrDectTime = _JnxBfdSessCurrDectTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 1, 1, 1, 4),
    _JnxBfdSessCurrDectTime_Type()
)
jnxBfdSessCurrDectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBfdSessCurrDectTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxBfdSessCurrDectTime.setUnits("microseconds")
_JnxBfdSessIntfName_Type = DisplayString
_JnxBfdSessIntfName_Object = MibTableColumn
jnxBfdSessIntfName = _JnxBfdSessIntfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 1, 1, 1, 5),
    _JnxBfdSessIntfName_Type()
)
jnxBfdSessIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBfdSessIntfName.setStatus("current")
_JnxBfdNotifyObjects_ObjectIdentity = ObjectIdentity
jnxBfdNotifyObjects = _JnxBfdNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 2)
)
_JnxBfdSessifName_Type = DisplayString
_JnxBfdSessifName_Object = MibScalar
jnxBfdSessifName = _JnxBfdSessifName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 2, 1),
    _JnxBfdSessifName_Type()
)
jnxBfdSessifName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxBfdSessifName.setStatus("current")

# Managed Objects groups


# Notification objects

jnxBfdSessTxIntervalHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 0, 1)
)
jnxBfdSessTxIntervalHigh.setObjects(
      *(("JUNIPER-BFD-MIB", "jnxBfdSessThreshTxInterval"),
        ("JUNIPER-BFD-MIB", "jnxBfdSessCurrTxInterval"))
)
if mibBuilder.loadTexts:
    jnxBfdSessTxIntervalHigh.setStatus(
        "current"
    )

jnxBfdSessDetectionTimeHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 45, 1, 0, 2)
)
jnxBfdSessDetectionTimeHigh.setObjects(
      *(("JUNIPER-BFD-MIB", "jnxBfdSessThreshDectTime"),
        ("JUNIPER-BFD-MIB", "jnxBfdSessCurrDectTime"))
)
if mibBuilder.loadTexts:
    jnxBfdSessDetectionTimeHigh.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-BFD-MIB",
    **{"jnxBfdMib": jnxBfdMib,
       "jnxBfdNotification": jnxBfdNotification,
       "jnxBfdSessTxIntervalHigh": jnxBfdSessTxIntervalHigh,
       "jnxBfdSessDetectionTimeHigh": jnxBfdSessDetectionTimeHigh,
       "jnxBfdObjects": jnxBfdObjects,
       "jnxBfdSessTable": jnxBfdSessTable,
       "jnxBfdSessEntry": jnxBfdSessEntry,
       "jnxBfdSessThreshTxInterval": jnxBfdSessThreshTxInterval,
       "jnxBfdSessCurrTxInterval": jnxBfdSessCurrTxInterval,
       "jnxBfdSessThreshDectTime": jnxBfdSessThreshDectTime,
       "jnxBfdSessCurrDectTime": jnxBfdSessCurrDectTime,
       "jnxBfdSessIntfName": jnxBfdSessIntfName,
       "jnxBfdNotifyObjects": jnxBfdNotifyObjects,
       "jnxBfdSessifName": jnxBfdSessifName}
)
