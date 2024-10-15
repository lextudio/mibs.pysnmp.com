# SNMP MIB module (SNMPEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNMPEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:15 2024
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

(snmpExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "snmpExt")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

apSnmpExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApSnmpExtTrapGeneric_Type(Integer32):
    """Custom type apSnmpExtTrapGeneric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSnmpExtTrapGeneric_Type.__name__ = "Integer32"
_ApSnmpExtTrapGeneric_Object = MibScalar
apSnmpExtTrapGeneric = _ApSnmpExtTrapGeneric_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 2),
    _ApSnmpExtTrapGeneric_Type()
)
apSnmpExtTrapGeneric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtTrapGeneric.setStatus("current")


class _ApSnmpExtTrapEnterprise_Type(Integer32):
    """Custom type apSnmpExtTrapEnterprise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSnmpExtTrapEnterprise_Type.__name__ = "Integer32"
_ApSnmpExtTrapEnterprise_Object = MibScalar
apSnmpExtTrapEnterprise = _ApSnmpExtTrapEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 3),
    _ApSnmpExtTrapEnterprise_Type()
)
apSnmpExtTrapEnterprise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtTrapEnterprise.setStatus("current")
_ApSnmpExtCommunityTable_Object = MibTable
apSnmpExtCommunityTable = _ApSnmpExtCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 4)
)
if mibBuilder.loadTexts:
    apSnmpExtCommunityTable.setStatus("current")
_ApSnmpExtCommunityEntry_Object = MibTableRow
apSnmpExtCommunityEntry = _ApSnmpExtCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 4, 1)
)
apSnmpExtCommunityEntry.setIndexNames(
    (0, "SNMPEXT-MIB", "apSnmpExtCommunityName"),
)
if mibBuilder.loadTexts:
    apSnmpExtCommunityEntry.setStatus("current")


class _ApSnmpExtCommunityName_Type(DisplayString):
    """Custom type apSnmpExtCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_ApSnmpExtCommunityName_Type.__name__ = "DisplayString"
_ApSnmpExtCommunityName_Object = MibTableColumn
apSnmpExtCommunityName = _ApSnmpExtCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 4, 1, 1),
    _ApSnmpExtCommunityName_Type()
)
apSnmpExtCommunityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSnmpExtCommunityName.setStatus("current")


class _ApSnmpExtCommunityType_Type(Integer32):
    """Custom type apSnmpExtCommunityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ro", 0),
          ("rw", 1))
    )


_ApSnmpExtCommunityType_Type.__name__ = "Integer32"
_ApSnmpExtCommunityType_Object = MibTableColumn
apSnmpExtCommunityType = _ApSnmpExtCommunityType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 4, 1, 2),
    _ApSnmpExtCommunityType_Type()
)
apSnmpExtCommunityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSnmpExtCommunityType.setStatus("current")
_ApSnmpExtCommunityStatus_Type = RowStatus
_ApSnmpExtCommunityStatus_Object = MibTableColumn
apSnmpExtCommunityStatus = _ApSnmpExtCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 4, 1, 3),
    _ApSnmpExtCommunityStatus_Type()
)
apSnmpExtCommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSnmpExtCommunityStatus.setStatus("current")
_ApSnmpExtTrapTable_Object = MibTable
apSnmpExtTrapTable = _ApSnmpExtTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 5)
)
if mibBuilder.loadTexts:
    apSnmpExtTrapTable.setStatus("current")
_ApSnmpExtTrapEntry_Object = MibTableRow
apSnmpExtTrapEntry = _ApSnmpExtTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 5, 1)
)
apSnmpExtTrapEntry.setIndexNames(
    (0, "SNMPEXT-MIB", "apSnmpExtTrapIp"),
)
if mibBuilder.loadTexts:
    apSnmpExtTrapEntry.setStatus("current")
_ApSnmpExtTrapIp_Type = IpAddress
_ApSnmpExtTrapIp_Object = MibTableColumn
apSnmpExtTrapIp = _ApSnmpExtTrapIp_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 5, 1, 1),
    _ApSnmpExtTrapIp_Type()
)
apSnmpExtTrapIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSnmpExtTrapIp.setStatus("current")


class _ApSnmpExtTrapCommunity_Type(DisplayString):
    """Custom type apSnmpExtTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_ApSnmpExtTrapCommunity_Type.__name__ = "DisplayString"
_ApSnmpExtTrapCommunity_Object = MibTableColumn
apSnmpExtTrapCommunity = _ApSnmpExtTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 5, 1, 2),
    _ApSnmpExtTrapCommunity_Type()
)
apSnmpExtTrapCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSnmpExtTrapCommunity.setStatus("current")
_ApSnmpExtTrapStatus_Type = RowStatus
_ApSnmpExtTrapStatus_Object = MibTableColumn
apSnmpExtTrapStatus = _ApSnmpExtTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 5, 1, 3),
    _ApSnmpExtTrapStatus_Type()
)
apSnmpExtTrapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSnmpExtTrapStatus.setStatus("current")
_ApSnmpExtReloadConfigVal_Type = Integer32
_ApSnmpExtReloadConfigVal_Object = MibScalar
apSnmpExtReloadConfigVal = _ApSnmpExtReloadConfigVal_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 6),
    _ApSnmpExtReloadConfigVal_Type()
)
apSnmpExtReloadConfigVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtReloadConfigVal.setStatus("current")
_ApSnmpExtReloadSet_Type = Integer32
_ApSnmpExtReloadSet_Object = MibScalar
apSnmpExtReloadSet = _ApSnmpExtReloadSet_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 7),
    _ApSnmpExtReloadSet_Type()
)
apSnmpExtReloadSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtReloadSet.setStatus("current")


class _ApSnmpExtServiceTraps_Type(Integer32):
    """Custom type apSnmpExtServiceTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSnmpExtServiceTraps_Type.__name__ = "Integer32"
_ApSnmpExtServiceTraps_Object = MibScalar
apSnmpExtServiceTraps = _ApSnmpExtServiceTraps_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 8),
    _ApSnmpExtServiceTraps_Type()
)
apSnmpExtServiceTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtServiceTraps.setStatus("current")


class _ApSnmpExtLoginFailTraps_Type(Integer32):
    """Custom type apSnmpExtLoginFailTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSnmpExtLoginFailTraps_Type.__name__ = "Integer32"
_ApSnmpExtLoginFailTraps_Object = MibScalar
apSnmpExtLoginFailTraps = _ApSnmpExtLoginFailTraps_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 9),
    _ApSnmpExtLoginFailTraps_Type()
)
apSnmpExtLoginFailTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtLoginFailTraps.setStatus("current")


class _ApSnmpExtReloadTraps_Type(Integer32):
    """Custom type apSnmpExtReloadTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSnmpExtReloadTraps_Type.__name__ = "Integer32"
_ApSnmpExtReloadTraps_Object = MibScalar
apSnmpExtReloadTraps = _ApSnmpExtReloadTraps_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 10),
    _ApSnmpExtReloadTraps_Type()
)
apSnmpExtReloadTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtReloadTraps.setStatus("current")


class _ApSnmpExtLastTrap_Type(DisplayString):
    """Custom type apSnmpExtLastTrap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSnmpExtLastTrap_Type.__name__ = "DisplayString"
_ApSnmpExtLastTrap_Object = MibScalar
apSnmpExtLastTrap = _ApSnmpExtLastTrap_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 11),
    _ApSnmpExtLastTrap_Type()
)
apSnmpExtLastTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSnmpExtLastTrap.setStatus("current")


class _ApSnmpExtRedundancyTraps_Type(Integer32):
    """Custom type apSnmpExtRedundancyTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSnmpExtRedundancyTraps_Type.__name__ = "Integer32"
_ApSnmpExtRedundancyTraps_Object = MibScalar
apSnmpExtRedundancyTraps = _ApSnmpExtRedundancyTraps_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 12),
    _ApSnmpExtRedundancyTraps_Type()
)
apSnmpExtRedundancyTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtRedundancyTraps.setStatus("current")
_ApSnmpExtForceDumpConfigVal_Type = Integer32
_ApSnmpExtForceDumpConfigVal_Object = MibScalar
apSnmpExtForceDumpConfigVal = _ApSnmpExtForceDumpConfigVal_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 13),
    _ApSnmpExtForceDumpConfigVal_Type()
)
apSnmpExtForceDumpConfigVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtForceDumpConfigVal.setStatus("current")
_ApSnmpExtForceDumpSlot_Type = Integer32
_ApSnmpExtForceDumpSlot_Object = MibScalar
apSnmpExtForceDumpSlot = _ApSnmpExtForceDumpSlot_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 14),
    _ApSnmpExtForceDumpSlot_Type()
)
apSnmpExtForceDumpSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtForceDumpSlot.setStatus("current")
_ApSnmpExtForceDumpSubSlot_Type = Integer32
_ApSnmpExtForceDumpSubSlot_Object = MibScalar
apSnmpExtForceDumpSubSlot = _ApSnmpExtForceDumpSubSlot_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 15),
    _ApSnmpExtForceDumpSubSlot_Type()
)
apSnmpExtForceDumpSubSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtForceDumpSubSlot.setStatus("current")
_ApSnmpExtForceDump_Type = Integer32
_ApSnmpExtForceDump_Object = MibScalar
apSnmpExtForceDump = _ApSnmpExtForceDump_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 16),
    _ApSnmpExtForceDump_Type()
)
apSnmpExtForceDump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtForceDump.setStatus("current")


class _ApSnmpExtDosSynTraps_Type(Integer32):
    """Custom type apSnmpExtDosSynTraps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSnmpExtDosSynTraps_Type.__name__ = "Integer32"
_ApSnmpExtDosSynTraps_Object = MibScalar
apSnmpExtDosSynTraps = _ApSnmpExtDosSynTraps_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 17),
    _ApSnmpExtDosSynTraps_Type()
)
apSnmpExtDosSynTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtDosSynTraps.setStatus("current")


class _ApSnmpExtDosLandTraps_Type(Integer32):
    """Custom type apSnmpExtDosLandTraps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSnmpExtDosLandTraps_Type.__name__ = "Integer32"
_ApSnmpExtDosLandTraps_Object = MibScalar
apSnmpExtDosLandTraps = _ApSnmpExtDosLandTraps_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 18),
    _ApSnmpExtDosLandTraps_Type()
)
apSnmpExtDosLandTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtDosLandTraps.setStatus("current")


class _ApSnmpExtDosIllegalTraps_Type(Integer32):
    """Custom type apSnmpExtDosIllegalTraps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSnmpExtDosIllegalTraps_Type.__name__ = "Integer32"
_ApSnmpExtDosIllegalTraps_Object = MibScalar
apSnmpExtDosIllegalTraps = _ApSnmpExtDosIllegalTraps_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 19),
    _ApSnmpExtDosIllegalTraps_Type()
)
apSnmpExtDosIllegalTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtDosIllegalTraps.setStatus("current")


class _ApSnmpExtDosPingTraps_Type(Integer32):
    """Custom type apSnmpExtDosPingTraps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSnmpExtDosPingTraps_Type.__name__ = "Integer32"
_ApSnmpExtDosPingTraps_Object = MibScalar
apSnmpExtDosPingTraps = _ApSnmpExtDosPingTraps_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 20),
    _ApSnmpExtDosPingTraps_Type()
)
apSnmpExtDosPingTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtDosPingTraps.setStatus("obsolete")


class _ApSnmpExtDosSmurfTraps_Type(Integer32):
    """Custom type apSnmpExtDosSmurfTraps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSnmpExtDosSmurfTraps_Type.__name__ = "Integer32"
_ApSnmpExtDosSmurfTraps_Object = MibScalar
apSnmpExtDosSmurfTraps = _ApSnmpExtDosSmurfTraps_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 21),
    _ApSnmpExtDosSmurfTraps_Type()
)
apSnmpExtDosSmurfTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtDosSmurfTraps.setStatus("current")


class _ApSnmpExtDosSynTrapThreshold_Type(Integer32):
    """Custom type apSnmpExtDosSynTrapThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApSnmpExtDosSynTrapThreshold_Type.__name__ = "Integer32"
_ApSnmpExtDosSynTrapThreshold_Object = MibScalar
apSnmpExtDosSynTrapThreshold = _ApSnmpExtDosSynTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 22),
    _ApSnmpExtDosSynTrapThreshold_Type()
)
apSnmpExtDosSynTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtDosSynTrapThreshold.setStatus("current")


class _ApSnmpExtDosLandTrapThreshold_Type(Integer32):
    """Custom type apSnmpExtDosLandTrapThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApSnmpExtDosLandTrapThreshold_Type.__name__ = "Integer32"
_ApSnmpExtDosLandTrapThreshold_Object = MibScalar
apSnmpExtDosLandTrapThreshold = _ApSnmpExtDosLandTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 23),
    _ApSnmpExtDosLandTrapThreshold_Type()
)
apSnmpExtDosLandTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtDosLandTrapThreshold.setStatus("current")


class _ApSnmpExtDosIllegalTrapThreshold_Type(Integer32):
    """Custom type apSnmpExtDosIllegalTrapThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApSnmpExtDosIllegalTrapThreshold_Type.__name__ = "Integer32"
_ApSnmpExtDosIllegalTrapThreshold_Object = MibScalar
apSnmpExtDosIllegalTrapThreshold = _ApSnmpExtDosIllegalTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 24),
    _ApSnmpExtDosIllegalTrapThreshold_Type()
)
apSnmpExtDosIllegalTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtDosIllegalTrapThreshold.setStatus("current")


class _ApSnmpExtDosPingTrapThreshold_Type(Integer32):
    """Custom type apSnmpExtDosPingTrapThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApSnmpExtDosPingTrapThreshold_Type.__name__ = "Integer32"
_ApSnmpExtDosPingTrapThreshold_Object = MibScalar
apSnmpExtDosPingTrapThreshold = _ApSnmpExtDosPingTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 25),
    _ApSnmpExtDosPingTrapThreshold_Type()
)
apSnmpExtDosPingTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtDosPingTrapThreshold.setStatus("obsolete")


class _ApSnmpExtDosSmurfTrapThreshold_Type(Integer32):
    """Custom type apSnmpExtDosSmurfTrapThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApSnmpExtDosSmurfTrapThreshold_Type.__name__ = "Integer32"
_ApSnmpExtDosSmurfTrapThreshold_Object = MibScalar
apSnmpExtDosSmurfTrapThreshold = _ApSnmpExtDosSmurfTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 26),
    _ApSnmpExtDosSmurfTrapThreshold_Type()
)
apSnmpExtDosSmurfTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSnmpExtDosSmurfTrapThreshold.setStatus("current")

# Managed Objects groups


# Notification objects

apSnmpExtReloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2467, 1, 22, 0, 1)
)
if mibBuilder.loadTexts:
    apSnmpExtReloadTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMPEXT-MIB",
    **{"apSnmpExtReloadTrap": apSnmpExtReloadTrap,
       "apSnmpExtMib": apSnmpExtMib,
       "apSnmpExtTrapGeneric": apSnmpExtTrapGeneric,
       "apSnmpExtTrapEnterprise": apSnmpExtTrapEnterprise,
       "apSnmpExtCommunityTable": apSnmpExtCommunityTable,
       "apSnmpExtCommunityEntry": apSnmpExtCommunityEntry,
       "apSnmpExtCommunityName": apSnmpExtCommunityName,
       "apSnmpExtCommunityType": apSnmpExtCommunityType,
       "apSnmpExtCommunityStatus": apSnmpExtCommunityStatus,
       "apSnmpExtTrapTable": apSnmpExtTrapTable,
       "apSnmpExtTrapEntry": apSnmpExtTrapEntry,
       "apSnmpExtTrapIp": apSnmpExtTrapIp,
       "apSnmpExtTrapCommunity": apSnmpExtTrapCommunity,
       "apSnmpExtTrapStatus": apSnmpExtTrapStatus,
       "apSnmpExtReloadConfigVal": apSnmpExtReloadConfigVal,
       "apSnmpExtReloadSet": apSnmpExtReloadSet,
       "apSnmpExtServiceTraps": apSnmpExtServiceTraps,
       "apSnmpExtLoginFailTraps": apSnmpExtLoginFailTraps,
       "apSnmpExtReloadTraps": apSnmpExtReloadTraps,
       "apSnmpExtLastTrap": apSnmpExtLastTrap,
       "apSnmpExtRedundancyTraps": apSnmpExtRedundancyTraps,
       "apSnmpExtForceDumpConfigVal": apSnmpExtForceDumpConfigVal,
       "apSnmpExtForceDumpSlot": apSnmpExtForceDumpSlot,
       "apSnmpExtForceDumpSubSlot": apSnmpExtForceDumpSubSlot,
       "apSnmpExtForceDump": apSnmpExtForceDump,
       "apSnmpExtDosSynTraps": apSnmpExtDosSynTraps,
       "apSnmpExtDosLandTraps": apSnmpExtDosLandTraps,
       "apSnmpExtDosIllegalTraps": apSnmpExtDosIllegalTraps,
       "apSnmpExtDosPingTraps": apSnmpExtDosPingTraps,
       "apSnmpExtDosSmurfTraps": apSnmpExtDosSmurfTraps,
       "apSnmpExtDosSynTrapThreshold": apSnmpExtDosSynTrapThreshold,
       "apSnmpExtDosLandTrapThreshold": apSnmpExtDosLandTrapThreshold,
       "apSnmpExtDosIllegalTrapThreshold": apSnmpExtDosIllegalTrapThreshold,
       "apSnmpExtDosPingTrapThreshold": apSnmpExtDosPingTrapThreshold,
       "apSnmpExtDosSmurfTrapThreshold": apSnmpExtDosSmurfTrapThreshold}
)
