# SNMP MIB module (ENTERASYS-PWA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-PWA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:24 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

etsysPwaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8)
)
etsysPwaMIB.setRevisions(
        ("2003-11-05 16:56",
         "2003-08-04 11:22",
         "2003-05-14 19:32",
         "2002-12-13 21:56",
         "2002-05-15 20:44",
         "2002-05-14 21:30",
         "2002-03-21 21:49",
         "2001-06-07 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysPwaSystem_ObjectIdentity = ObjectIdentity
etsysPwaSystem = _EtsysPwaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1)
)


class _EtsysPwaSystemAuthControl_Type(EnabledStatus):
    """Custom type etsysPwaSystemAuthControl based on EnabledStatus"""


_EtsysPwaSystemAuthControl_Object = MibScalar
etsysPwaSystemAuthControl = _EtsysPwaSystemAuthControl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 1),
    _EtsysPwaSystemAuthControl_Type()
)
etsysPwaSystemAuthControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaSystemAuthControl.setStatus("current")


class _EtsysPwaSystemAuthHostName_Type(DisplayString):
    """Custom type etsysPwaSystemAuthHostName based on DisplayString"""
    defaultValue = OctetString("secureharbour")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EtsysPwaSystemAuthHostName_Type.__name__ = "DisplayString"
_EtsysPwaSystemAuthHostName_Object = MibScalar
etsysPwaSystemAuthHostName = _EtsysPwaSystemAuthHostName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 2),
    _EtsysPwaSystemAuthHostName_Type()
)
etsysPwaSystemAuthHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaSystemAuthHostName.setStatus("current")


class _EtsysPwaSystemAuthBanner_Type(SnmpAdminString):
    """Custom type etsysPwaSystemAuthBanner based on SnmpAdminString"""
    defaultValue = OctetString("""\
Enterasys Networks Incorporated
              P.O. Box 5005
              Rochester, NH 03866-5005 USA
              603 337-9400""")


_EtsysPwaSystemAuthBanner_Object = MibScalar
etsysPwaSystemAuthBanner = _EtsysPwaSystemAuthBanner_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 3),
    _EtsysPwaSystemAuthBanner_Type()
)
etsysPwaSystemAuthBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaSystemAuthBanner.setStatus("current")


class _EtsysPwaSystemPwaNameServicesEnable_Type(EnabledStatus):
    """Custom type etsysPwaSystemPwaNameServicesEnable based on EnabledStatus"""


_EtsysPwaSystemPwaNameServicesEnable_Object = MibScalar
etsysPwaSystemPwaNameServicesEnable = _EtsysPwaSystemPwaNameServicesEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 4),
    _EtsysPwaSystemPwaNameServicesEnable_Type()
)
etsysPwaSystemPwaNameServicesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaSystemPwaNameServicesEnable.setStatus("current")
_EtsysPwaSystemAuthIPAddressType_Type = InetAddressType
_EtsysPwaSystemAuthIPAddressType_Object = MibScalar
etsysPwaSystemAuthIPAddressType = _EtsysPwaSystemAuthIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 5),
    _EtsysPwaSystemAuthIPAddressType_Type()
)
etsysPwaSystemAuthIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaSystemAuthIPAddressType.setStatus("deprecated")
_EtsysPwaSystemAuthIPAddress_Type = IpAddress
_EtsysPwaSystemAuthIPAddress_Object = MibScalar
etsysPwaSystemAuthIPAddress = _EtsysPwaSystemAuthIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 6),
    _EtsysPwaSystemAuthIPAddress_Type()
)
etsysPwaSystemAuthIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaSystemAuthIPAddress.setStatus("deprecated")


class _EtsysPwaSystemAuthProtocol_Type(Integer32):
    """Custom type etsysPwaSystemAuthProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("pap", 2))
    )


_EtsysPwaSystemAuthProtocol_Type.__name__ = "Integer32"
_EtsysPwaSystemAuthProtocol_Object = MibScalar
etsysPwaSystemAuthProtocol = _EtsysPwaSystemAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 7),
    _EtsysPwaSystemAuthProtocol_Type()
)
etsysPwaSystemAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaSystemAuthProtocol.setStatus("current")
_EtsysPwaSystemAuthDomain_Type = SnmpAdminString
_EtsysPwaSystemAuthDomain_Object = MibScalar
etsysPwaSystemAuthDomain = _EtsysPwaSystemAuthDomain_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 8),
    _EtsysPwaSystemAuthDomain_Type()
)
etsysPwaSystemAuthDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaSystemAuthDomain.setStatus("current")
_EtsysPwaSystemAuthInetAddressType_Type = InetAddressType
_EtsysPwaSystemAuthInetAddressType_Object = MibScalar
etsysPwaSystemAuthInetAddressType = _EtsysPwaSystemAuthInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 9),
    _EtsysPwaSystemAuthInetAddressType_Type()
)
etsysPwaSystemAuthInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaSystemAuthInetAddressType.setStatus("current")
_EtsysPwaSystemAuthInetAddress_Type = InetAddress
_EtsysPwaSystemAuthInetAddress_Object = MibScalar
etsysPwaSystemAuthInetAddress = _EtsysPwaSystemAuthInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 10),
    _EtsysPwaSystemAuthInetAddress_Type()
)
etsysPwaSystemAuthInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaSystemAuthInetAddress.setStatus("current")


class _EtsysPwaSystemAuthEnhancedMode_Type(EnabledStatus):
    """Custom type etsysPwaSystemAuthEnhancedMode based on EnabledStatus"""


_EtsysPwaSystemAuthEnhancedMode_Object = MibScalar
etsysPwaSystemAuthEnhancedMode = _EtsysPwaSystemAuthEnhancedMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 11),
    _EtsysPwaSystemAuthEnhancedMode_Type()
)
etsysPwaSystemAuthEnhancedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaSystemAuthEnhancedMode.setStatus("current")


class _EtsysPwaLogoDisplayStatus_Type(EnabledStatus):
    """Custom type etsysPwaLogoDisplayStatus based on EnabledStatus"""


_EtsysPwaLogoDisplayStatus_Object = MibScalar
etsysPwaLogoDisplayStatus = _EtsysPwaLogoDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 12),
    _EtsysPwaLogoDisplayStatus_Type()
)
etsysPwaLogoDisplayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaLogoDisplayStatus.setStatus("current")


class _EtsysPwaSystemGuestUsername_Type(DisplayString):
    """Custom type etsysPwaSystemGuestUsername based on DisplayString"""
    defaultValue = OctetString("guest")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EtsysPwaSystemGuestUsername_Type.__name__ = "DisplayString"
_EtsysPwaSystemGuestUsername_Object = MibScalar
etsysPwaSystemGuestUsername = _EtsysPwaSystemGuestUsername_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 13),
    _EtsysPwaSystemGuestUsername_Type()
)
etsysPwaSystemGuestUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaSystemGuestUsername.setStatus("current")


class _EtsysPwaSystemGuestPassword_Type(DisplayString):
    """Custom type etsysPwaSystemGuestPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EtsysPwaSystemGuestPassword_Type.__name__ = "DisplayString"
_EtsysPwaSystemGuestPassword_Object = MibScalar
etsysPwaSystemGuestPassword = _EtsysPwaSystemGuestPassword_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 14),
    _EtsysPwaSystemGuestPassword_Type()
)
etsysPwaSystemGuestPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaSystemGuestPassword.setStatus("current")


class _EtsysPwaSystemGuestPasswordValid_Type(TruthValue):
    """Custom type etsysPwaSystemGuestPasswordValid based on TruthValue"""


_EtsysPwaSystemGuestPasswordValid_Object = MibScalar
etsysPwaSystemGuestPasswordValid = _EtsysPwaSystemGuestPasswordValid_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 15),
    _EtsysPwaSystemGuestPasswordValid_Type()
)
etsysPwaSystemGuestPasswordValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaSystemGuestPasswordValid.setStatus("current")


class _EtsysPwaSystemGuestNetworkingStatus_Type(Integer32):
    """Custom type etsysPwaSystemGuestNetworkingStatus based on Integer32"""
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
        *(("authNone", 2),
          ("authRadius", 3),
          ("disabled", 1))
    )


_EtsysPwaSystemGuestNetworkingStatus_Type.__name__ = "Integer32"
_EtsysPwaSystemGuestNetworkingStatus_Object = MibScalar
etsysPwaSystemGuestNetworkingStatus = _EtsysPwaSystemGuestNetworkingStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 16),
    _EtsysPwaSystemGuestNetworkingStatus_Type()
)
etsysPwaSystemGuestNetworkingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaSystemGuestNetworkingStatus.setStatus("current")


class _EtsysPwaSystemEnhancedModeRefreshTime_Type(Integer32):
    """Custom type etsysPwaSystemEnhancedModeRefreshTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_EtsysPwaSystemEnhancedModeRefreshTime_Type.__name__ = "Integer32"
_EtsysPwaSystemEnhancedModeRefreshTime_Object = MibScalar
etsysPwaSystemEnhancedModeRefreshTime = _EtsysPwaSystemEnhancedModeRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 1, 17),
    _EtsysPwaSystemEnhancedModeRefreshTime_Type()
)
etsysPwaSystemEnhancedModeRefreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaSystemEnhancedModeRefreshTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysPwaSystemEnhancedModeRefreshTime.setUnits("seconds")
_EtsysPwaPortConfiguration_ObjectIdentity = ObjectIdentity
etsysPwaPortConfiguration = _EtsysPwaPortConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 2)
)
_EtsysPwaPortConfigurationTable_Object = MibTable
etsysPwaPortConfigurationTable = _EtsysPwaPortConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    etsysPwaPortConfigurationTable.setStatus("current")
_EtsysPwaPortConfigurationEntry_Object = MibTableRow
etsysPwaPortConfigurationEntry = _EtsysPwaPortConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 2, 1, 1)
)
etsysPwaPortConfigurationEntry.setIndexNames(
    (0, "ENTERASYS-PWA-MIB", "etsysPwaPortNumber"),
)
if mibBuilder.loadTexts:
    etsysPwaPortConfigurationEntry.setStatus("current")
_EtsysPwaPortNumber_Type = InterfaceIndex
_EtsysPwaPortNumber_Object = MibTableColumn
etsysPwaPortNumber = _EtsysPwaPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 2, 1, 1, 1),
    _EtsysPwaPortNumber_Type()
)
etsysPwaPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysPwaPortNumber.setStatus("current")
_EtsysPwaInitializePort_Type = TruthValue
_EtsysPwaInitializePort_Object = MibTableColumn
etsysPwaInitializePort = _EtsysPwaInitializePort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 2, 1, 1, 2),
    _EtsysPwaInitializePort_Type()
)
etsysPwaInitializePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaInitializePort.setStatus("current")


class _EtsysPwaAuthQuietPeriod_Type(Integer32):
    """Custom type etsysPwaAuthQuietPeriod based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EtsysPwaAuthQuietPeriod_Type.__name__ = "Integer32"
_EtsysPwaAuthQuietPeriod_Object = MibTableColumn
etsysPwaAuthQuietPeriod = _EtsysPwaAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 2, 1, 1, 3),
    _EtsysPwaAuthQuietPeriod_Type()
)
etsysPwaAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaAuthQuietPeriod.setStatus("current")
if mibBuilder.loadTexts:
    etsysPwaAuthQuietPeriod.setUnits("seconds")


class _EtsysPwaAuthMaxReq_Type(Integer32):
    """Custom type etsysPwaAuthMaxReq based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EtsysPwaAuthMaxReq_Type.__name__ = "Integer32"
_EtsysPwaAuthMaxReq_Object = MibTableColumn
etsysPwaAuthMaxReq = _EtsysPwaAuthMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 2, 1, 1, 4),
    _EtsysPwaAuthMaxReq_Type()
)
etsysPwaAuthMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaAuthMaxReq.setStatus("current")


class _EtsysPwaControlledPortControl_Type(Integer32):
    """Custom type etsysPwaControlledPortControl based on Integer32"""
    defaultValue = 3

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
        *(("auto", 2),
          ("forceAuthorized", 3),
          ("forceUnauthorized", 1),
          ("promiscousAuto", 4))
    )


_EtsysPwaControlledPortControl_Type.__name__ = "Integer32"
_EtsysPwaControlledPortControl_Object = MibTableColumn
etsysPwaControlledPortControl = _EtsysPwaControlledPortControl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 2, 1, 1, 5),
    _EtsysPwaControlledPortControl_Type()
)
etsysPwaControlledPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysPwaControlledPortControl.setStatus("current")
_EtsysPwaPortStatus_ObjectIdentity = ObjectIdentity
etsysPwaPortStatus = _EtsysPwaPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 3)
)
_EtsysPwaAuthStatusTable_Object = MibTable
etsysPwaAuthStatusTable = _EtsysPwaAuthStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 3, 1)
)
if mibBuilder.loadTexts:
    etsysPwaAuthStatusTable.setStatus("current")
_EtsysPwaAuthStatusEntry_Object = MibTableRow
etsysPwaAuthStatusEntry = _EtsysPwaAuthStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 3, 1, 1)
)
etsysPwaAuthStatusEntry.setIndexNames(
    (0, "ENTERASYS-PWA-MIB", "etsysPwaPortNumber"),
)
if mibBuilder.loadTexts:
    etsysPwaAuthStatusEntry.setStatus("current")


class _EtsysPwaAuthPwaState_Type(Integer32):
    """Custom type etsysPwaAuthPwaState based on Integer32"""
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
        *(("authenticated", 3),
          ("authenticating", 2),
          ("disconnected", 1),
          ("held", 4))
    )


_EtsysPwaAuthPwaState_Type.__name__ = "Integer32"
_EtsysPwaAuthPwaState_Object = MibTableColumn
etsysPwaAuthPwaState = _EtsysPwaAuthPwaState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 3, 1, 1, 1),
    _EtsysPwaAuthPwaState_Type()
)
etsysPwaAuthPwaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthPwaState.setStatus("current")
_EtsysPwaMaxFailedAttempts_Type = ZeroBasedCounter32
_EtsysPwaMaxFailedAttempts_Object = MibTableColumn
etsysPwaMaxFailedAttempts = _EtsysPwaMaxFailedAttempts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 3, 1, 1, 2),
    _EtsysPwaMaxFailedAttempts_Type()
)
etsysPwaMaxFailedAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaMaxFailedAttempts.setStatus("current")
_EtsysPwaFailedAttemptsSinceLogon_Type = ZeroBasedCounter32
_EtsysPwaFailedAttemptsSinceLogon_Object = MibTableColumn
etsysPwaFailedAttemptsSinceLogon = _EtsysPwaFailedAttemptsSinceLogon_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 3, 1, 1, 3),
    _EtsysPwaFailedAttemptsSinceLogon_Type()
)
etsysPwaFailedAttemptsSinceLogon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaFailedAttemptsSinceLogon.setStatus("current")
_EtsysPwaLastLogonResult_Type = SnmpAdminString
_EtsysPwaLastLogonResult_Object = MibTableColumn
etsysPwaLastLogonResult = _EtsysPwaLastLogonResult_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 3, 1, 1, 4),
    _EtsysPwaLastLogonResult_Type()
)
etsysPwaLastLogonResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaLastLogonResult.setStatus("current")
_EtsysPwaSession_ObjectIdentity = ObjectIdentity
etsysPwaSession = _EtsysPwaSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4)
)
_EtsysPwaAuthSessionStatsTable_Object = MibTable
etsysPwaAuthSessionStatsTable = _EtsysPwaAuthSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 1)
)
if mibBuilder.loadTexts:
    etsysPwaAuthSessionStatsTable.setStatus("current")
_EtsysPwaAuthSessionStatsEntry_Object = MibTableRow
etsysPwaAuthSessionStatsEntry = _EtsysPwaAuthSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 1, 1)
)
etsysPwaAuthSessionStatsEntry.setIndexNames(
    (0, "ENTERASYS-PWA-MIB", "etsysPwaPortNumber"),
    (0, "ENTERASYS-PWA-MIB", "etsysPwaAuthSessionID"),
)
if mibBuilder.loadTexts:
    etsysPwaAuthSessionStatsEntry.setStatus("current")
_EtsysPwaAuthSessionID_Type = Integer32
_EtsysPwaAuthSessionID_Object = MibTableColumn
etsysPwaAuthSessionID = _EtsysPwaAuthSessionID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 1, 1, 1),
    _EtsysPwaAuthSessionID_Type()
)
etsysPwaAuthSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionID.setStatus("current")
_EtsysPwaAuthSessionOctetsRx_Type = Counter32
_EtsysPwaAuthSessionOctetsRx_Object = MibTableColumn
etsysPwaAuthSessionOctetsRx = _EtsysPwaAuthSessionOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 1, 1, 2),
    _EtsysPwaAuthSessionOctetsRx_Type()
)
etsysPwaAuthSessionOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionOctetsRx.setStatus("current")
_EtsysPwaAuthSessionOctetsRxOverflow_Type = Counter32
_EtsysPwaAuthSessionOctetsRxOverflow_Object = MibTableColumn
etsysPwaAuthSessionOctetsRxOverflow = _EtsysPwaAuthSessionOctetsRxOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 1, 1, 3),
    _EtsysPwaAuthSessionOctetsRxOverflow_Type()
)
etsysPwaAuthSessionOctetsRxOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionOctetsRxOverflow.setStatus("current")
_EtsysPwaAuthSessionOctetsTx_Type = Counter32
_EtsysPwaAuthSessionOctetsTx_Object = MibTableColumn
etsysPwaAuthSessionOctetsTx = _EtsysPwaAuthSessionOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 1, 1, 4),
    _EtsysPwaAuthSessionOctetsTx_Type()
)
etsysPwaAuthSessionOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionOctetsTx.setStatus("current")
_EtsysPwaAuthSessionOctetsTxOverflow_Type = Counter32
_EtsysPwaAuthSessionOctetsTxOverflow_Object = MibTableColumn
etsysPwaAuthSessionOctetsTxOverflow = _EtsysPwaAuthSessionOctetsTxOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 1, 1, 5),
    _EtsysPwaAuthSessionOctetsTxOverflow_Type()
)
etsysPwaAuthSessionOctetsTxOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionOctetsTxOverflow.setStatus("current")
_EtsysPwaAuthSessionFramesRx_Type = Counter32
_EtsysPwaAuthSessionFramesRx_Object = MibTableColumn
etsysPwaAuthSessionFramesRx = _EtsysPwaAuthSessionFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 1, 1, 6),
    _EtsysPwaAuthSessionFramesRx_Type()
)
etsysPwaAuthSessionFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionFramesRx.setStatus("current")
_EtsysPwaAuthSessionFramesTx_Type = Counter32
_EtsysPwaAuthSessionFramesTx_Object = MibTableColumn
etsysPwaAuthSessionFramesTx = _EtsysPwaAuthSessionFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 1, 1, 7),
    _EtsysPwaAuthSessionFramesTx_Type()
)
etsysPwaAuthSessionFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionFramesTx.setStatus("current")
_EtsysPwaAuthSessionStartTime_Type = TimeStamp
_EtsysPwaAuthSessionStartTime_Object = MibTableColumn
etsysPwaAuthSessionStartTime = _EtsysPwaAuthSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 1, 1, 8),
    _EtsysPwaAuthSessionStartTime_Type()
)
etsysPwaAuthSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionStartTime.setStatus("current")
_EtsysPwaAuthSessionDuration_Type = TimeInterval
_EtsysPwaAuthSessionDuration_Object = MibTableColumn
etsysPwaAuthSessionDuration = _EtsysPwaAuthSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 1, 1, 9),
    _EtsysPwaAuthSessionDuration_Type()
)
etsysPwaAuthSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionDuration.setStatus("current")


class _EtsysPwaAuthSessionTerminateCause_Type(Integer32):
    """Custom type etsysPwaAuthSessionTerminateCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              999)
        )
    )
    namedValues = NamedValues(
        *(("authControlForceUnauth", 3),
          ("linkDown", 1),
          ("logoff", 2),
          ("notTerminatedYet", 999),
          ("portDisabled", 5),
          ("portReInit", 4))
    )


_EtsysPwaAuthSessionTerminateCause_Type.__name__ = "Integer32"
_EtsysPwaAuthSessionTerminateCause_Object = MibTableColumn
etsysPwaAuthSessionTerminateCause = _EtsysPwaAuthSessionTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 1, 1, 10),
    _EtsysPwaAuthSessionTerminateCause_Type()
)
etsysPwaAuthSessionTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionTerminateCause.setStatus("current")
_EtsysPwaAuthSessionMacAddress_Type = MacAddress
_EtsysPwaAuthSessionMacAddress_Object = MibTableColumn
etsysPwaAuthSessionMacAddress = _EtsysPwaAuthSessionMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 1, 1, 11),
    _EtsysPwaAuthSessionMacAddress_Type()
)
etsysPwaAuthSessionMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionMacAddress.setStatus("current")
_EtsysPwaAuthSessionIPAddressType_Type = InetAddressType
_EtsysPwaAuthSessionIPAddressType_Object = MibTableColumn
etsysPwaAuthSessionIPAddressType = _EtsysPwaAuthSessionIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 1, 1, 12),
    _EtsysPwaAuthSessionIPAddressType_Type()
)
etsysPwaAuthSessionIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionIPAddressType.setStatus("current")
_EtsysPwaAuthSessionIPAddress_Type = InetAddress
_EtsysPwaAuthSessionIPAddress_Object = MibTableColumn
etsysPwaAuthSessionIPAddress = _EtsysPwaAuthSessionIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 1, 1, 13),
    _EtsysPwaAuthSessionIPAddress_Type()
)
etsysPwaAuthSessionIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionIPAddress.setStatus("current")
_EtsysPwaAuthSessionUserName_Type = SnmpAdminString
_EtsysPwaAuthSessionUserName_Object = MibTableColumn
etsysPwaAuthSessionUserName = _EtsysPwaAuthSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 1, 1, 14),
    _EtsysPwaAuthSessionUserName_Type()
)
etsysPwaAuthSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionUserName.setStatus("current")
_EtsysPwaAuthSessionStatsHCTable_Object = MibTable
etsysPwaAuthSessionStatsHCTable = _EtsysPwaAuthSessionStatsHCTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 2)
)
if mibBuilder.loadTexts:
    etsysPwaAuthSessionStatsHCTable.setStatus("current")
_EtsysPwaAuthSessionStatsHCEntry_Object = MibTableRow
etsysPwaAuthSessionStatsHCEntry = _EtsysPwaAuthSessionStatsHCEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 2, 1)
)
etsysPwaAuthSessionStatsHCEntry.setIndexNames(
    (0, "ENTERASYS-PWA-MIB", "etsysPwaPortNumber"),
    (0, "ENTERASYS-PWA-MIB", "etsysPwaAuthSessionHCID"),
)
if mibBuilder.loadTexts:
    etsysPwaAuthSessionStatsHCEntry.setStatus("current")
_EtsysPwaAuthSessionHCID_Type = Integer32
_EtsysPwaAuthSessionHCID_Object = MibTableColumn
etsysPwaAuthSessionHCID = _EtsysPwaAuthSessionHCID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 2, 1, 1),
    _EtsysPwaAuthSessionHCID_Type()
)
etsysPwaAuthSessionHCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionHCID.setStatus("current")
_EtsysPwaAuthSessionOctetsRxHc_Type = Counter64
_EtsysPwaAuthSessionOctetsRxHc_Object = MibTableColumn
etsysPwaAuthSessionOctetsRxHc = _EtsysPwaAuthSessionOctetsRxHc_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 2, 1, 2),
    _EtsysPwaAuthSessionOctetsRxHc_Type()
)
etsysPwaAuthSessionOctetsRxHc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionOctetsRxHc.setStatus("current")
_EtsysPwaAuthSessionOctetsTxHc_Type = Counter64
_EtsysPwaAuthSessionOctetsTxHc_Object = MibTableColumn
etsysPwaAuthSessionOctetsTxHc = _EtsysPwaAuthSessionOctetsTxHc_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 4, 2, 1, 3),
    _EtsysPwaAuthSessionOctetsTxHc_Type()
)
etsysPwaAuthSessionOctetsTxHc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysPwaAuthSessionOctetsTxHc.setStatus("current")
_EtsysPwaMIBGroups_ObjectIdentity = ObjectIdentity
etsysPwaMIBGroups = _EtsysPwaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 5)
)
_EtsysPwaMIBCompliances_ObjectIdentity = ObjectIdentity
etsysPwaMIBCompliances = _EtsysPwaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 6)
)

# Managed Objects groups

etsysPwaSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 5, 1)
)
etsysPwaSystemGroup.setObjects(
      *(("ENTERASYS-PWA-MIB", "etsysPwaSystemAuthControl"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemAuthHostName"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemAuthBanner"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemPwaNameServicesEnable"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemAuthIPAddressType"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemAuthIPAddress"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemAuthProtocol"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemAuthDomain"))
)
if mibBuilder.loadTexts:
    etsysPwaSystemGroup.setStatus("deprecated")

etsysPwaPortConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 5, 2)
)
etsysPwaPortConfigurationGroup.setObjects(
      *(("ENTERASYS-PWA-MIB", "etsysPwaInitializePort"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthQuietPeriod"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthMaxReq"),
        ("ENTERASYS-PWA-MIB", "etsysPwaControlledPortControl"))
)
if mibBuilder.loadTexts:
    etsysPwaPortConfigurationGroup.setStatus("current")

etsysPwaPortStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 5, 3)
)
etsysPwaPortStatusGroup.setObjects(
      *(("ENTERASYS-PWA-MIB", "etsysPwaAuthPwaState"),
        ("ENTERASYS-PWA-MIB", "etsysPwaMaxFailedAttempts"),
        ("ENTERASYS-PWA-MIB", "etsysPwaFailedAttemptsSinceLogon"),
        ("ENTERASYS-PWA-MIB", "etsysPwaLastLogonResult"))
)
if mibBuilder.loadTexts:
    etsysPwaPortStatusGroup.setStatus("current")

etsysPwaSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 5, 4)
)
etsysPwaSessionGroup.setObjects(
      *(("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionID"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionOctetsRx"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionOctetsRxOverflow"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionOctetsTx"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionOctetsTxOverflow"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionFramesRx"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionFramesTx"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionStartTime"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionDuration"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionTerminateCause"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionMacAddress"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionIPAddressType"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionIPAddress"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionUserName"))
)
if mibBuilder.loadTexts:
    etsysPwaSessionGroup.setStatus("current")

etsysPwaSessionHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 5, 5)
)
etsysPwaSessionHCGroup.setObjects(
      *(("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionHCID"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionOctetsRxHc"),
        ("ENTERASYS-PWA-MIB", "etsysPwaAuthSessionOctetsTxHc"))
)
if mibBuilder.loadTexts:
    etsysPwaSessionHCGroup.setStatus("current")

etsysPwaSystemGroupI = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 5, 6)
)
etsysPwaSystemGroupI.setObjects(
      *(("ENTERASYS-PWA-MIB", "etsysPwaSystemAuthControl"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemAuthHostName"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemAuthBanner"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemPwaNameServicesEnable"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemAuthProtocol"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemAuthDomain"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemAuthInetAddressType"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemAuthInetAddress"),
        ("ENTERASYS-PWA-MIB", "etsysPwaLogoDisplayStatus"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemGuestUsername"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemGuestPassword"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemGuestPasswordValid"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemGuestNetworkingStatus"),
        ("ENTERASYS-PWA-MIB", "etsysPwaSystemEnhancedModeRefreshTime"))
)
if mibBuilder.loadTexts:
    etsysPwaSystemGroupI.setStatus("current")

etsysPwaSystemAuthEnhancedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 5, 7)
)
etsysPwaSystemAuthEnhancedGroup.setObjects(
    ("ENTERASYS-PWA-MIB", "etsysPwaSystemAuthEnhancedMode")
)
if mibBuilder.loadTexts:
    etsysPwaSystemAuthEnhancedGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysPwaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 6, 1)
)
if mibBuilder.loadTexts:
    etsysPwaMIBCompliance.setStatus(
        "deprecated"
    )

etsysPwaMIBComplianceI = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 8, 6, 2)
)
if mibBuilder.loadTexts:
    etsysPwaMIBComplianceI.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-PWA-MIB",
    **{"etsysPwaMIB": etsysPwaMIB,
       "etsysPwaSystem": etsysPwaSystem,
       "etsysPwaSystemAuthControl": etsysPwaSystemAuthControl,
       "etsysPwaSystemAuthHostName": etsysPwaSystemAuthHostName,
       "etsysPwaSystemAuthBanner": etsysPwaSystemAuthBanner,
       "etsysPwaSystemPwaNameServicesEnable": etsysPwaSystemPwaNameServicesEnable,
       "etsysPwaSystemAuthIPAddressType": etsysPwaSystemAuthIPAddressType,
       "etsysPwaSystemAuthIPAddress": etsysPwaSystemAuthIPAddress,
       "etsysPwaSystemAuthProtocol": etsysPwaSystemAuthProtocol,
       "etsysPwaSystemAuthDomain": etsysPwaSystemAuthDomain,
       "etsysPwaSystemAuthInetAddressType": etsysPwaSystemAuthInetAddressType,
       "etsysPwaSystemAuthInetAddress": etsysPwaSystemAuthInetAddress,
       "etsysPwaSystemAuthEnhancedMode": etsysPwaSystemAuthEnhancedMode,
       "etsysPwaLogoDisplayStatus": etsysPwaLogoDisplayStatus,
       "etsysPwaSystemGuestUsername": etsysPwaSystemGuestUsername,
       "etsysPwaSystemGuestPassword": etsysPwaSystemGuestPassword,
       "etsysPwaSystemGuestPasswordValid": etsysPwaSystemGuestPasswordValid,
       "etsysPwaSystemGuestNetworkingStatus": etsysPwaSystemGuestNetworkingStatus,
       "etsysPwaSystemEnhancedModeRefreshTime": etsysPwaSystemEnhancedModeRefreshTime,
       "etsysPwaPortConfiguration": etsysPwaPortConfiguration,
       "etsysPwaPortConfigurationTable": etsysPwaPortConfigurationTable,
       "etsysPwaPortConfigurationEntry": etsysPwaPortConfigurationEntry,
       "etsysPwaPortNumber": etsysPwaPortNumber,
       "etsysPwaInitializePort": etsysPwaInitializePort,
       "etsysPwaAuthQuietPeriod": etsysPwaAuthQuietPeriod,
       "etsysPwaAuthMaxReq": etsysPwaAuthMaxReq,
       "etsysPwaControlledPortControl": etsysPwaControlledPortControl,
       "etsysPwaPortStatus": etsysPwaPortStatus,
       "etsysPwaAuthStatusTable": etsysPwaAuthStatusTable,
       "etsysPwaAuthStatusEntry": etsysPwaAuthStatusEntry,
       "etsysPwaAuthPwaState": etsysPwaAuthPwaState,
       "etsysPwaMaxFailedAttempts": etsysPwaMaxFailedAttempts,
       "etsysPwaFailedAttemptsSinceLogon": etsysPwaFailedAttemptsSinceLogon,
       "etsysPwaLastLogonResult": etsysPwaLastLogonResult,
       "etsysPwaSession": etsysPwaSession,
       "etsysPwaAuthSessionStatsTable": etsysPwaAuthSessionStatsTable,
       "etsysPwaAuthSessionStatsEntry": etsysPwaAuthSessionStatsEntry,
       "etsysPwaAuthSessionID": etsysPwaAuthSessionID,
       "etsysPwaAuthSessionOctetsRx": etsysPwaAuthSessionOctetsRx,
       "etsysPwaAuthSessionOctetsRxOverflow": etsysPwaAuthSessionOctetsRxOverflow,
       "etsysPwaAuthSessionOctetsTx": etsysPwaAuthSessionOctetsTx,
       "etsysPwaAuthSessionOctetsTxOverflow": etsysPwaAuthSessionOctetsTxOverflow,
       "etsysPwaAuthSessionFramesRx": etsysPwaAuthSessionFramesRx,
       "etsysPwaAuthSessionFramesTx": etsysPwaAuthSessionFramesTx,
       "etsysPwaAuthSessionStartTime": etsysPwaAuthSessionStartTime,
       "etsysPwaAuthSessionDuration": etsysPwaAuthSessionDuration,
       "etsysPwaAuthSessionTerminateCause": etsysPwaAuthSessionTerminateCause,
       "etsysPwaAuthSessionMacAddress": etsysPwaAuthSessionMacAddress,
       "etsysPwaAuthSessionIPAddressType": etsysPwaAuthSessionIPAddressType,
       "etsysPwaAuthSessionIPAddress": etsysPwaAuthSessionIPAddress,
       "etsysPwaAuthSessionUserName": etsysPwaAuthSessionUserName,
       "etsysPwaAuthSessionStatsHCTable": etsysPwaAuthSessionStatsHCTable,
       "etsysPwaAuthSessionStatsHCEntry": etsysPwaAuthSessionStatsHCEntry,
       "etsysPwaAuthSessionHCID": etsysPwaAuthSessionHCID,
       "etsysPwaAuthSessionOctetsRxHc": etsysPwaAuthSessionOctetsRxHc,
       "etsysPwaAuthSessionOctetsTxHc": etsysPwaAuthSessionOctetsTxHc,
       "etsysPwaMIBGroups": etsysPwaMIBGroups,
       "etsysPwaSystemGroup": etsysPwaSystemGroup,
       "etsysPwaPortConfigurationGroup": etsysPwaPortConfigurationGroup,
       "etsysPwaPortStatusGroup": etsysPwaPortStatusGroup,
       "etsysPwaSessionGroup": etsysPwaSessionGroup,
       "etsysPwaSessionHCGroup": etsysPwaSessionHCGroup,
       "etsysPwaSystemGroupI": etsysPwaSystemGroupI,
       "etsysPwaSystemAuthEnhancedGroup": etsysPwaSystemAuthEnhancedGroup,
       "etsysPwaMIBCompliances": etsysPwaMIBCompliances,
       "etsysPwaMIBCompliance": etsysPwaMIBCompliance,
       "etsysPwaMIBComplianceI": etsysPwaMIBComplianceI}
)
