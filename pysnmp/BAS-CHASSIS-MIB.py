# SNMP MIB module (BAS-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:20 2024
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

(BasCardClass,
 BasChassisId,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 basChassisInfo) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasCardClass",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basChassisInfo")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

basChassisInfoMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasChassisObjects_ObjectIdentity = ObjectIdentity
basChassisObjects = _BasChassisObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1)
)
_BasChassisInfoTable_Object = MibTable
basChassisInfoTable = _BasChassisInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    basChassisInfoTable.setStatus("current")
_BasChassisInfoEntry_Object = MibTableRow
basChassisInfoEntry = _BasChassisInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1)
)
basChassisInfoEntry.setIndexNames(
    (0, "BAS-CHASSIS-MIB", "basChassisInfoChassis"),
    (0, "BAS-CHASSIS-MIB", "basChassisInfoSlot"),
    (0, "BAS-CHASSIS-MIB", "basChassisInfoIf"),
    (0, "BAS-CHASSIS-MIB", "basChassisInfoLPort"),
)
if mibBuilder.loadTexts:
    basChassisInfoEntry.setStatus("current")
_BasChassisInfoChassis_Type = BasChassisId
_BasChassisInfoChassis_Object = MibTableColumn
basChassisInfoChassis = _BasChassisInfoChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 1),
    _BasChassisInfoChassis_Type()
)
basChassisInfoChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisInfoChassis.setStatus("current")
_BasChassisInfoSlot_Type = BasSlotId
_BasChassisInfoSlot_Object = MibTableColumn
basChassisInfoSlot = _BasChassisInfoSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 2),
    _BasChassisInfoSlot_Type()
)
basChassisInfoSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisInfoSlot.setStatus("current")
_BasChassisInfoIf_Type = BasInterfaceId
_BasChassisInfoIf_Object = MibTableColumn
basChassisInfoIf = _BasChassisInfoIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 3),
    _BasChassisInfoIf_Type()
)
basChassisInfoIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisInfoIf.setStatus("current")
_BasChassisInfoLPort_Type = BasLogicalPortId
_BasChassisInfoLPort_Object = MibTableColumn
basChassisInfoLPort = _BasChassisInfoLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 4),
    _BasChassisInfoLPort_Type()
)
basChassisInfoLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisInfoLPort.setStatus("current")
_BasChassisInfoChassisId_Type = BasChassisId
_BasChassisInfoChassisId_Object = MibTableColumn
basChassisInfoChassisId = _BasChassisInfoChassisId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 5),
    _BasChassisInfoChassisId_Type()
)
basChassisInfoChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basChassisInfoChassisId.setStatus("current")
_BasChassisInfoClusterId_Type = Integer32
_BasChassisInfoClusterId_Object = MibTableColumn
basChassisInfoClusterId = _BasChassisInfoClusterId_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 6),
    _BasChassisInfoClusterId_Type()
)
basChassisInfoClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basChassisInfoClusterId.setStatus("current")
_BasChassisInfoLdapServerIpAddr_Type = IpAddress
_BasChassisInfoLdapServerIpAddr_Object = MibTableColumn
basChassisInfoLdapServerIpAddr = _BasChassisInfoLdapServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 7),
    _BasChassisInfoLdapServerIpAddr_Type()
)
basChassisInfoLdapServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basChassisInfoLdapServerIpAddr.setStatus("current")


class _BasChassisInfoLdapServerPort_Type(Integer32):
    """Custom type basChassisInfoLdapServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BasChassisInfoLdapServerPort_Type.__name__ = "Integer32"
_BasChassisInfoLdapServerPort_Object = MibTableColumn
basChassisInfoLdapServerPort = _BasChassisInfoLdapServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 8),
    _BasChassisInfoLdapServerPort_Type()
)
basChassisInfoLdapServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basChassisInfoLdapServerPort.setStatus("current")


class _BasChassisInfoLdapServerUserName_Type(OctetString):
    """Custom type basChassisInfoLdapServerUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BasChassisInfoLdapServerUserName_Type.__name__ = "OctetString"
_BasChassisInfoLdapServerUserName_Object = MibTableColumn
basChassisInfoLdapServerUserName = _BasChassisInfoLdapServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 9),
    _BasChassisInfoLdapServerUserName_Type()
)
basChassisInfoLdapServerUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basChassisInfoLdapServerUserName.setStatus("current")


class _BasChassisInfoLdapServerPassword_Type(OctetString):
    """Custom type basChassisInfoLdapServerPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BasChassisInfoLdapServerPassword_Type.__name__ = "OctetString"
_BasChassisInfoLdapServerPassword_Object = MibTableColumn
basChassisInfoLdapServerPassword = _BasChassisInfoLdapServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 10),
    _BasChassisInfoLdapServerPassword_Type()
)
basChassisInfoLdapServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basChassisInfoLdapServerPassword.setStatus("current")


class _BasChassisInfoLdapServerEnable_Type(Integer32):
    """Custom type basChassisInfoLdapServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_BasChassisInfoLdapServerEnable_Type.__name__ = "Integer32"
_BasChassisInfoLdapServerEnable_Object = MibTableColumn
basChassisInfoLdapServerEnable = _BasChassisInfoLdapServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 11),
    _BasChassisInfoLdapServerEnable_Type()
)
basChassisInfoLdapServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basChassisInfoLdapServerEnable.setStatus("current")


class _BasChassisIsProvisioningServer_Type(TruthValue):
    """Custom type basChassisIsProvisioningServer based on TruthValue"""


_BasChassisIsProvisioningServer_Object = MibTableColumn
basChassisIsProvisioningServer = _BasChassisIsProvisioningServer_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 12),
    _BasChassisIsProvisioningServer_Type()
)
basChassisIsProvisioningServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basChassisIsProvisioningServer.setStatus("current")


class _BasChassisIsProvServerOnThisChassis_Type(TruthValue):
    """Custom type basChassisIsProvServerOnThisChassis based on TruthValue"""


_BasChassisIsProvServerOnThisChassis_Object = MibTableColumn
basChassisIsProvServerOnThisChassis = _BasChassisIsProvServerOnThisChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 1, 1, 13),
    _BasChassisIsProvServerOnThisChassis_Type()
)
basChassisIsProvServerOnThisChassis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basChassisIsProvServerOnThisChassis.setStatus("current")
_BasChassisManagerTable_Object = MibTable
basChassisManagerTable = _BasChassisManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    basChassisManagerTable.setStatus("current")
_BasChassisManagerEntry_Object = MibTableRow
basChassisManagerEntry = _BasChassisManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1)
)
basChassisManagerEntry.setIndexNames(
    (0, "BAS-CHASSIS-MIB", "basChassisManagerChassis"),
    (0, "BAS-CHASSIS-MIB", "basChassisManagerSlot"),
    (0, "BAS-CHASSIS-MIB", "basChassisManagerIf"),
    (0, "BAS-CHASSIS-MIB", "basChassisManagerLPort"),
)
if mibBuilder.loadTexts:
    basChassisManagerEntry.setStatus("current")
_BasChassisManagerChassis_Type = BasChassisId
_BasChassisManagerChassis_Object = MibTableColumn
basChassisManagerChassis = _BasChassisManagerChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1, 1),
    _BasChassisManagerChassis_Type()
)
basChassisManagerChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisManagerChassis.setStatus("current")
_BasChassisManagerSlot_Type = BasSlotId
_BasChassisManagerSlot_Object = MibTableColumn
basChassisManagerSlot = _BasChassisManagerSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1, 2),
    _BasChassisManagerSlot_Type()
)
basChassisManagerSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisManagerSlot.setStatus("current")
_BasChassisManagerIf_Type = BasInterfaceId
_BasChassisManagerIf_Object = MibTableColumn
basChassisManagerIf = _BasChassisManagerIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1, 3),
    _BasChassisManagerIf_Type()
)
basChassisManagerIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisManagerIf.setStatus("current")
_BasChassisManagerLPort_Type = BasLogicalPortId
_BasChassisManagerLPort_Object = MibTableColumn
basChassisManagerLPort = _BasChassisManagerLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1, 4),
    _BasChassisManagerLPort_Type()
)
basChassisManagerLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisManagerLPort.setStatus("current")


class _BasChassisManagerAgentTcpPort_Type(Integer32):
    """Custom type basChassisManagerAgentTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BasChassisManagerAgentTcpPort_Type.__name__ = "Integer32"
_BasChassisManagerAgentTcpPort_Object = MibTableColumn
basChassisManagerAgentTcpPort = _BasChassisManagerAgentTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1, 5),
    _BasChassisManagerAgentTcpPort_Type()
)
basChassisManagerAgentTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basChassisManagerAgentTcpPort.setStatus("current")


class _BasChassisManagerPriority_Type(Integer32):
    """Custom type basChassisManagerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_BasChassisManagerPriority_Type.__name__ = "Integer32"
_BasChassisManagerPriority_Object = MibTableColumn
basChassisManagerPriority = _BasChassisManagerPriority_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1, 6),
    _BasChassisManagerPriority_Type()
)
basChassisManagerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basChassisManagerPriority.setStatus("current")


class _BasChassisManagerScope_Type(Integer32):
    """Custom type basChassisManagerScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bca", 1),
          ("ca", 2))
    )


_BasChassisManagerScope_Type.__name__ = "Integer32"
_BasChassisManagerScope_Object = MibTableColumn
basChassisManagerScope = _BasChassisManagerScope_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1, 7),
    _BasChassisManagerScope_Type()
)
basChassisManagerScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basChassisManagerScope.setStatus("current")
_BasChassisManagerDateAndTime_Type = DateAndTime
_BasChassisManagerDateAndTime_Object = MibTableColumn
basChassisManagerDateAndTime = _BasChassisManagerDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 1, 2, 1, 8),
    _BasChassisManagerDateAndTime_Type()
)
basChassisManagerDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basChassisManagerDateAndTime.setStatus("current")
_BasChassisDhcpRelayObjects_ObjectIdentity = ObjectIdentity
basChassisDhcpRelayObjects = _BasChassisDhcpRelayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2)
)
_BasChassisDhcpRelayServerTable_Object = MibTable
basChassisDhcpRelayServerTable = _BasChassisDhcpRelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    basChassisDhcpRelayServerTable.setStatus("current")
_BasChassisDhcpRelayServerEntry_Object = MibTableRow
basChassisDhcpRelayServerEntry = _BasChassisDhcpRelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1, 1)
)
basChassisDhcpRelayServerEntry.setIndexNames(
    (0, "BAS-CHASSIS-MIB", "basChassisDhcpRelayServerChassis"),
    (0, "BAS-CHASSIS-MIB", "basChassisDhcpRelayServerSlot"),
    (0, "BAS-CHASSIS-MIB", "basChassisDhcpRelayServerIf"),
    (0, "BAS-CHASSIS-MIB", "basChassisDhcpRelayServerLPort"),
    (0, "BAS-CHASSIS-MIB", "basChassisDhcpRelayServerAddress"),
    (0, "BAS-CHASSIS-MIB", "basChassisDhcpRelayServerType"),
)
if mibBuilder.loadTexts:
    basChassisDhcpRelayServerEntry.setStatus("current")
_BasChassisDhcpRelayServerChassis_Type = BasChassisId
_BasChassisDhcpRelayServerChassis_Object = MibTableColumn
basChassisDhcpRelayServerChassis = _BasChassisDhcpRelayServerChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1, 1, 1),
    _BasChassisDhcpRelayServerChassis_Type()
)
basChassisDhcpRelayServerChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisDhcpRelayServerChassis.setStatus("current")
_BasChassisDhcpRelayServerSlot_Type = BasSlotId
_BasChassisDhcpRelayServerSlot_Object = MibTableColumn
basChassisDhcpRelayServerSlot = _BasChassisDhcpRelayServerSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1, 1, 2),
    _BasChassisDhcpRelayServerSlot_Type()
)
basChassisDhcpRelayServerSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisDhcpRelayServerSlot.setStatus("current")
_BasChassisDhcpRelayServerIf_Type = BasInterfaceId
_BasChassisDhcpRelayServerIf_Object = MibTableColumn
basChassisDhcpRelayServerIf = _BasChassisDhcpRelayServerIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1, 1, 3),
    _BasChassisDhcpRelayServerIf_Type()
)
basChassisDhcpRelayServerIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisDhcpRelayServerIf.setStatus("current")
_BasChassisDhcpRelayServerLPort_Type = BasLogicalPortId
_BasChassisDhcpRelayServerLPort_Object = MibTableColumn
basChassisDhcpRelayServerLPort = _BasChassisDhcpRelayServerLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1, 1, 4),
    _BasChassisDhcpRelayServerLPort_Type()
)
basChassisDhcpRelayServerLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisDhcpRelayServerLPort.setStatus("current")


class _BasChassisDhcpRelayServerAddress_Type(IpAddress):
    """Custom type basChassisDhcpRelayServerAddress based on IpAddress"""
    defaultValue = 2


_BasChassisDhcpRelayServerAddress_Object = MibTableColumn
basChassisDhcpRelayServerAddress = _BasChassisDhcpRelayServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1, 1, 5),
    _BasChassisDhcpRelayServerAddress_Type()
)
basChassisDhcpRelayServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisDhcpRelayServerAddress.setStatus("current")


class _BasChassisDhcpRelayServerType_Type(Integer32):
    """Custom type basChassisDhcpRelayServerType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 2),
          ("cablemodem", 3),
          ("unauthorized", 1))
    )


_BasChassisDhcpRelayServerType_Type.__name__ = "Integer32"
_BasChassisDhcpRelayServerType_Object = MibTableColumn
basChassisDhcpRelayServerType = _BasChassisDhcpRelayServerType_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1, 1, 6),
    _BasChassisDhcpRelayServerType_Type()
)
basChassisDhcpRelayServerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basChassisDhcpRelayServerType.setStatus("current")


class _BasChassisDhcpRelayServerStatus_Type(RowStatus):
    """Custom type basChassisDhcpRelayServerStatus based on RowStatus"""
    defaultValue = 1


_BasChassisDhcpRelayServerStatus_Object = MibTableColumn
basChassisDhcpRelayServerStatus = _BasChassisDhcpRelayServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 1, 3, 1, 2, 1, 1, 7),
    _BasChassisDhcpRelayServerStatus_Type()
)
basChassisDhcpRelayServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basChassisDhcpRelayServerStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-CHASSIS-MIB",
    **{"basChassisInfoMib": basChassisInfoMib,
       "basChassisObjects": basChassisObjects,
       "basChassisInfoTable": basChassisInfoTable,
       "basChassisInfoEntry": basChassisInfoEntry,
       "basChassisInfoChassis": basChassisInfoChassis,
       "basChassisInfoSlot": basChassisInfoSlot,
       "basChassisInfoIf": basChassisInfoIf,
       "basChassisInfoLPort": basChassisInfoLPort,
       "basChassisInfoChassisId": basChassisInfoChassisId,
       "basChassisInfoClusterId": basChassisInfoClusterId,
       "basChassisInfoLdapServerIpAddr": basChassisInfoLdapServerIpAddr,
       "basChassisInfoLdapServerPort": basChassisInfoLdapServerPort,
       "basChassisInfoLdapServerUserName": basChassisInfoLdapServerUserName,
       "basChassisInfoLdapServerPassword": basChassisInfoLdapServerPassword,
       "basChassisInfoLdapServerEnable": basChassisInfoLdapServerEnable,
       "basChassisIsProvisioningServer": basChassisIsProvisioningServer,
       "basChassisIsProvServerOnThisChassis": basChassisIsProvServerOnThisChassis,
       "basChassisManagerTable": basChassisManagerTable,
       "basChassisManagerEntry": basChassisManagerEntry,
       "basChassisManagerChassis": basChassisManagerChassis,
       "basChassisManagerSlot": basChassisManagerSlot,
       "basChassisManagerIf": basChassisManagerIf,
       "basChassisManagerLPort": basChassisManagerLPort,
       "basChassisManagerAgentTcpPort": basChassisManagerAgentTcpPort,
       "basChassisManagerPriority": basChassisManagerPriority,
       "basChassisManagerScope": basChassisManagerScope,
       "basChassisManagerDateAndTime": basChassisManagerDateAndTime,
       "basChassisDhcpRelayObjects": basChassisDhcpRelayObjects,
       "basChassisDhcpRelayServerTable": basChassisDhcpRelayServerTable,
       "basChassisDhcpRelayServerEntry": basChassisDhcpRelayServerEntry,
       "basChassisDhcpRelayServerChassis": basChassisDhcpRelayServerChassis,
       "basChassisDhcpRelayServerSlot": basChassisDhcpRelayServerSlot,
       "basChassisDhcpRelayServerIf": basChassisDhcpRelayServerIf,
       "basChassisDhcpRelayServerLPort": basChassisDhcpRelayServerLPort,
       "basChassisDhcpRelayServerAddress": basChassisDhcpRelayServerAddress,
       "basChassisDhcpRelayServerType": basChassisDhcpRelayServerType,
       "basChassisDhcpRelayServerStatus": basChassisDhcpRelayServerStatus}
)
