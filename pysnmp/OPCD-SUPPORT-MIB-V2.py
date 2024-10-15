# SNMP MIB module (OPCD-SUPPORT-MIB-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPCD-SUPPORT-MIB-V2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:13 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

opencode_systems = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30374)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ocsupport_ObjectIdentity = ObjectIdentity
ocsupport = _Ocsupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 3)
)
_Ocsupport_traps_ObjectIdentity = ObjectIdentity
ocsupport_traps = _Ocsupport_traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1)
)
_Definitions_ObjectIdentity = ObjectIdentity
definitions = _Definitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0)
)
_Vars_ObjectIdentity = ObjectIdentity
vars = _Vars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 1)
)


class _Mcr_Host_Type(DisplayString):
    """Custom type mcr_Host based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Mcr_Host_Type.__name__ = "DisplayString"
_Mcr_Host_Object = MibScalar
mcr_Host = _Mcr_Host_Object(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 1, 1),
    _Mcr_Host_Type()
)
mcr_Host.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mcr_Host.setStatus("current")


class _Mcr_Severity_Type(Integer32):
    """Custom type mcr_Severity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("normal", 4),
          ("warning", 5))
    )


_Mcr_Severity_Type.__name__ = "Integer32"
_Mcr_Severity_Object = MibScalar
mcr_Severity = _Mcr_Severity_Object(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 1, 2),
    _Mcr_Severity_Type()
)
mcr_Severity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mcr_Severity.setStatus("mandatory")


class _Mcr_Text_Type(DisplayString):
    """Custom type mcr_Text based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Mcr_Text_Type.__name__ = "DisplayString"
_Mcr_Text_Object = MibScalar
mcr_Text = _Mcr_Text_Object(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 1, 3),
    _Mcr_Text_Type()
)
mcr_Text.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mcr_Text.setStatus("current")

# Managed Objects groups


# Notification objects

mcr_FAN = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 2)
)
mcr_FAN.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_FAN.setStatus(
        "current"
    )

mcr_FAN_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 3)
)
mcr_FAN_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_FAN_Canceled.setStatus(
        "current"
    )

mcr_POWER = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 4)
)
mcr_POWER.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_POWER.setStatus(
        "current"
    )

mcr_POWER_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 5)
)
mcr_POWER_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_POWER_Canceled.setStatus(
        "current"
    )

mcr_TEMPERATURE = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 6)
)
mcr_TEMPERATURE.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_TEMPERATURE.setStatus(
        "current"
    )

mcr_TEMPERATURE_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 7)
)
mcr_TEMPERATURE_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_TEMPERATURE_Canceled.setStatus(
        "current"
    )

mcr_HddFreeSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 8)
)
mcr_HddFreeSpace.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_HddFreeSpace.setStatus(
        "current"
    )

mcr_HddFreeSpace_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 9)
)
mcr_HddFreeSpace_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_HddFreeSpace_Canceled.setStatus(
        "current"
    )

mcr_MysqlService = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 10)
)
mcr_MysqlService.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_MysqlService.setStatus(
        "current"
    )

mcr_MysqlService_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 11)
)
mcr_MysqlService_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_MysqlService_Canceled.setStatus(
        "current"
    )

mcr_DbFloatingIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 12)
)
mcr_DbFloatingIp.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_DbFloatingIp.setStatus(
        "current"
    )

mcr_DbFloatingIp_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 13)
)
mcr_DbFloatingIp_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_DbFloatingIp_Canceled.setStatus(
        "current"
    )

mcr_FailedEth = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 14)
)
mcr_FailedEth.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_FailedEth.setStatus(
        "current"
    )

mcr_FailedEth_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 15)
)
mcr_FailedEth_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_FailedEth_Canceled.setStatus(
        "current"
    )

mcr_UpsStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 16)
)
mcr_UpsStatus.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_UpsStatus.setStatus(
        "current"
    )

mcr_UpsStatus_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 17)
)
mcr_UpsStatus_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_UpsStatus_Canceled.setStatus(
        "current"
    )

mcr_SwitchConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 18)
)
mcr_SwitchConnection.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_SwitchConnection.setStatus(
        "current"
    )

mcr_SwitchConnection_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 19)
)
mcr_SwitchConnection_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_SwitchConnection_Canceled.setStatus(
        "current"
    )

mcr_HddBayCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 20)
)
mcr_HddBayCheck.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_HddBayCheck.setStatus(
        "current"
    )

mcr_HddBayCheck_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 21)
)
mcr_HddBayCheck_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_HddBayCheck_Canceled.setStatus(
        "current"
    )

ss7LinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 22)
)
ss7LinkDown.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ss7LinkDown.setStatus(
        "current"
    )

ss7LinkDown_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 23)
)
ss7LinkDown_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ss7LinkDown_Canceled.setStatus(
        "current"
    )

ussdb_RunSlave = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 24)
)
ussdb_RunSlave.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ussdb_RunSlave.setStatus(
        "current"
    )

ussdb_RunSlave_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 25)
)
ussdb_RunSlave_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ussdb_RunSlave_Canceled.setStatus(
        "current"
    )

ussdb_HeartbeatDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 26)
)
ussdb_HeartbeatDown.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ussdb_HeartbeatDown.setStatus(
        "current"
    )

ussdb_HeartbeatDown_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 27)
)
ussdb_HeartbeatDown_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ussdb_HeartbeatDown_Canceled.setStatus(
        "current"
    )

ussdb_ConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 28)
)
ussdb_ConnectionDown.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ussdb_ConnectionDown.setStatus(
        "current"
    )

ussdb_ConnectionDown_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 29)
)
ussdb_ConnectionDown_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ussdb_ConnectionDown_Canceled.setStatus(
        "current"
    )

ussdb_Switched = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 30)
)
ussdb_Switched.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ussdb_Switched.setStatus(
        "current"
    )

ussdb_Switched_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 31)
)
ussdb_Switched_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ussdb_Switched_Canceled.setStatus(
        "current"
    )

ussdb_AppDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 32)
)
ussdb_AppDown.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ussdb_AppDown.setStatus(
        "current"
    )

ussdb_AppDown_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 33)
)
ussdb_AppDown_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ussdb_AppDown_Canceled.setStatus(
        "current"
    )

ussdb_DbDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 34)
)
ussdb_DbDown.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ussdb_DbDown.setStatus(
        "current"
    )

ussdb_DbDown_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 35)
)
ussdb_DbDown_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    ussdb_DbDown_Canceled.setStatus(
        "current"
    )

mcr_DBbackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 36)
)
mcr_DBbackup.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_DBbackup.setStatus(
        "current"
    )

mcr_DBbackup_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 37)
)
mcr_DBbackup_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_DBbackup_Canceled.setStatus(
        "current"
    )

voicetrunks = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 38)
)
voicetrunks.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    voicetrunks.setStatus(
        "current"
    )

voicetrunks_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 39)
)
voicetrunks_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    voicetrunks_Canceled.setStatus(
        "current"
    )

nodedown = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 40)
)
nodedown.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    nodedown.setStatus(
        "current"
    )

nodedown_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 41)
)
nodedown_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    nodedown_Canceled.setStatus(
        "current"
    )

test = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 42)
)
test.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    test.setStatus(
        "current"
    )

test_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 43)
)
test_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    test_Canceled.setStatus(
        "current"
    )

mcr_MSA2012_Problem = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 44)
)
mcr_MSA2012_Problem.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_MSA2012_Problem.setStatus(
        "current"
    )

mcr_MSA2012_Problem_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 45)
)
mcr_MSA2012_Problem_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_MSA2012_Problem_Canceled.setStatus(
        "current"
    )

mcr_TEMPERATURE_CUST = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 46)
)
mcr_TEMPERATURE_CUST.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_TEMPERATURE_CUST.setStatus(
        "current"
    )

mcr_TEMPERATURE_CUST_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 47)
)
mcr_TEMPERATURE_CUST_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_TEMPERATURE_CUST_Canceled.setStatus(
        "current"
    )

mcr_DBReplication = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 48)
)
mcr_DBReplication.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_DBReplication.setStatus(
        "current"
    )

mcr_DBReplication_Canceled = NotificationType(
    (1, 3, 6, 1, 4, 1, 30374, 3, 1, 0, 49)
)
mcr_DBReplication_Canceled.setObjects(
      *(("OPCD-SUPPORT-MIB-V2", "mcr_Host"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Severity"),
        ("OPCD-SUPPORT-MIB-V2", "mcr_Text"))
)
if mibBuilder.loadTexts:
    mcr_DBReplication_Canceled.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPCD-SUPPORT-MIB-V2",
    **{"opencode-systems": opencode_systems,
       "ocsupport": ocsupport,
       "ocsupport-traps": ocsupport_traps,
       "definitions": definitions,
       "mcr-FAN": mcr_FAN,
       "mcr-FAN-Canceled": mcr_FAN_Canceled,
       "mcr-POWER": mcr_POWER,
       "mcr-POWER-Canceled": mcr_POWER_Canceled,
       "mcr-TEMPERATURE": mcr_TEMPERATURE,
       "mcr-TEMPERATURE-Canceled": mcr_TEMPERATURE_Canceled,
       "mcr-HddFreeSpace": mcr_HddFreeSpace,
       "mcr-HddFreeSpace-Canceled": mcr_HddFreeSpace_Canceled,
       "mcr-MysqlService": mcr_MysqlService,
       "mcr-MysqlService-Canceled": mcr_MysqlService_Canceled,
       "mcr-DbFloatingIp": mcr_DbFloatingIp,
       "mcr-DbFloatingIp-Canceled": mcr_DbFloatingIp_Canceled,
       "mcr-FailedEth": mcr_FailedEth,
       "mcr-FailedEth-Canceled": mcr_FailedEth_Canceled,
       "mcr-UpsStatus": mcr_UpsStatus,
       "mcr-UpsStatus-Canceled": mcr_UpsStatus_Canceled,
       "mcr-SwitchConnection": mcr_SwitchConnection,
       "mcr-SwitchConnection-Canceled": mcr_SwitchConnection_Canceled,
       "mcr-HddBayCheck": mcr_HddBayCheck,
       "mcr-HddBayCheck-Canceled": mcr_HddBayCheck_Canceled,
       "ss7LinkDown": ss7LinkDown,
       "ss7LinkDown-Canceled": ss7LinkDown_Canceled,
       "ussdb-RunSlave": ussdb_RunSlave,
       "ussdb-RunSlave-Canceled": ussdb_RunSlave_Canceled,
       "ussdb-HeartbeatDown": ussdb_HeartbeatDown,
       "ussdb-HeartbeatDown-Canceled": ussdb_HeartbeatDown_Canceled,
       "ussdb-ConnectionDown": ussdb_ConnectionDown,
       "ussdb-ConnectionDown-Canceled": ussdb_ConnectionDown_Canceled,
       "ussdb-Switched": ussdb_Switched,
       "ussdb-Switched-Canceled": ussdb_Switched_Canceled,
       "ussdb-AppDown": ussdb_AppDown,
       "ussdb-AppDown-Canceled": ussdb_AppDown_Canceled,
       "ussdb-DbDown": ussdb_DbDown,
       "ussdb-DbDown-Canceled": ussdb_DbDown_Canceled,
       "mcr-DBbackup": mcr_DBbackup,
       "mcr-DBbackup-Canceled": mcr_DBbackup_Canceled,
       "voicetrunks": voicetrunks,
       "voicetrunks-Canceled": voicetrunks_Canceled,
       "nodedown": nodedown,
       "nodedown-Canceled": nodedown_Canceled,
       "test": test,
       "test-Canceled": test_Canceled,
       "mcr-MSA2012-Problem": mcr_MSA2012_Problem,
       "mcr-MSA2012-Problem-Canceled": mcr_MSA2012_Problem_Canceled,
       "mcr-TEMPERATURE-CUST": mcr_TEMPERATURE_CUST,
       "mcr-TEMPERATURE-CUST-Canceled": mcr_TEMPERATURE_CUST_Canceled,
       "mcr-DBReplication": mcr_DBReplication,
       "mcr-DBReplication-Canceled": mcr_DBReplication_Canceled,
       "vars": vars,
       "mcr-Host": mcr_Host,
       "mcr-Severity": mcr_Severity,
       "mcr-Text": mcr_Text}
)
