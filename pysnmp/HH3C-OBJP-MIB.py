# SNMP MIB module (HH3C-OBJP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-OBJP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:25 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cObjp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 155)
)
hh3cObjp.setRevisions(
        ("2014-03-10 15:36",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cObjpZonePairObjects_ObjectIdentity = ObjectIdentity
hh3cObjpZonePairObjects = _Hh3cObjpZonePairObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 155, 1)
)
_Hh3cObjpZonePairRunningInfoTable_Object = MibTable
hh3cObjpZonePairRunningInfoTable = _Hh3cObjpZonePairRunningInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 155, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cObjpZonePairRunningInfoTable.setStatus("current")
_Hh3cObjpZonePairRunningInfoEntry_Object = MibTableRow
hh3cObjpZonePairRunningInfoEntry = _Hh3cObjpZonePairRunningInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 155, 1, 1, 1)
)
hh3cObjpZonePairRunningInfoEntry.setIndexNames(
    (0, "HH3C-OBJP-MIB", "hh3cObjpZonePairSrcZone"),
    (0, "HH3C-OBJP-MIB", "hh3cObjpZonePairDstZone"),
    (0, "HH3C-OBJP-MIB", "hh3cObjpZonePairIPVersion"),
    (0, "HH3C-OBJP-MIB", "hh3cObjpZonePairRuleID"),
)
if mibBuilder.loadTexts:
    hh3cObjpZonePairRunningInfoEntry.setStatus("current")


class _Hh3cObjpZonePairSrcZone_Type(OctetString):
    """Custom type hh3cObjpZonePairSrcZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cObjpZonePairSrcZone_Type.__name__ = "OctetString"
_Hh3cObjpZonePairSrcZone_Object = MibTableColumn
hh3cObjpZonePairSrcZone = _Hh3cObjpZonePairSrcZone_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 155, 1, 1, 1, 1),
    _Hh3cObjpZonePairSrcZone_Type()
)
hh3cObjpZonePairSrcZone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cObjpZonePairSrcZone.setStatus("current")


class _Hh3cObjpZonePairDstZone_Type(OctetString):
    """Custom type hh3cObjpZonePairDstZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cObjpZonePairDstZone_Type.__name__ = "OctetString"
_Hh3cObjpZonePairDstZone_Object = MibTableColumn
hh3cObjpZonePairDstZone = _Hh3cObjpZonePairDstZone_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 155, 1, 1, 1, 2),
    _Hh3cObjpZonePairDstZone_Type()
)
hh3cObjpZonePairDstZone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cObjpZonePairDstZone.setStatus("current")


class _Hh3cObjpZonePairIPVersion_Type(Integer32):
    """Custom type hh3cObjpZonePairIPVersion based on Integer32"""
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


_Hh3cObjpZonePairIPVersion_Type.__name__ = "Integer32"
_Hh3cObjpZonePairIPVersion_Object = MibTableColumn
hh3cObjpZonePairIPVersion = _Hh3cObjpZonePairIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 155, 1, 1, 1, 3),
    _Hh3cObjpZonePairIPVersion_Type()
)
hh3cObjpZonePairIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cObjpZonePairIPVersion.setStatus("current")


class _Hh3cObjpZonePairRuleID_Type(Unsigned32):
    """Custom type hh3cObjpZonePairRuleID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cObjpZonePairRuleID_Type.__name__ = "Unsigned32"
_Hh3cObjpZonePairRuleID_Object = MibTableColumn
hh3cObjpZonePairRuleID = _Hh3cObjpZonePairRuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 155, 1, 1, 1, 4),
    _Hh3cObjpZonePairRuleID_Type()
)
hh3cObjpZonePairRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cObjpZonePairRuleID.setStatus("current")
_Hh3cObjpZonePairMatchPacketCount_Type = Counter64
_Hh3cObjpZonePairMatchPacketCount_Object = MibTableColumn
hh3cObjpZonePairMatchPacketCount = _Hh3cObjpZonePairMatchPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 155, 1, 1, 1, 5),
    _Hh3cObjpZonePairMatchPacketCount_Type()
)
hh3cObjpZonePairMatchPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cObjpZonePairMatchPacketCount.setStatus("current")
_Hh3cObjpZonePairLastMatchTime_Type = Unsigned32
_Hh3cObjpZonePairLastMatchTime_Object = MibTableColumn
hh3cObjpZonePairLastMatchTime = _Hh3cObjpZonePairLastMatchTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 155, 1, 1, 1, 6),
    _Hh3cObjpZonePairLastMatchTime_Type()
)
hh3cObjpZonePairLastMatchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cObjpZonePairLastMatchTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-OBJP-MIB",
    **{"hh3cObjp": hh3cObjp,
       "hh3cObjpZonePairObjects": hh3cObjpZonePairObjects,
       "hh3cObjpZonePairRunningInfoTable": hh3cObjpZonePairRunningInfoTable,
       "hh3cObjpZonePairRunningInfoEntry": hh3cObjpZonePairRunningInfoEntry,
       "hh3cObjpZonePairSrcZone": hh3cObjpZonePairSrcZone,
       "hh3cObjpZonePairDstZone": hh3cObjpZonePairDstZone,
       "hh3cObjpZonePairIPVersion": hh3cObjpZonePairIPVersion,
       "hh3cObjpZonePairRuleID": hh3cObjpZonePairRuleID,
       "hh3cObjpZonePairMatchPacketCount": hh3cObjpZonePairMatchPacketCount,
       "hh3cObjpZonePairLastMatchTime": hh3cObjpZonePairLastMatchTime}
)
