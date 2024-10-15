# SNMP MIB module (HPN-ICF-OBJP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-OBJP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:24 2024
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

hpnicfObjp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155)
)
hpnicfObjp.setRevisions(
        ("2014-03-10 15:36",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfObjpZonePairObjects_ObjectIdentity = ObjectIdentity
hpnicfObjpZonePairObjects = _HpnicfObjpZonePairObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1)
)
_HpnicfObjpZonePairRunningInfoTable_Object = MibTable
hpnicfObjpZonePairRunningInfoTable = _HpnicfObjpZonePairRunningInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfObjpZonePairRunningInfoTable.setStatus("current")
_HpnicfObjpZonePairRunningInfoEntry_Object = MibTableRow
hpnicfObjpZonePairRunningInfoEntry = _HpnicfObjpZonePairRunningInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1, 1, 1)
)
hpnicfObjpZonePairRunningInfoEntry.setIndexNames(
    (0, "HPN-ICF-OBJP-MIB", "hpnicfObjpZonePairSrcZone"),
    (0, "HPN-ICF-OBJP-MIB", "hpnicfObjpZonePairDstZone"),
    (0, "HPN-ICF-OBJP-MIB", "hpnicfObjpZonePairIPVersion"),
    (0, "HPN-ICF-OBJP-MIB", "hpnicfObjpZonePairRuleID"),
)
if mibBuilder.loadTexts:
    hpnicfObjpZonePairRunningInfoEntry.setStatus("current")


class _HpnicfObjpZonePairSrcZone_Type(OctetString):
    """Custom type hpnicfObjpZonePairSrcZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfObjpZonePairSrcZone_Type.__name__ = "OctetString"
_HpnicfObjpZonePairSrcZone_Object = MibTableColumn
hpnicfObjpZonePairSrcZone = _HpnicfObjpZonePairSrcZone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1, 1, 1, 1),
    _HpnicfObjpZonePairSrcZone_Type()
)
hpnicfObjpZonePairSrcZone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfObjpZonePairSrcZone.setStatus("current")


class _HpnicfObjpZonePairDstZone_Type(OctetString):
    """Custom type hpnicfObjpZonePairDstZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfObjpZonePairDstZone_Type.__name__ = "OctetString"
_HpnicfObjpZonePairDstZone_Object = MibTableColumn
hpnicfObjpZonePairDstZone = _HpnicfObjpZonePairDstZone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1, 1, 1, 2),
    _HpnicfObjpZonePairDstZone_Type()
)
hpnicfObjpZonePairDstZone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfObjpZonePairDstZone.setStatus("current")


class _HpnicfObjpZonePairIPVersion_Type(Integer32):
    """Custom type hpnicfObjpZonePairIPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_HpnicfObjpZonePairIPVersion_Type.__name__ = "Integer32"
_HpnicfObjpZonePairIPVersion_Object = MibTableColumn
hpnicfObjpZonePairIPVersion = _HpnicfObjpZonePairIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1, 1, 1, 3),
    _HpnicfObjpZonePairIPVersion_Type()
)
hpnicfObjpZonePairIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfObjpZonePairIPVersion.setStatus("current")


class _HpnicfObjpZonePairRuleID_Type(Unsigned32):
    """Custom type hpnicfObjpZonePairRuleID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HpnicfObjpZonePairRuleID_Type.__name__ = "Unsigned32"
_HpnicfObjpZonePairRuleID_Object = MibTableColumn
hpnicfObjpZonePairRuleID = _HpnicfObjpZonePairRuleID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1, 1, 1, 4),
    _HpnicfObjpZonePairRuleID_Type()
)
hpnicfObjpZonePairRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfObjpZonePairRuleID.setStatus("current")
_HpnicfObjpZonePairMatchPacketCount_Type = Counter64
_HpnicfObjpZonePairMatchPacketCount_Object = MibTableColumn
hpnicfObjpZonePairMatchPacketCount = _HpnicfObjpZonePairMatchPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1, 1, 1, 5),
    _HpnicfObjpZonePairMatchPacketCount_Type()
)
hpnicfObjpZonePairMatchPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfObjpZonePairMatchPacketCount.setStatus("current")
_HpnicfObjpZonePairLastMatchTime_Type = Unsigned32
_HpnicfObjpZonePairLastMatchTime_Object = MibTableColumn
hpnicfObjpZonePairLastMatchTime = _HpnicfObjpZonePairLastMatchTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 155, 1, 1, 1, 6),
    _HpnicfObjpZonePairLastMatchTime_Type()
)
hpnicfObjpZonePairLastMatchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfObjpZonePairLastMatchTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-OBJP-MIB",
    **{"hpnicfObjp": hpnicfObjp,
       "hpnicfObjpZonePairObjects": hpnicfObjpZonePairObjects,
       "hpnicfObjpZonePairRunningInfoTable": hpnicfObjpZonePairRunningInfoTable,
       "hpnicfObjpZonePairRunningInfoEntry": hpnicfObjpZonePairRunningInfoEntry,
       "hpnicfObjpZonePairSrcZone": hpnicfObjpZonePairSrcZone,
       "hpnicfObjpZonePairDstZone": hpnicfObjpZonePairDstZone,
       "hpnicfObjpZonePairIPVersion": hpnicfObjpZonePairIPVersion,
       "hpnicfObjpZonePairRuleID": hpnicfObjpZonePairRuleID,
       "hpnicfObjpZonePairMatchPacketCount": hpnicfObjpZonePairMatchPacketCount,
       "hpnicfObjpZonePairLastMatchTime": hpnicfObjpZonePairLastMatchTime}
)
