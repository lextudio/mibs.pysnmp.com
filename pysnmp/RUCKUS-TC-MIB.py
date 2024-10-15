# SNMP MIB module (RUCKUS-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:36 2024
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

(ruckusCommonTCModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCommonTCModule")

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

ruckusTCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RuckusRadioMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11Mixed", 3),
          ("ieee802dot11a", 4),
          ("ieee802dot11b", 1),
          ("ieee802dot11g", 2),
          ("ieee802dot11na", 6),
          ("ieee802dot11ng", 5))
    )



class RuckusWEPKey(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(26, 26),
    )



class RuckusAdminStatus(Integer32, TextualConvention):
    status = "current"
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



class RuckusCountryCode(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class RuckusFequency(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2412, 5805),
    )



class RuckusWPAPassPhrase(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
        ValueSizeConstraint(64, 64),
    )



class RuckusSSID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )



class RuckusRate(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )



class RuckusdB(Integer32, TextualConvention):
    status = "current"


class RuckusRateLimiting(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("rate100Kbps", 1),
          ("rate10Mbps", 7),
          ("rate1Mbps", 4),
          ("rate20Mbps", 8),
          ("rate250Kbps", 2),
          ("rate2Mbps", 5),
          ("rate500Kbps", 3),
          ("rate50Mbps", 9),
          ("rate5Mbps", 6))
    )



class RuckusWLANServiceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("guestAccess", 2),
          ("hotSpotService", 3),
          ("standardUsage", 1))
    )



class RuckusAuthenticationType(Integer32, TextualConvention):
    status = "current"
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
        *(("eap", 3),
          ("eap-mac-mix", 5),
          ("mac-address", 4),
          ("open", 1),
          ("shared", 2))
    )



class RuckusEncryptionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none-enc", 6),
          ("wep-128", 5),
          ("wep-64", 4),
          ("wpa", 1),
          ("wpa-Mixed", 3),
          ("wpa2", 2))
    )



class RuckusWPACipherType(Integer32, TextualConvention):
    status = "current"
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
        *(("aes", 2),
          ("auto", 3),
          ("none", 4),
          ("tkip", 1))
    )



class RuckusWLANServicePriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )



class RuckusSysLogLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical-only", 3),
          ("more", 1),
          ("warning-and-critical", 2))
    )



class RuckusSNMPv3AuthenticationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )



class RuckusSNMPv3EncryptionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes", 2),
          ("des", 1))
    )



class RuckusSNMPVersionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v2", 1),
          ("v3", 2))
    )



class RuckusNameString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )



class RuckusPassPhrase(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )



class RuckusAAAServiceType(Integer32, TextualConvention):
    status = "current"
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
        *(("aaa-accounting", 4),
          ("aaa-authentication", 3),
          ("active-directory", 1),
          ("ldap-directory", 2))
    )



class RuckusAPIpAddressSettingMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admin-by-ap", 3),
          ("admin-by-dhcp", 2),
          ("admin-by-zd", 1))
    )



class RuckusAPRadioType(Integer32, TextualConvention):
    status = "current"
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
        *(("ieee80211a", 3),
          ("ieee80211bg", 1),
          ("ieee80211n", 4),
          ("ieee80211na", 2))
    )



class RuckusAPRadioType24(Integer32, TextualConvention):
    status = "current"
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
        *(("ieee80211b", 1),
          ("ieee80211bg", 3),
          ("ieee80211g", 2),
          ("ieee80211ng", 4))
    )



class RuckusAPRadioType5(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee80211a", 1),
          ("ieee80211n", 2),
          ("ieee80211nag", 3))
    )



class RuckusAPRadioTxPowerLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("full", 2),
          ("half-full", 3),
          ("one-eighth-full", 5),
          ("one-tenth-full", 6),
          ("quarter-full", 4))
    )



class RuckusAPWirelessChannel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )



class RuckusAPMeshConfigurationMode(Integer32, TextualConvention):
    status = "current"
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
        *(("auto", 1),
          ("disabled", 4),
          ("mesh-ap", 3),
          ("root-ap", 2))
    )



class RuckusAPUplinkSelectionMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 2),
          ("smart", 1))
    )



class RuckusAPApproveMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("approved", 1),
          ("not-approved", 2))
    )



class RuckusZDAPManagementAdminControl(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("associated", 2),
          ("delete", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RuckusTCObjects_ObjectIdentity = ObjectIdentity
ruckusTCObjects = _RuckusTCObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 1)
)
_RuckusTCEvents_ObjectIdentity = ObjectIdentity
ruckusTCEvents = _RuckusTCEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 2)
)
_RuckusTCConf_ObjectIdentity = ObjectIdentity
ruckusTCConf = _RuckusTCConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 3)
)
_RuckusTCGroups_ObjectIdentity = ObjectIdentity
ruckusTCGroups = _RuckusTCGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 3, 1)
)
_RuckusTCCompls_ObjectIdentity = ObjectIdentity
ruckusTCCompls = _RuckusTCCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 1, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-TC-MIB",
    **{"RuckusRadioMode": RuckusRadioMode,
       "RuckusWEPKey": RuckusWEPKey,
       "RuckusAdminStatus": RuckusAdminStatus,
       "RuckusCountryCode": RuckusCountryCode,
       "RuckusFequency": RuckusFequency,
       "RuckusWPAPassPhrase": RuckusWPAPassPhrase,
       "RuckusSSID": RuckusSSID,
       "RuckusRate": RuckusRate,
       "RuckusdB": RuckusdB,
       "RuckusRateLimiting": RuckusRateLimiting,
       "RuckusWLANServiceType": RuckusWLANServiceType,
       "RuckusAuthenticationType": RuckusAuthenticationType,
       "RuckusEncryptionType": RuckusEncryptionType,
       "RuckusWPACipherType": RuckusWPACipherType,
       "RuckusWLANServicePriority": RuckusWLANServicePriority,
       "RuckusSysLogLevel": RuckusSysLogLevel,
       "RuckusSNMPv3AuthenticationType": RuckusSNMPv3AuthenticationType,
       "RuckusSNMPv3EncryptionType": RuckusSNMPv3EncryptionType,
       "RuckusSNMPVersionType": RuckusSNMPVersionType,
       "RuckusNameString": RuckusNameString,
       "RuckusPassPhrase": RuckusPassPhrase,
       "RuckusAAAServiceType": RuckusAAAServiceType,
       "RuckusAPIpAddressSettingMode": RuckusAPIpAddressSettingMode,
       "RuckusAPRadioType": RuckusAPRadioType,
       "RuckusAPRadioType24": RuckusAPRadioType24,
       "RuckusAPRadioType5": RuckusAPRadioType5,
       "RuckusAPRadioTxPowerLevel": RuckusAPRadioTxPowerLevel,
       "RuckusAPWirelessChannel": RuckusAPWirelessChannel,
       "RuckusAPMeshConfigurationMode": RuckusAPMeshConfigurationMode,
       "RuckusAPUplinkSelectionMode": RuckusAPUplinkSelectionMode,
       "RuckusAPApproveMode": RuckusAPApproveMode,
       "RuckusZDAPManagementAdminControl": RuckusZDAPManagementAdminControl,
       "ruckusTCMIB": ruckusTCMIB,
       "ruckusTCObjects": ruckusTCObjects,
       "ruckusTCEvents": ruckusTCEvents,
       "ruckusTCConf": ruckusTCConf,
       "ruckusTCGroups": ruckusTCGroups,
       "ruckusTCCompls": ruckusTCCompls}
)
