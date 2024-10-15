# SNMP MIB module (CTRON-SFPS-SFLSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-SFLSP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:31 2024
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

(vlanSflsp1stHop,
 vlanSflspArea,
 vlanSflspGeneralVariables,
 vlanSflspIfMetric,
 vlanSflspInterfaces,
 vlanSflspLSDBFlood,
 vlanSflspLSPStats,
 vlanSflspLsdb,
 vlanSflspNeighbors,
 vlanSflspTracePathAPI,
 vlanSflspTracePathInternal) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "vlanSflsp1stHop",
    "vlanSflspArea",
    "vlanSflspGeneralVariables",
    "vlanSflspIfMetric",
    "vlanSflspInterfaces",
    "vlanSflspLSDBFlood",
    "vlanSflspLSPStats",
    "vlanSflspLsdb",
    "vlanSflspNeighbors",
    "vlanSflspTracePathAPI",
    "vlanSflspTracePathInternal")

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



class SfpsAddress(OctetString):
    """Custom type SfpsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VlanSflspGeneralSwitchID_Type = OctetString
_VlanSflspGeneralSwitchID_Object = MibScalar
vlanSflspGeneralSwitchID = _VlanSflspGeneralSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 1),
    _VlanSflspGeneralSwitchID_Type()
)
vlanSflspGeneralSwitchID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspGeneralSwitchID.setStatus("mandatory")


class _VlanSflspGeneralAdminStatus_Type(Integer32):
    """Custom type vlanSflspGeneralAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VlanSflspGeneralAdminStatus_Type.__name__ = "Integer32"
_VlanSflspGeneralAdminStatus_Object = MibScalar
vlanSflspGeneralAdminStatus = _VlanSflspGeneralAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 2),
    _VlanSflspGeneralAdminStatus_Type()
)
vlanSflspGeneralAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspGeneralAdminStatus.setStatus("mandatory")
_VlanSflspGeneralVersion_Type = Integer32
_VlanSflspGeneralVersion_Object = MibScalar
vlanSflspGeneralVersion = _VlanSflspGeneralVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 3),
    _VlanSflspGeneralVersion_Type()
)
vlanSflspGeneralVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspGeneralVersion.setStatus("mandatory")


class _VlanSflspGeneralAreaBRStatus_Type(Integer32):
    """Custom type vlanSflspGeneralAreaBRStatus based on Integer32"""
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


_VlanSflspGeneralAreaBRStatus_Type.__name__ = "Integer32"
_VlanSflspGeneralAreaBRStatus_Object = MibScalar
vlanSflspGeneralAreaBRStatus = _VlanSflspGeneralAreaBRStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 4),
    _VlanSflspGeneralAreaBRStatus_Type()
)
vlanSflspGeneralAreaBRStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspGeneralAreaBRStatus.setStatus("mandatory")


class _VlanSflspGeneralASBRStatus_Type(Integer32):
    """Custom type vlanSflspGeneralASBRStatus based on Integer32"""
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


_VlanSflspGeneralASBRStatus_Type.__name__ = "Integer32"
_VlanSflspGeneralASBRStatus_Object = MibScalar
vlanSflspGeneralASBRStatus = _VlanSflspGeneralASBRStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 5),
    _VlanSflspGeneralASBRStatus_Type()
)
vlanSflspGeneralASBRStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspGeneralASBRStatus.setStatus("mandatory")


class _VlanSflspGeneralTOSSupport_Type(Integer32):
    """Custom type vlanSflspGeneralTOSSupport based on Integer32"""
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


_VlanSflspGeneralTOSSupport_Type.__name__ = "Integer32"
_VlanSflspGeneralTOSSupport_Object = MibScalar
vlanSflspGeneralTOSSupport = _VlanSflspGeneralTOSSupport_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 6),
    _VlanSflspGeneralTOSSupport_Type()
)
vlanSflspGeneralTOSSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspGeneralTOSSupport.setStatus("mandatory")
_VlanSflspGeneralOrgNewLSAs_Type = Counter32
_VlanSflspGeneralOrgNewLSAs_Object = MibScalar
vlanSflspGeneralOrgNewLSAs = _VlanSflspGeneralOrgNewLSAs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 7),
    _VlanSflspGeneralOrgNewLSAs_Type()
)
vlanSflspGeneralOrgNewLSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspGeneralOrgNewLSAs.setStatus("mandatory")
_VlanSflspGeneralRcvNewLSAs_Type = Counter32
_VlanSflspGeneralRcvNewLSAs_Object = MibScalar
vlanSflspGeneralRcvNewLSAs = _VlanSflspGeneralRcvNewLSAs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 8),
    _VlanSflspGeneralRcvNewLSAs_Type()
)
vlanSflspGeneralRcvNewLSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspGeneralRcvNewLSAs.setStatus("mandatory")
_VlanSflspGeneralMaxOnQueue_Type = Integer32
_VlanSflspGeneralMaxOnQueue_Object = MibScalar
vlanSflspGeneralMaxOnQueue = _VlanSflspGeneralMaxOnQueue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 9),
    _VlanSflspGeneralMaxOnQueue_Type()
)
vlanSflspGeneralMaxOnQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspGeneralMaxOnQueue.setStatus("mandatory")
_VlanSflspGeneralCurOnQueue_Type = Integer32
_VlanSflspGeneralCurOnQueue_Object = MibScalar
vlanSflspGeneralCurOnQueue = _VlanSflspGeneralCurOnQueue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 10),
    _VlanSflspGeneralCurOnQueue_Type()
)
vlanSflspGeneralCurOnQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspGeneralCurOnQueue.setStatus("mandatory")
_VlanSflspGeneralMaxTimeUs_Type = Integer32
_VlanSflspGeneralMaxTimeUs_Object = MibScalar
vlanSflspGeneralMaxTimeUs = _VlanSflspGeneralMaxTimeUs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 11),
    _VlanSflspGeneralMaxTimeUs_Type()
)
vlanSflspGeneralMaxTimeUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspGeneralMaxTimeUs.setStatus("mandatory")
_VlanSflspGeneralCurTimeUs_Type = Integer32
_VlanSflspGeneralCurTimeUs_Object = MibScalar
vlanSflspGeneralCurTimeUs = _VlanSflspGeneralCurTimeUs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 12),
    _VlanSflspGeneralCurTimeUs_Type()
)
vlanSflspGeneralCurTimeUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspGeneralCurTimeUs.setStatus("mandatory")
_VlanSflspGeneralMaxEvents_Type = Integer32
_VlanSflspGeneralMaxEvents_Object = MibScalar
vlanSflspGeneralMaxEvents = _VlanSflspGeneralMaxEvents_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 13),
    _VlanSflspGeneralMaxEvents_Type()
)
vlanSflspGeneralMaxEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspGeneralMaxEvents.setStatus("mandatory")
_VlanSflspGeneralMaxTimeOccurred_Type = TimeTicks
_VlanSflspGeneralMaxTimeOccurred_Object = MibScalar
vlanSflspGeneralMaxTimeOccurred = _VlanSflspGeneralMaxTimeOccurred_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 14),
    _VlanSflspGeneralMaxTimeOccurred_Type()
)
vlanSflspGeneralMaxTimeOccurred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspGeneralMaxTimeOccurred.setStatus("mandatory")
_VlanSflspGeneralMaxOnQOccurred_Type = TimeTicks
_VlanSflspGeneralMaxOnQOccurred_Object = MibScalar
vlanSflspGeneralMaxOnQOccurred = _VlanSflspGeneralMaxOnQOccurred_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 15),
    _VlanSflspGeneralMaxOnQOccurred_Type()
)
vlanSflspGeneralMaxOnQOccurred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspGeneralMaxOnQOccurred.setStatus("mandatory")
_VlanSflspGeneralTotalSwLinks_Type = Integer32
_VlanSflspGeneralTotalSwLinks_Object = MibScalar
vlanSflspGeneralTotalSwLinks = _VlanSflspGeneralTotalSwLinks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 16),
    _VlanSflspGeneralTotalSwLinks_Type()
)
vlanSflspGeneralTotalSwLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspGeneralTotalSwLinks.setStatus("mandatory")
_VlanSflspGeneralLastChangeDet_Type = TimeTicks
_VlanSflspGeneralLastChangeDet_Object = MibScalar
vlanSflspGeneralLastChangeDet = _VlanSflspGeneralLastChangeDet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 17),
    _VlanSflspGeneralLastChangeDet_Type()
)
vlanSflspGeneralLastChangeDet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspGeneralLastChangeDet.setStatus("mandatory")
_VlanSflspGeneralFloodMask_Type = OctetString
_VlanSflspGeneralFloodMask_Object = MibScalar
vlanSflspGeneralFloodMask = _VlanSflspGeneralFloodMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 18),
    _VlanSflspGeneralFloodMask_Type()
)
vlanSflspGeneralFloodMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspGeneralFloodMask.setStatus("mandatory")
_VlanSflspGeneralLowestMac_Type = OctetString
_VlanSflspGeneralLowestMac_Object = MibScalar
vlanSflspGeneralLowestMac = _VlanSflspGeneralLowestMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 19),
    _VlanSflspGeneralLowestMac_Type()
)
vlanSflspGeneralLowestMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspGeneralLowestMac.setStatus("mandatory")
_VlanSflspGeneralRootId_Type = OctetString
_VlanSflspGeneralRootId_Object = MibScalar
vlanSflspGeneralRootId = _VlanSflspGeneralRootId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 20),
    _VlanSflspGeneralRootId_Type()
)
vlanSflspGeneralRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspGeneralRootId.setStatus("mandatory")


class _VlanSflspGeneralFloodAdminStatus_Type(Integer32):
    """Custom type vlanSflspGeneralFloodAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VlanSflspGeneralFloodAdminStatus_Type.__name__ = "Integer32"
_VlanSflspGeneralFloodAdminStatus_Object = MibScalar
vlanSflspGeneralFloodAdminStatus = _VlanSflspGeneralFloodAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 1, 1, 21),
    _VlanSflspGeneralFloodAdminStatus_Type()
)
vlanSflspGeneralFloodAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspGeneralFloodAdminStatus.setStatus("mandatory")
_VlanSflspLsdbTable_Object = MibTable
vlanSflspLsdbTable = _VlanSflspLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    vlanSflspLsdbTable.setStatus("mandatory")
_VlanSflspLsdbEntry_Object = MibTableRow
vlanSflspLsdbEntry = _VlanSflspLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 2, 1, 1)
)
vlanSflspLsdbEntry.setIndexNames(
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspLsdbAreaID"),
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspLsdbType"),
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspLsdbLSID"),
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspLsdbSwitchID"),
)
if mibBuilder.loadTexts:
    vlanSflspLsdbEntry.setStatus("mandatory")
_VlanSflspLsdbAreaID_Type = Integer32
_VlanSflspLsdbAreaID_Object = MibTableColumn
vlanSflspLsdbAreaID = _VlanSflspLsdbAreaID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 2, 1, 1, 1),
    _VlanSflspLsdbAreaID_Type()
)
vlanSflspLsdbAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLsdbAreaID.setStatus("mandatory")


class _VlanSflspLsdbType_Type(Integer32):
    """Custom type vlanSflspLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connection-link", 2),
          ("switch-link", 1))
    )


_VlanSflspLsdbType_Type.__name__ = "Integer32"
_VlanSflspLsdbType_Object = MibTableColumn
vlanSflspLsdbType = _VlanSflspLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 2, 1, 1, 2),
    _VlanSflspLsdbType_Type()
)
vlanSflspLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLsdbType.setStatus("mandatory")
_VlanSflspLsdbLSID_Type = OctetString
_VlanSflspLsdbLSID_Object = MibTableColumn
vlanSflspLsdbLSID = _VlanSflspLsdbLSID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 2, 1, 1, 3),
    _VlanSflspLsdbLSID_Type()
)
vlanSflspLsdbLSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLsdbLSID.setStatus("mandatory")
_VlanSflspLsdbSwitchID_Type = OctetString
_VlanSflspLsdbSwitchID_Object = MibTableColumn
vlanSflspLsdbSwitchID = _VlanSflspLsdbSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 2, 1, 1, 4),
    _VlanSflspLsdbSwitchID_Type()
)
vlanSflspLsdbSwitchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLsdbSwitchID.setStatus("mandatory")
_VlanSflspLsdbSequence_Type = Integer32
_VlanSflspLsdbSequence_Object = MibTableColumn
vlanSflspLsdbSequence = _VlanSflspLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 2, 1, 1, 5),
    _VlanSflspLsdbSequence_Type()
)
vlanSflspLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLsdbSequence.setStatus("mandatory")
_VlanSflspLsdbAge_Type = Integer32
_VlanSflspLsdbAge_Object = MibTableColumn
vlanSflspLsdbAge = _VlanSflspLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 2, 1, 1, 6),
    _VlanSflspLsdbAge_Type()
)
vlanSflspLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLsdbAge.setStatus("mandatory")
_VlanSflspLsdbChecksum_Type = Integer32
_VlanSflspLsdbChecksum_Object = MibTableColumn
vlanSflspLsdbChecksum = _VlanSflspLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 2, 1, 1, 7),
    _VlanSflspLsdbChecksum_Type()
)
vlanSflspLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLsdbChecksum.setStatus("mandatory")
_VlanSflspLsdbAdvertisement_Type = OctetString
_VlanSflspLsdbAdvertisement_Object = MibTableColumn
vlanSflspLsdbAdvertisement = _VlanSflspLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 2, 1, 1, 8),
    _VlanSflspLsdbAdvertisement_Type()
)
vlanSflspLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLsdbAdvertisement.setStatus("mandatory")


class _VlanSflspLsdbUsedInSPF_Type(Integer32):
    """Custom type vlanSflspLsdbUsedInSPF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_VlanSflspLsdbUsedInSPF_Type.__name__ = "Integer32"
_VlanSflspLsdbUsedInSPF_Object = MibTableColumn
vlanSflspLsdbUsedInSPF = _VlanSflspLsdbUsedInSPF_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 2, 1, 1, 9),
    _VlanSflspLsdbUsedInSPF_Type()
)
vlanSflspLsdbUsedInSPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLsdbUsedInSPF.setStatus("mandatory")
_VlanSflspInterfacesTable_Object = MibTable
vlanSflspInterfacesTable = _VlanSflspInterfacesTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1)
)
if mibBuilder.loadTexts:
    vlanSflspInterfacesTable.setStatus("mandatory")
_VlanSflspInterfacesEntry_Object = MibTableRow
vlanSflspInterfacesEntry = _VlanSflspInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1)
)
vlanSflspInterfacesEntry.setIndexNames(
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspInterfacesIFAddress"),
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspInterfacesSwAddressLess"),
)
if mibBuilder.loadTexts:
    vlanSflspInterfacesEntry.setStatus("mandatory")
_VlanSflspInterfacesIFAddress_Type = SfpsAddress
_VlanSflspInterfacesIFAddress_Object = MibTableColumn
vlanSflspInterfacesIFAddress = _VlanSflspInterfacesIFAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1, 1),
    _VlanSflspInterfacesIFAddress_Type()
)
vlanSflspInterfacesIFAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspInterfacesIFAddress.setStatus("mandatory")
_VlanSflspInterfacesSwAddressLess_Type = Integer32
_VlanSflspInterfacesSwAddressLess_Object = MibTableColumn
vlanSflspInterfacesSwAddressLess = _VlanSflspInterfacesSwAddressLess_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1, 2),
    _VlanSflspInterfacesSwAddressLess_Type()
)
vlanSflspInterfacesSwAddressLess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspInterfacesSwAddressLess.setStatus("mandatory")
_VlanSflspInterfacesAreaID_Type = IpAddress
_VlanSflspInterfacesAreaID_Object = MibTableColumn
vlanSflspInterfacesAreaID = _VlanSflspInterfacesAreaID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1, 3),
    _VlanSflspInterfacesAreaID_Type()
)
vlanSflspInterfacesAreaID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspInterfacesAreaID.setStatus("mandatory")


class _VlanSflspInterfacesIfType_Type(Integer32):
    """Custom type vlanSflspInterfacesIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("brodcast", 1),
          ("nbma", 2),
          ("point-to-point", 3))
    )


_VlanSflspInterfacesIfType_Type.__name__ = "Integer32"
_VlanSflspInterfacesIfType_Object = MibTableColumn
vlanSflspInterfacesIfType = _VlanSflspInterfacesIfType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1, 4),
    _VlanSflspInterfacesIfType_Type()
)
vlanSflspInterfacesIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspInterfacesIfType.setStatus("mandatory")


class _VlanSflspInterfacesAdminStatus_Type(Integer32):
    """Custom type vlanSflspInterfacesAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VlanSflspInterfacesAdminStatus_Type.__name__ = "Integer32"
_VlanSflspInterfacesAdminStatus_Object = MibTableColumn
vlanSflspInterfacesAdminStatus = _VlanSflspInterfacesAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1, 5),
    _VlanSflspInterfacesAdminStatus_Type()
)
vlanSflspInterfacesAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspInterfacesAdminStatus.setStatus("mandatory")
_VlanSflspInterfacesSwPriority_Type = Integer32
_VlanSflspInterfacesSwPriority_Object = MibTableColumn
vlanSflspInterfacesSwPriority = _VlanSflspInterfacesSwPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1, 6),
    _VlanSflspInterfacesSwPriority_Type()
)
vlanSflspInterfacesSwPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspInterfacesSwPriority.setStatus("mandatory")
_VlanSflspInterfacesTransDelay_Type = Integer32
_VlanSflspInterfacesTransDelay_Object = MibTableColumn
vlanSflspInterfacesTransDelay = _VlanSflspInterfacesTransDelay_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1, 7),
    _VlanSflspInterfacesTransDelay_Type()
)
vlanSflspInterfacesTransDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspInterfacesTransDelay.setStatus("mandatory")
_VlanSflspInterfacesReTransInterval_Type = Integer32
_VlanSflspInterfacesReTransInterval_Object = MibTableColumn
vlanSflspInterfacesReTransInterval = _VlanSflspInterfacesReTransInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1, 8),
    _VlanSflspInterfacesReTransInterval_Type()
)
vlanSflspInterfacesReTransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspInterfacesReTransInterval.setStatus("mandatory")
_VlanSflspInterfacesHelloInterval_Type = Integer32
_VlanSflspInterfacesHelloInterval_Object = MibTableColumn
vlanSflspInterfacesHelloInterval = _VlanSflspInterfacesHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1, 9),
    _VlanSflspInterfacesHelloInterval_Type()
)
vlanSflspInterfacesHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspInterfacesHelloInterval.setStatus("mandatory")
_VlanSflspInterfacesDeadInterval_Type = Integer32
_VlanSflspInterfacesDeadInterval_Object = MibTableColumn
vlanSflspInterfacesDeadInterval = _VlanSflspInterfacesDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1, 10),
    _VlanSflspInterfacesDeadInterval_Type()
)
vlanSflspInterfacesDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspInterfacesDeadInterval.setStatus("mandatory")
_VlanSflspInterfacesPollInterval_Type = Integer32
_VlanSflspInterfacesPollInterval_Object = MibTableColumn
vlanSflspInterfacesPollInterval = _VlanSflspInterfacesPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1, 11),
    _VlanSflspInterfacesPollInterval_Type()
)
vlanSflspInterfacesPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspInterfacesPollInterval.setStatus("mandatory")


class _VlanSflspInterfacesState_Type(Integer32):
    """Custom type vlanSflspInterfacesState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bdr", 6),
          ("down", 1),
          ("dr", 5),
          ("dr-other", 7),
          ("loopback", 2),
          ("point-to-point", 4),
          ("waiting", 3))
    )


_VlanSflspInterfacesState_Type.__name__ = "Integer32"
_VlanSflspInterfacesState_Object = MibTableColumn
vlanSflspInterfacesState = _VlanSflspInterfacesState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1, 12),
    _VlanSflspInterfacesState_Type()
)
vlanSflspInterfacesState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspInterfacesState.setStatus("mandatory")
_VlanSflspInterfacesDS_Type = SfpsAddress
_VlanSflspInterfacesDS_Object = MibTableColumn
vlanSflspInterfacesDS = _VlanSflspInterfacesDS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1, 13),
    _VlanSflspInterfacesDS_Type()
)
vlanSflspInterfacesDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspInterfacesDS.setStatus("mandatory")
_VlanSflspInterfacesBDS_Type = SfpsAddress
_VlanSflspInterfacesBDS_Object = MibTableColumn
vlanSflspInterfacesBDS = _VlanSflspInterfacesBDS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1, 14),
    _VlanSflspInterfacesBDS_Type()
)
vlanSflspInterfacesBDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspInterfacesBDS.setStatus("mandatory")
_VlanSflspInterfacesEvents_Type = Counter32
_VlanSflspInterfacesEvents_Object = MibTableColumn
vlanSflspInterfacesEvents = _VlanSflspInterfacesEvents_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1, 15),
    _VlanSflspInterfacesEvents_Type()
)
vlanSflspInterfacesEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspInterfacesEvents.setStatus("mandatory")
_VlanSflspInterfacesAuthKey_Type = SfpsAddress
_VlanSflspInterfacesAuthKey_Object = MibTableColumn
vlanSflspInterfacesAuthKey = _VlanSflspInterfacesAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 3, 1, 1, 16),
    _VlanSflspInterfacesAuthKey_Type()
)
vlanSflspInterfacesAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspInterfacesAuthKey.setStatus("mandatory")
_VlanSflspIfMetricTable_Object = MibTable
vlanSflspIfMetricTable = _VlanSflspIfMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 4, 1)
)
if mibBuilder.loadTexts:
    vlanSflspIfMetricTable.setStatus("mandatory")
_VlanSflspIfMetricEntry_Object = MibTableRow
vlanSflspIfMetricEntry = _VlanSflspIfMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 4, 1, 1)
)
vlanSflspIfMetricEntry.setIndexNames(
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspIfMetricIfAddress"),
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspIfMetricIfTOSType"),
)
if mibBuilder.loadTexts:
    vlanSflspIfMetricEntry.setStatus("mandatory")
_VlanSflspIfMetricIfAddress_Type = OctetString
_VlanSflspIfMetricIfAddress_Object = MibTableColumn
vlanSflspIfMetricIfAddress = _VlanSflspIfMetricIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 4, 1, 1, 1),
    _VlanSflspIfMetricIfAddress_Type()
)
vlanSflspIfMetricIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspIfMetricIfAddress.setStatus("mandatory")
_VlanSflspIfMetricIfTOSType_Type = Integer32
_VlanSflspIfMetricIfTOSType_Object = MibTableColumn
vlanSflspIfMetricIfTOSType = _VlanSflspIfMetricIfTOSType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 4, 1, 1, 2),
    _VlanSflspIfMetricIfTOSType_Type()
)
vlanSflspIfMetricIfTOSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspIfMetricIfTOSType.setStatus("mandatory")
_VlanSflspIfMetricIfMetric_Type = Integer32
_VlanSflspIfMetricIfMetric_Object = MibTableColumn
vlanSflspIfMetricIfMetric = _VlanSflspIfMetricIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 4, 1, 1, 3),
    _VlanSflspIfMetricIfMetric_Type()
)
vlanSflspIfMetricIfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspIfMetricIfMetric.setStatus("mandatory")


class _VlanSflspIfMetricIfStatus_Type(Integer32):
    """Custom type vlanSflspIfMetricIfStatus based on Integer32"""
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


_VlanSflspIfMetricIfStatus_Type.__name__ = "Integer32"
_VlanSflspIfMetricIfStatus_Object = MibTableColumn
vlanSflspIfMetricIfStatus = _VlanSflspIfMetricIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 4, 1, 1, 4),
    _VlanSflspIfMetricIfStatus_Type()
)
vlanSflspIfMetricIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspIfMetricIfStatus.setStatus("mandatory")
_VlanSflspNeighborsTable_Object = MibTable
vlanSflspNeighborsTable = _VlanSflspNeighborsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1)
)
if mibBuilder.loadTexts:
    vlanSflspNeighborsTable.setStatus("mandatory")
_VlanSflspNeighborsEntry_Object = MibTableRow
vlanSflspNeighborsEntry = _VlanSflspNeighborsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1)
)
vlanSflspNeighborsEntry.setIndexNames(
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspNeighborsPortName"),
)
if mibBuilder.loadTexts:
    vlanSflspNeighborsEntry.setStatus("mandatory")
_VlanSflspNeighborsPortName_Type = OctetString
_VlanSflspNeighborsPortName_Object = MibTableColumn
vlanSflspNeighborsPortName = _VlanSflspNeighborsPortName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 1),
    _VlanSflspNeighborsPortName_Type()
)
vlanSflspNeighborsPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsPortName.setStatus("mandatory")
_VlanSflspNeighborsSwitchID_Type = OctetString
_VlanSflspNeighborsSwitchID_Object = MibTableColumn
vlanSflspNeighborsSwitchID = _VlanSflspNeighborsSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 2),
    _VlanSflspNeighborsSwitchID_Type()
)
vlanSflspNeighborsSwitchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsSwitchID.setStatus("mandatory")
_VlanSflspNeighborsOptions_Type = Integer32
_VlanSflspNeighborsOptions_Object = MibTableColumn
vlanSflspNeighborsOptions = _VlanSflspNeighborsOptions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 3),
    _VlanSflspNeighborsOptions_Type()
)
vlanSflspNeighborsOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsOptions.setStatus("mandatory")
_VlanSflspNeighborsPriority_Type = Integer32
_VlanSflspNeighborsPriority_Object = MibTableColumn
vlanSflspNeighborsPriority = _VlanSflspNeighborsPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 4),
    _VlanSflspNeighborsPriority_Type()
)
vlanSflspNeighborsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsPriority.setStatus("mandatory")


class _VlanSflspNeighborsState_Type(Integer32):
    """Custom type vlanSflspNeighborsState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 5),
          ("exchange-start", 6),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("two-way", 4))
    )


_VlanSflspNeighborsState_Type.__name__ = "Integer32"
_VlanSflspNeighborsState_Object = MibTableColumn
vlanSflspNeighborsState = _VlanSflspNeighborsState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 5),
    _VlanSflspNeighborsState_Type()
)
vlanSflspNeighborsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsState.setStatus("mandatory")
_VlanSflspNeighborsEvents_Type = Counter32
_VlanSflspNeighborsEvents_Object = MibTableColumn
vlanSflspNeighborsEvents = _VlanSflspNeighborsEvents_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 6),
    _VlanSflspNeighborsEvents_Type()
)
vlanSflspNeighborsEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsEvents.setStatus("mandatory")
_VlanSflspNeighborsLSRetransQLen_Type = Gauge32
_VlanSflspNeighborsLSRetransQLen_Object = MibTableColumn
vlanSflspNeighborsLSRetransQLen = _VlanSflspNeighborsLSRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 7),
    _VlanSflspNeighborsLSRetransQLen_Type()
)
vlanSflspNeighborsLSRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsLSRetransQLen.setStatus("mandatory")
_VlanSflspNeighborsHELLOsRcvd_Type = Integer32
_VlanSflspNeighborsHELLOsRcvd_Object = MibTableColumn
vlanSflspNeighborsHELLOsRcvd = _VlanSflspNeighborsHELLOsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 8),
    _VlanSflspNeighborsHELLOsRcvd_Type()
)
vlanSflspNeighborsHELLOsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsHELLOsRcvd.setStatus("mandatory")
_VlanSflspNeighborsDBDsRcvd_Type = Integer32
_VlanSflspNeighborsDBDsRcvd_Object = MibTableColumn
vlanSflspNeighborsDBDsRcvd = _VlanSflspNeighborsDBDsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 9),
    _VlanSflspNeighborsDBDsRcvd_Type()
)
vlanSflspNeighborsDBDsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsDBDsRcvd.setStatus("mandatory")
_VlanSflspNeighborsLSUsRcvd_Type = Integer32
_VlanSflspNeighborsLSUsRcvd_Object = MibTableColumn
vlanSflspNeighborsLSUsRcvd = _VlanSflspNeighborsLSUsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 10),
    _VlanSflspNeighborsLSUsRcvd_Type()
)
vlanSflspNeighborsLSUsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsLSUsRcvd.setStatus("mandatory")
_VlanSflspNeighborsLSRsRcvd_Type = Integer32
_VlanSflspNeighborsLSRsRcvd_Object = MibTableColumn
vlanSflspNeighborsLSRsRcvd = _VlanSflspNeighborsLSRsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 11),
    _VlanSflspNeighborsLSRsRcvd_Type()
)
vlanSflspNeighborsLSRsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsLSRsRcvd.setStatus("mandatory")
_VlanSflspNeighborsLSACKsRcvd_Type = Integer32
_VlanSflspNeighborsLSACKsRcvd_Object = MibTableColumn
vlanSflspNeighborsLSACKsRcvd = _VlanSflspNeighborsLSACKsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 12),
    _VlanSflspNeighborsLSACKsRcvd_Type()
)
vlanSflspNeighborsLSACKsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsLSACKsRcvd.setStatus("mandatory")
_VlanSflspNeighborsHELLOsSent_Type = Integer32
_VlanSflspNeighborsHELLOsSent_Object = MibTableColumn
vlanSflspNeighborsHELLOsSent = _VlanSflspNeighborsHELLOsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 13),
    _VlanSflspNeighborsHELLOsSent_Type()
)
vlanSflspNeighborsHELLOsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsHELLOsSent.setStatus("mandatory")
_VlanSflspNeighborsDBDsSent_Type = Integer32
_VlanSflspNeighborsDBDsSent_Object = MibTableColumn
vlanSflspNeighborsDBDsSent = _VlanSflspNeighborsDBDsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 14),
    _VlanSflspNeighborsDBDsSent_Type()
)
vlanSflspNeighborsDBDsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsDBDsSent.setStatus("mandatory")
_VlanSflspNeighborsLSUsSent_Type = Integer32
_VlanSflspNeighborsLSUsSent_Object = MibTableColumn
vlanSflspNeighborsLSUsSent = _VlanSflspNeighborsLSUsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 15),
    _VlanSflspNeighborsLSUsSent_Type()
)
vlanSflspNeighborsLSUsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsLSUsSent.setStatus("mandatory")
_VlanSflspNeighborsLSRsSent_Type = Integer32
_VlanSflspNeighborsLSRsSent_Object = MibTableColumn
vlanSflspNeighborsLSRsSent = _VlanSflspNeighborsLSRsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 16),
    _VlanSflspNeighborsLSRsSent_Type()
)
vlanSflspNeighborsLSRsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsLSRsSent.setStatus("mandatory")
_VlanSflspNeighborsLSACKsSent_Type = Integer32
_VlanSflspNeighborsLSACKsSent_Object = MibTableColumn
vlanSflspNeighborsLSACKsSent = _VlanSflspNeighborsLSACKsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 17),
    _VlanSflspNeighborsLSACKsSent_Type()
)
vlanSflspNeighborsLSACKsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsLSACKsSent.setStatus("mandatory")


class _VlanSflspNeighborsNBMAStatus_Type(Integer32):
    """Custom type vlanSflspNeighborsNBMAStatus based on Integer32"""
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


_VlanSflspNeighborsNBMAStatus_Type.__name__ = "Integer32"
_VlanSflspNeighborsNBMAStatus_Object = MibTableColumn
vlanSflspNeighborsNBMAStatus = _VlanSflspNeighborsNBMAStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 18),
    _VlanSflspNeighborsNBMAStatus_Type()
)
vlanSflspNeighborsNBMAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsNBMAStatus.setStatus("mandatory")
_VlanSflspNeighborsFULLTimeSec_Type = TimeTicks
_VlanSflspNeighborsFULLTimeSec_Object = MibTableColumn
vlanSflspNeighborsFULLTimeSec = _VlanSflspNeighborsFULLTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 5, 1, 1, 19),
    _VlanSflspNeighborsFULLTimeSec_Type()
)
vlanSflspNeighborsFULLTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspNeighborsFULLTimeSec.setStatus("mandatory")
_VlanSflspAreaTable_Object = MibTable
vlanSflspAreaTable = _VlanSflspAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 6, 1)
)
if mibBuilder.loadTexts:
    vlanSflspAreaTable.setStatus("mandatory")
_VlanSflspAreaEntry_Object = MibTableRow
vlanSflspAreaEntry = _VlanSflspAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 6, 1, 1)
)
vlanSflspAreaEntry.setIndexNames(
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspAreaAreaID"),
)
if mibBuilder.loadTexts:
    vlanSflspAreaEntry.setStatus("mandatory")
_VlanSflspAreaAreaID_Type = IpAddress
_VlanSflspAreaAreaID_Object = MibTableColumn
vlanSflspAreaAreaID = _VlanSflspAreaAreaID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 6, 1, 1, 1),
    _VlanSflspAreaAreaID_Type()
)
vlanSflspAreaAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspAreaAreaID.setStatus("mandatory")
_VlanSflspAreaAuthType_Type = Integer32
_VlanSflspAreaAuthType_Object = MibTableColumn
vlanSflspAreaAuthType = _VlanSflspAreaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 6, 1, 1, 2),
    _VlanSflspAreaAuthType_Type()
)
vlanSflspAreaAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspAreaAuthType.setStatus("mandatory")
_VlanSflspAreaSPFRuns_Type = Counter32
_VlanSflspAreaSPFRuns_Object = MibTableColumn
vlanSflspAreaSPFRuns = _VlanSflspAreaSPFRuns_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 6, 1, 1, 3),
    _VlanSflspAreaSPFRuns_Type()
)
vlanSflspAreaSPFRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspAreaSPFRuns.setStatus("mandatory")
_VlanSflspAreaABRCount_Type = Gauge32
_VlanSflspAreaABRCount_Object = MibTableColumn
vlanSflspAreaABRCount = _VlanSflspAreaABRCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 6, 1, 1, 4),
    _VlanSflspAreaABRCount_Type()
)
vlanSflspAreaABRCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspAreaABRCount.setStatus("mandatory")
_VlanSflspAreaASBRCount_Type = Gauge32
_VlanSflspAreaASBRCount_Object = MibTableColumn
vlanSflspAreaASBRCount = _VlanSflspAreaASBRCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 6, 1, 1, 5),
    _VlanSflspAreaASBRCount_Type()
)
vlanSflspAreaASBRCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspAreaASBRCount.setStatus("mandatory")
_VlanSflspAreaAreaLSACnt_Type = Gauge32
_VlanSflspAreaAreaLSACnt_Object = MibTableColumn
vlanSflspAreaAreaLSACnt = _VlanSflspAreaAreaLSACnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 6, 1, 1, 6),
    _VlanSflspAreaAreaLSACnt_Type()
)
vlanSflspAreaAreaLSACnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspAreaAreaLSACnt.setStatus("mandatory")
_VlanSflspAreaAreaCheckSum_Type = Integer32
_VlanSflspAreaAreaCheckSum_Object = MibTableColumn
vlanSflspAreaAreaCheckSum = _VlanSflspAreaAreaCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 6, 1, 1, 7),
    _VlanSflspAreaAreaCheckSum_Type()
)
vlanSflspAreaAreaCheckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspAreaAreaCheckSum.setStatus("mandatory")
_VlanSflspAreaLastSpfRun_Type = TimeTicks
_VlanSflspAreaLastSpfRun_Object = MibTableColumn
vlanSflspAreaLastSpfRun = _VlanSflspAreaLastSpfRun_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 6, 1, 1, 8),
    _VlanSflspAreaLastSpfRun_Type()
)
vlanSflspAreaLastSpfRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspAreaLastSpfRun.setStatus("mandatory")
_VlanSflsp1stHopTable_Object = MibTable
vlanSflsp1stHopTable = _VlanSflsp1stHopTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 7, 1)
)
if mibBuilder.loadTexts:
    vlanSflsp1stHopTable.setStatus("mandatory")
_VlanSflsp1stHopEntry_Object = MibTableRow
vlanSflsp1stHopEntry = _VlanSflsp1stHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 7, 1, 1)
)
vlanSflsp1stHopEntry.setIndexNames(
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflsp1stHopDestSwitch"),
)
if mibBuilder.loadTexts:
    vlanSflsp1stHopEntry.setStatus("mandatory")
_VlanSflsp1stHopDestSwitch_Type = OctetString
_VlanSflsp1stHopDestSwitch_Object = MibTableColumn
vlanSflsp1stHopDestSwitch = _VlanSflsp1stHopDestSwitch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 7, 1, 1, 1),
    _VlanSflsp1stHopDestSwitch_Type()
)
vlanSflsp1stHopDestSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflsp1stHopDestSwitch.setStatus("mandatory")
_VlanSflsp1stHopPath11stHop_Type = OctetString
_VlanSflsp1stHopPath11stHop_Object = MibTableColumn
vlanSflsp1stHopPath11stHop = _VlanSflsp1stHopPath11stHop_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 7, 1, 1, 2),
    _VlanSflsp1stHopPath11stHop_Type()
)
vlanSflsp1stHopPath11stHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflsp1stHopPath11stHop.setStatus("mandatory")
_VlanSflsp1stHopPath21stHop_Type = OctetString
_VlanSflsp1stHopPath21stHop_Object = MibTableColumn
vlanSflsp1stHopPath21stHop = _VlanSflsp1stHopPath21stHop_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 7, 1, 1, 3),
    _VlanSflsp1stHopPath21stHop_Type()
)
vlanSflsp1stHopPath21stHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflsp1stHopPath21stHop.setStatus("mandatory")
_VlanSflsp1stHopPath31stHop_Type = OctetString
_VlanSflsp1stHopPath31stHop_Object = MibTableColumn
vlanSflsp1stHopPath31stHop = _VlanSflsp1stHopPath31stHop_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 7, 1, 1, 4),
    _VlanSflsp1stHopPath31stHop_Type()
)
vlanSflsp1stHopPath31stHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflsp1stHopPath31stHop.setStatus("mandatory")
_VlanSflspTracePathAPIDest_Type = OctetString
_VlanSflspTracePathAPIDest_Object = MibScalar
vlanSflspTracePathAPIDest = _VlanSflspTracePathAPIDest_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 1, 1, 1),
    _VlanSflspTracePathAPIDest_Type()
)
vlanSflspTracePathAPIDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspTracePathAPIDest.setStatus("mandatory")
_VlanSflspTracePathAPIID_Type = Integer32
_VlanSflspTracePathAPIID_Object = MibScalar
vlanSflspTracePathAPIID = _VlanSflspTracePathAPIID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 1, 1, 2),
    _VlanSflspTracePathAPIID_Type()
)
vlanSflspTracePathAPIID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspTracePathAPIID.setStatus("mandatory")


class _VlanSflspTracePathAPIType_Type(Integer32):
    """Custom type vlanSflspTracePathAPIType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_VlanSflspTracePathAPIType_Type.__name__ = "Integer32"
_VlanSflspTracePathAPIType_Object = MibScalar
vlanSflspTracePathAPIType = _VlanSflspTracePathAPIType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 1, 1, 3),
    _VlanSflspTracePathAPIType_Type()
)
vlanSflspTracePathAPIType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspTracePathAPIType.setStatus("mandatory")


class _VlanSflspTracePathAPIAction_Type(Integer32):
    """Custom type vlanSflspTracePathAPIAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 2),
          ("other", 1),
          ("suspend", 3))
    )


_VlanSflspTracePathAPIAction_Type.__name__ = "Integer32"
_VlanSflspTracePathAPIAction_Object = MibScalar
vlanSflspTracePathAPIAction = _VlanSflspTracePathAPIAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 1, 1, 4),
    _VlanSflspTracePathAPIAction_Type()
)
vlanSflspTracePathAPIAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspTracePathAPIAction.setStatus("mandatory")
_VlanSflspTracePathTable_Object = MibTable
vlanSflspTracePathTable = _VlanSflspTracePathTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 2, 1)
)
if mibBuilder.loadTexts:
    vlanSflspTracePathTable.setStatus("mandatory")
_VlanSflspTracePathEntry_Object = MibTableRow
vlanSflspTracePathEntry = _VlanSflspTracePathEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 2, 1, 1)
)
vlanSflspTracePathEntry.setIndexNames(
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspTracePathDest"),
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspTracePathID"),
)
if mibBuilder.loadTexts:
    vlanSflspTracePathEntry.setStatus("mandatory")
_VlanSflspTracePathDest_Type = OctetString
_VlanSflspTracePathDest_Object = MibTableColumn
vlanSflspTracePathDest = _VlanSflspTracePathDest_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 2, 1, 1, 1),
    _VlanSflspTracePathDest_Type()
)
vlanSflspTracePathDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspTracePathDest.setStatus("mandatory")
_VlanSflspTracePathID_Type = Integer32
_VlanSflspTracePathID_Object = MibTableColumn
vlanSflspTracePathID = _VlanSflspTracePathID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 2, 1, 1, 2),
    _VlanSflspTracePathID_Type()
)
vlanSflspTracePathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspTracePathID.setStatus("mandatory")


class _VlanSflspTracePathAction_Type(Integer32):
    """Custom type vlanSflspTracePathAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 2),
          ("other", 1),
          ("suspend", 3))
    )


_VlanSflspTracePathAction_Type.__name__ = "Integer32"
_VlanSflspTracePathAction_Object = MibTableColumn
vlanSflspTracePathAction = _VlanSflspTracePathAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 2, 1, 1, 3),
    _VlanSflspTracePathAction_Type()
)
vlanSflspTracePathAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspTracePathAction.setStatus("mandatory")


class _VlanSflspTracePathStatus_Type(Integer32):
    """Custom type vlanSflspTracePathStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("other", 1),
          ("success", 2))
    )


_VlanSflspTracePathStatus_Type.__name__ = "Integer32"
_VlanSflspTracePathStatus_Object = MibTableColumn
vlanSflspTracePathStatus = _VlanSflspTracePathStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 2, 1, 1, 4),
    _VlanSflspTracePathStatus_Type()
)
vlanSflspTracePathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspTracePathStatus.setStatus("mandatory")
_VlanSflspTracePathListTable_Object = MibTable
vlanSflspTracePathListTable = _VlanSflspTracePathListTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 2, 2)
)
if mibBuilder.loadTexts:
    vlanSflspTracePathListTable.setStatus("mandatory")
_VlanSflspTracePathListEntry_Object = MibTableRow
vlanSflspTracePathListEntry = _VlanSflspTracePathListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 2, 2, 1)
)
vlanSflspTracePathListEntry.setIndexNames(
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspTracePathListDest"),
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspTracePathListID"),
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspTracePathListPathNum"),
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspTracePathListHopNum"),
)
if mibBuilder.loadTexts:
    vlanSflspTracePathListEntry.setStatus("mandatory")
_VlanSflspTracePathListDest_Type = OctetString
_VlanSflspTracePathListDest_Object = MibTableColumn
vlanSflspTracePathListDest = _VlanSflspTracePathListDest_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 2, 2, 1, 1),
    _VlanSflspTracePathListDest_Type()
)
vlanSflspTracePathListDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspTracePathListDest.setStatus("mandatory")
_VlanSflspTracePathListID_Type = Integer32
_VlanSflspTracePathListID_Object = MibTableColumn
vlanSflspTracePathListID = _VlanSflspTracePathListID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 2, 2, 1, 2),
    _VlanSflspTracePathListID_Type()
)
vlanSflspTracePathListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspTracePathListID.setStatus("mandatory")
_VlanSflspTracePathListPathNum_Type = Integer32
_VlanSflspTracePathListPathNum_Object = MibTableColumn
vlanSflspTracePathListPathNum = _VlanSflspTracePathListPathNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 2, 2, 1, 3),
    _VlanSflspTracePathListPathNum_Type()
)
vlanSflspTracePathListPathNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspTracePathListPathNum.setStatus("mandatory")
_VlanSflspTracePathListHopNum_Type = Integer32
_VlanSflspTracePathListHopNum_Object = MibTableColumn
vlanSflspTracePathListHopNum = _VlanSflspTracePathListHopNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 2, 2, 1, 4),
    _VlanSflspTracePathListHopNum_Type()
)
vlanSflspTracePathListHopNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspTracePathListHopNum.setStatus("mandatory")
_VlanSflspTracePathListHopAddr_Type = OctetString
_VlanSflspTracePathListHopAddr_Object = MibTableColumn
vlanSflspTracePathListHopAddr = _VlanSflspTracePathListHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 8, 2, 2, 1, 5),
    _VlanSflspTracePathListHopAddr_Type()
)
vlanSflspTracePathListHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspTracePathListHopAddr.setStatus("mandatory")
_VlanSflspLSDBFloodTable_Object = MibTable
vlanSflspLSDBFloodTable = _VlanSflspLSDBFloodTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 20, 1)
)
if mibBuilder.loadTexts:
    vlanSflspLSDBFloodTable.setStatus("mandatory")
_VlanSflspLSDBFloodEntry_Object = MibTableRow
vlanSflspLSDBFloodEntry = _VlanSflspLSDBFloodEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 20, 1, 1)
)
vlanSflspLSDBFloodEntry.setIndexNames(
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspLSDBFloodAreaID"),
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspLSDBFloodType"),
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspLSDBFloodLSID"),
    (0, "CTRON-SFPS-SFLSP-MIB", "vlanSflspLSDBFloodAdvSwitchID"),
)
if mibBuilder.loadTexts:
    vlanSflspLSDBFloodEntry.setStatus("mandatory")
_VlanSflspLSDBFloodAreaID_Type = Integer32
_VlanSflspLSDBFloodAreaID_Object = MibTableColumn
vlanSflspLSDBFloodAreaID = _VlanSflspLSDBFloodAreaID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 20, 1, 1, 1),
    _VlanSflspLSDBFloodAreaID_Type()
)
vlanSflspLSDBFloodAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSDBFloodAreaID.setStatus("mandatory")


class _VlanSflspLSDBFloodType_Type(Integer32):
    """Custom type vlanSflspLSDBFloodType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connectionLink", 2),
          ("switchLink", 1))
    )


_VlanSflspLSDBFloodType_Type.__name__ = "Integer32"
_VlanSflspLSDBFloodType_Object = MibTableColumn
vlanSflspLSDBFloodType = _VlanSflspLSDBFloodType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 20, 1, 1, 2),
    _VlanSflspLSDBFloodType_Type()
)
vlanSflspLSDBFloodType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSDBFloodType.setStatus("mandatory")
_VlanSflspLSDBFloodLSID_Type = SfpsAddress
_VlanSflspLSDBFloodLSID_Object = MibTableColumn
vlanSflspLSDBFloodLSID = _VlanSflspLSDBFloodLSID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 20, 1, 1, 3),
    _VlanSflspLSDBFloodLSID_Type()
)
vlanSflspLSDBFloodLSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSDBFloodLSID.setStatus("mandatory")
_VlanSflspLSDBFloodAdvSwitchID_Type = SfpsAddress
_VlanSflspLSDBFloodAdvSwitchID_Object = MibTableColumn
vlanSflspLSDBFloodAdvSwitchID = _VlanSflspLSDBFloodAdvSwitchID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 20, 1, 1, 4),
    _VlanSflspLSDBFloodAdvSwitchID_Type()
)
vlanSflspLSDBFloodAdvSwitchID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSDBFloodAdvSwitchID.setStatus("mandatory")
_VlanSflspLSDBFloodSequence_Type = Integer32
_VlanSflspLSDBFloodSequence_Object = MibTableColumn
vlanSflspLSDBFloodSequence = _VlanSflspLSDBFloodSequence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 20, 1, 1, 5),
    _VlanSflspLSDBFloodSequence_Type()
)
vlanSflspLSDBFloodSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSDBFloodSequence.setStatus("mandatory")
_VlanSflspLSDBFloodAge_Type = Integer32
_VlanSflspLSDBFloodAge_Object = MibTableColumn
vlanSflspLSDBFloodAge = _VlanSflspLSDBFloodAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 20, 1, 1, 6),
    _VlanSflspLSDBFloodAge_Type()
)
vlanSflspLSDBFloodAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSDBFloodAge.setStatus("mandatory")
_VlanSflspLSDBFloodChecksum_Type = Integer32
_VlanSflspLSDBFloodChecksum_Object = MibTableColumn
vlanSflspLSDBFloodChecksum = _VlanSflspLSDBFloodChecksum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 20, 1, 1, 7),
    _VlanSflspLSDBFloodChecksum_Type()
)
vlanSflspLSDBFloodChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSDBFloodChecksum.setStatus("mandatory")
_VlanSflspLSDBFloodAdvertisement_Type = SfpsAddress
_VlanSflspLSDBFloodAdvertisement_Object = MibTableColumn
vlanSflspLSDBFloodAdvertisement = _VlanSflspLSDBFloodAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 20, 1, 1, 8),
    _VlanSflspLSDBFloodAdvertisement_Type()
)
vlanSflspLSDBFloodAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSDBFloodAdvertisement.setStatus("mandatory")


class _VlanSflspLSDBFloodUsedInSPF_Type(Integer32):
    """Custom type vlanSflspLSDBFloodUsedInSPF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_VlanSflspLSDBFloodUsedInSPF_Type.__name__ = "Integer32"
_VlanSflspLSDBFloodUsedInSPF_Object = MibTableColumn
vlanSflspLSDBFloodUsedInSPF = _VlanSflspLSDBFloodUsedInSPF_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 20, 1, 1, 9),
    _VlanSflspLSDBFloodUsedInSPF_Type()
)
vlanSflspLSDBFloodUsedInSPF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSDBFloodUsedInSPF.setStatus("mandatory")


class _VlanSflspLSDBFloodEverUsed_Type(Integer32):
    """Custom type vlanSflspLSDBFloodEverUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_VlanSflspLSDBFloodEverUsed_Type.__name__ = "Integer32"
_VlanSflspLSDBFloodEverUsed_Object = MibTableColumn
vlanSflspLSDBFloodEverUsed = _VlanSflspLSDBFloodEverUsed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 20, 1, 1, 10),
    _VlanSflspLSDBFloodEverUsed_Type()
)
vlanSflspLSDBFloodEverUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSDBFloodEverUsed.setStatus("mandatory")
_VlanSflspLSPStatsMaxOnQueue_Type = Integer32
_VlanSflspLSPStatsMaxOnQueue_Object = MibScalar
vlanSflspLSPStatsMaxOnQueue = _VlanSflspLSPStatsMaxOnQueue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 21, 1),
    _VlanSflspLSPStatsMaxOnQueue_Type()
)
vlanSflspLSPStatsMaxOnQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSPStatsMaxOnQueue.setStatus("mandatory")
_VlanSflspLSPStatsCurOnQueue_Type = Integer32
_VlanSflspLSPStatsCurOnQueue_Object = MibScalar
vlanSflspLSPStatsCurOnQueue = _VlanSflspLSPStatsCurOnQueue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 21, 2),
    _VlanSflspLSPStatsCurOnQueue_Type()
)
vlanSflspLSPStatsCurOnQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSPStatsCurOnQueue.setStatus("mandatory")
_VlanSflspLSPStatsMaxTimeUs_Type = Integer32
_VlanSflspLSPStatsMaxTimeUs_Object = MibScalar
vlanSflspLSPStatsMaxTimeUs = _VlanSflspLSPStatsMaxTimeUs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 21, 3),
    _VlanSflspLSPStatsMaxTimeUs_Type()
)
vlanSflspLSPStatsMaxTimeUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSPStatsMaxTimeUs.setStatus("mandatory")
_VlanSflspLSPStatsCurTimeUs_Type = Integer32
_VlanSflspLSPStatsCurTimeUs_Object = MibScalar
vlanSflspLSPStatsCurTimeUs = _VlanSflspLSPStatsCurTimeUs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 21, 4),
    _VlanSflspLSPStatsCurTimeUs_Type()
)
vlanSflspLSPStatsCurTimeUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSPStatsCurTimeUs.setStatus("mandatory")
_VlanSflspLSPStatsMaxTimeOccurred_Type = Integer32
_VlanSflspLSPStatsMaxTimeOccurred_Object = MibScalar
vlanSflspLSPStatsMaxTimeOccurred = _VlanSflspLSPStatsMaxTimeOccurred_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 21, 5),
    _VlanSflspLSPStatsMaxTimeOccurred_Type()
)
vlanSflspLSPStatsMaxTimeOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSPStatsMaxTimeOccurred.setStatus("mandatory")
_VlanSflspLSPStatsMaxOnQOccurred_Type = TimeTicks
_VlanSflspLSPStatsMaxOnQOccurred_Object = MibScalar
vlanSflspLSPStatsMaxOnQOccurred = _VlanSflspLSPStatsMaxOnQOccurred_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 21, 6),
    _VlanSflspLSPStatsMaxOnQOccurred_Type()
)
vlanSflspLSPStatsMaxOnQOccurred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSPStatsMaxOnQOccurred.setStatus("mandatory")
_VlanSflspLSPStatsTotalSwLinks_Type = Integer32
_VlanSflspLSPStatsTotalSwLinks_Object = MibScalar
vlanSflspLSPStatsTotalSwLinks = _VlanSflspLSPStatsTotalSwLinks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 21, 7),
    _VlanSflspLSPStatsTotalSwLinks_Type()
)
vlanSflspLSPStatsTotalSwLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSPStatsTotalSwLinks.setStatus("mandatory")
_VlanSflspLSPStatsLastChangeDet_Type = TimeTicks
_VlanSflspLSPStatsLastChangeDet_Object = MibScalar
vlanSflspLSPStatsLastChangeDet = _VlanSflspLSPStatsLastChangeDet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 21, 8),
    _VlanSflspLSPStatsLastChangeDet_Type()
)
vlanSflspLSPStatsLastChangeDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSPStatsLastChangeDet.setStatus("mandatory")
_VlanSflspLSPStatsNumSPFRuns_Type = Integer32
_VlanSflspLSPStatsNumSPFRuns_Object = MibScalar
vlanSflspLSPStatsNumSPFRuns = _VlanSflspLSPStatsNumSPFRuns_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 21, 9),
    _VlanSflspLSPStatsNumSPFRuns_Type()
)
vlanSflspLSPStatsNumSPFRuns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSflspLSPStatsNumSPFRuns.setStatus("mandatory")
_VlanSflspLSPStatsNumFULLNbrs_Type = Integer32
_VlanSflspLSPStatsNumFULLNbrs_Object = MibScalar
vlanSflspLSPStatsNumFULLNbrs = _VlanSflspLSPStatsNumFULLNbrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 21, 10),
    _VlanSflspLSPStatsNumFULLNbrs_Type()
)
vlanSflspLSPStatsNumFULLNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSPStatsNumFULLNbrs.setStatus("mandatory")
_VlanSflspLSPStatsNumIntfs_Type = Integer32
_VlanSflspLSPStatsNumIntfs_Object = MibScalar
vlanSflspLSPStatsNumIntfs = _VlanSflspLSPStatsNumIntfs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 21, 11),
    _VlanSflspLSPStatsNumIntfs_Type()
)
vlanSflspLSPStatsNumIntfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSPStatsNumIntfs.setStatus("mandatory")
_VlanSflspLSPStatsNum1stHops_Type = Integer32
_VlanSflspLSPStatsNum1stHops_Object = MibScalar
vlanSflspLSPStatsNum1stHops = _VlanSflspLSPStatsNum1stHops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 21, 12),
    _VlanSflspLSPStatsNum1stHops_Type()
)
vlanSflspLSPStatsNum1stHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSPStatsNum1stHops.setStatus("mandatory")
_VlanSflspLSPStatsNumUpdates_Type = Integer32
_VlanSflspLSPStatsNumUpdates_Object = MibScalar
vlanSflspLSPStatsNumUpdates = _VlanSflspLSPStatsNumUpdates_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 21, 13),
    _VlanSflspLSPStatsNumUpdates_Type()
)
vlanSflspLSPStatsNumUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSPStatsNumUpdates.setStatus("mandatory")
_VlanSflspLSPStatsLastUpdateRecvd_Type = TimeTicks
_VlanSflspLSPStatsLastUpdateRecvd_Object = MibScalar
vlanSflspLSPStatsLastUpdateRecvd = _VlanSflspLSPStatsLastUpdateRecvd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 7, 21, 14),
    _VlanSflspLSPStatsLastUpdateRecvd_Type()
)
vlanSflspLSPStatsLastUpdateRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSflspLSPStatsLastUpdateRecvd.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-SFLSP-MIB",
    **{"SfpsAddress": SfpsAddress,
       "vlanSflspGeneralSwitchID": vlanSflspGeneralSwitchID,
       "vlanSflspGeneralAdminStatus": vlanSflspGeneralAdminStatus,
       "vlanSflspGeneralVersion": vlanSflspGeneralVersion,
       "vlanSflspGeneralAreaBRStatus": vlanSflspGeneralAreaBRStatus,
       "vlanSflspGeneralASBRStatus": vlanSflspGeneralASBRStatus,
       "vlanSflspGeneralTOSSupport": vlanSflspGeneralTOSSupport,
       "vlanSflspGeneralOrgNewLSAs": vlanSflspGeneralOrgNewLSAs,
       "vlanSflspGeneralRcvNewLSAs": vlanSflspGeneralRcvNewLSAs,
       "vlanSflspGeneralMaxOnQueue": vlanSflspGeneralMaxOnQueue,
       "vlanSflspGeneralCurOnQueue": vlanSflspGeneralCurOnQueue,
       "vlanSflspGeneralMaxTimeUs": vlanSflspGeneralMaxTimeUs,
       "vlanSflspGeneralCurTimeUs": vlanSflspGeneralCurTimeUs,
       "vlanSflspGeneralMaxEvents": vlanSflspGeneralMaxEvents,
       "vlanSflspGeneralMaxTimeOccurred": vlanSflspGeneralMaxTimeOccurred,
       "vlanSflspGeneralMaxOnQOccurred": vlanSflspGeneralMaxOnQOccurred,
       "vlanSflspGeneralTotalSwLinks": vlanSflspGeneralTotalSwLinks,
       "vlanSflspGeneralLastChangeDet": vlanSflspGeneralLastChangeDet,
       "vlanSflspGeneralFloodMask": vlanSflspGeneralFloodMask,
       "vlanSflspGeneralLowestMac": vlanSflspGeneralLowestMac,
       "vlanSflspGeneralRootId": vlanSflspGeneralRootId,
       "vlanSflspGeneralFloodAdminStatus": vlanSflspGeneralFloodAdminStatus,
       "vlanSflspLsdbTable": vlanSflspLsdbTable,
       "vlanSflspLsdbEntry": vlanSflspLsdbEntry,
       "vlanSflspLsdbAreaID": vlanSflspLsdbAreaID,
       "vlanSflspLsdbType": vlanSflspLsdbType,
       "vlanSflspLsdbLSID": vlanSflspLsdbLSID,
       "vlanSflspLsdbSwitchID": vlanSflspLsdbSwitchID,
       "vlanSflspLsdbSequence": vlanSflspLsdbSequence,
       "vlanSflspLsdbAge": vlanSflspLsdbAge,
       "vlanSflspLsdbChecksum": vlanSflspLsdbChecksum,
       "vlanSflspLsdbAdvertisement": vlanSflspLsdbAdvertisement,
       "vlanSflspLsdbUsedInSPF": vlanSflspLsdbUsedInSPF,
       "vlanSflspInterfacesTable": vlanSflspInterfacesTable,
       "vlanSflspInterfacesEntry": vlanSflspInterfacesEntry,
       "vlanSflspInterfacesIFAddress": vlanSflspInterfacesIFAddress,
       "vlanSflspInterfacesSwAddressLess": vlanSflspInterfacesSwAddressLess,
       "vlanSflspInterfacesAreaID": vlanSflspInterfacesAreaID,
       "vlanSflspInterfacesIfType": vlanSflspInterfacesIfType,
       "vlanSflspInterfacesAdminStatus": vlanSflspInterfacesAdminStatus,
       "vlanSflspInterfacesSwPriority": vlanSflspInterfacesSwPriority,
       "vlanSflspInterfacesTransDelay": vlanSflspInterfacesTransDelay,
       "vlanSflspInterfacesReTransInterval": vlanSflspInterfacesReTransInterval,
       "vlanSflspInterfacesHelloInterval": vlanSflspInterfacesHelloInterval,
       "vlanSflspInterfacesDeadInterval": vlanSflspInterfacesDeadInterval,
       "vlanSflspInterfacesPollInterval": vlanSflspInterfacesPollInterval,
       "vlanSflspInterfacesState": vlanSflspInterfacesState,
       "vlanSflspInterfacesDS": vlanSflspInterfacesDS,
       "vlanSflspInterfacesBDS": vlanSflspInterfacesBDS,
       "vlanSflspInterfacesEvents": vlanSflspInterfacesEvents,
       "vlanSflspInterfacesAuthKey": vlanSflspInterfacesAuthKey,
       "vlanSflspIfMetricTable": vlanSflspIfMetricTable,
       "vlanSflspIfMetricEntry": vlanSflspIfMetricEntry,
       "vlanSflspIfMetricIfAddress": vlanSflspIfMetricIfAddress,
       "vlanSflspIfMetricIfTOSType": vlanSflspIfMetricIfTOSType,
       "vlanSflspIfMetricIfMetric": vlanSflspIfMetricIfMetric,
       "vlanSflspIfMetricIfStatus": vlanSflspIfMetricIfStatus,
       "vlanSflspNeighborsTable": vlanSflspNeighborsTable,
       "vlanSflspNeighborsEntry": vlanSflspNeighborsEntry,
       "vlanSflspNeighborsPortName": vlanSflspNeighborsPortName,
       "vlanSflspNeighborsSwitchID": vlanSflspNeighborsSwitchID,
       "vlanSflspNeighborsOptions": vlanSflspNeighborsOptions,
       "vlanSflspNeighborsPriority": vlanSflspNeighborsPriority,
       "vlanSflspNeighborsState": vlanSflspNeighborsState,
       "vlanSflspNeighborsEvents": vlanSflspNeighborsEvents,
       "vlanSflspNeighborsLSRetransQLen": vlanSflspNeighborsLSRetransQLen,
       "vlanSflspNeighborsHELLOsRcvd": vlanSflspNeighborsHELLOsRcvd,
       "vlanSflspNeighborsDBDsRcvd": vlanSflspNeighborsDBDsRcvd,
       "vlanSflspNeighborsLSUsRcvd": vlanSflspNeighborsLSUsRcvd,
       "vlanSflspNeighborsLSRsRcvd": vlanSflspNeighborsLSRsRcvd,
       "vlanSflspNeighborsLSACKsRcvd": vlanSflspNeighborsLSACKsRcvd,
       "vlanSflspNeighborsHELLOsSent": vlanSflspNeighborsHELLOsSent,
       "vlanSflspNeighborsDBDsSent": vlanSflspNeighborsDBDsSent,
       "vlanSflspNeighborsLSUsSent": vlanSflspNeighborsLSUsSent,
       "vlanSflspNeighborsLSRsSent": vlanSflspNeighborsLSRsSent,
       "vlanSflspNeighborsLSACKsSent": vlanSflspNeighborsLSACKsSent,
       "vlanSflspNeighborsNBMAStatus": vlanSflspNeighborsNBMAStatus,
       "vlanSflspNeighborsFULLTimeSec": vlanSflspNeighborsFULLTimeSec,
       "vlanSflspAreaTable": vlanSflspAreaTable,
       "vlanSflspAreaEntry": vlanSflspAreaEntry,
       "vlanSflspAreaAreaID": vlanSflspAreaAreaID,
       "vlanSflspAreaAuthType": vlanSflspAreaAuthType,
       "vlanSflspAreaSPFRuns": vlanSflspAreaSPFRuns,
       "vlanSflspAreaABRCount": vlanSflspAreaABRCount,
       "vlanSflspAreaASBRCount": vlanSflspAreaASBRCount,
       "vlanSflspAreaAreaLSACnt": vlanSflspAreaAreaLSACnt,
       "vlanSflspAreaAreaCheckSum": vlanSflspAreaAreaCheckSum,
       "vlanSflspAreaLastSpfRun": vlanSflspAreaLastSpfRun,
       "vlanSflsp1stHopTable": vlanSflsp1stHopTable,
       "vlanSflsp1stHopEntry": vlanSflsp1stHopEntry,
       "vlanSflsp1stHopDestSwitch": vlanSflsp1stHopDestSwitch,
       "vlanSflsp1stHopPath11stHop": vlanSflsp1stHopPath11stHop,
       "vlanSflsp1stHopPath21stHop": vlanSflsp1stHopPath21stHop,
       "vlanSflsp1stHopPath31stHop": vlanSflsp1stHopPath31stHop,
       "vlanSflspTracePathAPIDest": vlanSflspTracePathAPIDest,
       "vlanSflspTracePathAPIID": vlanSflspTracePathAPIID,
       "vlanSflspTracePathAPIType": vlanSflspTracePathAPIType,
       "vlanSflspTracePathAPIAction": vlanSflspTracePathAPIAction,
       "vlanSflspTracePathTable": vlanSflspTracePathTable,
       "vlanSflspTracePathEntry": vlanSflspTracePathEntry,
       "vlanSflspTracePathDest": vlanSflspTracePathDest,
       "vlanSflspTracePathID": vlanSflspTracePathID,
       "vlanSflspTracePathAction": vlanSflspTracePathAction,
       "vlanSflspTracePathStatus": vlanSflspTracePathStatus,
       "vlanSflspTracePathListTable": vlanSflspTracePathListTable,
       "vlanSflspTracePathListEntry": vlanSflspTracePathListEntry,
       "vlanSflspTracePathListDest": vlanSflspTracePathListDest,
       "vlanSflspTracePathListID": vlanSflspTracePathListID,
       "vlanSflspTracePathListPathNum": vlanSflspTracePathListPathNum,
       "vlanSflspTracePathListHopNum": vlanSflspTracePathListHopNum,
       "vlanSflspTracePathListHopAddr": vlanSflspTracePathListHopAddr,
       "vlanSflspLSDBFloodTable": vlanSflspLSDBFloodTable,
       "vlanSflspLSDBFloodEntry": vlanSflspLSDBFloodEntry,
       "vlanSflspLSDBFloodAreaID": vlanSflspLSDBFloodAreaID,
       "vlanSflspLSDBFloodType": vlanSflspLSDBFloodType,
       "vlanSflspLSDBFloodLSID": vlanSflspLSDBFloodLSID,
       "vlanSflspLSDBFloodAdvSwitchID": vlanSflspLSDBFloodAdvSwitchID,
       "vlanSflspLSDBFloodSequence": vlanSflspLSDBFloodSequence,
       "vlanSflspLSDBFloodAge": vlanSflspLSDBFloodAge,
       "vlanSflspLSDBFloodChecksum": vlanSflspLSDBFloodChecksum,
       "vlanSflspLSDBFloodAdvertisement": vlanSflspLSDBFloodAdvertisement,
       "vlanSflspLSDBFloodUsedInSPF": vlanSflspLSDBFloodUsedInSPF,
       "vlanSflspLSDBFloodEverUsed": vlanSflspLSDBFloodEverUsed,
       "vlanSflspLSPStatsMaxOnQueue": vlanSflspLSPStatsMaxOnQueue,
       "vlanSflspLSPStatsCurOnQueue": vlanSflspLSPStatsCurOnQueue,
       "vlanSflspLSPStatsMaxTimeUs": vlanSflspLSPStatsMaxTimeUs,
       "vlanSflspLSPStatsCurTimeUs": vlanSflspLSPStatsCurTimeUs,
       "vlanSflspLSPStatsMaxTimeOccurred": vlanSflspLSPStatsMaxTimeOccurred,
       "vlanSflspLSPStatsMaxOnQOccurred": vlanSflspLSPStatsMaxOnQOccurred,
       "vlanSflspLSPStatsTotalSwLinks": vlanSflspLSPStatsTotalSwLinks,
       "vlanSflspLSPStatsLastChangeDet": vlanSflspLSPStatsLastChangeDet,
       "vlanSflspLSPStatsNumSPFRuns": vlanSflspLSPStatsNumSPFRuns,
       "vlanSflspLSPStatsNumFULLNbrs": vlanSflspLSPStatsNumFULLNbrs,
       "vlanSflspLSPStatsNumIntfs": vlanSflspLSPStatsNumIntfs,
       "vlanSflspLSPStatsNum1stHops": vlanSflspLSPStatsNum1stHops,
       "vlanSflspLSPStatsNumUpdates": vlanSflspLSPStatsNumUpdates,
       "vlanSflspLSPStatsLastUpdateRecvd": vlanSflspLSPStatsLastUpdateRecvd}
)
