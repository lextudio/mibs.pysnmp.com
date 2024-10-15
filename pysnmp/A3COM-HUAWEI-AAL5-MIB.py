# SNMP MIB module (A3COM-HUAWEI-AAL5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-AAL5-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:16 2024
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

(h3cAAL5,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cAAL5")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

h3cAAL5MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1)
)
h3cAAL5MIB.setRevisions(
        ("2004-11-04 13:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cAal5MIBTraps_ObjectIdentity = ObjectIdentity
h3cAal5MIBTraps = _H3cAal5MIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 0)
)
_H3cAal5MIBObjects_ObjectIdentity = ObjectIdentity
h3cAal5MIBObjects = _H3cAal5MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 1)
)
_H3cAal5VccTable_Object = MibTable
h3cAal5VccTable = _H3cAal5VccTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cAal5VccTable.setStatus("current")
_H3cAal5VccEntry_Object = MibTableRow
h3cAal5VccEntry = _H3cAal5VccEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 1, 1, 1)
)
h3cAal5VccEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-AAL5-MIB", "h3cAal5VccVpi"),
    (0, "A3COM-HUAWEI-AAL5-MIB", "h3cAal5VccVci"),
)
if mibBuilder.loadTexts:
    h3cAal5VccEntry.setStatus("current")


class _H3cAal5VccVpi_Type(Integer32):
    """Custom type h3cAal5VccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_H3cAal5VccVpi_Type.__name__ = "Integer32"
_H3cAal5VccVpi_Object = MibTableColumn
h3cAal5VccVpi = _H3cAal5VccVpi_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 1, 1, 1, 1),
    _H3cAal5VccVpi_Type()
)
h3cAal5VccVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAal5VccVpi.setStatus("current")


class _H3cAal5VccVci_Type(Integer32):
    """Custom type h3cAal5VccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cAal5VccVci_Type.__name__ = "Integer32"
_H3cAal5VccVci_Object = MibTableColumn
h3cAal5VccVci = _H3cAal5VccVci_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 1, 1, 1, 2),
    _H3cAal5VccVci_Type()
)
h3cAal5VccVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cAal5VccVci.setStatus("current")
_H3cAal5VccInPkts_Type = Counter32
_H3cAal5VccInPkts_Object = MibTableColumn
h3cAal5VccInPkts = _H3cAal5VccInPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 1, 1, 1, 3),
    _H3cAal5VccInPkts_Type()
)
h3cAal5VccInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAal5VccInPkts.setStatus("current")
_H3cAal5VccOutPkts_Type = Counter32
_H3cAal5VccOutPkts_Object = MibTableColumn
h3cAal5VccOutPkts = _H3cAal5VccOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 1, 1, 1, 4),
    _H3cAal5VccOutPkts_Type()
)
h3cAal5VccOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAal5VccOutPkts.setStatus("current")
_H3cAal5VccInOctets_Type = Counter32
_H3cAal5VccInOctets_Object = MibTableColumn
h3cAal5VccInOctets = _H3cAal5VccInOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 1, 1, 1, 5),
    _H3cAal5VccInOctets_Type()
)
h3cAal5VccInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAal5VccInOctets.setStatus("current")
_H3cAal5VccOutOctets_Type = Counter32
_H3cAal5VccOutOctets_Object = MibTableColumn
h3cAal5VccOutOctets = _H3cAal5VccOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 1, 1, 1, 6),
    _H3cAal5VccOutOctets_Type()
)
h3cAal5VccOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAal5VccOutOctets.setStatus("current")


class _H3cAal5VccState_Type(Integer32):
    """Custom type h3cAal5VccState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("invalid", 1))
    )


_H3cAal5VccState_Type.__name__ = "Integer32"
_H3cAal5VccState_Object = MibTableColumn
h3cAal5VccState = _H3cAal5VccState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 1, 1, 1, 7),
    _H3cAal5VccState_Type()
)
h3cAal5VccState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cAal5VccState.setStatus("current")
_H3cAal5MIBConformance_ObjectIdentity = ObjectIdentity
h3cAal5MIBConformance = _H3cAal5MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 3)
)
_H3cAal5MIBCompliances_ObjectIdentity = ObjectIdentity
h3cAal5MIBCompliances = _H3cAal5MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 3, 1)
)
_H3cAal5MIBGroups_ObjectIdentity = ObjectIdentity
h3cAal5MIBGroups = _H3cAal5MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 3, 2)
)

# Managed Objects groups

h3cAal5MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 3, 2, 1)
)
h3cAal5MIBGroup.setObjects(
      *(("A3COM-HUAWEI-AAL5-MIB", "h3cAal5VccInPkts"),
        ("A3COM-HUAWEI-AAL5-MIB", "h3cAal5VccOutPkts"),
        ("A3COM-HUAWEI-AAL5-MIB", "h3cAal5VccInOctets"),
        ("A3COM-HUAWEI-AAL5-MIB", "h3cAal5VccOutOctets"))
)
if mibBuilder.loadTexts:
    h3cAal5MIBGroup.setStatus("current")


# Notification objects

h3cAal5VccStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 0, 1)
)
h3cAal5VccStateChange.setObjects(
    ("A3COM-HUAWEI-AAL5-MIB", "h3cAal5VccState")
)
if mibBuilder.loadTexts:
    h3cAal5VccStateChange.setStatus(
        "current"
    )


# Notifications groups

h3cAal5NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 3, 2, 2)
)
h3cAal5NotificationGroup.setObjects(
    ("A3COM-HUAWEI-AAL5-MIB", "h3cAal5VccStateChange")
)
if mibBuilder.loadTexts:
    h3cAal5NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h3cAal5MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 21, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h3cAal5MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-AAL5-MIB",
    **{"h3cAAL5MIB": h3cAAL5MIB,
       "h3cAal5MIBTraps": h3cAal5MIBTraps,
       "h3cAal5VccStateChange": h3cAal5VccStateChange,
       "h3cAal5MIBObjects": h3cAal5MIBObjects,
       "h3cAal5VccTable": h3cAal5VccTable,
       "h3cAal5VccEntry": h3cAal5VccEntry,
       "h3cAal5VccVpi": h3cAal5VccVpi,
       "h3cAal5VccVci": h3cAal5VccVci,
       "h3cAal5VccInPkts": h3cAal5VccInPkts,
       "h3cAal5VccOutPkts": h3cAal5VccOutPkts,
       "h3cAal5VccInOctets": h3cAal5VccInOctets,
       "h3cAal5VccOutOctets": h3cAal5VccOutOctets,
       "h3cAal5VccState": h3cAal5VccState,
       "h3cAal5MIBConformance": h3cAal5MIBConformance,
       "h3cAal5MIBCompliances": h3cAal5MIBCompliances,
       "h3cAal5MIBCompliance": h3cAal5MIBCompliance,
       "h3cAal5MIBGroups": h3cAal5MIBGroups,
       "h3cAal5MIBGroup": h3cAal5MIBGroup,
       "h3cAal5NotificationGroup": h3cAal5NotificationGroup}
)
