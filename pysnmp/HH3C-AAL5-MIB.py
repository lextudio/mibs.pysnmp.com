# SNMP MIB module (HH3C-AAL5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-AAL5-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:25 2024
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

(hh3cAAL5,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cAAL5")

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

hh3cAAL5MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1)
)
hh3cAAL5MIB.setRevisions(
        ("2004-11-04 13:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cAal5MIBTraps_ObjectIdentity = ObjectIdentity
hh3cAal5MIBTraps = _Hh3cAal5MIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 0)
)
_Hh3cAal5MIBObjects_ObjectIdentity = ObjectIdentity
hh3cAal5MIBObjects = _Hh3cAal5MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 1)
)
_Hh3cAal5VccTable_Object = MibTable
hh3cAal5VccTable = _Hh3cAal5VccTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cAal5VccTable.setStatus("current")
_Hh3cAal5VccEntry_Object = MibTableRow
hh3cAal5VccEntry = _Hh3cAal5VccEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 1, 1, 1)
)
hh3cAal5VccEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-AAL5-MIB", "hh3cAal5VccVpi"),
    (0, "HH3C-AAL5-MIB", "hh3cAal5VccVci"),
)
if mibBuilder.loadTexts:
    hh3cAal5VccEntry.setStatus("current")


class _Hh3cAal5VccVpi_Type(Integer32):
    """Custom type hh3cAal5VccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Hh3cAal5VccVpi_Type.__name__ = "Integer32"
_Hh3cAal5VccVpi_Object = MibTableColumn
hh3cAal5VccVpi = _Hh3cAal5VccVpi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 1, 1, 1, 1),
    _Hh3cAal5VccVpi_Type()
)
hh3cAal5VccVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAal5VccVpi.setStatus("current")


class _Hh3cAal5VccVci_Type(Integer32):
    """Custom type hh3cAal5VccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAal5VccVci_Type.__name__ = "Integer32"
_Hh3cAal5VccVci_Object = MibTableColumn
hh3cAal5VccVci = _Hh3cAal5VccVci_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 1, 1, 1, 2),
    _Hh3cAal5VccVci_Type()
)
hh3cAal5VccVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAal5VccVci.setStatus("current")
_Hh3cAal5VccInPkts_Type = Counter32
_Hh3cAal5VccInPkts_Object = MibTableColumn
hh3cAal5VccInPkts = _Hh3cAal5VccInPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 1, 1, 1, 3),
    _Hh3cAal5VccInPkts_Type()
)
hh3cAal5VccInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAal5VccInPkts.setStatus("current")
_Hh3cAal5VccOutPkts_Type = Counter32
_Hh3cAal5VccOutPkts_Object = MibTableColumn
hh3cAal5VccOutPkts = _Hh3cAal5VccOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 1, 1, 1, 4),
    _Hh3cAal5VccOutPkts_Type()
)
hh3cAal5VccOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAal5VccOutPkts.setStatus("current")
_Hh3cAal5VccInOctets_Type = Counter32
_Hh3cAal5VccInOctets_Object = MibTableColumn
hh3cAal5VccInOctets = _Hh3cAal5VccInOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 1, 1, 1, 5),
    _Hh3cAal5VccInOctets_Type()
)
hh3cAal5VccInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAal5VccInOctets.setStatus("current")
_Hh3cAal5VccOutOctets_Type = Counter32
_Hh3cAal5VccOutOctets_Object = MibTableColumn
hh3cAal5VccOutOctets = _Hh3cAal5VccOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 1, 1, 1, 6),
    _Hh3cAal5VccOutOctets_Type()
)
hh3cAal5VccOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAal5VccOutOctets.setStatus("current")


class _Hh3cAal5VccState_Type(Integer32):
    """Custom type hh3cAal5VccState based on Integer32"""
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


_Hh3cAal5VccState_Type.__name__ = "Integer32"
_Hh3cAal5VccState_Object = MibTableColumn
hh3cAal5VccState = _Hh3cAal5VccState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 1, 1, 1, 7),
    _Hh3cAal5VccState_Type()
)
hh3cAal5VccState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAal5VccState.setStatus("current")
_Hh3cAal5MIBConformance_ObjectIdentity = ObjectIdentity
hh3cAal5MIBConformance = _Hh3cAal5MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 3)
)
_Hh3cAal5MIBCompliances_ObjectIdentity = ObjectIdentity
hh3cAal5MIBCompliances = _Hh3cAal5MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 3, 1)
)
_Hh3cAal5MIBGroups_ObjectIdentity = ObjectIdentity
hh3cAal5MIBGroups = _Hh3cAal5MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 3, 2)
)

# Managed Objects groups

hh3cAal5MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 3, 2, 1)
)
hh3cAal5MIBGroup.setObjects(
      *(("HH3C-AAL5-MIB", "hh3cAal5VccInPkts"),
        ("HH3C-AAL5-MIB", "hh3cAal5VccOutPkts"),
        ("HH3C-AAL5-MIB", "hh3cAal5VccInOctets"),
        ("HH3C-AAL5-MIB", "hh3cAal5VccOutOctets"))
)
if mibBuilder.loadTexts:
    hh3cAal5MIBGroup.setStatus("current")


# Notification objects

hh3cAal5VccStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 0, 1)
)
hh3cAal5VccStateChange.setObjects(
    ("HH3C-AAL5-MIB", "hh3cAal5VccState")
)
if mibBuilder.loadTexts:
    hh3cAal5VccStateChange.setStatus(
        "current"
    )


# Notifications groups

hh3cAal5NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 3, 2, 2)
)
hh3cAal5NotificationGroup.setObjects(
    ("HH3C-AAL5-MIB", "hh3cAal5VccStateChange")
)
if mibBuilder.loadTexts:
    hh3cAal5NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hh3cAal5MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 21, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cAal5MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-AAL5-MIB",
    **{"hh3cAAL5MIB": hh3cAAL5MIB,
       "hh3cAal5MIBTraps": hh3cAal5MIBTraps,
       "hh3cAal5VccStateChange": hh3cAal5VccStateChange,
       "hh3cAal5MIBObjects": hh3cAal5MIBObjects,
       "hh3cAal5VccTable": hh3cAal5VccTable,
       "hh3cAal5VccEntry": hh3cAal5VccEntry,
       "hh3cAal5VccVpi": hh3cAal5VccVpi,
       "hh3cAal5VccVci": hh3cAal5VccVci,
       "hh3cAal5VccInPkts": hh3cAal5VccInPkts,
       "hh3cAal5VccOutPkts": hh3cAal5VccOutPkts,
       "hh3cAal5VccInOctets": hh3cAal5VccInOctets,
       "hh3cAal5VccOutOctets": hh3cAal5VccOutOctets,
       "hh3cAal5VccState": hh3cAal5VccState,
       "hh3cAal5MIBConformance": hh3cAal5MIBConformance,
       "hh3cAal5MIBCompliances": hh3cAal5MIBCompliances,
       "hh3cAal5MIBCompliance": hh3cAal5MIBCompliance,
       "hh3cAal5MIBGroups": hh3cAal5MIBGroups,
       "hh3cAal5MIBGroup": hh3cAal5MIBGroup,
       "hh3cAal5NotificationGroup": hh3cAal5NotificationGroup}
)
