# SNMP MIB module (AVAYA-WLAN-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVAYA-WLAN-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:38 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(avayaWlanMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "avayaWlanMibs")


# MODULE-IDENTITY

avayaWlanTcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 7, 1)
)
avayaWlanTcMib.setRevisions(
        ("2011-12-15 00:00",
         "2011-11-21 00:00",
         "2011-10-11 00:00",
         "2011-07-23 00:00",
         "2011-01-07 00:00",
         "2010-06-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AvWlanDomainRole(Integer32, TextualConvention):
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
        *(("activeMdc", 1),
          ("backupMdc", 2),
          ("peerWc", 3),
          ("standalone", 4))
    )



class AvWlanControllerModel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("wc8180", 1)
    )



class AvWlanSwitchModel(Integer32, TextualConvention):
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
        *(("ers8800", 3),
          ("wc8180", 1),
          ("wsp8180", 2))
    )



class AvWlanNumberAPsPerWC(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )



class AvWlanAPModel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ap8120", 2),
          ("ap8120-E", 3),
          ("ap8120-O", 4))
    )



class AvWlanAPModelOrNone(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ap8120", 2),
          ("ap8120-E", 3),
          ("ap8120-O", 4),
          ("none", 255))
    )



class AvWlanAPStatus(Integer32, TextualConvention):
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
        *(("knownForeign", 5),
          ("managed", 1),
          ("rogue", 4),
          ("standalone", 3),
          ("unknown", 2))
    )



class AvWlanRadioChannel(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
        ValueRangeConstraint(34, 34),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(38, 38),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(46, 46),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(149, 149),
        ValueRangeConstraint(153, 153),
        ValueRangeConstraint(157, 157),
        ValueRangeConstraint(161, 161),
        ValueRangeConstraint(165, 165),
        ValueRangeConstraint(184, 184),
        ValueRangeConstraint(188, 188),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(196, 196),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(204, 204),
        ValueRangeConstraint(208, 208),
        ValueRangeConstraint(212, 212),
        ValueRangeConstraint(216, 216),
    )



class AvWlanRadioChannelOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
        ValueRangeConstraint(34, 34),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(38, 38),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(46, 46),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(149, 149),
        ValueRangeConstraint(153, 153),
        ValueRangeConstraint(157, 157),
        ValueRangeConstraint(161, 161),
        ValueRangeConstraint(165, 165),
        ValueRangeConstraint(184, 184),
        ValueRangeConstraint(188, 188),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(196, 196),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(204, 204),
        ValueRangeConstraint(208, 208),
        ValueRangeConstraint(212, 212),
        ValueRangeConstraint(216, 216),
    )



class AvWlanRadioPower(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class AvWlanRadioAntenna(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("wl81AT070E6", 2),
          ("wl81AT180E6", 4))
    )



class AvWlanRadioAntennaOrNone(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 255),
          ("wl81AT070E6", 2),
          ("wl81AT180E6", 4))
    )



class AvWlanRadioExtCable(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ft10", 2),
          ("ft3", 1))
    )



class AvWlanRadioExtCableOrNone(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ft10", 2),
          ("ft3", 1),
          ("none", 255))
    )



class AvWlanRadioOperationMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accessWids", 1),
          ("widsWips", 2))
    )



class AvWlanRadioInterface(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )



class AvWlanRadioInterfaceOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )



class AvWlanDataRateSet(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class AvWlanChannelSet(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class AvWlanRPTimeOfDay(OctetString, TextualConvention):
    status = "current"
    displayHint = "255t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class AvWlanOui(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class AvWlanTspecSuppAccessCategory(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("video", 2),
          ("voice", 1))
    )



class AvWlanConfigSyncComponents(Bits, TextualConvention):
    status = "current"


class AvWlanAPLicenseCapacity(Integer32, TextualConvention):
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
        *(("none", 1),
          ("sixteenLocked", 2),
          ("unlimited", 3))
    )



class AvWlanLogMsgLevel(Integer32, TextualConvention):
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
        *(("critical", 1),
          ("informational", 3),
          ("none", 4),
          ("serious", 2))
    )



class AvWlanCountryCode(SnmpAdminString, TextualConvention):
    status = "current"
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
    )



class AvWlanImageFileOrNone(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("account", 2),
          ("all", 1),
          ("background", 4),
          ("brand", 3),
          ("logout", 5),
          ("none", 255),
          ("pkgfile", 6))
    )



class AvWlanFileUpdateStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("fileNotFound", 6),
          ("fileProcFailed", 5),
          ("inProgress", 4),
          ("internalError", 7),
          ("maxFileSizeExceed", 11),
          ("maxProfileSizeExceed", 12),
          ("noSuchController", 10),
          ("noSuchLocale", 9),
          ("noSuchProfile", 8),
          ("none", 1),
          ("success", 2),
          ("transferFailed", 3))
    )



class AvWlanPacketCaptureFilterMask(Bits, TextualConvention):
    status = "current"


class AvWlanLoadBalanceMetric(Integer32, TextualConvention):
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
        *(("alternate", 2),
          ("cbfs", 4),
          ("leastLoad", 3),
          ("preferred", 1))
    )



class AvWlanMobVlanRole(Integer32, TextualConvention):
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
        *(("dynamicClient", 3),
          ("none", 4),
          ("server", 1),
          ("staticClient", 2))
    )



class AvWlanMobVlanState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )



class AvWlanSwitchNotifAuxLimitsMap(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVAYA-WLAN-TC-MIB",
    **{"AvWlanDomainRole": AvWlanDomainRole,
       "AvWlanControllerModel": AvWlanControllerModel,
       "AvWlanSwitchModel": AvWlanSwitchModel,
       "AvWlanNumberAPsPerWC": AvWlanNumberAPsPerWC,
       "AvWlanAPModel": AvWlanAPModel,
       "AvWlanAPModelOrNone": AvWlanAPModelOrNone,
       "AvWlanAPStatus": AvWlanAPStatus,
       "AvWlanRadioChannel": AvWlanRadioChannel,
       "AvWlanRadioChannelOrZero": AvWlanRadioChannelOrZero,
       "AvWlanRadioPower": AvWlanRadioPower,
       "AvWlanRadioAntenna": AvWlanRadioAntenna,
       "AvWlanRadioAntennaOrNone": AvWlanRadioAntennaOrNone,
       "AvWlanRadioExtCable": AvWlanRadioExtCable,
       "AvWlanRadioExtCableOrNone": AvWlanRadioExtCableOrNone,
       "AvWlanRadioOperationMode": AvWlanRadioOperationMode,
       "AvWlanRadioInterface": AvWlanRadioInterface,
       "AvWlanRadioInterfaceOrZero": AvWlanRadioInterfaceOrZero,
       "AvWlanDataRateSet": AvWlanDataRateSet,
       "AvWlanChannelSet": AvWlanChannelSet,
       "AvWlanRPTimeOfDay": AvWlanRPTimeOfDay,
       "AvWlanOui": AvWlanOui,
       "AvWlanTspecSuppAccessCategory": AvWlanTspecSuppAccessCategory,
       "AvWlanConfigSyncComponents": AvWlanConfigSyncComponents,
       "AvWlanAPLicenseCapacity": AvWlanAPLicenseCapacity,
       "AvWlanLogMsgLevel": AvWlanLogMsgLevel,
       "AvWlanCountryCode": AvWlanCountryCode,
       "AvWlanImageFileOrNone": AvWlanImageFileOrNone,
       "AvWlanFileUpdateStatus": AvWlanFileUpdateStatus,
       "AvWlanPacketCaptureFilterMask": AvWlanPacketCaptureFilterMask,
       "AvWlanLoadBalanceMetric": AvWlanLoadBalanceMetric,
       "AvWlanMobVlanRole": AvWlanMobVlanRole,
       "AvWlanMobVlanState": AvWlanMobVlanState,
       "AvWlanSwitchNotifAuxLimitsMap": AvWlanSwitchNotifAuxLimitsMap,
       "avayaWlanTcMib": avayaWlanTcMib}
)
