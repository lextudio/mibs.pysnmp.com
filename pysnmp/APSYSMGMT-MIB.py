# SNMP MIB module (APSYSMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APSYSMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:03 2024
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

(ApHardwareModuleFamily,
 ApRedundancyState) = mibBuilder.importSymbols(
    "ACMEPACKET-TC",
    "ApHardwareModuleFamily",
    "ApRedundancyState")

(apLicenseDatabaseRegCap,) = mibBuilder.importSymbols(
    "APLICENSE-MIB",
    "apLicenseDatabaseRegCap")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetVersion,
 InetZoneIndex) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetVersion",
    "InetZoneIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

apSystemManagementModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2)
)
apSystemManagementModule.setRevisions(
        ("2012-02-06 12:00",
         "2007-07-11 12:00",
         "2005-01-04 12:00",
         "2003-01-06 12:00",
         "2012-07-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SysMgmtPercentage(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class ApSessionAgentStatusOptions(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("constraintsViolation", 4),
          ("disabled", 0),
          ("inService", 3),
          ("inServiceTimedOut", 5),
          ("oosprovisionedresponse", 6),
          ("outOfService", 1),
          ("standby", 2))
    )



class ApSessionAgentType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("h323", 2),
          ("sip", 1))
    )



class ApNetMgmtCtrlType(Integer32, TextualConvention):
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
        *(("gap-percent", 2),
          ("gap-rate", 1),
          ("priority", 3))
    )



class ApSipInterfaceStatusOptions(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("constraintsViolation", 4),
          ("inService", 3))
    )



class ApSigRealmStatusOptions(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("callLoadReduction", 7),
          ("constraintsViolation", 4),
          ("inService", 3))
    )



class ApNetMgmtCtrlState(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_ApSysMgmtMIBObjects_ObjectIdentity = ObjectIdentity
apSysMgmtMIBObjects = _ApSysMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1)
)
_ApSysMgmtMIBGeneralObjects_ObjectIdentity = ObjectIdentity
apSysMgmtMIBGeneralObjects = _ApSysMgmtMIBGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1)
)
_ApSysCPUUtil_Type = SysMgmtPercentage
_ApSysCPUUtil_Object = MibScalar
apSysCPUUtil = _ApSysCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 1),
    _ApSysCPUUtil_Type()
)
apSysCPUUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysCPUUtil.setStatus("current")
_ApSysMemoryUtil_Type = SysMgmtPercentage
_ApSysMemoryUtil_Object = MibScalar
apSysMemoryUtil = _ApSysMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 2),
    _ApSysMemoryUtil_Type()
)
apSysMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysMemoryUtil.setStatus("current")
_ApSysHealthScore_Type = SysMgmtPercentage
_ApSysHealthScore_Object = MibScalar
apSysHealthScore = _ApSysHealthScore_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 3),
    _ApSysHealthScore_Type()
)
apSysHealthScore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysHealthScore.setStatus("current")
_ApSysRedundancy_Type = ApRedundancyState
_ApSysRedundancy_Object = MibScalar
apSysRedundancy = _ApSysRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 4),
    _ApSysRedundancy_Type()
)
apSysRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysRedundancy.setStatus("current")
_ApSysGlobalConSess_Type = Integer32
_ApSysGlobalConSess_Object = MibScalar
apSysGlobalConSess = _ApSysGlobalConSess_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 5),
    _ApSysGlobalConSess_Type()
)
apSysGlobalConSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysGlobalConSess.setStatus("current")
if mibBuilder.loadTexts:
    apSysGlobalConSess.setUnits("sessions")
_ApSysGlobalCPS_Type = Integer32
_ApSysGlobalCPS_Object = MibScalar
apSysGlobalCPS = _ApSysGlobalCPS_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 6),
    _ApSysGlobalCPS_Type()
)
apSysGlobalCPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysGlobalCPS.setStatus("current")
if mibBuilder.loadTexts:
    apSysGlobalCPS.setUnits("calls")
_ApSysNATCapacity_Type = SysMgmtPercentage
_ApSysNATCapacity_Object = MibScalar
apSysNATCapacity = _ApSysNATCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 7),
    _ApSysNATCapacity_Type()
)
apSysNATCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysNATCapacity.setStatus("current")
_ApSysARPCapacity_Type = SysMgmtPercentage
_ApSysARPCapacity_Object = MibScalar
apSysARPCapacity = _ApSysARPCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 8),
    _ApSysARPCapacity_Type()
)
apSysARPCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysARPCapacity.setStatus("current")


class _ApSysState_Type(Integer32):
    """Custom type apSysState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("becomingoffline", 1),
          ("offline", 2),
          ("online", 0))
    )


_ApSysState_Type.__name__ = "Integer32"
_ApSysState_Object = MibScalar
apSysState = _ApSysState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 9),
    _ApSysState_Type()
)
apSysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysState.setStatus("current")
_ApSysLicenseCapacity_Type = SysMgmtPercentage
_ApSysLicenseCapacity_Object = MibScalar
apSysLicenseCapacity = _ApSysLicenseCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 10),
    _ApSysLicenseCapacity_Type()
)
apSysLicenseCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysLicenseCapacity.setStatus("current")
_ApSysSipStatsActiveLocalContacts_Type = Unsigned32
_ApSysSipStatsActiveLocalContacts_Object = MibScalar
apSysSipStatsActiveLocalContacts = _ApSysSipStatsActiveLocalContacts_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 11),
    _ApSysSipStatsActiveLocalContacts_Type()
)
apSysSipStatsActiveLocalContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysSipStatsActiveLocalContacts.setStatus("current")
_ApSysMgcpGWEndpoints_Type = Unsigned32
_ApSysMgcpGWEndpoints_Object = MibScalar
apSysMgcpGWEndpoints = _ApSysMgcpGWEndpoints_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 12),
    _ApSysMgcpGWEndpoints_Type()
)
apSysMgcpGWEndpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysMgcpGWEndpoints.setStatus("current")
_ApSysH323Registration_Type = Unsigned32
_ApSysH323Registration_Object = MibScalar
apSysH323Registration = _ApSysH323Registration_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 13),
    _ApSysH323Registration_Type()
)
apSysH323Registration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysH323Registration.setStatus("current")
_ApSysRegCacheLimit_Type = Integer32
_ApSysRegCacheLimit_Object = MibScalar
apSysRegCacheLimit = _ApSysRegCacheLimit_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 14),
    _ApSysRegCacheLimit_Type()
)
apSysRegCacheLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysRegCacheLimit.setStatus("current")
if mibBuilder.loadTexts:
    apSysRegCacheLimit.setUnits("contacts")
_ApSysShortSessionThreshold_Type = Unsigned32
_ApSysShortSessionThreshold_Object = MibScalar
apSysShortSessionThreshold = _ApSysShortSessionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 15),
    _ApSysShortSessionThreshold_Type()
)
apSysShortSessionThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysShortSessionThreshold.setStatus("current")
if mibBuilder.loadTexts:
    apSysShortSessionThreshold.setUnits("sessions")
_ApSysApplicationCPULoadRate_Type = SysMgmtPercentage
_ApSysApplicationCPULoadRate_Object = MibScalar
apSysApplicationCPULoadRate = _ApSysApplicationCPULoadRate_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 16),
    _ApSysApplicationCPULoadRate_Type()
)
apSysApplicationCPULoadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysApplicationCPULoadRate.setStatus("current")
_ApSysRegistrationCapacity_Type = SysMgmtPercentage
_ApSysRegistrationCapacity_Object = MibScalar
apSysRegistrationCapacity = _ApSysRegistrationCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 17),
    _ApSysRegistrationCapacity_Type()
)
apSysRegistrationCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysRegistrationCapacity.setStatus("obsolete")
_ApSysRejectedMessages_Type = Counter32
_ApSysRejectedMessages_Object = MibScalar
apSysRejectedMessages = _ApSysRejectedMessages_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 18),
    _ApSysRejectedMessages_Type()
)
apSysRejectedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysRejectedMessages.setStatus("current")
_ApSysSipEndptDemTrustToUntrust_Type = Unsigned32
_ApSysSipEndptDemTrustToUntrust_Object = MibScalar
apSysSipEndptDemTrustToUntrust = _ApSysSipEndptDemTrustToUntrust_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 19),
    _ApSysSipEndptDemTrustToUntrust_Type()
)
apSysSipEndptDemTrustToUntrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysSipEndptDemTrustToUntrust.setStatus("current")
_ApSysSipEndptDemUntrustToDeny_Type = Unsigned32
_ApSysSipEndptDemUntrustToDeny_Object = MibScalar
apSysSipEndptDemUntrustToDeny = _ApSysSipEndptDemUntrustToDeny_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 20),
    _ApSysSipEndptDemUntrustToDeny_Type()
)
apSysSipEndptDemUntrustToDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysSipEndptDemUntrustToDeny.setStatus("current")
_ApSysMgcpEndptDemTrustToUntrust_Type = Unsigned32
_ApSysMgcpEndptDemTrustToUntrust_Object = MibScalar
apSysMgcpEndptDemTrustToUntrust = _ApSysMgcpEndptDemTrustToUntrust_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 21),
    _ApSysMgcpEndptDemTrustToUntrust_Type()
)
apSysMgcpEndptDemTrustToUntrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysMgcpEndptDemTrustToUntrust.setStatus("current")
_ApSysMgcpEndptDemUntrustToDeny_Type = Unsigned32
_ApSysMgcpEndptDemUntrustToDeny_Object = MibScalar
apSysMgcpEndptDemUntrustToDeny = _ApSysMgcpEndptDemUntrustToDeny_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 22),
    _ApSysMgcpEndptDemUntrustToDeny_Type()
)
apSysMgcpEndptDemUntrustToDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysMgcpEndptDemUntrustToDeny.setStatus("current")
_ApSysStorageSpaceTable_Object = MibTable
apSysStorageSpaceTable = _ApSysStorageSpaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 23)
)
if mibBuilder.loadTexts:
    apSysStorageSpaceTable.setStatus("current")
_ApSysStorageSpaceEntry_Object = MibTableRow
apSysStorageSpaceEntry = _ApSysStorageSpaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 23, 1)
)
apSysStorageSpaceEntry.setIndexNames(
    (0, "APSYSMGMT-MIB", "apSysVolumeIndex"),
)
if mibBuilder.loadTexts:
    apSysStorageSpaceEntry.setStatus("current")


class _ApSysVolumeIndex_Type(Integer32):
    """Custom type apSysVolumeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApSysVolumeIndex_Type.__name__ = "Integer32"
_ApSysVolumeIndex_Object = MibTableColumn
apSysVolumeIndex = _ApSysVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 23, 1, 1),
    _ApSysVolumeIndex_Type()
)
apSysVolumeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysVolumeIndex.setStatus("current")


class _ApSysVolumeName_Type(DisplayString):
    """Custom type apSysVolumeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSysVolumeName_Type.__name__ = "DisplayString"
_ApSysVolumeName_Object = MibTableColumn
apSysVolumeName = _ApSysVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 23, 1, 2),
    _ApSysVolumeName_Type()
)
apSysVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysVolumeName.setStatus("current")
_ApSysVolumeTotalSpace_Type = Unsigned32
_ApSysVolumeTotalSpace_Object = MibTableColumn
apSysVolumeTotalSpace = _ApSysVolumeTotalSpace_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 23, 1, 3),
    _ApSysVolumeTotalSpace_Type()
)
apSysVolumeTotalSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysVolumeTotalSpace.setStatus("current")
_ApSysVolumeAvailSpace_Type = Unsigned32
_ApSysVolumeAvailSpace_Object = MibTableColumn
apSysVolumeAvailSpace = _ApSysVolumeAvailSpace_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 23, 1, 4),
    _ApSysVolumeAvailSpace_Type()
)
apSysVolumeAvailSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysVolumeAvailSpace.setStatus("current")
_ApSysSipStatsActiveDatabaseContacts_Type = Unsigned32
_ApSysSipStatsActiveDatabaseContacts_Object = MibScalar
apSysSipStatsActiveDatabaseContacts = _ApSysSipStatsActiveDatabaseContacts_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 24),
    _ApSysSipStatsActiveDatabaseContacts_Type()
)
apSysSipStatsActiveDatabaseContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysSipStatsActiveDatabaseContacts.setStatus("current")
_ApSysSipTotalCallsRejected_Type = Unsigned32
_ApSysSipTotalCallsRejected_Object = MibScalar
apSysSipTotalCallsRejected = _ApSysSipTotalCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 25),
    _ApSysSipTotalCallsRejected_Type()
)
apSysSipTotalCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysSipTotalCallsRejected.setStatus("current")
_ApSysCurrentEndptsDenied_Type = Unsigned32
_ApSysCurrentEndptsDenied_Object = MibScalar
apSysCurrentEndptsDenied = _ApSysCurrentEndptsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 26),
    _ApSysCurrentEndptsDenied_Type()
)
apSysCurrentEndptsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysCurrentEndptsDenied.setStatus("current")
_ApSysSipStatsActiveSubscriptions_Type = Unsigned32
_ApSysSipStatsActiveSubscriptions_Object = MibScalar
apSysSipStatsActiveSubscriptions = _ApSysSipStatsActiveSubscriptions_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 27),
    _ApSysSipStatsActiveSubscriptions_Type()
)
apSysSipStatsActiveSubscriptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysSipStatsActiveSubscriptions.setStatus("current")
_ApSysSipStatsPerMaxSubscriptions_Type = Counter32
_ApSysSipStatsPerMaxSubscriptions_Object = MibScalar
apSysSipStatsPerMaxSubscriptions = _ApSysSipStatsPerMaxSubscriptions_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 28),
    _ApSysSipStatsPerMaxSubscriptions_Type()
)
apSysSipStatsPerMaxSubscriptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysSipStatsPerMaxSubscriptions.setStatus("current")
_ApSysSipStatsMaximumActiveSubscriptions_Type = Counter32
_ApSysSipStatsMaximumActiveSubscriptions_Object = MibScalar
apSysSipStatsMaximumActiveSubscriptions = _ApSysSipStatsMaximumActiveSubscriptions_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 29),
    _ApSysSipStatsMaximumActiveSubscriptions_Type()
)
apSysSipStatsMaximumActiveSubscriptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysSipStatsMaximumActiveSubscriptions.setStatus("current")
_ApSysSipStatsTotalSubscriptions_Type = Counter32
_ApSysSipStatsTotalSubscriptions_Object = MibScalar
apSysSipStatsTotalSubscriptions = _ApSysSipStatsTotalSubscriptions_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 30),
    _ApSysSipStatsTotalSubscriptions_Type()
)
apSysSipStatsTotalSubscriptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysSipStatsTotalSubscriptions.setStatus("current")
_ApSysMgmtH248MgcName_Type = DisplayString
_ApSysMgmtH248MgcName_Object = MibScalar
apSysMgmtH248MgcName = _ApSysMgmtH248MgcName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 31),
    _ApSysMgmtH248MgcName_Type()
)
apSysMgmtH248MgcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysMgmtH248MgcName.setStatus("current")
_ApSysMgmtH248Realm_Type = DisplayString
_ApSysMgmtH248Realm_Object = MibScalar
apSysMgmtH248Realm = _ApSysMgmtH248Realm_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 32),
    _ApSysMgmtH248Realm_Type()
)
apSysMgmtH248Realm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysMgmtH248Realm.setStatus("current")
_ApSysMgmtH248PortMapUsage_Type = Unsigned32
_ApSysMgmtH248PortMapUsage_Object = MibScalar
apSysMgmtH248PortMapUsage = _ApSysMgmtH248PortMapUsage_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 33),
    _ApSysMgmtH248PortMapUsage_Type()
)
apSysMgmtH248PortMapUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysMgmtH248PortMapUsage.setStatus("current")
_ApSysXCodeCapacity_Type = SysMgmtPercentage
_ApSysXCodeCapacity_Object = MibScalar
apSysXCodeCapacity = _ApSysXCodeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 34),
    _ApSysXCodeCapacity_Type()
)
apSysXCodeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysXCodeCapacity.setStatus("current")
_ApSysXCodeAMRCapacity_Type = SysMgmtPercentage
_ApSysXCodeAMRCapacity_Object = MibScalar
apSysXCodeAMRCapacity = _ApSysXCodeAMRCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 35),
    _ApSysXCodeAMRCapacity_Type()
)
apSysXCodeAMRCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysXCodeAMRCapacity.setStatus("current")
_ApSysXCodeAMRWBCapacity_Type = SysMgmtPercentage
_ApSysXCodeAMRWBCapacity_Object = MibScalar
apSysXCodeAMRWBCapacity = _ApSysXCodeAMRWBCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 36),
    _ApSysXCodeAMRWBCapacity_Type()
)
apSysXCodeAMRWBCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSysXCodeAMRWBCapacity.setStatus("current")
_ApSysETCCoreUtilTable_Object = MibTable
apSysETCCoreUtilTable = _ApSysETCCoreUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 37)
)
if mibBuilder.loadTexts:
    apSysETCCoreUtilTable.setStatus("current")
_ApSysETCCoreUtilEntry_Object = MibTableRow
apSysETCCoreUtilEntry = _ApSysETCCoreUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 37, 1)
)
apSysETCCoreUtilEntry.setIndexNames(
    (0, "APSYSMGMT-MIB", "apSysETCIndex"),
    (0, "APSYSMGMT-MIB", "apSysETCCoreIndex"),
)
if mibBuilder.loadTexts:
    apSysETCCoreUtilEntry.setStatus("current")


class _ApSysETCIndex_Type(Integer32):
    """Custom type apSysETCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApSysETCIndex_Type.__name__ = "Integer32"
_ApSysETCIndex_Object = MibTableColumn
apSysETCIndex = _ApSysETCIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 37, 1, 1),
    _ApSysETCIndex_Type()
)
apSysETCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSysETCIndex.setStatus("current")


class _ApSysETCCoreIndex_Type(Integer32):
    """Custom type apSysETCCoreIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApSysETCCoreIndex_Type.__name__ = "Integer32"
_ApSysETCCoreIndex_Object = MibTableColumn
apSysETCCoreIndex = _ApSysETCCoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 37, 1, 2),
    _ApSysETCCoreIndex_Type()
)
apSysETCCoreIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSysETCCoreIndex.setStatus("current")
_ApSysETCCoreCPUUtil_Type = SysMgmtPercentage
_ApSysETCCoreCPUUtil_Object = MibTableColumn
apSysETCCoreCPUUtil = _ApSysETCCoreCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 37, 1, 3),
    _ApSysETCCoreCPUUtil_Type()
)
apSysETCCoreCPUUtil.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysETCCoreCPUUtil.setStatus("current")
_ApSysETCMemoryPoolUtilTable_Object = MibTable
apSysETCMemoryPoolUtilTable = _ApSysETCMemoryPoolUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 38)
)
if mibBuilder.loadTexts:
    apSysETCMemoryPoolUtilTable.setStatus("current")
_ApSysETCMemoryPoolUtilEntry_Object = MibTableRow
apSysETCMemoryPoolUtilEntry = _ApSysETCMemoryPoolUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 38, 1)
)
apSysETCMemoryPoolUtilEntry.setIndexNames(
    (0, "APSYSMGMT-MIB", "apSysETCIndex"),
    (0, "APSYSMGMT-MIB", "apSysETCMemoryPoolIndex"),
)
if mibBuilder.loadTexts:
    apSysETCMemoryPoolUtilEntry.setStatus("current")


class _ApSysETCMemoryPoolIndex_Type(Integer32):
    """Custom type apSysETCMemoryPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApSysETCMemoryPoolIndex_Type.__name__ = "Integer32"
_ApSysETCMemoryPoolIndex_Object = MibTableColumn
apSysETCMemoryPoolIndex = _ApSysETCMemoryPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 38, 1, 1),
    _ApSysETCMemoryPoolIndex_Type()
)
apSysETCMemoryPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSysETCMemoryPoolIndex.setStatus("current")
_ApSysETCMemoryPoolMemUtil_Type = SysMgmtPercentage
_ApSysETCMemoryPoolMemUtil_Object = MibTableColumn
apSysETCMemoryPoolMemUtil = _ApSysETCMemoryPoolMemUtil_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 1, 38, 1, 2),
    _ApSysETCMemoryPoolMemUtil_Type()
)
apSysETCMemoryPoolMemUtil.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysETCMemoryPoolMemUtil.setStatus("current")
_ApSysMgmtMIBSessionObjects_ObjectIdentity = ObjectIdentity
apSysMgmtMIBSessionObjects = _ApSysMgmtMIBSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2)
)
_ApCombinedSessionAgentStatsTable_Object = MibTable
apCombinedSessionAgentStatsTable = _ApCombinedSessionAgentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    apCombinedSessionAgentStatsTable.setStatus("obsolete")
_ApCombinedSessionAgentStatsEntry_Object = MibTableRow
apCombinedSessionAgentStatsEntry = _ApCombinedSessionAgentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1)
)
apCombinedSessionAgentStatsEntry.setIndexNames(
    (0, "APSYSMGMT-MIB", "apCombinedStatsSessionAgentIndex"),
)
if mibBuilder.loadTexts:
    apCombinedSessionAgentStatsEntry.setStatus("obsolete")


class _ApCombinedStatsSessionAgentIndex_Type(Integer32):
    """Custom type apCombinedStatsSessionAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApCombinedStatsSessionAgentIndex_Type.__name__ = "Integer32"
_ApCombinedStatsSessionAgentIndex_Object = MibTableColumn
apCombinedStatsSessionAgentIndex = _ApCombinedStatsSessionAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 1),
    _ApCombinedStatsSessionAgentIndex_Type()
)
apCombinedStatsSessionAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsSessionAgentIndex.setStatus("obsolete")


class _ApCombinedStatsSessionAgentHostname_Type(DisplayString):
    """Custom type apCombinedStatsSessionAgentHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApCombinedStatsSessionAgentHostname_Type.__name__ = "DisplayString"
_ApCombinedStatsSessionAgentHostname_Object = MibTableColumn
apCombinedStatsSessionAgentHostname = _ApCombinedStatsSessionAgentHostname_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 2),
    _ApCombinedStatsSessionAgentHostname_Type()
)
apCombinedStatsSessionAgentHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsSessionAgentHostname.setStatus("obsolete")
_ApCombinedStatsSessionAgentType_Type = ApSessionAgentType
_ApCombinedStatsSessionAgentType_Object = MibTableColumn
apCombinedStatsSessionAgentType = _ApCombinedStatsSessionAgentType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 3),
    _ApCombinedStatsSessionAgentType_Type()
)
apCombinedStatsSessionAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsSessionAgentType.setStatus("obsolete")
_ApCombinedStatsCurrentActiveSessionsInbound_Type = Unsigned32
_ApCombinedStatsCurrentActiveSessionsInbound_Object = MibTableColumn
apCombinedStatsCurrentActiveSessionsInbound = _ApCombinedStatsCurrentActiveSessionsInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 4),
    _ApCombinedStatsCurrentActiveSessionsInbound_Type()
)
apCombinedStatsCurrentActiveSessionsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsCurrentActiveSessionsInbound.setStatus("obsolete")
_ApCombinedStatsCurrentSessionRateInbound_Type = Unsigned32
_ApCombinedStatsCurrentSessionRateInbound_Object = MibTableColumn
apCombinedStatsCurrentSessionRateInbound = _ApCombinedStatsCurrentSessionRateInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 5),
    _ApCombinedStatsCurrentSessionRateInbound_Type()
)
apCombinedStatsCurrentSessionRateInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsCurrentSessionRateInbound.setStatus("obsolete")
_ApCombinedStatsCurrentActiveSessionsOutbound_Type = Unsigned32
_ApCombinedStatsCurrentActiveSessionsOutbound_Object = MibTableColumn
apCombinedStatsCurrentActiveSessionsOutbound = _ApCombinedStatsCurrentActiveSessionsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 6),
    _ApCombinedStatsCurrentActiveSessionsOutbound_Type()
)
apCombinedStatsCurrentActiveSessionsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsCurrentActiveSessionsOutbound.setStatus("obsolete")
_ApCombinedStatsCurrentSessionRateOutbound_Type = Unsigned32
_ApCombinedStatsCurrentSessionRateOutbound_Object = MibTableColumn
apCombinedStatsCurrentSessionRateOutbound = _ApCombinedStatsCurrentSessionRateOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 7),
    _ApCombinedStatsCurrentSessionRateOutbound_Type()
)
apCombinedStatsCurrentSessionRateOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsCurrentSessionRateOutbound.setStatus("obsolete")
_ApCombinedStatsTotalSessionsInbound_Type = Counter32
_ApCombinedStatsTotalSessionsInbound_Object = MibTableColumn
apCombinedStatsTotalSessionsInbound = _ApCombinedStatsTotalSessionsInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 8),
    _ApCombinedStatsTotalSessionsInbound_Type()
)
apCombinedStatsTotalSessionsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsTotalSessionsInbound.setStatus("obsolete")
_ApCombinedStatsTotalSessionsNotAdmittedInbound_Type = Counter32
_ApCombinedStatsTotalSessionsNotAdmittedInbound_Object = MibTableColumn
apCombinedStatsTotalSessionsNotAdmittedInbound = _ApCombinedStatsTotalSessionsNotAdmittedInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 9),
    _ApCombinedStatsTotalSessionsNotAdmittedInbound_Type()
)
apCombinedStatsTotalSessionsNotAdmittedInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsTotalSessionsNotAdmittedInbound.setStatus("obsolete")
_ApCombinedStatsPeriodHighInbound_Type = Unsigned32
_ApCombinedStatsPeriodHighInbound_Object = MibTableColumn
apCombinedStatsPeriodHighInbound = _ApCombinedStatsPeriodHighInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 10),
    _ApCombinedStatsPeriodHighInbound_Type()
)
apCombinedStatsPeriodHighInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsPeriodHighInbound.setStatus("obsolete")
_ApCombinedStatsAverageRateInbound_Type = Unsigned32
_ApCombinedStatsAverageRateInbound_Object = MibTableColumn
apCombinedStatsAverageRateInbound = _ApCombinedStatsAverageRateInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 11),
    _ApCombinedStatsAverageRateInbound_Type()
)
apCombinedStatsAverageRateInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsAverageRateInbound.setStatus("obsolete")
_ApCombinedStatsTotalSessionsOutbound_Type = Counter32
_ApCombinedStatsTotalSessionsOutbound_Object = MibTableColumn
apCombinedStatsTotalSessionsOutbound = _ApCombinedStatsTotalSessionsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 12),
    _ApCombinedStatsTotalSessionsOutbound_Type()
)
apCombinedStatsTotalSessionsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsTotalSessionsOutbound.setStatus("obsolete")
_ApCombinedStatsTotalSessionsNotAdmittedOutbound_Type = Counter32
_ApCombinedStatsTotalSessionsNotAdmittedOutbound_Object = MibTableColumn
apCombinedStatsTotalSessionsNotAdmittedOutbound = _ApCombinedStatsTotalSessionsNotAdmittedOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 13),
    _ApCombinedStatsTotalSessionsNotAdmittedOutbound_Type()
)
apCombinedStatsTotalSessionsNotAdmittedOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsTotalSessionsNotAdmittedOutbound.setStatus("obsolete")
_ApCombinedStatsPeriodHighOutbound_Type = Unsigned32
_ApCombinedStatsPeriodHighOutbound_Object = MibTableColumn
apCombinedStatsPeriodHighOutbound = _ApCombinedStatsPeriodHighOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 14),
    _ApCombinedStatsPeriodHighOutbound_Type()
)
apCombinedStatsPeriodHighOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsPeriodHighOutbound.setStatus("obsolete")
_ApCombinedStatsAverageRateOutbound_Type = Unsigned32
_ApCombinedStatsAverageRateOutbound_Object = MibTableColumn
apCombinedStatsAverageRateOutbound = _ApCombinedStatsAverageRateOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 15),
    _ApCombinedStatsAverageRateOutbound_Type()
)
apCombinedStatsAverageRateOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsAverageRateOutbound.setStatus("obsolete")
_ApCombinedStatsMaxBurstRate_Type = Unsigned32
_ApCombinedStatsMaxBurstRate_Object = MibTableColumn
apCombinedStatsMaxBurstRate = _ApCombinedStatsMaxBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 16),
    _ApCombinedStatsMaxBurstRate_Type()
)
apCombinedStatsMaxBurstRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsMaxBurstRate.setStatus("obsolete")
_ApCombinedStatsPeriodSeizures_Type = Counter32
_ApCombinedStatsPeriodSeizures_Object = MibTableColumn
apCombinedStatsPeriodSeizures = _ApCombinedStatsPeriodSeizures_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 17),
    _ApCombinedStatsPeriodSeizures_Type()
)
apCombinedStatsPeriodSeizures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsPeriodSeizures.setStatus("obsolete")
_ApCombinedStatsPeriodAnswers_Type = Counter32
_ApCombinedStatsPeriodAnswers_Object = MibTableColumn
apCombinedStatsPeriodAnswers = _ApCombinedStatsPeriodAnswers_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 18),
    _ApCombinedStatsPeriodAnswers_Type()
)
apCombinedStatsPeriodAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsPeriodAnswers.setStatus("obsolete")
_ApCombinedStatsPeriodASR_Type = Unsigned32
_ApCombinedStatsPeriodASR_Object = MibTableColumn
apCombinedStatsPeriodASR = _ApCombinedStatsPeriodASR_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 19),
    _ApCombinedStatsPeriodASR_Type()
)
apCombinedStatsPeriodASR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsPeriodASR.setStatus("obsolete")
_ApCombinedStatsAverageLatency_Type = Unsigned32
_ApCombinedStatsAverageLatency_Object = MibTableColumn
apCombinedStatsAverageLatency = _ApCombinedStatsAverageLatency_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 20),
    _ApCombinedStatsAverageLatency_Type()
)
apCombinedStatsAverageLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsAverageLatency.setStatus("obsolete")
_ApCombinedStatsMaxLatency_Type = Unsigned32
_ApCombinedStatsMaxLatency_Object = MibTableColumn
apCombinedStatsMaxLatency = _ApCombinedStatsMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 21),
    _ApCombinedStatsMaxLatency_Type()
)
apCombinedStatsMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsMaxLatency.setStatus("obsolete")
_ApCombinedStatsSessionAgentStatus_Type = ApSessionAgentStatusOptions
_ApCombinedStatsSessionAgentStatus_Object = MibTableColumn
apCombinedStatsSessionAgentStatus = _ApCombinedStatsSessionAgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 1, 1, 22),
    _ApCombinedStatsSessionAgentStatus_Type()
)
apCombinedStatsSessionAgentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCombinedStatsSessionAgentStatus.setStatus("obsolete")
_ApSipSessionAgentStatsTable_Object = MibTable
apSipSessionAgentStatsTable = _ApSipSessionAgentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    apSipSessionAgentStatsTable.setStatus("current")
_ApSipSessionAgentStatsEntry_Object = MibTableRow
apSipSessionAgentStatsEntry = _ApSipSessionAgentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1)
)
apSipSessionAgentStatsEntry.setIndexNames(
    (0, "APSYSMGMT-MIB", "apSipSAStatsSessionAgentIndex"),
)
if mibBuilder.loadTexts:
    apSipSessionAgentStatsEntry.setStatus("current")


class _ApSipSAStatsSessionAgentIndex_Type(Integer32):
    """Custom type apSipSAStatsSessionAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApSipSAStatsSessionAgentIndex_Type.__name__ = "Integer32"
_ApSipSAStatsSessionAgentIndex_Object = MibTableColumn
apSipSAStatsSessionAgentIndex = _ApSipSAStatsSessionAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 1),
    _ApSipSAStatsSessionAgentIndex_Type()
)
apSipSAStatsSessionAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsSessionAgentIndex.setStatus("current")


class _ApSipSAStatsSessionAgentHostname_Type(DisplayString):
    """Custom type apSipSAStatsSessionAgentHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSipSAStatsSessionAgentHostname_Type.__name__ = "DisplayString"
_ApSipSAStatsSessionAgentHostname_Object = MibTableColumn
apSipSAStatsSessionAgentHostname = _ApSipSAStatsSessionAgentHostname_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 2),
    _ApSipSAStatsSessionAgentHostname_Type()
)
apSipSAStatsSessionAgentHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsSessionAgentHostname.setStatus("current")
_ApSipSAStatsSessionAgentType_Type = ApSessionAgentType
_ApSipSAStatsSessionAgentType_Object = MibTableColumn
apSipSAStatsSessionAgentType = _ApSipSAStatsSessionAgentType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 3),
    _ApSipSAStatsSessionAgentType_Type()
)
apSipSAStatsSessionAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsSessionAgentType.setStatus("current")
_ApSipSAStatsCurrentActiveSessionsInbound_Type = Unsigned32
_ApSipSAStatsCurrentActiveSessionsInbound_Object = MibTableColumn
apSipSAStatsCurrentActiveSessionsInbound = _ApSipSAStatsCurrentActiveSessionsInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 4),
    _ApSipSAStatsCurrentActiveSessionsInbound_Type()
)
apSipSAStatsCurrentActiveSessionsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsCurrentActiveSessionsInbound.setStatus("current")
_ApSipSAStatsCurrentSessionRateInbound_Type = Unsigned32
_ApSipSAStatsCurrentSessionRateInbound_Object = MibTableColumn
apSipSAStatsCurrentSessionRateInbound = _ApSipSAStatsCurrentSessionRateInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 5),
    _ApSipSAStatsCurrentSessionRateInbound_Type()
)
apSipSAStatsCurrentSessionRateInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsCurrentSessionRateInbound.setStatus("current")
_ApSipSAStatsCurrentActiveSessionsOutbound_Type = Unsigned32
_ApSipSAStatsCurrentActiveSessionsOutbound_Object = MibTableColumn
apSipSAStatsCurrentActiveSessionsOutbound = _ApSipSAStatsCurrentActiveSessionsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 6),
    _ApSipSAStatsCurrentActiveSessionsOutbound_Type()
)
apSipSAStatsCurrentActiveSessionsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsCurrentActiveSessionsOutbound.setStatus("current")
_ApSipSAStatsCurrentSessionRateOutbound_Type = Unsigned32
_ApSipSAStatsCurrentSessionRateOutbound_Object = MibTableColumn
apSipSAStatsCurrentSessionRateOutbound = _ApSipSAStatsCurrentSessionRateOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 7),
    _ApSipSAStatsCurrentSessionRateOutbound_Type()
)
apSipSAStatsCurrentSessionRateOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsCurrentSessionRateOutbound.setStatus("current")
_ApSipSAStatsTotalSessionsInbound_Type = Counter32
_ApSipSAStatsTotalSessionsInbound_Object = MibTableColumn
apSipSAStatsTotalSessionsInbound = _ApSipSAStatsTotalSessionsInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 8),
    _ApSipSAStatsTotalSessionsInbound_Type()
)
apSipSAStatsTotalSessionsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsTotalSessionsInbound.setStatus("current")
_ApSipSAStatsTotalSessionsNotAdmittedInbound_Type = Counter32
_ApSipSAStatsTotalSessionsNotAdmittedInbound_Object = MibTableColumn
apSipSAStatsTotalSessionsNotAdmittedInbound = _ApSipSAStatsTotalSessionsNotAdmittedInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 9),
    _ApSipSAStatsTotalSessionsNotAdmittedInbound_Type()
)
apSipSAStatsTotalSessionsNotAdmittedInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsTotalSessionsNotAdmittedInbound.setStatus("current")
_ApSipSAStatsPeriodHighInbound_Type = Unsigned32
_ApSipSAStatsPeriodHighInbound_Object = MibTableColumn
apSipSAStatsPeriodHighInbound = _ApSipSAStatsPeriodHighInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 10),
    _ApSipSAStatsPeriodHighInbound_Type()
)
apSipSAStatsPeriodHighInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsPeriodHighInbound.setStatus("current")
_ApSipSAStatsAverageRateInbound_Type = Unsigned32
_ApSipSAStatsAverageRateInbound_Object = MibTableColumn
apSipSAStatsAverageRateInbound = _ApSipSAStatsAverageRateInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 11),
    _ApSipSAStatsAverageRateInbound_Type()
)
apSipSAStatsAverageRateInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsAverageRateInbound.setStatus("current")
_ApSipSAStatsTotalSessionsOutbound_Type = Counter32
_ApSipSAStatsTotalSessionsOutbound_Object = MibTableColumn
apSipSAStatsTotalSessionsOutbound = _ApSipSAStatsTotalSessionsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 12),
    _ApSipSAStatsTotalSessionsOutbound_Type()
)
apSipSAStatsTotalSessionsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsTotalSessionsOutbound.setStatus("current")
_ApSipSAStatsTotalSessionsNotAdmittedOutbound_Type = Counter32
_ApSipSAStatsTotalSessionsNotAdmittedOutbound_Object = MibTableColumn
apSipSAStatsTotalSessionsNotAdmittedOutbound = _ApSipSAStatsTotalSessionsNotAdmittedOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 13),
    _ApSipSAStatsTotalSessionsNotAdmittedOutbound_Type()
)
apSipSAStatsTotalSessionsNotAdmittedOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsTotalSessionsNotAdmittedOutbound.setStatus("current")
_ApSipSAStatsPeriodHighOutbound_Type = Unsigned32
_ApSipSAStatsPeriodHighOutbound_Object = MibTableColumn
apSipSAStatsPeriodHighOutbound = _ApSipSAStatsPeriodHighOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 14),
    _ApSipSAStatsPeriodHighOutbound_Type()
)
apSipSAStatsPeriodHighOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsPeriodHighOutbound.setStatus("current")
_ApSipSAStatsAverageRateOutbound_Type = Unsigned32
_ApSipSAStatsAverageRateOutbound_Object = MibTableColumn
apSipSAStatsAverageRateOutbound = _ApSipSAStatsAverageRateOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 15),
    _ApSipSAStatsAverageRateOutbound_Type()
)
apSipSAStatsAverageRateOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsAverageRateOutbound.setStatus("current")
_ApSipSAStatsMaxBurstRate_Type = Unsigned32
_ApSipSAStatsMaxBurstRate_Object = MibTableColumn
apSipSAStatsMaxBurstRate = _ApSipSAStatsMaxBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 16),
    _ApSipSAStatsMaxBurstRate_Type()
)
apSipSAStatsMaxBurstRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsMaxBurstRate.setStatus("current")
_ApSipSAStatsPeriodSeizures_Type = Counter32
_ApSipSAStatsPeriodSeizures_Object = MibTableColumn
apSipSAStatsPeriodSeizures = _ApSipSAStatsPeriodSeizures_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 17),
    _ApSipSAStatsPeriodSeizures_Type()
)
apSipSAStatsPeriodSeizures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsPeriodSeizures.setStatus("current")
_ApSipSAStatsPeriodAnswers_Type = Counter32
_ApSipSAStatsPeriodAnswers_Object = MibTableColumn
apSipSAStatsPeriodAnswers = _ApSipSAStatsPeriodAnswers_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 18),
    _ApSipSAStatsPeriodAnswers_Type()
)
apSipSAStatsPeriodAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsPeriodAnswers.setStatus("current")
_ApSipSAStatsPeriodASR_Type = Unsigned32
_ApSipSAStatsPeriodASR_Object = MibTableColumn
apSipSAStatsPeriodASR = _ApSipSAStatsPeriodASR_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 19),
    _ApSipSAStatsPeriodASR_Type()
)
apSipSAStatsPeriodASR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsPeriodASR.setStatus("current")
_ApSipSAStatsAverageLatency_Type = Unsigned32
_ApSipSAStatsAverageLatency_Object = MibTableColumn
apSipSAStatsAverageLatency = _ApSipSAStatsAverageLatency_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 20),
    _ApSipSAStatsAverageLatency_Type()
)
apSipSAStatsAverageLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsAverageLatency.setStatus("current")
_ApSipSAStatsMaxLatency_Type = Unsigned32
_ApSipSAStatsMaxLatency_Object = MibTableColumn
apSipSAStatsMaxLatency = _ApSipSAStatsMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 21),
    _ApSipSAStatsMaxLatency_Type()
)
apSipSAStatsMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsMaxLatency.setStatus("current")
_ApSipSAStatsSessionAgentStatus_Type = ApSessionAgentStatusOptions
_ApSipSAStatsSessionAgentStatus_Object = MibTableColumn
apSipSAStatsSessionAgentStatus = _ApSipSAStatsSessionAgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 2, 1, 22),
    _ApSipSAStatsSessionAgentStatus_Type()
)
apSipSAStatsSessionAgentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSipSAStatsSessionAgentStatus.setStatus("current")
_ApH323SessionAgentStatsTable_Object = MibTable
apH323SessionAgentStatsTable = _ApH323SessionAgentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    apH323SessionAgentStatsTable.setStatus("current")
_ApH323SessionAgentStatsEntry_Object = MibTableRow
apH323SessionAgentStatsEntry = _ApH323SessionAgentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1)
)
apH323SessionAgentStatsEntry.setIndexNames(
    (0, "APSYSMGMT-MIB", "apH323SAStatsSessionAgentIndex"),
)
if mibBuilder.loadTexts:
    apH323SessionAgentStatsEntry.setStatus("current")


class _ApH323SAStatsSessionAgentIndex_Type(Integer32):
    """Custom type apH323SAStatsSessionAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApH323SAStatsSessionAgentIndex_Type.__name__ = "Integer32"
_ApH323SAStatsSessionAgentIndex_Object = MibTableColumn
apH323SAStatsSessionAgentIndex = _ApH323SAStatsSessionAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 1),
    _ApH323SAStatsSessionAgentIndex_Type()
)
apH323SAStatsSessionAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsSessionAgentIndex.setStatus("current")


class _ApH323SAStatsSessionAgentHostname_Type(DisplayString):
    """Custom type apH323SAStatsSessionAgentHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApH323SAStatsSessionAgentHostname_Type.__name__ = "DisplayString"
_ApH323SAStatsSessionAgentHostname_Object = MibTableColumn
apH323SAStatsSessionAgentHostname = _ApH323SAStatsSessionAgentHostname_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 2),
    _ApH323SAStatsSessionAgentHostname_Type()
)
apH323SAStatsSessionAgentHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsSessionAgentHostname.setStatus("current")
_ApH323SAStatsSessionAgentType_Type = ApSessionAgentType
_ApH323SAStatsSessionAgentType_Object = MibTableColumn
apH323SAStatsSessionAgentType = _ApH323SAStatsSessionAgentType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 3),
    _ApH323SAStatsSessionAgentType_Type()
)
apH323SAStatsSessionAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsSessionAgentType.setStatus("current")
_ApH323SAStatsCurrentActiveSessionsInbound_Type = Unsigned32
_ApH323SAStatsCurrentActiveSessionsInbound_Object = MibTableColumn
apH323SAStatsCurrentActiveSessionsInbound = _ApH323SAStatsCurrentActiveSessionsInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 4),
    _ApH323SAStatsCurrentActiveSessionsInbound_Type()
)
apH323SAStatsCurrentActiveSessionsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsCurrentActiveSessionsInbound.setStatus("current")
_ApH323SAStatsCurrentSessionRateInbound_Type = Unsigned32
_ApH323SAStatsCurrentSessionRateInbound_Object = MibTableColumn
apH323SAStatsCurrentSessionRateInbound = _ApH323SAStatsCurrentSessionRateInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 5),
    _ApH323SAStatsCurrentSessionRateInbound_Type()
)
apH323SAStatsCurrentSessionRateInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsCurrentSessionRateInbound.setStatus("current")
_ApH323SAStatsCurrentActiveSessionsOutbound_Type = Unsigned32
_ApH323SAStatsCurrentActiveSessionsOutbound_Object = MibTableColumn
apH323SAStatsCurrentActiveSessionsOutbound = _ApH323SAStatsCurrentActiveSessionsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 6),
    _ApH323SAStatsCurrentActiveSessionsOutbound_Type()
)
apH323SAStatsCurrentActiveSessionsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsCurrentActiveSessionsOutbound.setStatus("current")
_ApH323SAStatsCurrentSessionRateOutbound_Type = Unsigned32
_ApH323SAStatsCurrentSessionRateOutbound_Object = MibTableColumn
apH323SAStatsCurrentSessionRateOutbound = _ApH323SAStatsCurrentSessionRateOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 7),
    _ApH323SAStatsCurrentSessionRateOutbound_Type()
)
apH323SAStatsCurrentSessionRateOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsCurrentSessionRateOutbound.setStatus("current")
_ApH323SAStatsTotalSessionsInbound_Type = Counter32
_ApH323SAStatsTotalSessionsInbound_Object = MibTableColumn
apH323SAStatsTotalSessionsInbound = _ApH323SAStatsTotalSessionsInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 8),
    _ApH323SAStatsTotalSessionsInbound_Type()
)
apH323SAStatsTotalSessionsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsTotalSessionsInbound.setStatus("current")
_ApH323SAStatsTotalSessionsNotAdmittedInbound_Type = Counter32
_ApH323SAStatsTotalSessionsNotAdmittedInbound_Object = MibTableColumn
apH323SAStatsTotalSessionsNotAdmittedInbound = _ApH323SAStatsTotalSessionsNotAdmittedInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 9),
    _ApH323SAStatsTotalSessionsNotAdmittedInbound_Type()
)
apH323SAStatsTotalSessionsNotAdmittedInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsTotalSessionsNotAdmittedInbound.setStatus("current")
_ApH323SAStatsPeriodHighInbound_Type = Unsigned32
_ApH323SAStatsPeriodHighInbound_Object = MibTableColumn
apH323SAStatsPeriodHighInbound = _ApH323SAStatsPeriodHighInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 10),
    _ApH323SAStatsPeriodHighInbound_Type()
)
apH323SAStatsPeriodHighInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsPeriodHighInbound.setStatus("current")
_ApH323SAStatsAverageRateInbound_Type = Unsigned32
_ApH323SAStatsAverageRateInbound_Object = MibTableColumn
apH323SAStatsAverageRateInbound = _ApH323SAStatsAverageRateInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 11),
    _ApH323SAStatsAverageRateInbound_Type()
)
apH323SAStatsAverageRateInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsAverageRateInbound.setStatus("current")
_ApH323SAStatsTotalSessionsOutbound_Type = Counter32
_ApH323SAStatsTotalSessionsOutbound_Object = MibTableColumn
apH323SAStatsTotalSessionsOutbound = _ApH323SAStatsTotalSessionsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 12),
    _ApH323SAStatsTotalSessionsOutbound_Type()
)
apH323SAStatsTotalSessionsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsTotalSessionsOutbound.setStatus("current")
_ApH323SAStatsTotalSessionsNotAdmittedOutbound_Type = Counter32
_ApH323SAStatsTotalSessionsNotAdmittedOutbound_Object = MibTableColumn
apH323SAStatsTotalSessionsNotAdmittedOutbound = _ApH323SAStatsTotalSessionsNotAdmittedOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 13),
    _ApH323SAStatsTotalSessionsNotAdmittedOutbound_Type()
)
apH323SAStatsTotalSessionsNotAdmittedOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsTotalSessionsNotAdmittedOutbound.setStatus("current")
_ApH323SAStatsPeriodHighOutbound_Type = Unsigned32
_ApH323SAStatsPeriodHighOutbound_Object = MibTableColumn
apH323SAStatsPeriodHighOutbound = _ApH323SAStatsPeriodHighOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 14),
    _ApH323SAStatsPeriodHighOutbound_Type()
)
apH323SAStatsPeriodHighOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsPeriodHighOutbound.setStatus("current")
_ApH323SAStatsAverageRateOutbound_Type = Unsigned32
_ApH323SAStatsAverageRateOutbound_Object = MibTableColumn
apH323SAStatsAverageRateOutbound = _ApH323SAStatsAverageRateOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 15),
    _ApH323SAStatsAverageRateOutbound_Type()
)
apH323SAStatsAverageRateOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsAverageRateOutbound.setStatus("current")
_ApH323SAStatsMaxBurstRate_Type = Unsigned32
_ApH323SAStatsMaxBurstRate_Object = MibTableColumn
apH323SAStatsMaxBurstRate = _ApH323SAStatsMaxBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 16),
    _ApH323SAStatsMaxBurstRate_Type()
)
apH323SAStatsMaxBurstRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsMaxBurstRate.setStatus("current")
_ApH323SAStatsPeriodSeizures_Type = Counter32
_ApH323SAStatsPeriodSeizures_Object = MibTableColumn
apH323SAStatsPeriodSeizures = _ApH323SAStatsPeriodSeizures_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 17),
    _ApH323SAStatsPeriodSeizures_Type()
)
apH323SAStatsPeriodSeizures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsPeriodSeizures.setStatus("current")
_ApH323SAStatsPeriodAnswers_Type = Counter32
_ApH323SAStatsPeriodAnswers_Object = MibTableColumn
apH323SAStatsPeriodAnswers = _ApH323SAStatsPeriodAnswers_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 18),
    _ApH323SAStatsPeriodAnswers_Type()
)
apH323SAStatsPeriodAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsPeriodAnswers.setStatus("current")
_ApH323SAStatsPeriodASR_Type = Unsigned32
_ApH323SAStatsPeriodASR_Object = MibTableColumn
apH323SAStatsPeriodASR = _ApH323SAStatsPeriodASR_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 19),
    _ApH323SAStatsPeriodASR_Type()
)
apH323SAStatsPeriodASR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsPeriodASR.setStatus("current")
_ApH323SAStatsAverageLatency_Type = Unsigned32
_ApH323SAStatsAverageLatency_Object = MibTableColumn
apH323SAStatsAverageLatency = _ApH323SAStatsAverageLatency_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 20),
    _ApH323SAStatsAverageLatency_Type()
)
apH323SAStatsAverageLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsAverageLatency.setStatus("current")
_ApH323SAStatsMaxLatency_Type = Unsigned32
_ApH323SAStatsMaxLatency_Object = MibTableColumn
apH323SAStatsMaxLatency = _ApH323SAStatsMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 21),
    _ApH323SAStatsMaxLatency_Type()
)
apH323SAStatsMaxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsMaxLatency.setStatus("current")
_ApH323SAStatsSessionAgentStatus_Type = ApSessionAgentStatusOptions
_ApH323SAStatsSessionAgentStatus_Object = MibTableColumn
apH323SAStatsSessionAgentStatus = _ApH323SAStatsSessionAgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 3, 1, 22),
    _ApH323SAStatsSessionAgentStatus_Type()
)
apH323SAStatsSessionAgentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apH323SAStatsSessionAgentStatus.setStatus("current")
_ApSigRealmStatsTable_Object = MibTable
apSigRealmStatsTable = _ApSigRealmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    apSigRealmStatsTable.setStatus("current")
_ApSigRealmStatsEntry_Object = MibTableRow
apSigRealmStatsEntry = _ApSigRealmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1)
)
apSigRealmStatsEntry.setIndexNames(
    (0, "APSYSMGMT-MIB", "apSigRealmStatsRealmIndex"),
)
if mibBuilder.loadTexts:
    apSigRealmStatsEntry.setStatus("current")


class _ApSigRealmStatsRealmIndex_Type(Integer32):
    """Custom type apSigRealmStatsRealmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApSigRealmStatsRealmIndex_Type.__name__ = "Integer32"
_ApSigRealmStatsRealmIndex_Object = MibTableColumn
apSigRealmStatsRealmIndex = _ApSigRealmStatsRealmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 1),
    _ApSigRealmStatsRealmIndex_Type()
)
apSigRealmStatsRealmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsRealmIndex.setStatus("current")


class _ApSigRealmStatsRealmName_Type(DisplayString):
    """Custom type apSigRealmStatsRealmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSigRealmStatsRealmName_Type.__name__ = "DisplayString"
_ApSigRealmStatsRealmName_Object = MibTableColumn
apSigRealmStatsRealmName = _ApSigRealmStatsRealmName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 2),
    _ApSigRealmStatsRealmName_Type()
)
apSigRealmStatsRealmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsRealmName.setStatus("current")
_ApSigRealmStatsCurrentActiveSessionsInbound_Type = Unsigned32
_ApSigRealmStatsCurrentActiveSessionsInbound_Object = MibTableColumn
apSigRealmStatsCurrentActiveSessionsInbound = _ApSigRealmStatsCurrentActiveSessionsInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 3),
    _ApSigRealmStatsCurrentActiveSessionsInbound_Type()
)
apSigRealmStatsCurrentActiveSessionsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsCurrentActiveSessionsInbound.setStatus("current")
_ApSigRealmStatsCurrentSessionRateInbound_Type = Unsigned32
_ApSigRealmStatsCurrentSessionRateInbound_Object = MibTableColumn
apSigRealmStatsCurrentSessionRateInbound = _ApSigRealmStatsCurrentSessionRateInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 4),
    _ApSigRealmStatsCurrentSessionRateInbound_Type()
)
apSigRealmStatsCurrentSessionRateInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsCurrentSessionRateInbound.setStatus("current")
_ApSigRealmStatsCurrentActiveSessionsOutbound_Type = Unsigned32
_ApSigRealmStatsCurrentActiveSessionsOutbound_Object = MibTableColumn
apSigRealmStatsCurrentActiveSessionsOutbound = _ApSigRealmStatsCurrentActiveSessionsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 5),
    _ApSigRealmStatsCurrentActiveSessionsOutbound_Type()
)
apSigRealmStatsCurrentActiveSessionsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsCurrentActiveSessionsOutbound.setStatus("current")
_ApSigRealmStatsCurrentSessionRateOutbound_Type = Unsigned32
_ApSigRealmStatsCurrentSessionRateOutbound_Object = MibTableColumn
apSigRealmStatsCurrentSessionRateOutbound = _ApSigRealmStatsCurrentSessionRateOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 6),
    _ApSigRealmStatsCurrentSessionRateOutbound_Type()
)
apSigRealmStatsCurrentSessionRateOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsCurrentSessionRateOutbound.setStatus("current")
_ApSigRealmStatsTotalSessionsInbound_Type = Counter32
_ApSigRealmStatsTotalSessionsInbound_Object = MibTableColumn
apSigRealmStatsTotalSessionsInbound = _ApSigRealmStatsTotalSessionsInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 7),
    _ApSigRealmStatsTotalSessionsInbound_Type()
)
apSigRealmStatsTotalSessionsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsTotalSessionsInbound.setStatus("current")
_ApSigRealmStatsTotalSessionsNotAdmittedInbound_Type = Counter32
_ApSigRealmStatsTotalSessionsNotAdmittedInbound_Object = MibTableColumn
apSigRealmStatsTotalSessionsNotAdmittedInbound = _ApSigRealmStatsTotalSessionsNotAdmittedInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 8),
    _ApSigRealmStatsTotalSessionsNotAdmittedInbound_Type()
)
apSigRealmStatsTotalSessionsNotAdmittedInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsTotalSessionsNotAdmittedInbound.setStatus("current")
_ApSigRealmStatsPeriodHighInbound_Type = Unsigned32
_ApSigRealmStatsPeriodHighInbound_Object = MibTableColumn
apSigRealmStatsPeriodHighInbound = _ApSigRealmStatsPeriodHighInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 9),
    _ApSigRealmStatsPeriodHighInbound_Type()
)
apSigRealmStatsPeriodHighInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsPeriodHighInbound.setStatus("current")
_ApSigRealmStatsAverageRateInbound_Type = Unsigned32
_ApSigRealmStatsAverageRateInbound_Object = MibTableColumn
apSigRealmStatsAverageRateInbound = _ApSigRealmStatsAverageRateInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 10),
    _ApSigRealmStatsAverageRateInbound_Type()
)
apSigRealmStatsAverageRateInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsAverageRateInbound.setStatus("current")
_ApSigRealmStatsTotalSessionsOutbound_Type = Counter32
_ApSigRealmStatsTotalSessionsOutbound_Object = MibTableColumn
apSigRealmStatsTotalSessionsOutbound = _ApSigRealmStatsTotalSessionsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 11),
    _ApSigRealmStatsTotalSessionsOutbound_Type()
)
apSigRealmStatsTotalSessionsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsTotalSessionsOutbound.setStatus("current")
_ApSigRealmStatsTotalSessionsNotAdmittedOutbound_Type = Counter32
_ApSigRealmStatsTotalSessionsNotAdmittedOutbound_Object = MibTableColumn
apSigRealmStatsTotalSessionsNotAdmittedOutbound = _ApSigRealmStatsTotalSessionsNotAdmittedOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 12),
    _ApSigRealmStatsTotalSessionsNotAdmittedOutbound_Type()
)
apSigRealmStatsTotalSessionsNotAdmittedOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsTotalSessionsNotAdmittedOutbound.setStatus("current")
_ApSigRealmStatsPeriodHighOutbound_Type = Unsigned32
_ApSigRealmStatsPeriodHighOutbound_Object = MibTableColumn
apSigRealmStatsPeriodHighOutbound = _ApSigRealmStatsPeriodHighOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 13),
    _ApSigRealmStatsPeriodHighOutbound_Type()
)
apSigRealmStatsPeriodHighOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsPeriodHighOutbound.setStatus("current")
_ApSigRealmStatsAverageRateOutbound_Type = Unsigned32
_ApSigRealmStatsAverageRateOutbound_Object = MibTableColumn
apSigRealmStatsAverageRateOutbound = _ApSigRealmStatsAverageRateOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 14),
    _ApSigRealmStatsAverageRateOutbound_Type()
)
apSigRealmStatsAverageRateOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsAverageRateOutbound.setStatus("current")
_ApSigRealmStatsMaxBurstRate_Type = Unsigned32
_ApSigRealmStatsMaxBurstRate_Object = MibTableColumn
apSigRealmStatsMaxBurstRate = _ApSigRealmStatsMaxBurstRate_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 15),
    _ApSigRealmStatsMaxBurstRate_Type()
)
apSigRealmStatsMaxBurstRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsMaxBurstRate.setStatus("current")
_ApSigRealmStatsPeriodSeizures_Type = Counter32
_ApSigRealmStatsPeriodSeizures_Object = MibTableColumn
apSigRealmStatsPeriodSeizures = _ApSigRealmStatsPeriodSeizures_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 16),
    _ApSigRealmStatsPeriodSeizures_Type()
)
apSigRealmStatsPeriodSeizures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsPeriodSeizures.setStatus("current")
_ApSigRealmStatsPeriodAnswers_Type = Counter32
_ApSigRealmStatsPeriodAnswers_Object = MibTableColumn
apSigRealmStatsPeriodAnswers = _ApSigRealmStatsPeriodAnswers_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 17),
    _ApSigRealmStatsPeriodAnswers_Type()
)
apSigRealmStatsPeriodAnswers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsPeriodAnswers.setStatus("current")
_ApSigRealmStatsPeriodASR_Type = Unsigned32
_ApSigRealmStatsPeriodASR_Object = MibTableColumn
apSigRealmStatsPeriodASR = _ApSigRealmStatsPeriodASR_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 18),
    _ApSigRealmStatsPeriodASR_Type()
)
apSigRealmStatsPeriodASR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsPeriodASR.setStatus("current")
_ApSigRealmStatsAverageLatency_Type = Unsigned32
_ApSigRealmStatsAverageLatency_Object = MibTableColumn
apSigRealmStatsAverageLatency = _ApSigRealmStatsAverageLatency_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 19),
    _ApSigRealmStatsAverageLatency_Type()
)
apSigRealmStatsAverageLatency.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSigRealmStatsAverageLatency.setStatus("obsolete")
_ApSigRealmStatsMaxLatency_Type = Unsigned32
_ApSigRealmStatsMaxLatency_Object = MibTableColumn
apSigRealmStatsMaxLatency = _ApSigRealmStatsMaxLatency_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 20),
    _ApSigRealmStatsMaxLatency_Type()
)
apSigRealmStatsMaxLatency.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSigRealmStatsMaxLatency.setStatus("obsolete")
_ApSigRealmStatsMinutesLeft_Type = Unsigned32
_ApSigRealmStatsMinutesLeft_Object = MibTableColumn
apSigRealmStatsMinutesLeft = _ApSigRealmStatsMinutesLeft_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 21),
    _ApSigRealmStatsMinutesLeft_Type()
)
apSigRealmStatsMinutesLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsMinutesLeft.setStatus("current")
_ApSigRealmStatsMinutesReject_Type = Unsigned32
_ApSigRealmStatsMinutesReject_Object = MibTableColumn
apSigRealmStatsMinutesReject = _ApSigRealmStatsMinutesReject_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 22),
    _ApSigRealmStatsMinutesReject_Type()
)
apSigRealmStatsMinutesReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsMinutesReject.setStatus("current")
_ApSigRealmStatsShortSessions_Type = Counter32
_ApSigRealmStatsShortSessions_Object = MibTableColumn
apSigRealmStatsShortSessions = _ApSigRealmStatsShortSessions_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 23),
    _ApSigRealmStatsShortSessions_Type()
)
apSigRealmStatsShortSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsShortSessions.setStatus("current")
_ApSigRealmStatsAverageQoSRFactor_Type = Unsigned32
_ApSigRealmStatsAverageQoSRFactor_Object = MibTableColumn
apSigRealmStatsAverageQoSRFactor = _ApSigRealmStatsAverageQoSRFactor_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 24),
    _ApSigRealmStatsAverageQoSRFactor_Type()
)
apSigRealmStatsAverageQoSRFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsAverageQoSRFactor.setStatus("current")
_ApSigRealmStatsMaximumQoSRFactor_Type = Unsigned32
_ApSigRealmStatsMaximumQoSRFactor_Object = MibTableColumn
apSigRealmStatsMaximumQoSRFactor = _ApSigRealmStatsMaximumQoSRFactor_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 25),
    _ApSigRealmStatsMaximumQoSRFactor_Type()
)
apSigRealmStatsMaximumQoSRFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsMaximumQoSRFactor.setStatus("current")
_ApSigRealmStatsCurrentMajorRFactorExceeded_Type = Unsigned32
_ApSigRealmStatsCurrentMajorRFactorExceeded_Object = MibTableColumn
apSigRealmStatsCurrentMajorRFactorExceeded = _ApSigRealmStatsCurrentMajorRFactorExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 26),
    _ApSigRealmStatsCurrentMajorRFactorExceeded_Type()
)
apSigRealmStatsCurrentMajorRFactorExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsCurrentMajorRFactorExceeded.setStatus("current")
_ApSigRealmStatsTotalMajorRFactorExceeded_Type = Counter32
_ApSigRealmStatsTotalMajorRFactorExceeded_Object = MibTableColumn
apSigRealmStatsTotalMajorRFactorExceeded = _ApSigRealmStatsTotalMajorRFactorExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 27),
    _ApSigRealmStatsTotalMajorRFactorExceeded_Type()
)
apSigRealmStatsTotalMajorRFactorExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsTotalMajorRFactorExceeded.setStatus("current")
_ApSigRealmStatsCurrentCriticalRFactorExceeded_Type = Unsigned32
_ApSigRealmStatsCurrentCriticalRFactorExceeded_Object = MibTableColumn
apSigRealmStatsCurrentCriticalRFactorExceeded = _ApSigRealmStatsCurrentCriticalRFactorExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 28),
    _ApSigRealmStatsCurrentCriticalRFactorExceeded_Type()
)
apSigRealmStatsCurrentCriticalRFactorExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsCurrentCriticalRFactorExceeded.setStatus("current")
_ApSigRealmStatsTotalCriticalRFactorExceeded_Type = Counter32
_ApSigRealmStatsTotalCriticalRFactorExceeded_Object = MibTableColumn
apSigRealmStatsTotalCriticalRFactorExceeded = _ApSigRealmStatsTotalCriticalRFactorExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 29),
    _ApSigRealmStatsTotalCriticalRFactorExceeded_Type()
)
apSigRealmStatsTotalCriticalRFactorExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsTotalCriticalRFactorExceeded.setStatus("current")
_ApSigRealmStatsRealmStatus_Type = ApSigRealmStatusOptions
_ApSigRealmStatsRealmStatus_Object = MibTableColumn
apSigRealmStatsRealmStatus = _ApSigRealmStatsRealmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 30),
    _ApSigRealmStatsRealmStatus_Type()
)
apSigRealmStatsRealmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsRealmStatus.setStatus("current")
_ApSigRealmStatsActiveLocalContacts_Type = Unsigned32
_ApSigRealmStatsActiveLocalContacts_Object = MibTableColumn
apSigRealmStatsActiveLocalContacts = _ApSigRealmStatsActiveLocalContacts_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 31),
    _ApSigRealmStatsActiveLocalContacts_Type()
)
apSigRealmStatsActiveLocalContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsActiveLocalContacts.setStatus("current")
_ApSigRealmStatsActiveSubscriptions_Type = Unsigned32
_ApSigRealmStatsActiveSubscriptions_Object = MibTableColumn
apSigRealmStatsActiveSubscriptions = _ApSigRealmStatsActiveSubscriptions_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 32),
    _ApSigRealmStatsActiveSubscriptions_Type()
)
apSigRealmStatsActiveSubscriptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsActiveSubscriptions.setStatus("current")
_ApSigRealmStatsPerMaxSubscriptions_Type = Counter32
_ApSigRealmStatsPerMaxSubscriptions_Object = MibTableColumn
apSigRealmStatsPerMaxSubscriptions = _ApSigRealmStatsPerMaxSubscriptions_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 33),
    _ApSigRealmStatsPerMaxSubscriptions_Type()
)
apSigRealmStatsPerMaxSubscriptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsPerMaxSubscriptions.setStatus("current")
_ApSigRealmStatsMaximumActiveSubscriptions_Type = Counter32
_ApSigRealmStatsMaximumActiveSubscriptions_Object = MibTableColumn
apSigRealmStatsMaximumActiveSubscriptions = _ApSigRealmStatsMaximumActiveSubscriptions_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 34),
    _ApSigRealmStatsMaximumActiveSubscriptions_Type()
)
apSigRealmStatsMaximumActiveSubscriptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsMaximumActiveSubscriptions.setStatus("current")
_ApSigRealmStatsTotalSubscriptions_Type = Counter32
_ApSigRealmStatsTotalSubscriptions_Object = MibTableColumn
apSigRealmStatsTotalSubscriptions = _ApSigRealmStatsTotalSubscriptions_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 2, 4, 1, 35),
    _ApSigRealmStatsTotalSubscriptions_Type()
)
apSigRealmStatsTotalSubscriptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSigRealmStatsTotalSubscriptions.setStatus("current")
_ApSysMgmtMIBNetMgmtCtrlObjects_ObjectIdentity = ObjectIdentity
apSysMgmtMIBNetMgmtCtrlObjects = _ApSysMgmtMIBNetMgmtCtrlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 3)
)
_ApNetMgmtCtrlStatsTable_Object = MibTable
apNetMgmtCtrlStatsTable = _ApNetMgmtCtrlStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    apNetMgmtCtrlStatsTable.setStatus("current")
_ApNetMgmtCtrlStatsEntry_Object = MibTableRow
apNetMgmtCtrlStatsEntry = _ApNetMgmtCtrlStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 3, 1, 1)
)
apNetMgmtCtrlStatsEntry.setIndexNames(
    (1, "APSYSMGMT-MIB", "apNetMgmtCtrlStatsName"),
)
if mibBuilder.loadTexts:
    apNetMgmtCtrlStatsEntry.setStatus("current")


class _ApNetMgmtCtrlStatsName_Type(DisplayString):
    """Custom type apNetMgmtCtrlStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApNetMgmtCtrlStatsName_Type.__name__ = "DisplayString"
_ApNetMgmtCtrlStatsName_Object = MibTableColumn
apNetMgmtCtrlStatsName = _ApNetMgmtCtrlStatsName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 3, 1, 1, 1),
    _ApNetMgmtCtrlStatsName_Type()
)
apNetMgmtCtrlStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNetMgmtCtrlStatsName.setStatus("current")
_ApNetMgmtCtrlStatsType_Type = ApNetMgmtCtrlType
_ApNetMgmtCtrlStatsType_Object = MibTableColumn
apNetMgmtCtrlStatsType = _ApNetMgmtCtrlStatsType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 3, 1, 1, 2),
    _ApNetMgmtCtrlStatsType_Type()
)
apNetMgmtCtrlStatsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNetMgmtCtrlStatsType.setStatus("current")
_ApNetMgmtCtrlStatsIncomingTotal_Type = Unsigned32
_ApNetMgmtCtrlStatsIncomingTotal_Object = MibTableColumn
apNetMgmtCtrlStatsIncomingTotal = _ApNetMgmtCtrlStatsIncomingTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 3, 1, 1, 3),
    _ApNetMgmtCtrlStatsIncomingTotal_Type()
)
apNetMgmtCtrlStatsIncomingTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNetMgmtCtrlStatsIncomingTotal.setStatus("current")
_ApNetMgmtCtrlStatsRejectedTotal_Type = Unsigned32
_ApNetMgmtCtrlStatsRejectedTotal_Object = MibTableColumn
apNetMgmtCtrlStatsRejectedTotal = _ApNetMgmtCtrlStatsRejectedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 3, 1, 1, 4),
    _ApNetMgmtCtrlStatsRejectedTotal_Type()
)
apNetMgmtCtrlStatsRejectedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNetMgmtCtrlStatsRejectedTotal.setStatus("current")
_ApNetMgmtCtrlStatsDivertedTotal_Type = Unsigned32
_ApNetMgmtCtrlStatsDivertedTotal_Object = MibTableColumn
apNetMgmtCtrlStatsDivertedTotal = _ApNetMgmtCtrlStatsDivertedTotal_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 3, 1, 1, 5),
    _ApNetMgmtCtrlStatsDivertedTotal_Type()
)
apNetMgmtCtrlStatsDivertedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNetMgmtCtrlStatsDivertedTotal.setStatus("current")
_ApNetMgmtCtrlStatsIncomingCurrent_Type = Unsigned32
_ApNetMgmtCtrlStatsIncomingCurrent_Object = MibTableColumn
apNetMgmtCtrlStatsIncomingCurrent = _ApNetMgmtCtrlStatsIncomingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 3, 1, 1, 6),
    _ApNetMgmtCtrlStatsIncomingCurrent_Type()
)
apNetMgmtCtrlStatsIncomingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNetMgmtCtrlStatsIncomingCurrent.setStatus("current")
_ApNetMgmtCtrlStatsRejectedCurrent_Type = Unsigned32
_ApNetMgmtCtrlStatsRejectedCurrent_Object = MibTableColumn
apNetMgmtCtrlStatsRejectedCurrent = _ApNetMgmtCtrlStatsRejectedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 3, 1, 1, 7),
    _ApNetMgmtCtrlStatsRejectedCurrent_Type()
)
apNetMgmtCtrlStatsRejectedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNetMgmtCtrlStatsRejectedCurrent.setStatus("current")
_ApNetMgmtCtrlStatsDivertedCurrent_Type = Unsigned32
_ApNetMgmtCtrlStatsDivertedCurrent_Object = MibTableColumn
apNetMgmtCtrlStatsDivertedCurrent = _ApNetMgmtCtrlStatsDivertedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 3, 1, 1, 8),
    _ApNetMgmtCtrlStatsDivertedCurrent_Type()
)
apNetMgmtCtrlStatsDivertedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNetMgmtCtrlStatsDivertedCurrent.setStatus("current")
_ApNetMgmtCtrlStatsIncomingPeriodMax_Type = Unsigned32
_ApNetMgmtCtrlStatsIncomingPeriodMax_Object = MibTableColumn
apNetMgmtCtrlStatsIncomingPeriodMax = _ApNetMgmtCtrlStatsIncomingPeriodMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 3, 1, 1, 9),
    _ApNetMgmtCtrlStatsIncomingPeriodMax_Type()
)
apNetMgmtCtrlStatsIncomingPeriodMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNetMgmtCtrlStatsIncomingPeriodMax.setStatus("current")
_ApNetMgmtCtrlStatsRejectedPeriodMax_Type = Unsigned32
_ApNetMgmtCtrlStatsRejectedPeriodMax_Object = MibTableColumn
apNetMgmtCtrlStatsRejectedPeriodMax = _ApNetMgmtCtrlStatsRejectedPeriodMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 3, 1, 1, 10),
    _ApNetMgmtCtrlStatsRejectedPeriodMax_Type()
)
apNetMgmtCtrlStatsRejectedPeriodMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNetMgmtCtrlStatsRejectedPeriodMax.setStatus("current")
_ApNetMgmtCtrlStatsDivertedPeriodMax_Type = Unsigned32
_ApNetMgmtCtrlStatsDivertedPeriodMax_Object = MibTableColumn
apNetMgmtCtrlStatsDivertedPeriodMax = _ApNetMgmtCtrlStatsDivertedPeriodMax_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 3, 1, 1, 11),
    _ApNetMgmtCtrlStatsDivertedPeriodMax_Type()
)
apNetMgmtCtrlStatsDivertedPeriodMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNetMgmtCtrlStatsDivertedPeriodMax.setStatus("current")
_ApNetMgmtCtrlStatsState_Type = ApNetMgmtCtrlState
_ApNetMgmtCtrlStatsState_Object = MibTableColumn
apNetMgmtCtrlStatsState = _ApNetMgmtCtrlStatsState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 3, 1, 1, 12),
    _ApNetMgmtCtrlStatsState_Type()
)
apNetMgmtCtrlStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNetMgmtCtrlStatsState.setStatus("current")
_ApSysMgmtMIBENUMServerStatusObjects_ObjectIdentity = ObjectIdentity
apSysMgmtMIBENUMServerStatusObjects = _ApSysMgmtMIBENUMServerStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 4)
)
_ApENUMServerStatusTable_Object = MibTable
apENUMServerStatusTable = _ApENUMServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    apENUMServerStatusTable.setStatus("obsolete")
_ApENUMServerStatusEntry_Object = MibTableRow
apENUMServerStatusEntry = _ApENUMServerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 4, 1, 1)
)
apENUMServerStatusEntry.setIndexNames(
    (0, "APSYSMGMT-MIB", "apENUMConfigName"),
    (0, "APSYSMGMT-MIB", "apENUMServerIpAddress"),
)
if mibBuilder.loadTexts:
    apENUMServerStatusEntry.setStatus("obsolete")
_ApENUMConfigName_Type = DisplayString
_ApENUMConfigName_Object = MibTableColumn
apENUMConfigName = _ApENUMConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 4, 1, 1, 1),
    _ApENUMConfigName_Type()
)
apENUMConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apENUMConfigName.setStatus("obsolete")
_ApENUMServerIpAddress_Type = IpAddress
_ApENUMServerIpAddress_Object = MibTableColumn
apENUMServerIpAddress = _ApENUMServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 4, 1, 1, 2),
    _ApENUMServerIpAddress_Type()
)
apENUMServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apENUMServerIpAddress.setStatus("obsolete")


class _ApENUMServerStatus_Type(Integer32):
    """Custom type apENUMServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inservice", 0),
          ("lowerpriority", 1),
          ("oosunreachable", 2))
    )


_ApENUMServerStatus_Type.__name__ = "Integer32"
_ApENUMServerStatus_Object = MibTableColumn
apENUMServerStatus = _ApENUMServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 4, 1, 1, 3),
    _ApENUMServerStatus_Type()
)
apENUMServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apENUMServerStatus.setStatus("obsolete")
_ApSysMgmtMIBNSEPStatsObjects_ObjectIdentity = ObjectIdentity
apSysMgmtMIBNSEPStatsObjects = _ApSysMgmtMIBNSEPStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 5)
)
_ApNSEPStatsCurrentActiveSessionsInbound_Type = Unsigned32
_ApNSEPStatsCurrentActiveSessionsInbound_Object = MibScalar
apNSEPStatsCurrentActiveSessionsInbound = _ApNSEPStatsCurrentActiveSessionsInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 5, 1),
    _ApNSEPStatsCurrentActiveSessionsInbound_Type()
)
apNSEPStatsCurrentActiveSessionsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNSEPStatsCurrentActiveSessionsInbound.setStatus("current")
_ApNSEPStatsTotalSessionsInbound_Type = Counter32
_ApNSEPStatsTotalSessionsInbound_Object = MibScalar
apNSEPStatsTotalSessionsInbound = _ApNSEPStatsTotalSessionsInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 5, 2),
    _ApNSEPStatsTotalSessionsInbound_Type()
)
apNSEPStatsTotalSessionsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNSEPStatsTotalSessionsInbound.setStatus("current")
_ApNSEPStatsPeriodHighInbound_Type = Unsigned32
_ApNSEPStatsPeriodHighInbound_Object = MibScalar
apNSEPStatsPeriodHighInbound = _ApNSEPStatsPeriodHighInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 5, 3),
    _ApNSEPStatsPeriodHighInbound_Type()
)
apNSEPStatsPeriodHighInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNSEPStatsPeriodHighInbound.setStatus("current")
_ApNSEPStatsPeriod_Type = Unsigned32
_ApNSEPStatsPeriod_Object = MibScalar
apNSEPStatsPeriod = _ApNSEPStatsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 5, 4),
    _ApNSEPStatsPeriod_Type()
)
apNSEPStatsPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNSEPStatsPeriod.setStatus("current")
_ApNSEPStatsRPHTable_Object = MibTable
apNSEPStatsRPHTable = _ApNSEPStatsRPHTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 5, 5)
)
if mibBuilder.loadTexts:
    apNSEPStatsRPHTable.setStatus("current")
_ApNSEPStatsRPHEntry_Object = MibTableRow
apNSEPStatsRPHEntry = _ApNSEPStatsRPHEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 5, 5, 1)
)
apNSEPStatsRPHEntry.setIndexNames(
    (1, "APSYSMGMT-MIB", "apNSEPStatsRPHValue"),
)
if mibBuilder.loadTexts:
    apNSEPStatsRPHEntry.setStatus("current")


class _ApNSEPStatsRPHValue_Type(DisplayString):
    """Custom type apNSEPStatsRPHValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApNSEPStatsRPHValue_Type.__name__ = "DisplayString"
_ApNSEPStatsRPHValue_Object = MibTableColumn
apNSEPStatsRPHValue = _ApNSEPStatsRPHValue_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 5, 5, 1, 1),
    _ApNSEPStatsRPHValue_Type()
)
apNSEPStatsRPHValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNSEPStatsRPHValue.setStatus("current")
_ApNSEPStatsRPHCurrentActiveSessionsInbound_Type = Unsigned32
_ApNSEPStatsRPHCurrentActiveSessionsInbound_Object = MibTableColumn
apNSEPStatsRPHCurrentActiveSessionsInbound = _ApNSEPStatsRPHCurrentActiveSessionsInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 5, 5, 1, 2),
    _ApNSEPStatsRPHCurrentActiveSessionsInbound_Type()
)
apNSEPStatsRPHCurrentActiveSessionsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNSEPStatsRPHCurrentActiveSessionsInbound.setStatus("current")
_ApNSEPStatsRPHTotalSessionsInbound_Type = Unsigned32
_ApNSEPStatsRPHTotalSessionsInbound_Object = MibTableColumn
apNSEPStatsRPHTotalSessionsInbound = _ApNSEPStatsRPHTotalSessionsInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 5, 5, 1, 3),
    _ApNSEPStatsRPHTotalSessionsInbound_Type()
)
apNSEPStatsRPHTotalSessionsInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNSEPStatsRPHTotalSessionsInbound.setStatus("current")
_ApNSEPStatsRPHPeriodHighInbound_Type = Unsigned32
_ApNSEPStatsRPHPeriodHighInbound_Object = MibTableColumn
apNSEPStatsRPHPeriodHighInbound = _ApNSEPStatsRPHPeriodHighInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 5, 5, 1, 4),
    _ApNSEPStatsRPHPeriodHighInbound_Type()
)
apNSEPStatsRPHPeriodHighInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNSEPStatsRPHPeriodHighInbound.setStatus("current")
_ApNSEPStatsRPHTotalSessionsNotAdmittedInbound_Type = Unsigned32
_ApNSEPStatsRPHTotalSessionsNotAdmittedInbound_Object = MibTableColumn
apNSEPStatsRPHTotalSessionsNotAdmittedInbound = _ApNSEPStatsRPHTotalSessionsNotAdmittedInbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 5, 5, 1, 5),
    _ApNSEPStatsRPHTotalSessionsNotAdmittedInbound_Type()
)
apNSEPStatsRPHTotalSessionsNotAdmittedInbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNSEPStatsRPHTotalSessionsNotAdmittedInbound.setStatus("current")
_ApNSEPStatsRPHCurrentActiveSessionsOutbound_Type = Unsigned32
_ApNSEPStatsRPHCurrentActiveSessionsOutbound_Object = MibTableColumn
apNSEPStatsRPHCurrentActiveSessionsOutbound = _ApNSEPStatsRPHCurrentActiveSessionsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 5, 5, 1, 6),
    _ApNSEPStatsRPHCurrentActiveSessionsOutbound_Type()
)
apNSEPStatsRPHCurrentActiveSessionsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNSEPStatsRPHCurrentActiveSessionsOutbound.setStatus("current")
_ApNSEPStatsRPHTotalSessionsOutbound_Type = Unsigned32
_ApNSEPStatsRPHTotalSessionsOutbound_Object = MibTableColumn
apNSEPStatsRPHTotalSessionsOutbound = _ApNSEPStatsRPHTotalSessionsOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 5, 5, 1, 7),
    _ApNSEPStatsRPHTotalSessionsOutbound_Type()
)
apNSEPStatsRPHTotalSessionsOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNSEPStatsRPHTotalSessionsOutbound.setStatus("current")
_ApNSEPStatsRPHPeriodHighOutbound_Type = Unsigned32
_ApNSEPStatsRPHPeriodHighOutbound_Object = MibTableColumn
apNSEPStatsRPHPeriodHighOutbound = _ApNSEPStatsRPHPeriodHighOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 5, 5, 1, 8),
    _ApNSEPStatsRPHPeriodHighOutbound_Type()
)
apNSEPStatsRPHPeriodHighOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNSEPStatsRPHPeriodHighOutbound.setStatus("current")
_ApNSEPStatsRPHTotalSessionsNotAdmittedOutbound_Type = Unsigned32
_ApNSEPStatsRPHTotalSessionsNotAdmittedOutbound_Object = MibTableColumn
apNSEPStatsRPHTotalSessionsNotAdmittedOutbound = _ApNSEPStatsRPHTotalSessionsNotAdmittedOutbound_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 5, 5, 1, 9),
    _ApNSEPStatsRPHTotalSessionsNotAdmittedOutbound_Type()
)
apNSEPStatsRPHTotalSessionsNotAdmittedOutbound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apNSEPStatsRPHTotalSessionsNotAdmittedOutbound.setStatus("current")
_ApSysMgmtMIBLDAPServerStatusObjects_ObjectIdentity = ObjectIdentity
apSysMgmtMIBLDAPServerStatusObjects = _ApSysMgmtMIBLDAPServerStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 6)
)
_ApLDAPServerStatusTable_Object = MibTable
apLDAPServerStatusTable = _ApLDAPServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    apLDAPServerStatusTable.setStatus("current")
_ApLDAPServerStatusEntry_Object = MibTableRow
apLDAPServerStatusEntry = _ApLDAPServerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 6, 1, 1)
)
apLDAPServerStatusEntry.setIndexNames(
    (0, "APSYSMGMT-MIB", "apLDAPConfigName"),
    (0, "APSYSMGMT-MIB", "apLDAPServerIpAddress"),
)
if mibBuilder.loadTexts:
    apLDAPServerStatusEntry.setStatus("current")
_ApLDAPConfigName_Type = DisplayString
_ApLDAPConfigName_Object = MibTableColumn
apLDAPConfigName = _ApLDAPConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 6, 1, 1, 1),
    _ApLDAPConfigName_Type()
)
apLDAPConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLDAPConfigName.setStatus("current")
_ApLDAPServerIpAddress_Type = IpAddress
_ApLDAPServerIpAddress_Object = MibTableColumn
apLDAPServerIpAddress = _ApLDAPServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 6, 1, 1, 2),
    _ApLDAPServerIpAddress_Type()
)
apLDAPServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLDAPServerIpAddress.setStatus("current")


class _ApLDAPServerStatus_Type(Integer32):
    """Custom type apLDAPServerStatus based on Integer32"""
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
        *(("inservice", 1),
          ("servertimeout", 3),
          ("sessionlost", 2),
          ("unknown", 0))
    )


_ApLDAPServerStatus_Type.__name__ = "Integer32"
_ApLDAPServerStatus_Object = MibTableColumn
apLDAPServerStatus = _ApLDAPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 6, 1, 1, 3),
    _ApLDAPServerStatus_Type()
)
apLDAPServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLDAPServerStatus.setStatus("current")
_ApSysMgmtSystemTrapObjects_ObjectIdentity = ObjectIdentity
apSysMgmtSystemTrapObjects = _ApSysMgmtSystemTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 7)
)
_ApSysMgmtTrapTable_Object = MibTable
apSysMgmtTrapTable = _ApSysMgmtTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    apSysMgmtTrapTable.setStatus("current")
_ApSysMgmtTrapTableEntry_Object = MibTableRow
apSysMgmtTrapTableEntry = _ApSysMgmtTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 7, 1, 1)
)
apSysMgmtTrapTableEntry.setIndexNames(
    (0, "APSYSMGMT-MIB", "apTrapTableSystemTime"),
    (0, "APSYSMGMT-MIB", "apTrapTableInstanceIndex"),
)
if mibBuilder.loadTexts:
    apSysMgmtTrapTableEntry.setStatus("current")
_ApTrapTableSystemTime_Type = Unsigned32
_ApTrapTableSystemTime_Object = MibTableColumn
apTrapTableSystemTime = _ApTrapTableSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 7, 1, 1, 1),
    _ApTrapTableSystemTime_Type()
)
apTrapTableSystemTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apTrapTableSystemTime.setStatus("current")
_ApTrapTableInstanceIndex_Type = Unsigned32
_ApTrapTableInstanceIndex_Object = MibTableColumn
apTrapTableInstanceIndex = _ApTrapTableInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 7, 1, 1, 2),
    _ApTrapTableInstanceIndex_Type()
)
apTrapTableInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apTrapTableInstanceIndex.setStatus("current")
_ApTrapTableNumVariables_Type = Unsigned32
_ApTrapTableNumVariables_Object = MibTableColumn
apTrapTableNumVariables = _ApTrapTableNumVariables_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 7, 1, 1, 3),
    _ApTrapTableNumVariables_Type()
)
apTrapTableNumVariables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapTableNumVariables.setStatus("current")
_ApTrapTableSysUptime_Type = TimeTicks
_ApTrapTableSysUptime_Object = MibTableColumn
apTrapTableSysUptime = _ApTrapTableSysUptime_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 7, 1, 1, 4),
    _ApTrapTableSysUptime_Type()
)
apTrapTableSysUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapTableSysUptime.setStatus("current")
_ApTrapTableTrapId_Type = ObjectIdentifier
_ApTrapTableTrapId_Object = MibTableColumn
apTrapTableTrapId = _ApTrapTableTrapId_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 7, 1, 1, 5),
    _ApTrapTableTrapId_Type()
)
apTrapTableTrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapTableTrapId.setStatus("current")
_ApSysMgmtTrapInformationTable_Object = MibTable
apSysMgmtTrapInformationTable = _ApSysMgmtTrapInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    apSysMgmtTrapInformationTable.setStatus("current")
_ApSysMgmtTrapInformationTableEntry_Object = MibTableRow
apSysMgmtTrapInformationTableEntry = _ApSysMgmtTrapInformationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 7, 2, 1)
)
apSysMgmtTrapInformationTableEntry.setIndexNames(
    (0, "APSYSMGMT-MIB", "apTrapTableSystemTime"),
    (0, "APSYSMGMT-MIB", "apTrapTableInstanceIndex"),
    (0, "APSYSMGMT-MIB", "apTrapInformationTableDataIndex"),
)
if mibBuilder.loadTexts:
    apSysMgmtTrapInformationTableEntry.setStatus("current")
_ApTrapInformationTableDataIndex_Type = Unsigned32
_ApTrapInformationTableDataIndex_Object = MibTableColumn
apTrapInformationTableDataIndex = _ApTrapInformationTableDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 7, 2, 1, 1),
    _ApTrapInformationTableDataIndex_Type()
)
apTrapInformationTableDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apTrapInformationTableDataIndex.setStatus("current")


class _ApTrapInformationTableDataType_Type(Integer32):
    """Custom type apTrapInformationTableDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              6,
              64,
              70)
        )
    )
    namedValues = NamedValues(
        *(("snmpTypeInteger", 2),
          ("snmpTypeInteger64", 70),
          ("snmpTypeObjectIdentifier", 6),
          ("snmpTypeObjectIpAddress", 64),
          ("snmpTypeOctetString", 4),
          ("snmpTypeUnknown", 0))
    )


_ApTrapInformationTableDataType_Type.__name__ = "Integer32"
_ApTrapInformationTableDataType_Object = MibTableColumn
apTrapInformationTableDataType = _ApTrapInformationTableDataType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 7, 2, 1, 2),
    _ApTrapInformationTableDataType_Type()
)
apTrapInformationTableDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapInformationTableDataType.setStatus("current")
_ApTrapInformationTableDataLength_Type = Unsigned32
_ApTrapInformationTableDataLength_Object = MibTableColumn
apTrapInformationTableDataLength = _ApTrapInformationTableDataLength_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 7, 2, 1, 3),
    _ApTrapInformationTableDataLength_Type()
)
apTrapInformationTableDataLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapInformationTableDataLength.setStatus("current")


class _ApTrapInformationTableDataOctets_Type(OctetString):
    """Custom type apTrapInformationTableDataOctets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApTrapInformationTableDataOctets_Type.__name__ = "OctetString"
_ApTrapInformationTableDataOctets_Object = MibTableColumn
apTrapInformationTableDataOctets = _ApTrapInformationTableDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 7, 2, 1, 4),
    _ApTrapInformationTableDataOctets_Type()
)
apTrapInformationTableDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTrapInformationTableDataOctets.setStatus("current")
_ApSysMgmtInterfaceObjects_ObjectIdentity = ObjectIdentity
apSysMgmtInterfaceObjects = _ApSysMgmtInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 8)
)
_ApSysMgmtPhyUtilTable_Object = MibTable
apSysMgmtPhyUtilTable = _ApSysMgmtPhyUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    apSysMgmtPhyUtilTable.setStatus("current")
_ApSysMgmtPhyUtilTableEntry_Object = MibTableRow
apSysMgmtPhyUtilTableEntry = _ApSysMgmtPhyUtilTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 8, 1, 1)
)
apSysMgmtPhyUtilTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apSysMgmtPhyUtilTableEntry.setStatus("current")
_ApPhyUtilTableRXUtil_Type = SysMgmtPercentage
_ApPhyUtilTableRXUtil_Object = MibTableColumn
apPhyUtilTableRXUtil = _ApPhyUtilTableRXUtil_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 8, 1, 1, 1),
    _ApPhyUtilTableRXUtil_Type()
)
apPhyUtilTableRXUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPhyUtilTableRXUtil.setStatus("current")
_ApPhyUtilTableTXUtil_Type = SysMgmtPercentage
_ApPhyUtilTableTXUtil_Object = MibTableColumn
apPhyUtilTableTXUtil = _ApPhyUtilTableTXUtil_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 1, 8, 1, 1, 2),
    _ApPhyUtilTableTXUtil_Type()
)
apPhyUtilTableTXUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPhyUtilTableTXUtil.setStatus("current")
_ApSysMgmtNotificationObjects_ObjectIdentity = ObjectIdentity
apSysMgmtNotificationObjects = _ApSysMgmtNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 2)
)
_ApSysMgmtTrapType_Type = ObjectIdentifier
_ApSysMgmtTrapType_Object = MibScalar
apSysMgmtTrapType = _ApSysMgmtTrapType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 2, 1),
    _ApSysMgmtTrapType_Type()
)
apSysMgmtTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtTrapType.setStatus("current")
_ApSysMgmtTrapValue_Type = Integer32
_ApSysMgmtTrapValue_Object = MibScalar
apSysMgmtTrapValue = _ApSysMgmtTrapValue_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 2, 2),
    _ApSysMgmtTrapValue_Type()
)
apSysMgmtTrapValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtTrapValue.setStatus("current")
_ApSysMgmtSlotID_Type = Integer32
_ApSysMgmtSlotID_Object = MibScalar
apSysMgmtSlotID = _ApSysMgmtSlotID_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 2, 3),
    _ApSysMgmtSlotID_Type()
)
apSysMgmtSlotID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSlotID.setStatus("current")
_ApSysMgmtSlotType_Type = ApHardwareModuleFamily
_ApSysMgmtSlotType_Object = MibScalar
apSysMgmtSlotType = _ApSysMgmtSlotType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 2, 4),
    _ApSysMgmtSlotType_Type()
)
apSysMgmtSlotType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSlotType.setStatus("current")


class _ApSysMgmtRedundancyState_Type(Integer32):
    """Custom type apSysMgmtRedundancyState based on Integer32"""
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
        *(("active", 1),
          ("outOfService", 5),
          ("recovery", 4),
          ("standby", 2),
          ("unassigned", 3))
    )


_ApSysMgmtRedundancyState_Type.__name__ = "Integer32"
_ApSysMgmtRedundancyState_Object = MibScalar
apSysMgmtRedundancyState = _ApSysMgmtRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 2, 5),
    _ApSysMgmtRedundancyState_Type()
)
apSysMgmtRedundancyState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtRedundancyState.setStatus("current")
_ApSysMgmtSingleUnitRedundancyState_Type = ApRedundancyState
_ApSysMgmtSingleUnitRedundancyState_Object = MibScalar
apSysMgmtSingleUnitRedundancyState = _ApSysMgmtSingleUnitRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 2, 6),
    _ApSysMgmtSingleUnitRedundancyState_Type()
)
apSysMgmtSingleUnitRedundancyState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSingleUnitRedundancyState.setStatus("current")
_ApSysMgmtSipInterfaceActiveLocalContacts_Type = Unsigned32
_ApSysMgmtSipInterfaceActiveLocalContacts_Object = MibScalar
apSysMgmtSipInterfaceActiveLocalContacts = _ApSysMgmtSipInterfaceActiveLocalContacts_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 2, 7),
    _ApSysMgmtSipInterfaceActiveLocalContacts_Type()
)
apSysMgmtSipInterfaceActiveLocalContacts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSipInterfaceActiveLocalContacts.setStatus("obsolete")
_ApSysMgmtSipInterfaceRegCacheLimit_Type = Unsigned32
_ApSysMgmtSipInterfaceRegCacheLimit_Object = MibScalar
apSysMgmtSipInterfaceRegCacheLimit = _ApSysMgmtSipInterfaceRegCacheLimit_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 2, 8),
    _ApSysMgmtSipInterfaceRegCacheLimit_Type()
)
apSysMgmtSipInterfaceRegCacheLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSipInterfaceRegCacheLimit.setStatus("current")
_ApSystemManagementNotificationPrefix_ObjectIdentity = ObjectIdentity
apSystemManagementNotificationPrefix = _ApSystemManagementNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 3)
)
_ApSystemManagementNotifications_ObjectIdentity = ObjectIdentity
apSystemManagementNotifications = _ApSystemManagementNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 3, 0)
)
_ApSystemManagementConformance_ObjectIdentity = ObjectIdentity
apSystemManagementConformance = _ApSystemManagementConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4)
)
_ApSystemManagementCompliances_ObjectIdentity = ObjectIdentity
apSystemManagementCompliances = _ApSystemManagementCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 1)
)
_ApSystemManagementGroups_ObjectIdentity = ObjectIdentity
apSystemManagementGroups = _ApSystemManagementGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2)
)
_ApSystemManagementNotificationsGroups_ObjectIdentity = ObjectIdentity
apSystemManagementNotificationsGroups = _ApSystemManagementNotificationsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3)
)
_ApSystemManagementMonitorGroups_ObjectIdentity = ObjectIdentity
apSystemManagementMonitorGroups = _ApSystemManagementMonitorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 4)
)
_ApSysMgmtMonitorObjects_ObjectIdentity = ObjectIdentity
apSysMgmtMonitorObjects = _ApSysMgmtMonitorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5)
)


class _ApSysMgmtPowerLocation_Type(Integer32):
    """Custom type apSysMgmtPowerLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("left", 0),
          ("right", 1))
    )


_ApSysMgmtPowerLocation_Type.__name__ = "Integer32"
_ApSysMgmtPowerLocation_Object = MibScalar
apSysMgmtPowerLocation = _ApSysMgmtPowerLocation_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 1),
    _ApSysMgmtPowerLocation_Type()
)
apSysMgmtPowerLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtPowerLocation.setStatus("current")


class _ApSysMgmtPowerPresence_Type(Integer32):
    """Custom type apSysMgmtPowerPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_ApSysMgmtPowerPresence_Type.__name__ = "Integer32"
_ApSysMgmtPowerPresence_Object = MibScalar
apSysMgmtPowerPresence = _ApSysMgmtPowerPresence_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 2),
    _ApSysMgmtPowerPresence_Type()
)
apSysMgmtPowerPresence.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtPowerPresence.setStatus("current")
_ApSysMgmtTempValue_Type = Unsigned32
_ApSysMgmtTempValue_Object = MibScalar
apSysMgmtTempValue = _ApSysMgmtTempValue_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 3),
    _ApSysMgmtTempValue_Type()
)
apSysMgmtTempValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtTempValue.setStatus("current")
if mibBuilder.loadTexts:
    apSysMgmtTempValue.setUnits("degrees celsius")


class _ApSysMgmtFanLocation_Type(Integer32):
    """Custom type apSysMgmtFanLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("left", 0),
          ("middle", 1),
          ("right", 2))
    )


_ApSysMgmtFanLocation_Type.__name__ = "Integer32"
_ApSysMgmtFanLocation_Object = MibScalar
apSysMgmtFanLocation = _ApSysMgmtFanLocation_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 4),
    _ApSysMgmtFanLocation_Type()
)
apSysMgmtFanLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtFanLocation.setStatus("current")
_ApSysMgmtFanSpeed_Type = Integer32
_ApSysMgmtFanSpeed_Object = MibScalar
apSysMgmtFanSpeed = _ApSysMgmtFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 5),
    _ApSysMgmtFanSpeed_Type()
)
apSysMgmtFanSpeed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    apSysMgmtFanSpeed.setUnits("%")


class _ApSysMgmtTaskSuspend_Type(DisplayString):
    """Custom type apSysMgmtTaskSuspend based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtTaskSuspend_Type.__name__ = "DisplayString"
_ApSysMgmtTaskSuspend_Object = MibScalar
apSysMgmtTaskSuspend = _ApSysMgmtTaskSuspend_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 6),
    _ApSysMgmtTaskSuspend_Type()
)
apSysMgmtTaskSuspend.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtTaskSuspend.setStatus("current")


class _ApSysMgmtRedRole_Type(Integer32):
    """Custom type apSysMgmtRedRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1))
    )


_ApSysMgmtRedRole_Type.__name__ = "Integer32"
_ApSysMgmtRedRole_Object = MibScalar
apSysMgmtRedRole = _ApSysMgmtRedRole_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 7),
    _ApSysMgmtRedRole_Type()
)
apSysMgmtRedRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtRedRole.setStatus("current")


class _ApSysMgmtRedTransState_Type(Integer32):
    """Custom type apSysMgmtRedTransState based on Integer32"""
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
        *(("active", 1),
          ("no-peer", 3),
          ("out-of-service", 0),
          ("standby", 2))
    )


_ApSysMgmtRedTransState_Type.__name__ = "Integer32"
_ApSysMgmtRedTransState_Object = MibScalar
apSysMgmtRedTransState = _ApSysMgmtRedTransState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 8),
    _ApSysMgmtRedTransState_Type()
)
apSysMgmtRedTransState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtRedTransState.setStatus("current")
_ApSysMgmtMediaPorts_Type = SysMgmtPercentage
_ApSysMgmtMediaPorts_Object = MibScalar
apSysMgmtMediaPorts = _ApSysMgmtMediaPorts_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 9),
    _ApSysMgmtMediaPorts_Type()
)
apSysMgmtMediaPorts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtMediaPorts.setStatus("current")
_ApSysMgmtMediaBandwidth_Type = SysMgmtPercentage
_ApSysMgmtMediaBandwidth_Object = MibScalar
apSysMgmtMediaBandwidth = _ApSysMgmtMediaBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 10),
    _ApSysMgmtMediaBandwidth_Type()
)
apSysMgmtMediaBandwidth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtMediaBandwidth.setStatus("current")


class _ApSysMgmtGatewayUnreachable_Type(DisplayString):
    """Custom type apSysMgmtGatewayUnreachable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtGatewayUnreachable_Type.__name__ = "DisplayString"
_ApSysMgmtGatewayUnreachable_Object = MibScalar
apSysMgmtGatewayUnreachable = _ApSysMgmtGatewayUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 11),
    _ApSysMgmtGatewayUnreachable_Type()
)
apSysMgmtGatewayUnreachable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtGatewayUnreachable.setStatus("current")


class _ApSysMgmtRadiusDown_Type(Integer32):
    """Custom type apSysMgmtRadiusDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("all-servers-down", 0),
          ("some-servers-down", 1))
    )


_ApSysMgmtRadiusDown_Type.__name__ = "Integer32"
_ApSysMgmtRadiusDown_Object = MibScalar
apSysMgmtRadiusDown = _ApSysMgmtRadiusDown_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 12),
    _ApSysMgmtRadiusDown_Type()
)
apSysMgmtRadiusDown.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtRadiusDown.setStatus("current")


class _ApSysMgmtH323InitFail_Type(DisplayString):
    """Custom type apSysMgmtH323InitFail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtH323InitFail_Type.__name__ = "DisplayString"
_ApSysMgmtH323InitFail_Object = MibScalar
apSysMgmtH323InitFail = _ApSysMgmtH323InitFail_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 13),
    _ApSysMgmtH323InitFail_Type()
)
apSysMgmtH323InitFail.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtH323InitFail.setStatus("current")


class _ApSysMgmtCfgSaveFail_Type(DisplayString):
    """Custom type apSysMgmtCfgSaveFail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtCfgSaveFail_Type.__name__ = "DisplayString"
_ApSysMgmtCfgSaveFail_Object = MibScalar
apSysMgmtCfgSaveFail = _ApSysMgmtCfgSaveFail_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 14),
    _ApSysMgmtCfgSaveFail_Type()
)
apSysMgmtCfgSaveFail.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtCfgSaveFail.setStatus("current")


class _ApSysMgmtHardwareError_Type(DisplayString):
    """Custom type apSysMgmtHardwareError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtHardwareError_Type.__name__ = "DisplayString"
_ApSysMgmtHardwareError_Object = MibScalar
apSysMgmtHardwareError = _ApSysMgmtHardwareError_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 15),
    _ApSysMgmtHardwareError_Type()
)
apSysMgmtHardwareError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtHardwareError.setStatus("current")


class _ApSysMgmtSAHostname_Type(DisplayString):
    """Custom type apSysMgmtSAHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtSAHostname_Type.__name__ = "DisplayString"
_ApSysMgmtSAHostname_Object = MibScalar
apSysMgmtSAHostname = _ApSysMgmtSAHostname_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 16),
    _ApSysMgmtSAHostname_Type()
)
apSysMgmtSAHostname.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSAHostname.setStatus("current")


class _ApSysMgmtSAIP_Type(DisplayString):
    """Custom type apSysMgmtSAIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtSAIP_Type.__name__ = "DisplayString"
_ApSysMgmtSAIP_Object = MibScalar
apSysMgmtSAIP = _ApSysMgmtSAIP_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 17),
    _ApSysMgmtSAIP_Type()
)
apSysMgmtSAIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSAIP.setStatus("current")


class _ApSysMgmtSAStatus_Type(Integer32):
    """Custom type apSysMgmtSAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inservice", 0),
          ("outofservice", 1))
    )


_ApSysMgmtSAStatus_Type.__name__ = "Integer32"
_ApSysMgmtSAStatus_Object = MibScalar
apSysMgmtSAStatus = _ApSysMgmtSAStatus_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 18),
    _ApSysMgmtSAStatus_Type()
)
apSysMgmtSAStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSAStatus.setStatus("current")


class _ApSysMgmtSAStatusReason_Type(Integer32):
    """Custom type apSysMgmtSAStatusReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("administrative", 0),
          ("constraintsexceeded", 4),
          ("inservice", 3),
          ("oosbyproxyerror", 1),
          ("oosprovisionedresponse", 6),
          ("standby", 2),
          ("unresponsive", 5))
    )


_ApSysMgmtSAStatusReason_Type.__name__ = "Integer32"
_ApSysMgmtSAStatusReason_Object = MibScalar
apSysMgmtSAStatusReason = _ApSysMgmtSAStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 19),
    _ApSysMgmtSAStatusReason_Type()
)
apSysMgmtSAStatusReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSAStatusReason.setStatus("current")


class _ApSysMgmtAuthFailLevel_Type(Integer32):
    """Custom type apSysMgmtAuthFailLevel based on Integer32"""
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
        *(("login", 0),
          ("priv", 2),
          ("shell", 3),
          ("user", 1))
    )


_ApSysMgmtAuthFailLevel_Type.__name__ = "Integer32"
_ApSysMgmtAuthFailLevel_Object = MibScalar
apSysMgmtAuthFailLevel = _ApSysMgmtAuthFailLevel_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 20),
    _ApSysMgmtAuthFailLevel_Type()
)
apSysMgmtAuthFailLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtAuthFailLevel.setStatus("current")


class _ApSysMgmtAuthFailProto_Type(Integer32):
    """Custom type apSysMgmtAuthFailProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("console", 0),
          ("ftp", 2),
          ("sftp", 4),
          ("ssh", 3),
          ("telnet", 1))
    )


_ApSysMgmtAuthFailProto_Type.__name__ = "Integer32"
_ApSysMgmtAuthFailProto_Object = MibScalar
apSysMgmtAuthFailProto = _ApSysMgmtAuthFailProto_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 21),
    _ApSysMgmtAuthFailProto_Type()
)
apSysMgmtAuthFailProto.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtAuthFailProto.setStatus("current")


class _ApSysMgmtAuthFailOrigin_Type(DisplayString):
    """Custom type apSysMgmtAuthFailOrigin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtAuthFailOrigin_Type.__name__ = "DisplayString"
_ApSysMgmtAuthFailOrigin_Object = MibScalar
apSysMgmtAuthFailOrigin = _ApSysMgmtAuthFailOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 22),
    _ApSysMgmtAuthFailOrigin_Type()
)
apSysMgmtAuthFailOrigin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtAuthFailOrigin.setStatus("current")


class _ApSysMgmtSystemState_Type(Integer32):
    """Custom type apSysMgmtSystemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("becoming-offline", 1),
          ("offline", 2),
          ("online", 0))
    )


_ApSysMgmtSystemState_Type.__name__ = "Integer32"
_ApSysMgmtSystemState_Object = MibScalar
apSysMgmtSystemState = _ApSysMgmtSystemState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 23),
    _ApSysMgmtSystemState_Type()
)
apSysMgmtSystemState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSystemState.setStatus("current")


class _ApSysMgmtTaskDelete_Type(DisplayString):
    """Custom type apSysMgmtTaskDelete based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtTaskDelete_Type.__name__ = "DisplayString"
_ApSysMgmtTaskDelete_Object = MibScalar
apSysMgmtTaskDelete = _ApSysMgmtTaskDelete_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 24),
    _ApSysMgmtTaskDelete_Type()
)
apSysMgmtTaskDelete.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtTaskDelete.setStatus("current")
_ApSysMgmtAlgdCPULoad_Type = SysMgmtPercentage
_ApSysMgmtAlgdCPULoad_Object = MibScalar
apSysMgmtAlgdCPULoad = _ApSysMgmtAlgdCPULoad_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 25),
    _ApSysMgmtAlgdCPULoad_Type()
)
apSysMgmtAlgdCPULoad.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtAlgdCPULoad.setStatus("current")


class _ApSysMgmtSipInterfaceRealmName_Type(DisplayString):
    """Custom type apSysMgmtSipInterfaceRealmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtSipInterfaceRealmName_Type.__name__ = "DisplayString"
_ApSysMgmtSipInterfaceRealmName_Object = MibScalar
apSysMgmtSipInterfaceRealmName = _ApSysMgmtSipInterfaceRealmName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 26),
    _ApSysMgmtSipInterfaceRealmName_Type()
)
apSysMgmtSipInterfaceRealmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSipInterfaceRealmName.setStatus("current")


class _ApSysMgmtSipInterfaceIP_Type(DisplayString):
    """Custom type apSysMgmtSipInterfaceIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtSipInterfaceIP_Type.__name__ = "DisplayString"
_ApSysMgmtSipInterfaceIP_Object = MibScalar
apSysMgmtSipInterfaceIP = _ApSysMgmtSipInterfaceIP_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 27),
    _ApSysMgmtSipInterfaceIP_Type()
)
apSysMgmtSipInterfaceIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSipInterfaceIP.setStatus("current")


class _ApSysMgmtSipInterfaceStatus_Type(Integer32):
    """Custom type apSysMgmtSipInterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inservice", 0),
          ("outofservice", 1))
    )


_ApSysMgmtSipInterfaceStatus_Type.__name__ = "Integer32"
_ApSysMgmtSipInterfaceStatus_Object = MibScalar
apSysMgmtSipInterfaceStatus = _ApSysMgmtSipInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 28),
    _ApSysMgmtSipInterfaceStatus_Type()
)
apSysMgmtSipInterfaceStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSipInterfaceStatus.setStatus("current")


class _ApSysMgmtSipInterfaceStatusReason_Type(Integer32):
    """Custom type apSysMgmtSipInterfaceStatusReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("administrative", 0),
          ("constraintsexceeded", 4),
          ("inservice", 3),
          ("oosbyproxyerror", 1),
          ("standby", 2),
          ("unresponsive", 5))
    )


_ApSysMgmtSipInterfaceStatusReason_Type.__name__ = "Integer32"
_ApSysMgmtSipInterfaceStatusReason_Object = MibScalar
apSysMgmtSipInterfaceStatusReason = _ApSysMgmtSipInterfaceStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 29),
    _ApSysMgmtSipInterfaceStatusReason_Type()
)
apSysMgmtSipInterfaceStatusReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSipInterfaceStatusReason.setStatus("current")


class _ApSysMgmtCollectPushServerUnreachable_Type(DisplayString):
    """Custom type apSysMgmtCollectPushServerUnreachable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtCollectPushServerUnreachable_Type.__name__ = "DisplayString"
_ApSysMgmtCollectPushServerUnreachable_Object = MibScalar
apSysMgmtCollectPushServerUnreachable = _ApSysMgmtCollectPushServerUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 30),
    _ApSysMgmtCollectPushServerUnreachable_Type()
)
apSysMgmtCollectPushServerUnreachable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtCollectPushServerUnreachable.setStatus("current")


class _ApSysMgmtNTPServer_Type(DisplayString):
    """Custom type apSysMgmtNTPServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtNTPServer_Type.__name__ = "DisplayString"
_ApSysMgmtNTPServer_Object = MibScalar
apSysMgmtNTPServer = _ApSysMgmtNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 31),
    _ApSysMgmtNTPServer_Type()
)
apSysMgmtNTPServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtNTPServer.setStatus("current")


class _ApSysMgmtBorderGatewayId_Type(DisplayString):
    """Custom type apSysMgmtBorderGatewayId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtBorderGatewayId_Type.__name__ = "DisplayString"
_ApSysMgmtBorderGatewayId_Object = MibScalar
apSysMgmtBorderGatewayId = _ApSysMgmtBorderGatewayId_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 32),
    _ApSysMgmtBorderGatewayId_Type()
)
apSysMgmtBorderGatewayId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtBorderGatewayId.setStatus("current")


class _ApSysMgmtRFactor_Type(DisplayString):
    """Custom type apSysMgmtRFactor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtRFactor_Type.__name__ = "DisplayString"
_ApSysMgmtRFactor_Object = MibScalar
apSysMgmtRFactor = _ApSysMgmtRFactor_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 33),
    _ApSysMgmtRFactor_Type()
)
apSysMgmtRFactor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtRFactor.setStatus("current")


class _ApSysMgmtCallId_Type(DisplayString):
    """Custom type apSysMgmtCallId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtCallId_Type.__name__ = "DisplayString"
_ApSysMgmtCallId_Object = MibScalar
apSysMgmtCallId = _ApSysMgmtCallId_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 34),
    _ApSysMgmtCallId_Type()
)
apSysMgmtCallId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtCallId.setStatus("current")


class _ApSysMgmtSurrogateRegHost_Type(DisplayString):
    """Custom type apSysMgmtSurrogateRegHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtSurrogateRegHost_Type.__name__ = "DisplayString"
_ApSysMgmtSurrogateRegHost_Object = MibScalar
apSysMgmtSurrogateRegHost = _ApSysMgmtSurrogateRegHost_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 35),
    _ApSysMgmtSurrogateRegHost_Type()
)
apSysMgmtSurrogateRegHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSurrogateRegHost.setStatus("current")


class _ApSysMgmtSurrogateRegAor_Type(DisplayString):
    """Custom type apSysMgmtSurrogateRegAor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtSurrogateRegAor_Type.__name__ = "DisplayString"
_ApSysMgmtSurrogateRegAor_Object = MibScalar
apSysMgmtSurrogateRegAor = _ApSysMgmtSurrogateRegAor_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 36),
    _ApSysMgmtSurrogateRegAor_Type()
)
apSysMgmtSurrogateRegAor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSurrogateRegAor.setStatus("current")


class _ApSysMgmtRealmID_Type(DisplayString):
    """Custom type apSysMgmtRealmID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtRealmID_Type.__name__ = "DisplayString"
_ApSysMgmtRealmID_Object = MibScalar
apSysMgmtRealmID = _ApSysMgmtRealmID_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 37),
    _ApSysMgmtRealmID_Type()
)
apSysMgmtRealmID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtRealmID.setStatus("current")


class _ApSysMgmtCollectorPushNodeName_Type(DisplayString):
    """Custom type apSysMgmtCollectorPushNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtCollectorPushNodeName_Type.__name__ = "DisplayString"
_ApSysMgmtCollectorPushNodeName_Object = MibScalar
apSysMgmtCollectorPushNodeName = _ApSysMgmtCollectorPushNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 38),
    _ApSysMgmtCollectorPushNodeName_Type()
)
apSysMgmtCollectorPushNodeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtCollectorPushNodeName.setStatus("current")


class _ApSysMgmtCollectorPushUniqueFileName_Type(DisplayString):
    """Custom type apSysMgmtCollectorPushUniqueFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtCollectorPushUniqueFileName_Type.__name__ = "DisplayString"
_ApSysMgmtCollectorPushUniqueFileName_Object = MibScalar
apSysMgmtCollectorPushUniqueFileName = _ApSysMgmtCollectorPushUniqueFileName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 39),
    _ApSysMgmtCollectorPushUniqueFileName_Type()
)
apSysMgmtCollectorPushUniqueFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtCollectorPushUniqueFileName.setStatus("current")


class _ApSysMgmtCollectorPushReceiverAddress_Type(DisplayString):
    """Custom type apSysMgmtCollectorPushReceiverAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtCollectorPushReceiverAddress_Type.__name__ = "DisplayString"
_ApSysMgmtCollectorPushReceiverAddress_Object = MibScalar
apSysMgmtCollectorPushReceiverAddress = _ApSysMgmtCollectorPushReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 40),
    _ApSysMgmtCollectorPushReceiverAddress_Type()
)
apSysMgmtCollectorPushReceiverAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtCollectorPushReceiverAddress.setStatus("current")


class _ApSysMgmtRealmName_Type(DisplayString):
    """Custom type apSysMgmtRealmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtRealmName_Type.__name__ = "DisplayString"
_ApSysMgmtRealmName_Object = MibScalar
apSysMgmtRealmName = _ApSysMgmtRealmName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 41),
    _ApSysMgmtRealmName_Type()
)
apSysMgmtRealmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtRealmName.setStatus("current")


class _ApSysMgmtRealmStatusReason_Type(Integer32):
    """Custom type apSysMgmtRealmStatusReason based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("administrative", 0),
          ("callloadreduction", 7),
          ("constraintsexceeded", 4),
          ("inservice", 3),
          ("oosbyproxyerror", 1),
          ("oosprovisionedresponse", 6),
          ("standby", 2),
          ("unresponsive", 5))
    )


_ApSysMgmtRealmStatusReason_Type.__name__ = "Integer32"
_ApSysMgmtRealmStatusReason_Object = MibScalar
apSysMgmtRealmStatusReason = _ApSysMgmtRealmStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 42),
    _ApSysMgmtRealmStatusReason_Type()
)
apSysMgmtRealmStatusReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtRealmStatusReason.setStatus("current")


class _ApSysMgmtGatewaySynchronized_Type(DisplayString):
    """Custom type apSysMgmtGatewaySynchronized based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtGatewaySynchronized_Type.__name__ = "DisplayString"
_ApSysMgmtGatewaySynchronized_Object = MibScalar
apSysMgmtGatewaySynchronized = _ApSysMgmtGatewaySynchronized_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 43),
    _ApSysMgmtGatewaySynchronized_Type()
)
apSysMgmtGatewaySynchronized.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtGatewaySynchronized.setStatus("current")


class _ApSysCallRecordingServerName_Type(DisplayString):
    """Custom type apSysCallRecordingServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysCallRecordingServerName_Type.__name__ = "DisplayString"
_ApSysCallRecordingServerName_Object = MibScalar
apSysCallRecordingServerName = _ApSysCallRecordingServerName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 44),
    _ApSysCallRecordingServerName_Type()
)
apSysCallRecordingServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysCallRecordingServerName.setStatus("current")


class _ApSysCallRecordingServerState_Type(Integer32):
    """Custom type apSysCallRecordingServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("no-active", 4),
          ("not-monitoring", 1),
          ("primary-active", 2),
          ("secondary-active", 3),
          ("unknown", 0))
    )


_ApSysCallRecordingServerState_Type.__name__ = "Integer32"
_ApSysCallRecordingServerState_Object = MibScalar
apSysCallRecordingServerState = _ApSysCallRecordingServerState_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 45),
    _ApSysCallRecordingServerState_Type()
)
apSysCallRecordingServerState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysCallRecordingServerState.setStatus("current")
_ApSysCDRPushReceiverAddressType_Type = InetAddressType
_ApSysCDRPushReceiverAddressType_Object = MibScalar
apSysCDRPushReceiverAddressType = _ApSysCDRPushReceiverAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 46),
    _ApSysCDRPushReceiverAddressType_Type()
)
apSysCDRPushReceiverAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysCDRPushReceiverAddressType.setStatus("current")
_ApSysCDRPushReceiverAddress_Type = InetAddress
_ApSysCDRPushReceiverAddress_Object = MibScalar
apSysCDRPushReceiverAddress = _ApSysCDRPushReceiverAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 47),
    _ApSysCDRPushReceiverAddress_Type()
)
apSysCDRPushReceiverAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysCDRPushReceiverAddress.setStatus("current")


class _ApSysCDRPushReceiverFailureReasonCode_Type(Integer32):
    """Custom type apSysCDRPushReceiverFailureReasonCode based on Integer32"""
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
        *(("authentication-error", 3),
          ("connection-error", 2),
          ("file-access-error", 1),
          ("unknown", 0))
    )


_ApSysCDRPushReceiverFailureReasonCode_Type.__name__ = "Integer32"
_ApSysCDRPushReceiverFailureReasonCode_Object = MibScalar
apSysCDRPushReceiverFailureReasonCode = _ApSysCDRPushReceiverFailureReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 48),
    _ApSysCDRPushReceiverFailureReasonCode_Type()
)
apSysCDRPushReceiverFailureReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysCDRPushReceiverFailureReasonCode.setStatus("current")


class _ApSysAdminAuditLogFullReason_Type(Integer32):
    """Custom type apSysAdminAuditLogFullReason based on Integer32"""
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
        *(("file-size", 0),
          ("file-transfer-time", 2),
          ("maxspaceused-deletingfile", 3),
          ("percentage-full", 1))
    )


_ApSysAdminAuditLogFullReason_Type.__name__ = "Integer32"
_ApSysAdminAuditLogFullReason_Object = MibScalar
apSysAdminAuditLogFullReason = _ApSysAdminAuditLogFullReason_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 49),
    _ApSysAdminAuditLogFullReason_Type()
)
apSysAdminAuditLogFullReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysAdminAuditLogFullReason.setStatus("current")


class _ApSysAdminWriteErrorCode_Type(Integer32):
    """Custom type apSysAdminWriteErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("comress-error", 3),
          ("encrypt-error", 4),
          ("io-error", 2),
          ("no-space", 5),
          ("not-open", 1),
          ("unknown", 0))
    )


_ApSysAdminWriteErrorCode_Type.__name__ = "Integer32"
_ApSysAdminWriteErrorCode_Object = MibScalar
apSysAdminWriteErrorCode = _ApSysAdminWriteErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 50),
    _ApSysAdminWriteErrorCode_Type()
)
apSysAdminWriteErrorCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysAdminWriteErrorCode.setStatus("current")


class _ApSysAdminFileName_Type(DisplayString):
    """Custom type apSysAdminFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysAdminFileName_Type.__name__ = "DisplayString"
_ApSysAdminFileName_Object = MibScalar
apSysAdminFileName = _ApSysAdminFileName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 51),
    _ApSysAdminFileName_Type()
)
apSysAdminFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysAdminFileName.setStatus("current")
_ApSysAddressType_Type = InetAddressType
_ApSysAddressType_Object = MibScalar
apSysAddressType = _ApSysAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 52),
    _ApSysAddressType_Type()
)
apSysAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysAddressType.setStatus("current")
_ApSysAddress_Type = InetAddress
_ApSysAddress_Object = MibScalar
apSysAddress = _ApSysAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 53),
    _ApSysAddress_Type()
)
apSysAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysAddress.setStatus("current")


class _ApSysReasonCode_Type(Integer32):
    """Custom type apSysReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("file-transfer-error", 2),
          ("login-error", 1),
          ("unknown", 0))
    )


_ApSysReasonCode_Type.__name__ = "Integer32"
_ApSysReasonCode_Object = MibScalar
apSysReasonCode = _ApSysReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 54),
    _ApSysReasonCode_Type()
)
apSysReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysReasonCode.setStatus("current")
_ApSysMgmtPhyUtilCurrent_Type = Unsigned32
_ApSysMgmtPhyUtilCurrent_Object = MibScalar
apSysMgmtPhyUtilCurrent = _ApSysMgmtPhyUtilCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 55),
    _ApSysMgmtPhyUtilCurrent_Type()
)
apSysMgmtPhyUtilCurrent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtPhyUtilCurrent.setStatus("current")
_ApSysMgmtPhyUtilMinorThreshold_Type = Unsigned32
_ApSysMgmtPhyUtilMinorThreshold_Object = MibScalar
apSysMgmtPhyUtilMinorThreshold = _ApSysMgmtPhyUtilMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 56),
    _ApSysMgmtPhyUtilMinorThreshold_Type()
)
apSysMgmtPhyUtilMinorThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtPhyUtilMinorThreshold.setStatus("current")
_ApSysMgmtPhyUtilMajorThreshold_Type = Unsigned32
_ApSysMgmtPhyUtilMajorThreshold_Object = MibScalar
apSysMgmtPhyUtilMajorThreshold = _ApSysMgmtPhyUtilMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 57),
    _ApSysMgmtPhyUtilMajorThreshold_Type()
)
apSysMgmtPhyUtilMajorThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtPhyUtilMajorThreshold.setStatus("current")
_ApSysMgmtPhyUtilCriticalThreshold_Type = Unsigned32
_ApSysMgmtPhyUtilCriticalThreshold_Object = MibScalar
apSysMgmtPhyUtilCriticalThreshold = _ApSysMgmtPhyUtilCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 58),
    _ApSysMgmtPhyUtilCriticalThreshold_Type()
)
apSysMgmtPhyUtilCriticalThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtPhyUtilCriticalThreshold.setStatus("current")
_ApSysMgmtPhyRejectOverUtil_Type = Unsigned32
_ApSysMgmtPhyRejectOverUtil_Object = MibScalar
apSysMgmtPhyRejectOverUtil = _ApSysMgmtPhyRejectOverUtil_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 59),
    _ApSysMgmtPhyRejectOverUtil_Type()
)
apSysMgmtPhyRejectOverUtil.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtPhyRejectOverUtil.setStatus("current")
_ApSysMgmtSpaceAvailCurrent_Type = Unsigned32
_ApSysMgmtSpaceAvailCurrent_Object = MibScalar
apSysMgmtSpaceAvailCurrent = _ApSysMgmtSpaceAvailCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 60),
    _ApSysMgmtSpaceAvailCurrent_Type()
)
apSysMgmtSpaceAvailCurrent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSpaceAvailCurrent.setStatus("current")
_ApSysMgmtSpaceAvailMinorThreshold_Type = Unsigned32
_ApSysMgmtSpaceAvailMinorThreshold_Object = MibScalar
apSysMgmtSpaceAvailMinorThreshold = _ApSysMgmtSpaceAvailMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 61),
    _ApSysMgmtSpaceAvailMinorThreshold_Type()
)
apSysMgmtSpaceAvailMinorThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSpaceAvailMinorThreshold.setStatus("current")
_ApSysMgmtSpaceAvailMajorThreshold_Type = Unsigned32
_ApSysMgmtSpaceAvailMajorThreshold_Object = MibScalar
apSysMgmtSpaceAvailMajorThreshold = _ApSysMgmtSpaceAvailMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 62),
    _ApSysMgmtSpaceAvailMajorThreshold_Type()
)
apSysMgmtSpaceAvailMajorThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSpaceAvailMajorThreshold.setStatus("current")
_ApSysMgmtSpaceAvailCriticalThreshold_Type = Unsigned32
_ApSysMgmtSpaceAvailCriticalThreshold_Object = MibScalar
apSysMgmtSpaceAvailCriticalThreshold = _ApSysMgmtSpaceAvailCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 63),
    _ApSysMgmtSpaceAvailCriticalThreshold_Type()
)
apSysMgmtSpaceAvailCriticalThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSpaceAvailCriticalThreshold.setStatus("current")


class _ApSysMgmtPartitionPath_Type(DisplayString):
    """Custom type apSysMgmtPartitionPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtPartitionPath_Type.__name__ = "DisplayString"
_ApSysMgmtPartitionPath_Object = MibScalar
apSysMgmtPartitionPath = _ApSysMgmtPartitionPath_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 64),
    _ApSysMgmtPartitionPath_Type()
)
apSysMgmtPartitionPath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtPartitionPath.setStatus("current")
_ApSysMgmtTcaOid_Type = ObjectIdentifier
_ApSysMgmtTcaOid_Object = MibScalar
apSysMgmtTcaOid = _ApSysMgmtTcaOid_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 65),
    _ApSysMgmtTcaOid_Type()
)
apSysMgmtTcaOid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtTcaOid.setStatus("current")
_ApSysMgmtTcaCurrent_Type = Unsigned32
_ApSysMgmtTcaCurrent_Object = MibScalar
apSysMgmtTcaCurrent = _ApSysMgmtTcaCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 66),
    _ApSysMgmtTcaCurrent_Type()
)
apSysMgmtTcaCurrent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtTcaCurrent.setStatus("current")
_ApSysMgmtTcaMinorThreshold_Type = Unsigned32
_ApSysMgmtTcaMinorThreshold_Object = MibScalar
apSysMgmtTcaMinorThreshold = _ApSysMgmtTcaMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 67),
    _ApSysMgmtTcaMinorThreshold_Type()
)
apSysMgmtTcaMinorThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtTcaMinorThreshold.setStatus("current")
_ApSysMgmtTcaMajorThreshold_Type = Unsigned32
_ApSysMgmtTcaMajorThreshold_Object = MibScalar
apSysMgmtTcaMajorThreshold = _ApSysMgmtTcaMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 68),
    _ApSysMgmtTcaMajorThreshold_Type()
)
apSysMgmtTcaMajorThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtTcaMajorThreshold.setStatus("current")
_ApSysMgmtTcaCriticalThreshold_Type = Unsigned32
_ApSysMgmtTcaCriticalThreshold_Object = MibScalar
apSysMgmtTcaCriticalThreshold = _ApSysMgmtTcaCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 69),
    _ApSysMgmtTcaCriticalThreshold_Type()
)
apSysMgmtTcaCriticalThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtTcaCriticalThreshold.setStatus("current")


class _ApSysEPSName_Type(DisplayString):
    """Custom type apSysEPSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysEPSName_Type.__name__ = "DisplayString"
_ApSysEPSName_Object = MibScalar
apSysEPSName = _ApSysEPSName_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 70),
    _ApSysEPSName_Type()
)
apSysEPSName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysEPSName.setStatus("current")


class _ApSysEPSFqdn_Type(DisplayString):
    """Custom type apSysEPSFqdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysEPSFqdn_Type.__name__ = "DisplayString"
_ApSysEPSFqdn_Object = MibScalar
apSysEPSFqdn = _ApSysEPSFqdn_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 71),
    _ApSysEPSFqdn_Type()
)
apSysEPSFqdn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysEPSFqdn.setStatus("current")


class _ApSysEPSAddress_Type(DisplayString):
    """Custom type apSysEPSAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysEPSAddress_Type.__name__ = "DisplayString"
_ApSysEPSAddress_Object = MibScalar
apSysEPSAddress = _ApSysEPSAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 72),
    _ApSysEPSAddress_Type()
)
apSysEPSAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysEPSAddress.setStatus("current")


class _ApSysEPSRealm_Type(DisplayString):
    """Custom type apSysEPSRealm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysEPSRealm_Type.__name__ = "DisplayString"
_ApSysEPSRealm_Object = MibScalar
apSysEPSRealm = _ApSysEPSRealm_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 73),
    _ApSysEPSRealm_Type()
)
apSysEPSRealm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysEPSRealm.setStatus("current")


class _ApSysEPSOperationType_Type(DisplayString):
    """Custom type apSysEPSOperationType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysEPSOperationType_Type.__name__ = "DisplayString"
_ApSysEPSOperationType_Object = MibScalar
apSysEPSOperationType = _ApSysEPSOperationType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 74),
    _ApSysEPSOperationType_Type()
)
apSysEPSOperationType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysEPSOperationType.setStatus("current")
_ApSysMgmtDatabaseContactMinorThreshold_Type = Unsigned32
_ApSysMgmtDatabaseContactMinorThreshold_Object = MibScalar
apSysMgmtDatabaseContactMinorThreshold = _ApSysMgmtDatabaseContactMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 75),
    _ApSysMgmtDatabaseContactMinorThreshold_Type()
)
apSysMgmtDatabaseContactMinorThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtDatabaseContactMinorThreshold.setStatus("current")
_ApSysMgmtDatabaseContactMajorThreshold_Type = Unsigned32
_ApSysMgmtDatabaseContactMajorThreshold_Object = MibScalar
apSysMgmtDatabaseContactMajorThreshold = _ApSysMgmtDatabaseContactMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 76),
    _ApSysMgmtDatabaseContactMajorThreshold_Type()
)
apSysMgmtDatabaseContactMajorThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtDatabaseContactMajorThreshold.setStatus("current")
_ApSysMgmtDatabaseContactCriticalThreshold_Type = Unsigned32
_ApSysMgmtDatabaseContactCriticalThreshold_Object = MibScalar
apSysMgmtDatabaseContactCriticalThreshold = _ApSysMgmtDatabaseContactCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 77),
    _ApSysMgmtDatabaseContactCriticalThreshold_Type()
)
apSysMgmtDatabaseContactCriticalThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtDatabaseContactCriticalThreshold.setStatus("current")


class _ApSysMgmtTacacsDown_Type(Integer32):
    """Custom type apSysMgmtTacacsDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("all-servers-down", 0),
          ("some-servers-down", 1))
    )


_ApSysMgmtTacacsDown_Type.__name__ = "Integer32"
_ApSysMgmtTacacsDown_Object = MibScalar
apSysMgmtTacacsDown = _ApSysMgmtTacacsDown_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 78),
    _ApSysMgmtTacacsDown_Type()
)
apSysMgmtTacacsDown.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtTacacsDown.setStatus("current")


class _ApSysMgmtOCSRDown_Type(Integer32):
    """Custom type apSysMgmtOCSRDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("all-servers-down", 0),
          ("some-servers-down", 1))
    )


_ApSysMgmtOCSRDown_Type.__name__ = "Integer32"
_ApSysMgmtOCSRDown_Object = MibScalar
apSysMgmtOCSRDown = _ApSysMgmtOCSRDown_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 5, 79),
    _ApSysMgmtOCSRDown_Type()
)
apSysMgmtOCSRDown.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtOCSRDown.setStatus("current")
_ApSystemManagementMonitorPrefix_ObjectIdentity = ObjectIdentity
apSystemManagementMonitorPrefix = _ApSystemManagementMonitorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6)
)
_ApSystemManagementMonitors_ObjectIdentity = ObjectIdentity
apSystemManagementMonitors = _ApSystemManagementMonitors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0)
)
_ApSysMgmtDOSObjects_ObjectIdentity = ObjectIdentity
apSysMgmtDOSObjects = _ApSysMgmtDOSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 7)
)
_ApSysMgmtDOSNotificationObjects_ObjectIdentity = ObjectIdentity
apSysMgmtDOSNotificationObjects = _ApSysMgmtDOSNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 7, 1)
)
_ApSysMgmtDOSIpAddress_Type = IpAddress
_ApSysMgmtDOSIpAddress_Object = MibScalar
apSysMgmtDOSIpAddress = _ApSysMgmtDOSIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 7, 1, 1),
    _ApSysMgmtDOSIpAddress_Type()
)
apSysMgmtDOSIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtDOSIpAddress.setStatus("deprecated")


class _ApSysMgmtDOSRealmID_Type(DisplayString):
    """Custom type apSysMgmtDOSRealmID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtDOSRealmID_Type.__name__ = "DisplayString"
_ApSysMgmtDOSRealmID_Object = MibScalar
apSysMgmtDOSRealmID = _ApSysMgmtDOSRealmID_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 7, 1, 2),
    _ApSysMgmtDOSRealmID_Type()
)
apSysMgmtDOSRealmID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtDOSRealmID.setStatus("current")


class _ApSysMgmtDOSFromUri_Type(DisplayString):
    """Custom type apSysMgmtDOSFromUri based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtDOSFromUri_Type.__name__ = "DisplayString"
_ApSysMgmtDOSFromUri_Object = MibScalar
apSysMgmtDOSFromUri = _ApSysMgmtDOSFromUri_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 7, 1, 3),
    _ApSysMgmtDOSFromUri_Type()
)
apSysMgmtDOSFromUri.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtDOSFromUri.setStatus("current")
_ApSysMgmtDOSInetAddressType_Type = InetAddressType
_ApSysMgmtDOSInetAddressType_Object = MibScalar
apSysMgmtDOSInetAddressType = _ApSysMgmtDOSInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 7, 1, 4),
    _ApSysMgmtDOSInetAddressType_Type()
)
apSysMgmtDOSInetAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtDOSInetAddressType.setStatus("current")
_ApSysMgmtDOSInetAddress_Type = InetAddress
_ApSysMgmtDOSInetAddress_Object = MibScalar
apSysMgmtDOSInetAddress = _ApSysMgmtDOSInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 7, 1, 5),
    _ApSysMgmtDOSInetAddress_Type()
)
apSysMgmtDOSInetAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtDOSInetAddress.setStatus("current")


class _ApSysMgmtDOSReason_Type(DisplayString):
    """Custom type apSysMgmtDOSReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtDOSReason_Type.__name__ = "DisplayString"
_ApSysMgmtDOSReason_Object = MibScalar
apSysMgmtDOSReason = _ApSysMgmtDOSReason_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 7, 1, 6),
    _ApSysMgmtDOSReason_Type()
)
apSysMgmtDOSReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtDOSReason.setStatus("current")
_ApSysMgmtDOSNotificationPrefix_ObjectIdentity = ObjectIdentity
apSysMgmtDOSNotificationPrefix = _ApSysMgmtDOSNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 8)
)
_ApSysMgmtDOSNotifications_ObjectIdentity = ObjectIdentity
apSysMgmtDOSNotifications = _ApSysMgmtDOSNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 8, 0)
)
_ApSysMgmtSipRejectionObjects_ObjectIdentity = ObjectIdentity
apSysMgmtSipRejectionObjects = _ApSysMgmtSipRejectionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 9)
)
_ApSysMgmtSipRejectionNotificationObjects_ObjectIdentity = ObjectIdentity
apSysMgmtSipRejectionNotificationObjects = _ApSysMgmtSipRejectionNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 9, 1)
)


class _ApSysMgmtSipRejFromUriUser_Type(DisplayString):
    """Custom type apSysMgmtSipRejFromUriUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSysMgmtSipRejFromUriUser_Type.__name__ = "DisplayString"
_ApSysMgmtSipRejFromUriUser_Object = MibScalar
apSysMgmtSipRejFromUriUser = _ApSysMgmtSipRejFromUriUser_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 9, 1, 1),
    _ApSysMgmtSipRejFromUriUser_Type()
)
apSysMgmtSipRejFromUriUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSipRejFromUriUser.setStatus("current")


class _ApSysMgmtSipRejToUriUser_Type(DisplayString):
    """Custom type apSysMgmtSipRejToUriUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSysMgmtSipRejToUriUser_Type.__name__ = "DisplayString"
_ApSysMgmtSipRejToUriUser_Object = MibScalar
apSysMgmtSipRejToUriUser = _ApSysMgmtSipRejToUriUser_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 9, 1, 2),
    _ApSysMgmtSipRejToUriUser_Type()
)
apSysMgmtSipRejToUriUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSipRejToUriUser.setStatus("current")


class _ApSysMgmtSipRejRequestUri_Type(DisplayString):
    """Custom type apSysMgmtSipRejRequestUri based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSysMgmtSipRejRequestUri_Type.__name__ = "DisplayString"
_ApSysMgmtSipRejRequestUri_Object = MibScalar
apSysMgmtSipRejRequestUri = _ApSysMgmtSipRejRequestUri_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 9, 1, 3),
    _ApSysMgmtSipRejRequestUri_Type()
)
apSysMgmtSipRejRequestUri.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSipRejRequestUri.setStatus("current")


class _ApSysMgmtSipRejContactUri_Type(DisplayString):
    """Custom type apSysMgmtSipRejContactUri based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ApSysMgmtSipRejContactUri_Type.__name__ = "DisplayString"
_ApSysMgmtSipRejContactUri_Object = MibScalar
apSysMgmtSipRejContactUri = _ApSysMgmtSipRejContactUri_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 9, 1, 4),
    _ApSysMgmtSipRejContactUri_Type()
)
apSysMgmtSipRejContactUri.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSipRejContactUri.setStatus("current")
_ApSysMgmtSipRejIpAddress_Type = IpAddress
_ApSysMgmtSipRejIpAddress_Object = MibScalar
apSysMgmtSipRejIpAddress = _ApSysMgmtSipRejIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 9, 1, 5),
    _ApSysMgmtSipRejIpAddress_Type()
)
apSysMgmtSipRejIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSipRejIpAddress.setStatus("current")


class _ApSysMgmtSipRejMsgType_Type(Integer32):
    """Custom type apSysMgmtSipRejMsgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("call", 1),
          ("registration", 0))
    )


_ApSysMgmtSipRejMsgType_Type.__name__ = "Integer32"
_ApSysMgmtSipRejMsgType_Object = MibScalar
apSysMgmtSipRejMsgType = _ApSysMgmtSipRejMsgType_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 9, 1, 6),
    _ApSysMgmtSipRejMsgType_Type()
)
apSysMgmtSipRejMsgType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSipRejMsgType.setStatus("current")
_ApSysMgmtSipRejMethod_Type = Integer32
_ApSysMgmtSipRejMethod_Object = MibScalar
apSysMgmtSipRejMethod = _ApSysMgmtSipRejMethod_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 9, 1, 7),
    _ApSysMgmtSipRejMethod_Type()
)
apSysMgmtSipRejMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSipRejMethod.setStatus("current")


class _ApSysMgmtSipRejReason_Type(DisplayString):
    """Custom type apSysMgmtSipRejReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApSysMgmtSipRejReason_Type.__name__ = "DisplayString"
_ApSysMgmtSipRejReason_Object = MibScalar
apSysMgmtSipRejReason = _ApSysMgmtSipRejReason_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 9, 1, 8),
    _ApSysMgmtSipRejReason_Type()
)
apSysMgmtSipRejReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    apSysMgmtSipRejReason.setStatus("current")
_ApSysMgmtSipRejectionNotificationPrefix_ObjectIdentity = ObjectIdentity
apSysMgmtSipRejectionNotificationPrefix = _ApSysMgmtSipRejectionNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 10)
)
_ApSysMgmtSipRejectionNotifications_ObjectIdentity = ObjectIdentity
apSysMgmtSipRejectionNotifications = _ApSysMgmtSipRejectionNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 10, 0)
)

# Managed Objects groups

apSysMgmtGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 1)
)
apSysMgmtGeneralGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysCPUUtil"),
        ("APSYSMGMT-MIB", "apSysMemoryUtil"),
        ("APSYSMGMT-MIB", "apSysHealthScore"),
        ("APSYSMGMT-MIB", "apSysRedundancy"),
        ("APSYSMGMT-MIB", "apSysGlobalConSess"),
        ("APSYSMGMT-MIB", "apSysGlobalCPS"),
        ("APSYSMGMT-MIB", "apSysNATCapacity"),
        ("APSYSMGMT-MIB", "apSysARPCapacity"),
        ("APSYSMGMT-MIB", "apSysState"),
        ("APSYSMGMT-MIB", "apSysLicenseCapacity"),
        ("APSYSMGMT-MIB", "apSysCurrentEndptsDenied"),
        ("APSYSMGMT-MIB", "apSysXCodeCapacity"),
        ("APSYSMGMT-MIB", "apSysXCodeAMRCapacity"),
        ("APSYSMGMT-MIB", "apSysXCodeAMRWBCapacity"))
)
if mibBuilder.loadTexts:
    apSysMgmtGeneralGroup.setStatus("current")

apSysMgmtCombinedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 2)
)
apSysMgmtCombinedGroup.setObjects(
      *(("APSYSMGMT-MIB", "apCombinedStatsSessionAgentIndex"),
        ("APSYSMGMT-MIB", "apCombinedStatsSessionAgentHostname"),
        ("APSYSMGMT-MIB", "apCombinedStatsSessionAgentType"),
        ("APSYSMGMT-MIB", "apCombinedStatsCurrentActiveSessionsInbound"),
        ("APSYSMGMT-MIB", "apCombinedStatsCurrentSessionRateInbound"),
        ("APSYSMGMT-MIB", "apCombinedStatsCurrentActiveSessionsOutbound"),
        ("APSYSMGMT-MIB", "apCombinedStatsCurrentSessionRateOutbound"),
        ("APSYSMGMT-MIB", "apCombinedStatsTotalSessionsInbound"),
        ("APSYSMGMT-MIB", "apCombinedStatsTotalSessionsNotAdmittedInbound"),
        ("APSYSMGMT-MIB", "apCombinedStatsPeriodHighInbound"),
        ("APSYSMGMT-MIB", "apCombinedStatsAverageRateInbound"),
        ("APSYSMGMT-MIB", "apCombinedStatsTotalSessionsOutbound"),
        ("APSYSMGMT-MIB", "apCombinedStatsTotalSessionsNotAdmittedOutbound"),
        ("APSYSMGMT-MIB", "apCombinedStatsPeriodHighOutbound"),
        ("APSYSMGMT-MIB", "apCombinedStatsAverageRateOutbound"),
        ("APSYSMGMT-MIB", "apCombinedStatsMaxBurstRate"),
        ("APSYSMGMT-MIB", "apCombinedStatsPeriodSeizures"),
        ("APSYSMGMT-MIB", "apCombinedStatsPeriodAnswers"),
        ("APSYSMGMT-MIB", "apCombinedStatsPeriodASR"),
        ("APSYSMGMT-MIB", "apCombinedStatsAverageLatency"),
        ("APSYSMGMT-MIB", "apCombinedStatsMaxLatency"),
        ("APSYSMGMT-MIB", "apCombinedStatsSessionAgentStatus"))
)
if mibBuilder.loadTexts:
    apSysMgmtCombinedGroup.setStatus("current")

apSysMgmtSipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 3)
)
apSysMgmtSipGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSipSAStatsSessionAgentIndex"),
        ("APSYSMGMT-MIB", "apSipSAStatsSessionAgentHostname"),
        ("APSYSMGMT-MIB", "apSipSAStatsSessionAgentType"),
        ("APSYSMGMT-MIB", "apSipSAStatsCurrentActiveSessionsInbound"),
        ("APSYSMGMT-MIB", "apSipSAStatsCurrentSessionRateInbound"),
        ("APSYSMGMT-MIB", "apSipSAStatsCurrentActiveSessionsOutbound"),
        ("APSYSMGMT-MIB", "apSipSAStatsCurrentSessionRateOutbound"),
        ("APSYSMGMT-MIB", "apSipSAStatsTotalSessionsInbound"),
        ("APSYSMGMT-MIB", "apSipSAStatsTotalSessionsNotAdmittedInbound"),
        ("APSYSMGMT-MIB", "apSipSAStatsPeriodHighInbound"),
        ("APSYSMGMT-MIB", "apSipSAStatsAverageRateInbound"),
        ("APSYSMGMT-MIB", "apSipSAStatsTotalSessionsOutbound"),
        ("APSYSMGMT-MIB", "apSipSAStatsTotalSessionsNotAdmittedOutbound"),
        ("APSYSMGMT-MIB", "apSipSAStatsPeriodHighOutbound"),
        ("APSYSMGMT-MIB", "apSipSAStatsAverageRateOutbound"),
        ("APSYSMGMT-MIB", "apSipSAStatsMaxBurstRate"),
        ("APSYSMGMT-MIB", "apSipSAStatsPeriodSeizures"),
        ("APSYSMGMT-MIB", "apSipSAStatsPeriodAnswers"),
        ("APSYSMGMT-MIB", "apSipSAStatsPeriodASR"),
        ("APSYSMGMT-MIB", "apSipSAStatsAverageLatency"),
        ("APSYSMGMT-MIB", "apSipSAStatsMaxLatency"),
        ("APSYSMGMT-MIB", "apSipSAStatsSessionAgentStatus"))
)
if mibBuilder.loadTexts:
    apSysMgmtSipGroup.setStatus("current")

apSysMgmtH323Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 4)
)
apSysMgmtH323Group.setObjects(
      *(("APSYSMGMT-MIB", "apH323SAStatsSessionAgentIndex"),
        ("APSYSMGMT-MIB", "apH323SAStatsSessionAgentHostname"),
        ("APSYSMGMT-MIB", "apH323SAStatsSessionAgentType"),
        ("APSYSMGMT-MIB", "apH323SAStatsCurrentActiveSessionsInbound"),
        ("APSYSMGMT-MIB", "apH323SAStatsCurrentSessionRateInbound"),
        ("APSYSMGMT-MIB", "apH323SAStatsCurrentActiveSessionsOutbound"),
        ("APSYSMGMT-MIB", "apH323SAStatsCurrentSessionRateOutbound"),
        ("APSYSMGMT-MIB", "apH323SAStatsTotalSessionsInbound"),
        ("APSYSMGMT-MIB", "apH323SAStatsTotalSessionsNotAdmittedInbound"),
        ("APSYSMGMT-MIB", "apH323SAStatsPeriodHighInbound"),
        ("APSYSMGMT-MIB", "apH323SAStatsAverageRateInbound"),
        ("APSYSMGMT-MIB", "apH323SAStatsTotalSessionsOutbound"),
        ("APSYSMGMT-MIB", "apH323SAStatsTotalSessionsNotAdmittedOutbound"),
        ("APSYSMGMT-MIB", "apH323SAStatsPeriodHighOutbound"),
        ("APSYSMGMT-MIB", "apH323SAStatsAverageRateOutbound"),
        ("APSYSMGMT-MIB", "apH323SAStatsMaxBurstRate"),
        ("APSYSMGMT-MIB", "apH323SAStatsPeriodSeizures"),
        ("APSYSMGMT-MIB", "apH323SAStatsPeriodAnswers"),
        ("APSYSMGMT-MIB", "apH323SAStatsPeriodASR"),
        ("APSYSMGMT-MIB", "apH323SAStatsAverageLatency"),
        ("APSYSMGMT-MIB", "apH323SAStatsMaxLatency"),
        ("APSYSMGMT-MIB", "apH323SAStatsSessionAgentStatus"))
)
if mibBuilder.loadTexts:
    apSysMgmtH323Group.setStatus("current")

apSysMgmtSigRealmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 5)
)
apSysMgmtSigRealmGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSigRealmStatsRealmIndex"),
        ("APSYSMGMT-MIB", "apSigRealmStatsRealmName"),
        ("APSYSMGMT-MIB", "apSigRealmStatsCurrentActiveSessionsInbound"),
        ("APSYSMGMT-MIB", "apSigRealmStatsCurrentSessionRateInbound"),
        ("APSYSMGMT-MIB", "apSigRealmStatsCurrentActiveSessionsOutbound"),
        ("APSYSMGMT-MIB", "apSigRealmStatsCurrentSessionRateOutbound"),
        ("APSYSMGMT-MIB", "apSigRealmStatsTotalSessionsInbound"),
        ("APSYSMGMT-MIB", "apSigRealmStatsTotalSessionsNotAdmittedInbound"),
        ("APSYSMGMT-MIB", "apSigRealmStatsPeriodHighInbound"),
        ("APSYSMGMT-MIB", "apSigRealmStatsAverageRateInbound"),
        ("APSYSMGMT-MIB", "apSigRealmStatsTotalSessionsOutbound"),
        ("APSYSMGMT-MIB", "apSigRealmStatsTotalSessionsNotAdmittedOutbound"),
        ("APSYSMGMT-MIB", "apSigRealmStatsPeriodHighOutbound"),
        ("APSYSMGMT-MIB", "apSigRealmStatsAverageRateOutbound"),
        ("APSYSMGMT-MIB", "apSigRealmStatsMaxBurstRate"),
        ("APSYSMGMT-MIB", "apSigRealmStatsPeriodSeizures"),
        ("APSYSMGMT-MIB", "apSigRealmStatsPeriodAnswers"),
        ("APSYSMGMT-MIB", "apSigRealmStatsPeriodASR"))
)
if mibBuilder.loadTexts:
    apSysMgmtSigRealmGroup.setStatus("current")

apSysMgmtCtrlStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 6)
)
apSysMgmtCtrlStatsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apNetMgmtCtrlStatsName"),
        ("APSYSMGMT-MIB", "apNetMgmtCtrlStatsType"),
        ("APSYSMGMT-MIB", "apNetMgmtCtrlStatsIncomingTotal"),
        ("APSYSMGMT-MIB", "apNetMgmtCtrlStatsRejectedTotal"),
        ("APSYSMGMT-MIB", "apNetMgmtCtrlStatsDivertedTotal"),
        ("APSYSMGMT-MIB", "apNetMgmtCtrlStatsIncomingCurrent"),
        ("APSYSMGMT-MIB", "apNetMgmtCtrlStatsRejectedCurrent"),
        ("APSYSMGMT-MIB", "apNetMgmtCtrlStatsDivertedCurrent"),
        ("APSYSMGMT-MIB", "apNetMgmtCtrlStatsIncomingPeriodMax"),
        ("APSYSMGMT-MIB", "apNetMgmtCtrlStatsRejectedPeriodMax"),
        ("APSYSMGMT-MIB", "apNetMgmtCtrlStatsDivertedPeriodMax"))
)
if mibBuilder.loadTexts:
    apSysMgmtCtrlStatsGroup.setStatus("current")

apSysMgmtENUMServerStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 7)
)
apSysMgmtENUMServerStatusGroup.setObjects(
      *(("APSYSMGMT-MIB", "apENUMConfigName"),
        ("APSYSMGMT-MIB", "apENUMServerIpAddress"),
        ("APSYSMGMT-MIB", "apENUMServerStatus"))
)
if mibBuilder.loadTexts:
    apSysMgmtENUMServerStatusGroup.setStatus("obsolete")

apSysMgmtNSEPStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 8)
)
apSysMgmtNSEPStatsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apNSEPStatsCurrentActiveSessionsInbound"),
        ("APSYSMGMT-MIB", "apNSEPStatsTotalSessionsInbound"),
        ("APSYSMGMT-MIB", "apNSEPStatsPeriodHighInbound"),
        ("APSYSMGMT-MIB", "apNSEPStatsPeriod"),
        ("APSYSMGMT-MIB", "apNSEPStatsRPHValue"),
        ("APSYSMGMT-MIB", "apNSEPStatsRPHCurrentActiveSessionsInbound"),
        ("APSYSMGMT-MIB", "apNSEPStatsRPHTotalSessionsInbound"),
        ("APSYSMGMT-MIB", "apNSEPStatsRPHPeriodHighInbound"),
        ("APSYSMGMT-MIB", "apNSEPStatsRPHTotalSessionsNotAdmittedInbound"),
        ("APSYSMGMT-MIB", "apNSEPStatsRPHCurrentActiveSessionsOutbound"),
        ("APSYSMGMT-MIB", "apNSEPStatsRPHTotalSessionsOutbound"),
        ("APSYSMGMT-MIB", "apNSEPStatsRPHPeriodHighOutbound"),
        ("APSYSMGMT-MIB", "apNSEPStatsRPHTotalSessionsNotAdmittedOutbound"))
)
if mibBuilder.loadTexts:
    apSysMgmtNSEPStatsGroup.setStatus("current")

apSysMgmtExtSigRealmStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 9)
)
apSysMgmtExtSigRealmStatsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSigRealmStatsMinutesLeft"),
        ("APSYSMGMT-MIB", "apSigRealmStatsMinutesReject"))
)
if mibBuilder.loadTexts:
    apSysMgmtExtSigRealmStatsGroup.setStatus("current")

apSysMgmtLDAPServerStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 10)
)
apSysMgmtLDAPServerStatusGroup.setObjects(
      *(("APSYSMGMT-MIB", "apLDAPConfigName"),
        ("APSYSMGMT-MIB", "apLDAPServerIpAddress"),
        ("APSYSMGMT-MIB", "apLDAPServerStatus"))
)
if mibBuilder.loadTexts:
    apSysMgmtLDAPServerStatusGroup.setStatus("current")

apSysMgmtRegistrationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 11)
)
apSysMgmtRegistrationGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysSipStatsActiveLocalContacts"),
        ("APSYSMGMT-MIB", "apSysMgcpGWEndpoints"),
        ("APSYSMGMT-MIB", "apSysH323Registration"))
)
if mibBuilder.loadTexts:
    apSysMgmtRegistrationGroup.setStatus("current")

apSysMgmtRegCacheLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 12)
)
apSysMgmtRegCacheLimitGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysRegCacheLimit")
)
if mibBuilder.loadTexts:
    apSysMgmtRegCacheLimitGroup.setStatus("current")

apSysMgmtShortSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 13)
)
apSysMgmtShortSessionGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysShortSessionThreshold"),
        ("APSYSMGMT-MIB", "apSigRealmStatsShortSessions"))
)
if mibBuilder.loadTexts:
    apSysMgmtShortSessionGroup.setStatus("current")

apSysMgmtTrapTableObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 14)
)
apSysMgmtTrapTableObjectGroup.setObjects(
      *(("APSYSMGMT-MIB", "apTrapTableNumVariables"),
        ("APSYSMGMT-MIB", "apTrapTableSysUptime"),
        ("APSYSMGMT-MIB", "apTrapInformationTableDataType"),
        ("APSYSMGMT-MIB", "apTrapInformationTableDataLength"),
        ("APSYSMGMT-MIB", "apTrapInformationTableDataOctets"))
)
if mibBuilder.loadTexts:
    apSysMgmtTrapTableObjectGroup.setStatus("current")

apSysMgmtRealmStatsQoSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 15)
)
apSysMgmtRealmStatsQoSGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSigRealmStatsAverageQoSRFactor"),
        ("APSYSMGMT-MIB", "apSigRealmStatsMaximumQoSRFactor"),
        ("APSYSMGMT-MIB", "apSigRealmStatsCurrentMajorRFactorExceeded"),
        ("APSYSMGMT-MIB", "apSigRealmStatsTotalMajorRFactorExceeded"),
        ("APSYSMGMT-MIB", "apSigRealmStatsCurrentCriticalRFactorExceeded"),
        ("APSYSMGMT-MIB", "apSigRealmStatsTotalCriticalRFactorExceeded"),
        ("APSYSMGMT-MIB", "apSigRealmStatsRealmStatus"))
)
if mibBuilder.loadTexts:
    apSysMgmtRealmStatsQoSGroup.setStatus("current")

apSysMgmtApplicationCPUUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 16)
)
apSysMgmtApplicationCPUUsageGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysApplicationCPULoadRate")
)
if mibBuilder.loadTexts:
    apSysMgmtApplicationCPUUsageGroup.setStatus("current")

apSysMgmtRegistrationCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 17)
)
apSysMgmtRegistrationCapacityGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysRegistrationCapacity")
)
if mibBuilder.loadTexts:
    apSysMgmtRegistrationCapacityGroup.setStatus("obsolete")

apSysMgmtRejectedMessagesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 18)
)
apSysMgmtRejectedMessagesGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysRejectedMessages")
)
if mibBuilder.loadTexts:
    apSysMgmtRejectedMessagesGroup.setStatus("current")

apSysMgmtEndPtDemotionObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 19)
)
apSysMgmtEndPtDemotionObjectGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysSipEndptDemTrustToUntrust"),
        ("APSYSMGMT-MIB", "apSysSipEndptDemUntrustToDeny"),
        ("APSYSMGMT-MIB", "apSysMgcpEndptDemTrustToUntrust"),
        ("APSYSMGMT-MIB", "apSysMgcpEndptDemUntrustToDeny"))
)
if mibBuilder.loadTexts:
    apSysMgmtEndPtDemotionObjectGroup.setStatus("current")

apSysMgmtCallRecordingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 20)
)
apSysMgmtCallRecordingGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysCallRecordingServerName"),
        ("APSYSMGMT-MIB", "apSysCallRecordingServerState"))
)
if mibBuilder.loadTexts:
    apSysMgmtCallRecordingGroup.setStatus("current")

apSysMgmtPhyUtilGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 21)
)
apSysMgmtPhyUtilGroup.setObjects(
      *(("APSYSMGMT-MIB", "apPhyUtilTableRXUtil"),
        ("APSYSMGMT-MIB", "apPhyUtilTableTXUtil"))
)
if mibBuilder.loadTexts:
    apSysMgmtPhyUtilGroup.setStatus("current")

apSysMgmtStorageSpaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 22)
)
apSysMgmtStorageSpaceGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysVolumeIndex"),
        ("APSYSMGMT-MIB", "apSysVolumeName"),
        ("APSYSMGMT-MIB", "apSysVolumeTotalSpace"),
        ("APSYSMGMT-MIB", "apSysVolumeAvailSpace"))
)
if mibBuilder.loadTexts:
    apSysMgmtStorageSpaceGroup.setStatus("current")

apSysMgmtCtrlStatsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 23)
)
apSysMgmtCtrlStatsGroup2.setObjects(
    ("APSYSMGMT-MIB", "apNetMgmtCtrlStatsState")
)
if mibBuilder.loadTexts:
    apSysMgmtCtrlStatsGroup2.setStatus("current")

apSysMgmtDatabaseRegGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 24)
)
apSysMgmtDatabaseRegGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysSipStatsActiveDatabaseContacts"),
        ("APSYSMGMT-MIB", "apSysMgmtDatabaseContactMinorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtDatabaseContactMajorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtDatabaseContactCriticalThreshold"))
)
if mibBuilder.loadTexts:
    apSysMgmtDatabaseRegGroup.setStatus("current")

apSysMgmtCallsRejectedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 25)
)
apSysMgmtCallsRejectedGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysSipTotalCallsRejected")
)
if mibBuilder.loadTexts:
    apSysMgmtCallsRejectedGroup.setStatus("current")

apSysMgmtRealmRegCacheSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 26)
)
apSysMgmtRealmRegCacheSummaryGroup.setObjects(
    ("APSYSMGMT-MIB", "apSigRealmStatsActiveLocalContacts")
)
if mibBuilder.loadTexts:
    apSysMgmtRealmRegCacheSummaryGroup.setStatus("current")

apSysMgmtSubscriptionSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 27)
)
apSysMgmtSubscriptionSummaryGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSigRealmStatsActiveSubscriptions"),
        ("APSYSMGMT-MIB", "apSigRealmStatsPerMaxSubscriptions"),
        ("APSYSMGMT-MIB", "apSigRealmStatsMaximumActiveSubscriptions"),
        ("APSYSMGMT-MIB", "apSigRealmStatsTotalSubscriptions"),
        ("APSYSMGMT-MIB", "apSysSipStatsActiveSubscriptions"),
        ("APSYSMGMT-MIB", "apSysSipStatsPerMaxSubscriptions"),
        ("APSYSMGMT-MIB", "apSysSipStatsMaximumActiveSubscriptions"),
        ("APSYSMGMT-MIB", "apSysSipStatsTotalSubscriptions"))
)
if mibBuilder.loadTexts:
    apSysMgmtSubscriptionSummaryGroup.setStatus("current")

apSysMgmtETCUtilGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 2, 28)
)
apSysMgmtETCUtilGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysETCCoreCPUUtil"),
        ("APSYSMGMT-MIB", "apSysETCMemoryPoolMemUtil"))
)
if mibBuilder.loadTexts:
    apSysMgmtETCUtilGroup.setStatus("current")


# Notification objects

apSysMgmtGroupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 3, 0, 1)
)
apSysMgmtGroupTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtTrapType"),
        ("APSYSMGMT-MIB", "apSysMgmtTrapValue"))
)
if mibBuilder.loadTexts:
    apSysMgmtGroupTrap.setStatus(
        "current"
    )

apSysMgmtGroupClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 3, 0, 2)
)
apSysMgmtGroupClearTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtTrapType")
)
if mibBuilder.loadTexts:
    apSysMgmtGroupClearTrap.setStatus(
        "current"
    )

apSysMgmtSingleUnitRedundancyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 3, 0, 3)
)
apSysMgmtSingleUnitRedundancyTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtSlotID"),
        ("APSYSMGMT-MIB", "apSysMgmtSlotType"),
        ("APSYSMGMT-MIB", "apSysMgmtSingleUnitRedundancyState"))
)
if mibBuilder.loadTexts:
    apSysMgmtSingleUnitRedundancyTrap.setStatus(
        "current"
    )

apSysMgmtPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 1)
)
apSysMgmtPowerTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtPowerLocation"),
        ("APSYSMGMT-MIB", "apSysMgmtPowerPresence"))
)
if mibBuilder.loadTexts:
    apSysMgmtPowerTrap.setStatus(
        "current"
    )

apSysMgmtTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 2)
)
apSysMgmtTempTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtTempValue")
)
if mibBuilder.loadTexts:
    apSysMgmtTempTrap.setStatus(
        "current"
    )

apSysMgmtFanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 3)
)
apSysMgmtFanTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtFanLocation"),
        ("APSYSMGMT-MIB", "apSysMgmtFanSpeed"))
)
if mibBuilder.loadTexts:
    apSysMgmtFanTrap.setStatus(
        "current"
    )

apSysMgmtTaskSuspendTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 4)
)
apSysMgmtTaskSuspendTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtTaskSuspend")
)
if mibBuilder.loadTexts:
    apSysMgmtTaskSuspendTrap.setStatus(
        "current"
    )

apSysMgmtRedundancyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 5)
)
apSysMgmtRedundancyTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtRedRole"),
        ("APSYSMGMT-MIB", "apSysMgmtRedTransState"))
)
if mibBuilder.loadTexts:
    apSysMgmtRedundancyTrap.setStatus(
        "current"
    )

apSysMgmtMediaPortsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 6)
)
apSysMgmtMediaPortsTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtMediaPorts")
)
if mibBuilder.loadTexts:
    apSysMgmtMediaPortsTrap.setStatus(
        "current"
    )

apSysMgmtMediaBandwidthTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 7)
)
apSysMgmtMediaBandwidthTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtMediaBandwidth")
)
if mibBuilder.loadTexts:
    apSysMgmtMediaBandwidthTrap.setStatus(
        "current"
    )

apSysMgmtMediaOutOfMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 8)
)
if mibBuilder.loadTexts:
    apSysMgmtMediaOutOfMemory.setStatus(
        "current"
    )

apSysMgmtMediaUnknownRealm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 9)
)
if mibBuilder.loadTexts:
    apSysMgmtMediaUnknownRealm.setStatus(
        "current"
    )

apSysMgmtGatewayUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 10)
)
apSysMgmtGatewayUnreachableTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtGatewayUnreachable")
)
if mibBuilder.loadTexts:
    apSysMgmtGatewayUnreachableTrap.setStatus(
        "current"
    )

apSysMgmtRadiusDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 11)
)
apSysMgmtRadiusDownTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtRadiusDown")
)
if mibBuilder.loadTexts:
    apSysMgmtRadiusDownTrap.setStatus(
        "current"
    )

apSysMgmtH323InitFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 12)
)
apSysMgmtH323InitFailTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtH323InitFail")
)
if mibBuilder.loadTexts:
    apSysMgmtH323InitFailTrap.setStatus(
        "current"
    )

apSysMgmtCfgSaveFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 13)
)
apSysMgmtCfgSaveFailTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtCfgSaveFail")
)
if mibBuilder.loadTexts:
    apSysMgmtCfgSaveFailTrap.setStatus(
        "current"
    )

apSysMgmtHardwareErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 14)
)
apSysMgmtHardwareErrorTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtHardwareError")
)
if mibBuilder.loadTexts:
    apSysMgmtHardwareErrorTrap.setStatus(
        "current"
    )

apSysMgmtSAStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 15)
)
apSysMgmtSAStatusChangeTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtSAHostname"),
        ("APSYSMGMT-MIB", "apSysMgmtSAIP"),
        ("APSYSMGMT-MIB", "apSysMgmtSAStatus"),
        ("APSYSMGMT-MIB", "apSysMgmtSAStatusReason"))
)
if mibBuilder.loadTexts:
    apSysMgmtSAStatusChangeTrap.setStatus(
        "current"
    )

apSysMgmtAuthenticationFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 16)
)
apSysMgmtAuthenticationFailedTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtAuthFailLevel"),
        ("APSYSMGMT-MIB", "apSysMgmtAuthFailProto"),
        ("APSYSMGMT-MIB", "apSysMgmtAuthFailOrigin"))
)
if mibBuilder.loadTexts:
    apSysMgmtAuthenticationFailedTrap.setStatus(
        "current"
    )

apSysMgmtSystemStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 17)
)
apSysMgmtSystemStateTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtSystemState")
)
if mibBuilder.loadTexts:
    apSysMgmtSystemStateTrap.setStatus(
        "current"
    )

apSysMgmtMediaPortsClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 18)
)
if mibBuilder.loadTexts:
    apSysMgmtMediaPortsClearTrap.setStatus(
        "current"
    )

apSysMgmtMediaBandwidthClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 19)
)
if mibBuilder.loadTexts:
    apSysMgmtMediaBandwidthClearTrap.setStatus(
        "current"
    )

apSysMgmtMediaOutOfMemoryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 20)
)
if mibBuilder.loadTexts:
    apSysMgmtMediaOutOfMemoryClear.setStatus(
        "current"
    )

apSysMgmtGatewayUnreachableClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 21)
)
apSysMgmtGatewayUnreachableClearTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtGatewayUnreachable")
)
if mibBuilder.loadTexts:
    apSysMgmtGatewayUnreachableClearTrap.setStatus(
        "current"
    )

apSysMgmtRadiusDownClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 22)
)
if mibBuilder.loadTexts:
    apSysMgmtRadiusDownClearTrap.setStatus(
        "current"
    )

apSysMgmtTaskDeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 23)
)
apSysMgmtTaskDeleteTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtTaskDelete")
)
if mibBuilder.loadTexts:
    apSysMgmtTaskDeleteTrap.setStatus(
        "current"
    )

apSysMgmtAlgdCPULoadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 24)
)
apSysMgmtAlgdCPULoadTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtAlgdCPULoad")
)
if mibBuilder.loadTexts:
    apSysMgmtAlgdCPULoadTrap.setStatus(
        "current"
    )

apSysMgmtAlgdCPULoadClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 25)
)
if mibBuilder.loadTexts:
    apSysMgmtAlgdCPULoadClearTrap.setStatus(
        "current"
    )

apSysMgmtInterfaceStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 26)
)
apSysMgmtInterfaceStatusChangeTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtSipInterfaceRealmName"),
        ("APSYSMGMT-MIB", "apSysMgmtSipInterfaceIP"),
        ("APSYSMGMT-MIB", "apSysMgmtSipInterfaceStatus"),
        ("APSYSMGMT-MIB", "apSysMgmtSipInterfaceStatusReason"))
)
if mibBuilder.loadTexts:
    apSysMgmtInterfaceStatusChangeTrap.setStatus(
        "current"
    )

apSysMgmtENUMStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 27)
)
apSysMgmtENUMStatusChangeTrap.setObjects(
      *(("APSYSMGMT-MIB", "apENUMConfigName"),
        ("APSYSMGMT-MIB", "apENUMServerIpAddress"),
        ("APSYSMGMT-MIB", "apENUMServerStatus"))
)
if mibBuilder.loadTexts:
    apSysMgmtENUMStatusChangeTrap.setStatus(
        "obsolete"
    )

apSysMgmtPushServerUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 28)
)
apSysMgmtPushServerUnreachableTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtCollectPushServerUnreachable")
)
if mibBuilder.loadTexts:
    apSysMgmtPushServerUnreachableTrap.setStatus(
        "current"
    )

apSysMgmtPushServerUnreachableClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 29)
)
apSysMgmtPushServerUnreachableClearTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtCollectPushServerUnreachable")
)
if mibBuilder.loadTexts:
    apSysMgmtPushServerUnreachableClearTrap.setStatus(
        "current"
    )

apSysMgmtNTPServerUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 30)
)
apSysMgmtNTPServerUnreachableTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtNTPServer")
)
if mibBuilder.loadTexts:
    apSysMgmtNTPServerUnreachableTrap.setStatus(
        "current"
    )

apSysMgmtNTPServerUnreachableClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 31)
)
apSysMgmtNTPServerUnreachableClearTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtNTPServer")
)
if mibBuilder.loadTexts:
    apSysMgmtNTPServerUnreachableClearTrap.setStatus(
        "current"
    )

apSysMgmtNTPServiceDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 32)
)
if mibBuilder.loadTexts:
    apSysMgmtNTPServiceDownTrap.setStatus(
        "current"
    )

apSysMgmtNTPServiceDownClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 33)
)
if mibBuilder.loadTexts:
    apSysMgmtNTPServiceDownClearTrap.setStatus(
        "current"
    )

apSysMgmtMediaSupervisionTimerExpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 34)
)
apSysMgmtMediaSupervisionTimerExpTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtCallId")
)
if mibBuilder.loadTexts:
    apSysMgmtMediaSupervisionTimerExpTrap.setStatus(
        "current"
    )

apSysMgmntH248AssociationLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 35)
)
apSysMgmntH248AssociationLostTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtBorderGatewayId")
)
if mibBuilder.loadTexts:
    apSysMgmntH248AssociationLostTrap.setStatus(
        "current"
    )

apSysMgmntH248AssociationLostClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 36)
)
apSysMgmntH248AssociationLostClearTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtBorderGatewayId")
)
if mibBuilder.loadTexts:
    apSysMgmntH248AssociationLostClearTrap.setStatus(
        "current"
    )

apSysMgmtRFactorBelowThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 37)
)
apSysMgmtRFactorBelowThresholdTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtRFactor"),
        ("APSYSMGMT-MIB", "apSysMgmtCallId"))
)
if mibBuilder.loadTexts:
    apSysMgmtRFactorBelowThresholdTrap.setStatus(
        "current"
    )

apSysMgmtRFactorBelowThresholdClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 38)
)
apSysMgmtRFactorBelowThresholdClearTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtCallId")
)
if mibBuilder.loadTexts:
    apSysMgmtRFactorBelowThresholdClearTrap.setStatus(
        "current"
    )

apSysMgmtSurrogateRegFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 39)
)
apSysMgmtSurrogateRegFailed.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtSurrogateRegHost"),
        ("APSYSMGMT-MIB", "apSysMgmtSurrogateRegAor"))
)
if mibBuilder.loadTexts:
    apSysMgmtSurrogateRegFailed.setStatus(
        "current"
    )

apSysMgmtRealmMinutesExceedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 40)
)
apSysMgmtRealmMinutesExceedTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtRealmID")
)
if mibBuilder.loadTexts:
    apSysMgmtRealmMinutesExceedTrap.setStatus(
        "current"
    )

apSysMgmtRealmMinutesExceedClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 41)
)
apSysMgmtRealmMinutesExceedClearTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtRealmID")
)
if mibBuilder.loadTexts:
    apSysMgmtRealmMinutesExceedClearTrap.setStatus(
        "current"
    )

apSysMgmtLDAPStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 42)
)
apSysMgmtLDAPStatusChangeTrap.setObjects(
      *(("APSYSMGMT-MIB", "apLDAPConfigName"),
        ("APSYSMGMT-MIB", "apLDAPServerIpAddress"),
        ("APSYSMGMT-MIB", "apLDAPServerStatus"))
)
if mibBuilder.loadTexts:
    apSysMgmtLDAPStatusChangeTrap.setStatus(
        "current"
    )

apSysMgmtNTPClockSkewTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 43)
)
if mibBuilder.loadTexts:
    apSysMgmtNTPClockSkewTrap.setStatus(
        "current"
    )

apSysMgmtCollectorPushSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 44)
)
apSysMgmtCollectorPushSuccessTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtCollectorPushNodeName"),
        ("APSYSMGMT-MIB", "apSysMgmtCollectorPushUniqueFileName"),
        ("APSYSMGMT-MIB", "apSysMgmtCollectorPushReceiverAddress"))
)
if mibBuilder.loadTexts:
    apSysMgmtCollectorPushSuccessTrap.setStatus(
        "current"
    )

apSysMgmtRealmStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 45)
)
apSysMgmtRealmStatusChangeTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtRealmName"),
        ("APSYSMGMT-MIB", "apSysMgmtRealmStatusReason"))
)
if mibBuilder.loadTexts:
    apSysMgmtRealmStatusChangeTrap.setStatus(
        "current"
    )

apSysMgmtRegCacheThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 46)
)
apSysMgmtRegCacheThresholdTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysSipStatsActiveLocalContacts"),
        ("APSYSMGMT-MIB", "apSysRegCacheLimit"))
)
if mibBuilder.loadTexts:
    apSysMgmtRegCacheThresholdTrap.setStatus(
        "current"
    )

apSysMgmtRegCacheThresholdClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 47)
)
apSysMgmtRegCacheThresholdClearTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysSipStatsActiveLocalContacts"),
        ("APSYSMGMT-MIB", "apSysRegCacheLimit"))
)
if mibBuilder.loadTexts:
    apSysMgmtRegCacheThresholdClearTrap.setStatus(
        "current"
    )

apSysMgmtShortSessionExceedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 48)
)
apSysMgmtShortSessionExceedTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtRealmID")
)
if mibBuilder.loadTexts:
    apSysMgmtShortSessionExceedTrap.setStatus(
        "current"
    )

apSysMgmtGatewaySynchronizedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 49)
)
apSysMgmtGatewaySynchronizedTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtGatewaySynchronized")
)
if mibBuilder.loadTexts:
    apSysMgmtGatewaySynchronizedTrap.setStatus(
        "current"
    )

apSysMgmtCallRecordingStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 50)
)
apSysMgmtCallRecordingStateChangeTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysCallRecordingServerName"),
        ("APSYSMGMT-MIB", "apSysCallRecordingServerState"))
)
if mibBuilder.loadTexts:
    apSysMgmtCallRecordingStateChangeTrap.setStatus(
        "current"
    )

apSysMgmtRealmIcmpFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 51)
)
apSysMgmtRealmIcmpFailureTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtRealmID")
)
if mibBuilder.loadTexts:
    apSysMgmtRealmIcmpFailureTrap.setStatus(
        "current"
    )

apSysMgmtRealmIcmpFailureClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 52)
)
apSysMgmtRealmIcmpFailureClearTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtRealmID")
)
if mibBuilder.loadTexts:
    apSysMgmtRealmIcmpFailureClearTrap.setStatus(
        "current"
    )

apSysMgmtCDRPushReceiverFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 53)
)
apSysMgmtCDRPushReceiverFailureTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysCDRPushReceiverAddressType"),
        ("APSYSMGMT-MIB", "apSysCDRPushReceiverAddress"),
        ("APSYSMGMT-MIB", "apSysCDRPushReceiverFailureReasonCode"))
)
if mibBuilder.loadTexts:
    apSysMgmtCDRPushReceiverFailureTrap.setStatus(
        "current"
    )

apSysMgmtCDRPushReceiverFailureClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 54)
)
apSysMgmtCDRPushReceiverFailureClearTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysCDRPushReceiverAddressType"),
        ("APSYSMGMT-MIB", "apSysCDRPushReceiverAddress"))
)
if mibBuilder.loadTexts:
    apSysMgmtCDRPushReceiverFailureClearTrap.setStatus(
        "current"
    )

apSysMgmtCDRPushAllReceiversFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 55)
)
if mibBuilder.loadTexts:
    apSysMgmtCDRPushAllReceiversFailureTrap.setStatus(
        "current"
    )

apSysMgmtCDRPushAllReceiversFailureClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 56)
)
if mibBuilder.loadTexts:
    apSysMgmtCDRPushAllReceiversFailureClearTrap.setStatus(
        "current"
    )

apSysMgmtRejectedMesagesThresholdExeededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 57)
)
apSysMgmtRejectedMesagesThresholdExeededTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysRejectedMessages")
)
if mibBuilder.loadTexts:
    apSysMgmtRejectedMesagesThresholdExeededTrap.setStatus(
        "current"
    )

apSysMgmtAdminAuditLogFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 58)
)
apSysMgmtAdminAuditLogFullTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysAdminAuditLogFullReason"),
        ("APSYSMGMT-MIB", "apSysAdminFileName"))
)
if mibBuilder.loadTexts:
    apSysMgmtAdminAuditLogFullTrap.setStatus(
        "current"
    )

apSysMgmtAdminAuditLogFullClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 59)
)
if mibBuilder.loadTexts:
    apSysMgmtAdminAuditLogFullClearTrap.setStatus(
        "current"
    )

apSysMgmtAdminAuditPushFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 60)
)
apSysMgmtAdminAuditPushFailTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysAddressType"),
        ("APSYSMGMT-MIB", "apSysAddress"),
        ("APSYSMGMT-MIB", "apSysReasonCode"))
)
if mibBuilder.loadTexts:
    apSysMgmtAdminAuditPushFailTrap.setStatus(
        "current"
    )

apSysMgmtAdminAuditPushFailClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 61)
)
apSysMgmtAdminAuditPushFailClearTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysAddressType"),
        ("APSYSMGMT-MIB", "apSysAddress"))
)
if mibBuilder.loadTexts:
    apSysMgmtAdminAuditPushFailClearTrap.setStatus(
        "current"
    )

apSysMgmtAdminWriteFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 62)
)
apSysMgmtAdminWriteFailTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysAdminWriteErrorCode"),
        ("APSYSMGMT-MIB", "apSysAdminFileName"))
)
if mibBuilder.loadTexts:
    apSysMgmtAdminWriteFailTrap.setStatus(
        "current"
    )

apSysMgmtAdminWriteFailClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 63)
)
if mibBuilder.loadTexts:
    apSysMgmtAdminWriteFailClearTrap.setStatus(
        "current"
    )

apSysMgmtAdminAuthLockoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 64)
)
apSysMgmtAdminAuthLockoutTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtAuthFailProto")
)
if mibBuilder.loadTexts:
    apSysMgmtAdminAuthLockoutTrap.setStatus(
        "current"
    )

apSysMgmtLPLookupExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 65)
)
if mibBuilder.loadTexts:
    apSysMgmtLPLookupExceededTrap.setStatus(
        "current"
    )

apSysMgmtPhyUtilThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 66)
)
apSysMgmtPhyUtilThresholdTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("APSYSMGMT-MIB", "apSysMgmtPhyUtilCurrent"),
        ("APSYSMGMT-MIB", "apSysMgmtPhyUtilMinorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtPhyUtilMajorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtPhyUtilCriticalThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtPhyRejectOverUtil"))
)
if mibBuilder.loadTexts:
    apSysMgmtPhyUtilThresholdTrap.setStatus(
        "current"
    )

apSysMgmtPhyUtilThresholdClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 67)
)
apSysMgmtPhyUtilThresholdClearTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("APSYSMGMT-MIB", "apSysMgmtPhyUtilCurrent"),
        ("APSYSMGMT-MIB", "apSysMgmtPhyUtilMinorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtPhyUtilMajorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtPhyUtilCriticalThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtPhyRejectOverUtil"))
)
if mibBuilder.loadTexts:
    apSysMgmtPhyUtilThresholdClearTrap.setStatus(
        "current"
    )

apSysMgmtSpaceAvailThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 68)
)
apSysMgmtSpaceAvailThresholdTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtSpaceAvailCurrent"),
        ("APSYSMGMT-MIB", "apSysMgmtSpaceAvailMinorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtSpaceAvailMajorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtSpaceAvailCriticalThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtPartitionPath"))
)
if mibBuilder.loadTexts:
    apSysMgmtSpaceAvailThresholdTrap.setStatus(
        "current"
    )

apSysMgmtSpaceAvailThresholdClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 69)
)
apSysMgmtSpaceAvailThresholdClearTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtSpaceAvailCurrent"),
        ("APSYSMGMT-MIB", "apSysMgmtSpaceAvailMinorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtSpaceAvailMajorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtSpaceAvailCriticalThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtPartitionPath"))
)
if mibBuilder.loadTexts:
    apSysMgmtSpaceAvailThresholdClearTrap.setStatus(
        "current"
    )

apSysMgmtCdrFileDeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 70)
)
apSysMgmtCdrFileDeleteTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysAdminFileName")
)
if mibBuilder.loadTexts:
    apSysMgmtCdrFileDeleteTrap.setStatus(
        "current"
    )

apSysMgmtSataAccessErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 71)
)
if mibBuilder.loadTexts:
    apSysMgmtSataAccessErrorTrap.setStatus(
        "current"
    )

apSysMgmtTcaTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 72)
)
apSysMgmtTcaTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtTcaOid"),
        ("APSYSMGMT-MIB", "apSysMgmtTcaCurrent"),
        ("APSYSMGMT-MIB", "apSysMgmtTcaMinorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtTcaMajorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtTcaCriticalThreshold"))
)
if mibBuilder.loadTexts:
    apSysMgmtTcaTrap.setStatus(
        "current"
    )

apSysMgmtTcaClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 73)
)
apSysMgmtTcaClearTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtTcaOid"),
        ("APSYSMGMT-MIB", "apSysMgmtTcaCurrent"),
        ("APSYSMGMT-MIB", "apSysMgmtTcaMinorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtTcaMajorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtTcaCriticalThreshold"))
)
if mibBuilder.loadTexts:
    apSysMgmtTcaClearTrap.setStatus(
        "current"
    )

apSysMgmtExtPolicyServerConnDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 74)
)
apSysMgmtExtPolicyServerConnDownTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysEPSName"),
        ("APSYSMGMT-MIB", "apSysEPSFqdn"),
        ("APSYSMGMT-MIB", "apSysEPSAddress"),
        ("APSYSMGMT-MIB", "apSysEPSRealm"),
        ("APSYSMGMT-MIB", "apSysEPSOperationType"))
)
if mibBuilder.loadTexts:
    apSysMgmtExtPolicyServerConnDownTrap.setStatus(
        "current"
    )

apSysMgmtExtPolicyServerConnEstTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 75)
)
apSysMgmtExtPolicyServerConnEstTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysEPSName"),
        ("APSYSMGMT-MIB", "apSysEPSFqdn"),
        ("APSYSMGMT-MIB", "apSysEPSAddress"),
        ("APSYSMGMT-MIB", "apSysEPSRealm"),
        ("APSYSMGMT-MIB", "apSysEPSOperationType"))
)
if mibBuilder.loadTexts:
    apSysMgmtExtPolicyServerConnEstTrap.setStatus(
        "current"
    )

apSysMgmtDatabaseRegCacheCapTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 76)
)
apSysMgmtDatabaseRegCacheCapTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysSipStatsActiveDatabaseContacts"),
        ("APSYSMGMT-MIB", "apSysMgmtDatabaseContactMinorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtDatabaseContactMajorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtDatabaseContactCriticalThreshold"),
        ("APLICENSE-MIB", "apLicenseDatabaseRegCap"))
)
if mibBuilder.loadTexts:
    apSysMgmtDatabaseRegCacheCapTrap.setStatus(
        "current"
    )

apSysMgmtDatabaseRegCacheCapClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 77)
)
apSysMgmtDatabaseRegCacheCapClearTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysSipStatsActiveDatabaseContacts"),
        ("APSYSMGMT-MIB", "apSysMgmtDatabaseContactMinorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtDatabaseContactMajorThreshold"),
        ("APSYSMGMT-MIB", "apSysMgmtDatabaseContactCriticalThreshold"),
        ("APLICENSE-MIB", "apLicenseDatabaseRegCap"))
)
if mibBuilder.loadTexts:
    apSysMgmtDatabaseRegCacheCapClearTrap.setStatus(
        "current"
    )

apSysMgmtTacacsDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 78)
)
apSysMgmtTacacsDownTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtTacacsDown")
)
if mibBuilder.loadTexts:
    apSysMgmtTacacsDownTrap.setStatus(
        "current"
    )

apSysMgmtTacacsDownClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 79)
)
if mibBuilder.loadTexts:
    apSysMgmtTacacsDownClearTrap.setStatus(
        "current"
    )

apSysMgmtOCSRDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 80)
)
apSysMgmtOCSRDownTrap.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtOCSRDown")
)
if mibBuilder.loadTexts:
    apSysMgmtOCSRDownTrap.setStatus(
        "current"
    )

apSysMgmtOCSRDownClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 81)
)
if mibBuilder.loadTexts:
    apSysMgmtOCSRDownClearTrap.setStatus(
        "current"
    )

apSysMgmtSipInterfaceRegCacheThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 82)
)
apSysMgmtSipInterfaceRegCacheThresholdTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtSipInterfaceRealmName"),
        ("APSYSMGMT-MIB", "apSigRealmStatsActiveLocalContacts"),
        ("APSYSMGMT-MIB", "apSysMgmtSipInterfaceRegCacheLimit"))
)
if mibBuilder.loadTexts:
    apSysMgmtSipInterfaceRegCacheThresholdTrap.setStatus(
        "current"
    )

apSysMgmtSipInterfaceRegCacheThresholdClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 83)
)
apSysMgmtSipInterfaceRegCacheThresholdClearTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtSipInterfaceRealmName"),
        ("APSYSMGMT-MIB", "apSigRealmStatsActiveLocalContacts"),
        ("APSYSMGMT-MIB", "apSysMgmtSipInterfaceRegCacheLimit"))
)
if mibBuilder.loadTexts:
    apSysMgmtSipInterfaceRegCacheThresholdClearTrap.setStatus(
        "current"
    )

apSysMgmtH248PortMapUsageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 84)
)
apSysMgmtH248PortMapUsageTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtH248MgcName"),
        ("APSYSMGMT-MIB", "apSysMgmtH248Realm"),
        ("APSYSMGMT-MIB", "apSysMgmtH248PortMapUsage"))
)
if mibBuilder.loadTexts:
    apSysMgmtH248PortMapUsageTrap.setStatus(
        "current"
    )

apSysMgmtH248PortMapUsageClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 6, 0, 85)
)
apSysMgmtH248PortMapUsageClearTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtH248MgcName"),
        ("APSYSMGMT-MIB", "apSysMgmtH248Realm"))
)
if mibBuilder.loadTexts:
    apSysMgmtH248PortMapUsageClearTrap.setStatus(
        "current"
    )

apSysMgmtDOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 8, 0, 1)
)
apSysMgmtDOSTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtDOSIpAddress"),
        ("APSYSMGMT-MIB", "apSysMgmtDOSRealmID"))
)
if mibBuilder.loadTexts:
    apSysMgmtDOSTrap.setStatus(
        "obsolete"
    )

apSysMgmtExpDOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 8, 0, 2)
)
apSysMgmtExpDOSTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtDOSIpAddress"),
        ("APSYSMGMT-MIB", "apSysMgmtDOSRealmID"),
        ("APSYSMGMT-MIB", "apSysMgmtDOSFromUri"))
)
if mibBuilder.loadTexts:
    apSysMgmtExpDOSTrap.setStatus(
        "deprecated"
    )

apSysMgmtInetAddrDOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 8, 0, 3)
)
apSysMgmtInetAddrDOSTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtDOSInetAddressType"),
        ("APSYSMGMT-MIB", "apSysMgmtDOSInetAddress"),
        ("APSYSMGMT-MIB", "apSysMgmtDOSRealmID"),
        ("APSYSMGMT-MIB", "apSysMgmtDOSFromUri"))
)
if mibBuilder.loadTexts:
    apSysMgmtInetAddrDOSTrap.setStatus(
        "current"
    )

apSysMgmtInetAddrWithReasonDOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 8, 0, 4)
)
apSysMgmtInetAddrWithReasonDOSTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtDOSInetAddressType"),
        ("APSYSMGMT-MIB", "apSysMgmtDOSInetAddress"),
        ("APSYSMGMT-MIB", "apSysMgmtDOSRealmID"),
        ("APSYSMGMT-MIB", "apSysMgmtDOSFromUri"),
        ("APSYSMGMT-MIB", "apSysMgmtDOSReason"))
)
if mibBuilder.loadTexts:
    apSysMgmtInetAddrWithReasonDOSTrap.setStatus(
        "current"
    )

apSysMgmtInetAddrTrustedToUntrustedDOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 8, 0, 5)
)
apSysMgmtInetAddrTrustedToUntrustedDOSTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtDOSInetAddressType"),
        ("APSYSMGMT-MIB", "apSysMgmtDOSInetAddress"),
        ("APSYSMGMT-MIB", "apSysMgmtDOSRealmID"),
        ("APSYSMGMT-MIB", "apSysMgmtDOSFromUri"),
        ("APSYSMGMT-MIB", "apSysMgmtDOSReason"))
)
if mibBuilder.loadTexts:
    apSysMgmtInetAddrTrustedToUntrustedDOSTrap.setStatus(
        "current"
    )

apSysMgmtSipRejectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 10, 0, 1)
)
apSysMgmtSipRejectionTrap.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtSipRejFromUriUser"),
        ("APSYSMGMT-MIB", "apSysMgmtSipRejToUriUser"),
        ("APSYSMGMT-MIB", "apSysMgmtSipRejRequestUri"),
        ("APSYSMGMT-MIB", "apSysMgmtSipRejContactUri"),
        ("APSYSMGMT-MIB", "apSysMgmtSipRejIpAddress"),
        ("APSYSMGMT-MIB", "apSysMgmtSipRejMsgType"),
        ("APSYSMGMT-MIB", "apSysMgmtSipRejMethod"),
        ("APSYSMGMT-MIB", "apSysMgmtSipRejReason"))
)
if mibBuilder.loadTexts:
    apSysMgmtSipRejectionTrap.setStatus(
        "current"
    )


# Notifications groups

apSysMgmtNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 1)
)
apSysMgmtNotificationsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtGroupTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtGroupClearTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtPowerTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtTempTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtFanTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtTaskSuspendTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtRedundancyTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtMediaPortsTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtMediaBandwidthTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtMediaOutOfMemory"),
        ("APSYSMGMT-MIB", "apSysMgmtMediaUnknownRealm"),
        ("APSYSMGMT-MIB", "apSysMgmtGatewayUnreachableTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtRadiusDownTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtCfgSaveFailTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtHardwareErrorTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtSAStatusChangeTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtAuthenticationFailedTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtSystemStateTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtMediaPortsClearTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtMediaBandwidthClearTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtMediaOutOfMemoryClear"),
        ("APSYSMGMT-MIB", "apSysMgmtGatewayUnreachableClearTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtRadiusDownClearTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtTaskDeleteTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtCdrFileDeleteTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtSataAccessErrorTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtTcaTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtTcaClearTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtTacacsDownTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtTacacsDownClearTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtOCSRDownTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtOCSRDownClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtH323NotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 2)
)
apSysMgmtH323NotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtH323InitFailTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtH323NotificationsGroup.setStatus(
        "current"
    )

apSysMgmtNotificationsGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 3)
)
apSysMgmtNotificationsGroup2.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtSingleUnitRedundancyTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtNotificationsGroup2.setStatus(
        "current"
    )

apSysMgmtNotificationsGroup3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 4)
)
apSysMgmtNotificationsGroup3.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtAlgdCPULoadTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtAlgdCPULoadClearTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtInterfaceStatusChangeTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtENUMStatusChangeTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtRealmStatusChangeTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtNotificationsGroup3.setStatus(
        "current"
    )

apSysMgmtHDRNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 5)
)
apSysMgmtHDRNotificationsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtPushServerUnreachableTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtPushServerUnreachableClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtHDRNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtObsoleteNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 6)
)
apSysMgmtObsoleteNotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtDOSTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtObsoleteNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtRegNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 7)
)
apSysMgmtRegNotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtSurrogateRegFailed")
)
if mibBuilder.loadTexts:
    apSysMgmtRegNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtNTPNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 8)
)
apSysMgmtNTPNotificationsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtNTPServerUnreachableTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtNTPServerUnreachableClearTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtNTPServiceDownTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtNTPServiceDownClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtNTPNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtMediaNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 9)
)
apSysMgmtMediaNotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtMediaSupervisionTimerExpTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtMediaNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtH248NotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 10)
)
apSysMgmtH248NotificationsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmntH248AssociationLostTrap"),
        ("APSYSMGMT-MIB", "apSysMgmntH248AssociationLostClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtH248NotificationsGroup.setStatus(
        "current"
    )

apSysMgmtRFactorNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 11)
)
apSysMgmtRFactorNotificationsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtRFactorBelowThresholdTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtRFactorBelowThresholdClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtRFactorNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtRealmExceedNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 12)
)
apSysMgmtRealmExceedNotificationsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtRealmMinutesExceedTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtRealmMinutesExceedClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtRealmExceedNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtDOSNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 13)
)
apSysMgmtDOSNotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtExpDOSTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtDOSNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtClockSkewNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 14)
)
apSysMgmtClockSkewNotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtNTPClockSkewTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtClockSkewNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtLDAPServerStatusNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 15)
)
apSysMgmtLDAPServerStatusNotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtLDAPStatusChangeTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtLDAPServerStatusNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtSipRejectNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 16)
)
apSysMgmtSipRejectNotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtSipRejectionTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtSipRejectNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtCollectorPushSuccessNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 17)
)
apSysMgmtCollectorPushSuccessNotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtCollectorPushSuccessTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtCollectorPushSuccessNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtRegCacheLimitNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 18)
)
apSysMgmtRegCacheLimitNotificationsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtRegCacheThresholdTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtRegCacheThresholdClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtRegCacheLimitNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtShortSessionNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 19)
)
apSysMgmtShortSessionNotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtShortSessionExceedTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtShortSessionNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtMonitorNetworkGatewaySynchronizedNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 20)
)
apSysMgmtMonitorNetworkGatewaySynchronizedNotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtGatewaySynchronizedTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtMonitorNetworkGatewaySynchronizedNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtCallRecordingNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 21)
)
apSysMgmtCallRecordingNotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtCallRecordingStateChangeTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtCallRecordingNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtSipExtNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 22)
)
apSysMgmtSipExtNotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtInterfaceStatusChangeTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtSipExtNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtIcmpFailureNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 23)
)
apSysMgmtIcmpFailureNotificationsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtRealmIcmpFailureTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtRealmIcmpFailureClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtIcmpFailureNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtCDRPushReceiverNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 24)
)
apSysMgmtCDRPushReceiverNotificationsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtCDRPushReceiverFailureTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtCDRPushReceiverFailureClearTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtCDRPushAllReceiversFailureTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtCDRPushAllReceiversFailureClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtCDRPushReceiverNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtInetAddrDOSNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 25)
)
apSysMgmtInetAddrDOSNotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtInetAddrDOSTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtInetAddrDOSNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtRejectedMessagesNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 26)
)
apSysMgmtRejectedMessagesNotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtRejectedMesagesThresholdExeededTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtRejectedMessagesNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtInetAddrWithReasonDOSNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 27)
)
apSysMgmtInetAddrWithReasonDOSNotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtInetAddrWithReasonDOSTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtInetAddrWithReasonDOSNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtAdminGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 28)
)
apSysMgmtAdminGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtAdminAuthLockoutTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtAdminAuditLogFullTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtAdminAuditLogFullClearTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtAdminAuditPushFailTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtAdminAuditPushFailClearTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtAdminWriteFailTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtAdminWriteFailClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtAdminGroup.setStatus(
        "current"
    )

apSysMgmtLPGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 29)
)
apSysMgmtLPGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtLPLookupExceededTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtLPGroup.setStatus(
        "current"
    )

apSysMgmtPhyUtilNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 30)
)
apSysMgmtPhyUtilNotificationsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtPhyUtilThresholdTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtPhyUtilThresholdClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtPhyUtilNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtStorageSpaceNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 31)
)
apSysMgmtStorageSpaceNotificationsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtSpaceAvailThresholdTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtSpaceAvailThresholdClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtStorageSpaceNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtTcaGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 32)
)
apSysMgmtTcaGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtTcaClearTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtTcaTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtTcaGroup.setStatus(
        "current"
    )

apSysMgmtDatabaseRegNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 33)
)
apSysMgmtDatabaseRegNotificationsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtDatabaseRegCacheCapTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtDatabaseRegCacheCapClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtDatabaseRegNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtTacacsNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 34)
)
apSysMgmtTacacsNotificationsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtTacacsDownTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtTacacsDownClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtTacacsNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtOCSRNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 35)
)
apSysMgmtOCSRNotificationsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtOCSRDownTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtOCSRDownClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtOCSRNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtSipInterfaceRegCacheLimitNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 36)
)
apSysMgmtSipInterfaceRegCacheLimitNotificationsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtSipInterfaceRegCacheThresholdTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtSipInterfaceRegCacheThresholdClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtSipInterfaceRegCacheLimitNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtH248PortMapUsageNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 37)
)
apSysMgmtH248PortMapUsageNotificationsGroup.setObjects(
      *(("APSYSMGMT-MIB", "apSysMgmtH248PortMapUsageTrap"),
        ("APSYSMGMT-MIB", "apSysMgmtH248PortMapUsageClearTrap"))
)
if mibBuilder.loadTexts:
    apSysMgmtH248PortMapUsageNotificationsGroup.setStatus(
        "current"
    )

apSysMgmtInetAddrDOSTrustedtoUntrustedNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 2, 4, 3, 38)
)
apSysMgmtInetAddrDOSTrustedtoUntrustedNotificationsGroup.setObjects(
    ("APSYSMGMT-MIB", "apSysMgmtInetAddrTrustedToUntrustedDOSTrap")
)
if mibBuilder.loadTexts:
    apSysMgmtInetAddrDOSTrustedtoUntrustedNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APSYSMGMT-MIB",
    **{"SysMgmtPercentage": SysMgmtPercentage,
       "ApSessionAgentStatusOptions": ApSessionAgentStatusOptions,
       "ApSessionAgentType": ApSessionAgentType,
       "ApNetMgmtCtrlType": ApNetMgmtCtrlType,
       "ApSipInterfaceStatusOptions": ApSipInterfaceStatusOptions,
       "ApSigRealmStatusOptions": ApSigRealmStatusOptions,
       "ApNetMgmtCtrlState": ApNetMgmtCtrlState,
       "apSystemManagementModule": apSystemManagementModule,
       "apSysMgmtMIBObjects": apSysMgmtMIBObjects,
       "apSysMgmtMIBGeneralObjects": apSysMgmtMIBGeneralObjects,
       "apSysCPUUtil": apSysCPUUtil,
       "apSysMemoryUtil": apSysMemoryUtil,
       "apSysHealthScore": apSysHealthScore,
       "apSysRedundancy": apSysRedundancy,
       "apSysGlobalConSess": apSysGlobalConSess,
       "apSysGlobalCPS": apSysGlobalCPS,
       "apSysNATCapacity": apSysNATCapacity,
       "apSysARPCapacity": apSysARPCapacity,
       "apSysState": apSysState,
       "apSysLicenseCapacity": apSysLicenseCapacity,
       "apSysSipStatsActiveLocalContacts": apSysSipStatsActiveLocalContacts,
       "apSysMgcpGWEndpoints": apSysMgcpGWEndpoints,
       "apSysH323Registration": apSysH323Registration,
       "apSysRegCacheLimit": apSysRegCacheLimit,
       "apSysShortSessionThreshold": apSysShortSessionThreshold,
       "apSysApplicationCPULoadRate": apSysApplicationCPULoadRate,
       "apSysRegistrationCapacity": apSysRegistrationCapacity,
       "apSysRejectedMessages": apSysRejectedMessages,
       "apSysSipEndptDemTrustToUntrust": apSysSipEndptDemTrustToUntrust,
       "apSysSipEndptDemUntrustToDeny": apSysSipEndptDemUntrustToDeny,
       "apSysMgcpEndptDemTrustToUntrust": apSysMgcpEndptDemTrustToUntrust,
       "apSysMgcpEndptDemUntrustToDeny": apSysMgcpEndptDemUntrustToDeny,
       "apSysStorageSpaceTable": apSysStorageSpaceTable,
       "apSysStorageSpaceEntry": apSysStorageSpaceEntry,
       "apSysVolumeIndex": apSysVolumeIndex,
       "apSysVolumeName": apSysVolumeName,
       "apSysVolumeTotalSpace": apSysVolumeTotalSpace,
       "apSysVolumeAvailSpace": apSysVolumeAvailSpace,
       "apSysSipStatsActiveDatabaseContacts": apSysSipStatsActiveDatabaseContacts,
       "apSysSipTotalCallsRejected": apSysSipTotalCallsRejected,
       "apSysCurrentEndptsDenied": apSysCurrentEndptsDenied,
       "apSysSipStatsActiveSubscriptions": apSysSipStatsActiveSubscriptions,
       "apSysSipStatsPerMaxSubscriptions": apSysSipStatsPerMaxSubscriptions,
       "apSysSipStatsMaximumActiveSubscriptions": apSysSipStatsMaximumActiveSubscriptions,
       "apSysSipStatsTotalSubscriptions": apSysSipStatsTotalSubscriptions,
       "apSysMgmtH248MgcName": apSysMgmtH248MgcName,
       "apSysMgmtH248Realm": apSysMgmtH248Realm,
       "apSysMgmtH248PortMapUsage": apSysMgmtH248PortMapUsage,
       "apSysXCodeCapacity": apSysXCodeCapacity,
       "apSysXCodeAMRCapacity": apSysXCodeAMRCapacity,
       "apSysXCodeAMRWBCapacity": apSysXCodeAMRWBCapacity,
       "apSysETCCoreUtilTable": apSysETCCoreUtilTable,
       "apSysETCCoreUtilEntry": apSysETCCoreUtilEntry,
       "apSysETCIndex": apSysETCIndex,
       "apSysETCCoreIndex": apSysETCCoreIndex,
       "apSysETCCoreCPUUtil": apSysETCCoreCPUUtil,
       "apSysETCMemoryPoolUtilTable": apSysETCMemoryPoolUtilTable,
       "apSysETCMemoryPoolUtilEntry": apSysETCMemoryPoolUtilEntry,
       "apSysETCMemoryPoolIndex": apSysETCMemoryPoolIndex,
       "apSysETCMemoryPoolMemUtil": apSysETCMemoryPoolMemUtil,
       "apSysMgmtMIBSessionObjects": apSysMgmtMIBSessionObjects,
       "apCombinedSessionAgentStatsTable": apCombinedSessionAgentStatsTable,
       "apCombinedSessionAgentStatsEntry": apCombinedSessionAgentStatsEntry,
       "apCombinedStatsSessionAgentIndex": apCombinedStatsSessionAgentIndex,
       "apCombinedStatsSessionAgentHostname": apCombinedStatsSessionAgentHostname,
       "apCombinedStatsSessionAgentType": apCombinedStatsSessionAgentType,
       "apCombinedStatsCurrentActiveSessionsInbound": apCombinedStatsCurrentActiveSessionsInbound,
       "apCombinedStatsCurrentSessionRateInbound": apCombinedStatsCurrentSessionRateInbound,
       "apCombinedStatsCurrentActiveSessionsOutbound": apCombinedStatsCurrentActiveSessionsOutbound,
       "apCombinedStatsCurrentSessionRateOutbound": apCombinedStatsCurrentSessionRateOutbound,
       "apCombinedStatsTotalSessionsInbound": apCombinedStatsTotalSessionsInbound,
       "apCombinedStatsTotalSessionsNotAdmittedInbound": apCombinedStatsTotalSessionsNotAdmittedInbound,
       "apCombinedStatsPeriodHighInbound": apCombinedStatsPeriodHighInbound,
       "apCombinedStatsAverageRateInbound": apCombinedStatsAverageRateInbound,
       "apCombinedStatsTotalSessionsOutbound": apCombinedStatsTotalSessionsOutbound,
       "apCombinedStatsTotalSessionsNotAdmittedOutbound": apCombinedStatsTotalSessionsNotAdmittedOutbound,
       "apCombinedStatsPeriodHighOutbound": apCombinedStatsPeriodHighOutbound,
       "apCombinedStatsAverageRateOutbound": apCombinedStatsAverageRateOutbound,
       "apCombinedStatsMaxBurstRate": apCombinedStatsMaxBurstRate,
       "apCombinedStatsPeriodSeizures": apCombinedStatsPeriodSeizures,
       "apCombinedStatsPeriodAnswers": apCombinedStatsPeriodAnswers,
       "apCombinedStatsPeriodASR": apCombinedStatsPeriodASR,
       "apCombinedStatsAverageLatency": apCombinedStatsAverageLatency,
       "apCombinedStatsMaxLatency": apCombinedStatsMaxLatency,
       "apCombinedStatsSessionAgentStatus": apCombinedStatsSessionAgentStatus,
       "apSipSessionAgentStatsTable": apSipSessionAgentStatsTable,
       "apSipSessionAgentStatsEntry": apSipSessionAgentStatsEntry,
       "apSipSAStatsSessionAgentIndex": apSipSAStatsSessionAgentIndex,
       "apSipSAStatsSessionAgentHostname": apSipSAStatsSessionAgentHostname,
       "apSipSAStatsSessionAgentType": apSipSAStatsSessionAgentType,
       "apSipSAStatsCurrentActiveSessionsInbound": apSipSAStatsCurrentActiveSessionsInbound,
       "apSipSAStatsCurrentSessionRateInbound": apSipSAStatsCurrentSessionRateInbound,
       "apSipSAStatsCurrentActiveSessionsOutbound": apSipSAStatsCurrentActiveSessionsOutbound,
       "apSipSAStatsCurrentSessionRateOutbound": apSipSAStatsCurrentSessionRateOutbound,
       "apSipSAStatsTotalSessionsInbound": apSipSAStatsTotalSessionsInbound,
       "apSipSAStatsTotalSessionsNotAdmittedInbound": apSipSAStatsTotalSessionsNotAdmittedInbound,
       "apSipSAStatsPeriodHighInbound": apSipSAStatsPeriodHighInbound,
       "apSipSAStatsAverageRateInbound": apSipSAStatsAverageRateInbound,
       "apSipSAStatsTotalSessionsOutbound": apSipSAStatsTotalSessionsOutbound,
       "apSipSAStatsTotalSessionsNotAdmittedOutbound": apSipSAStatsTotalSessionsNotAdmittedOutbound,
       "apSipSAStatsPeriodHighOutbound": apSipSAStatsPeriodHighOutbound,
       "apSipSAStatsAverageRateOutbound": apSipSAStatsAverageRateOutbound,
       "apSipSAStatsMaxBurstRate": apSipSAStatsMaxBurstRate,
       "apSipSAStatsPeriodSeizures": apSipSAStatsPeriodSeizures,
       "apSipSAStatsPeriodAnswers": apSipSAStatsPeriodAnswers,
       "apSipSAStatsPeriodASR": apSipSAStatsPeriodASR,
       "apSipSAStatsAverageLatency": apSipSAStatsAverageLatency,
       "apSipSAStatsMaxLatency": apSipSAStatsMaxLatency,
       "apSipSAStatsSessionAgentStatus": apSipSAStatsSessionAgentStatus,
       "apH323SessionAgentStatsTable": apH323SessionAgentStatsTable,
       "apH323SessionAgentStatsEntry": apH323SessionAgentStatsEntry,
       "apH323SAStatsSessionAgentIndex": apH323SAStatsSessionAgentIndex,
       "apH323SAStatsSessionAgentHostname": apH323SAStatsSessionAgentHostname,
       "apH323SAStatsSessionAgentType": apH323SAStatsSessionAgentType,
       "apH323SAStatsCurrentActiveSessionsInbound": apH323SAStatsCurrentActiveSessionsInbound,
       "apH323SAStatsCurrentSessionRateInbound": apH323SAStatsCurrentSessionRateInbound,
       "apH323SAStatsCurrentActiveSessionsOutbound": apH323SAStatsCurrentActiveSessionsOutbound,
       "apH323SAStatsCurrentSessionRateOutbound": apH323SAStatsCurrentSessionRateOutbound,
       "apH323SAStatsTotalSessionsInbound": apH323SAStatsTotalSessionsInbound,
       "apH323SAStatsTotalSessionsNotAdmittedInbound": apH323SAStatsTotalSessionsNotAdmittedInbound,
       "apH323SAStatsPeriodHighInbound": apH323SAStatsPeriodHighInbound,
       "apH323SAStatsAverageRateInbound": apH323SAStatsAverageRateInbound,
       "apH323SAStatsTotalSessionsOutbound": apH323SAStatsTotalSessionsOutbound,
       "apH323SAStatsTotalSessionsNotAdmittedOutbound": apH323SAStatsTotalSessionsNotAdmittedOutbound,
       "apH323SAStatsPeriodHighOutbound": apH323SAStatsPeriodHighOutbound,
       "apH323SAStatsAverageRateOutbound": apH323SAStatsAverageRateOutbound,
       "apH323SAStatsMaxBurstRate": apH323SAStatsMaxBurstRate,
       "apH323SAStatsPeriodSeizures": apH323SAStatsPeriodSeizures,
       "apH323SAStatsPeriodAnswers": apH323SAStatsPeriodAnswers,
       "apH323SAStatsPeriodASR": apH323SAStatsPeriodASR,
       "apH323SAStatsAverageLatency": apH323SAStatsAverageLatency,
       "apH323SAStatsMaxLatency": apH323SAStatsMaxLatency,
       "apH323SAStatsSessionAgentStatus": apH323SAStatsSessionAgentStatus,
       "apSigRealmStatsTable": apSigRealmStatsTable,
       "apSigRealmStatsEntry": apSigRealmStatsEntry,
       "apSigRealmStatsRealmIndex": apSigRealmStatsRealmIndex,
       "apSigRealmStatsRealmName": apSigRealmStatsRealmName,
       "apSigRealmStatsCurrentActiveSessionsInbound": apSigRealmStatsCurrentActiveSessionsInbound,
       "apSigRealmStatsCurrentSessionRateInbound": apSigRealmStatsCurrentSessionRateInbound,
       "apSigRealmStatsCurrentActiveSessionsOutbound": apSigRealmStatsCurrentActiveSessionsOutbound,
       "apSigRealmStatsCurrentSessionRateOutbound": apSigRealmStatsCurrentSessionRateOutbound,
       "apSigRealmStatsTotalSessionsInbound": apSigRealmStatsTotalSessionsInbound,
       "apSigRealmStatsTotalSessionsNotAdmittedInbound": apSigRealmStatsTotalSessionsNotAdmittedInbound,
       "apSigRealmStatsPeriodHighInbound": apSigRealmStatsPeriodHighInbound,
       "apSigRealmStatsAverageRateInbound": apSigRealmStatsAverageRateInbound,
       "apSigRealmStatsTotalSessionsOutbound": apSigRealmStatsTotalSessionsOutbound,
       "apSigRealmStatsTotalSessionsNotAdmittedOutbound": apSigRealmStatsTotalSessionsNotAdmittedOutbound,
       "apSigRealmStatsPeriodHighOutbound": apSigRealmStatsPeriodHighOutbound,
       "apSigRealmStatsAverageRateOutbound": apSigRealmStatsAverageRateOutbound,
       "apSigRealmStatsMaxBurstRate": apSigRealmStatsMaxBurstRate,
       "apSigRealmStatsPeriodSeizures": apSigRealmStatsPeriodSeizures,
       "apSigRealmStatsPeriodAnswers": apSigRealmStatsPeriodAnswers,
       "apSigRealmStatsPeriodASR": apSigRealmStatsPeriodASR,
       "apSigRealmStatsAverageLatency": apSigRealmStatsAverageLatency,
       "apSigRealmStatsMaxLatency": apSigRealmStatsMaxLatency,
       "apSigRealmStatsMinutesLeft": apSigRealmStatsMinutesLeft,
       "apSigRealmStatsMinutesReject": apSigRealmStatsMinutesReject,
       "apSigRealmStatsShortSessions": apSigRealmStatsShortSessions,
       "apSigRealmStatsAverageQoSRFactor": apSigRealmStatsAverageQoSRFactor,
       "apSigRealmStatsMaximumQoSRFactor": apSigRealmStatsMaximumQoSRFactor,
       "apSigRealmStatsCurrentMajorRFactorExceeded": apSigRealmStatsCurrentMajorRFactorExceeded,
       "apSigRealmStatsTotalMajorRFactorExceeded": apSigRealmStatsTotalMajorRFactorExceeded,
       "apSigRealmStatsCurrentCriticalRFactorExceeded": apSigRealmStatsCurrentCriticalRFactorExceeded,
       "apSigRealmStatsTotalCriticalRFactorExceeded": apSigRealmStatsTotalCriticalRFactorExceeded,
       "apSigRealmStatsRealmStatus": apSigRealmStatsRealmStatus,
       "apSigRealmStatsActiveLocalContacts": apSigRealmStatsActiveLocalContacts,
       "apSigRealmStatsActiveSubscriptions": apSigRealmStatsActiveSubscriptions,
       "apSigRealmStatsPerMaxSubscriptions": apSigRealmStatsPerMaxSubscriptions,
       "apSigRealmStatsMaximumActiveSubscriptions": apSigRealmStatsMaximumActiveSubscriptions,
       "apSigRealmStatsTotalSubscriptions": apSigRealmStatsTotalSubscriptions,
       "apSysMgmtMIBNetMgmtCtrlObjects": apSysMgmtMIBNetMgmtCtrlObjects,
       "apNetMgmtCtrlStatsTable": apNetMgmtCtrlStatsTable,
       "apNetMgmtCtrlStatsEntry": apNetMgmtCtrlStatsEntry,
       "apNetMgmtCtrlStatsName": apNetMgmtCtrlStatsName,
       "apNetMgmtCtrlStatsType": apNetMgmtCtrlStatsType,
       "apNetMgmtCtrlStatsIncomingTotal": apNetMgmtCtrlStatsIncomingTotal,
       "apNetMgmtCtrlStatsRejectedTotal": apNetMgmtCtrlStatsRejectedTotal,
       "apNetMgmtCtrlStatsDivertedTotal": apNetMgmtCtrlStatsDivertedTotal,
       "apNetMgmtCtrlStatsIncomingCurrent": apNetMgmtCtrlStatsIncomingCurrent,
       "apNetMgmtCtrlStatsRejectedCurrent": apNetMgmtCtrlStatsRejectedCurrent,
       "apNetMgmtCtrlStatsDivertedCurrent": apNetMgmtCtrlStatsDivertedCurrent,
       "apNetMgmtCtrlStatsIncomingPeriodMax": apNetMgmtCtrlStatsIncomingPeriodMax,
       "apNetMgmtCtrlStatsRejectedPeriodMax": apNetMgmtCtrlStatsRejectedPeriodMax,
       "apNetMgmtCtrlStatsDivertedPeriodMax": apNetMgmtCtrlStatsDivertedPeriodMax,
       "apNetMgmtCtrlStatsState": apNetMgmtCtrlStatsState,
       "apSysMgmtMIBENUMServerStatusObjects": apSysMgmtMIBENUMServerStatusObjects,
       "apENUMServerStatusTable": apENUMServerStatusTable,
       "apENUMServerStatusEntry": apENUMServerStatusEntry,
       "apENUMConfigName": apENUMConfigName,
       "apENUMServerIpAddress": apENUMServerIpAddress,
       "apENUMServerStatus": apENUMServerStatus,
       "apSysMgmtMIBNSEPStatsObjects": apSysMgmtMIBNSEPStatsObjects,
       "apNSEPStatsCurrentActiveSessionsInbound": apNSEPStatsCurrentActiveSessionsInbound,
       "apNSEPStatsTotalSessionsInbound": apNSEPStatsTotalSessionsInbound,
       "apNSEPStatsPeriodHighInbound": apNSEPStatsPeriodHighInbound,
       "apNSEPStatsPeriod": apNSEPStatsPeriod,
       "apNSEPStatsRPHTable": apNSEPStatsRPHTable,
       "apNSEPStatsRPHEntry": apNSEPStatsRPHEntry,
       "apNSEPStatsRPHValue": apNSEPStatsRPHValue,
       "apNSEPStatsRPHCurrentActiveSessionsInbound": apNSEPStatsRPHCurrentActiveSessionsInbound,
       "apNSEPStatsRPHTotalSessionsInbound": apNSEPStatsRPHTotalSessionsInbound,
       "apNSEPStatsRPHPeriodHighInbound": apNSEPStatsRPHPeriodHighInbound,
       "apNSEPStatsRPHTotalSessionsNotAdmittedInbound": apNSEPStatsRPHTotalSessionsNotAdmittedInbound,
       "apNSEPStatsRPHCurrentActiveSessionsOutbound": apNSEPStatsRPHCurrentActiveSessionsOutbound,
       "apNSEPStatsRPHTotalSessionsOutbound": apNSEPStatsRPHTotalSessionsOutbound,
       "apNSEPStatsRPHPeriodHighOutbound": apNSEPStatsRPHPeriodHighOutbound,
       "apNSEPStatsRPHTotalSessionsNotAdmittedOutbound": apNSEPStatsRPHTotalSessionsNotAdmittedOutbound,
       "apSysMgmtMIBLDAPServerStatusObjects": apSysMgmtMIBLDAPServerStatusObjects,
       "apLDAPServerStatusTable": apLDAPServerStatusTable,
       "apLDAPServerStatusEntry": apLDAPServerStatusEntry,
       "apLDAPConfigName": apLDAPConfigName,
       "apLDAPServerIpAddress": apLDAPServerIpAddress,
       "apLDAPServerStatus": apLDAPServerStatus,
       "apSysMgmtSystemTrapObjects": apSysMgmtSystemTrapObjects,
       "apSysMgmtTrapTable": apSysMgmtTrapTable,
       "apSysMgmtTrapTableEntry": apSysMgmtTrapTableEntry,
       "apTrapTableSystemTime": apTrapTableSystemTime,
       "apTrapTableInstanceIndex": apTrapTableInstanceIndex,
       "apTrapTableNumVariables": apTrapTableNumVariables,
       "apTrapTableSysUptime": apTrapTableSysUptime,
       "apTrapTableTrapId": apTrapTableTrapId,
       "apSysMgmtTrapInformationTable": apSysMgmtTrapInformationTable,
       "apSysMgmtTrapInformationTableEntry": apSysMgmtTrapInformationTableEntry,
       "apTrapInformationTableDataIndex": apTrapInformationTableDataIndex,
       "apTrapInformationTableDataType": apTrapInformationTableDataType,
       "apTrapInformationTableDataLength": apTrapInformationTableDataLength,
       "apTrapInformationTableDataOctets": apTrapInformationTableDataOctets,
       "apSysMgmtInterfaceObjects": apSysMgmtInterfaceObjects,
       "apSysMgmtPhyUtilTable": apSysMgmtPhyUtilTable,
       "apSysMgmtPhyUtilTableEntry": apSysMgmtPhyUtilTableEntry,
       "apPhyUtilTableRXUtil": apPhyUtilTableRXUtil,
       "apPhyUtilTableTXUtil": apPhyUtilTableTXUtil,
       "apSysMgmtNotificationObjects": apSysMgmtNotificationObjects,
       "apSysMgmtTrapType": apSysMgmtTrapType,
       "apSysMgmtTrapValue": apSysMgmtTrapValue,
       "apSysMgmtSlotID": apSysMgmtSlotID,
       "apSysMgmtSlotType": apSysMgmtSlotType,
       "apSysMgmtRedundancyState": apSysMgmtRedundancyState,
       "apSysMgmtSingleUnitRedundancyState": apSysMgmtSingleUnitRedundancyState,
       "apSysMgmtSipInterfaceActiveLocalContacts": apSysMgmtSipInterfaceActiveLocalContacts,
       "apSysMgmtSipInterfaceRegCacheLimit": apSysMgmtSipInterfaceRegCacheLimit,
       "apSystemManagementNotificationPrefix": apSystemManagementNotificationPrefix,
       "apSystemManagementNotifications": apSystemManagementNotifications,
       "apSysMgmtGroupTrap": apSysMgmtGroupTrap,
       "apSysMgmtGroupClearTrap": apSysMgmtGroupClearTrap,
       "apSysMgmtSingleUnitRedundancyTrap": apSysMgmtSingleUnitRedundancyTrap,
       "apSystemManagementConformance": apSystemManagementConformance,
       "apSystemManagementCompliances": apSystemManagementCompliances,
       "apSystemManagementGroups": apSystemManagementGroups,
       "apSysMgmtGeneralGroup": apSysMgmtGeneralGroup,
       "apSysMgmtCombinedGroup": apSysMgmtCombinedGroup,
       "apSysMgmtSipGroup": apSysMgmtSipGroup,
       "apSysMgmtH323Group": apSysMgmtH323Group,
       "apSysMgmtSigRealmGroup": apSysMgmtSigRealmGroup,
       "apSysMgmtCtrlStatsGroup": apSysMgmtCtrlStatsGroup,
       "apSysMgmtENUMServerStatusGroup": apSysMgmtENUMServerStatusGroup,
       "apSysMgmtNSEPStatsGroup": apSysMgmtNSEPStatsGroup,
       "apSysMgmtExtSigRealmStatsGroup": apSysMgmtExtSigRealmStatsGroup,
       "apSysMgmtLDAPServerStatusGroup": apSysMgmtLDAPServerStatusGroup,
       "apSysMgmtRegistrationGroup": apSysMgmtRegistrationGroup,
       "apSysMgmtRegCacheLimitGroup": apSysMgmtRegCacheLimitGroup,
       "apSysMgmtShortSessionGroup": apSysMgmtShortSessionGroup,
       "apSysMgmtTrapTableObjectGroup": apSysMgmtTrapTableObjectGroup,
       "apSysMgmtRealmStatsQoSGroup": apSysMgmtRealmStatsQoSGroup,
       "apSysMgmtApplicationCPUUsageGroup": apSysMgmtApplicationCPUUsageGroup,
       "apSysMgmtRegistrationCapacityGroup": apSysMgmtRegistrationCapacityGroup,
       "apSysMgmtRejectedMessagesGroup": apSysMgmtRejectedMessagesGroup,
       "apSysMgmtEndPtDemotionObjectGroup": apSysMgmtEndPtDemotionObjectGroup,
       "apSysMgmtCallRecordingGroup": apSysMgmtCallRecordingGroup,
       "apSysMgmtPhyUtilGroup": apSysMgmtPhyUtilGroup,
       "apSysMgmtStorageSpaceGroup": apSysMgmtStorageSpaceGroup,
       "apSysMgmtCtrlStatsGroup2": apSysMgmtCtrlStatsGroup2,
       "apSysMgmtDatabaseRegGroup": apSysMgmtDatabaseRegGroup,
       "apSysMgmtCallsRejectedGroup": apSysMgmtCallsRejectedGroup,
       "apSysMgmtRealmRegCacheSummaryGroup": apSysMgmtRealmRegCacheSummaryGroup,
       "apSysMgmtSubscriptionSummaryGroup": apSysMgmtSubscriptionSummaryGroup,
       "apSysMgmtETCUtilGroup": apSysMgmtETCUtilGroup,
       "apSystemManagementNotificationsGroups": apSystemManagementNotificationsGroups,
       "apSysMgmtNotificationsGroup": apSysMgmtNotificationsGroup,
       "apSysMgmtH323NotificationsGroup": apSysMgmtH323NotificationsGroup,
       "apSysMgmtNotificationsGroup2": apSysMgmtNotificationsGroup2,
       "apSysMgmtNotificationsGroup3": apSysMgmtNotificationsGroup3,
       "apSysMgmtHDRNotificationsGroup": apSysMgmtHDRNotificationsGroup,
       "apSysMgmtObsoleteNotificationsGroup": apSysMgmtObsoleteNotificationsGroup,
       "apSysMgmtRegNotificationsGroup": apSysMgmtRegNotificationsGroup,
       "apSysMgmtNTPNotificationsGroup": apSysMgmtNTPNotificationsGroup,
       "apSysMgmtMediaNotificationsGroup": apSysMgmtMediaNotificationsGroup,
       "apSysMgmtH248NotificationsGroup": apSysMgmtH248NotificationsGroup,
       "apSysMgmtRFactorNotificationsGroup": apSysMgmtRFactorNotificationsGroup,
       "apSysMgmtRealmExceedNotificationsGroup": apSysMgmtRealmExceedNotificationsGroup,
       "apSysMgmtDOSNotificationsGroup": apSysMgmtDOSNotificationsGroup,
       "apSysMgmtClockSkewNotificationsGroup": apSysMgmtClockSkewNotificationsGroup,
       "apSysMgmtLDAPServerStatusNotificationsGroup": apSysMgmtLDAPServerStatusNotificationsGroup,
       "apSysMgmtSipRejectNotificationsGroup": apSysMgmtSipRejectNotificationsGroup,
       "apSysMgmtCollectorPushSuccessNotificationsGroup": apSysMgmtCollectorPushSuccessNotificationsGroup,
       "apSysMgmtRegCacheLimitNotificationsGroup": apSysMgmtRegCacheLimitNotificationsGroup,
       "apSysMgmtShortSessionNotificationsGroup": apSysMgmtShortSessionNotificationsGroup,
       "apSysMgmtMonitorNetworkGatewaySynchronizedNotificationsGroup": apSysMgmtMonitorNetworkGatewaySynchronizedNotificationsGroup,
       "apSysMgmtCallRecordingNotificationsGroup": apSysMgmtCallRecordingNotificationsGroup,
       "apSysMgmtSipExtNotificationsGroup": apSysMgmtSipExtNotificationsGroup,
       "apSysMgmtIcmpFailureNotificationsGroup": apSysMgmtIcmpFailureNotificationsGroup,
       "apSysMgmtCDRPushReceiverNotificationsGroup": apSysMgmtCDRPushReceiverNotificationsGroup,
       "apSysMgmtInetAddrDOSNotificationsGroup": apSysMgmtInetAddrDOSNotificationsGroup,
       "apSysMgmtRejectedMessagesNotificationsGroup": apSysMgmtRejectedMessagesNotificationsGroup,
       "apSysMgmtInetAddrWithReasonDOSNotificationsGroup": apSysMgmtInetAddrWithReasonDOSNotificationsGroup,
       "apSysMgmtAdminGroup": apSysMgmtAdminGroup,
       "apSysMgmtLPGroup": apSysMgmtLPGroup,
       "apSysMgmtPhyUtilNotificationsGroup": apSysMgmtPhyUtilNotificationsGroup,
       "apSysMgmtStorageSpaceNotificationsGroup": apSysMgmtStorageSpaceNotificationsGroup,
       "apSysMgmtTcaGroup": apSysMgmtTcaGroup,
       "apSysMgmtDatabaseRegNotificationsGroup": apSysMgmtDatabaseRegNotificationsGroup,
       "apSysMgmtTacacsNotificationsGroup": apSysMgmtTacacsNotificationsGroup,
       "apSysMgmtOCSRNotificationsGroup": apSysMgmtOCSRNotificationsGroup,
       "apSysMgmtSipInterfaceRegCacheLimitNotificationsGroup": apSysMgmtSipInterfaceRegCacheLimitNotificationsGroup,
       "apSysMgmtH248PortMapUsageNotificationsGroup": apSysMgmtH248PortMapUsageNotificationsGroup,
       "apSysMgmtInetAddrDOSTrustedtoUntrustedNotificationsGroup": apSysMgmtInetAddrDOSTrustedtoUntrustedNotificationsGroup,
       "apSystemManagementMonitorGroups": apSystemManagementMonitorGroups,
       "apSysMgmtMonitorObjects": apSysMgmtMonitorObjects,
       "apSysMgmtPowerLocation": apSysMgmtPowerLocation,
       "apSysMgmtPowerPresence": apSysMgmtPowerPresence,
       "apSysMgmtTempValue": apSysMgmtTempValue,
       "apSysMgmtFanLocation": apSysMgmtFanLocation,
       "apSysMgmtFanSpeed": apSysMgmtFanSpeed,
       "apSysMgmtTaskSuspend": apSysMgmtTaskSuspend,
       "apSysMgmtRedRole": apSysMgmtRedRole,
       "apSysMgmtRedTransState": apSysMgmtRedTransState,
       "apSysMgmtMediaPorts": apSysMgmtMediaPorts,
       "apSysMgmtMediaBandwidth": apSysMgmtMediaBandwidth,
       "apSysMgmtGatewayUnreachable": apSysMgmtGatewayUnreachable,
       "apSysMgmtRadiusDown": apSysMgmtRadiusDown,
       "apSysMgmtH323InitFail": apSysMgmtH323InitFail,
       "apSysMgmtCfgSaveFail": apSysMgmtCfgSaveFail,
       "apSysMgmtHardwareError": apSysMgmtHardwareError,
       "apSysMgmtSAHostname": apSysMgmtSAHostname,
       "apSysMgmtSAIP": apSysMgmtSAIP,
       "apSysMgmtSAStatus": apSysMgmtSAStatus,
       "apSysMgmtSAStatusReason": apSysMgmtSAStatusReason,
       "apSysMgmtAuthFailLevel": apSysMgmtAuthFailLevel,
       "apSysMgmtAuthFailProto": apSysMgmtAuthFailProto,
       "apSysMgmtAuthFailOrigin": apSysMgmtAuthFailOrigin,
       "apSysMgmtSystemState": apSysMgmtSystemState,
       "apSysMgmtTaskDelete": apSysMgmtTaskDelete,
       "apSysMgmtAlgdCPULoad": apSysMgmtAlgdCPULoad,
       "apSysMgmtSipInterfaceRealmName": apSysMgmtSipInterfaceRealmName,
       "apSysMgmtSipInterfaceIP": apSysMgmtSipInterfaceIP,
       "apSysMgmtSipInterfaceStatus": apSysMgmtSipInterfaceStatus,
       "apSysMgmtSipInterfaceStatusReason": apSysMgmtSipInterfaceStatusReason,
       "apSysMgmtCollectPushServerUnreachable": apSysMgmtCollectPushServerUnreachable,
       "apSysMgmtNTPServer": apSysMgmtNTPServer,
       "apSysMgmtBorderGatewayId": apSysMgmtBorderGatewayId,
       "apSysMgmtRFactor": apSysMgmtRFactor,
       "apSysMgmtCallId": apSysMgmtCallId,
       "apSysMgmtSurrogateRegHost": apSysMgmtSurrogateRegHost,
       "apSysMgmtSurrogateRegAor": apSysMgmtSurrogateRegAor,
       "apSysMgmtRealmID": apSysMgmtRealmID,
       "apSysMgmtCollectorPushNodeName": apSysMgmtCollectorPushNodeName,
       "apSysMgmtCollectorPushUniqueFileName": apSysMgmtCollectorPushUniqueFileName,
       "apSysMgmtCollectorPushReceiverAddress": apSysMgmtCollectorPushReceiverAddress,
       "apSysMgmtRealmName": apSysMgmtRealmName,
       "apSysMgmtRealmStatusReason": apSysMgmtRealmStatusReason,
       "apSysMgmtGatewaySynchronized": apSysMgmtGatewaySynchronized,
       "apSysCallRecordingServerName": apSysCallRecordingServerName,
       "apSysCallRecordingServerState": apSysCallRecordingServerState,
       "apSysCDRPushReceiverAddressType": apSysCDRPushReceiverAddressType,
       "apSysCDRPushReceiverAddress": apSysCDRPushReceiverAddress,
       "apSysCDRPushReceiverFailureReasonCode": apSysCDRPushReceiverFailureReasonCode,
       "apSysAdminAuditLogFullReason": apSysAdminAuditLogFullReason,
       "apSysAdminWriteErrorCode": apSysAdminWriteErrorCode,
       "apSysAdminFileName": apSysAdminFileName,
       "apSysAddressType": apSysAddressType,
       "apSysAddress": apSysAddress,
       "apSysReasonCode": apSysReasonCode,
       "apSysMgmtPhyUtilCurrent": apSysMgmtPhyUtilCurrent,
       "apSysMgmtPhyUtilMinorThreshold": apSysMgmtPhyUtilMinorThreshold,
       "apSysMgmtPhyUtilMajorThreshold": apSysMgmtPhyUtilMajorThreshold,
       "apSysMgmtPhyUtilCriticalThreshold": apSysMgmtPhyUtilCriticalThreshold,
       "apSysMgmtPhyRejectOverUtil": apSysMgmtPhyRejectOverUtil,
       "apSysMgmtSpaceAvailCurrent": apSysMgmtSpaceAvailCurrent,
       "apSysMgmtSpaceAvailMinorThreshold": apSysMgmtSpaceAvailMinorThreshold,
       "apSysMgmtSpaceAvailMajorThreshold": apSysMgmtSpaceAvailMajorThreshold,
       "apSysMgmtSpaceAvailCriticalThreshold": apSysMgmtSpaceAvailCriticalThreshold,
       "apSysMgmtPartitionPath": apSysMgmtPartitionPath,
       "apSysMgmtTcaOid": apSysMgmtTcaOid,
       "apSysMgmtTcaCurrent": apSysMgmtTcaCurrent,
       "apSysMgmtTcaMinorThreshold": apSysMgmtTcaMinorThreshold,
       "apSysMgmtTcaMajorThreshold": apSysMgmtTcaMajorThreshold,
       "apSysMgmtTcaCriticalThreshold": apSysMgmtTcaCriticalThreshold,
       "apSysEPSName": apSysEPSName,
       "apSysEPSFqdn": apSysEPSFqdn,
       "apSysEPSAddress": apSysEPSAddress,
       "apSysEPSRealm": apSysEPSRealm,
       "apSysEPSOperationType": apSysEPSOperationType,
       "apSysMgmtDatabaseContactMinorThreshold": apSysMgmtDatabaseContactMinorThreshold,
       "apSysMgmtDatabaseContactMajorThreshold": apSysMgmtDatabaseContactMajorThreshold,
       "apSysMgmtDatabaseContactCriticalThreshold": apSysMgmtDatabaseContactCriticalThreshold,
       "apSysMgmtTacacsDown": apSysMgmtTacacsDown,
       "apSysMgmtOCSRDown": apSysMgmtOCSRDown,
       "apSystemManagementMonitorPrefix": apSystemManagementMonitorPrefix,
       "apSystemManagementMonitors": apSystemManagementMonitors,
       "apSysMgmtPowerTrap": apSysMgmtPowerTrap,
       "apSysMgmtTempTrap": apSysMgmtTempTrap,
       "apSysMgmtFanTrap": apSysMgmtFanTrap,
       "apSysMgmtTaskSuspendTrap": apSysMgmtTaskSuspendTrap,
       "apSysMgmtRedundancyTrap": apSysMgmtRedundancyTrap,
       "apSysMgmtMediaPortsTrap": apSysMgmtMediaPortsTrap,
       "apSysMgmtMediaBandwidthTrap": apSysMgmtMediaBandwidthTrap,
       "apSysMgmtMediaOutOfMemory": apSysMgmtMediaOutOfMemory,
       "apSysMgmtMediaUnknownRealm": apSysMgmtMediaUnknownRealm,
       "apSysMgmtGatewayUnreachableTrap": apSysMgmtGatewayUnreachableTrap,
       "apSysMgmtRadiusDownTrap": apSysMgmtRadiusDownTrap,
       "apSysMgmtH323InitFailTrap": apSysMgmtH323InitFailTrap,
       "apSysMgmtCfgSaveFailTrap": apSysMgmtCfgSaveFailTrap,
       "apSysMgmtHardwareErrorTrap": apSysMgmtHardwareErrorTrap,
       "apSysMgmtSAStatusChangeTrap": apSysMgmtSAStatusChangeTrap,
       "apSysMgmtAuthenticationFailedTrap": apSysMgmtAuthenticationFailedTrap,
       "apSysMgmtSystemStateTrap": apSysMgmtSystemStateTrap,
       "apSysMgmtMediaPortsClearTrap": apSysMgmtMediaPortsClearTrap,
       "apSysMgmtMediaBandwidthClearTrap": apSysMgmtMediaBandwidthClearTrap,
       "apSysMgmtMediaOutOfMemoryClear": apSysMgmtMediaOutOfMemoryClear,
       "apSysMgmtGatewayUnreachableClearTrap": apSysMgmtGatewayUnreachableClearTrap,
       "apSysMgmtRadiusDownClearTrap": apSysMgmtRadiusDownClearTrap,
       "apSysMgmtTaskDeleteTrap": apSysMgmtTaskDeleteTrap,
       "apSysMgmtAlgdCPULoadTrap": apSysMgmtAlgdCPULoadTrap,
       "apSysMgmtAlgdCPULoadClearTrap": apSysMgmtAlgdCPULoadClearTrap,
       "apSysMgmtInterfaceStatusChangeTrap": apSysMgmtInterfaceStatusChangeTrap,
       "apSysMgmtENUMStatusChangeTrap": apSysMgmtENUMStatusChangeTrap,
       "apSysMgmtPushServerUnreachableTrap": apSysMgmtPushServerUnreachableTrap,
       "apSysMgmtPushServerUnreachableClearTrap": apSysMgmtPushServerUnreachableClearTrap,
       "apSysMgmtNTPServerUnreachableTrap": apSysMgmtNTPServerUnreachableTrap,
       "apSysMgmtNTPServerUnreachableClearTrap": apSysMgmtNTPServerUnreachableClearTrap,
       "apSysMgmtNTPServiceDownTrap": apSysMgmtNTPServiceDownTrap,
       "apSysMgmtNTPServiceDownClearTrap": apSysMgmtNTPServiceDownClearTrap,
       "apSysMgmtMediaSupervisionTimerExpTrap": apSysMgmtMediaSupervisionTimerExpTrap,
       "apSysMgmntH248AssociationLostTrap": apSysMgmntH248AssociationLostTrap,
       "apSysMgmntH248AssociationLostClearTrap": apSysMgmntH248AssociationLostClearTrap,
       "apSysMgmtRFactorBelowThresholdTrap": apSysMgmtRFactorBelowThresholdTrap,
       "apSysMgmtRFactorBelowThresholdClearTrap": apSysMgmtRFactorBelowThresholdClearTrap,
       "apSysMgmtSurrogateRegFailed": apSysMgmtSurrogateRegFailed,
       "apSysMgmtRealmMinutesExceedTrap": apSysMgmtRealmMinutesExceedTrap,
       "apSysMgmtRealmMinutesExceedClearTrap": apSysMgmtRealmMinutesExceedClearTrap,
       "apSysMgmtLDAPStatusChangeTrap": apSysMgmtLDAPStatusChangeTrap,
       "apSysMgmtNTPClockSkewTrap": apSysMgmtNTPClockSkewTrap,
       "apSysMgmtCollectorPushSuccessTrap": apSysMgmtCollectorPushSuccessTrap,
       "apSysMgmtRealmStatusChangeTrap": apSysMgmtRealmStatusChangeTrap,
       "apSysMgmtRegCacheThresholdTrap": apSysMgmtRegCacheThresholdTrap,
       "apSysMgmtRegCacheThresholdClearTrap": apSysMgmtRegCacheThresholdClearTrap,
       "apSysMgmtShortSessionExceedTrap": apSysMgmtShortSessionExceedTrap,
       "apSysMgmtGatewaySynchronizedTrap": apSysMgmtGatewaySynchronizedTrap,
       "apSysMgmtCallRecordingStateChangeTrap": apSysMgmtCallRecordingStateChangeTrap,
       "apSysMgmtRealmIcmpFailureTrap": apSysMgmtRealmIcmpFailureTrap,
       "apSysMgmtRealmIcmpFailureClearTrap": apSysMgmtRealmIcmpFailureClearTrap,
       "apSysMgmtCDRPushReceiverFailureTrap": apSysMgmtCDRPushReceiverFailureTrap,
       "apSysMgmtCDRPushReceiverFailureClearTrap": apSysMgmtCDRPushReceiverFailureClearTrap,
       "apSysMgmtCDRPushAllReceiversFailureTrap": apSysMgmtCDRPushAllReceiversFailureTrap,
       "apSysMgmtCDRPushAllReceiversFailureClearTrap": apSysMgmtCDRPushAllReceiversFailureClearTrap,
       "apSysMgmtRejectedMesagesThresholdExeededTrap": apSysMgmtRejectedMesagesThresholdExeededTrap,
       "apSysMgmtAdminAuditLogFullTrap": apSysMgmtAdminAuditLogFullTrap,
       "apSysMgmtAdminAuditLogFullClearTrap": apSysMgmtAdminAuditLogFullClearTrap,
       "apSysMgmtAdminAuditPushFailTrap": apSysMgmtAdminAuditPushFailTrap,
       "apSysMgmtAdminAuditPushFailClearTrap": apSysMgmtAdminAuditPushFailClearTrap,
       "apSysMgmtAdminWriteFailTrap": apSysMgmtAdminWriteFailTrap,
       "apSysMgmtAdminWriteFailClearTrap": apSysMgmtAdminWriteFailClearTrap,
       "apSysMgmtAdminAuthLockoutTrap": apSysMgmtAdminAuthLockoutTrap,
       "apSysMgmtLPLookupExceededTrap": apSysMgmtLPLookupExceededTrap,
       "apSysMgmtPhyUtilThresholdTrap": apSysMgmtPhyUtilThresholdTrap,
       "apSysMgmtPhyUtilThresholdClearTrap": apSysMgmtPhyUtilThresholdClearTrap,
       "apSysMgmtSpaceAvailThresholdTrap": apSysMgmtSpaceAvailThresholdTrap,
       "apSysMgmtSpaceAvailThresholdClearTrap": apSysMgmtSpaceAvailThresholdClearTrap,
       "apSysMgmtCdrFileDeleteTrap": apSysMgmtCdrFileDeleteTrap,
       "apSysMgmtSataAccessErrorTrap": apSysMgmtSataAccessErrorTrap,
       "apSysMgmtTcaTrap": apSysMgmtTcaTrap,
       "apSysMgmtTcaClearTrap": apSysMgmtTcaClearTrap,
       "apSysMgmtExtPolicyServerConnDownTrap": apSysMgmtExtPolicyServerConnDownTrap,
       "apSysMgmtExtPolicyServerConnEstTrap": apSysMgmtExtPolicyServerConnEstTrap,
       "apSysMgmtDatabaseRegCacheCapTrap": apSysMgmtDatabaseRegCacheCapTrap,
       "apSysMgmtDatabaseRegCacheCapClearTrap": apSysMgmtDatabaseRegCacheCapClearTrap,
       "apSysMgmtTacacsDownTrap": apSysMgmtTacacsDownTrap,
       "apSysMgmtTacacsDownClearTrap": apSysMgmtTacacsDownClearTrap,
       "apSysMgmtOCSRDownTrap": apSysMgmtOCSRDownTrap,
       "apSysMgmtOCSRDownClearTrap": apSysMgmtOCSRDownClearTrap,
       "apSysMgmtSipInterfaceRegCacheThresholdTrap": apSysMgmtSipInterfaceRegCacheThresholdTrap,
       "apSysMgmtSipInterfaceRegCacheThresholdClearTrap": apSysMgmtSipInterfaceRegCacheThresholdClearTrap,
       "apSysMgmtH248PortMapUsageTrap": apSysMgmtH248PortMapUsageTrap,
       "apSysMgmtH248PortMapUsageClearTrap": apSysMgmtH248PortMapUsageClearTrap,
       "apSysMgmtDOSObjects": apSysMgmtDOSObjects,
       "apSysMgmtDOSNotificationObjects": apSysMgmtDOSNotificationObjects,
       "apSysMgmtDOSIpAddress": apSysMgmtDOSIpAddress,
       "apSysMgmtDOSRealmID": apSysMgmtDOSRealmID,
       "apSysMgmtDOSFromUri": apSysMgmtDOSFromUri,
       "apSysMgmtDOSInetAddressType": apSysMgmtDOSInetAddressType,
       "apSysMgmtDOSInetAddress": apSysMgmtDOSInetAddress,
       "apSysMgmtDOSReason": apSysMgmtDOSReason,
       "apSysMgmtDOSNotificationPrefix": apSysMgmtDOSNotificationPrefix,
       "apSysMgmtDOSNotifications": apSysMgmtDOSNotifications,
       "apSysMgmtDOSTrap": apSysMgmtDOSTrap,
       "apSysMgmtExpDOSTrap": apSysMgmtExpDOSTrap,
       "apSysMgmtInetAddrDOSTrap": apSysMgmtInetAddrDOSTrap,
       "apSysMgmtInetAddrWithReasonDOSTrap": apSysMgmtInetAddrWithReasonDOSTrap,
       "apSysMgmtInetAddrTrustedToUntrustedDOSTrap": apSysMgmtInetAddrTrustedToUntrustedDOSTrap,
       "apSysMgmtSipRejectionObjects": apSysMgmtSipRejectionObjects,
       "apSysMgmtSipRejectionNotificationObjects": apSysMgmtSipRejectionNotificationObjects,
       "apSysMgmtSipRejFromUriUser": apSysMgmtSipRejFromUriUser,
       "apSysMgmtSipRejToUriUser": apSysMgmtSipRejToUriUser,
       "apSysMgmtSipRejRequestUri": apSysMgmtSipRejRequestUri,
       "apSysMgmtSipRejContactUri": apSysMgmtSipRejContactUri,
       "apSysMgmtSipRejIpAddress": apSysMgmtSipRejIpAddress,
       "apSysMgmtSipRejMsgType": apSysMgmtSipRejMsgType,
       "apSysMgmtSipRejMethod": apSysMgmtSipRejMethod,
       "apSysMgmtSipRejReason": apSysMgmtSipRejReason,
       "apSysMgmtSipRejectionNotificationPrefix": apSysMgmtSipRejectionNotificationPrefix,
       "apSysMgmtSipRejectionNotifications": apSysMgmtSipRejectionNotifications,
       "apSysMgmtSipRejectionTrap": apSysMgmtSipRejectionTrap}
)
