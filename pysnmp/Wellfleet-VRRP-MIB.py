# SNMP MIB module (Wellfleet-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-VRRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:25 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(wfVrrpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfVrrpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfVrrpAdminTable_Object = MibTable
wfVrrpAdminTable = _WfVrrpAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1)
)
if mibBuilder.loadTexts:
    wfVrrpAdminTable.setStatus("mandatory")
_WfVrrpAdminEntry_Object = MibTableRow
wfVrrpAdminEntry = _WfVrrpAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1, 1)
)
wfVrrpAdminEntry.setIndexNames(
    (0, "Wellfleet-VRRP-MIB", "wfVrrpAdminPrimaryIpAddr"),
    (0, "Wellfleet-VRRP-MIB", "wfVrrpAdminVrId"),
)
if mibBuilder.loadTexts:
    wfVrrpAdminEntry.setStatus("mandatory")


class _WfVrrpAdminDelete_Type(Integer32):
    """Custom type wfVrrpAdminDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfVrrpAdminDelete_Type.__name__ = "Integer32"
_WfVrrpAdminDelete_Object = MibTableColumn
wfVrrpAdminDelete = _WfVrrpAdminDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1, 1, 1),
    _WfVrrpAdminDelete_Type()
)
wfVrrpAdminDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVrrpAdminDelete.setStatus("mandatory")


class _WfVrrpAdminDisable_Type(Integer32):
    """Custom type wfVrrpAdminDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfVrrpAdminDisable_Type.__name__ = "Integer32"
_WfVrrpAdminDisable_Object = MibTableColumn
wfVrrpAdminDisable = _WfVrrpAdminDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1, 1, 2),
    _WfVrrpAdminDisable_Type()
)
wfVrrpAdminDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVrrpAdminDisable.setStatus("mandatory")


class _WfVrrpAdminState_Type(Integer32):
    """Custom type wfVrrpAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("down", 4),
          ("initialize", 1),
          ("master", 3))
    )


_WfVrrpAdminState_Type.__name__ = "Integer32"
_WfVrrpAdminState_Object = MibTableColumn
wfVrrpAdminState = _WfVrrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1, 1, 3),
    _WfVrrpAdminState_Type()
)
wfVrrpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpAdminState.setStatus("mandatory")
_WfVrrpAdminPrimaryIpAddr_Type = IpAddress
_WfVrrpAdminPrimaryIpAddr_Object = MibTableColumn
wfVrrpAdminPrimaryIpAddr = _WfVrrpAdminPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1, 1, 4),
    _WfVrrpAdminPrimaryIpAddr_Type()
)
wfVrrpAdminPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpAdminPrimaryIpAddr.setStatus("mandatory")


class _WfVrrpAdminVrId_Type(Integer32):
    """Custom type wfVrrpAdminVrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfVrrpAdminVrId_Type.__name__ = "Integer32"
_WfVrrpAdminVrId_Object = MibTableColumn
wfVrrpAdminVrId = _WfVrrpAdminVrId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1, 1, 5),
    _WfVrrpAdminVrId_Type()
)
wfVrrpAdminVrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpAdminVrId.setStatus("mandatory")
_WfVrrpAdminIpAddr_Type = IpAddress
_WfVrrpAdminIpAddr_Object = MibTableColumn
wfVrrpAdminIpAddr = _WfVrrpAdminIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1, 1, 6),
    _WfVrrpAdminIpAddr_Type()
)
wfVrrpAdminIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVrrpAdminIpAddr.setStatus("mandatory")
_WfVrrpAdminVirtualMacAddr_Type = PhysAddress
_WfVrrpAdminVirtualMacAddr_Object = MibTableColumn
wfVrrpAdminVirtualMacAddr = _WfVrrpAdminVirtualMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1, 1, 7),
    _WfVrrpAdminVirtualMacAddr_Type()
)
wfVrrpAdminVirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpAdminVirtualMacAddr.setStatus("mandatory")


class _WfVrrpAdminPriority_Type(Integer32):
    """Custom type wfVrrpAdminPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfVrrpAdminPriority_Type.__name__ = "Integer32"
_WfVrrpAdminPriority_Object = MibTableColumn
wfVrrpAdminPriority = _WfVrrpAdminPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1, 1, 8),
    _WfVrrpAdminPriority_Type()
)
wfVrrpAdminPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVrrpAdminPriority.setStatus("mandatory")


class _WfVrrpAdminAdvertisementInterval_Type(Integer32):
    """Custom type wfVrrpAdminAdvertisementInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfVrrpAdminAdvertisementInterval_Type.__name__ = "Integer32"
_WfVrrpAdminAdvertisementInterval_Object = MibTableColumn
wfVrrpAdminAdvertisementInterval = _WfVrrpAdminAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1, 1, 9),
    _WfVrrpAdminAdvertisementInterval_Type()
)
wfVrrpAdminAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVrrpAdminAdvertisementInterval.setStatus("mandatory")
_WfVrrpAdminCriticalIpInterface_Type = IpAddress
_WfVrrpAdminCriticalIpInterface_Object = MibTableColumn
wfVrrpAdminCriticalIpInterface = _WfVrrpAdminCriticalIpInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1, 1, 10),
    _WfVrrpAdminCriticalIpInterface_Type()
)
wfVrrpAdminCriticalIpInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVrrpAdminCriticalIpInterface.setStatus("mandatory")


class _WfVrrpAdminIPXBackup_Type(Integer32):
    """Custom type wfVrrpAdminIPXBackup based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfVrrpAdminIPXBackup_Type.__name__ = "Integer32"
_WfVrrpAdminIPXBackup_Object = MibTableColumn
wfVrrpAdminIPXBackup = _WfVrrpAdminIPXBackup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1, 1, 11),
    _WfVrrpAdminIPXBackup_Type()
)
wfVrrpAdminIPXBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVrrpAdminIPXBackup.setStatus("mandatory")


class _WfVrrpAdminIGMPBackup_Type(Integer32):
    """Custom type wfVrrpAdminIGMPBackup based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfVrrpAdminIGMPBackup_Type.__name__ = "Integer32"
_WfVrrpAdminIGMPBackup_Object = MibTableColumn
wfVrrpAdminIGMPBackup = _WfVrrpAdminIGMPBackup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1, 1, 12),
    _WfVrrpAdminIGMPBackup_Type()
)
wfVrrpAdminIGMPBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVrrpAdminIGMPBackup.setStatus("mandatory")
_WfVrrpAdminTokenRingAddress_Type = OctetString
_WfVrrpAdminTokenRingAddress_Object = MibTableColumn
wfVrrpAdminTokenRingAddress = _WfVrrpAdminTokenRingAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1, 1, 13),
    _WfVrrpAdminTokenRingAddress_Type()
)
wfVrrpAdminTokenRingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVrrpAdminTokenRingAddress.setStatus("mandatory")


class _WfVrrpAdminPreemptMode_Type(Integer32):
    """Custom type wfVrrpAdminPreemptMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfVrrpAdminPreemptMode_Type.__name__ = "Integer32"
_WfVrrpAdminPreemptMode_Object = MibTableColumn
wfVrrpAdminPreemptMode = _WfVrrpAdminPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1, 1, 14),
    _WfVrrpAdminPreemptMode_Type()
)
wfVrrpAdminPreemptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVrrpAdminPreemptMode.setStatus("mandatory")


class _WfVrrpAdminMasterPingEnable_Type(Integer32):
    """Custom type wfVrrpAdminMasterPingEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfVrrpAdminMasterPingEnable_Type.__name__ = "Integer32"
_WfVrrpAdminMasterPingEnable_Object = MibTableColumn
wfVrrpAdminMasterPingEnable = _WfVrrpAdminMasterPingEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 1, 1, 15),
    _WfVrrpAdminMasterPingEnable_Type()
)
wfVrrpAdminMasterPingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfVrrpAdminMasterPingEnable.setStatus("mandatory")
_WfVrrpRouterStatsTable_Object = MibTable
wfVrrpRouterStatsTable = _WfVrrpRouterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 2)
)
if mibBuilder.loadTexts:
    wfVrrpRouterStatsTable.setStatus("mandatory")
_WfVrrpRouterStatsEntry_Object = MibTableRow
wfVrrpRouterStatsEntry = _WfVrrpRouterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 2, 1)
)
wfVrrpRouterStatsEntry.setIndexNames(
    (0, "Wellfleet-VRRP-MIB", "wfVrrpStatsPrimaryIpAddr"),
    (0, "Wellfleet-VRRP-MIB", "wfVrrpStatsVrId"),
)
if mibBuilder.loadTexts:
    wfVrrpRouterStatsEntry.setStatus("mandatory")
_WfVrrpStatsPrimaryIpAddr_Type = IpAddress
_WfVrrpStatsPrimaryIpAddr_Object = MibTableColumn
wfVrrpStatsPrimaryIpAddr = _WfVrrpStatsPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 2, 1, 1),
    _WfVrrpStatsPrimaryIpAddr_Type()
)
wfVrrpStatsPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpStatsPrimaryIpAddr.setStatus("mandatory")


class _WfVrrpStatsVrId_Type(Integer32):
    """Custom type wfVrrpStatsVrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfVrrpStatsVrId_Type.__name__ = "Integer32"
_WfVrrpStatsVrId_Object = MibTableColumn
wfVrrpStatsVrId = _WfVrrpStatsVrId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 2, 1, 2),
    _WfVrrpStatsVrId_Type()
)
wfVrrpStatsVrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpStatsVrId.setStatus("mandatory")
_WfVrrpStatsMasterTransitions_Type = Counter32
_WfVrrpStatsMasterTransitions_Object = MibTableColumn
wfVrrpStatsMasterTransitions = _WfVrrpStatsMasterTransitions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 2, 1, 3),
    _WfVrrpStatsMasterTransitions_Type()
)
wfVrrpStatsMasterTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpStatsMasterTransitions.setStatus("mandatory")
_WfVrrpStatsInAdvertisements_Type = Counter32
_WfVrrpStatsInAdvertisements_Object = MibTableColumn
wfVrrpStatsInAdvertisements = _WfVrrpStatsInAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 2, 1, 4),
    _WfVrrpStatsInAdvertisements_Type()
)
wfVrrpStatsInAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpStatsInAdvertisements.setStatus("mandatory")
_WfVrrpStatsChecksumErrors_Type = Counter32
_WfVrrpStatsChecksumErrors_Object = MibTableColumn
wfVrrpStatsChecksumErrors = _WfVrrpStatsChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 2, 1, 5),
    _WfVrrpStatsChecksumErrors_Type()
)
wfVrrpStatsChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpStatsChecksumErrors.setStatus("mandatory")
_WfVrrpStatsVersionErrors_Type = Counter32
_WfVrrpStatsVersionErrors_Object = MibTableColumn
wfVrrpStatsVersionErrors = _WfVrrpStatsVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 2, 1, 6),
    _WfVrrpStatsVersionErrors_Type()
)
wfVrrpStatsVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpStatsVersionErrors.setStatus("mandatory")
_WfVrrpStatsVrIdErrors_Type = Counter32
_WfVrrpStatsVrIdErrors_Object = MibTableColumn
wfVrrpStatsVrIdErrors = _WfVrrpStatsVrIdErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 2, 1, 7),
    _WfVrrpStatsVrIdErrors_Type()
)
wfVrrpStatsVrIdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpStatsVrIdErrors.setStatus("mandatory")
_WfVrrpStatsAdvertiseIntervalErrors_Type = Counter32
_WfVrrpStatsAdvertiseIntervalErrors_Object = MibTableColumn
wfVrrpStatsAdvertiseIntervalErrors = _WfVrrpStatsAdvertiseIntervalErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 2, 1, 8),
    _WfVrrpStatsAdvertiseIntervalErrors_Type()
)
wfVrrpStatsAdvertiseIntervalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpStatsAdvertiseIntervalErrors.setStatus("mandatory")
_WfVrrpStatsIpTtlErrors_Type = Counter32
_WfVrrpStatsIpTtlErrors_Object = MibTableColumn
wfVrrpStatsIpTtlErrors = _WfVrrpStatsIpTtlErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 2, 1, 9),
    _WfVrrpStatsIpTtlErrors_Type()
)
wfVrrpStatsIpTtlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpStatsIpTtlErrors.setStatus("mandatory")
_WfVrrpStatsInPriorityZeroAdvertisements_Type = Counter32
_WfVrrpStatsInPriorityZeroAdvertisements_Object = MibTableColumn
wfVrrpStatsInPriorityZeroAdvertisements = _WfVrrpStatsInPriorityZeroAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 2, 1, 10),
    _WfVrrpStatsInPriorityZeroAdvertisements_Type()
)
wfVrrpStatsInPriorityZeroAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpStatsInPriorityZeroAdvertisements.setStatus("mandatory")
_WfVrrpStatsOutPriorityZeroAdvertisements_Type = Counter32
_WfVrrpStatsOutPriorityZeroAdvertisements_Object = MibTableColumn
wfVrrpStatsOutPriorityZeroAdvertisements = _WfVrrpStatsOutPriorityZeroAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 2, 1, 11),
    _WfVrrpStatsOutPriorityZeroAdvertisements_Type()
)
wfVrrpStatsOutPriorityZeroAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpStatsOutPriorityZeroAdvertisements.setStatus("mandatory")
_WfVrrpStatsInInvalidTypeAdvertisements_Type = Counter32
_WfVrrpStatsInInvalidTypeAdvertisements_Object = MibTableColumn
wfVrrpStatsInInvalidTypeAdvertisements = _WfVrrpStatsInInvalidTypeAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 2, 1, 12),
    _WfVrrpStatsInInvalidTypeAdvertisements_Type()
)
wfVrrpStatsInInvalidTypeAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpStatsInInvalidTypeAdvertisements.setStatus("mandatory")
_WfVrrpStatsUnknownTypeAdvertisements_Type = Counter32
_WfVrrpStatsUnknownTypeAdvertisements_Object = MibTableColumn
wfVrrpStatsUnknownTypeAdvertisements = _WfVrrpStatsUnknownTypeAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 25, 2, 1, 13),
    _WfVrrpStatsUnknownTypeAdvertisements_Type()
)
wfVrrpStatsUnknownTypeAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfVrrpStatsUnknownTypeAdvertisements.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-VRRP-MIB",
    **{"wfVrrpAdminTable": wfVrrpAdminTable,
       "wfVrrpAdminEntry": wfVrrpAdminEntry,
       "wfVrrpAdminDelete": wfVrrpAdminDelete,
       "wfVrrpAdminDisable": wfVrrpAdminDisable,
       "wfVrrpAdminState": wfVrrpAdminState,
       "wfVrrpAdminPrimaryIpAddr": wfVrrpAdminPrimaryIpAddr,
       "wfVrrpAdminVrId": wfVrrpAdminVrId,
       "wfVrrpAdminIpAddr": wfVrrpAdminIpAddr,
       "wfVrrpAdminVirtualMacAddr": wfVrrpAdminVirtualMacAddr,
       "wfVrrpAdminPriority": wfVrrpAdminPriority,
       "wfVrrpAdminAdvertisementInterval": wfVrrpAdminAdvertisementInterval,
       "wfVrrpAdminCriticalIpInterface": wfVrrpAdminCriticalIpInterface,
       "wfVrrpAdminIPXBackup": wfVrrpAdminIPXBackup,
       "wfVrrpAdminIGMPBackup": wfVrrpAdminIGMPBackup,
       "wfVrrpAdminTokenRingAddress": wfVrrpAdminTokenRingAddress,
       "wfVrrpAdminPreemptMode": wfVrrpAdminPreemptMode,
       "wfVrrpAdminMasterPingEnable": wfVrrpAdminMasterPingEnable,
       "wfVrrpRouterStatsTable": wfVrrpRouterStatsTable,
       "wfVrrpRouterStatsEntry": wfVrrpRouterStatsEntry,
       "wfVrrpStatsPrimaryIpAddr": wfVrrpStatsPrimaryIpAddr,
       "wfVrrpStatsVrId": wfVrrpStatsVrId,
       "wfVrrpStatsMasterTransitions": wfVrrpStatsMasterTransitions,
       "wfVrrpStatsInAdvertisements": wfVrrpStatsInAdvertisements,
       "wfVrrpStatsChecksumErrors": wfVrrpStatsChecksumErrors,
       "wfVrrpStatsVersionErrors": wfVrrpStatsVersionErrors,
       "wfVrrpStatsVrIdErrors": wfVrrpStatsVrIdErrors,
       "wfVrrpStatsAdvertiseIntervalErrors": wfVrrpStatsAdvertiseIntervalErrors,
       "wfVrrpStatsIpTtlErrors": wfVrrpStatsIpTtlErrors,
       "wfVrrpStatsInPriorityZeroAdvertisements": wfVrrpStatsInPriorityZeroAdvertisements,
       "wfVrrpStatsOutPriorityZeroAdvertisements": wfVrrpStatsOutPriorityZeroAdvertisements,
       "wfVrrpStatsInInvalidTypeAdvertisements": wfVrrpStatsInInvalidTypeAdvertisements,
       "wfVrrpStatsUnknownTypeAdvertisements": wfVrrpStatsUnknownTypeAdvertisements}
)
