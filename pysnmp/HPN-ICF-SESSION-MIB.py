# SNMP MIB module (HPN-ICF-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-SESSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:47 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfSession = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149)
)
hpnicfSession.setRevisions(
        ("2013-12-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfSessionTables_ObjectIdentity = ObjectIdentity
hpnicfSessionTables = _HpnicfSessionTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1)
)
_HpnicfSessionStatTable_Object = MibTable
hpnicfSessionStatTable = _HpnicfSessionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfSessionStatTable.setStatus("current")
_HpnicfSessionStatEntry_Object = MibTableRow
hpnicfSessionStatEntry = _HpnicfSessionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1)
)
hpnicfSessionStatEntry.setIndexNames(
    (0, "HPN-ICF-SESSION-MIB", "hpnicfSessionStatChassis"),
    (0, "HPN-ICF-SESSION-MIB", "hpnicfSessionStatSlot"),
    (0, "HPN-ICF-SESSION-MIB", "hpnicfSessionStatCPUID"),
)
if mibBuilder.loadTexts:
    hpnicfSessionStatEntry.setStatus("current")


class _HpnicfSessionStatChassis_Type(Unsigned32):
    """Custom type hpnicfSessionStatChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HpnicfSessionStatChassis_Type.__name__ = "Unsigned32"
_HpnicfSessionStatChassis_Object = MibTableColumn
hpnicfSessionStatChassis = _HpnicfSessionStatChassis_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1, 1),
    _HpnicfSessionStatChassis_Type()
)
hpnicfSessionStatChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSessionStatChassis.setStatus("current")


class _HpnicfSessionStatSlot_Type(Unsigned32):
    """Custom type hpnicfSessionStatSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HpnicfSessionStatSlot_Type.__name__ = "Unsigned32"
_HpnicfSessionStatSlot_Object = MibTableColumn
hpnicfSessionStatSlot = _HpnicfSessionStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1, 2),
    _HpnicfSessionStatSlot_Type()
)
hpnicfSessionStatSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSessionStatSlot.setStatus("current")


class _HpnicfSessionStatCPUID_Type(Unsigned32):
    """Custom type hpnicfSessionStatCPUID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfSessionStatCPUID_Type.__name__ = "Unsigned32"
_HpnicfSessionStatCPUID_Object = MibTableColumn
hpnicfSessionStatCPUID = _HpnicfSessionStatCPUID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1, 3),
    _HpnicfSessionStatCPUID_Type()
)
hpnicfSessionStatCPUID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSessionStatCPUID.setStatus("current")
_HpnicfSessionStatCount_Type = Unsigned32
_HpnicfSessionStatCount_Object = MibTableColumn
hpnicfSessionStatCount = _HpnicfSessionStatCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1, 4),
    _HpnicfSessionStatCount_Type()
)
hpnicfSessionStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSessionStatCount.setStatus("current")
_HpnicfSessionStatCreateRate_Type = Unsigned32
_HpnicfSessionStatCreateRate_Object = MibTableColumn
hpnicfSessionStatCreateRate = _HpnicfSessionStatCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 149, 1, 1, 1, 5),
    _HpnicfSessionStatCreateRate_Type()
)
hpnicfSessionStatCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSessionStatCreateRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-SESSION-MIB",
    **{"hpnicfSession": hpnicfSession,
       "hpnicfSessionTables": hpnicfSessionTables,
       "hpnicfSessionStatTable": hpnicfSessionStatTable,
       "hpnicfSessionStatEntry": hpnicfSessionStatEntry,
       "hpnicfSessionStatChassis": hpnicfSessionStatChassis,
       "hpnicfSessionStatSlot": hpnicfSessionStatSlot,
       "hpnicfSessionStatCPUID": hpnicfSessionStatCPUID,
       "hpnicfSessionStatCount": hpnicfSessionStatCount,
       "hpnicfSessionStatCreateRate": hpnicfSessionStatCreateRate}
)
