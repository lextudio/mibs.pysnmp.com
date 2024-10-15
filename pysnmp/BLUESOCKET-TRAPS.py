# SNMP MIB module (BLUESOCKET-TRAPS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLUESOCKET-TRAPS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:27 2024
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

(blueSocket,) = mibBuilder.importSymbols(
    "BLUESOCKET-ROOT",
    "blueSocket")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BlueNotification_ObjectIdentity = ObjectIdentity
blueNotification = _BlueNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2)
)
_NotifyObjects_ObjectIdentity = ObjectIdentity
notifyObjects = _NotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 1)
)


class _NtyobjLevel_Type(OctetString):
    """Custom type ntyobjLevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_NtyobjLevel_Type.__name__ = "OctetString"
_NtyobjLevel_Object = MibScalar
ntyobjLevel = _NtyobjLevel_Object(
    (1, 3, 6, 1, 4, 1, 9967, 2, 1, 1),
    _NtyobjLevel_Type()
)
ntyobjLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntyobjLevel.setStatus("current")


class _NtyobjName_Type(OctetString):
    """Custom type ntyobjName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NtyobjName_Type.__name__ = "OctetString"
_NtyobjName_Object = MibScalar
ntyobjName = _NtyobjName_Object(
    (1, 3, 6, 1, 4, 1, 9967, 2, 1, 2),
    _NtyobjName_Type()
)
ntyobjName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntyobjName.setStatus("current")


class _NtyobjDesc_Type(OctetString):
    """Custom type ntyobjDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtyobjDesc_Type.__name__ = "OctetString"
_NtyobjDesc_Object = MibScalar
ntyobjDesc = _NtyobjDesc_Object(
    (1, 3, 6, 1, 4, 1, 9967, 2, 1, 3),
    _NtyobjDesc_Type()
)
ntyobjDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntyobjDesc.setStatus("current")
_NtyobjOID_Type = ObjectIdentifier
_NtyobjOID_Object = MibScalar
ntyobjOID = _NtyobjOID_Object(
    (1, 3, 6, 1, 4, 1, 9967, 2, 1, 4),
    _NtyobjOID_Type()
)
ntyobjOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntyobjOID.setStatus("current")


class _NtyobjValue_Type(OctetString):
    """Custom type ntyobjValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtyobjValue_Type.__name__ = "OctetString"
_NtyobjValue_Object = MibScalar
ntyobjValue = _NtyobjValue_Object(
    (1, 3, 6, 1, 4, 1, 9967, 2, 1, 5),
    _NtyobjValue_Type()
)
ntyobjValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntyobjValue.setStatus("current")
_BlueTraps_ObjectIdentity = ObjectIdentity
blueTraps = _BlueTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2)
)
_BlueConfigTraps_ObjectIdentity = ObjectIdentity
blueConfigTraps = _BlueConfigTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1)
)
_BlueConfigTraps0_ObjectIdentity = ObjectIdentity
blueConfigTraps0 = _BlueConfigTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0)
)
_BlueFailureTraps_ObjectIdentity = ObjectIdentity
blueFailureTraps = _BlueFailureTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 2)
)
_BlueFailureTraps0_ObjectIdentity = ObjectIdentity
blueFailureTraps0 = _BlueFailureTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 2, 0)
)
_BlueThresholdTraps_ObjectIdentity = ObjectIdentity
blueThresholdTraps = _BlueThresholdTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 3)
)
_BlueThresholdTraps0_ObjectIdentity = ObjectIdentity
blueThresholdTraps0 = _BlueThresholdTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 3, 0)
)
_BlueGeneralTraps_ObjectIdentity = ObjectIdentity
blueGeneralTraps = _BlueGeneralTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 4)
)
_BlueGeneralTraps0_ObjectIdentity = ObjectIdentity
blueGeneralTraps0 = _BlueGeneralTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 4, 0)
)

# Managed Objects groups


# Notification objects

cctSystemConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 1)
)
cctSystemConfChange.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctSystemConfChange.setStatus(
        "current"
    )

cctUserConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 2)
)
cctUserConfChange.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctUserConfChange.setStatus(
        "current"
    )

cctExternalServConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 3)
)
cctExternalServConfChange.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctExternalServConfChange.setStatus(
        "current"
    )

cctRoleConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 4)
)
cctRoleConfChange.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctRoleConfChange.setStatus(
        "current"
    )

cctDestinationConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 5)
)
cctDestinationConfChange.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctDestinationConfChange.setStatus(
        "current"
    )

cctServiceConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 6)
)
cctServiceConfChange.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctServiceConfChange.setStatus(
        "current"
    )

cctNetworkConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 7)
)
cctNetworkConfChange.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctNetworkConfChange.setStatus(
        "current"
    )

cctVpnConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 8)
)
cctVpnConfChange.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctVpnConfChange.setStatus(
        "current"
    )

cctMobilityConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 9)
)
cctMobilityConfChange.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctMobilityConfChange.setStatus(
        "current"
    )

cctProcessConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 1, 0, 10)
)
cctProcessConfChange.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    cctProcessConfChange.setStatus(
        "current"
    )

btSysGeneralFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 2, 0, 1)
)
btSysGeneralFailure.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btSysGeneralFailure.setStatus(
        "current"
    )

btUserLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 2, 0, 2)
)
btUserLoginFailure.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btUserLoginFailure.setStatus(
        "current"
    )

btProcessFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 2, 0, 3)
)
btProcessFailure.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btProcessFailure.setStatus(
        "current"
    )

btAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 2, 0, 4)
)
btAuthFailure.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btAuthFailure.setStatus(
        "current"
    )

btSystemFailover = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 2, 0, 5)
)
btSystemFailover.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btSystemFailover.setStatus(
        "current"
    )

btConditionalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 3, 0, 1)
)
btConditionalEvent.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjOID"),
        ("BLUESOCKET-TRAPS", "ntyobjValue"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btConditionalEvent.setStatus(
        "current"
    )

btCpuLoadEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 3, 0, 2)
)
btCpuLoadEvent.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjOID"),
        ("BLUESOCKET-TRAPS", "ntyobjValue"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btCpuLoadEvent.setStatus(
        "current"
    )

btMemSwapUsageEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 3, 0, 3)
)
btMemSwapUsageEvent.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjOID"),
        ("BLUESOCKET-TRAPS", "ntyobjValue"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btMemSwapUsageEvent.setStatus(
        "current"
    )

btDiskUsageEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 3, 0, 4)
)
btDiskUsageEvent.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjOID"),
        ("BLUESOCKET-TRAPS", "ntyobjValue"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btDiskUsageEvent.setStatus(
        "current"
    )

btLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 4, 0, 1)
)
btLinkUp.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btLinkUp.setStatus(
        "current"
    )

btLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 4, 0, 2)
)
btLinkDown.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btLinkDown.setStatus(
        "current"
    )

btSystemGeneralTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9967, 2, 2, 4, 0, 3)
)
btSystemGeneralTrap.setObjects(
      *(("BLUESOCKET-TRAPS", "ntyobjLevel"),
        ("BLUESOCKET-TRAPS", "ntyobjName"),
        ("BLUESOCKET-TRAPS", "ntyobjDesc"))
)
if mibBuilder.loadTexts:
    btSystemGeneralTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUESOCKET-TRAPS",
    **{"blueNotification": blueNotification,
       "notifyObjects": notifyObjects,
       "ntyobjLevel": ntyobjLevel,
       "ntyobjName": ntyobjName,
       "ntyobjDesc": ntyobjDesc,
       "ntyobjOID": ntyobjOID,
       "ntyobjValue": ntyobjValue,
       "blueTraps": blueTraps,
       "blueConfigTraps": blueConfigTraps,
       "blueConfigTraps0": blueConfigTraps0,
       "cctSystemConfChange": cctSystemConfChange,
       "cctUserConfChange": cctUserConfChange,
       "cctExternalServConfChange": cctExternalServConfChange,
       "cctRoleConfChange": cctRoleConfChange,
       "cctDestinationConfChange": cctDestinationConfChange,
       "cctServiceConfChange": cctServiceConfChange,
       "cctNetworkConfChange": cctNetworkConfChange,
       "cctVpnConfChange": cctVpnConfChange,
       "cctMobilityConfChange": cctMobilityConfChange,
       "cctProcessConfChange": cctProcessConfChange,
       "blueFailureTraps": blueFailureTraps,
       "blueFailureTraps0": blueFailureTraps0,
       "btSysGeneralFailure": btSysGeneralFailure,
       "btUserLoginFailure": btUserLoginFailure,
       "btProcessFailure": btProcessFailure,
       "btAuthFailure": btAuthFailure,
       "btSystemFailover": btSystemFailover,
       "blueThresholdTraps": blueThresholdTraps,
       "blueThresholdTraps0": blueThresholdTraps0,
       "btConditionalEvent": btConditionalEvent,
       "btCpuLoadEvent": btCpuLoadEvent,
       "btMemSwapUsageEvent": btMemSwapUsageEvent,
       "btDiskUsageEvent": btDiskUsageEvent,
       "blueGeneralTraps": blueGeneralTraps,
       "blueGeneralTraps0": blueGeneralTraps0,
       "btLinkUp": btLinkUp,
       "btLinkDown": btLinkDown,
       "btSystemGeneralTrap": btSystemGeneralTrap}
)
