# SNMP MIB module (AVICI-MODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVICI-MODULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:43 2024
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

(aviciBayIndex,
 aviciSlotIndex) = mibBuilder.importSymbols(
    "AVICI-BAY-MIB",
    "aviciBayIndex",
    "aviciSlotIndex")

(aviciMibs,) = mibBuilder.importSymbols(
    "AVICI-SMI",
    "aviciMibs")

(aviciSysTrapDescr,) = mibBuilder.importSymbols(
    "AVICI-SYSTEM-MIB",
    "aviciSysTrapDescr")

(AviciHighAvailabilityType,
 AviciPartNumberType,
 AviciProductIdType,
 AviciRevisionType,
 AviciSerialNumberType) = mibBuilder.importSymbols(
    "AVICI-TC",
    "AviciHighAvailabilityType",
    "AviciPartNumberType",
    "AviciProductIdType",
    "AviciRevisionType",
    "AviciSerialNumberType")

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

aviciModuleMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5)
)
aviciModuleMIB.setRevisions(
        ("1970-01-01 00:00",
         "0003-03-18 12:00",
         "1970-01-01 00:00",
         "1970-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AviciModuleObjects_ObjectIdentity = ObjectIdentity
aviciModuleObjects = _AviciModuleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1)
)
_AviciModuleTable_Object = MibTable
aviciModuleTable = _AviciModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    aviciModuleTable.setStatus("current")
_AviciModuleEntry_Object = MibTableRow
aviciModuleEntry = _AviciModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1)
)
aviciModuleEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciSlotIndex"),
)
if mibBuilder.loadTexts:
    aviciModuleEntry.setStatus("current")


class _AviciModuleAdminStatus_Type(Integer32):
    """Custom type aviciModuleAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AviciModuleAdminStatus_Type.__name__ = "Integer32"
_AviciModuleAdminStatus_Object = MibTableColumn
aviciModuleAdminStatus = _AviciModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 1),
    _AviciModuleAdminStatus_Type()
)
aviciModuleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviciModuleAdminStatus.setStatus("current")


class _AviciModuleOperStatus_Type(Integer32):
    """Custom type aviciModuleOperStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("failed", 6),
          ("incompatibleSW", 8),
          ("misconfigured", 7),
          ("testing", 5),
          ("unconfigured", 3),
          ("unknown", 4),
          ("up", 1),
          ("upgrading", 9))
    )


_AviciModuleOperStatus_Type.__name__ = "Integer32"
_AviciModuleOperStatus_Object = MibTableColumn
aviciModuleOperStatus = _AviciModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 2),
    _AviciModuleOperStatus_Type()
)
aviciModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleOperStatus.setStatus("current")
_AviciModuleUpTime_Type = TimeTicks
_AviciModuleUpTime_Object = MibTableColumn
aviciModuleUpTime = _AviciModuleUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 3),
    _AviciModuleUpTime_Type()
)
aviciModuleUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleUpTime.setStatus("current")
_AviciModuleCurrTemp_Type = Integer32
_AviciModuleCurrTemp_Object = MibTableColumn
aviciModuleCurrTemp = _AviciModuleCurrTemp_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 4),
    _AviciModuleCurrTemp_Type()
)
aviciModuleCurrTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleCurrTemp.setStatus("current")
_AviciModuleMaxTemp_Type = Gauge32
_AviciModuleMaxTemp_Object = MibTableColumn
aviciModuleMaxTemp = _AviciModuleMaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 5),
    _AviciModuleMaxTemp_Type()
)
aviciModuleMaxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleMaxTemp.setStatus("current")


class _AviciModuleDescr_Type(DisplayString):
    """Custom type aviciModuleDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AviciModuleDescr_Type.__name__ = "DisplayString"
_AviciModuleDescr_Object = MibTableColumn
aviciModuleDescr = _AviciModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 6),
    _AviciModuleDescr_Type()
)
aviciModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleDescr.setStatus("current")
_AviciModuleAssySerialNumber_Type = AviciSerialNumberType
_AviciModuleAssySerialNumber_Object = MibTableColumn
aviciModuleAssySerialNumber = _AviciModuleAssySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 7),
    _AviciModuleAssySerialNumber_Type()
)
aviciModuleAssySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleAssySerialNumber.setStatus("current")
_AviciModuleLineSerialNumber_Type = AviciSerialNumberType
_AviciModuleLineSerialNumber_Object = MibTableColumn
aviciModuleLineSerialNumber = _AviciModuleLineSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 8),
    _AviciModuleLineSerialNumber_Type()
)
aviciModuleLineSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleLineSerialNumber.setStatus("current")
_AviciModuleMbSerialNumber_Type = AviciSerialNumberType
_AviciModuleMbSerialNumber_Object = MibTableColumn
aviciModuleMbSerialNumber = _AviciModuleMbSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 9),
    _AviciModuleMbSerialNumber_Type()
)
aviciModuleMbSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleMbSerialNumber.setStatus("current")
_AviciModuleAssyRevision_Type = AviciRevisionType
_AviciModuleAssyRevision_Object = MibTableColumn
aviciModuleAssyRevision = _AviciModuleAssyRevision_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 10),
    _AviciModuleAssyRevision_Type()
)
aviciModuleAssyRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleAssyRevision.setStatus("current")
_AviciModuleLineRevision_Type = AviciRevisionType
_AviciModuleLineRevision_Object = MibTableColumn
aviciModuleLineRevision = _AviciModuleLineRevision_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 11),
    _AviciModuleLineRevision_Type()
)
aviciModuleLineRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleLineRevision.setStatus("current")
_AviciModuleMbRevision_Type = AviciRevisionType
_AviciModuleMbRevision_Object = MibTableColumn
aviciModuleMbRevision = _AviciModuleMbRevision_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 12),
    _AviciModuleMbRevision_Type()
)
aviciModuleMbRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleMbRevision.setStatus("current")


class _AviciModuleSoftwareVersion_Type(DisplayString):
    """Custom type aviciModuleSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AviciModuleSoftwareVersion_Type.__name__ = "DisplayString"
_AviciModuleSoftwareVersion_Object = MibTableColumn
aviciModuleSoftwareVersion = _AviciModuleSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 13),
    _AviciModuleSoftwareVersion_Type()
)
aviciModuleSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleSoftwareVersion.setStatus("current")


class _AviciModuleFirmwareVersion_Type(DisplayString):
    """Custom type aviciModuleFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AviciModuleFirmwareVersion_Type.__name__ = "DisplayString"
_AviciModuleFirmwareVersion_Object = MibTableColumn
aviciModuleFirmwareVersion = _AviciModuleFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 14),
    _AviciModuleFirmwareVersion_Type()
)
aviciModuleFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleFirmwareVersion.setStatus("current")
_AviciModuleAssyProductId_Type = AviciProductIdType
_AviciModuleAssyProductId_Object = MibTableColumn
aviciModuleAssyProductId = _AviciModuleAssyProductId_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 15),
    _AviciModuleAssyProductId_Type()
)
aviciModuleAssyProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleAssyProductId.setStatus("current")
_AviciModuleLinePartNumber_Type = AviciPartNumberType
_AviciModuleLinePartNumber_Object = MibTableColumn
aviciModuleLinePartNumber = _AviciModuleLinePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 16),
    _AviciModuleLinePartNumber_Type()
)
aviciModuleLinePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleLinePartNumber.setStatus("current")
_AviciModuleMbPartNumber_Type = AviciPartNumberType
_AviciModuleMbPartNumber_Object = MibTableColumn
aviciModuleMbPartNumber = _AviciModuleMbPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 1, 1, 17),
    _AviciModuleMbPartNumber_Type()
)
aviciModuleMbPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleMbPartNumber.setStatus("current")
_AviciModuleIpTable_Object = MibTable
aviciModuleIpTable = _AviciModuleIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    aviciModuleIpTable.setStatus("current")
_AviciModuleIpEntry_Object = MibTableRow
aviciModuleIpEntry = _AviciModuleIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 2, 1)
)
aviciModuleIpEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciSlotIndex"),
)
if mibBuilder.loadTexts:
    aviciModuleIpEntry.setStatus("current")
_AviciModuleIpInReceives_Type = Counter64
_AviciModuleIpInReceives_Object = MibTableColumn
aviciModuleIpInReceives = _AviciModuleIpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 2, 1, 1),
    _AviciModuleIpInReceives_Type()
)
aviciModuleIpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIpInReceives.setStatus("current")
_AviciModuleIpInHdrErrors_Type = Counter64
_AviciModuleIpInHdrErrors_Object = MibTableColumn
aviciModuleIpInHdrErrors = _AviciModuleIpInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 2, 1, 2),
    _AviciModuleIpInHdrErrors_Type()
)
aviciModuleIpInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIpInHdrErrors.setStatus("current")
_AviciModuleIpInAddrErrors_Type = Counter64
_AviciModuleIpInAddrErrors_Object = MibTableColumn
aviciModuleIpInAddrErrors = _AviciModuleIpInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 2, 1, 3),
    _AviciModuleIpInAddrErrors_Type()
)
aviciModuleIpInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIpInAddrErrors.setStatus("current")
_AviciModuleIpForwDatagrams_Type = Counter64
_AviciModuleIpForwDatagrams_Object = MibTableColumn
aviciModuleIpForwDatagrams = _AviciModuleIpForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 2, 1, 4),
    _AviciModuleIpForwDatagrams_Type()
)
aviciModuleIpForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIpForwDatagrams.setStatus("current")
_AviciModuleIpInUnknownProtos_Type = Counter64
_AviciModuleIpInUnknownProtos_Object = MibTableColumn
aviciModuleIpInUnknownProtos = _AviciModuleIpInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 2, 1, 5),
    _AviciModuleIpInUnknownProtos_Type()
)
aviciModuleIpInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIpInUnknownProtos.setStatus("current")
_AviciModuleIpInDiscards_Type = Counter64
_AviciModuleIpInDiscards_Object = MibTableColumn
aviciModuleIpInDiscards = _AviciModuleIpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 2, 1, 6),
    _AviciModuleIpInDiscards_Type()
)
aviciModuleIpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIpInDiscards.setStatus("current")
_AviciModuleIpInDelivers_Type = Counter64
_AviciModuleIpInDelivers_Object = MibTableColumn
aviciModuleIpInDelivers = _AviciModuleIpInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 2, 1, 7),
    _AviciModuleIpInDelivers_Type()
)
aviciModuleIpInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIpInDelivers.setStatus("current")
_AviciModuleIpOutRequests_Type = Counter64
_AviciModuleIpOutRequests_Object = MibTableColumn
aviciModuleIpOutRequests = _AviciModuleIpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 2, 1, 8),
    _AviciModuleIpOutRequests_Type()
)
aviciModuleIpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIpOutRequests.setStatus("current")
_AviciModuleIpOutDiscards_Type = Counter64
_AviciModuleIpOutDiscards_Object = MibTableColumn
aviciModuleIpOutDiscards = _AviciModuleIpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 2, 1, 9),
    _AviciModuleIpOutDiscards_Type()
)
aviciModuleIpOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIpOutDiscards.setStatus("current")
_AviciModuleIpOutNoRoutes_Type = Counter64
_AviciModuleIpOutNoRoutes_Object = MibTableColumn
aviciModuleIpOutNoRoutes = _AviciModuleIpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 2, 1, 10),
    _AviciModuleIpOutNoRoutes_Type()
)
aviciModuleIpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIpOutNoRoutes.setStatus("current")
_AviciModuleIpFragOKs_Type = Counter64
_AviciModuleIpFragOKs_Object = MibTableColumn
aviciModuleIpFragOKs = _AviciModuleIpFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 2, 1, 11),
    _AviciModuleIpFragOKs_Type()
)
aviciModuleIpFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIpFragOKs.setStatus("current")
_AviciModuleIpFragFails_Type = Counter64
_AviciModuleIpFragFails_Object = MibTableColumn
aviciModuleIpFragFails = _AviciModuleIpFragFails_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 2, 1, 12),
    _AviciModuleIpFragFails_Type()
)
aviciModuleIpFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIpFragFails.setStatus("current")
_AviciModuleIpFragCreates_Type = Counter64
_AviciModuleIpFragCreates_Object = MibTableColumn
aviciModuleIpFragCreates = _AviciModuleIpFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 2, 1, 13),
    _AviciModuleIpFragCreates_Type()
)
aviciModuleIpFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIpFragCreates.setStatus("current")
_AviciModuleIcmpTable_Object = MibTable
aviciModuleIcmpTable = _AviciModuleIcmpTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    aviciModuleIcmpTable.setStatus("current")
_AviciModuleIcmpEntry_Object = MibTableRow
aviciModuleIcmpEntry = _AviciModuleIcmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1)
)
aviciModuleIcmpEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciSlotIndex"),
)
if mibBuilder.loadTexts:
    aviciModuleIcmpEntry.setStatus("current")
_AviciModuleIcmpInMsgs_Type = Counter64
_AviciModuleIcmpInMsgs_Object = MibTableColumn
aviciModuleIcmpInMsgs = _AviciModuleIcmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 1),
    _AviciModuleIcmpInMsgs_Type()
)
aviciModuleIcmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpInMsgs.setStatus("current")
_AviciModuleIcmpInErrors_Type = Counter64
_AviciModuleIcmpInErrors_Object = MibTableColumn
aviciModuleIcmpInErrors = _AviciModuleIcmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 2),
    _AviciModuleIcmpInErrors_Type()
)
aviciModuleIcmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpInErrors.setStatus("current")
_AviciModuleIcmpInDestUnreachs_Type = Counter64
_AviciModuleIcmpInDestUnreachs_Object = MibTableColumn
aviciModuleIcmpInDestUnreachs = _AviciModuleIcmpInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 3),
    _AviciModuleIcmpInDestUnreachs_Type()
)
aviciModuleIcmpInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpInDestUnreachs.setStatus("current")
_AviciModuleIcmpInTimeExcds_Type = Counter64
_AviciModuleIcmpInTimeExcds_Object = MibTableColumn
aviciModuleIcmpInTimeExcds = _AviciModuleIcmpInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 4),
    _AviciModuleIcmpInTimeExcds_Type()
)
aviciModuleIcmpInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpInTimeExcds.setStatus("current")
_AviciModuleIcmpInParmProbs_Type = Counter64
_AviciModuleIcmpInParmProbs_Object = MibTableColumn
aviciModuleIcmpInParmProbs = _AviciModuleIcmpInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 5),
    _AviciModuleIcmpInParmProbs_Type()
)
aviciModuleIcmpInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpInParmProbs.setStatus("current")
_AviciModuleIcmpInSrcQuenchs_Type = Counter64
_AviciModuleIcmpInSrcQuenchs_Object = MibTableColumn
aviciModuleIcmpInSrcQuenchs = _AviciModuleIcmpInSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 6),
    _AviciModuleIcmpInSrcQuenchs_Type()
)
aviciModuleIcmpInSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpInSrcQuenchs.setStatus("current")
_AviciModuleIcmpInRedirects_Type = Counter64
_AviciModuleIcmpInRedirects_Object = MibTableColumn
aviciModuleIcmpInRedirects = _AviciModuleIcmpInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 7),
    _AviciModuleIcmpInRedirects_Type()
)
aviciModuleIcmpInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpInRedirects.setStatus("current")
_AviciModuleIcmpInEchos_Type = Counter64
_AviciModuleIcmpInEchos_Object = MibTableColumn
aviciModuleIcmpInEchos = _AviciModuleIcmpInEchos_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 8),
    _AviciModuleIcmpInEchos_Type()
)
aviciModuleIcmpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpInEchos.setStatus("current")
_AviciModuleIcmpInEchoReps_Type = Counter64
_AviciModuleIcmpInEchoReps_Object = MibTableColumn
aviciModuleIcmpInEchoReps = _AviciModuleIcmpInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 9),
    _AviciModuleIcmpInEchoReps_Type()
)
aviciModuleIcmpInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpInEchoReps.setStatus("current")
_AviciModuleIcmpInTimestamps_Type = Counter64
_AviciModuleIcmpInTimestamps_Object = MibTableColumn
aviciModuleIcmpInTimestamps = _AviciModuleIcmpInTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 10),
    _AviciModuleIcmpInTimestamps_Type()
)
aviciModuleIcmpInTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpInTimestamps.setStatus("current")
_AviciModuleIcmpInTimestampReps_Type = Counter64
_AviciModuleIcmpInTimestampReps_Object = MibTableColumn
aviciModuleIcmpInTimestampReps = _AviciModuleIcmpInTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 11),
    _AviciModuleIcmpInTimestampReps_Type()
)
aviciModuleIcmpInTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpInTimestampReps.setStatus("current")
_AviciModuleIcmpInAddrMasks_Type = Counter64
_AviciModuleIcmpInAddrMasks_Object = MibTableColumn
aviciModuleIcmpInAddrMasks = _AviciModuleIcmpInAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 12),
    _AviciModuleIcmpInAddrMasks_Type()
)
aviciModuleIcmpInAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpInAddrMasks.setStatus("current")
_AviciModuleIcmpInAddrMaskReps_Type = Counter64
_AviciModuleIcmpInAddrMaskReps_Object = MibTableColumn
aviciModuleIcmpInAddrMaskReps = _AviciModuleIcmpInAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 13),
    _AviciModuleIcmpInAddrMaskReps_Type()
)
aviciModuleIcmpInAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpInAddrMaskReps.setStatus("current")
_AviciModuleIcmpOutMsgs_Type = Counter64
_AviciModuleIcmpOutMsgs_Object = MibTableColumn
aviciModuleIcmpOutMsgs = _AviciModuleIcmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 14),
    _AviciModuleIcmpOutMsgs_Type()
)
aviciModuleIcmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpOutMsgs.setStatus("current")
_AviciModuleIcmpOutErrors_Type = Counter64
_AviciModuleIcmpOutErrors_Object = MibTableColumn
aviciModuleIcmpOutErrors = _AviciModuleIcmpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 15),
    _AviciModuleIcmpOutErrors_Type()
)
aviciModuleIcmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpOutErrors.setStatus("current")
_AviciModuleIcmpOutDestUnreachs_Type = Counter64
_AviciModuleIcmpOutDestUnreachs_Object = MibTableColumn
aviciModuleIcmpOutDestUnreachs = _AviciModuleIcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 16),
    _AviciModuleIcmpOutDestUnreachs_Type()
)
aviciModuleIcmpOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpOutDestUnreachs.setStatus("current")
_AviciModuleIcmpOutTimeExcds_Type = Counter64
_AviciModuleIcmpOutTimeExcds_Object = MibTableColumn
aviciModuleIcmpOutTimeExcds = _AviciModuleIcmpOutTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 17),
    _AviciModuleIcmpOutTimeExcds_Type()
)
aviciModuleIcmpOutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpOutTimeExcds.setStatus("current")
_AviciModuleIcmpOutParmProbs_Type = Counter64
_AviciModuleIcmpOutParmProbs_Object = MibTableColumn
aviciModuleIcmpOutParmProbs = _AviciModuleIcmpOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 18),
    _AviciModuleIcmpOutParmProbs_Type()
)
aviciModuleIcmpOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpOutParmProbs.setStatus("current")
_AviciModuleIcmpOutSrcQuenchs_Type = Counter64
_AviciModuleIcmpOutSrcQuenchs_Object = MibTableColumn
aviciModuleIcmpOutSrcQuenchs = _AviciModuleIcmpOutSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 19),
    _AviciModuleIcmpOutSrcQuenchs_Type()
)
aviciModuleIcmpOutSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpOutSrcQuenchs.setStatus("current")
_AviciModuleIcmpOutRedirects_Type = Counter64
_AviciModuleIcmpOutRedirects_Object = MibTableColumn
aviciModuleIcmpOutRedirects = _AviciModuleIcmpOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 20),
    _AviciModuleIcmpOutRedirects_Type()
)
aviciModuleIcmpOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpOutRedirects.setStatus("current")
_AviciModuleIcmpOutEchos_Type = Counter64
_AviciModuleIcmpOutEchos_Object = MibTableColumn
aviciModuleIcmpOutEchos = _AviciModuleIcmpOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 21),
    _AviciModuleIcmpOutEchos_Type()
)
aviciModuleIcmpOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpOutEchos.setStatus("current")
_AviciModuleIcmpOutEchoReps_Type = Counter64
_AviciModuleIcmpOutEchoReps_Object = MibTableColumn
aviciModuleIcmpOutEchoReps = _AviciModuleIcmpOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 22),
    _AviciModuleIcmpOutEchoReps_Type()
)
aviciModuleIcmpOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpOutEchoReps.setStatus("current")
_AviciModuleIcmpOutTimestamps_Type = Counter64
_AviciModuleIcmpOutTimestamps_Object = MibTableColumn
aviciModuleIcmpOutTimestamps = _AviciModuleIcmpOutTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 23),
    _AviciModuleIcmpOutTimestamps_Type()
)
aviciModuleIcmpOutTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpOutTimestamps.setStatus("current")
_AviciModuleIcmpOutTimestampReps_Type = Counter64
_AviciModuleIcmpOutTimestampReps_Object = MibTableColumn
aviciModuleIcmpOutTimestampReps = _AviciModuleIcmpOutTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 24),
    _AviciModuleIcmpOutTimestampReps_Type()
)
aviciModuleIcmpOutTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpOutTimestampReps.setStatus("current")
_AviciModuleIcmpOutAddrMasks_Type = Counter64
_AviciModuleIcmpOutAddrMasks_Object = MibTableColumn
aviciModuleIcmpOutAddrMasks = _AviciModuleIcmpOutAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 25),
    _AviciModuleIcmpOutAddrMasks_Type()
)
aviciModuleIcmpOutAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpOutAddrMasks.setStatus("current")
_AviciModuleIcmpOutAddrMaskReps_Type = Counter64
_AviciModuleIcmpOutAddrMaskReps_Object = MibTableColumn
aviciModuleIcmpOutAddrMaskReps = _AviciModuleIcmpOutAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 3, 1, 26),
    _AviciModuleIcmpOutAddrMaskReps_Type()
)
aviciModuleIcmpOutAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciModuleIcmpOutAddrMaskReps.setStatus("current")
_AviciServerAccessModuleTable_Object = MibTable
aviciServerAccessModuleTable = _AviciServerAccessModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    aviciServerAccessModuleTable.setStatus("current")
_AviciServerAccessModuleEntry_Object = MibTableRow
aviciServerAccessModuleEntry = _AviciServerAccessModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 4, 1)
)
aviciServerAccessModuleEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciSlotIndex"),
)
if mibBuilder.loadTexts:
    aviciServerAccessModuleEntry.setStatus("current")
_AviciServerAccessModuleType_Type = AviciHighAvailabilityType
_AviciServerAccessModuleType_Object = MibTableColumn
aviciServerAccessModuleType = _AviciServerAccessModuleType_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 4, 1, 1),
    _AviciServerAccessModuleType_Type()
)
aviciServerAccessModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciServerAccessModuleType.setStatus("current")


class _AviciServerAccessModuleLinkStatus_Type(Integer32):
    """Custom type aviciServerAccessModuleLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AviciServerAccessModuleLinkStatus_Type.__name__ = "Integer32"
_AviciServerAccessModuleLinkStatus_Object = MibTableColumn
aviciServerAccessModuleLinkStatus = _AviciServerAccessModuleLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 4, 1, 2),
    _AviciServerAccessModuleLinkStatus_Type()
)
aviciServerAccessModuleLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciServerAccessModuleLinkStatus.setStatus("current")
_AviciServerAccessModuleNumTransitions_Type = Gauge32
_AviciServerAccessModuleNumTransitions_Object = MibTableColumn
aviciServerAccessModuleNumTransitions = _AviciServerAccessModuleNumTransitions_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 4, 1, 3),
    _AviciServerAccessModuleNumTransitions_Type()
)
aviciServerAccessModuleNumTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciServerAccessModuleNumTransitions.setStatus("current")
_AviciServerAccessModuleLastTransition_Type = TimeTicks
_AviciServerAccessModuleLastTransition_Object = MibTableColumn
aviciServerAccessModuleLastTransition = _AviciServerAccessModuleLastTransition_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 1, 4, 1, 4),
    _AviciServerAccessModuleLastTransition_Type()
)
aviciServerAccessModuleLastTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciServerAccessModuleLastTransition.setStatus("current")
_AviciModuleNotifications_ObjectIdentity = ObjectIdentity
aviciModuleNotifications = _AviciModuleNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 2)
)
_AviciModuleNotificationPrefix_ObjectIdentity = ObjectIdentity
aviciModuleNotificationPrefix = _AviciModuleNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 2, 0)
)
_AviciModuleMIBConformance_ObjectIdentity = ObjectIdentity
aviciModuleMIBConformance = _AviciModuleMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 3)
)
_AviciModuleMIBCompliances_ObjectIdentity = ObjectIdentity
aviciModuleMIBCompliances = _AviciModuleMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 3, 1)
)
_AviciModuleMIBGroups_ObjectIdentity = ObjectIdentity
aviciModuleMIBGroups = _AviciModuleMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 3, 2)
)
_AviciServerAccessModuleNotifications_ObjectIdentity = ObjectIdentity
aviciServerAccessModuleNotifications = _AviciServerAccessModuleNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 4)
)
_AviciServerAccessModuleNotificationPrefix_ObjectIdentity = ObjectIdentity
aviciServerAccessModuleNotificationPrefix = _AviciServerAccessModuleNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 4, 0)
)

# Managed Objects groups

aviciModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 3, 2, 1)
)
aviciModuleGroup.setObjects(
      *(("AVICI-MODULE-MIB", "aviciModuleAdminStatus"),
        ("AVICI-MODULE-MIB", "aviciModuleOperStatus"),
        ("AVICI-MODULE-MIB", "aviciModuleUpTime"),
        ("AVICI-MODULE-MIB", "aviciModuleCurrTemp"),
        ("AVICI-MODULE-MIB", "aviciModuleMaxTemp"),
        ("AVICI-MODULE-MIB", "aviciModuleDescr"),
        ("AVICI-MODULE-MIB", "aviciModuleAssySerialNumber"),
        ("AVICI-MODULE-MIB", "aviciModuleLineSerialNumber"),
        ("AVICI-MODULE-MIB", "aviciModuleMbSerialNumber"),
        ("AVICI-MODULE-MIB", "aviciModuleAssyRevision"),
        ("AVICI-MODULE-MIB", "aviciModuleLineRevision"),
        ("AVICI-MODULE-MIB", "aviciModuleMbRevision"),
        ("AVICI-MODULE-MIB", "aviciModuleSoftwareVersion"),
        ("AVICI-MODULE-MIB", "aviciModuleFirmwareVersion"),
        ("AVICI-MODULE-MIB", "aviciModuleAssyProductId"),
        ("AVICI-MODULE-MIB", "aviciModuleLinePartNumber"),
        ("AVICI-MODULE-MIB", "aviciModuleMbPartNumber"))
)
if mibBuilder.loadTexts:
    aviciModuleGroup.setStatus("current")

aviciModuleIpCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 3, 2, 2)
)
aviciModuleIpCountersGroup.setObjects(
      *(("AVICI-MODULE-MIB", "aviciModuleIpInReceives"),
        ("AVICI-MODULE-MIB", "aviciModuleIpInHdrErrors"),
        ("AVICI-MODULE-MIB", "aviciModuleIpInAddrErrors"),
        ("AVICI-MODULE-MIB", "aviciModuleIpForwDatagrams"),
        ("AVICI-MODULE-MIB", "aviciModuleIpInUnknownProtos"),
        ("AVICI-MODULE-MIB", "aviciModuleIpInDiscards"),
        ("AVICI-MODULE-MIB", "aviciModuleIpInDelivers"),
        ("AVICI-MODULE-MIB", "aviciModuleIpOutRequests"),
        ("AVICI-MODULE-MIB", "aviciModuleIpOutDiscards"),
        ("AVICI-MODULE-MIB", "aviciModuleIpOutNoRoutes"),
        ("AVICI-MODULE-MIB", "aviciModuleIpFragOKs"),
        ("AVICI-MODULE-MIB", "aviciModuleIpFragFails"),
        ("AVICI-MODULE-MIB", "aviciModuleIpFragCreates"))
)
if mibBuilder.loadTexts:
    aviciModuleIpCountersGroup.setStatus("current")

aviciModuleIcmpCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 3, 2, 3)
)
aviciModuleIcmpCountersGroup.setObjects(
      *(("AVICI-MODULE-MIB", "aviciModuleIcmpInMsgs"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpInErrors"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpInDestUnreachs"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpInTimeExcds"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpInParmProbs"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpInSrcQuenchs"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpInRedirects"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpInEchos"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpInEchoReps"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpInTimestamps"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpInTimestampReps"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpInAddrMasks"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpInAddrMaskReps"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpOutMsgs"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpOutErrors"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpOutDestUnreachs"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpOutTimeExcds"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpOutParmProbs"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpOutSrcQuenchs"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpOutRedirects"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpOutEchos"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpOutEchoReps"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpOutTimestamps"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpOutTimestampReps"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpOutAddrMasks"),
        ("AVICI-MODULE-MIB", "aviciModuleIcmpOutAddrMaskReps"))
)
if mibBuilder.loadTexts:
    aviciModuleIcmpCountersGroup.setStatus("current")


# Notification objects

aviciModuleColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 2, 0, 1)
)
aviciModuleColdStart.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciSlotIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciModuleColdStart.setStatus(
        "current"
    )

aviciModuleWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 2, 0, 2)
)
aviciModuleWarmStart.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciSlotIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciModuleWarmStart.setStatus(
        "current"
    )

aviciModuleDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 2, 0, 3)
)
aviciModuleDown.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciSlotIndex"),
        ("AVICI-MODULE-MIB", "aviciModuleAdminStatus"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciModuleDown.setStatus(
        "current"
    )

aviciModuleTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 2, 0, 4)
)
aviciModuleTemperatureNormal.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciSlotIndex"),
        ("AVICI-MODULE-MIB", "aviciModuleCurrTemp"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciModuleTemperatureNormal.setStatus(
        "current"
    )

aviciModuleTemperatureMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 2, 0, 5)
)
aviciModuleTemperatureMinor.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciSlotIndex"),
        ("AVICI-MODULE-MIB", "aviciModuleCurrTemp"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciModuleTemperatureMinor.setStatus(
        "current"
    )

aviciModuleTemperatureMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 2, 0, 6)
)
aviciModuleTemperatureMajor.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciSlotIndex"),
        ("AVICI-MODULE-MIB", "aviciModuleCurrTemp"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciModuleTemperatureMajor.setStatus(
        "current"
    )

aviciModuleTemperatureCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 2, 0, 7)
)
aviciModuleTemperatureCritical.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciSlotIndex"),
        ("AVICI-MODULE-MIB", "aviciModuleCurrTemp"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciModuleTemperatureCritical.setStatus(
        "current"
    )

aviciModuleMisconfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 2, 0, 8)
)
aviciModuleMisconfigured.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciSlotIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciModuleMisconfigured.setStatus(
        "current"
    )

aviciModuleIncompatibleSW = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 2, 0, 9)
)
aviciModuleIncompatibleSW.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciSlotIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciModuleIncompatibleSW.setStatus(
        "current"
    )

aviciServerAccessModuleDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 4, 0, 1)
)
aviciServerAccessModuleDown.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciSlotIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciServerAccessModuleDown.setStatus(
        "current"
    )

aviciServerAccessModuleUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 4, 0, 2)
)
aviciServerAccessModuleUp.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciSlotIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciServerAccessModuleUp.setStatus(
        "current"
    )

aviciAllServerAccessModulesDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 4, 0, 3)
)
aviciAllServerAccessModulesDown.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciSlotIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciAllServerAccessModulesDown.setStatus(
        "current"
    )

aviciAllServerAccessModulesDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 4, 0, 4)
)
aviciAllServerAccessModulesDownClear.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciSlotIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciAllServerAccessModulesDownClear.setStatus(
        "current"
    )


# Notifications groups

aviciModuleNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 3, 2, 4)
)
aviciModuleNotificationGroup.setObjects(
      *(("AVICI-MODULE-MIB", "aviciModuleColdStart"),
        ("AVICI-MODULE-MIB", "aviciModuleWarmStart"),
        ("AVICI-MODULE-MIB", "aviciModuleDown"),
        ("AVICI-MODULE-MIB", "aviciModuleTemperatureNormal"),
        ("AVICI-MODULE-MIB", "aviciModuleTemperatureMinor"),
        ("AVICI-MODULE-MIB", "aviciModuleTemperatureMajor"),
        ("AVICI-MODULE-MIB", "aviciModuleTemperatureCritical"),
        ("AVICI-MODULE-MIB", "aviciModuleMisconfigured"),
        ("AVICI-MODULE-MIB", "aviciModuleIncompatibleSW"))
)
if mibBuilder.loadTexts:
    aviciModuleNotificationGroup.setStatus(
        "current"
    )

aviciServerAccessModuleNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 3, 2, 5)
)
aviciServerAccessModuleNotificationGroup.setObjects(
      *(("AVICI-MODULE-MIB", "aviciServerAccessModuleDown"),
        ("AVICI-MODULE-MIB", "aviciServerAccessModuleUp"),
        ("AVICI-MODULE-MIB", "aviciAllServerAccessModulesDown"),
        ("AVICI-MODULE-MIB", "aviciAllServerAccessModulesDownClear"))
)
if mibBuilder.loadTexts:
    aviciServerAccessModuleNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aviciModuleMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2474, 1, 5, 3, 1, 1)
)
if mibBuilder.loadTexts:
    aviciModuleMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVICI-MODULE-MIB",
    **{"aviciModuleMIB": aviciModuleMIB,
       "aviciModuleObjects": aviciModuleObjects,
       "aviciModuleTable": aviciModuleTable,
       "aviciModuleEntry": aviciModuleEntry,
       "aviciModuleAdminStatus": aviciModuleAdminStatus,
       "aviciModuleOperStatus": aviciModuleOperStatus,
       "aviciModuleUpTime": aviciModuleUpTime,
       "aviciModuleCurrTemp": aviciModuleCurrTemp,
       "aviciModuleMaxTemp": aviciModuleMaxTemp,
       "aviciModuleDescr": aviciModuleDescr,
       "aviciModuleAssySerialNumber": aviciModuleAssySerialNumber,
       "aviciModuleLineSerialNumber": aviciModuleLineSerialNumber,
       "aviciModuleMbSerialNumber": aviciModuleMbSerialNumber,
       "aviciModuleAssyRevision": aviciModuleAssyRevision,
       "aviciModuleLineRevision": aviciModuleLineRevision,
       "aviciModuleMbRevision": aviciModuleMbRevision,
       "aviciModuleSoftwareVersion": aviciModuleSoftwareVersion,
       "aviciModuleFirmwareVersion": aviciModuleFirmwareVersion,
       "aviciModuleAssyProductId": aviciModuleAssyProductId,
       "aviciModuleLinePartNumber": aviciModuleLinePartNumber,
       "aviciModuleMbPartNumber": aviciModuleMbPartNumber,
       "aviciModuleIpTable": aviciModuleIpTable,
       "aviciModuleIpEntry": aviciModuleIpEntry,
       "aviciModuleIpInReceives": aviciModuleIpInReceives,
       "aviciModuleIpInHdrErrors": aviciModuleIpInHdrErrors,
       "aviciModuleIpInAddrErrors": aviciModuleIpInAddrErrors,
       "aviciModuleIpForwDatagrams": aviciModuleIpForwDatagrams,
       "aviciModuleIpInUnknownProtos": aviciModuleIpInUnknownProtos,
       "aviciModuleIpInDiscards": aviciModuleIpInDiscards,
       "aviciModuleIpInDelivers": aviciModuleIpInDelivers,
       "aviciModuleIpOutRequests": aviciModuleIpOutRequests,
       "aviciModuleIpOutDiscards": aviciModuleIpOutDiscards,
       "aviciModuleIpOutNoRoutes": aviciModuleIpOutNoRoutes,
       "aviciModuleIpFragOKs": aviciModuleIpFragOKs,
       "aviciModuleIpFragFails": aviciModuleIpFragFails,
       "aviciModuleIpFragCreates": aviciModuleIpFragCreates,
       "aviciModuleIcmpTable": aviciModuleIcmpTable,
       "aviciModuleIcmpEntry": aviciModuleIcmpEntry,
       "aviciModuleIcmpInMsgs": aviciModuleIcmpInMsgs,
       "aviciModuleIcmpInErrors": aviciModuleIcmpInErrors,
       "aviciModuleIcmpInDestUnreachs": aviciModuleIcmpInDestUnreachs,
       "aviciModuleIcmpInTimeExcds": aviciModuleIcmpInTimeExcds,
       "aviciModuleIcmpInParmProbs": aviciModuleIcmpInParmProbs,
       "aviciModuleIcmpInSrcQuenchs": aviciModuleIcmpInSrcQuenchs,
       "aviciModuleIcmpInRedirects": aviciModuleIcmpInRedirects,
       "aviciModuleIcmpInEchos": aviciModuleIcmpInEchos,
       "aviciModuleIcmpInEchoReps": aviciModuleIcmpInEchoReps,
       "aviciModuleIcmpInTimestamps": aviciModuleIcmpInTimestamps,
       "aviciModuleIcmpInTimestampReps": aviciModuleIcmpInTimestampReps,
       "aviciModuleIcmpInAddrMasks": aviciModuleIcmpInAddrMasks,
       "aviciModuleIcmpInAddrMaskReps": aviciModuleIcmpInAddrMaskReps,
       "aviciModuleIcmpOutMsgs": aviciModuleIcmpOutMsgs,
       "aviciModuleIcmpOutErrors": aviciModuleIcmpOutErrors,
       "aviciModuleIcmpOutDestUnreachs": aviciModuleIcmpOutDestUnreachs,
       "aviciModuleIcmpOutTimeExcds": aviciModuleIcmpOutTimeExcds,
       "aviciModuleIcmpOutParmProbs": aviciModuleIcmpOutParmProbs,
       "aviciModuleIcmpOutSrcQuenchs": aviciModuleIcmpOutSrcQuenchs,
       "aviciModuleIcmpOutRedirects": aviciModuleIcmpOutRedirects,
       "aviciModuleIcmpOutEchos": aviciModuleIcmpOutEchos,
       "aviciModuleIcmpOutEchoReps": aviciModuleIcmpOutEchoReps,
       "aviciModuleIcmpOutTimestamps": aviciModuleIcmpOutTimestamps,
       "aviciModuleIcmpOutTimestampReps": aviciModuleIcmpOutTimestampReps,
       "aviciModuleIcmpOutAddrMasks": aviciModuleIcmpOutAddrMasks,
       "aviciModuleIcmpOutAddrMaskReps": aviciModuleIcmpOutAddrMaskReps,
       "aviciServerAccessModuleTable": aviciServerAccessModuleTable,
       "aviciServerAccessModuleEntry": aviciServerAccessModuleEntry,
       "aviciServerAccessModuleType": aviciServerAccessModuleType,
       "aviciServerAccessModuleLinkStatus": aviciServerAccessModuleLinkStatus,
       "aviciServerAccessModuleNumTransitions": aviciServerAccessModuleNumTransitions,
       "aviciServerAccessModuleLastTransition": aviciServerAccessModuleLastTransition,
       "aviciModuleNotifications": aviciModuleNotifications,
       "aviciModuleNotificationPrefix": aviciModuleNotificationPrefix,
       "aviciModuleColdStart": aviciModuleColdStart,
       "aviciModuleWarmStart": aviciModuleWarmStart,
       "aviciModuleDown": aviciModuleDown,
       "aviciModuleTemperatureNormal": aviciModuleTemperatureNormal,
       "aviciModuleTemperatureMinor": aviciModuleTemperatureMinor,
       "aviciModuleTemperatureMajor": aviciModuleTemperatureMajor,
       "aviciModuleTemperatureCritical": aviciModuleTemperatureCritical,
       "aviciModuleMisconfigured": aviciModuleMisconfigured,
       "aviciModuleIncompatibleSW": aviciModuleIncompatibleSW,
       "aviciModuleMIBConformance": aviciModuleMIBConformance,
       "aviciModuleMIBCompliances": aviciModuleMIBCompliances,
       "aviciModuleMIBCompliance": aviciModuleMIBCompliance,
       "aviciModuleMIBGroups": aviciModuleMIBGroups,
       "aviciModuleGroup": aviciModuleGroup,
       "aviciModuleIpCountersGroup": aviciModuleIpCountersGroup,
       "aviciModuleIcmpCountersGroup": aviciModuleIcmpCountersGroup,
       "aviciModuleNotificationGroup": aviciModuleNotificationGroup,
       "aviciServerAccessModuleNotificationGroup": aviciServerAccessModuleNotificationGroup,
       "aviciServerAccessModuleNotifications": aviciServerAccessModuleNotifications,
       "aviciServerAccessModuleNotificationPrefix": aviciServerAccessModuleNotificationPrefix,
       "aviciServerAccessModuleDown": aviciServerAccessModuleDown,
       "aviciServerAccessModuleUp": aviciServerAccessModuleUp,
       "aviciAllServerAccessModulesDown": aviciAllServerAccessModulesDown,
       "aviciAllServerAccessModulesDownClear": aviciAllServerAccessModulesDownClear}
)
