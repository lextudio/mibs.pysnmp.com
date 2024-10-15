# SNMP MIB module (BSUVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BSUVLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:49 2024
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

(bsu,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "bsu")

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

aniBsuVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AniBsuVlanConf_ObjectIdentity = ObjectIdentity
aniBsuVlanConf = _AniBsuVlanConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 11, 1)
)


class _AniBsuVlanConfMgmtVlanId_Type(Integer32):
    """Custom type aniBsuVlanConfMgmtVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AniBsuVlanConfMgmtVlanId_Type.__name__ = "Integer32"
_AniBsuVlanConfMgmtVlanId_Object = MibScalar
aniBsuVlanConfMgmtVlanId = _AniBsuVlanConfMgmtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 11, 1, 1),
    _AniBsuVlanConfMgmtVlanId_Type()
)
aniBsuVlanConfMgmtVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuVlanConfMgmtVlanId.setStatus("current")


class _AniBsuVlanConfOuterTagId_Type(Integer32):
    """Custom type aniBsuVlanConfOuterTagId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AniBsuVlanConfOuterTagId_Type.__name__ = "Integer32"
_AniBsuVlanConfOuterTagId_Object = MibScalar
aniBsuVlanConfOuterTagId = _AniBsuVlanConfOuterTagId_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 11, 1, 4),
    _AniBsuVlanConfOuterTagId_Type()
)
aniBsuVlanConfOuterTagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuVlanConfOuterTagId.setStatus("current")


class _AniBsuVlanConfMgmtVlanIdPriority_Type(Integer32):
    """Custom type aniBsuVlanConfMgmtVlanIdPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AniBsuVlanConfMgmtVlanIdPriority_Type.__name__ = "Integer32"
_AniBsuVlanConfMgmtVlanIdPriority_Object = MibScalar
aniBsuVlanConfMgmtVlanIdPriority = _AniBsuVlanConfMgmtVlanIdPriority_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 11, 1, 5),
    _AniBsuVlanConfMgmtVlanIdPriority_Type()
)
aniBsuVlanConfMgmtVlanIdPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuVlanConfMgmtVlanIdPriority.setStatus("current")


class _AniBsuVlanConfOuterTagPriority_Type(Integer32):
    """Custom type aniBsuVlanConfOuterTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AniBsuVlanConfOuterTagPriority_Type.__name__ = "Integer32"
_AniBsuVlanConfOuterTagPriority_Object = MibScalar
aniBsuVlanConfOuterTagPriority = _AniBsuVlanConfOuterTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 11, 1, 6),
    _AniBsuVlanConfOuterTagPriority_Type()
)
aniBsuVlanConfOuterTagPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuVlanConfOuterTagPriority.setStatus("current")
_AniBsuVlanConfSUMgmtVlanIdList_Type = DisplayString
_AniBsuVlanConfSUMgmtVlanIdList_Object = MibScalar
aniBsuVlanConfSUMgmtVlanIdList = _AniBsuVlanConfSUMgmtVlanIdList_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 11, 1, 7),
    _AniBsuVlanConfSUMgmtVlanIdList_Type()
)
aniBsuVlanConfSUMgmtVlanIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuVlanConfSUMgmtVlanIdList.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BSUVLAN-MIB",
    **{"aniBsuVlan": aniBsuVlan,
       "aniBsuVlanConf": aniBsuVlanConf,
       "aniBsuVlanConfMgmtVlanId": aniBsuVlanConfMgmtVlanId,
       "aniBsuVlanConfOuterTagId": aniBsuVlanConfOuterTagId,
       "aniBsuVlanConfMgmtVlanIdPriority": aniBsuVlanConfMgmtVlanIdPriority,
       "aniBsuVlanConfOuterTagPriority": aniBsuVlanConfOuterTagPriority,
       "aniBsuVlanConfSUMgmtVlanIdList": aniBsuVlanConfSUMgmtVlanIdList}
)
