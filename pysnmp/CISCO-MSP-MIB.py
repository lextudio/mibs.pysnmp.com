# SNMP MIB module (CISCO-MSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MSP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:58 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoMspMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 793)
)
ciscoMspMIB.setRevisions(
        ("2012-04-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoMspMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoMspMIBNotifs = _CiscoMspMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 0)
)
_CiscoMspMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMspMIBObjects = _CiscoMspMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1)
)


class _CMspGlobalStatus_Type(Integer32):
    """Custom type cMspGlobalStatus based on Integer32"""
    defaultValue = 2

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


_CMspGlobalStatus_Type.__name__ = "Integer32"
_CMspGlobalStatus_Object = MibScalar
cMspGlobalStatus = _CMspGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 1),
    _CMspGlobalStatus_Type()
)
cMspGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMspGlobalStatus.setStatus("current")


class _CMspGlobalProfile_Type(SnmpAdminString):
    """Custom type cMspGlobalProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CMspGlobalProfile_Type.__name__ = "SnmpAdminString"
_CMspGlobalProfile_Object = MibScalar
cMspGlobalProfile = _CMspGlobalProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 2),
    _CMspGlobalProfile_Type()
)
cMspGlobalProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMspGlobalProfile.setStatus("current")
_CMspIfProfileTable_Object = MibTable
cMspIfProfileTable = _CMspIfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 3)
)
if mibBuilder.loadTexts:
    cMspIfProfileTable.setStatus("current")
_CMspIfProfileEntry_Object = MibTableRow
cMspIfProfileEntry = _CMspIfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 3, 1)
)
cMspIfProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cMspIfProfileEntry.setStatus("current")


class _CMspIfProfileName_Type(SnmpAdminString):
    """Custom type cMspIfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CMspIfProfileName_Type.__name__ = "SnmpAdminString"
_CMspIfProfileName_Object = MibTableColumn
cMspIfProfileName = _CMspIfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 3, 1, 1),
    _CMspIfProfileName_Type()
)
cMspIfProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspIfProfileName.setStatus("current")


class _CMspIfProfileStorageType_Type(StorageType):
    """Custom type cMspIfProfileStorageType based on StorageType"""


_CMspIfProfileStorageType_Object = MibTableColumn
cMspIfProfileStorageType = _CMspIfProfileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 3, 1, 2),
    _CMspIfProfileStorageType_Type()
)
cMspIfProfileStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspIfProfileStorageType.setStatus("current")
_CMspIfProfileRowStatus_Type = RowStatus
_CMspIfProfileRowStatus_Object = MibTableColumn
cMspIfProfileRowStatus = _CMspIfProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 3, 1, 3),
    _CMspIfProfileRowStatus_Type()
)
cMspIfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspIfProfileRowStatus.setStatus("current")
_CMspProfileTable_Object = MibTable
cMspProfileTable = _CMspProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 4)
)
if mibBuilder.loadTexts:
    cMspProfileTable.setStatus("current")
_CMspProfileEntry_Object = MibTableRow
cMspProfileEntry = _CMspProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 4, 1)
)
cMspProfileEntry.setIndexNames(
    (0, "CISCO-MSP-MIB", "cMspProfileName"),
)
if mibBuilder.loadTexts:
    cMspProfileEntry.setStatus("current")


class _CMspProfileName_Type(SnmpAdminString):
    """Custom type cMspProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CMspProfileName_Type.__name__ = "SnmpAdminString"
_CMspProfileName_Object = MibTableColumn
cMspProfileName = _CMspProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 4, 1, 1),
    _CMspProfileName_Type()
)
cMspProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspProfileName.setStatus("current")


class _CMspProfileService_Type(Bits):
    """Custom type cMspProfileService based on Bits"""
    namedValues = NamedValues(
        *(("metadata", 1),
          ("rsvp", 0))
    )

_CMspProfileService_Type.__name__ = "Bits"
_CMspProfileService_Object = MibTableColumn
cMspProfileService = _CMspProfileService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 4, 1, 2),
    _CMspProfileService_Type()
)
cMspProfileService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspProfileService.setStatus("current")


class _CMspProfileRsvp_Type(SnmpAdminString):
    """Custom type cMspProfileRsvp based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CMspProfileRsvp_Type.__name__ = "SnmpAdminString"
_CMspProfileRsvp_Object = MibTableColumn
cMspProfileRsvp = _CMspProfileRsvp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 4, 1, 3),
    _CMspProfileRsvp_Type()
)
cMspProfileRsvp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspProfileRsvp.setStatus("current")


class _CMspProfileMetadata_Type(SnmpAdminString):
    """Custom type cMspProfileMetadata based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CMspProfileMetadata_Type.__name__ = "SnmpAdminString"
_CMspProfileMetadata_Object = MibTableColumn
cMspProfileMetadata = _CMspProfileMetadata_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 4, 1, 4),
    _CMspProfileMetadata_Type()
)
cMspProfileMetadata.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspProfileMetadata.setStatus("current")


class _CMspProfileStorageType_Type(StorageType):
    """Custom type cMspProfileStorageType based on StorageType"""


_CMspProfileStorageType_Object = MibTableColumn
cMspProfileStorageType = _CMspProfileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 4, 1, 5),
    _CMspProfileStorageType_Type()
)
cMspProfileStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspProfileStorageType.setStatus("current")
_CMspProfileRowStatus_Type = RowStatus
_CMspProfileRowStatus_Object = MibTableColumn
cMspProfileRowStatus = _CMspProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 4, 1, 6),
    _CMspProfileRowStatus_Type()
)
cMspProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspProfileRowStatus.setStatus("current")
_CMspRsvpParamsTable_Object = MibTable
cMspRsvpParamsTable = _CMspRsvpParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 5)
)
if mibBuilder.loadTexts:
    cMspRsvpParamsTable.setStatus("current")
_CMspRsvpParamsEntry_Object = MibTableRow
cMspRsvpParamsEntry = _CMspRsvpParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 5, 1)
)
cMspRsvpParamsEntry.setIndexNames(
    (0, "CISCO-MSP-MIB", "cMspRsvpParamsName"),
)
if mibBuilder.loadTexts:
    cMspRsvpParamsEntry.setStatus("current")


class _CMspRsvpParamsName_Type(SnmpAdminString):
    """Custom type cMspRsvpParamsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CMspRsvpParamsName_Type.__name__ = "SnmpAdminString"
_CMspRsvpParamsName_Object = MibTableColumn
cMspRsvpParamsName = _CMspRsvpParamsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 5, 1, 1),
    _CMspRsvpParamsName_Type()
)
cMspRsvpParamsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspRsvpParamsName.setStatus("current")


class _CMspRsvpParamsBandwidth_Type(Unsigned32):
    """Custom type cMspRsvpParamsBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )


_CMspRsvpParamsBandwidth_Type.__name__ = "Unsigned32"
_CMspRsvpParamsBandwidth_Object = MibTableColumn
cMspRsvpParamsBandwidth = _CMspRsvpParamsBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 5, 1, 2),
    _CMspRsvpParamsBandwidth_Type()
)
cMspRsvpParamsBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspRsvpParamsBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cMspRsvpParamsBandwidth.setUnits("kbps")


class _CMspRsvpParamsPeakRate_Type(Unsigned32):
    """Custom type cMspRsvpParamsPeakRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )


_CMspRsvpParamsPeakRate_Type.__name__ = "Unsigned32"
_CMspRsvpParamsPeakRate_Object = MibTableColumn
cMspRsvpParamsPeakRate = _CMspRsvpParamsPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 5, 1, 3),
    _CMspRsvpParamsPeakRate_Type()
)
cMspRsvpParamsPeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspRsvpParamsPeakRate.setStatus("current")
if mibBuilder.loadTexts:
    cMspRsvpParamsPeakRate.setUnits("kbps")


class _CMspRsvpParamsMaxBurst_Type(Unsigned32):
    """Custom type cMspRsvpParamsMaxBurst based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CMspRsvpParamsMaxBurst_Type.__name__ = "Unsigned32"
_CMspRsvpParamsMaxBurst_Object = MibTableColumn
cMspRsvpParamsMaxBurst = _CMspRsvpParamsMaxBurst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 5, 1, 4),
    _CMspRsvpParamsMaxBurst_Type()
)
cMspRsvpParamsMaxBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspRsvpParamsMaxBurst.setStatus("current")
if mibBuilder.loadTexts:
    cMspRsvpParamsMaxBurst.setUnits("kB")


class _CMspRsvpParamsPriorityPrempt_Type(Unsigned32):
    """Custom type cMspRsvpParamsPriorityPrempt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CMspRsvpParamsPriorityPrempt_Type.__name__ = "Unsigned32"
_CMspRsvpParamsPriorityPrempt_Object = MibTableColumn
cMspRsvpParamsPriorityPrempt = _CMspRsvpParamsPriorityPrempt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 5, 1, 5),
    _CMspRsvpParamsPriorityPrempt_Type()
)
cMspRsvpParamsPriorityPrempt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspRsvpParamsPriorityPrempt.setStatus("current")


class _CMspRsvpParamsPriorityDefend_Type(Unsigned32):
    """Custom type cMspRsvpParamsPriorityDefend based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CMspRsvpParamsPriorityDefend_Type.__name__ = "Unsigned32"
_CMspRsvpParamsPriorityDefend_Object = MibTableColumn
cMspRsvpParamsPriorityDefend = _CMspRsvpParamsPriorityDefend_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 5, 1, 6),
    _CMspRsvpParamsPriorityDefend_Type()
)
cMspRsvpParamsPriorityDefend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspRsvpParamsPriorityDefend.setStatus("current")


class _CMspRsvpParamsStorageType_Type(StorageType):
    """Custom type cMspRsvpParamsStorageType based on StorageType"""


_CMspRsvpParamsStorageType_Object = MibTableColumn
cMspRsvpParamsStorageType = _CMspRsvpParamsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 5, 1, 7),
    _CMspRsvpParamsStorageType_Type()
)
cMspRsvpParamsStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspRsvpParamsStorageType.setStatus("current")
_CMspRsvpParamsRowStatus_Type = RowStatus
_CMspRsvpParamsRowStatus_Object = MibTableColumn
cMspRsvpParamsRowStatus = _CMspRsvpParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 5, 1, 8),
    _CMspRsvpParamsRowStatus_Type()
)
cMspRsvpParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspRsvpParamsRowStatus.setStatus("current")
_CMspMetaParamsTable_Object = MibTable
cMspMetaParamsTable = _CMspMetaParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6)
)
if mibBuilder.loadTexts:
    cMspMetaParamsTable.setStatus("current")
_CMspMetaParamsEntry_Object = MibTableRow
cMspMetaParamsEntry = _CMspMetaParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1)
)
cMspMetaParamsEntry.setIndexNames(
    (0, "CISCO-MSP-MIB", "cMspMetaParamsName"),
)
if mibBuilder.loadTexts:
    cMspMetaParamsEntry.setStatus("current")


class _CMspMetaParamsName_Type(SnmpAdminString):
    """Custom type cMspMetaParamsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CMspMetaParamsName_Type.__name__ = "SnmpAdminString"
_CMspMetaParamsName_Object = MibTableColumn
cMspMetaParamsName = _CMspMetaParamsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1, 1),
    _CMspMetaParamsName_Type()
)
cMspMetaParamsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspMetaParamsName.setStatus("current")


class _CMspMetaParamsBandwidth_Type(Unsigned32):
    """Custom type cMspMetaParamsBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000000),
    )


_CMspMetaParamsBandwidth_Type.__name__ = "Unsigned32"
_CMspMetaParamsBandwidth_Object = MibTableColumn
cMspMetaParamsBandwidth = _CMspMetaParamsBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1, 2),
    _CMspMetaParamsBandwidth_Type()
)
cMspMetaParamsBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspMetaParamsBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cMspMetaParamsBandwidth.setUnits("kbps")
_CMspMetaParamsSyncSrc_Type = Unsigned32
_CMspMetaParamsSyncSrc_Object = MibTableColumn
cMspMetaParamsSyncSrc = _CMspMetaParamsSyncSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1, 3),
    _CMspMetaParamsSyncSrc_Type()
)
cMspMetaParamsSyncSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspMetaParamsSyncSrc.setStatus("current")
_CMspMetaParamsClockFreq_Type = Unsigned32
_CMspMetaParamsClockFreq_Object = MibTableColumn
cMspMetaParamsClockFreq = _CMspMetaParamsClockFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1, 4),
    _CMspMetaParamsClockFreq_Type()
)
cMspMetaParamsClockFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspMetaParamsClockFreq.setStatus("current")


class _CMspMetaParamsSessId_Type(SnmpAdminString):
    """Custom type cMspMetaParamsSessId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CMspMetaParamsSessId_Type.__name__ = "SnmpAdminString"
_CMspMetaParamsSessId_Object = MibTableColumn
cMspMetaParamsSessId = _CMspMetaParamsSessId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1, 5),
    _CMspMetaParamsSessId_Type()
)
cMspMetaParamsSessId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspMetaParamsSessId.setStatus("current")


class _CMspMetaParamsDomainName_Type(SnmpAdminString):
    """Custom type cMspMetaParamsDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CMspMetaParamsDomainName_Type.__name__ = "SnmpAdminString"
_CMspMetaParamsDomainName_Object = MibTableColumn
cMspMetaParamsDomainName = _CMspMetaParamsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1, 6),
    _CMspMetaParamsDomainName_Type()
)
cMspMetaParamsDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspMetaParamsDomainName.setStatus("current")


class _CMspMetaParamsCname_Type(SnmpAdminString):
    """Custom type cMspMetaParamsCname based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CMspMetaParamsCname_Type.__name__ = "SnmpAdminString"
_CMspMetaParamsCname_Object = MibTableColumn
cMspMetaParamsCname = _CMspMetaParamsCname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1, 7),
    _CMspMetaParamsCname_Type()
)
cMspMetaParamsCname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspMetaParamsCname.setStatus("current")


class _CMspMetaParamsMimeType_Type(SnmpAdminString):
    """Custom type cMspMetaParamsMimeType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CMspMetaParamsMimeType_Type.__name__ = "SnmpAdminString"
_CMspMetaParamsMimeType_Object = MibTableColumn
cMspMetaParamsMimeType = _CMspMetaParamsMimeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1, 8),
    _CMspMetaParamsMimeType_Type()
)
cMspMetaParamsMimeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspMetaParamsMimeType.setStatus("current")


class _CMspMetaParamsPayloadType_Type(Unsigned32):
    """Custom type cMspMetaParamsPayloadType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CMspMetaParamsPayloadType_Type.__name__ = "Unsigned32"
_CMspMetaParamsPayloadType_Object = MibTableColumn
cMspMetaParamsPayloadType = _CMspMetaParamsPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1, 9),
    _CMspMetaParamsPayloadType_Type()
)
cMspMetaParamsPayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspMetaParamsPayloadType.setStatus("current")


class _CMspMetaParamsSipUserName_Type(SnmpAdminString):
    """Custom type cMspMetaParamsSipUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CMspMetaParamsSipUserName_Type.__name__ = "SnmpAdminString"
_CMspMetaParamsSipUserName_Object = MibTableColumn
cMspMetaParamsSipUserName = _CMspMetaParamsSipUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1, 10),
    _CMspMetaParamsSipUserName_Type()
)
cMspMetaParamsSipUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspMetaParamsSipUserName.setStatus("current")


class _CMspMetaParamsSipEmail_Type(SnmpAdminString):
    """Custom type cMspMetaParamsSipEmail based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_CMspMetaParamsSipEmail_Type.__name__ = "SnmpAdminString"
_CMspMetaParamsSipEmail_Object = MibTableColumn
cMspMetaParamsSipEmail = _CMspMetaParamsSipEmail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1, 11),
    _CMspMetaParamsSipEmail_Type()
)
cMspMetaParamsSipEmail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspMetaParamsSipEmail.setStatus("current")


class _CMspMetaParamsAppName_Type(SnmpAdminString):
    """Custom type cMspMetaParamsAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CMspMetaParamsAppName_Type.__name__ = "SnmpAdminString"
_CMspMetaParamsAppName_Object = MibTableColumn
cMspMetaParamsAppName = _CMspMetaParamsAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1, 12),
    _CMspMetaParamsAppName_Type()
)
cMspMetaParamsAppName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspMetaParamsAppName.setStatus("current")


class _CMspMetaParamsAppVendor_Type(SnmpAdminString):
    """Custom type cMspMetaParamsAppVendor based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CMspMetaParamsAppVendor_Type.__name__ = "SnmpAdminString"
_CMspMetaParamsAppVendor_Object = MibTableColumn
cMspMetaParamsAppVendor = _CMspMetaParamsAppVendor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1, 13),
    _CMspMetaParamsAppVendor_Type()
)
cMspMetaParamsAppVendor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspMetaParamsAppVendor.setStatus("current")


class _CMspMetaParamsAppVersion_Type(SnmpAdminString):
    """Custom type cMspMetaParamsAppVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CMspMetaParamsAppVersion_Type.__name__ = "SnmpAdminString"
_CMspMetaParamsAppVersion_Object = MibTableColumn
cMspMetaParamsAppVersion = _CMspMetaParamsAppVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1, 14),
    _CMspMetaParamsAppVersion_Type()
)
cMspMetaParamsAppVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspMetaParamsAppVersion.setStatus("current")


class _CMspMetaParamsStorageType_Type(StorageType):
    """Custom type cMspMetaParamsStorageType based on StorageType"""


_CMspMetaParamsStorageType_Object = MibTableColumn
cMspMetaParamsStorageType = _CMspMetaParamsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1, 15),
    _CMspMetaParamsStorageType_Type()
)
cMspMetaParamsStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspMetaParamsStorageType.setStatus("current")
_CMspMetaParamsRowStatus_Type = RowStatus
_CMspMetaParamsRowStatus_Object = MibTableColumn
cMspMetaParamsRowStatus = _CMspMetaParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 1, 6, 1, 16),
    _CMspMetaParamsRowStatus_Type()
)
cMspMetaParamsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMspMetaParamsRowStatus.setStatus("current")
_CiscoMspMIBConform_ObjectIdentity = ObjectIdentity
ciscoMspMIBConform = _CiscoMspMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 2)
)
_CiscoMspMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoMspMIBCompliances = _CiscoMspMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 2, 1)
)
_CiscoMspMIBGroups_ObjectIdentity = ObjectIdentity
ciscoMspMIBGroups = _CiscoMspMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 2, 2)
)

# Managed Objects groups

ciscoMspMIBScalarObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 2, 2, 1)
)
ciscoMspMIBScalarObjectGroup.setObjects(
      *(("CISCO-MSP-MIB", "cMspGlobalStatus"),
        ("CISCO-MSP-MIB", "cMspGlobalProfile"))
)
if mibBuilder.loadTexts:
    ciscoMspMIBScalarObjectGroup.setStatus("current")

ciscoMspMIBIfProfileObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 2, 2, 2)
)
ciscoMspMIBIfProfileObjectGroup.setObjects(
      *(("CISCO-MSP-MIB", "cMspIfProfileName"),
        ("CISCO-MSP-MIB", "cMspIfProfileStorageType"),
        ("CISCO-MSP-MIB", "cMspIfProfileRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoMspMIBIfProfileObjectGroup.setStatus("current")

ciscoMspMIBProfileNameObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 2, 2, 3)
)
ciscoMspMIBProfileNameObjectGroup.setObjects(
      *(("CISCO-MSP-MIB", "cMspProfileName"),
        ("CISCO-MSP-MIB", "cMspProfileService"),
        ("CISCO-MSP-MIB", "cMspProfileRsvp"),
        ("CISCO-MSP-MIB", "cMspProfileMetadata"),
        ("CISCO-MSP-MIB", "cMspProfileStorageType"),
        ("CISCO-MSP-MIB", "cMspProfileRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoMspMIBProfileNameObjectGroup.setStatus("current")

ciscoMspMIBRsvpParamsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 2, 2, 4)
)
ciscoMspMIBRsvpParamsObjectGroup.setObjects(
      *(("CISCO-MSP-MIB", "cMspRsvpParamsName"),
        ("CISCO-MSP-MIB", "cMspRsvpParamsBandwidth"),
        ("CISCO-MSP-MIB", "cMspRsvpParamsPeakRate"),
        ("CISCO-MSP-MIB", "cMspRsvpParamsMaxBurst"),
        ("CISCO-MSP-MIB", "cMspRsvpParamsPriorityPrempt"),
        ("CISCO-MSP-MIB", "cMspRsvpParamsPriorityDefend"),
        ("CISCO-MSP-MIB", "cMspRsvpParamsStorageType"),
        ("CISCO-MSP-MIB", "cMspRsvpParamsRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoMspMIBRsvpParamsObjectGroup.setStatus("current")

ciscoMspMIBMetaParamsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 2, 2, 5)
)
ciscoMspMIBMetaParamsObjectGroup.setObjects(
      *(("CISCO-MSP-MIB", "cMspMetaParamsName"),
        ("CISCO-MSP-MIB", "cMspMetaParamsBandwidth"),
        ("CISCO-MSP-MIB", "cMspMetaParamsSyncSrc"),
        ("CISCO-MSP-MIB", "cMspMetaParamsClockFreq"),
        ("CISCO-MSP-MIB", "cMspMetaParamsSessId"),
        ("CISCO-MSP-MIB", "cMspMetaParamsDomainName"),
        ("CISCO-MSP-MIB", "cMspMetaParamsCname"),
        ("CISCO-MSP-MIB", "cMspMetaParamsMimeType"),
        ("CISCO-MSP-MIB", "cMspMetaParamsPayloadType"),
        ("CISCO-MSP-MIB", "cMspMetaParamsSipUserName"),
        ("CISCO-MSP-MIB", "cMspMetaParamsSipEmail"),
        ("CISCO-MSP-MIB", "cMspMetaParamsAppName"),
        ("CISCO-MSP-MIB", "cMspMetaParamsAppVendor"),
        ("CISCO-MSP-MIB", "cMspMetaParamsAppVersion"),
        ("CISCO-MSP-MIB", "cMspMetaParamsStorageType"),
        ("CISCO-MSP-MIB", "cMspMetaParamsRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoMspMIBMetaParamsObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoMspMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 793, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoMspMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MSP-MIB",
    **{"ciscoMspMIB": ciscoMspMIB,
       "ciscoMspMIBNotifs": ciscoMspMIBNotifs,
       "ciscoMspMIBObjects": ciscoMspMIBObjects,
       "cMspGlobalStatus": cMspGlobalStatus,
       "cMspGlobalProfile": cMspGlobalProfile,
       "cMspIfProfileTable": cMspIfProfileTable,
       "cMspIfProfileEntry": cMspIfProfileEntry,
       "cMspIfProfileName": cMspIfProfileName,
       "cMspIfProfileStorageType": cMspIfProfileStorageType,
       "cMspIfProfileRowStatus": cMspIfProfileRowStatus,
       "cMspProfileTable": cMspProfileTable,
       "cMspProfileEntry": cMspProfileEntry,
       "cMspProfileName": cMspProfileName,
       "cMspProfileService": cMspProfileService,
       "cMspProfileRsvp": cMspProfileRsvp,
       "cMspProfileMetadata": cMspProfileMetadata,
       "cMspProfileStorageType": cMspProfileStorageType,
       "cMspProfileRowStatus": cMspProfileRowStatus,
       "cMspRsvpParamsTable": cMspRsvpParamsTable,
       "cMspRsvpParamsEntry": cMspRsvpParamsEntry,
       "cMspRsvpParamsName": cMspRsvpParamsName,
       "cMspRsvpParamsBandwidth": cMspRsvpParamsBandwidth,
       "cMspRsvpParamsPeakRate": cMspRsvpParamsPeakRate,
       "cMspRsvpParamsMaxBurst": cMspRsvpParamsMaxBurst,
       "cMspRsvpParamsPriorityPrempt": cMspRsvpParamsPriorityPrempt,
       "cMspRsvpParamsPriorityDefend": cMspRsvpParamsPriorityDefend,
       "cMspRsvpParamsStorageType": cMspRsvpParamsStorageType,
       "cMspRsvpParamsRowStatus": cMspRsvpParamsRowStatus,
       "cMspMetaParamsTable": cMspMetaParamsTable,
       "cMspMetaParamsEntry": cMspMetaParamsEntry,
       "cMspMetaParamsName": cMspMetaParamsName,
       "cMspMetaParamsBandwidth": cMspMetaParamsBandwidth,
       "cMspMetaParamsSyncSrc": cMspMetaParamsSyncSrc,
       "cMspMetaParamsClockFreq": cMspMetaParamsClockFreq,
       "cMspMetaParamsSessId": cMspMetaParamsSessId,
       "cMspMetaParamsDomainName": cMspMetaParamsDomainName,
       "cMspMetaParamsCname": cMspMetaParamsCname,
       "cMspMetaParamsMimeType": cMspMetaParamsMimeType,
       "cMspMetaParamsPayloadType": cMspMetaParamsPayloadType,
       "cMspMetaParamsSipUserName": cMspMetaParamsSipUserName,
       "cMspMetaParamsSipEmail": cMspMetaParamsSipEmail,
       "cMspMetaParamsAppName": cMspMetaParamsAppName,
       "cMspMetaParamsAppVendor": cMspMetaParamsAppVendor,
       "cMspMetaParamsAppVersion": cMspMetaParamsAppVersion,
       "cMspMetaParamsStorageType": cMspMetaParamsStorageType,
       "cMspMetaParamsRowStatus": cMspMetaParamsRowStatus,
       "ciscoMspMIBConform": ciscoMspMIBConform,
       "ciscoMspMIBCompliances": ciscoMspMIBCompliances,
       "ciscoMspMIBCompliance": ciscoMspMIBCompliance,
       "ciscoMspMIBGroups": ciscoMspMIBGroups,
       "ciscoMspMIBScalarObjectGroup": ciscoMspMIBScalarObjectGroup,
       "ciscoMspMIBIfProfileObjectGroup": ciscoMspMIBIfProfileObjectGroup,
       "ciscoMspMIBProfileNameObjectGroup": ciscoMspMIBProfileNameObjectGroup,
       "ciscoMspMIBRsvpParamsObjectGroup": ciscoMspMIBRsvpParamsObjectGroup,
       "ciscoMspMIBMetaParamsObjectGroup": ciscoMspMIBMetaParamsObjectGroup}
)
