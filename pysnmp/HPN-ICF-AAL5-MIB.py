# SNMP MIB module (HPN-ICF-AAL5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-AAL5-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:25 2024
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

(hpnicfAAL5,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfAAL5")

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

hpnicfAAL5MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1)
)
hpnicfAAL5MIB.setRevisions(
        ("2004-11-04 13:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfAal5MIBTraps_ObjectIdentity = ObjectIdentity
hpnicfAal5MIBTraps = _HpnicfAal5MIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 0)
)
_HpnicfAal5MIBObjects_ObjectIdentity = ObjectIdentity
hpnicfAal5MIBObjects = _HpnicfAal5MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 1)
)
_HpnicfAal5VccTable_Object = MibTable
hpnicfAal5VccTable = _HpnicfAal5VccTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfAal5VccTable.setStatus("current")
_HpnicfAal5VccEntry_Object = MibTableRow
hpnicfAal5VccEntry = _HpnicfAal5VccEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 1, 1, 1)
)
hpnicfAal5VccEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-AAL5-MIB", "hpnicfAal5VccVpi"),
    (0, "HPN-ICF-AAL5-MIB", "hpnicfAal5VccVci"),
)
if mibBuilder.loadTexts:
    hpnicfAal5VccEntry.setStatus("current")


class _HpnicfAal5VccVpi_Type(Integer32):
    """Custom type hpnicfAal5VccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HpnicfAal5VccVpi_Type.__name__ = "Integer32"
_HpnicfAal5VccVpi_Object = MibTableColumn
hpnicfAal5VccVpi = _HpnicfAal5VccVpi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 1, 1, 1, 1),
    _HpnicfAal5VccVpi_Type()
)
hpnicfAal5VccVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAal5VccVpi.setStatus("current")


class _HpnicfAal5VccVci_Type(Integer32):
    """Custom type hpnicfAal5VccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfAal5VccVci_Type.__name__ = "Integer32"
_HpnicfAal5VccVci_Object = MibTableColumn
hpnicfAal5VccVci = _HpnicfAal5VccVci_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 1, 1, 1, 2),
    _HpnicfAal5VccVci_Type()
)
hpnicfAal5VccVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfAal5VccVci.setStatus("current")
_HpnicfAal5VccInPkts_Type = Counter32
_HpnicfAal5VccInPkts_Object = MibTableColumn
hpnicfAal5VccInPkts = _HpnicfAal5VccInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 1, 1, 1, 3),
    _HpnicfAal5VccInPkts_Type()
)
hpnicfAal5VccInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAal5VccInPkts.setStatus("current")
_HpnicfAal5VccOutPkts_Type = Counter32
_HpnicfAal5VccOutPkts_Object = MibTableColumn
hpnicfAal5VccOutPkts = _HpnicfAal5VccOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 1, 1, 1, 4),
    _HpnicfAal5VccOutPkts_Type()
)
hpnicfAal5VccOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAal5VccOutPkts.setStatus("current")
_HpnicfAal5VccInOctets_Type = Counter32
_HpnicfAal5VccInOctets_Object = MibTableColumn
hpnicfAal5VccInOctets = _HpnicfAal5VccInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 1, 1, 1, 5),
    _HpnicfAal5VccInOctets_Type()
)
hpnicfAal5VccInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAal5VccInOctets.setStatus("current")
_HpnicfAal5VccOutOctets_Type = Counter32
_HpnicfAal5VccOutOctets_Object = MibTableColumn
hpnicfAal5VccOutOctets = _HpnicfAal5VccOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 1, 1, 1, 6),
    _HpnicfAal5VccOutOctets_Type()
)
hpnicfAal5VccOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAal5VccOutOctets.setStatus("current")


class _HpnicfAal5VccState_Type(Integer32):
    """Custom type hpnicfAal5VccState based on Integer32"""
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


_HpnicfAal5VccState_Type.__name__ = "Integer32"
_HpnicfAal5VccState_Object = MibTableColumn
hpnicfAal5VccState = _HpnicfAal5VccState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 1, 1, 1, 7),
    _HpnicfAal5VccState_Type()
)
hpnicfAal5VccState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfAal5VccState.setStatus("current")
_HpnicfAal5MIBConformance_ObjectIdentity = ObjectIdentity
hpnicfAal5MIBConformance = _HpnicfAal5MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 3)
)
_HpnicfAal5MIBCompliances_ObjectIdentity = ObjectIdentity
hpnicfAal5MIBCompliances = _HpnicfAal5MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 3, 1)
)
_HpnicfAal5MIBGroups_ObjectIdentity = ObjectIdentity
hpnicfAal5MIBGroups = _HpnicfAal5MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 3, 2)
)

# Managed Objects groups

hpnicfAal5MIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 3, 2, 1)
)
hpnicfAal5MIBGroup.setObjects(
      *(("HPN-ICF-AAL5-MIB", "hpnicfAal5VccInPkts"),
        ("HPN-ICF-AAL5-MIB", "hpnicfAal5VccOutPkts"),
        ("HPN-ICF-AAL5-MIB", "hpnicfAal5VccInOctets"),
        ("HPN-ICF-AAL5-MIB", "hpnicfAal5VccOutOctets"))
)
if mibBuilder.loadTexts:
    hpnicfAal5MIBGroup.setStatus("current")


# Notification objects

hpnicfAal5VccStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 0, 1)
)
hpnicfAal5VccStateChange.setObjects(
    ("HPN-ICF-AAL5-MIB", "hpnicfAal5VccState")
)
if mibBuilder.loadTexts:
    hpnicfAal5VccStateChange.setStatus(
        "current"
    )


# Notifications groups

hpnicfAal5NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 3, 2, 2)
)
hpnicfAal5NotificationGroup.setObjects(
    ("HPN-ICF-AAL5-MIB", "hpnicfAal5VccStateChange")
)
if mibBuilder.loadTexts:
    hpnicfAal5NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpnicfAal5MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 21, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfAal5MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-AAL5-MIB",
    **{"hpnicfAAL5MIB": hpnicfAAL5MIB,
       "hpnicfAal5MIBTraps": hpnicfAal5MIBTraps,
       "hpnicfAal5VccStateChange": hpnicfAal5VccStateChange,
       "hpnicfAal5MIBObjects": hpnicfAal5MIBObjects,
       "hpnicfAal5VccTable": hpnicfAal5VccTable,
       "hpnicfAal5VccEntry": hpnicfAal5VccEntry,
       "hpnicfAal5VccVpi": hpnicfAal5VccVpi,
       "hpnicfAal5VccVci": hpnicfAal5VccVci,
       "hpnicfAal5VccInPkts": hpnicfAal5VccInPkts,
       "hpnicfAal5VccOutPkts": hpnicfAal5VccOutPkts,
       "hpnicfAal5VccInOctets": hpnicfAal5VccInOctets,
       "hpnicfAal5VccOutOctets": hpnicfAal5VccOutOctets,
       "hpnicfAal5VccState": hpnicfAal5VccState,
       "hpnicfAal5MIBConformance": hpnicfAal5MIBConformance,
       "hpnicfAal5MIBCompliances": hpnicfAal5MIBCompliances,
       "hpnicfAal5MIBCompliance": hpnicfAal5MIBCompliance,
       "hpnicfAal5MIBGroups": hpnicfAal5MIBGroups,
       "hpnicfAal5MIBGroup": hpnicfAal5MIBGroup,
       "hpnicfAal5NotificationGroup": hpnicfAal5NotificationGroup}
)
