# SNMP MIB module (BREEZECOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BREEZECOM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:12 2024
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Breezecom_ObjectIdentity = ObjectIdentity
breezecom = _Breezecom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710)
)
_BreezecomPrvRev_ObjectIdentity = ObjectIdentity
breezecomPrvRev = _BreezecomPrvRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3)
)
_Brznetmib_ObjectIdentity = ObjectIdentity
brznetmib = _Brznetmib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2)
)
_BrzSys_ObjectIdentity = ObjectIdentity
brzSys = _BrzSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1)
)
_SysCmd_ObjectIdentity = ObjectIdentity
sysCmd = _SysCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1)
)


class _SysReset_Type(Integer32):
    """Custom type sysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SysReset_Type.__name__ = "Integer32"
_SysReset_Object = MibScalar
sysReset = _SysReset_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 1),
    _SysReset_Type()
)
sysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysReset.setStatus("mandatory")


class _SysSetDefaults_Type(Integer32):
    """Custom type sysSetDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SysSetDefaults_Type.__name__ = "Integer32"
_SysSetDefaults_Object = MibScalar
sysSetDefaults = _SysSetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 2),
    _SysSetDefaults_Type()
)
sysSetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSetDefaults.setStatus("mandatory")


class _SysResetCounters_Type(Integer32):
    """Custom type sysResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SysResetCounters_Type.__name__ = "Integer32"
_SysResetCounters_Object = MibScalar
sysResetCounters = _SysResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 3),
    _SysResetCounters_Type()
)
sysResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResetCounters.setStatus("mandatory")


class _SysTrapEnable_Type(Integer32):
    """Custom type sysTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SysTrapEnable_Type.__name__ = "Integer32"
_SysTrapEnable_Object = MibScalar
sysTrapEnable = _SysTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 4),
    _SysTrapEnable_Type()
)
sysTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapEnable.setStatus("mandatory")
_SysTrapCounter_Type = Counter32
_SysTrapCounter_Object = MibScalar
sysTrapCounter = _SysTrapCounter_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 5),
    _SysTrapCounter_Type()
)
sysTrapCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTrapCounter.setStatus("mandatory")
_SysCarrierSense_Type = Integer32
_SysCarrierSense_Object = MibScalar
sysCarrierSense = _SysCarrierSense_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 6),
    _SysCarrierSense_Type()
)
sysCarrierSense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCarrierSense.setStatus("mandatory")
_SysDeltaCarrierSense_Type = Integer32
_SysDeltaCarrierSense_Object = MibScalar
sysDeltaCarrierSense = _SysDeltaCarrierSense_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 7),
    _SysDeltaCarrierSense_Type()
)
sysDeltaCarrierSense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDeltaCarrierSense.setStatus("mandatory")


class _SysPartialDefaults_Type(Integer32):
    """Custom type sysPartialDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_SysPartialDefaults_Type.__name__ = "Integer32"
_SysPartialDefaults_Object = MibScalar
sysPartialDefaults = _SysPartialDefaults_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 8),
    _SysPartialDefaults_Type()
)
sysPartialDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPartialDefaults.setStatus("mandatory")


class _SysRunFromNonActiveCode_Type(Integer32):
    """Custom type sysRunFromNonActiveCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SysRunFromNonActiveCode_Type.__name__ = "Integer32"
_SysRunFromNonActiveCode_Object = MibScalar
sysRunFromNonActiveCode = _SysRunFromNonActiveCode_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 9),
    _SysRunFromNonActiveCode_Type()
)
sysRunFromNonActiveCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRunFromNonActiveCode.setStatus("mandatory")
_AccessRights_ObjectIdentity = ObjectIdentity
accessRights = _AccessRights_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 10)
)


class _SysDisplayAccessRights_Type(Integer32):
    """Custom type sysDisplayAccessRights based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized-technician", 2),
          ("installer", 1),
          ("user", 0))
    )


_SysDisplayAccessRights_Type.__name__ = "Integer32"
_SysDisplayAccessRights_Object = MibScalar
sysDisplayAccessRights = _SysDisplayAccessRights_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 10, 1),
    _SysDisplayAccessRights_Type()
)
sysDisplayAccessRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDisplayAccessRights.setStatus("mandatory")


class _SysChangeRightsToUSER_Type(Integer32):
    """Custom type sysChangeRightsToUSER based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("change", 1),
          ("unchanged", 0))
    )


_SysChangeRightsToUSER_Type.__name__ = "Integer32"
_SysChangeRightsToUSER_Object = MibScalar
sysChangeRightsToUSER = _SysChangeRightsToUSER_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 10, 2),
    _SysChangeRightsToUSER_Type()
)
sysChangeRightsToUSER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysChangeRightsToUSER.setStatus("mandatory")


class _SysChangeRightsToINSTALLER_Type(DisplayString):
    """Custom type sysChangeRightsToINSTALLER based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )


_SysChangeRightsToINSTALLER_Type.__name__ = "DisplayString"
_SysChangeRightsToINSTALLER_Object = MibScalar
sysChangeRightsToINSTALLER = _SysChangeRightsToINSTALLER_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 10, 3),
    _SysChangeRightsToINSTALLER_Type()
)
sysChangeRightsToINSTALLER.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysChangeRightsToINSTALLER.setStatus("mandatory")


class _SysChangeRightsToTECHNICIAN_Type(DisplayString):
    """Custom type sysChangeRightsToTECHNICIAN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SysChangeRightsToTECHNICIAN_Type.__name__ = "DisplayString"
_SysChangeRightsToTECHNICIAN_Object = MibScalar
sysChangeRightsToTECHNICIAN = _SysChangeRightsToTECHNICIAN_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 10, 4),
    _SysChangeRightsToTECHNICIAN_Type()
)
sysChangeRightsToTECHNICIAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysChangeRightsToTECHNICIAN.setStatus("mandatory")


class _SysChangeInstallerPassword_Type(DisplayString):
    """Custom type sysChangeInstallerPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_SysChangeInstallerPassword_Type.__name__ = "DisplayString"
_SysChangeInstallerPassword_Object = MibScalar
sysChangeInstallerPassword = _SysChangeInstallerPassword_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 10, 5),
    _SysChangeInstallerPassword_Type()
)
sysChangeInstallerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysChangeInstallerPassword.setStatus("mandatory")
_SysNoiseFloor_Type = Integer32
_SysNoiseFloor_Object = MibScalar
sysNoiseFloor = _SysNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 11),
    _SysNoiseFloor_Type()
)
sysNoiseFloor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNoiseFloor.setStatus("mandatory")


class _SysExternalAmplifier_Type(Integer32):
    """Custom type sysExternalAmplifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SysExternalAmplifier_Type.__name__ = "Integer32"
_SysExternalAmplifier_Object = MibScalar
sysExternalAmplifier = _SysExternalAmplifier_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 1, 12),
    _SysExternalAmplifier_Type()
)
sysExternalAmplifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysExternalAmplifier.setStatus("mandatory")
_SysParams_ObjectIdentity = ObjectIdentity
sysParams = _SysParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2)
)
_BrzHWMacAddress_Type = MacAddress
_BrzHWMacAddress_Object = MibScalar
brzHWMacAddress = _BrzHWMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 1),
    _BrzHWMacAddress_Type()
)
brzHWMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzHWMacAddress.setStatus("mandatory")


class _BrzApplTunneling_Type(Integer32):
    """Custom type brzApplTunneling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("apple-talk", 3),
          ("both", 1),
          ("ipx", 0),
          ("none", 2))
    )


_BrzApplTunneling_Type.__name__ = "Integer32"
_BrzApplTunneling_Object = MibScalar
brzApplTunneling = _BrzApplTunneling_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 2),
    _BrzApplTunneling_Type()
)
brzApplTunneling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzApplTunneling.setStatus("mandatory")


class _BrzPositiveBrg_Type(Integer32):
    """Custom type brzPositiveBrg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("forward-unknown", 2),
          ("intelligent", 3),
          ("na", 255),
          ("reject-unknown", 1))
    )


_BrzPositiveBrg_Type.__name__ = "Integer32"
_BrzPositiveBrg_Object = MibScalar
brzPositiveBrg = _BrzPositiveBrg_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 3),
    _BrzPositiveBrg_Type()
)
brzPositiveBrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzPositiveBrg.setStatus("mandatory")


class _BrzIpFilter_Type(Integer32):
    """Custom type brzIpFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("na", 255),
          ("off", 2),
          ("on", 1))
    )


_BrzIpFilter_Type.__name__ = "Integer32"
_BrzIpFilter_Object = MibScalar
brzIpFilter = _BrzIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 4),
    _BrzIpFilter_Type()
)
brzIpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzIpFilter.setStatus("mandatory")


class _BrzTranslationMode_Type(Integer32):
    """Custom type brzTranslationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_BrzTranslationMode_Type.__name__ = "Integer32"
_BrzTranslationMode_Object = MibScalar
brzTranslationMode = _BrzTranslationMode_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 5),
    _BrzTranslationMode_Type()
)
brzTranslationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzTranslationMode.setStatus("mandatory")


class _BrzWIXSupport_Type(Integer32):
    """Custom type brzWIXSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_BrzWIXSupport_Type.__name__ = "Integer32"
_BrzWIXSupport_Object = MibScalar
brzWIXSupport = _BrzWIXSupport_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 6),
    _BrzWIXSupport_Type()
)
brzWIXSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzWIXSupport.setStatus("mandatory")


class _BrzWlanNetID_Type(DisplayString):
    """Custom type brzWlanNetID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(31, 31),
    )


_BrzWlanNetID_Type.__name__ = "DisplayString"
_BrzWlanNetID_Object = MibScalar
brzWlanNetID = _BrzWlanNetID_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 7),
    _BrzWlanNetID_Type()
)
brzWlanNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzWlanNetID.setStatus("mandatory")
_BrzAuthenticationType_Type = Integer32
_BrzAuthenticationType_Object = MibScalar
brzAuthenticationType = _BrzAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 8),
    _BrzAuthenticationType_Type()
)
brzAuthenticationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzAuthenticationType.setStatus("mandatory")


class _BrzWlanRTNetID_Type(DisplayString):
    """Custom type brzWlanRTNetID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(31, 31),
    )


_BrzWlanRTNetID_Type.__name__ = "DisplayString"
_BrzWlanRTNetID_Object = MibScalar
brzWlanRTNetID = _BrzWlanRTNetID_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 9),
    _BrzWlanRTNetID_Type()
)
brzWlanRTNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzWlanRTNetID.setStatus("mandatory")


class _BrzApRedundancySupport_Type(Integer32):
    """Custom type brzApRedundancySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("na", 255),
          ("off", 2),
          ("on", 1))
    )


_BrzApRedundancySupport_Type.__name__ = "Integer32"
_BrzApRedundancySupport_Object = MibScalar
brzApRedundancySupport = _BrzApRedundancySupport_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 10),
    _BrzApRedundancySupport_Type()
)
brzApRedundancySupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzApRedundancySupport.setStatus("mandatory")


class _BrzWlanRelayUnicast_Type(Integer32):
    """Custom type brzWlanRelayUnicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("na", 255),
          ("off", 2),
          ("on", 1))
    )


_BrzWlanRelayUnicast_Type.__name__ = "Integer32"
_BrzWlanRelayUnicast_Object = MibScalar
brzWlanRelayUnicast = _BrzWlanRelayUnicast_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 11),
    _BrzWlanRelayUnicast_Type()
)
brzWlanRelayUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzWlanRelayUnicast.setStatus("mandatory")


class _BrzWlanRelayBroadcast_Type(Integer32):
    """Custom type brzWlanRelayBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("na", 255),
          ("off", 2),
          ("on", 1))
    )


_BrzWlanRelayBroadcast_Type.__name__ = "Integer32"
_BrzWlanRelayBroadcast_Object = MibScalar
brzWlanRelayBroadcast = _BrzWlanRelayBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 12),
    _BrzWlanRelayBroadcast_Type()
)
brzWlanRelayBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzWlanRelayBroadcast.setStatus("mandatory")


class _BrzApRedundancyLimit_Type(Integer32):
    """Custom type brzApRedundancyLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("na", 255)
    )


_BrzApRedundancyLimit_Type.__name__ = "Integer32"
_BrzApRedundancyLimit_Object = MibScalar
brzApRedundancyLimit = _BrzApRedundancyLimit_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 13),
    _BrzApRedundancyLimit_Type()
)
brzApRedundancyLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzApRedundancyLimit.setStatus("mandatory")
_BrzStaNumForLargeCW_Type = Integer32
_BrzStaNumForLargeCW_Object = MibScalar
brzStaNumForLargeCW = _BrzStaNumForLargeCW_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 14),
    _BrzStaNumForLargeCW_Type()
)
brzStaNumForLargeCW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzStaNumForLargeCW.setStatus("mandatory")


class _BrzPowerMngMode_Type(Integer32):
    """Custom type brzPowerMngMode based on Integer32"""
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


_BrzPowerMngMode_Type.__name__ = "Integer32"
_BrzPowerMngMode_Object = MibScalar
brzPowerMngMode = _BrzPowerMngMode_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 15),
    _BrzPowerMngMode_Type()
)
brzPowerMngMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzPowerMngMode.setStatus("mandatory")


class _BrzACKDelayed_Type(Integer32):
    """Custom type brzACKDelayed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_BrzACKDelayed_Type.__name__ = "Integer32"
_BrzACKDelayed_Object = MibScalar
brzACKDelayed = _BrzACKDelayed_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 16),
    _BrzACKDelayed_Type()
)
brzACKDelayed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzACKDelayed.setStatus("mandatory")
_BrzDTIMPperiod_Type = Integer32
_BrzDTIMPperiod_Object = MibScalar
brzDTIMPperiod = _BrzDTIMPperiod_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 17),
    _BrzDTIMPperiod_Type()
)
brzDTIMPperiod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzDTIMPperiod.setStatus("mandatory")


class _BrzPowerMngBitTestMode_Type(Integer32):
    """Custom type brzPowerMngBitTestMode based on Integer32"""
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


_BrzPowerMngBitTestMode_Type.__name__ = "Integer32"
_BrzPowerMngBitTestMode_Object = MibScalar
brzPowerMngBitTestMode = _BrzPowerMngBitTestMode_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 18),
    _BrzPowerMngBitTestMode_Type()
)
brzPowerMngBitTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzPowerMngBitTestMode.setStatus("mandatory")
_BrzBeaconInterval_Type = Integer32
_BrzBeaconInterval_Object = MibScalar
brzBeaconInterval = _BrzBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 19),
    _BrzBeaconInterval_Type()
)
brzBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzBeaconInterval.setStatus("mandatory")


class _BrzPowerSaveSupport_Type(Integer32):
    """Custom type brzPowerSaveSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("enabled-with-pm-bit", 2))
    )


_BrzPowerSaveSupport_Type.__name__ = "Integer32"
_BrzPowerSaveSupport_Object = MibScalar
brzPowerSaveSupport = _BrzPowerSaveSupport_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 20),
    _BrzPowerSaveSupport_Type()
)
brzPowerSaveSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzPowerSaveSupport.setStatus("mandatory")
_BrzWlanAssocAge_Type = Integer32
_BrzWlanAssocAge_Object = MibScalar
brzWlanAssocAge = _BrzWlanAssocAge_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 21),
    _BrzWlanAssocAge_Type()
)
brzWlanAssocAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzWlanAssocAge.setStatus("mandatory")


class _BrzEnableVoice_Type(Integer32):
    """Custom type brzEnableVoice based on Integer32"""
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


_BrzEnableVoice_Type.__name__ = "Integer32"
_BrzEnableVoice_Object = MibScalar
brzEnableVoice = _BrzEnableVoice_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 22),
    _BrzEnableVoice_Type()
)
brzEnableVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzEnableVoice.setStatus("mandatory")


class _BrzNonActiveCodeState_Type(DisplayString):
    """Custom type brzNonActiveCodeState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(25, 25),
    )


_BrzNonActiveCodeState_Type.__name__ = "DisplayString"
_BrzNonActiveCodeState_Object = MibScalar
brzNonActiveCodeState = _BrzNonActiveCodeState_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 26),
    _BrzNonActiveCodeState_Type()
)
brzNonActiveCodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzNonActiveCodeState.setStatus("mandatory")


class _BrzDisplayNonActiveCodeVersion_Type(DisplayString):
    """Custom type brzDisplayNonActiveCodeVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )


_BrzDisplayNonActiveCodeVersion_Type.__name__ = "DisplayString"
_BrzDisplayNonActiveCodeVersion_Object = MibScalar
brzDisplayNonActiveCodeVersion = _BrzDisplayNonActiveCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 27),
    _BrzDisplayNonActiveCodeVersion_Type()
)
brzDisplayNonActiveCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzDisplayNonActiveCodeVersion.setStatus("mandatory")
_BrzIntelligentBridgingPeriod_Type = Integer32
_BrzIntelligentBridgingPeriod_Object = MibScalar
brzIntelligentBridgingPeriod = _BrzIntelligentBridgingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 1, 2, 28),
    _BrzIntelligentBridgingPeriod_Type()
)
brzIntelligentBridgingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzIntelligentBridgingPeriod.setStatus("mandatory")
_IpParams_ObjectIdentity = ObjectIdentity
ipParams = _IpParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 2)
)
_TrapHostsTable_Object = MibTable
trapHostsTable = _TrapHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    trapHostsTable.setStatus("mandatory")
_TrapHostsEntry_Object = MibTableRow
trapHostsEntry = _TrapHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 2, 1, 1)
)
trapHostsEntry.setIndexNames(
    (0, "BREEZECOM-MIB", "trapHostsIndex"),
)
if mibBuilder.loadTexts:
    trapHostsEntry.setStatus("mandatory")
_TrapHostsIndex_Type = Integer32
_TrapHostsIndex_Object = MibTableColumn
trapHostsIndex = _TrapHostsIndex_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 2, 1, 1, 1),
    _TrapHostsIndex_Type()
)
trapHostsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapHostsIndex.setStatus("mandatory")
_TrapIPaddress_Type = IpAddress
_TrapIPaddress_Object = MibTableColumn
trapIPaddress = _TrapIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 2, 1, 1, 2),
    _TrapIPaddress_Type()
)
trapIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIPaddress.setStatus("mandatory")


class _TrapCommunity_Type(DisplayString):
    """Custom type trapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TrapCommunity_Type.__name__ = "DisplayString"
_TrapCommunity_Object = MibTableColumn
trapCommunity = _TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 2, 1, 1, 3),
    _TrapCommunity_Type()
)
trapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunity.setStatus("mandatory")
_IpAddr_Type = IpAddress
_IpAddr_Object = MibScalar
ipAddr = _IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 2, 2),
    _IpAddr_Type()
)
ipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddr.setStatus("mandatory")
_MaskIP_Type = IpAddress
_MaskIP_Object = MibScalar
maskIP = _MaskIP_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 2, 3),
    _MaskIP_Type()
)
maskIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maskIP.setStatus("mandatory")
_ReadCommunity_Type = DisplayString
_ReadCommunity_Object = MibScalar
readCommunity = _ReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 2, 4),
    _ReadCommunity_Type()
)
readCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    readCommunity.setStatus("mandatory")
_WriteCommunity_Type = DisplayString
_WriteCommunity_Object = MibScalar
writeCommunity = _WriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 2, 5),
    _WriteCommunity_Type()
)
writeCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    writeCommunity.setStatus("mandatory")
_GatewayIPaddr_Type = IpAddress
_GatewayIPaddr_Object = MibScalar
gatewayIPaddr = _GatewayIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 2, 6),
    _GatewayIPaddr_Type()
)
gatewayIPaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayIPaddr.setStatus("mandatory")


class _BrzIPStack_Type(Integer32):
    """Custom type brzIPStack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_BrzIPStack_Type.__name__ = "Integer32"
_BrzIPStack_Object = MibScalar
brzIPStack = _BrzIPStack_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 2, 7),
    _BrzIPStack_Type()
)
brzIPStack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzIPStack.setStatus("mandatory")
_BrzWlan_ObjectIdentity = ObjectIdentity
brzWlan = _BrzWlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3)
)
_BrzWlanParams_ObjectIdentity = ObjectIdentity
brzWlanParams = _BrzWlanParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1)
)


class _BrzMaxRate_Type(Integer32):
    """Custom type brzMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BrzMaxRate_Type.__name__ = "Integer32"
_BrzMaxRate_Object = MibScalar
brzMaxRate = _BrzMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 1),
    _BrzMaxRate_Type()
)
brzMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzMaxRate.setStatus("mandatory")


class _BrzMobilLvl_Type(Integer32):
    """Custom type brzMobilLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_BrzMobilLvl_Type.__name__ = "Integer32"
_BrzMobilLvl_Object = MibScalar
brzMobilLvl = _BrzMobilLvl_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 2),
    _BrzMobilLvl_Type()
)
brzMobilLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzMobilLvl.setStatus("mandatory")


class _BrzAvrgRssi_Type(Integer32):
    """Custom type brzAvrgRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("na", 255)
    )


_BrzAvrgRssi_Type.__name__ = "Integer32"
_BrzAvrgRssi_Object = MibScalar
brzAvrgRssi = _BrzAvrgRssi_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 3),
    _BrzAvrgRssi_Type()
)
brzAvrgRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzAvrgRssi.setStatus("mandatory")
_BrzWlanProtocol_Type = Integer32
_BrzWlanProtocol_Object = MibScalar
brzWlanProtocol = _BrzWlanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 4),
    _BrzWlanProtocol_Type()
)
brzWlanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzWlanProtocol.setStatus("mandatory")
_BrzWlanTrapThreashold_Type = Integer32
_BrzWlanTrapThreashold_Object = MibScalar
brzWlanTrapThreashold = _BrzWlanTrapThreashold_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 5),
    _BrzWlanTrapThreashold_Type()
)
brzWlanTrapThreashold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzWlanTrapThreashold.setStatus("mandatory")


class _BrzWlanQuality_Type(Integer32):
    """Custom type brzWlanQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("bad", 4),
          ("excellent", 1),
          ("good", 2),
          ("medium", 3),
          ("unknown", 10))
    )


_BrzWlanQuality_Type.__name__ = "Integer32"
_BrzWlanQuality_Object = MibScalar
brzWlanQuality = _BrzWlanQuality_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 6),
    _BrzWlanQuality_Type()
)
brzWlanQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzWlanQuality.setStatus("mandatory")
_KnownAPsTable_Object = MibTable
knownAPsTable = _KnownAPsTable_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 7)
)
if mibBuilder.loadTexts:
    knownAPsTable.setStatus("mandatory")
_KnownAPsEntry_Object = MibTableRow
knownAPsEntry = _KnownAPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 7, 1)
)
knownAPsEntry.setIndexNames(
    (0, "BREEZECOM-MIB", "knownAPsIndex"),
)
if mibBuilder.loadTexts:
    knownAPsEntry.setStatus("mandatory")
_KnownAPsIndex_Type = Integer32
_KnownAPsIndex_Object = MibTableColumn
knownAPsIndex = _KnownAPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 7, 1, 1),
    _KnownAPsIndex_Type()
)
knownAPsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownAPsIndex.setStatus("mandatory")
_KnownAPsValue_Type = MacAddress
_KnownAPsValue_Object = MibTableColumn
knownAPsValue = _KnownAPsValue_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 7, 1, 2),
    _KnownAPsValue_Type()
)
knownAPsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    knownAPsValue.setStatus("mandatory")


class _KnownAPsQuality_Type(Integer32):
    """Custom type knownAPsQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("good", 2),
          ("poor", 1),
          ("unknown", 10))
    )


_KnownAPsQuality_Type.__name__ = "Integer32"
_KnownAPsQuality_Object = MibTableColumn
knownAPsQuality = _KnownAPsQuality_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 7, 1, 3),
    _KnownAPsQuality_Type()
)
knownAPsQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownAPsQuality.setStatus("mandatory")
_KnownAPsAvrgRssi_Type = Integer32
_KnownAPsAvrgRssi_Object = MibTableColumn
knownAPsAvrgRssi = _KnownAPsAvrgRssi_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 7, 1, 4),
    _KnownAPsAvrgRssi_Type()
)
knownAPsAvrgRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownAPsAvrgRssi.setStatus("mandatory")


class _KnownAPsStatus_Type(Integer32):
    """Custom type knownAPsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_KnownAPsStatus_Type.__name__ = "Integer32"
_KnownAPsStatus_Object = MibTableColumn
knownAPsStatus = _KnownAPsStatus_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 7, 1, 5),
    _KnownAPsStatus_Type()
)
knownAPsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    knownAPsStatus.setStatus("mandatory")
_KnownAPsLoadStations_Type = Integer32
_KnownAPsLoadStations_Object = MibTableColumn
knownAPsLoadStations = _KnownAPsLoadStations_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 7, 1, 6),
    _KnownAPsLoadStations_Type()
)
knownAPsLoadStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownAPsLoadStations.setStatus("mandatory")
_KnownAPsGoodBeacons_Type = Integer32
_KnownAPsGoodBeacons_Object = MibTableColumn
knownAPsGoodBeacons = _KnownAPsGoodBeacons_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 7, 1, 7),
    _KnownAPsGoodBeacons_Type()
)
knownAPsGoodBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownAPsGoodBeacons.setStatus("mandatory")
_KnownAPsTotalBeacons_Type = Integer32
_KnownAPsTotalBeacons_Object = MibTableColumn
knownAPsTotalBeacons = _KnownAPsTotalBeacons_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 7, 1, 8),
    _KnownAPsTotalBeacons_Type()
)
knownAPsTotalBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownAPsTotalBeacons.setStatus("mandatory")


class _KnownAPsAvrgDbm_Type(DisplayString):
    """Custom type knownAPsAvrgDbm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_KnownAPsAvrgDbm_Type.__name__ = "DisplayString"
_KnownAPsAvrgDbm_Object = MibTableColumn
knownAPsAvrgDbm = _KnownAPsAvrgDbm_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 7, 1, 9),
    _KnownAPsAvrgDbm_Type()
)
knownAPsAvrgDbm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    knownAPsAvrgDbm.setStatus("mandatory")
_BrzLastBeacon_Type = Integer32
_BrzLastBeacon_Object = MibScalar
brzLastBeacon = _BrzLastBeacon_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 8),
    _BrzLastBeacon_Type()
)
brzLastBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzLastBeacon.setStatus("mandatory")
_BrzBadBeacons_Type = Integer32
_BrzBadBeacons_Object = MibScalar
brzBadBeacons = _BrzBadBeacons_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 9),
    _BrzBadBeacons_Type()
)
brzBadBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzBadBeacons.setStatus("mandatory")
_BrzLoadStations_Type = Integer32
_BrzLoadStations_Object = MibScalar
brzLoadStations = _BrzLoadStations_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 10),
    _BrzLoadStations_Type()
)
brzLoadStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzLoadStations.setStatus("mandatory")


class _BrzAvrgDBm_Type(DisplayString):
    """Custom type brzAvrgDBm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_BrzAvrgDBm_Type.__name__ = "DisplayString"
_BrzAvrgDBm_Object = MibScalar
brzAvrgDBm = _BrzAvrgDBm_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 1, 11),
    _BrzAvrgDBm_Type()
)
brzAvrgDBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzAvrgDBm.setStatus("mandatory")
_BrzAP_ObjectIdentity = ObjectIdentity
brzAP = _BrzAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2)
)
_BssInfo_ObjectIdentity = ObjectIdentity
bssInfo = _BssInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 1)
)
_BssNumOfStations_Type = Integer32
_BssNumOfStations_Object = MibScalar
bssNumOfStations = _BssNumOfStations_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 1, 1),
    _BssNumOfStations_Type()
)
bssNumOfStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bssNumOfStations.setStatus("mandatory")
_BssNumOfStationsPeak_Type = Integer32
_BssNumOfStationsPeak_Object = MibScalar
bssNumOfStationsPeak = _BssNumOfStationsPeak_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 1, 2),
    _BssNumOfStationsPeak_Type()
)
bssNumOfStationsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bssNumOfStationsPeak.setStatus("mandatory")


class _BssCollectPerStationInfo_Type(Integer32):
    """Custom type bssCollectPerStationInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("na", 255),
          ("off", 2),
          ("on", 1))
    )


_BssCollectPerStationInfo_Type.__name__ = "Integer32"
_BssCollectPerStationInfo_Object = MibScalar
bssCollectPerStationInfo = _BssCollectPerStationInfo_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 1, 3),
    _BssCollectPerStationInfo_Type()
)
bssCollectPerStationInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bssCollectPerStationInfo.setStatus("mandatory")
_BssNumOfBeaconSent_Type = Integer32
_BssNumOfBeaconSent_Object = MibScalar
bssNumOfBeaconSent = _BssNumOfBeaconSent_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 1, 4),
    _BssNumOfBeaconSent_Type()
)
bssNumOfBeaconSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bssNumOfBeaconSent.setStatus("mandatory")
_BssNumOfBeaconLost_Type = Integer32
_BssNumOfBeaconLost_Object = MibScalar
bssNumOfBeaconLost = _BssNumOfBeaconLost_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 1, 5),
    _BssNumOfBeaconLost_Type()
)
bssNumOfBeaconLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bssNumOfBeaconLost.setStatus("mandatory")
_BssNumOfStationsAuthenticated_Type = Integer32
_BssNumOfStationsAuthenticated_Object = MibScalar
bssNumOfStationsAuthenticated = _BssNumOfStationsAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 1, 6),
    _BssNumOfStationsAuthenticated_Type()
)
bssNumOfStationsAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bssNumOfStationsAuthenticated.setStatus("mandatory")
_BssNumOfStationsAuthenticatedPeak_Type = Integer32
_BssNumOfStationsAuthenticatedPeak_Object = MibScalar
bssNumOfStationsAuthenticatedPeak = _BssNumOfStationsAuthenticatedPeak_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 1, 7),
    _BssNumOfStationsAuthenticatedPeak_Type()
)
bssNumOfStationsAuthenticatedPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bssNumOfStationsAuthenticatedPeak.setStatus("mandatory")
_BssApAdb_ObjectIdentity = ObjectIdentity
bssApAdb = _BssApAdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2)
)
_AdbTable_Object = MibTable
adbTable = _AdbTable_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    adbTable.setStatus("mandatory")
_AdbEntry_Object = MibTableRow
adbEntry = _AdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1)
)
adbEntry.setIndexNames(
    (0, "BREEZECOM-MIB", "stAddress"),
)
if mibBuilder.loadTexts:
    adbEntry.setStatus("mandatory")
_StAddress_Type = MacAddress
_StAddress_Object = MibTableColumn
stAddress = _StAddress_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 1),
    _StAddress_Type()
)
stAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stAddress.setStatus("mandatory")


class _StCFMode_Type(Integer32):
    """Custom type stCFMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_StCFMode_Type.__name__ = "Integer32"
_StCFMode_Object = MibTableColumn
stCFMode = _StCFMode_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 4),
    _StCFMode_Type()
)
stCFMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stCFMode.setStatus("mandatory")
_StMaxRate_Type = Integer32
_StMaxRate_Object = MibTableColumn
stMaxRate = _StMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 5),
    _StMaxRate_Type()
)
stMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stMaxRate.setStatus("mandatory")
_StCurTxRate_Type = Integer32
_StCurTxRate_Object = MibTableColumn
stCurTxRate = _StCurTxRate_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 6),
    _StCurTxRate_Type()
)
stCurTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stCurTxRate.setStatus("mandatory")
_StRssi_Type = Integer32
_StRssi_Object = MibTableColumn
stRssi = _StRssi_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 7),
    _StRssi_Type()
)
stRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stRssi.setStatus("mandatory")


class _StPMMode_Type(Integer32):
    """Custom type stPMMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("power-saved", 2))
    )


_StPMMode_Type.__name__ = "Integer32"
_StPMMode_Object = MibTableColumn
stPMMode = _StPMMode_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 8),
    _StPMMode_Type()
)
stPMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stPMMode.setStatus("mandatory")
_StTxFragments_Type = Counter32
_StTxFragments_Object = MibTableColumn
stTxFragments = _StTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 9),
    _StTxFragments_Type()
)
stTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stTxFragments.setStatus("mandatory")
_StTxFragments1M_Type = Counter32
_StTxFragments1M_Object = MibTableColumn
stTxFragments1M = _StTxFragments1M_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 10),
    _StTxFragments1M_Type()
)
stTxFragments1M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stTxFragments1M.setStatus("mandatory")
_StTxFragments2M_Type = Counter32
_StTxFragments2M_Object = MibTableColumn
stTxFragments2M = _StTxFragments2M_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 11),
    _StTxFragments2M_Type()
)
stTxFragments2M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stTxFragments2M.setStatus("mandatory")
_StTxFragments3M_Type = Counter32
_StTxFragments3M_Object = MibTableColumn
stTxFragments3M = _StTxFragments3M_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 12),
    _StTxFragments3M_Type()
)
stTxFragments3M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stTxFragments3M.setStatus("mandatory")
_StTxRetry_Type = Counter32
_StTxRetry_Object = MibTableColumn
stTxRetry = _StTxRetry_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 13),
    _StTxRetry_Type()
)
stTxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stTxRetry.setStatus("mandatory")
_StTxDroppedPackets_Type = Counter32
_StTxDroppedPackets_Object = MibTableColumn
stTxDroppedPackets = _StTxDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 14),
    _StTxDroppedPackets_Type()
)
stTxDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stTxDroppedPackets.setStatus("mandatory")
_StRxFragments_Type = Counter32
_StRxFragments_Object = MibTableColumn
stRxFragments = _StRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 15),
    _StRxFragments_Type()
)
stRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stRxFragments.setStatus("mandatory")


class _StWlanStatus_Type(Integer32):
    """Custom type stWlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("good", 2),
          ("poor", 1),
          ("unknown", 10))
    )


_StWlanStatus_Type.__name__ = "Integer32"
_StWlanStatus_Object = MibTableColumn
stWlanStatus = _StWlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 16),
    _StWlanStatus_Type()
)
stWlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stWlanStatus.setStatus("mandatory")


class _StResetCounters_Type(Integer32):
    """Custom type stResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_StResetCounters_Type.__name__ = "Integer32"
_StResetCounters_Object = MibTableColumn
stResetCounters = _StResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 17),
    _StResetCounters_Type()
)
stResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stResetCounters.setStatus("mandatory")


class _StType_Type(Integer32):
    """Custom type stType based on Integer32"""
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
        *(("breeze-new", 5),
          ("sa-10", 1),
          ("sa-40", 3),
          ("sa-pc", 4),
          ("unknown", 6),
          ("wb-10", 2))
    )


_StType_Type.__name__ = "Integer32"
_StType_Object = MibTableColumn
stType = _StType_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 18),
    _StType_Type()
)
stType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stType.setStatus("mandatory")
_StTxRetryPercent_Type = Counter32
_StTxRetryPercent_Object = MibTableColumn
stTxRetryPercent = _StTxRetryPercent_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 19),
    _StTxRetryPercent_Type()
)
stTxRetryPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stTxRetryPercent.setStatus("mandatory")
_StReTxFragments1M_Type = Counter32
_StReTxFragments1M_Object = MibTableColumn
stReTxFragments1M = _StReTxFragments1M_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 20),
    _StReTxFragments1M_Type()
)
stReTxFragments1M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stReTxFragments1M.setStatus("mandatory")
_StReTxFragments2M_Type = Counter32
_StReTxFragments2M_Object = MibTableColumn
stReTxFragments2M = _StReTxFragments2M_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 21),
    _StReTxFragments2M_Type()
)
stReTxFragments2M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stReTxFragments2M.setStatus("mandatory")
_StReTxFragments3M_Type = Counter32
_StReTxFragments3M_Object = MibTableColumn
stReTxFragments3M = _StReTxFragments3M_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 22),
    _StReTxFragments3M_Type()
)
stReTxFragments3M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stReTxFragments3M.setStatus("mandatory")


class _StDbm_Type(DisplayString):
    """Custom type stDbm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_StDbm_Type.__name__ = "DisplayString"
_StDbm_Object = MibTableColumn
stDbm = _StDbm_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 2, 2, 1, 1, 23),
    _StDbm_Type()
)
stDbm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stDbm.setStatus("mandatory")
_BrzSTA_ObjectIdentity = ObjectIdentity
brzSTA = _BrzSTA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 3)
)
_BrzCurrentAPMacAddress_Type = MacAddress
_BrzCurrentAPMacAddress_Object = MibScalar
brzCurrentAPMacAddress = _BrzCurrentAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 3, 1),
    _BrzCurrentAPMacAddress_Type()
)
brzCurrentAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzCurrentAPMacAddress.setStatus("mandatory")
_BrzLastAPMacAddress_Type = MacAddress
_BrzLastAPMacAddress_Object = MibScalar
brzLastAPMacAddress = _BrzLastAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 3, 2),
    _BrzLastAPMacAddress_Type()
)
brzLastAPMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzLastAPMacAddress.setStatus("mandatory")
_BrzPreferredAPMacAddress_Type = MacAddress
_BrzPreferredAPMacAddress_Object = MibScalar
brzPreferredAPMacAddress = _BrzPreferredAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 3, 3),
    _BrzPreferredAPMacAddress_Type()
)
brzPreferredAPMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzPreferredAPMacAddress.setStatus("mandatory")
_BrzRoamToAPMacAddress_Type = MacAddress
_BrzRoamToAPMacAddress_Object = MibScalar
brzRoamToAPMacAddress = _BrzRoamToAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 3, 4),
    _BrzRoamToAPMacAddress_Type()
)
brzRoamToAPMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzRoamToAPMacAddress.setStatus("mandatory")


class _BrzCFMode_Type(Integer32):
    """Custom type brzCFMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("na", 255),
          ("off", 2),
          ("on", 1))
    )


_BrzCFMode_Type.__name__ = "Integer32"
_BrzCFMode_Object = MibScalar
brzCFMode = _BrzCFMode_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 3, 5),
    _BrzCFMode_Type()
)
brzCFMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzCFMode.setStatus("mandatory")
_BrzTx1MBitRate_Type = Counter32
_BrzTx1MBitRate_Object = MibScalar
brzTx1MBitRate = _BrzTx1MBitRate_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 3, 6),
    _BrzTx1MBitRate_Type()
)
brzTx1MBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTx1MBitRate.setStatus("mandatory")
_BrzTx2MBitRate_Type = Counter32
_BrzTx2MBitRate_Object = MibScalar
brzTx2MBitRate = _BrzTx2MBitRate_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 3, 7),
    _BrzTx2MBitRate_Type()
)
brzTx2MBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTx2MBitRate.setStatus("mandatory")
_BrzTx3MBitRate_Type = Counter32
_BrzTx3MBitRate_Object = MibScalar
brzTx3MBitRate = _BrzTx3MBitRate_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 3, 8),
    _BrzTx3MBitRate_Type()
)
brzTx3MBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTx3MBitRate.setStatus("mandatory")
_BrzTotalRetx_Type = MacAddress
_BrzTotalRetx_Object = MibScalar
brzTotalRetx = _BrzTotalRetx_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 3, 9),
    _BrzTotalRetx_Type()
)
brzTotalRetx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTotalRetx.setStatus("mandatory")
_BrzRoamParams_ObjectIdentity = ObjectIdentity
brzRoamParams = _BrzRoamParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 4)
)
_BrzRoamDecisionWin_Type = Integer32
_BrzRoamDecisionWin_Object = MibScalar
brzRoamDecisionWin = _BrzRoamDecisionWin_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 4, 1),
    _BrzRoamDecisionWin_Type()
)
brzRoamDecisionWin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzRoamDecisionWin.setStatus("mandatory")
_BrzRoamDecisionNumerator_Type = Integer32
_BrzRoamDecisionNumerator_Object = MibScalar
brzRoamDecisionNumerator = _BrzRoamDecisionNumerator_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 4, 2),
    _BrzRoamDecisionNumerator_Type()
)
brzRoamDecisionNumerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzRoamDecisionNumerator.setStatus("mandatory")
_BrzRoamDecisionRSSIThreshold_Type = Integer32
_BrzRoamDecisionRSSIThreshold_Object = MibScalar
brzRoamDecisionRSSIThreshold = _BrzRoamDecisionRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 4, 3),
    _BrzRoamDecisionRSSIThreshold_Type()
)
brzRoamDecisionRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzRoamDecisionRSSIThreshold.setStatus("mandatory")
_BrzJoinDecisionRSSIThreshold_Type = Integer32
_BrzJoinDecisionRSSIThreshold_Object = MibScalar
brzJoinDecisionRSSIThreshold = _BrzJoinDecisionRSSIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 4, 4),
    _BrzJoinDecisionRSSIThreshold_Type()
)
brzJoinDecisionRSSIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzJoinDecisionRSSIThreshold.setStatus("mandatory")
_BrzNeighboringBeacons_Type = Integer32
_BrzNeighboringBeacons_Object = MibScalar
brzNeighboringBeacons = _BrzNeighboringBeacons_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 4, 5),
    _BrzNeighboringBeacons_Type()
)
brzNeighboringBeacons.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzNeighboringBeacons.setStatus("mandatory")
_BrzNumberOfProbeResponses_Type = Integer32
_BrzNumberOfProbeResponses_Object = MibScalar
brzNumberOfProbeResponses = _BrzNumberOfProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 4, 6),
    _BrzNumberOfProbeResponses_Type()
)
brzNumberOfProbeResponses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzNumberOfProbeResponses.setStatus("mandatory")
_BrzNumberOfBeaconsForDisconnect_Type = Integer32
_BrzNumberOfBeaconsForDisconnect_Object = MibScalar
brzNumberOfBeaconsForDisconnect = _BrzNumberOfBeaconsForDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 4, 7),
    _BrzNumberOfBeaconsForDisconnect_Type()
)
brzNumberOfBeaconsForDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzNumberOfBeaconsForDisconnect.setStatus("mandatory")
_BrzMaxNumberOfScanning_Type = Integer32
_BrzMaxNumberOfScanning_Object = MibScalar
brzMaxNumberOfScanning = _BrzMaxNumberOfScanning_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 4, 8),
    _BrzMaxNumberOfScanning_Type()
)
brzMaxNumberOfScanning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzMaxNumberOfScanning.setStatus("mandatory")
_BrzNeighboringBeaconRate_Type = Integer32
_BrzNeighboringBeaconRate_Object = MibScalar
brzNeighboringBeaconRate = _BrzNeighboringBeaconRate_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 3, 4, 9),
    _BrzNeighboringBeaconRate_Type()
)
brzNeighboringBeaconRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brzNeighboringBeaconRate.setStatus("mandatory")
_BrzCnt_ObjectIdentity = ObjectIdentity
brzCnt = _BrzCnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4)
)
_BrzDSCnt_ObjectIdentity = ObjectIdentity
brzDSCnt = _BrzDSCnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 1)
)
_BrzRxFromDS_Type = Counter32
_BrzRxFromDS_Object = MibScalar
brzRxFromDS = _BrzRxFromDS_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 1, 1),
    _BrzRxFromDS_Type()
)
brzRxFromDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzRxFromDS.setStatus("mandatory")
_BrzRxBadFromDS_Type = Counter32
_BrzRxBadFromDS_Object = MibScalar
brzRxBadFromDS = _BrzRxBadFromDS_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 1, 2),
    _BrzRxBadFromDS_Type()
)
brzRxBadFromDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzRxBadFromDS.setStatus("mandatory")
_BrzRxOctetsFromDS_Type = Counter32
_BrzRxOctetsFromDS_Object = MibScalar
brzRxOctetsFromDS = _BrzRxOctetsFromDS_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 1, 3),
    _BrzRxOctetsFromDS_Type()
)
brzRxOctetsFromDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzRxOctetsFromDS.setStatus("mandatory")
_BrzTxToDS_Type = Counter32
_BrzTxToDS_Object = MibScalar
brzTxToDS = _BrzTxToDS_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 1, 4),
    _BrzTxToDS_Type()
)
brzTxToDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTxToDS.setStatus("mandatory")
_BrzMissedFrames_Type = Counter32
_BrzMissedFrames_Object = MibScalar
brzMissedFrames = _BrzMissedFrames_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 1, 5),
    _BrzMissedFrames_Type()
)
brzMissedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzMissedFrames.setStatus("mandatory")
_BrzTxOctetsToDS_Type = Counter32
_BrzTxOctetsToDS_Object = MibScalar
brzTxOctetsToDS = _BrzTxOctetsToDS_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 1, 6),
    _BrzTxOctetsToDS_Type()
)
brzTxOctetsToDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTxOctetsToDS.setStatus("mandatory")
_BrzRxOctetsForwardToWlan_Type = Counter32
_BrzRxOctetsForwardToWlan_Object = MibScalar
brzRxOctetsForwardToWlan = _BrzRxOctetsForwardToWlan_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 1, 7),
    _BrzRxOctetsForwardToWlan_Type()
)
brzRxOctetsForwardToWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzRxOctetsForwardToWlan.setStatus("mandatory")
_BrzRxForwardToWlan_Type = Counter32
_BrzRxForwardToWlan_Object = MibScalar
brzRxForwardToWlan = _BrzRxForwardToWlan_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 1, 8),
    _BrzRxForwardToWlan_Type()
)
brzRxForwardToWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzRxForwardToWlan.setStatus("mandatory")
_BrzWlanCnt_ObjectIdentity = ObjectIdentity
brzWlanCnt = _BrzWlanCnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2)
)
_BrzTxWlanCnt_ObjectIdentity = ObjectIdentity
brzTxWlanCnt = _BrzTxWlanCnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1)
)
_BrzTxPacketsToWlan_Type = Counter32
_BrzTxPacketsToWlan_Object = MibScalar
brzTxPacketsToWlan = _BrzTxPacketsToWlan_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 1),
    _BrzTxPacketsToWlan_Type()
)
brzTxPacketsToWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTxPacketsToWlan.setStatus("mandatory")
_BrzTxMSDUToWlan_Type = Counter32
_BrzTxMSDUToWlan_Object = MibScalar
brzTxMSDUToWlan = _BrzTxMSDUToWlan_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 2),
    _BrzTxMSDUToWlan_Type()
)
brzTxMSDUToWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTxMSDUToWlan.setStatus("mandatory")
_BrzDiscarded_Type = Counter32
_BrzDiscarded_Object = MibScalar
brzDiscarded = _BrzDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 3),
    _BrzDiscarded_Type()
)
brzDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzDiscarded.setStatus("mandatory")
_BrzTxFragToWlan_Type = Counter32
_BrzTxFragToWlan_Object = MibScalar
brzTxFragToWlan = _BrzTxFragToWlan_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 4),
    _BrzTxFragToWlan_Type()
)
brzTxFragToWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTxFragToWlan.setStatus("mandatory")
_BrzRetryOnWlan_Type = Counter32
_BrzRetryOnWlan_Object = MibScalar
brzRetryOnWlan = _BrzRetryOnWlan_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 5),
    _BrzRetryOnWlan_Type()
)
brzRetryOnWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzRetryOnWlan.setStatus("mandatory")
_BrzFailedCountOnWlan_Type = Counter32
_BrzFailedCountOnWlan_Object = MibScalar
brzFailedCountOnWlan = _BrzFailedCountOnWlan_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 6),
    _BrzFailedCountOnWlan_Type()
)
brzFailedCountOnWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzFailedCountOnWlan.setStatus("mandatory")
_BrzRetryOnWlanPercent_Type = Counter32
_BrzRetryOnWlanPercent_Object = MibScalar
brzRetryOnWlanPercent = _BrzRetryOnWlanPercent_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 7),
    _BrzRetryOnWlanPercent_Type()
)
brzRetryOnWlanPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzRetryOnWlanPercent.setStatus("mandatory")
_BrzRetryTxDataToWlan_Type = Counter32
_BrzRetryTxDataToWlan_Object = MibScalar
brzRetryTxDataToWlan = _BrzRetryTxDataToWlan_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 8),
    _BrzRetryTxDataToWlan_Type()
)
brzRetryTxDataToWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzRetryTxDataToWlan.setStatus("mandatory")
_BrzRetryTxDataToWlanPercent_Type = Counter32
_BrzRetryTxDataToWlanPercent_Object = MibScalar
brzRetryTxDataToWlanPercent = _BrzRetryTxDataToWlanPercent_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 9),
    _BrzRetryTxDataToWlanPercent_Type()
)
brzRetryTxDataToWlanPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzRetryTxDataToWlanPercent.setStatus("mandatory")
_BrzTotalTxPacketsToWlan_Type = Counter32
_BrzTotalTxPacketsToWlan_Object = MibScalar
brzTotalTxPacketsToWlan = _BrzTotalTxPacketsToWlan_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 10),
    _BrzTotalTxPacketsToWlan_Type()
)
brzTotalTxPacketsToWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTotalTxPacketsToWlan.setStatus("mandatory")
_BrzTxErrTransmitions_ObjectIdentity = ObjectIdentity
brzTxErrTransmitions = _BrzTxErrTransmitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 15)
)
_BrzTxErrorAckTimeOut_Type = Counter32
_BrzTxErrorAckTimeOut_Object = MibScalar
brzTxErrorAckTimeOut = _BrzTxErrorAckTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 15, 1),
    _BrzTxErrorAckTimeOut_Type()
)
brzTxErrorAckTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTxErrorAckTimeOut.setStatus("mandatory")
_BrzTxErrorAckCRC_Type = Counter32
_BrzTxErrorAckCRC_Object = MibScalar
brzTxErrorAckCRC = _BrzTxErrorAckCRC_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 15, 2),
    _BrzTxErrorAckCRC_Type()
)
brzTxErrorAckCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTxErrorAckCRC.setStatus("mandatory")
_BrzTxErrorNoTimeUntilHop_Type = Counter32
_BrzTxErrorNoTimeUntilHop_Object = MibScalar
brzTxErrorNoTimeUntilHop = _BrzTxErrorNoTimeUntilHop_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 15, 3),
    _BrzTxErrorNoTimeUntilHop_Type()
)
brzTxErrorNoTimeUntilHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTxErrorNoTimeUntilHop.setStatus("mandatory")
_BrzTxErrorUnderRunAndCTS_Type = Counter32
_BrzTxErrorUnderRunAndCTS_Object = MibScalar
brzTxErrorUnderRunAndCTS = _BrzTxErrorUnderRunAndCTS_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 15, 4),
    _BrzTxErrorUnderRunAndCTS_Type()
)
brzTxErrorUnderRunAndCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTxErrorUnderRunAndCTS.setStatus("mandatory")
_BrzTxErrorAbort_Type = Counter32
_BrzTxErrorAbort_Object = MibScalar
brzTxErrorAbort = _BrzTxErrorAbort_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 15, 5),
    _BrzTxErrorAbort_Type()
)
brzTxErrorAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTxErrorAbort.setStatus("mandatory")
_BrzTxErrorFrameReceived_Type = Counter32
_BrzTxErrorFrameReceived_Object = MibScalar
brzTxErrorFrameReceived = _BrzTxErrorFrameReceived_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 1, 15, 6),
    _BrzTxErrorFrameReceived_Type()
)
brzTxErrorFrameReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTxErrorFrameReceived.setStatus("mandatory")
_BrzRxWlanCnt_ObjectIdentity = ObjectIdentity
brzRxWlanCnt = _BrzRxWlanCnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 2)
)
_BrzRxPacketsFromWlan_Type = Counter32
_BrzRxPacketsFromWlan_Object = MibScalar
brzRxPacketsFromWlan = _BrzRxPacketsFromWlan_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 2, 1),
    _BrzRxPacketsFromWlan_Type()
)
brzRxPacketsFromWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzRxPacketsFromWlan.setStatus("mandatory")
_BrzRxMSDUFromWlan_Type = Counter32
_BrzRxMSDUFromWlan_Object = MibScalar
brzRxMSDUFromWlan = _BrzRxMSDUFromWlan_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 2, 2),
    _BrzRxMSDUFromWlan_Type()
)
brzRxMSDUFromWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzRxMSDUFromWlan.setStatus("mandatory")
_BrzRxFragFromWlan_Type = Counter32
_BrzRxFragFromWlan_Object = MibScalar
brzRxFragFromWlan = _BrzRxFragFromWlan_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 2, 3),
    _BrzRxFragFromWlan_Type()
)
brzRxFragFromWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzRxFragFromWlan.setStatus("mandatory")
_BrzRxBadFragFromWlan_Type = Counter32
_BrzRxBadFragFromWlan_Object = MibScalar
brzRxBadFragFromWlan = _BrzRxBadFragFromWlan_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 2, 4),
    _BrzRxBadFragFromWlan_Type()
)
brzRxBadFragFromWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzRxBadFragFromWlan.setStatus("mandatory")
_BrzRxDuplicateFragFromWlan_Type = Counter32
_BrzRxDuplicateFragFromWlan_Object = MibScalar
brzRxDuplicateFragFromWlan = _BrzRxDuplicateFragFromWlan_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 2, 5),
    _BrzRxDuplicateFragFromWlan_Type()
)
brzRxDuplicateFragFromWlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzRxDuplicateFragFromWlan.setStatus("mandatory")
_FreqStatisticsTable_Object = MibTable
freqStatisticsTable = _FreqStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 2, 6)
)
if mibBuilder.loadTexts:
    freqStatisticsTable.setStatus("mandatory")
_FreqStatisticsEntry_Object = MibTableRow
freqStatisticsEntry = _FreqStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 2, 6, 1)
)
freqStatisticsEntry.setIndexNames(
    (0, "BREEZECOM-MIB", "freqStatisticsIndex"),
)
if mibBuilder.loadTexts:
    freqStatisticsEntry.setStatus("mandatory")
_FreqStatisticsIndex_Type = Integer32
_FreqStatisticsIndex_Object = MibTableColumn
freqStatisticsIndex = _FreqStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 2, 6, 1, 1),
    _FreqStatisticsIndex_Type()
)
freqStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freqStatisticsIndex.setStatus("mandatory")
_FreqNo_Type = Integer32
_FreqNo_Object = MibTableColumn
freqNo = _FreqNo_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 2, 6, 1, 2),
    _FreqNo_Type()
)
freqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freqNo.setStatus("mandatory")
_FreqTotalReceived_Type = Counter32
_FreqTotalReceived_Object = MibTableColumn
freqTotalReceived = _FreqTotalReceived_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 2, 2, 6, 1, 3),
    _FreqTotalReceived_Type()
)
freqTotalReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freqTotalReceived.setStatus("mandatory")
_BrzRoamCnt_ObjectIdentity = ObjectIdentity
brzRoamCnt = _BrzRoamCnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 3)
)
_BrzNumOfReassocRequests_Type = Counter32
_BrzNumOfReassocRequests_Object = MibScalar
brzNumOfReassocRequests = _BrzNumOfReassocRequests_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 3, 1),
    _BrzNumOfReassocRequests_Type()
)
brzNumOfReassocRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzNumOfReassocRequests.setStatus("mandatory")
_BrzMngCnt_ObjectIdentity = ObjectIdentity
brzMngCnt = _BrzMngCnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4)
)
_BrzMngAP_ObjectIdentity = ObjectIdentity
brzMngAP = _BrzMngAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 1)
)
_ProbeResponseSent_Type = Counter32
_ProbeResponseSent_Object = MibScalar
probeResponseSent = _ProbeResponseSent_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 1, 1),
    _ProbeResponseSent_Type()
)
probeResponseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeResponseSent.setStatus("mandatory")
_ProbeResponseLost_Type = Counter32
_ProbeResponseLost_Object = MibScalar
probeResponseLost = _ProbeResponseLost_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 1, 2),
    _ProbeResponseLost_Type()
)
probeResponseLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeResponseLost.setStatus("mandatory")
_ProbeResponseSentRetx_Type = Counter32
_ProbeResponseSentRetx_Object = MibScalar
probeResponseSentRetx = _ProbeResponseSentRetx_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 1, 3),
    _ProbeResponseSentRetx_Type()
)
probeResponseSentRetx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeResponseSentRetx.setStatus("mandatory")
_ProbeRequestRecive_Type = Counter32
_ProbeRequestRecive_Object = MibScalar
probeRequestRecive = _ProbeRequestRecive_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 1, 4),
    _ProbeRequestRecive_Type()
)
probeRequestRecive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeRequestRecive.setStatus("mandatory")
_AssocResponseSent_Type = Counter32
_AssocResponseSent_Object = MibScalar
assocResponseSent = _AssocResponseSent_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 1, 5),
    _AssocResponseSent_Type()
)
assocResponseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocResponseSent.setStatus("mandatory")
_AssocResponseLost_Type = Counter32
_AssocResponseLost_Object = MibScalar
assocResponseLost = _AssocResponseLost_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 1, 6),
    _AssocResponseLost_Type()
)
assocResponseLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocResponseLost.setStatus("mandatory")
_AssocResponseSentRetx_Type = Counter32
_AssocResponseSentRetx_Object = MibScalar
assocResponseSentRetx = _AssocResponseSentRetx_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 1, 7),
    _AssocResponseSentRetx_Type()
)
assocResponseSentRetx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocResponseSentRetx.setStatus("mandatory")
_AssocRequestRecive_Type = Counter32
_AssocRequestRecive_Object = MibScalar
assocRequestRecive = _AssocRequestRecive_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 1, 8),
    _AssocRequestRecive_Type()
)
assocRequestRecive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocRequestRecive.setStatus("mandatory")
_ReAssocRequestRecive_Type = Counter32
_ReAssocRequestRecive_Object = MibScalar
reAssocRequestRecive = _ReAssocRequestRecive_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 1, 9),
    _ReAssocRequestRecive_Type()
)
reAssocRequestRecive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reAssocRequestRecive.setStatus("mandatory")
_BrzMngSAWB_ObjectIdentity = ObjectIdentity
brzMngSAWB = _BrzMngSAWB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 2)
)
_ProbRequestSent_Type = Counter32
_ProbRequestSent_Object = MibScalar
probRequestSent = _ProbRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 2, 1),
    _ProbRequestSent_Type()
)
probRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probRequestSent.setStatus("mandatory")
_ProbResponceRecive_Type = Counter32
_ProbResponceRecive_Object = MibScalar
probResponceRecive = _ProbResponceRecive_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 2, 2),
    _ProbResponceRecive_Type()
)
probResponceRecive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probResponceRecive.setStatus("mandatory")
_AuthRequestSent_Type = Counter32
_AuthRequestSent_Object = MibScalar
authRequestSent = _AuthRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 2, 3),
    _AuthRequestSent_Type()
)
authRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authRequestSent.setStatus("mandatory")
_AuthRequestSentRetx_Type = Counter32
_AuthRequestSentRetx_Object = MibScalar
authRequestSentRetx = _AuthRequestSentRetx_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 2, 4),
    _AuthRequestSentRetx_Type()
)
authRequestSentRetx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authRequestSentRetx.setStatus("mandatory")
_AuthResponceRecive_Type = Counter32
_AuthResponceRecive_Object = MibScalar
authResponceRecive = _AuthResponceRecive_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 2, 5),
    _AuthResponceRecive_Type()
)
authResponceRecive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authResponceRecive.setStatus("mandatory")
_AssocRequestSent_Type = Counter32
_AssocRequestSent_Object = MibScalar
assocRequestSent = _AssocRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 2, 6),
    _AssocRequestSent_Type()
)
assocRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocRequestSent.setStatus("mandatory")
_AssocRequestSentRetx_Type = Counter32
_AssocRequestSentRetx_Object = MibScalar
assocRequestSentRetx = _AssocRequestSentRetx_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 2, 7),
    _AssocRequestSentRetx_Type()
)
assocRequestSentRetx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocRequestSentRetx.setStatus("mandatory")
_AssocResponceRecive_Type = Counter32
_AssocResponceRecive_Object = MibScalar
assocResponceRecive = _AssocResponceRecive_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 4, 2, 8),
    _AssocResponceRecive_Type()
)
assocResponceRecive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocResponceRecive.setStatus("mandatory")
_BrzPSCnt_ObjectIdentity = ObjectIdentity
brzPSCnt = _BrzPSCnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 5)
)
_PSFreeEntries_Type = Counter32
_PSFreeEntries_Object = MibScalar
pSFreeEntries = _PSFreeEntries_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 5, 1),
    _PSFreeEntries_Type()
)
pSFreeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSFreeEntries.setStatus("mandatory")
_PSInternallydiscarded_Type = Counter32
_PSInternallydiscarded_Object = MibScalar
pSInternallydiscarded = _PSInternallydiscarded_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 5, 2),
    _PSInternallydiscarded_Type()
)
pSInternallydiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSInternallydiscarded.setStatus("mandatory")
_PSstations_Type = Counter32
_PSstations_Object = MibScalar
pSstations = _PSstations_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 5, 3),
    _PSstations_Type()
)
pSstations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSstations.setStatus("mandatory")
_PSPowerSavingAged_Type = Counter32
_PSPowerSavingAged_Object = MibScalar
pSPowerSavingAged = _PSPowerSavingAged_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 5, 4),
    _PSPowerSavingAged_Type()
)
pSPowerSavingAged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pSPowerSavingAged.setStatus("mandatory")
_PowreStationsTable_Object = MibTable
powreStationsTable = _PowreStationsTable_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 5, 5)
)
if mibBuilder.loadTexts:
    powreStationsTable.setStatus("mandatory")
_PowreStationsEntry_Object = MibTableRow
powreStationsEntry = _PowreStationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 5, 5, 1)
)
powreStationsEntry.setIndexNames(
    (0, "BREEZECOM-MIB", "powerSaveIndex"),
)
if mibBuilder.loadTexts:
    powreStationsEntry.setStatus("mandatory")
_PowerSaveIndex_Type = Integer32
_PowerSaveIndex_Object = MibTableColumn
powerSaveIndex = _PowerSaveIndex_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 5, 5, 1, 1),
    _PowerSaveIndex_Type()
)
powerSaveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSaveIndex.setStatus("mandatory")
_PowerSaveStationID_Type = Integer32
_PowerSaveStationID_Object = MibTableColumn
powerSaveStationID = _PowerSaveStationID_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 5, 5, 1, 2),
    _PowerSaveStationID_Type()
)
powerSaveStationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSaveStationID.setStatus("mandatory")
_PowerSaveBuffered_Type = Integer32
_PowerSaveBuffered_Object = MibTableColumn
powerSaveBuffered = _PowerSaveBuffered_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 5, 5, 1, 3),
    _PowerSaveBuffered_Type()
)
powerSaveBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSaveBuffered.setStatus("mandatory")
_PowerSaveAged_Type = Integer32
_PowerSaveAged_Object = MibTableColumn
powerSaveAged = _PowerSaveAged_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 5, 5, 1, 4),
    _PowerSaveAged_Type()
)
powerSaveAged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSaveAged.setStatus("mandatory")
_PowerSaveSent_Type = Integer32
_PowerSaveSent_Object = MibTableColumn
powerSaveSent = _PowerSaveSent_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 5, 5, 1, 5),
    _PowerSaveSent_Type()
)
powerSaveSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSaveSent.setStatus("mandatory")
_PowerSaveQueueFull_Type = Integer32
_PowerSaveQueueFull_Object = MibTableColumn
powerSaveQueueFull = _PowerSaveQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 4, 5, 5, 1, 6),
    _PowerSaveQueueFull_Type()
)
powerSaveQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSaveQueueFull.setStatus("mandatory")
_BrzTraps_ObjectIdentity = ObjectIdentity
brzTraps = _BrzTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 5)
)
_BrzTrapAPMacAddr_Type = MacAddress
_BrzTrapAPMacAddr_Object = MibScalar
brzTrapAPMacAddr = _BrzTrapAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 5, 1),
    _BrzTrapAPMacAddr_Type()
)
brzTrapAPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTrapAPMacAddr.setStatus("mandatory")
_BrzTrapSTAMacAddr_Type = MacAddress
_BrzTrapSTAMacAddr_Object = MibScalar
brzTrapSTAMacAddr = _BrzTrapSTAMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 5, 2),
    _BrzTrapSTAMacAddr_Type()
)
brzTrapSTAMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTrapSTAMacAddr.setStatus("mandatory")
_BrzTrapMacAddress_Type = MacAddress
_BrzTrapMacAddress_Object = MibScalar
brzTrapMacAddress = _BrzTrapMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 5, 3),
    _BrzTrapMacAddress_Type()
)
brzTrapMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTrapMacAddress.setStatus("mandatory")
_BrzTrapRssiQuality_Type = Integer32
_BrzTrapRssiQuality_Object = MibScalar
brzTrapRssiQuality = _BrzTrapRssiQuality_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 5, 4),
    _BrzTrapRssiQuality_Type()
)
brzTrapRssiQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTrapRssiQuality.setStatus("mandatory")
_BrzTrapLastRssiQuality_Type = Integer32
_BrzTrapLastRssiQuality_Object = MibScalar
brzTrapLastRssiQuality = _BrzTrapLastRssiQuality_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 5, 5),
    _BrzTrapLastRssiQuality_Type()
)
brzTrapLastRssiQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTrapLastRssiQuality.setStatus("mandatory")
_BrzTrapIndex_Type = Integer32
_BrzTrapIndex_Object = MibScalar
brzTrapIndex = _BrzTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 5, 6),
    _BrzTrapIndex_Type()
)
brzTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTrapIndex.setStatus("mandatory")
_BrzTrapText_Type = DisplayString
_BrzTrapText_Object = MibScalar
brzTrapText = _BrzTrapText_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 5, 7),
    _BrzTrapText_Type()
)
brzTrapText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTrapText.setStatus("mandatory")


class _BrzTrapToggle_Type(Integer32):
    """Custom type brzTrapToggle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_BrzTrapToggle_Type.__name__ = "Integer32"
_BrzTrapToggle_Object = MibScalar
brzTrapToggle = _BrzTrapToggle_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 5, 8),
    _BrzTrapToggle_Type()
)
brzTrapToggle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTrapToggle.setStatus("mandatory")


class _BrzTrapSTAType_Type(Integer32):
    """Custom type brzTrapSTAType based on Integer32"""
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
        *(("breeze-new", 5),
          ("sa-pc", 4),
          ("sa10", 1),
          ("sa40", 3),
          ("unknown", 6),
          ("wb10", 2))
    )


_BrzTrapSTAType_Type.__name__ = "Integer32"
_BrzTrapSTAType_Object = MibScalar
brzTrapSTAType = _BrzTrapSTAType_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 5, 9),
    _BrzTrapSTAType_Type()
)
brzTrapSTAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brzTrapSTAType.setStatus("mandatory")
_Brzdot11_ObjectIdentity = ObjectIdentity
brzdot11 = _Brzdot11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6)
)
_Dot11smt_ObjectIdentity = ObjectIdentity
dot11smt = _Dot11smt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 1)
)
_Dot11DefaultWEPKeys_ObjectIdentity = ObjectIdentity
dot11DefaultWEPKeys = _Dot11DefaultWEPKeys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 1, 3)
)
_Dot11DefaultWEPKey1_Type = DisplayString
_Dot11DefaultWEPKey1_Object = MibScalar
dot11DefaultWEPKey1 = _Dot11DefaultWEPKey1_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 1, 3, 1),
    _Dot11DefaultWEPKey1_Type()
)
dot11DefaultWEPKey1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DefaultWEPKey1.setStatus("mandatory")
_Dot11DefaultWEPKey2_Type = DisplayString
_Dot11DefaultWEPKey2_Object = MibScalar
dot11DefaultWEPKey2 = _Dot11DefaultWEPKey2_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 1, 3, 2),
    _Dot11DefaultWEPKey2_Type()
)
dot11DefaultWEPKey2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DefaultWEPKey2.setStatus("mandatory")
_Dot11DefaultWEPKey3_Type = DisplayString
_Dot11DefaultWEPKey3_Object = MibScalar
dot11DefaultWEPKey3 = _Dot11DefaultWEPKey3_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 1, 3, 3),
    _Dot11DefaultWEPKey3_Type()
)
dot11DefaultWEPKey3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DefaultWEPKey3.setStatus("mandatory")
_Dot11DefaultWEPKey4_Type = DisplayString
_Dot11DefaultWEPKey4_Object = MibScalar
dot11DefaultWEPKey4 = _Dot11DefaultWEPKey4_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 1, 3, 4),
    _Dot11DefaultWEPKey4_Type()
)
dot11DefaultWEPKey4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DefaultWEPKey4.setStatus("mandatory")
_Dot11PrivacyGrp_ObjectIdentity = ObjectIdentity
dot11PrivacyGrp = _Dot11PrivacyGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 1, 6)
)


class _Dot11Preauthentication_Type(Integer32):
    """Custom type dot11Preauthentication based on Integer32"""
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


_Dot11Preauthentication_Type.__name__ = "Integer32"
_Dot11Preauthentication_Object = MibScalar
dot11Preauthentication = _Dot11Preauthentication_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 1, 6, 1),
    _Dot11Preauthentication_Type()
)
dot11Preauthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Preauthentication.setStatus("mandatory")


class _Dot11PrivacyOptionImplemented_Type(Integer32):
    """Custom type dot11PrivacyOptionImplemented based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Dot11PrivacyOptionImplemented_Type.__name__ = "Integer32"
_Dot11PrivacyOptionImplemented_Object = MibScalar
dot11PrivacyOptionImplemented = _Dot11PrivacyOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 1, 6, 2),
    _Dot11PrivacyOptionImplemented_Type()
)
dot11PrivacyOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PrivacyOptionImplemented.setStatus("mandatory")
_Dot11PrivacyInvoke_Type = Integer32
_Dot11PrivacyInvoke_Object = MibScalar
dot11PrivacyInvoke = _Dot11PrivacyInvoke_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 1, 6, 3),
    _Dot11PrivacyInvoke_Type()
)
dot11PrivacyInvoke.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11PrivacyInvoke.setStatus("mandatory")
_Dot11WEPDefaultKeyID_Type = Integer32
_Dot11WEPDefaultKeyID_Object = MibScalar
dot11WEPDefaultKeyID = _Dot11WEPDefaultKeyID_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 1, 6, 4),
    _Dot11WEPDefaultKeyID_Type()
)
dot11WEPDefaultKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WEPDefaultKeyID.setStatus("mandatory")
_Dot11mac_ObjectIdentity = ObjectIdentity
dot11mac = _Dot11mac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 2)
)
_Dot11OperationGrp_ObjectIdentity = ObjectIdentity
dot11OperationGrp = _Dot11OperationGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 2, 1)
)
_Dot11MaxMulticastRate_Type = Integer32
_Dot11MaxMulticastRate_Object = MibScalar
dot11MaxMulticastRate = _Dot11MaxMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 2, 1, 1),
    _Dot11MaxMulticastRate_Type()
)
dot11MaxMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MaxMulticastRate.setStatus("mandatory")
_Dot11DwellTime_Type = Integer32
_Dot11DwellTime_Object = MibScalar
dot11DwellTime = _Dot11DwellTime_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 2, 1, 2),
    _Dot11DwellTime_Type()
)
dot11DwellTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DwellTime.setStatus("mandatory")
_Dot11RTSThreshold_Type = Integer32
_Dot11RTSThreshold_Object = MibScalar
dot11RTSThreshold = _Dot11RTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 2, 1, 3),
    _Dot11RTSThreshold_Type()
)
dot11RTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RTSThreshold.setStatus("mandatory")
_Dot11ShortRetryLimit_Type = Integer32
_Dot11ShortRetryLimit_Object = MibScalar
dot11ShortRetryLimit = _Dot11ShortRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 2, 1, 4),
    _Dot11ShortRetryLimit_Type()
)
dot11ShortRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ShortRetryLimit.setStatus("mandatory")
_Dot11DwellRetryLimit_Type = Integer32
_Dot11DwellRetryLimit_Object = MibScalar
dot11DwellRetryLimit = _Dot11DwellRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 2, 1, 5),
    _Dot11DwellRetryLimit_Type()
)
dot11DwellRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DwellRetryLimit.setStatus("mandatory")
_Dot11FragmentationThreshold_Type = Integer32
_Dot11FragmentationThreshold_Object = MibScalar
dot11FragmentationThreshold = _Dot11FragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 2, 1, 6),
    _Dot11FragmentationThreshold_Type()
)
dot11FragmentationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11FragmentationThreshold.setStatus("mandatory")
_Dot11ShortRetryLimitForVoice_Type = Integer32
_Dot11ShortRetryLimitForVoice_Object = MibScalar
dot11ShortRetryLimitForVoice = _Dot11ShortRetryLimitForVoice_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 2, 1, 7),
    _Dot11ShortRetryLimitForVoice_Type()
)
dot11ShortRetryLimitForVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11ShortRetryLimitForVoice.setStatus("mandatory")
_Dot11DwellRetryLimitForVoice_Type = Integer32
_Dot11DwellRetryLimitForVoice_Object = MibScalar
dot11DwellRetryLimitForVoice = _Dot11DwellRetryLimitForVoice_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 2, 1, 8),
    _Dot11DwellRetryLimitForVoice_Type()
)
dot11DwellRetryLimitForVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DwellRetryLimitForVoice.setStatus("mandatory")
_Dot11res_ObjectIdentity = ObjectIdentity
dot11res = _Dot11res_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 3)
)
_Dot11resAttribute_ObjectIdentity = ObjectIdentity
dot11resAttribute = _Dot11resAttribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 3, 8)
)
_Dot11ResourceInfo_ObjectIdentity = ObjectIdentity
dot11ResourceInfo = _Dot11ResourceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 3, 8, 2)
)


class _Dot11CurrentStationStatus_Type(DisplayString):
    """Custom type dot11CurrentStationStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_Dot11CurrentStationStatus_Type.__name__ = "DisplayString"
_Dot11CurrentStationStatus_Object = MibScalar
dot11CurrentStationStatus = _Dot11CurrentStationStatus_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 3, 8, 2, 1),
    _Dot11CurrentStationStatus_Type()
)
dot11CurrentStationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11CurrentStationStatus.setStatus("mandatory")
_Dot11TotalNumberOfAssocSinceLastReset_Type = Counter32
_Dot11TotalNumberOfAssocSinceLastReset_Object = MibScalar
dot11TotalNumberOfAssocSinceLastReset = _Dot11TotalNumberOfAssocSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 3, 8, 2, 2),
    _Dot11TotalNumberOfAssocSinceLastReset_Type()
)
dot11TotalNumberOfAssocSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11TotalNumberOfAssocSinceLastReset.setStatus("mandatory")


class _Dot11manufacturerName_Type(DisplayString):
    """Custom type dot11manufacturerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_Dot11manufacturerName_Type.__name__ = "DisplayString"
_Dot11manufacturerName_Object = MibScalar
dot11manufacturerName = _Dot11manufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 3, 8, 2, 3),
    _Dot11manufacturerName_Type()
)
dot11manufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11manufacturerName.setStatus("mandatory")


class _Dot11manufacturerProductName_Type(DisplayString):
    """Custom type dot11manufacturerProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_Dot11manufacturerProductName_Type.__name__ = "DisplayString"
_Dot11manufacturerProductName_Object = MibScalar
dot11manufacturerProductName = _Dot11manufacturerProductName_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 3, 8, 2, 4),
    _Dot11manufacturerProductName_Type()
)
dot11manufacturerProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11manufacturerProductName.setStatus("mandatory")


class _Dot11manufacturerProductVersion_Type(DisplayString):
    """Custom type dot11manufacturerProductVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_Dot11manufacturerProductVersion_Type.__name__ = "DisplayString"
_Dot11manufacturerProductVersion_Object = MibScalar
dot11manufacturerProductVersion = _Dot11manufacturerProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 3, 8, 2, 5),
    _Dot11manufacturerProductVersion_Type()
)
dot11manufacturerProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11manufacturerProductVersion.setStatus("mandatory")
_Dot11phy_ObjectIdentity = ObjectIdentity
dot11phy = _Dot11phy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 4)
)
_Dot11PhyOperationGrp_ObjectIdentity = ObjectIdentity
dot11PhyOperationGrp = _Dot11PhyOperationGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 4, 1)
)


class _Dot11CurrentRegDomain_Type(Integer32):
    """Custom type dot11CurrentRegDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              32,
              48,
              49,
              50,
              55,
              56,
              64,
              65,
              72,
              73,
              96)
        )
    )
    namedValues = NamedValues(
        *(("australia", 73),
          ("canada", 32),
          ("ethairnet", 0),
          ("europe", 48),
          ("europe-dd", 55),
          ("france", 50),
          ("israel", 72),
          ("japan", 64),
          ("korea", 65),
          ("netherlands", 56),
          ("proprietary", 96),
          ("spain", 49),
          ("usa", 16))
    )


_Dot11CurrentRegDomain_Type.__name__ = "Integer32"
_Dot11CurrentRegDomain_Object = MibScalar
dot11CurrentRegDomain = _Dot11CurrentRegDomain_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 4, 1, 3),
    _Dot11CurrentRegDomain_Type()
)
dot11CurrentRegDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentRegDomain.setStatus("mandatory")
_Dot11PhyAntennaGrp_ObjectIdentity = ObjectIdentity
dot11PhyAntennaGrp = _Dot11PhyAntennaGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 4, 3)
)
_Dot11CurrentTxAntenna_Type = Integer32
_Dot11CurrentTxAntenna_Object = MibScalar
dot11CurrentTxAntenna = _Dot11CurrentTxAntenna_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 4, 3, 2),
    _Dot11CurrentTxAntenna_Type()
)
dot11CurrentTxAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentTxAntenna.setStatus("mandatory")
_Dot11PhyTxPwrGrp_ObjectIdentity = ObjectIdentity
dot11PhyTxPwrGrp = _Dot11PhyTxPwrGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 4, 4)
)


class _Dot11CurrentTxPwrLvl_Type(Integer32):
    """Custom type dot11CurrentTxPwrLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_Dot11CurrentTxPwrLvl_Type.__name__ = "Integer32"
_Dot11CurrentTxPwrLvl_Object = MibScalar
dot11CurrentTxPwrLvl = _Dot11CurrentTxPwrLvl_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 4, 4, 11),
    _Dot11CurrentTxPwrLvl_Type()
)
dot11CurrentTxPwrLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentTxPwrLvl.setStatus("mandatory")
_Dot11PhyFHSSGrp_ObjectIdentity = ObjectIdentity
dot11PhyFHSSGrp = _Dot11PhyFHSSGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 4, 5)
)
_Dot11CurrentDwellTime_Type = Integer32
_Dot11CurrentDwellTime_Object = MibScalar
dot11CurrentDwellTime = _Dot11CurrentDwellTime_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 4, 5, 5),
    _Dot11CurrentDwellTime_Type()
)
dot11CurrentDwellTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentDwellTime.setStatus("mandatory")
_Dot11CurrentSet_Type = Integer32
_Dot11CurrentSet_Object = MibScalar
dot11CurrentSet = _Dot11CurrentSet_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 4, 5, 6),
    _Dot11CurrentSet_Type()
)
dot11CurrentSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentSet.setStatus("mandatory")
_Dot11CurrentPattern_Type = Integer32
_Dot11CurrentPattern_Object = MibScalar
dot11CurrentPattern = _Dot11CurrentPattern_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 4, 5, 7),
    _Dot11CurrentPattern_Type()
)
dot11CurrentPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11CurrentPattern.setStatus("mandatory")
_Dot11MultySupport_ObjectIdentity = ObjectIdentity
dot11MultySupport = _Dot11MultySupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 5)
)


class _Dot11MultyRateSupport_Type(Integer32):
    """Custom type dot11MultyRateSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Dot11MultyRateSupport_Type.__name__ = "Integer32"
_Dot11MultyRateSupport_Object = MibScalar
dot11MultyRateSupport = _Dot11MultyRateSupport_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 5, 1),
    _Dot11MultyRateSupport_Type()
)
dot11MultyRateSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MultyRateSupport.setStatus("mandatory")
_Dot11MultyRateDecisionWindow_Type = Integer32
_Dot11MultyRateDecisionWindow_Object = MibScalar
dot11MultyRateDecisionWindow = _Dot11MultyRateDecisionWindow_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 5, 2),
    _Dot11MultyRateDecisionWindow_Type()
)
dot11MultyRateDecisionWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MultyRateDecisionWindow.setStatus("mandatory")
_Dot11Maintenance_ObjectIdentity = ObjectIdentity
dot11Maintenance = _Dot11Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 6)
)


class _Dot11WaitforAssociationAddress_Type(Integer32):
    """Custom type dot11WaitforAssociationAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("get-from-ethernet", 1),
          ("use-mine", 0))
    )


_Dot11WaitforAssociationAddress_Type.__name__ = "Integer32"
_Dot11WaitforAssociationAddress_Object = MibScalar
dot11WaitforAssociationAddress = _Dot11WaitforAssociationAddress_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 6, 1),
    _Dot11WaitforAssociationAddress_Type()
)
dot11WaitforAssociationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WaitforAssociationAddress.setStatus("mandatory")


class _Dot11JapanCallSign_Type(DisplayString):
    """Custom type dot11JapanCallSign based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )


_Dot11JapanCallSign_Type.__name__ = "DisplayString"
_Dot11JapanCallSign_Object = MibScalar
dot11JapanCallSign = _Dot11JapanCallSign_Object(
    (1, 3, 6, 1, 4, 1, 710, 3, 2, 6, 6, 2),
    _Dot11JapanCallSign_Type()
)
dot11JapanCallSign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11JapanCallSign.setStatus("mandatory")
_BreezecomOID_ObjectIdentity = ObjectIdentity
breezecomOID = _BreezecomOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 4)
)
_BreezecomAP10_ObjectIdentity = ObjectIdentity
breezecomAP10 = _BreezecomAP10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 4, 1)
)
_BreezecomWB10_ObjectIdentity = ObjectIdentity
breezecomWB10 = _BreezecomWB10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 4, 2)
)
_BreezecomSA10_ObjectIdentity = ObjectIdentity
breezecomSA10 = _BreezecomSA10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 4, 3)
)
_BreezecomSA40_ObjectIdentity = ObjectIdentity
breezecomSA40 = _BreezecomSA40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 710, 4, 4)
)

# Managed Objects groups


# Notification objects

brzAProamingIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 1, 0, 1)
)
brzAProamingIn.setObjects(
      *(("BREEZECOM-MIB", "brzTrapSTAMacAddr"),
        ("BREEZECOM-MIB", "brzTrapSTAType"))
)
if mibBuilder.loadTexts:
    brzAProamingIn.setStatus(
        ""
    )

brzAPassociated = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 1, 0, 2)
)
brzAPassociated.setObjects(
    ("BREEZECOM-MIB", "brzTrapSTAMacAddr")
)
if mibBuilder.loadTexts:
    brzAPassociated.setStatus(
        ""
    )

brzAPdisassociated = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 1, 0, 3)
)
brzAPdisassociated.setObjects(
    ("BREEZECOM-MIB", "brzTrapSTAMacAddr")
)
if mibBuilder.loadTexts:
    brzAPdisassociated.setStatus(
        ""
    )

brzAPaging = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 1, 0, 4)
)
brzAPaging.setObjects(
    ("BREEZECOM-MIB", "brzTrapSTAMacAddr")
)
if mibBuilder.loadTexts:
    brzAPaging.setStatus(
        ""
    )

brzAProamedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 1, 0, 5)
)
brzAProamedOut.setObjects(
    ("BREEZECOM-MIB", "brzTrapSTAMacAddr")
)
if mibBuilder.loadTexts:
    brzAProamedOut.setStatus(
        ""
    )

brzAPWlanStatusap = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 1, 0, 7)
)
brzAPWlanStatusap.setObjects(
      *(("BREEZECOM-MIB", "brzTrapToggle"),
        ("BREEZECOM-MIB", "brzTrapMacAddress"))
)
if mibBuilder.loadTexts:
    brzAPWlanStatusap.setStatus(
        ""
    )

brzWlanStatusOfStation = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 1, 0, 8)
)
brzWlanStatusOfStation.setObjects(
      *(("BREEZECOM-MIB", "brzTrapToggle"),
        ("BREEZECOM-MIB", "brzTrapMacAddress"))
)
if mibBuilder.loadTexts:
    brzWlanStatusOfStation.setStatus(
        ""
    )

brzGeneralAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 1, 0, 9)
)
brzGeneralAP.setObjects(
      *(("BREEZECOM-MIB", "brzTrapIndex"),
        ("BREEZECOM-MIB", "brzTrapText"))
)
if mibBuilder.loadTexts:
    brzGeneralAP.setStatus(
        ""
    )

brzWBassociated = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 2, 0, 6)
)
brzWBassociated.setObjects(
      *(("BREEZECOM-MIB", "brzLastAPMacAddress"),
        ("BREEZECOM-MIB", "brzTrapAPMacAddr"),
        ("BREEZECOM-MIB", "brzTrapLastRssiQuality"),
        ("BREEZECOM-MIB", "brzTrapRssiQuality"))
)
if mibBuilder.loadTexts:
    brzWBassociated.setStatus(
        ""
    )

brzWBWlanStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 2, 0, 7)
)
brzWBWlanStatus.setObjects(
      *(("BREEZECOM-MIB", "brzTrapToggle"),
        ("BREEZECOM-MIB", "brzTrapMacAddress"))
)
if mibBuilder.loadTexts:
    brzWBWlanStatus.setStatus(
        ""
    )

brzGeneralWB = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 2, 0, 9)
)
brzGeneralWB.setObjects(
      *(("BREEZECOM-MIB", "brzTrapIndex"),
        ("BREEZECOM-MIB", "brzTrapText"))
)
if mibBuilder.loadTexts:
    brzGeneralWB.setStatus(
        ""
    )

brzSTAassociated = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 3, 0, 6)
)
brzSTAassociated.setObjects(
      *(("BREEZECOM-MIB", "brzLastAPMacAddress"),
        ("BREEZECOM-MIB", "brzTrapAPMacAddr"),
        ("BREEZECOM-MIB", "brzTrapLastRssiQuality"),
        ("BREEZECOM-MIB", "brzTrapRssiQuality"))
)
if mibBuilder.loadTexts:
    brzSTAassociated.setStatus(
        ""
    )

brzSTAWlanStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 3, 0, 7)
)
brzSTAWlanStatus.setObjects(
      *(("BREEZECOM-MIB", "brzTrapToggle"),
        ("BREEZECOM-MIB", "brzTrapMacAddress"))
)
if mibBuilder.loadTexts:
    brzSTAWlanStatus.setStatus(
        ""
    )

brzGeneralSTA = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 3, 0, 9)
)
brzGeneralSTA.setObjects(
      *(("BREEZECOM-MIB", "brzTrapIndex"),
        ("BREEZECOM-MIB", "brzTrapText"))
)
if mibBuilder.loadTexts:
    brzGeneralSTA.setStatus(
        ""
    )

brzSA40associated = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 4, 0, 6)
)
brzSA40associated.setObjects(
      *(("BREEZECOM-MIB", "brzLastAPMacAddress"),
        ("BREEZECOM-MIB", "brzTrapAPMacAddr"),
        ("BREEZECOM-MIB", "brzTrapLastRssiQuality"),
        ("BREEZECOM-MIB", "brzTrapRssiQuality"))
)
if mibBuilder.loadTexts:
    brzSA40associated.setStatus(
        ""
    )

brzSA40WlanStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 4, 0, 7)
)
brzSA40WlanStatus.setObjects(
      *(("BREEZECOM-MIB", "brzTrapToggle"),
        ("BREEZECOM-MIB", "brzTrapMacAddress"))
)
if mibBuilder.loadTexts:
    brzSA40WlanStatus.setStatus(
        ""
    )

brzGeneralSA40 = NotificationType(
    (1, 3, 6, 1, 4, 1, 710, 4, 4, 0, 9)
)
brzGeneralSA40.setObjects(
      *(("BREEZECOM-MIB", "brzTrapIndex"),
        ("BREEZECOM-MIB", "brzTrapText"))
)
if mibBuilder.loadTexts:
    brzGeneralSA40.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BREEZECOM-MIB",
    **{"MacAddress": MacAddress,
       "breezecom": breezecom,
       "breezecomPrvRev": breezecomPrvRev,
       "brznetmib": brznetmib,
       "brzSys": brzSys,
       "sysCmd": sysCmd,
       "sysReset": sysReset,
       "sysSetDefaults": sysSetDefaults,
       "sysResetCounters": sysResetCounters,
       "sysTrapEnable": sysTrapEnable,
       "sysTrapCounter": sysTrapCounter,
       "sysCarrierSense": sysCarrierSense,
       "sysDeltaCarrierSense": sysDeltaCarrierSense,
       "sysPartialDefaults": sysPartialDefaults,
       "sysRunFromNonActiveCode": sysRunFromNonActiveCode,
       "accessRights": accessRights,
       "sysDisplayAccessRights": sysDisplayAccessRights,
       "sysChangeRightsToUSER": sysChangeRightsToUSER,
       "sysChangeRightsToINSTALLER": sysChangeRightsToINSTALLER,
       "sysChangeRightsToTECHNICIAN": sysChangeRightsToTECHNICIAN,
       "sysChangeInstallerPassword": sysChangeInstallerPassword,
       "sysNoiseFloor": sysNoiseFloor,
       "sysExternalAmplifier": sysExternalAmplifier,
       "sysParams": sysParams,
       "brzHWMacAddress": brzHWMacAddress,
       "brzApplTunneling": brzApplTunneling,
       "brzPositiveBrg": brzPositiveBrg,
       "brzIpFilter": brzIpFilter,
       "brzTranslationMode": brzTranslationMode,
       "brzWIXSupport": brzWIXSupport,
       "brzWlanNetID": brzWlanNetID,
       "brzAuthenticationType": brzAuthenticationType,
       "brzWlanRTNetID": brzWlanRTNetID,
       "brzApRedundancySupport": brzApRedundancySupport,
       "brzWlanRelayUnicast": brzWlanRelayUnicast,
       "brzWlanRelayBroadcast": brzWlanRelayBroadcast,
       "brzApRedundancyLimit": brzApRedundancyLimit,
       "brzStaNumForLargeCW": brzStaNumForLargeCW,
       "brzPowerMngMode": brzPowerMngMode,
       "brzACKDelayed": brzACKDelayed,
       "brzDTIMPperiod": brzDTIMPperiod,
       "brzPowerMngBitTestMode": brzPowerMngBitTestMode,
       "brzBeaconInterval": brzBeaconInterval,
       "brzPowerSaveSupport": brzPowerSaveSupport,
       "brzWlanAssocAge": brzWlanAssocAge,
       "brzEnableVoice": brzEnableVoice,
       "brzNonActiveCodeState": brzNonActiveCodeState,
       "brzDisplayNonActiveCodeVersion": brzDisplayNonActiveCodeVersion,
       "brzIntelligentBridgingPeriod": brzIntelligentBridgingPeriod,
       "ipParams": ipParams,
       "trapHostsTable": trapHostsTable,
       "trapHostsEntry": trapHostsEntry,
       "trapHostsIndex": trapHostsIndex,
       "trapIPaddress": trapIPaddress,
       "trapCommunity": trapCommunity,
       "ipAddr": ipAddr,
       "maskIP": maskIP,
       "readCommunity": readCommunity,
       "writeCommunity": writeCommunity,
       "gatewayIPaddr": gatewayIPaddr,
       "brzIPStack": brzIPStack,
       "brzWlan": brzWlan,
       "brzWlanParams": brzWlanParams,
       "brzMaxRate": brzMaxRate,
       "brzMobilLvl": brzMobilLvl,
       "brzAvrgRssi": brzAvrgRssi,
       "brzWlanProtocol": brzWlanProtocol,
       "brzWlanTrapThreashold": brzWlanTrapThreashold,
       "brzWlanQuality": brzWlanQuality,
       "knownAPsTable": knownAPsTable,
       "knownAPsEntry": knownAPsEntry,
       "knownAPsIndex": knownAPsIndex,
       "knownAPsValue": knownAPsValue,
       "knownAPsQuality": knownAPsQuality,
       "knownAPsAvrgRssi": knownAPsAvrgRssi,
       "knownAPsStatus": knownAPsStatus,
       "knownAPsLoadStations": knownAPsLoadStations,
       "knownAPsGoodBeacons": knownAPsGoodBeacons,
       "knownAPsTotalBeacons": knownAPsTotalBeacons,
       "knownAPsAvrgDbm": knownAPsAvrgDbm,
       "brzLastBeacon": brzLastBeacon,
       "brzBadBeacons": brzBadBeacons,
       "brzLoadStations": brzLoadStations,
       "brzAvrgDBm": brzAvrgDBm,
       "brzAP": brzAP,
       "bssInfo": bssInfo,
       "bssNumOfStations": bssNumOfStations,
       "bssNumOfStationsPeak": bssNumOfStationsPeak,
       "bssCollectPerStationInfo": bssCollectPerStationInfo,
       "bssNumOfBeaconSent": bssNumOfBeaconSent,
       "bssNumOfBeaconLost": bssNumOfBeaconLost,
       "bssNumOfStationsAuthenticated": bssNumOfStationsAuthenticated,
       "bssNumOfStationsAuthenticatedPeak": bssNumOfStationsAuthenticatedPeak,
       "bssApAdb": bssApAdb,
       "adbTable": adbTable,
       "adbEntry": adbEntry,
       "stAddress": stAddress,
       "stCFMode": stCFMode,
       "stMaxRate": stMaxRate,
       "stCurTxRate": stCurTxRate,
       "stRssi": stRssi,
       "stPMMode": stPMMode,
       "stTxFragments": stTxFragments,
       "stTxFragments1M": stTxFragments1M,
       "stTxFragments2M": stTxFragments2M,
       "stTxFragments3M": stTxFragments3M,
       "stTxRetry": stTxRetry,
       "stTxDroppedPackets": stTxDroppedPackets,
       "stRxFragments": stRxFragments,
       "stWlanStatus": stWlanStatus,
       "stResetCounters": stResetCounters,
       "stType": stType,
       "stTxRetryPercent": stTxRetryPercent,
       "stReTxFragments1M": stReTxFragments1M,
       "stReTxFragments2M": stReTxFragments2M,
       "stReTxFragments3M": stReTxFragments3M,
       "stDbm": stDbm,
       "brzSTA": brzSTA,
       "brzCurrentAPMacAddress": brzCurrentAPMacAddress,
       "brzLastAPMacAddress": brzLastAPMacAddress,
       "brzPreferredAPMacAddress": brzPreferredAPMacAddress,
       "brzRoamToAPMacAddress": brzRoamToAPMacAddress,
       "brzCFMode": brzCFMode,
       "brzTx1MBitRate": brzTx1MBitRate,
       "brzTx2MBitRate": brzTx2MBitRate,
       "brzTx3MBitRate": brzTx3MBitRate,
       "brzTotalRetx": brzTotalRetx,
       "brzRoamParams": brzRoamParams,
       "brzRoamDecisionWin": brzRoamDecisionWin,
       "brzRoamDecisionNumerator": brzRoamDecisionNumerator,
       "brzRoamDecisionRSSIThreshold": brzRoamDecisionRSSIThreshold,
       "brzJoinDecisionRSSIThreshold": brzJoinDecisionRSSIThreshold,
       "brzNeighboringBeacons": brzNeighboringBeacons,
       "brzNumberOfProbeResponses": brzNumberOfProbeResponses,
       "brzNumberOfBeaconsForDisconnect": brzNumberOfBeaconsForDisconnect,
       "brzMaxNumberOfScanning": brzMaxNumberOfScanning,
       "brzNeighboringBeaconRate": brzNeighboringBeaconRate,
       "brzCnt": brzCnt,
       "brzDSCnt": brzDSCnt,
       "brzRxFromDS": brzRxFromDS,
       "brzRxBadFromDS": brzRxBadFromDS,
       "brzRxOctetsFromDS": brzRxOctetsFromDS,
       "brzTxToDS": brzTxToDS,
       "brzMissedFrames": brzMissedFrames,
       "brzTxOctetsToDS": brzTxOctetsToDS,
       "brzRxOctetsForwardToWlan": brzRxOctetsForwardToWlan,
       "brzRxForwardToWlan": brzRxForwardToWlan,
       "brzWlanCnt": brzWlanCnt,
       "brzTxWlanCnt": brzTxWlanCnt,
       "brzTxPacketsToWlan": brzTxPacketsToWlan,
       "brzTxMSDUToWlan": brzTxMSDUToWlan,
       "brzDiscarded": brzDiscarded,
       "brzTxFragToWlan": brzTxFragToWlan,
       "brzRetryOnWlan": brzRetryOnWlan,
       "brzFailedCountOnWlan": brzFailedCountOnWlan,
       "brzRetryOnWlanPercent": brzRetryOnWlanPercent,
       "brzRetryTxDataToWlan": brzRetryTxDataToWlan,
       "brzRetryTxDataToWlanPercent": brzRetryTxDataToWlanPercent,
       "brzTotalTxPacketsToWlan": brzTotalTxPacketsToWlan,
       "brzTxErrTransmitions": brzTxErrTransmitions,
       "brzTxErrorAckTimeOut": brzTxErrorAckTimeOut,
       "brzTxErrorAckCRC": brzTxErrorAckCRC,
       "brzTxErrorNoTimeUntilHop": brzTxErrorNoTimeUntilHop,
       "brzTxErrorUnderRunAndCTS": brzTxErrorUnderRunAndCTS,
       "brzTxErrorAbort": brzTxErrorAbort,
       "brzTxErrorFrameReceived": brzTxErrorFrameReceived,
       "brzRxWlanCnt": brzRxWlanCnt,
       "brzRxPacketsFromWlan": brzRxPacketsFromWlan,
       "brzRxMSDUFromWlan": brzRxMSDUFromWlan,
       "brzRxFragFromWlan": brzRxFragFromWlan,
       "brzRxBadFragFromWlan": brzRxBadFragFromWlan,
       "brzRxDuplicateFragFromWlan": brzRxDuplicateFragFromWlan,
       "freqStatisticsTable": freqStatisticsTable,
       "freqStatisticsEntry": freqStatisticsEntry,
       "freqStatisticsIndex": freqStatisticsIndex,
       "freqNo": freqNo,
       "freqTotalReceived": freqTotalReceived,
       "brzRoamCnt": brzRoamCnt,
       "brzNumOfReassocRequests": brzNumOfReassocRequests,
       "brzMngCnt": brzMngCnt,
       "brzMngAP": brzMngAP,
       "probeResponseSent": probeResponseSent,
       "probeResponseLost": probeResponseLost,
       "probeResponseSentRetx": probeResponseSentRetx,
       "probeRequestRecive": probeRequestRecive,
       "assocResponseSent": assocResponseSent,
       "assocResponseLost": assocResponseLost,
       "assocResponseSentRetx": assocResponseSentRetx,
       "assocRequestRecive": assocRequestRecive,
       "reAssocRequestRecive": reAssocRequestRecive,
       "brzMngSAWB": brzMngSAWB,
       "probRequestSent": probRequestSent,
       "probResponceRecive": probResponceRecive,
       "authRequestSent": authRequestSent,
       "authRequestSentRetx": authRequestSentRetx,
       "authResponceRecive": authResponceRecive,
       "assocRequestSent": assocRequestSent,
       "assocRequestSentRetx": assocRequestSentRetx,
       "assocResponceRecive": assocResponceRecive,
       "brzPSCnt": brzPSCnt,
       "pSFreeEntries": pSFreeEntries,
       "pSInternallydiscarded": pSInternallydiscarded,
       "pSstations": pSstations,
       "pSPowerSavingAged": pSPowerSavingAged,
       "powreStationsTable": powreStationsTable,
       "powreStationsEntry": powreStationsEntry,
       "powerSaveIndex": powerSaveIndex,
       "powerSaveStationID": powerSaveStationID,
       "powerSaveBuffered": powerSaveBuffered,
       "powerSaveAged": powerSaveAged,
       "powerSaveSent": powerSaveSent,
       "powerSaveQueueFull": powerSaveQueueFull,
       "brzTraps": brzTraps,
       "brzTrapAPMacAddr": brzTrapAPMacAddr,
       "brzTrapSTAMacAddr": brzTrapSTAMacAddr,
       "brzTrapMacAddress": brzTrapMacAddress,
       "brzTrapRssiQuality": brzTrapRssiQuality,
       "brzTrapLastRssiQuality": brzTrapLastRssiQuality,
       "brzTrapIndex": brzTrapIndex,
       "brzTrapText": brzTrapText,
       "brzTrapToggle": brzTrapToggle,
       "brzTrapSTAType": brzTrapSTAType,
       "brzdot11": brzdot11,
       "dot11smt": dot11smt,
       "dot11DefaultWEPKeys": dot11DefaultWEPKeys,
       "dot11DefaultWEPKey1": dot11DefaultWEPKey1,
       "dot11DefaultWEPKey2": dot11DefaultWEPKey2,
       "dot11DefaultWEPKey3": dot11DefaultWEPKey3,
       "dot11DefaultWEPKey4": dot11DefaultWEPKey4,
       "dot11PrivacyGrp": dot11PrivacyGrp,
       "dot11Preauthentication": dot11Preauthentication,
       "dot11PrivacyOptionImplemented": dot11PrivacyOptionImplemented,
       "dot11PrivacyInvoke": dot11PrivacyInvoke,
       "dot11WEPDefaultKeyID": dot11WEPDefaultKeyID,
       "dot11mac": dot11mac,
       "dot11OperationGrp": dot11OperationGrp,
       "dot11MaxMulticastRate": dot11MaxMulticastRate,
       "dot11DwellTime": dot11DwellTime,
       "dot11RTSThreshold": dot11RTSThreshold,
       "dot11ShortRetryLimit": dot11ShortRetryLimit,
       "dot11DwellRetryLimit": dot11DwellRetryLimit,
       "dot11FragmentationThreshold": dot11FragmentationThreshold,
       "dot11ShortRetryLimitForVoice": dot11ShortRetryLimitForVoice,
       "dot11DwellRetryLimitForVoice": dot11DwellRetryLimitForVoice,
       "dot11res": dot11res,
       "dot11resAttribute": dot11resAttribute,
       "dot11ResourceInfo": dot11ResourceInfo,
       "dot11CurrentStationStatus": dot11CurrentStationStatus,
       "dot11TotalNumberOfAssocSinceLastReset": dot11TotalNumberOfAssocSinceLastReset,
       "dot11manufacturerName": dot11manufacturerName,
       "dot11manufacturerProductName": dot11manufacturerProductName,
       "dot11manufacturerProductVersion": dot11manufacturerProductVersion,
       "dot11phy": dot11phy,
       "dot11PhyOperationGrp": dot11PhyOperationGrp,
       "dot11CurrentRegDomain": dot11CurrentRegDomain,
       "dot11PhyAntennaGrp": dot11PhyAntennaGrp,
       "dot11CurrentTxAntenna": dot11CurrentTxAntenna,
       "dot11PhyTxPwrGrp": dot11PhyTxPwrGrp,
       "dot11CurrentTxPwrLvl": dot11CurrentTxPwrLvl,
       "dot11PhyFHSSGrp": dot11PhyFHSSGrp,
       "dot11CurrentDwellTime": dot11CurrentDwellTime,
       "dot11CurrentSet": dot11CurrentSet,
       "dot11CurrentPattern": dot11CurrentPattern,
       "dot11MultySupport": dot11MultySupport,
       "dot11MultyRateSupport": dot11MultyRateSupport,
       "dot11MultyRateDecisionWindow": dot11MultyRateDecisionWindow,
       "dot11Maintenance": dot11Maintenance,
       "dot11WaitforAssociationAddress": dot11WaitforAssociationAddress,
       "dot11JapanCallSign": dot11JapanCallSign,
       "breezecomOID": breezecomOID,
       "breezecomAP10": breezecomAP10,
       "brzAProamingIn": brzAProamingIn,
       "brzAPassociated": brzAPassociated,
       "brzAPdisassociated": brzAPdisassociated,
       "brzAPaging": brzAPaging,
       "brzAProamedOut": brzAProamedOut,
       "brzAPWlanStatusap": brzAPWlanStatusap,
       "brzWlanStatusOfStation": brzWlanStatusOfStation,
       "brzGeneralAP": brzGeneralAP,
       "breezecomWB10": breezecomWB10,
       "brzWBassociated": brzWBassociated,
       "brzWBWlanStatus": brzWBWlanStatus,
       "brzGeneralWB": brzGeneralWB,
       "breezecomSA10": breezecomSA10,
       "brzSTAassociated": brzSTAassociated,
       "brzSTAWlanStatus": brzSTAWlanStatus,
       "brzGeneralSTA": brzGeneralSTA,
       "breezecomSA40": breezecomSA40,
       "brzSA40associated": brzSA40associated,
       "brzSA40WlanStatus": brzSA40WlanStatus,
       "brzGeneralSA40": brzGeneralSA40}
)
