# SNMP MIB module (AT-ATMF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-ATMF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:57 2024
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

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

atmf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603)
)
atmf.setRevisions(
        ("2013-07-15 12:00",
         "2013-05-27 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtAtmfTraps_ObjectIdentity = ObjectIdentity
atAtmfTraps = _AtAtmfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0)
)
_AtAtmfTrapVariable_ObjectIdentity = ObjectIdentity
atAtmfTrapVariable = _AtAtmfTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1)
)


class _AtAtmfTrapNodeName_Type(DisplayStringUnsized):
    """Custom type atAtmfTrapNodeName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AtAtmfTrapNodeName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfTrapNodeName_Object = MibScalar
atAtmfTrapNodeName = _AtAtmfTrapNodeName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 1),
    _AtAtmfTrapNodeName_Type()
)
atAtmfTrapNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapNodeName.setStatus("current")


class _AtAtmfTrapMasterNodeName_Type(DisplayStringUnsized):
    """Custom type atAtmfTrapMasterNodeName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AtAtmfTrapMasterNodeName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfTrapMasterNodeName_Object = MibScalar
atAtmfTrapMasterNodeName = _AtAtmfTrapMasterNodeName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 2),
    _AtAtmfTrapMasterNodeName_Type()
)
atAtmfTrapMasterNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapMasterNodeName.setStatus("current")


class _AtAtmfTrapNetworkName_Type(DisplayStringUnsized):
    """Custom type atAtmfTrapNetworkName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AtAtmfTrapNetworkName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfTrapNetworkName_Object = MibScalar
atAtmfTrapNetworkName = _AtAtmfTrapNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 3),
    _AtAtmfTrapNetworkName_Type()
)
atAtmfTrapNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapNetworkName.setStatus("current")


class _AtAtmfTrapInterfaceName_Type(DisplayStringUnsized):
    """Custom type atAtmfTrapInterfaceName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AtAtmfTrapInterfaceName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfTrapInterfaceName_Object = MibScalar
atAtmfTrapInterfaceName = _AtAtmfTrapInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 4),
    _AtAtmfTrapInterfaceName_Type()
)
atAtmfTrapInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapInterfaceName.setStatus("current")


class _AtAtmfTrapBackupStatus_Type(Integer32):
    """Custom type atAtmfTrapBackupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AtAtmfTrapBackupStatus_Type.__name__ = "Integer32"
_AtAtmfTrapBackupStatus_Object = MibScalar
atAtmfTrapBackupStatus = _AtAtmfTrapBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 5),
    _AtAtmfTrapBackupStatus_Type()
)
atAtmfTrapBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapBackupStatus.setStatus("current")


class _AtAtmfTrapNodeStatusChange_Type(Integer32):
    """Custom type atAtmfTrapNodeStatusChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("joined", 2),
          ("left", 1))
    )


_AtAtmfTrapNodeStatusChange_Type.__name__ = "Integer32"
_AtAtmfTrapNodeStatusChange_Object = MibScalar
atAtmfTrapNodeStatusChange = _AtAtmfTrapNodeStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 6),
    _AtAtmfTrapNodeStatusChange_Type()
)
atAtmfTrapNodeStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapNodeStatusChange.setStatus("current")


class _AtAtmfTrapInterfaceStatusChange_Type(Integer32):
    """Custom type atAtmfTrapInterfaceStatusChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("forwarding", 2))
    )


_AtAtmfTrapInterfaceStatusChange_Type.__name__ = "Integer32"
_AtAtmfTrapInterfaceStatusChange_Object = MibScalar
atAtmfTrapInterfaceStatusChange = _AtAtmfTrapInterfaceStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 7),
    _AtAtmfTrapInterfaceStatusChange_Type()
)
atAtmfTrapInterfaceStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapInterfaceStatusChange.setStatus("current")


class _AtAtmfTrapNodeRecoveryStatus_Type(Integer32):
    """Custom type atAtmfTrapNodeRecoveryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AtAtmfTrapNodeRecoveryStatus_Type.__name__ = "Integer32"
_AtAtmfTrapNodeRecoveryStatus_Object = MibScalar
atAtmfTrapNodeRecoveryStatus = _AtAtmfTrapNodeRecoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 8),
    _AtAtmfTrapNodeRecoveryStatus_Type()
)
atAtmfTrapNodeRecoveryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapNodeRecoveryStatus.setStatus("current")


class _AtAtmfTrapMediaType_Type(DisplayStringUnsized):
    """Custom type atAtmfTrapMediaType based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AtAtmfTrapMediaType_Type.__name__ = "DisplayStringUnsized"
_AtAtmfTrapMediaType_Object = MibScalar
atAtmfTrapMediaType = _AtAtmfTrapMediaType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 9),
    _AtAtmfTrapMediaType_Type()
)
atAtmfTrapMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapMediaType.setStatus("current")
_AtAtmfTrapMediaTotal_Type = Integer32
_AtAtmfTrapMediaTotal_Object = MibScalar
atAtmfTrapMediaTotal = _AtAtmfTrapMediaTotal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 10),
    _AtAtmfTrapMediaTotal_Type()
)
atAtmfTrapMediaTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapMediaTotal.setStatus("current")
_AtAtmfTrapMediaFree_Type = Integer32
_AtAtmfTrapMediaFree_Object = MibScalar
atAtmfTrapMediaFree = _AtAtmfTrapMediaFree_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 11),
    _AtAtmfTrapMediaFree_Type()
)
atAtmfTrapMediaFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapMediaFree.setStatus("current")


class _AtAtmfTrapRollingRebootStatus_Type(Integer32):
    """Custom type atAtmfTrapRollingRebootStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AtAtmfTrapRollingRebootStatus_Type.__name__ = "Integer32"
_AtAtmfTrapRollingRebootStatus_Object = MibScalar
atAtmfTrapRollingRebootStatus = _AtAtmfTrapRollingRebootStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 12),
    _AtAtmfTrapRollingRebootStatus_Type()
)
atAtmfTrapRollingRebootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapRollingRebootStatus.setStatus("current")


class _AtAtmfTrapRollingRebootReleaseName_Type(DisplayStringUnsized):
    """Custom type atAtmfTrapRollingRebootReleaseName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AtAtmfTrapRollingRebootReleaseName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfTrapRollingRebootReleaseName_Object = MibScalar
atAtmfTrapRollingRebootReleaseName = _AtAtmfTrapRollingRebootReleaseName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 13),
    _AtAtmfTrapRollingRebootReleaseName_Type()
)
atAtmfTrapRollingRebootReleaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapRollingRebootReleaseName.setStatus("current")


class _AtAtmfTrapRollingRebootReleaseStatus_Type(Integer32):
    """Custom type atAtmfTrapRollingRebootReleaseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AtAtmfTrapRollingRebootReleaseStatus_Type.__name__ = "Integer32"
_AtAtmfTrapRollingRebootReleaseStatus_Object = MibScalar
atAtmfTrapRollingRebootReleaseStatus = _AtAtmfTrapRollingRebootReleaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 14),
    _AtAtmfTrapRollingRebootReleaseStatus_Type()
)
atAtmfTrapRollingRebootReleaseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapRollingRebootReleaseStatus.setStatus("current")
_AtAtmfSummary_ObjectIdentity = ObjectIdentity
atAtmfSummary = _AtAtmfSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2)
)


class _AtAtmfSummaryNodeName_Type(DisplayStringUnsized):
    """Custom type atAtmfSummaryNodeName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AtAtmfSummaryNodeName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfSummaryNodeName_Object = MibScalar
atAtmfSummaryNodeName = _AtAtmfSummaryNodeName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 1),
    _AtAtmfSummaryNodeName_Type()
)
atAtmfSummaryNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryNodeName.setStatus("current")


class _AtAtmfSummaryStatus_Type(Integer32):
    """Custom type atAtmfSummaryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AtAtmfSummaryStatus_Type.__name__ = "Integer32"
_AtAtmfSummaryStatus_Object = MibScalar
atAtmfSummaryStatus = _AtAtmfSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 2),
    _AtAtmfSummaryStatus_Type()
)
atAtmfSummaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryStatus.setStatus("current")


class _AtAtmfSummaryRole_Type(Integer32):
    """Custom type atAtmfSummaryRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("member", 1))
    )


_AtAtmfSummaryRole_Type.__name__ = "Integer32"
_AtAtmfSummaryRole_Object = MibScalar
atAtmfSummaryRole = _AtAtmfSummaryRole_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 3),
    _AtAtmfSummaryRole_Type()
)
atAtmfSummaryRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryRole.setStatus("current")


class _AtAtmfSummaryNetworkName_Type(DisplayStringUnsized):
    """Custom type atAtmfSummaryNetworkName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AtAtmfSummaryNetworkName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfSummaryNetworkName_Object = MibScalar
atAtmfSummaryNetworkName = _AtAtmfSummaryNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 4),
    _AtAtmfSummaryNetworkName_Type()
)
atAtmfSummaryNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryNetworkName.setStatus("current")


class _AtAtmfSummaryParentName_Type(DisplayStringUnsized):
    """Custom type atAtmfSummaryParentName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AtAtmfSummaryParentName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfSummaryParentName_Object = MibScalar
atAtmfSummaryParentName = _AtAtmfSummaryParentName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 5),
    _AtAtmfSummaryParentName_Type()
)
atAtmfSummaryParentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryParentName.setStatus("current")
_AtAtmfSummaryCoreDistance_Type = Integer32
_AtAtmfSummaryCoreDistance_Object = MibScalar
atAtmfSummaryCoreDistance = _AtAtmfSummaryCoreDistance_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 6),
    _AtAtmfSummaryCoreDistance_Type()
)
atAtmfSummaryCoreDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryCoreDistance.setStatus("current")
_AtAtmfSummaryDomainId_Type = Integer32
_AtAtmfSummaryDomainId_Object = MibScalar
atAtmfSummaryDomainId = _AtAtmfSummaryDomainId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 7),
    _AtAtmfSummaryDomainId_Type()
)
atAtmfSummaryDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryDomainId.setStatus("current")


class _AtAtmfSummaryRestrictedLogin_Type(Integer32):
    """Custom type atAtmfSummaryRestrictedLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AtAtmfSummaryRestrictedLogin_Type.__name__ = "Integer32"
_AtAtmfSummaryRestrictedLogin_Object = MibScalar
atAtmfSummaryRestrictedLogin = _AtAtmfSummaryRestrictedLogin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 8),
    _AtAtmfSummaryRestrictedLogin_Type()
)
atAtmfSummaryRestrictedLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryRestrictedLogin.setStatus("current")
_AtAtmfSummaryNodes_Type = Integer32
_AtAtmfSummaryNodes_Object = MibScalar
atAtmfSummaryNodes = _AtAtmfSummaryNodes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 9),
    _AtAtmfSummaryNodes_Type()
)
atAtmfSummaryNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryNodes.setStatus("current")
_AtAtmfNodeTable_Object = MibTable
atAtmfNodeTable = _AtAtmfNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 3)
)
if mibBuilder.loadTexts:
    atAtmfNodeTable.setStatus("current")
_AtAtmfNodeEntry_Object = MibTableRow
atAtmfNodeEntry = _AtAtmfNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 3, 1)
)
atAtmfNodeEntry.setIndexNames(
    (0, "AT-ATMF-MIB", "atAtmfNodeName"),
)
if mibBuilder.loadTexts:
    atAtmfNodeEntry.setStatus("current")


class _AtAtmfNodeName_Type(DisplayStringUnsized):
    """Custom type atAtmfNodeName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AtAtmfNodeName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfNodeName_Object = MibTableColumn
atAtmfNodeName = _AtAtmfNodeName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 3, 1, 1),
    _AtAtmfNodeName_Type()
)
atAtmfNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfNodeName.setStatus("current")

# Managed Objects groups


# Notification objects

atAtmfBackupStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 1)
)
atAtmfBackupStatusTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapMasterNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapBackupStatus"))
)
if mibBuilder.loadTexts:
    atAtmfBackupStatusTrap.setStatus(
        "current"
    )

atAtmfNodeStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 2)
)
atAtmfNodeStatusChangeTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapNodeStatusChange"),
        ("AT-ATMF-MIB", "atAtmfTrapNetworkName"))
)
if mibBuilder.loadTexts:
    atAtmfNodeStatusChangeTrap.setStatus(
        "current"
    )

atAtmfNodeRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 3)
)
atAtmfNodeRecoveryTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapMasterNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapNodeRecoveryStatus"))
)
if mibBuilder.loadTexts:
    atAtmfNodeRecoveryTrap.setStatus(
        "current"
    )

atAtmfInterfaceStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 4)
)
atAtmfInterfaceStatusChangeTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapInterfaceName"),
        ("AT-ATMF-MIB", "atAtmfTrapInterfaceStatusChange"))
)
if mibBuilder.loadTexts:
    atAtmfInterfaceStatusChangeTrap.setStatus(
        "current"
    )

atAtmfExternalMediaLowMemoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 5)
)
atAtmfExternalMediaLowMemoryTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapMasterNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapMediaType"),
        ("AT-ATMF-MIB", "atAtmfTrapMediaTotal"),
        ("AT-ATMF-MIB", "atAtmfTrapMediaFree"))
)
if mibBuilder.loadTexts:
    atAtmfExternalMediaLowMemoryTrap.setStatus(
        "current"
    )

atAtmfRollingRebootCompleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 6)
)
atAtmfRollingRebootCompleteTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapRollingRebootStatus"))
)
if mibBuilder.loadTexts:
    atAtmfRollingRebootCompleteTrap.setStatus(
        "current"
    )

atAtmfRollingRebootReleaseCompleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 7)
)
atAtmfRollingRebootReleaseCompleteTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapRollingRebootStatus"),
        ("AT-ATMF-MIB", "atAtmfTrapRollingRebootReleaseName"),
        ("AT-ATMF-MIB", "atAtmfTrapRollingRebootReleaseStatus"))
)
if mibBuilder.loadTexts:
    atAtmfRollingRebootReleaseCompleteTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-ATMF-MIB",
    **{"atmf": atmf,
       "atAtmfTraps": atAtmfTraps,
       "atAtmfBackupStatusTrap": atAtmfBackupStatusTrap,
       "atAtmfNodeStatusChangeTrap": atAtmfNodeStatusChangeTrap,
       "atAtmfNodeRecoveryTrap": atAtmfNodeRecoveryTrap,
       "atAtmfInterfaceStatusChangeTrap": atAtmfInterfaceStatusChangeTrap,
       "atAtmfExternalMediaLowMemoryTrap": atAtmfExternalMediaLowMemoryTrap,
       "atAtmfRollingRebootCompleteTrap": atAtmfRollingRebootCompleteTrap,
       "atAtmfRollingRebootReleaseCompleteTrap": atAtmfRollingRebootReleaseCompleteTrap,
       "atAtmfTrapVariable": atAtmfTrapVariable,
       "atAtmfTrapNodeName": atAtmfTrapNodeName,
       "atAtmfTrapMasterNodeName": atAtmfTrapMasterNodeName,
       "atAtmfTrapNetworkName": atAtmfTrapNetworkName,
       "atAtmfTrapInterfaceName": atAtmfTrapInterfaceName,
       "atAtmfTrapBackupStatus": atAtmfTrapBackupStatus,
       "atAtmfTrapNodeStatusChange": atAtmfTrapNodeStatusChange,
       "atAtmfTrapInterfaceStatusChange": atAtmfTrapInterfaceStatusChange,
       "atAtmfTrapNodeRecoveryStatus": atAtmfTrapNodeRecoveryStatus,
       "atAtmfTrapMediaType": atAtmfTrapMediaType,
       "atAtmfTrapMediaTotal": atAtmfTrapMediaTotal,
       "atAtmfTrapMediaFree": atAtmfTrapMediaFree,
       "atAtmfTrapRollingRebootStatus": atAtmfTrapRollingRebootStatus,
       "atAtmfTrapRollingRebootReleaseName": atAtmfTrapRollingRebootReleaseName,
       "atAtmfTrapRollingRebootReleaseStatus": atAtmfTrapRollingRebootReleaseStatus,
       "atAtmfSummary": atAtmfSummary,
       "atAtmfSummaryNodeName": atAtmfSummaryNodeName,
       "atAtmfSummaryStatus": atAtmfSummaryStatus,
       "atAtmfSummaryRole": atAtmfSummaryRole,
       "atAtmfSummaryNetworkName": atAtmfSummaryNetworkName,
       "atAtmfSummaryParentName": atAtmfSummaryParentName,
       "atAtmfSummaryCoreDistance": atAtmfSummaryCoreDistance,
       "atAtmfSummaryDomainId": atAtmfSummaryDomainId,
       "atAtmfSummaryRestrictedLogin": atAtmfSummaryRestrictedLogin,
       "atAtmfSummaryNodes": atAtmfSummaryNodes,
       "atAtmfNodeTable": atAtmfNodeTable,
       "atAtmfNodeEntry": atAtmfNodeEntry,
       "atAtmfNodeName": atAtmfNodeName}
)
