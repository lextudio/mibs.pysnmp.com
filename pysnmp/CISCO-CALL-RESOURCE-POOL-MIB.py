# SNMP MIB module (CISCO-CALL-RESOURCE-POOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CALL-RESOURCE-POOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:47 2024
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

(CiscoRowOperStatus,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoRowOperStatus")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCallResourcePoolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 124)
)
ciscoCallResourcePoolMIB.setRevisions(
        ("2005-11-18 00:00",
         "1998-11-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CcrpPhoneNumber(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class CcrpPhoneNumberPattern(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class PhysicalPosition(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CCallResourcePoolMIBObjects_ObjectIdentity = ObjectIdentity
cCallResourcePoolMIBObjects = _CCallResourcePoolMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1)
)
_CcrpConfiguration_ObjectIdentity = ObjectIdentity
ccrpConfiguration = _CcrpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1)
)
_CcrpGeneralConfig_ObjectIdentity = ObjectIdentity
ccrpGeneralConfig = _CcrpGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 1)
)


class _CcrpNoCPCallTreatment_Type(Integer32):
    """Custom type ccrpNoCPCallTreatment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 2),
          ("noAnswer", 1))
    )


_CcrpNoCPCallTreatment_Type.__name__ = "Integer32"
_CcrpNoCPCallTreatment_Object = MibScalar
ccrpNoCPCallTreatment = _CcrpNoCPCallTreatment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 1, 1),
    _CcrpNoCPCallTreatment_Type()
)
ccrpNoCPCallTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrpNoCPCallTreatment.setStatus("current")


class _CcrpNoResourceCallTreatment_Type(Integer32):
    """Custom type ccrpNoResourceCallTreatment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 2),
          ("channelNotAvailable", 1))
    )


_CcrpNoResourceCallTreatment_Type.__name__ = "Integer32"
_CcrpNoResourceCallTreatment_Object = MibScalar
ccrpNoResourceCallTreatment = _CcrpNoResourceCallTreatment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 1, 2),
    _CcrpNoResourceCallTreatment_Type()
)
ccrpNoResourceCallTreatment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrpNoResourceCallTreatment.setStatus("current")
_CcrpDnisConfig_ObjectIdentity = ObjectIdentity
ccrpDnisConfig = _CcrpDnisConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 2)
)
_CcrpDnisGroupTable_Object = MibTable
ccrpDnisGroupTable = _CcrpDnisGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ccrpDnisGroupTable.setStatus("current")
_CcrpDnisGroupEntry_Object = MibTableRow
ccrpDnisGroupEntry = _CcrpDnisGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 2, 1, 1)
)
ccrpDnisGroupEntry.setIndexNames(
    (0, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisGroupName"),
    (1, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisGroupMember"),
)
if mibBuilder.loadTexts:
    ccrpDnisGroupEntry.setStatus("current")


class _CcrpDnisGroupName_Type(SnmpAdminString):
    """Custom type ccrpDnisGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_CcrpDnisGroupName_Type.__name__ = "SnmpAdminString"
_CcrpDnisGroupName_Object = MibTableColumn
ccrpDnisGroupName = _CcrpDnisGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 2, 1, 1, 1),
    _CcrpDnisGroupName_Type()
)
ccrpDnisGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccrpDnisGroupName.setStatus("current")


class _CcrpDnisGroupMember_Type(CcrpPhoneNumberPattern):
    """Custom type ccrpDnisGroupMember based on CcrpPhoneNumberPattern"""
    subtypeSpec = CcrpPhoneNumberPattern.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CcrpDnisGroupMember_Type.__name__ = "CcrpPhoneNumberPattern"
_CcrpDnisGroupMember_Object = MibTableColumn
ccrpDnisGroupMember = _CcrpDnisGroupMember_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 2, 1, 1, 2),
    _CcrpDnisGroupMember_Type()
)
ccrpDnisGroupMember.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccrpDnisGroupMember.setStatus("current")
_CcrpDnisGroupRowStatus_Type = RowStatus
_CcrpDnisGroupRowStatus_Object = MibTableColumn
ccrpDnisGroupRowStatus = _CcrpDnisGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 2, 1, 1, 3),
    _CcrpDnisGroupRowStatus_Type()
)
ccrpDnisGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpDnisGroupRowStatus.setStatus("current")
_CcrpDnisGroupCallTypeTable_Object = MibTable
ccrpDnisGroupCallTypeTable = _CcrpDnisGroupCallTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ccrpDnisGroupCallTypeTable.setStatus("current")
_CcrpDnisGroupCallTypeEntry_Object = MibTableRow
ccrpDnisGroupCallTypeEntry = _CcrpDnisGroupCallTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 2, 2, 1)
)
ccrpDnisGroupCallTypeEntry.setIndexNames(
    (1, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisGroupName"),
)
if mibBuilder.loadTexts:
    ccrpDnisGroupCallTypeEntry.setStatus("current")


class _CcrpDnisGroupCallType_Type(Integer32):
    """Custom type ccrpDnisGroupCallType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("digital", 1),
          ("speech", 2),
          ("undefined", 3))
    )


_CcrpDnisGroupCallType_Type.__name__ = "Integer32"
_CcrpDnisGroupCallType_Object = MibTableColumn
ccrpDnisGroupCallType = _CcrpDnisGroupCallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 2, 2, 1, 1),
    _CcrpDnisGroupCallType_Type()
)
ccrpDnisGroupCallType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpDnisGroupCallType.setStatus("current")
_CcrpDnisGroupCallTypeOperStatus_Type = CiscoRowOperStatus
_CcrpDnisGroupCallTypeOperStatus_Object = MibTableColumn
ccrpDnisGroupCallTypeOperStatus = _CcrpDnisGroupCallTypeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 2, 2, 1, 2),
    _CcrpDnisGroupCallTypeOperStatus_Type()
)
ccrpDnisGroupCallTypeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpDnisGroupCallTypeOperStatus.setStatus("current")
_CcrpDnisGroupCallTypeRowStatus_Type = RowStatus
_CcrpDnisGroupCallTypeRowStatus_Object = MibTableColumn
ccrpDnisGroupCallTypeRowStatus = _CcrpDnisGroupCallTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 2, 2, 1, 3),
    _CcrpDnisGroupCallTypeRowStatus_Type()
)
ccrpDnisGroupCallTypeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpDnisGroupCallTypeRowStatus.setStatus("current")
_CcrpCallDiscriminatorConfig_ObjectIdentity = ObjectIdentity
ccrpCallDiscriminatorConfig = _CcrpCallDiscriminatorConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 3)
)
_CcrpCallDiscriminatorTable_Object = MibTable
ccrpCallDiscriminatorTable = _CcrpCallDiscriminatorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ccrpCallDiscriminatorTable.setStatus("current")
_CcrpCallDiscriminatorEntry_Object = MibTableRow
ccrpCallDiscriminatorEntry = _CcrpCallDiscriminatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 3, 1, 1)
)
ccrpCallDiscriminatorEntry.setIndexNames(
    (1, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCDName"),
)
if mibBuilder.loadTexts:
    ccrpCallDiscriminatorEntry.setStatus("current")


class _CcrpCDName_Type(SnmpAdminString):
    """Custom type ccrpCDName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_CcrpCDName_Type.__name__ = "SnmpAdminString"
_CcrpCDName_Object = MibTableColumn
ccrpCDName = _CcrpCDName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 3, 1, 1, 1),
    _CcrpCDName_Type()
)
ccrpCDName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccrpCDName.setStatus("current")


class _CcrpCDCallType_Type(Bits):
    """Custom type ccrpCDCallType based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("digital", 0),
          ("speech", 1),
          ("v110", 2),
          ("v120", 3))
    )

_CcrpCDCallType_Type.__name__ = "Bits"
_CcrpCDCallType_Object = MibTableColumn
ccrpCDCallType = _CcrpCDCallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 3, 1, 1, 2),
    _CcrpCDCallType_Type()
)
ccrpCDCallType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpCDCallType.setStatus("current")
_CcrpCDRowStatus_Type = RowStatus
_CcrpCDRowStatus_Object = MibTableColumn
ccrpCDRowStatus = _CcrpCDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 3, 1, 1, 3),
    _CcrpCDRowStatus_Type()
)
ccrpCDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpCDRowStatus.setStatus("current")
_CcrpCDDiscriminatedGrpTable_Object = MibTable
ccrpCDDiscriminatedGrpTable = _CcrpCDDiscriminatedGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ccrpCDDiscriminatedGrpTable.setStatus("current")
_CcrpCDDiscriminatedGrpEntry_Object = MibTableRow
ccrpCDDiscriminatedGrpEntry = _CcrpCDDiscriminatedGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 3, 2, 1)
)
ccrpCDDiscriminatedGrpEntry.setIndexNames(
    (0, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCDName"),
    (0, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCDDiscriminatedGroupName"),
    (0, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCDDiscriminatedGroupType"),
)
if mibBuilder.loadTexts:
    ccrpCDDiscriminatedGrpEntry.setStatus("current")


class _CcrpCDDiscriminatedGroupName_Type(SnmpAdminString):
    """Custom type ccrpCDDiscriminatedGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_CcrpCDDiscriminatedGroupName_Type.__name__ = "SnmpAdminString"
_CcrpCDDiscriminatedGroupName_Object = MibTableColumn
ccrpCDDiscriminatedGroupName = _CcrpCDDiscriminatedGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 3, 2, 1, 1),
    _CcrpCDDiscriminatedGroupName_Type()
)
ccrpCDDiscriminatedGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccrpCDDiscriminatedGroupName.setStatus("current")


class _CcrpCDDiscriminatedGroupType_Type(Integer32):
    """Custom type ccrpCDDiscriminatedGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("dnis", 1)
    )


_CcrpCDDiscriminatedGroupType_Type.__name__ = "Integer32"
_CcrpCDDiscriminatedGroupType_Object = MibTableColumn
ccrpCDDiscriminatedGroupType = _CcrpCDDiscriminatedGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 3, 2, 1, 2),
    _CcrpCDDiscriminatedGroupType_Type()
)
ccrpCDDiscriminatedGroupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccrpCDDiscriminatedGroupType.setStatus("current")
_CcrpCDDiscriminatedGroupOperStatus_Type = CiscoRowOperStatus
_CcrpCDDiscriminatedGroupOperStatus_Object = MibTableColumn
ccrpCDDiscriminatedGroupOperStatus = _CcrpCDDiscriminatedGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 3, 2, 1, 3),
    _CcrpCDDiscriminatedGroupOperStatus_Type()
)
ccrpCDDiscriminatedGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpCDDiscriminatedGroupOperStatus.setStatus("current")
_CcrpCDDiscriminatedGroupRowStatus_Type = RowStatus
_CcrpCDDiscriminatedGroupRowStatus_Object = MibTableColumn
ccrpCDDiscriminatedGroupRowStatus = _CcrpCDDiscriminatedGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 3, 2, 1, 4),
    _CcrpCDDiscriminatedGroupRowStatus_Type()
)
ccrpCDDiscriminatedGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpCDDiscriminatedGroupRowStatus.setStatus("current")
_CcrpResourceConfig_ObjectIdentity = ObjectIdentity
ccrpResourceConfig = _CcrpResourceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 4)
)
_CcrpResourceTable_Object = MibTable
ccrpResourceTable = _CcrpResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ccrpResourceTable.setStatus("current")
_CcrpResourceEntry_Object = MibTableRow
ccrpResourceEntry = _CcrpResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 4, 1, 1)
)
ccrpResourceEntry.setIndexNames(
    (1, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpResourceName"),
)
if mibBuilder.loadTexts:
    ccrpResourceEntry.setStatus("current")


class _CcrpResourceName_Type(SnmpAdminString):
    """Custom type ccrpResourceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_CcrpResourceName_Type.__name__ = "SnmpAdminString"
_CcrpResourceName_Object = MibTableColumn
ccrpResourceName = _CcrpResourceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 4, 1, 1, 1),
    _CcrpResourceName_Type()
)
ccrpResourceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccrpResourceName.setStatus("current")


class _CcrpResourcePortBased_Type(TruthValue):
    """Custom type ccrpResourcePortBased based on TruthValue"""


_CcrpResourcePortBased_Object = MibTableColumn
ccrpResourcePortBased = _CcrpResourcePortBased_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 4, 1, 1, 2),
    _CcrpResourcePortBased_Type()
)
ccrpResourcePortBased.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpResourcePortBased.setStatus("current")


class _CcrpResourceLimit_Type(Unsigned32):
    """Custom type ccrpResourceLimit based on Unsigned32"""
    defaultValue = 0


_CcrpResourceLimit_Object = MibTableColumn
ccrpResourceLimit = _CcrpResourceLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 4, 1, 1, 3),
    _CcrpResourceLimit_Type()
)
ccrpResourceLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpResourceLimit.setStatus("current")
_CcrpResourceGroupOperStatus_Type = CiscoRowOperStatus
_CcrpResourceGroupOperStatus_Object = MibTableColumn
ccrpResourceGroupOperStatus = _CcrpResourceGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 4, 1, 1, 4),
    _CcrpResourceGroupOperStatus_Type()
)
ccrpResourceGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpResourceGroupOperStatus.setStatus("current")
_CcrpResourceGroupRowStatus_Type = RowStatus
_CcrpResourceGroupRowStatus_Object = MibTableColumn
ccrpResourceGroupRowStatus = _CcrpResourceGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 4, 1, 1, 5),
    _CcrpResourceGroupRowStatus_Type()
)
ccrpResourceGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpResourceGroupRowStatus.setStatus("current")
_CcrpResourceRangeTable_Object = MibTable
ccrpResourceRangeTable = _CcrpResourceRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ccrpResourceRangeTable.setStatus("current")
_CcrpResourceRangeEntry_Object = MibTableRow
ccrpResourceRangeEntry = _CcrpResourceRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 4, 2, 1)
)
ccrpResourceRangeEntry.setIndexNames(
    (0, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpResourceName"),
    (0, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpResourceRangeIndex"),
)
if mibBuilder.loadTexts:
    ccrpResourceRangeEntry.setStatus("current")


class _CcrpResourceRangeIndex_Type(Unsigned32):
    """Custom type ccrpResourceRangeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CcrpResourceRangeIndex_Type.__name__ = "Unsigned32"
_CcrpResourceRangeIndex_Object = MibTableColumn
ccrpResourceRangeIndex = _CcrpResourceRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 4, 2, 1, 1),
    _CcrpResourceRangeIndex_Type()
)
ccrpResourceRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccrpResourceRangeIndex.setStatus("current")


class _CcrpResourceRangeStartPort_Type(PhysicalPosition):
    """Custom type ccrpResourceRangeStartPort based on PhysicalPosition"""
    defaultValue = 0


_CcrpResourceRangeStartPort_Object = MibTableColumn
ccrpResourceRangeStartPort = _CcrpResourceRangeStartPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 4, 2, 1, 2),
    _CcrpResourceRangeStartPort_Type()
)
ccrpResourceRangeStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpResourceRangeStartPort.setStatus("current")


class _CcrpResourceRangeEndPort_Type(PhysicalPosition):
    """Custom type ccrpResourceRangeEndPort based on PhysicalPosition"""
    defaultValue = 0


_CcrpResourceRangeEndPort_Object = MibTableColumn
ccrpResourceRangeEndPort = _CcrpResourceRangeEndPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 4, 2, 1, 3),
    _CcrpResourceRangeEndPort_Type()
)
ccrpResourceRangeEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpResourceRangeEndPort.setStatus("current")
_CcrpResourceRangeOperStatus_Type = CiscoRowOperStatus
_CcrpResourceRangeOperStatus_Object = MibTableColumn
ccrpResourceRangeOperStatus = _CcrpResourceRangeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 4, 2, 1, 4),
    _CcrpResourceRangeOperStatus_Type()
)
ccrpResourceRangeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpResourceRangeOperStatus.setStatus("current")
_CcrpResourceRangeRowStatus_Type = RowStatus
_CcrpResourceRangeRowStatus_Object = MibTableColumn
ccrpResourceRangeRowStatus = _CcrpResourceRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 4, 2, 1, 5),
    _CcrpResourceRangeRowStatus_Type()
)
ccrpResourceRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpResourceRangeRowStatus.setStatus("current")
_CcrpCustomerProfileConfig_ObjectIdentity = ObjectIdentity
ccrpCustomerProfileConfig = _CcrpCustomerProfileConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5)
)
_CcrpCustomerProfileTable_Object = MibTable
ccrpCustomerProfileTable = _CcrpCustomerProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ccrpCustomerProfileTable.setStatus("current")
_CcrpCustomerProfileEntry_Object = MibTableRow
ccrpCustomerProfileEntry = _CcrpCustomerProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 1, 1)
)
ccrpCustomerProfileEntry.setIndexNames(
    (1, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPName"),
)
if mibBuilder.loadTexts:
    ccrpCustomerProfileEntry.setStatus("current")


class _CcrpCPName_Type(SnmpAdminString):
    """Custom type ccrpCPName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_CcrpCPName_Type.__name__ = "SnmpAdminString"
_CcrpCPName_Object = MibTableColumn
ccrpCPName = _CcrpCPName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 1, 1, 1),
    _CcrpCPName_Type()
)
ccrpCPName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccrpCPName.setStatus("current")


class _CcrpCPSessionLimit_Type(Unsigned32):
    """Custom type ccrpCPSessionLimit based on Unsigned32"""
    defaultValue = 0


_CcrpCPSessionLimit_Object = MibTableColumn
ccrpCPSessionLimit = _CcrpCPSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 1, 1, 2),
    _CcrpCPSessionLimit_Type()
)
ccrpCPSessionLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpCPSessionLimit.setStatus("current")


class _CcrpCPOverflow_Type(Integer32):
    """Custom type ccrpCPOverflow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CcrpCPOverflow_Type.__name__ = "Integer32"
_CcrpCPOverflow_Object = MibTableColumn
ccrpCPOverflow = _CcrpCPOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 1, 1, 3),
    _CcrpCPOverflow_Type()
)
ccrpCPOverflow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpCPOverflow.setStatus("current")
_CcrpCPRowStatus_Type = RowStatus
_CcrpCPRowStatus_Object = MibTableColumn
ccrpCPRowStatus = _CcrpCPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 1, 1, 4),
    _CcrpCPRowStatus_Type()
)
ccrpCPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpCPRowStatus.setStatus("current")
_CcrpCPDnisGrpTable_Object = MibTable
ccrpCPDnisGrpTable = _CcrpCPDnisGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ccrpCPDnisGrpTable.setStatus("current")
_CcrpCPDnisGrpEntry_Object = MibTableRow
ccrpCPDnisGrpEntry = _CcrpCPDnisGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 2, 1)
)
ccrpCPDnisGrpEntry.setIndexNames(
    (0, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPName"),
    (1, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisGroupName"),
)
if mibBuilder.loadTexts:
    ccrpCPDnisGrpEntry.setStatus("current")
_CcrpCPDnisGroupOperStatus_Type = CiscoRowOperStatus
_CcrpCPDnisGroupOperStatus_Object = MibTableColumn
ccrpCPDnisGroupOperStatus = _CcrpCPDnisGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 2, 1, 1),
    _CcrpCPDnisGroupOperStatus_Type()
)
ccrpCPDnisGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpCPDnisGroupOperStatus.setStatus("current")
_CcrpCPDnisGroupRowStatus_Type = RowStatus
_CcrpCPDnisGroupRowStatus_Object = MibTableColumn
ccrpCPDnisGroupRowStatus = _CcrpCPDnisGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 2, 1, 2),
    _CcrpCPDnisGroupRowStatus_Type()
)
ccrpCPDnisGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpCPDnisGroupRowStatus.setStatus("current")
_CcrpCPResourceGrpTable_Object = MibTable
ccrpCPResourceGrpTable = _CcrpCPResourceGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ccrpCPResourceGrpTable.setStatus("current")
_CcrpCPResourceGrpEntry_Object = MibTableRow
ccrpCPResourceGrpEntry = _CcrpCPResourceGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 3, 1)
)
ccrpCPResourceGrpEntry.setIndexNames(
    (0, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPName"),
    (0, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpResourceName"),
    (0, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPResourceCallType"),
)
if mibBuilder.loadTexts:
    ccrpCPResourceGrpEntry.setStatus("current")


class _CcrpCPResourceCallType_Type(Bits):
    """Custom type ccrpCPResourceCallType based on Bits"""
    namedValues = NamedValues(
        *(("digital", 0),
          ("speech", 1),
          ("v110", 2),
          ("v120", 3))
    )

_CcrpCPResourceCallType_Type.__name__ = "Bits"
_CcrpCPResourceCallType_Object = MibTableColumn
ccrpCPResourceCallType = _CcrpCPResourceCallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 3, 1, 1),
    _CcrpCPResourceCallType_Type()
)
ccrpCPResourceCallType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccrpCPResourceCallType.setStatus("current")


class _CcrpCPResourceServiceProfileName_Type(SnmpAdminString):
    """Custom type ccrpCPResourceServiceProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_CcrpCPResourceServiceProfileName_Type.__name__ = "SnmpAdminString"
_CcrpCPResourceServiceProfileName_Object = MibTableColumn
ccrpCPResourceServiceProfileName = _CcrpCPResourceServiceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 3, 1, 2),
    _CcrpCPResourceServiceProfileName_Type()
)
ccrpCPResourceServiceProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpCPResourceServiceProfileName.setStatus("current")
_CcrpCPResourceOperStatus_Type = CiscoRowOperStatus
_CcrpCPResourceOperStatus_Object = MibTableColumn
ccrpCPResourceOperStatus = _CcrpCPResourceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 3, 1, 3),
    _CcrpCPResourceOperStatus_Type()
)
ccrpCPResourceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpCPResourceOperStatus.setStatus("current")
_CcrpCPResourceRowStatus_Type = RowStatus
_CcrpCPResourceRowStatus_Object = MibTableColumn
ccrpCPResourceRowStatus = _CcrpCPResourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 3, 1, 4),
    _CcrpCPResourceRowStatus_Type()
)
ccrpCPResourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpCPResourceRowStatus.setStatus("current")
_CcrpCPVGTable_Object = MibTable
ccrpCPVGTable = _CcrpCPVGTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 4)
)
if mibBuilder.loadTexts:
    ccrpCPVGTable.setStatus("current")
_CcrpCPVGEntry_Object = MibTableRow
ccrpCPVGEntry = _CcrpCPVGEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 4, 1)
)
ccrpCPVGEntry.setIndexNames(
    (0, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPName"),
    (1, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPVGName"),
)
if mibBuilder.loadTexts:
    ccrpCPVGEntry.setStatus("current")


class _CcrpCPVGName_Type(SnmpAdminString):
    """Custom type ccrpCPVGName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_CcrpCPVGName_Type.__name__ = "SnmpAdminString"
_CcrpCPVGName_Object = MibTableColumn
ccrpCPVGName = _CcrpCPVGName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 4, 1, 1),
    _CcrpCPVGName_Type()
)
ccrpCPVGName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccrpCPVGName.setStatus("current")
_CcrpCPVGOperStatus_Type = CiscoRowOperStatus
_CcrpCPVGOperStatus_Object = MibTableColumn
ccrpCPVGOperStatus = _CcrpCPVGOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 4, 1, 2),
    _CcrpCPVGOperStatus_Type()
)
ccrpCPVGOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpCPVGOperStatus.setStatus("current")
_CcrpCPVGRowStatus_Type = RowStatus
_CcrpCPVGRowStatus_Object = MibTableColumn
ccrpCPVGRowStatus = _CcrpCPVGRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 1, 5, 4, 1, 3),
    _CcrpCPVGRowStatus_Type()
)
ccrpCPVGRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccrpCPVGRowStatus.setStatus("current")
_CcrpStatistics_ObjectIdentity = ObjectIdentity
ccrpStatistics = _CcrpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2)
)
_CcrpCPStatistics_ObjectIdentity = ObjectIdentity
ccrpCPStatistics = _CcrpCPStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 1)
)
_CcrpCPStatisticsTable_Object = MibTable
ccrpCPStatisticsTable = _CcrpCPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ccrpCPStatisticsTable.setStatus("current")
_CcrpCPStatisticsEntry_Object = MibTableRow
ccrpCPStatisticsEntry = _CcrpCPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccrpCPStatisticsEntry.setStatus("current")
_CcrpCPActiveSessions_Type = Gauge32
_CcrpCPActiveSessions_Object = MibTableColumn
ccrpCPActiveSessions = _CcrpCPActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 1, 1, 1, 1),
    _CcrpCPActiveSessions_Type()
)
ccrpCPActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpCPActiveSessions.setStatus("current")
if mibBuilder.loadTexts:
    ccrpCPActiveSessions.setUnits("sessions")
_CcrpCPActiveOverflowSessions_Type = Gauge32
_CcrpCPActiveOverflowSessions_Object = MibTableColumn
ccrpCPActiveOverflowSessions = _CcrpCPActiveOverflowSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 1, 1, 1, 2),
    _CcrpCPActiveOverflowSessions_Type()
)
ccrpCPActiveOverflowSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpCPActiveOverflowSessions.setStatus("current")
if mibBuilder.loadTexts:
    ccrpCPActiveOverflowSessions.setUnits("sessions")
_CcrpCPTotalSessions_Type = Counter32
_CcrpCPTotalSessions_Object = MibTableColumn
ccrpCPTotalSessions = _CcrpCPTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 1, 1, 1, 3),
    _CcrpCPTotalSessions_Type()
)
ccrpCPTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpCPTotalSessions.setStatus("current")
if mibBuilder.loadTexts:
    ccrpCPTotalSessions.setUnits("sessions")
_CcrpCPTotalOverflowSessions_Type = Counter32
_CcrpCPTotalOverflowSessions_Object = MibTableColumn
ccrpCPTotalOverflowSessions = _CcrpCPTotalOverflowSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 1, 1, 1, 4),
    _CcrpCPTotalOverflowSessions_Type()
)
ccrpCPTotalOverflowSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpCPTotalOverflowSessions.setStatus("current")
if mibBuilder.loadTexts:
    ccrpCPTotalOverflowSessions.setUnits("sessions")
_CcrpCPNumberOverflowState_Type = Counter32
_CcrpCPNumberOverflowState_Object = MibTableColumn
ccrpCPNumberOverflowState = _CcrpCPNumberOverflowState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 1, 1, 1, 5),
    _CcrpCPNumberOverflowState_Type()
)
ccrpCPNumberOverflowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpCPNumberOverflowState.setStatus("current")
if mibBuilder.loadTexts:
    ccrpCPNumberOverflowState.setUnits("occurrences")
_CcrpCPNumberMaxState_Type = Counter32
_CcrpCPNumberMaxState_Object = MibTableColumn
ccrpCPNumberMaxState = _CcrpCPNumberMaxState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 1, 1, 1, 6),
    _CcrpCPNumberMaxState_Type()
)
ccrpCPNumberMaxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpCPNumberMaxState.setStatus("current")
if mibBuilder.loadTexts:
    ccrpCPNumberMaxState.setUnits("occurrences")
_CcrpCPOverflowTime_Type = TimeTicks
_CcrpCPOverflowTime_Object = MibTableColumn
ccrpCPOverflowTime = _CcrpCPOverflowTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 1, 1, 1, 7),
    _CcrpCPOverflowTime_Type()
)
ccrpCPOverflowTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpCPOverflowTime.setStatus("current")
_CcrpCPMaxStateTime_Type = TimeTicks
_CcrpCPMaxStateTime_Object = MibTableColumn
ccrpCPMaxStateTime = _CcrpCPMaxStateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 1, 1, 1, 8),
    _CcrpCPMaxStateTime_Type()
)
ccrpCPMaxStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpCPMaxStateTime.setStatus("current")
_CcrpCPPeakActiveSessions_Type = Gauge32
_CcrpCPPeakActiveSessions_Object = MibTableColumn
ccrpCPPeakActiveSessions = _CcrpCPPeakActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 1, 1, 1, 9),
    _CcrpCPPeakActiveSessions_Type()
)
ccrpCPPeakActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpCPPeakActiveSessions.setStatus("current")
if mibBuilder.loadTexts:
    ccrpCPPeakActiveSessions.setUnits("sessions")
_CcrpCPOverflowRejected_Type = Counter32
_CcrpCPOverflowRejected_Object = MibTableColumn
ccrpCPOverflowRejected = _CcrpCPOverflowRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 1, 1, 1, 10),
    _CcrpCPOverflowRejected_Type()
)
ccrpCPOverflowRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpCPOverflowRejected.setStatus("current")
if mibBuilder.loadTexts:
    ccrpCPOverflowRejected.setUnits("call attempts")
_CcrpCPResourceRejected_Type = Counter32
_CcrpCPResourceRejected_Object = MibTableColumn
ccrpCPResourceRejected = _CcrpCPResourceRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 1, 1, 1, 11),
    _CcrpCPResourceRejected_Type()
)
ccrpCPResourceRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpCPResourceRejected.setStatus("current")
if mibBuilder.loadTexts:
    ccrpCPResourceRejected.setUnits("call attempts")
_CcrpDnisStatistics_ObjectIdentity = ObjectIdentity
ccrpDnisStatistics = _CcrpDnisStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 2)
)


class _CcrpDnisStatisticsTableMaxEntries_Type(Unsigned32):
    """Custom type ccrpDnisStatisticsTableMaxEntries based on Unsigned32"""
    defaultValue = 0


_CcrpDnisStatisticsTableMaxEntries_Object = MibScalar
ccrpDnisStatisticsTableMaxEntries = _CcrpDnisStatisticsTableMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 2, 1),
    _CcrpDnisStatisticsTableMaxEntries_Type()
)
ccrpDnisStatisticsTableMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccrpDnisStatisticsTableMaxEntries.setStatus("current")
_CcrpDnisStatisticsTableSystemMax_Type = Unsigned32
_CcrpDnisStatisticsTableSystemMax_Object = MibScalar
ccrpDnisStatisticsTableSystemMax = _CcrpDnisStatisticsTableSystemMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 2, 2),
    _CcrpDnisStatisticsTableSystemMax_Type()
)
ccrpDnisStatisticsTableSystemMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpDnisStatisticsTableSystemMax.setStatus("current")
_CcrpDnisStatisticsTableLengthExceeded_Type = Counter32
_CcrpDnisStatisticsTableLengthExceeded_Object = MibScalar
ccrpDnisStatisticsTableLengthExceeded = _CcrpDnisStatisticsTableLengthExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 2, 3),
    _CcrpDnisStatisticsTableLengthExceeded_Type()
)
ccrpDnisStatisticsTableLengthExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpDnisStatisticsTableLengthExceeded.setStatus("current")
_CcrpDnisStatisticsTable_Object = MibTable
ccrpDnisStatisticsTable = _CcrpDnisStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    ccrpDnisStatisticsTable.setStatus("current")
_CcrpDnisStatisticsEntry_Object = MibTableRow
ccrpDnisStatisticsEntry = _CcrpDnisStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 2, 4, 1)
)
ccrpDnisStatisticsEntry.setIndexNames(
    (1, "CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisStatisticsDnisNumber"),
)
if mibBuilder.loadTexts:
    ccrpDnisStatisticsEntry.setStatus("current")
_CcrpDnisStatisticsDnisNumber_Type = CcrpPhoneNumber
_CcrpDnisStatisticsDnisNumber_Object = MibTableColumn
ccrpDnisStatisticsDnisNumber = _CcrpDnisStatisticsDnisNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 2, 4, 1, 1),
    _CcrpDnisStatisticsDnisNumber_Type()
)
ccrpDnisStatisticsDnisNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccrpDnisStatisticsDnisNumber.setStatus("current")


class _CcrpDnisStatisticsGroupName_Type(SnmpAdminString):
    """Custom type ccrpDnisStatisticsGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_CcrpDnisStatisticsGroupName_Type.__name__ = "SnmpAdminString"
_CcrpDnisStatisticsGroupName_Object = MibTableColumn
ccrpDnisStatisticsGroupName = _CcrpDnisStatisticsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 2, 4, 1, 2),
    _CcrpDnisStatisticsGroupName_Type()
)
ccrpDnisStatisticsGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpDnisStatisticsGroupName.setStatus("current")
_CcrpDnisActiveSessions_Type = Gauge32
_CcrpDnisActiveSessions_Object = MibTableColumn
ccrpDnisActiveSessions = _CcrpDnisActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 2, 4, 1, 3),
    _CcrpDnisActiveSessions_Type()
)
ccrpDnisActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpDnisActiveSessions.setStatus("current")
if mibBuilder.loadTexts:
    ccrpDnisActiveSessions.setUnits("sessions")
_CcrpDnisTotalSessions_Type = Counter32
_CcrpDnisTotalSessions_Object = MibTableColumn
ccrpDnisTotalSessions = _CcrpDnisTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 2, 4, 1, 4),
    _CcrpDnisTotalSessions_Type()
)
ccrpDnisTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpDnisTotalSessions.setStatus("current")
if mibBuilder.loadTexts:
    ccrpDnisTotalSessions.setUnits("sessions")
_CcrpDnisPeakActiveSessions_Type = Gauge32
_CcrpDnisPeakActiveSessions_Object = MibTableColumn
ccrpDnisPeakActiveSessions = _CcrpDnisPeakActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 2, 4, 1, 5),
    _CcrpDnisPeakActiveSessions_Type()
)
ccrpDnisPeakActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpDnisPeakActiveSessions.setStatus("current")
if mibBuilder.loadTexts:
    ccrpDnisPeakActiveSessions.setUnits("sessions")
_CcrpDnisCallTypeRejected_Type = Counter32
_CcrpDnisCallTypeRejected_Object = MibTableColumn
ccrpDnisCallTypeRejected = _CcrpDnisCallTypeRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 2, 4, 1, 6),
    _CcrpDnisCallTypeRejected_Type()
)
ccrpDnisCallTypeRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpDnisCallTypeRejected.setStatus("current")
if mibBuilder.loadTexts:
    ccrpDnisCallTypeRejected.setUnits("sessions")
_CcrpCDStatistics_ObjectIdentity = ObjectIdentity
ccrpCDStatistics = _CcrpCDStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 3)
)
_CcrpCDStatisticsTable_Object = MibTable
ccrpCDStatisticsTable = _CcrpCDStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ccrpCDStatisticsTable.setStatus("current")
_CcrpCDStatisticsEntry_Object = MibTableRow
ccrpCDStatisticsEntry = _CcrpCDStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ccrpCDStatisticsEntry.setStatus("current")
_CcrpCDRejected_Type = Counter32
_CcrpCDRejected_Object = MibTableColumn
ccrpCDRejected = _CcrpCDRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 1, 2, 3, 1, 1, 1),
    _CcrpCDRejected_Type()
)
ccrpCDRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccrpCDRejected.setStatus("current")
if mibBuilder.loadTexts:
    ccrpCDRejected.setUnits("sessions")
_CcrpMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ccrpMIBNotificationPrefix = _CcrpMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 2)
)
_CcrpMIBConformance_ObjectIdentity = ObjectIdentity
ccrpMIBConformance = _CcrpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 3)
)
_CcrpMIBCompliances_ObjectIdentity = ObjectIdentity
ccrpMIBCompliances = _CcrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 3, 1)
)
_CcrpMIBGroups_ObjectIdentity = ObjectIdentity
ccrpMIBGroups = _CcrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 3, 2)
)
ccrpCustomerProfileEntry.registerAugmentions(
    ("CISCO-CALL-RESOURCE-POOL-MIB",
     "ccrpCPStatisticsEntry")
)
ccrpCPStatisticsEntry.setIndexNames(*ccrpCustomerProfileEntry.getIndexNames())
ccrpCallDiscriminatorEntry.registerAugmentions(
    ("CISCO-CALL-RESOURCE-POOL-MIB",
     "ccrpCDStatisticsEntry")
)
ccrpCDStatisticsEntry.setIndexNames(*ccrpCallDiscriminatorEntry.getIndexNames())

# Managed Objects groups

ccrpGeneralConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 3, 2, 1)
)
ccrpGeneralConfigGroup.setObjects(
      *(("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpNoCPCallTreatment"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpNoResourceCallTreatment"))
)
if mibBuilder.loadTexts:
    ccrpGeneralConfigGroup.setStatus("current")

ccrpDnisConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 3, 2, 2)
)
ccrpDnisConfigGroup.setObjects(
      *(("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisGroupRowStatus"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisGroupCallType"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisGroupCallTypeOperStatus"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisGroupCallTypeRowStatus"))
)
if mibBuilder.loadTexts:
    ccrpDnisConfigGroup.setStatus("current")

ccrpCDConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 3, 2, 3)
)
ccrpCDConfigGroup.setObjects(
      *(("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCDCallType"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCDRowStatus"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCDDiscriminatedGroupOperStatus"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCDDiscriminatedGroupRowStatus"))
)
if mibBuilder.loadTexts:
    ccrpCDConfigGroup.setStatus("current")

ccrpResourceConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 3, 2, 4)
)
ccrpResourceConfigGroup.setObjects(
      *(("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpResourcePortBased"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpResourceLimit"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpResourceGroupOperStatus"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpResourceGroupRowStatus"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpResourceRangeStartPort"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpResourceRangeEndPort"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpResourceRangeOperStatus"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpResourceRangeRowStatus"))
)
if mibBuilder.loadTexts:
    ccrpResourceConfigGroup.setStatus("current")

ccrpCPConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 3, 2, 5)
)
ccrpCPConfigGroup.setObjects(
      *(("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPSessionLimit"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPOverflow"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPRowStatus"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPDnisGroupOperStatus"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPDnisGroupRowStatus"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPResourceServiceProfileName"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPResourceOperStatus"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPResourceRowStatus"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPVGOperStatus"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPVGRowStatus"))
)
if mibBuilder.loadTexts:
    ccrpCPConfigGroup.setStatus("current")

ccrpCPStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 3, 2, 6)
)
ccrpCPStatisticsGroup.setObjects(
      *(("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPActiveSessions"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPActiveOverflowSessions"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPTotalSessions"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPTotalOverflowSessions"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPNumberOverflowState"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPNumberMaxState"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPOverflowTime"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPMaxStateTime"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPPeakActiveSessions"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPOverflowRejected"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCPResourceRejected"))
)
if mibBuilder.loadTexts:
    ccrpCPStatisticsGroup.setStatus("current")

ccrpDnisStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 3, 2, 7)
)
ccrpDnisStatisticsGroup.setObjects(
      *(("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisStatisticsTableMaxEntries"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisStatisticsTableSystemMax"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisStatisticsTableLengthExceeded"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisStatisticsGroupName"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisActiveSessions"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisTotalSessions"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisPeakActiveSessions"),
        ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpDnisCallTypeRejected"))
)
if mibBuilder.loadTexts:
    ccrpDnisStatisticsGroup.setStatus("current")

ccrpCDStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 3, 2, 8)
)
ccrpCDStatisticsGroup.setObjects(
    ("CISCO-CALL-RESOURCE-POOL-MIB", "ccrpCDRejected")
)
if mibBuilder.loadTexts:
    ccrpCDStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ccrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 124, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ccrpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CALL-RESOURCE-POOL-MIB",
    **{"CcrpPhoneNumber": CcrpPhoneNumber,
       "CcrpPhoneNumberPattern": CcrpPhoneNumberPattern,
       "PhysicalPosition": PhysicalPosition,
       "ciscoCallResourcePoolMIB": ciscoCallResourcePoolMIB,
       "cCallResourcePoolMIBObjects": cCallResourcePoolMIBObjects,
       "ccrpConfiguration": ccrpConfiguration,
       "ccrpGeneralConfig": ccrpGeneralConfig,
       "ccrpNoCPCallTreatment": ccrpNoCPCallTreatment,
       "ccrpNoResourceCallTreatment": ccrpNoResourceCallTreatment,
       "ccrpDnisConfig": ccrpDnisConfig,
       "ccrpDnisGroupTable": ccrpDnisGroupTable,
       "ccrpDnisGroupEntry": ccrpDnisGroupEntry,
       "ccrpDnisGroupName": ccrpDnisGroupName,
       "ccrpDnisGroupMember": ccrpDnisGroupMember,
       "ccrpDnisGroupRowStatus": ccrpDnisGroupRowStatus,
       "ccrpDnisGroupCallTypeTable": ccrpDnisGroupCallTypeTable,
       "ccrpDnisGroupCallTypeEntry": ccrpDnisGroupCallTypeEntry,
       "ccrpDnisGroupCallType": ccrpDnisGroupCallType,
       "ccrpDnisGroupCallTypeOperStatus": ccrpDnisGroupCallTypeOperStatus,
       "ccrpDnisGroupCallTypeRowStatus": ccrpDnisGroupCallTypeRowStatus,
       "ccrpCallDiscriminatorConfig": ccrpCallDiscriminatorConfig,
       "ccrpCallDiscriminatorTable": ccrpCallDiscriminatorTable,
       "ccrpCallDiscriminatorEntry": ccrpCallDiscriminatorEntry,
       "ccrpCDName": ccrpCDName,
       "ccrpCDCallType": ccrpCDCallType,
       "ccrpCDRowStatus": ccrpCDRowStatus,
       "ccrpCDDiscriminatedGrpTable": ccrpCDDiscriminatedGrpTable,
       "ccrpCDDiscriminatedGrpEntry": ccrpCDDiscriminatedGrpEntry,
       "ccrpCDDiscriminatedGroupName": ccrpCDDiscriminatedGroupName,
       "ccrpCDDiscriminatedGroupType": ccrpCDDiscriminatedGroupType,
       "ccrpCDDiscriminatedGroupOperStatus": ccrpCDDiscriminatedGroupOperStatus,
       "ccrpCDDiscriminatedGroupRowStatus": ccrpCDDiscriminatedGroupRowStatus,
       "ccrpResourceConfig": ccrpResourceConfig,
       "ccrpResourceTable": ccrpResourceTable,
       "ccrpResourceEntry": ccrpResourceEntry,
       "ccrpResourceName": ccrpResourceName,
       "ccrpResourcePortBased": ccrpResourcePortBased,
       "ccrpResourceLimit": ccrpResourceLimit,
       "ccrpResourceGroupOperStatus": ccrpResourceGroupOperStatus,
       "ccrpResourceGroupRowStatus": ccrpResourceGroupRowStatus,
       "ccrpResourceRangeTable": ccrpResourceRangeTable,
       "ccrpResourceRangeEntry": ccrpResourceRangeEntry,
       "ccrpResourceRangeIndex": ccrpResourceRangeIndex,
       "ccrpResourceRangeStartPort": ccrpResourceRangeStartPort,
       "ccrpResourceRangeEndPort": ccrpResourceRangeEndPort,
       "ccrpResourceRangeOperStatus": ccrpResourceRangeOperStatus,
       "ccrpResourceRangeRowStatus": ccrpResourceRangeRowStatus,
       "ccrpCustomerProfileConfig": ccrpCustomerProfileConfig,
       "ccrpCustomerProfileTable": ccrpCustomerProfileTable,
       "ccrpCustomerProfileEntry": ccrpCustomerProfileEntry,
       "ccrpCPName": ccrpCPName,
       "ccrpCPSessionLimit": ccrpCPSessionLimit,
       "ccrpCPOverflow": ccrpCPOverflow,
       "ccrpCPRowStatus": ccrpCPRowStatus,
       "ccrpCPDnisGrpTable": ccrpCPDnisGrpTable,
       "ccrpCPDnisGrpEntry": ccrpCPDnisGrpEntry,
       "ccrpCPDnisGroupOperStatus": ccrpCPDnisGroupOperStatus,
       "ccrpCPDnisGroupRowStatus": ccrpCPDnisGroupRowStatus,
       "ccrpCPResourceGrpTable": ccrpCPResourceGrpTable,
       "ccrpCPResourceGrpEntry": ccrpCPResourceGrpEntry,
       "ccrpCPResourceCallType": ccrpCPResourceCallType,
       "ccrpCPResourceServiceProfileName": ccrpCPResourceServiceProfileName,
       "ccrpCPResourceOperStatus": ccrpCPResourceOperStatus,
       "ccrpCPResourceRowStatus": ccrpCPResourceRowStatus,
       "ccrpCPVGTable": ccrpCPVGTable,
       "ccrpCPVGEntry": ccrpCPVGEntry,
       "ccrpCPVGName": ccrpCPVGName,
       "ccrpCPVGOperStatus": ccrpCPVGOperStatus,
       "ccrpCPVGRowStatus": ccrpCPVGRowStatus,
       "ccrpStatistics": ccrpStatistics,
       "ccrpCPStatistics": ccrpCPStatistics,
       "ccrpCPStatisticsTable": ccrpCPStatisticsTable,
       "ccrpCPStatisticsEntry": ccrpCPStatisticsEntry,
       "ccrpCPActiveSessions": ccrpCPActiveSessions,
       "ccrpCPActiveOverflowSessions": ccrpCPActiveOverflowSessions,
       "ccrpCPTotalSessions": ccrpCPTotalSessions,
       "ccrpCPTotalOverflowSessions": ccrpCPTotalOverflowSessions,
       "ccrpCPNumberOverflowState": ccrpCPNumberOverflowState,
       "ccrpCPNumberMaxState": ccrpCPNumberMaxState,
       "ccrpCPOverflowTime": ccrpCPOverflowTime,
       "ccrpCPMaxStateTime": ccrpCPMaxStateTime,
       "ccrpCPPeakActiveSessions": ccrpCPPeakActiveSessions,
       "ccrpCPOverflowRejected": ccrpCPOverflowRejected,
       "ccrpCPResourceRejected": ccrpCPResourceRejected,
       "ccrpDnisStatistics": ccrpDnisStatistics,
       "ccrpDnisStatisticsTableMaxEntries": ccrpDnisStatisticsTableMaxEntries,
       "ccrpDnisStatisticsTableSystemMax": ccrpDnisStatisticsTableSystemMax,
       "ccrpDnisStatisticsTableLengthExceeded": ccrpDnisStatisticsTableLengthExceeded,
       "ccrpDnisStatisticsTable": ccrpDnisStatisticsTable,
       "ccrpDnisStatisticsEntry": ccrpDnisStatisticsEntry,
       "ccrpDnisStatisticsDnisNumber": ccrpDnisStatisticsDnisNumber,
       "ccrpDnisStatisticsGroupName": ccrpDnisStatisticsGroupName,
       "ccrpDnisActiveSessions": ccrpDnisActiveSessions,
       "ccrpDnisTotalSessions": ccrpDnisTotalSessions,
       "ccrpDnisPeakActiveSessions": ccrpDnisPeakActiveSessions,
       "ccrpDnisCallTypeRejected": ccrpDnisCallTypeRejected,
       "ccrpCDStatistics": ccrpCDStatistics,
       "ccrpCDStatisticsTable": ccrpCDStatisticsTable,
       "ccrpCDStatisticsEntry": ccrpCDStatisticsEntry,
       "ccrpCDRejected": ccrpCDRejected,
       "ccrpMIBNotificationPrefix": ccrpMIBNotificationPrefix,
       "ccrpMIBConformance": ccrpMIBConformance,
       "ccrpMIBCompliances": ccrpMIBCompliances,
       "ccrpMIBCompliance": ccrpMIBCompliance,
       "ccrpMIBGroups": ccrpMIBGroups,
       "ccrpGeneralConfigGroup": ccrpGeneralConfigGroup,
       "ccrpDnisConfigGroup": ccrpDnisConfigGroup,
       "ccrpCDConfigGroup": ccrpCDConfigGroup,
       "ccrpResourceConfigGroup": ccrpResourceConfigGroup,
       "ccrpCPConfigGroup": ccrpCPConfigGroup,
       "ccrpCPStatisticsGroup": ccrpCPStatisticsGroup,
       "ccrpDnisStatisticsGroup": ccrpDnisStatisticsGroup,
       "ccrpCDStatisticsGroup": ccrpCDStatisticsGroup}
)
