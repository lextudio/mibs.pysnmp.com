# SNMP MIB module (CISCO-ITP-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:13 2024
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

(CItpTcAclId,
 CItpTcEncodingSchemeValue,
 CItpTcGlobalTitleSelector,
 CItpTcNAI,
 CItpTcNumberingPlan,
 CItpTcPointCode,
 CItpTcPointCodeMask,
 CItpTcServiceIndicator,
 CItpTcSubSystemNumber,
 CItpTcSubSystemNumberMask,
 CItpTcTranslationType) = mibBuilder.importSymbols(
    "CISCO-ITP-TC-MIB",
    "CItpTcAclId",
    "CItpTcEncodingSchemeValue",
    "CItpTcGlobalTitleSelector",
    "CItpTcNAI",
    "CItpTcNumberingPlan",
    "CItpTcPointCode",
    "CItpTcPointCodeMask",
    "CItpTcServiceIndicator",
    "CItpTcSubSystemNumber",
    "CItpTcSubSystemNumberMask",
    "CItpTcTranslationType")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoItpAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 227)
)
ciscoItpAclMIB.setRevisions(
        ("2001-08-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CItpAclAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("discard", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CItpAclMIBNotifs_ObjectIdentity = ObjectIdentity
cItpAclMIBNotifs = _CItpAclMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 0)
)
_CItpAclMIBObjects_ObjectIdentity = ObjectIdentity
cItpAclMIBObjects = _CItpAclMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1)
)
_CItpAclScalars_ObjectIdentity = ObjectIdentity
cItpAclScalars = _CItpAclScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 1)
)
_CItpAclConfigLastChanged_Type = TimeStamp
_CItpAclConfigLastChanged_Object = MibScalar
cItpAclConfigLastChanged = _CItpAclConfigLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 1, 1),
    _CItpAclConfigLastChanged_Type()
)
cItpAclConfigLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpAclConfigLastChanged.setStatus("current")
_CItpAclConfig_ObjectIdentity = ObjectIdentity
cItpAclConfig = _CItpAclConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2)
)
_CItpAclTable_Object = MibTable
cItpAclTable = _CItpAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cItpAclTable.setStatus("current")
_CItpAclTableEntry_Object = MibTableRow
cItpAclTableEntry = _CItpAclTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1)
)
cItpAclTableEntry.setIndexNames(
    (0, "CISCO-ITP-ACL-MIB", "cItpAclId"),
    (0, "CISCO-ITP-ACL-MIB", "cItpAclEntryType"),
    (0, "CISCO-ITP-ACL-MIB", "cItpAclEntryNumber"),
)
if mibBuilder.loadTexts:
    cItpAclTableEntry.setStatus("current")
_CItpAclId_Type = CItpTcAclId
_CItpAclId_Object = MibTableColumn
cItpAclId = _CItpAclId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 1),
    _CItpAclId_Type()
)
cItpAclId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpAclId.setStatus("current")


class _CItpAclEntryType_Type(Integer32):
    """Custom type cItpAclEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("comment", 1),
          ("entry", 2))
    )


_CItpAclEntryType_Type.__name__ = "Integer32"
_CItpAclEntryType_Object = MibTableColumn
cItpAclEntryType = _CItpAclEntryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 2),
    _CItpAclEntryType_Type()
)
cItpAclEntryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpAclEntryType.setStatus("current")


class _CItpAclEntryNumber_Type(Unsigned32):
    """Custom type cItpAclEntryNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CItpAclEntryNumber_Type.__name__ = "Unsigned32"
_CItpAclEntryNumber_Object = MibTableColumn
cItpAclEntryNumber = _CItpAclEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 3),
    _CItpAclEntryNumber_Type()
)
cItpAclEntryNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpAclEntryNumber.setStatus("current")


class _CItpAclAction_Type(CItpAclAction):
    """Custom type cItpAclAction based on CItpAclAction"""


_CItpAclAction_Object = MibTableColumn
cItpAclAction = _CItpAclAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 4),
    _CItpAclAction_Type()
)
cItpAclAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclAction.setStatus("current")


class _CItpAclParameters_Type(Bits):
    """Custom type cItpAclParameters based on Bits"""
    namedValues = NamedValues(
        *(("aft", 12),
          ("aftMask", 13),
          ("all", 14),
          ("cdpa", 9),
          ("cdpaMask", 10),
          ("cgpa", 7),
          ("cgpaMask", 8),
          ("comment", 6),
          ("dpc", 1),
          ("dpcMask", 2),
          ("opc", 3),
          ("opcMask", 4),
          ("pattern", 5),
          ("selector", 11),
          ("si", 0))
    )

_CItpAclParameters_Type.__name__ = "Bits"
_CItpAclParameters_Object = MibTableColumn
cItpAclParameters = _CItpAclParameters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 5),
    _CItpAclParameters_Type()
)
cItpAclParameters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclParameters.setStatus("current")
_CItpAclDpc_Type = CItpTcPointCode
_CItpAclDpc_Object = MibTableColumn
cItpAclDpc = _CItpAclDpc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 6),
    _CItpAclDpc_Type()
)
cItpAclDpc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclDpc.setStatus("current")
_CItpAclDpcMask_Type = CItpTcPointCodeMask
_CItpAclDpcMask_Object = MibTableColumn
cItpAclDpcMask = _CItpAclDpcMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 7),
    _CItpAclDpcMask_Type()
)
cItpAclDpcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclDpcMask.setStatus("current")
_CItpAclOpc_Type = CItpTcPointCode
_CItpAclOpc_Object = MibTableColumn
cItpAclOpc = _CItpAclOpc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 8),
    _CItpAclOpc_Type()
)
cItpAclOpc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclOpc.setStatus("current")
_CItpAclOpcMask_Type = CItpTcPointCodeMask
_CItpAclOpcMask_Object = MibTableColumn
cItpAclOpcMask = _CItpAclOpcMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 9),
    _CItpAclOpcMask_Type()
)
cItpAclOpcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclOpcMask.setStatus("current")
_CItpAclSi_Type = CItpTcServiceIndicator
_CItpAclSi_Object = MibTableColumn
cItpAclSi = _CItpAclSi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 10),
    _CItpAclSi_Type()
)
cItpAclSi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclSi.setStatus("current")


class _CItpAclPattern_Type(SnmpAdminString):
    """Custom type cItpAclPattern based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CItpAclPattern_Type.__name__ = "SnmpAdminString"
_CItpAclPattern_Object = MibTableColumn
cItpAclPattern = _CItpAclPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 11),
    _CItpAclPattern_Type()
)
cItpAclPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclPattern.setStatus("current")


class _CItpAclOffset_Type(Unsigned32):
    """Custom type cItpAclOffset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CItpAclOffset_Type.__name__ = "Unsigned32"
_CItpAclOffset_Object = MibTableColumn
cItpAclOffset = _CItpAclOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 12),
    _CItpAclOffset_Type()
)
cItpAclOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclOffset.setStatus("current")


class _CItpAclComment_Type(SnmpAdminString):
    """Custom type cItpAclComment based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CItpAclComment_Type.__name__ = "SnmpAdminString"
_CItpAclComment_Object = MibTableColumn
cItpAclComment = _CItpAclComment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 13),
    _CItpAclComment_Type()
)
cItpAclComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclComment.setStatus("current")
_CItpAclCgpa_Type = CItpTcPointCode
_CItpAclCgpa_Object = MibTableColumn
cItpAclCgpa = _CItpAclCgpa_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 14),
    _CItpAclCgpa_Type()
)
cItpAclCgpa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclCgpa.setStatus("current")
_CItpAclCgpaMask_Type = CItpTcPointCodeMask
_CItpAclCgpaMask_Object = MibTableColumn
cItpAclCgpaMask = _CItpAclCgpaMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 15),
    _CItpAclCgpaMask_Type()
)
cItpAclCgpaMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclCgpaMask.setStatus("current")
_CItpAclCgpaSsn_Type = CItpTcSubSystemNumber
_CItpAclCgpaSsn_Object = MibTableColumn
cItpAclCgpaSsn = _CItpAclCgpaSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 16),
    _CItpAclCgpaSsn_Type()
)
cItpAclCgpaSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclCgpaSsn.setStatus("current")
_CItpAclCgpaSsnMask_Type = CItpTcSubSystemNumberMask
_CItpAclCgpaSsnMask_Object = MibTableColumn
cItpAclCgpaSsnMask = _CItpAclCgpaSsnMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 17),
    _CItpAclCgpaSsnMask_Type()
)
cItpAclCgpaSsnMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclCgpaSsnMask.setStatus("current")
_CItpAclCdpa_Type = CItpTcPointCode
_CItpAclCdpa_Object = MibTableColumn
cItpAclCdpa = _CItpAclCdpa_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 18),
    _CItpAclCdpa_Type()
)
cItpAclCdpa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclCdpa.setStatus("current")
_CItpAclCdpaMask_Type = CItpTcPointCodeMask
_CItpAclCdpaMask_Object = MibTableColumn
cItpAclCdpaMask = _CItpAclCdpaMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 19),
    _CItpAclCdpaMask_Type()
)
cItpAclCdpaMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclCdpaMask.setStatus("current")
_CItpAclCdpaSsn_Type = CItpTcSubSystemNumber
_CItpAclCdpaSsn_Object = MibTableColumn
cItpAclCdpaSsn = _CItpAclCdpaSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 20),
    _CItpAclCdpaSsn_Type()
)
cItpAclCdpaSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclCdpaSsn.setStatus("current")
_CItpAclCdpaSsnMask_Type = CItpTcSubSystemNumberMask
_CItpAclCdpaSsnMask_Object = MibTableColumn
cItpAclCdpaSsnMask = _CItpAclCdpaSsnMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 21),
    _CItpAclCdpaSsnMask_Type()
)
cItpAclCdpaSsnMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclCdpaSsnMask.setStatus("current")
_CItpAclGtiSelector_Type = CItpTcGlobalTitleSelector
_CItpAclGtiSelector_Object = MibTableColumn
cItpAclGtiSelector = _CItpAclGtiSelector_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 22),
    _CItpAclGtiSelector_Type()
)
cItpAclGtiSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclGtiSelector.setStatus("current")
_CItpAclGtiTranslateType_Type = CItpTcTranslationType
_CItpAclGtiTranslateType_Object = MibTableColumn
cItpAclGtiTranslateType = _CItpAclGtiTranslateType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 23),
    _CItpAclGtiTranslateType_Type()
)
cItpAclGtiTranslateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclGtiTranslateType.setStatus("current")
_CItpAclGtiNumberingPlan_Type = CItpTcNumberingPlan
_CItpAclGtiNumberingPlan_Object = MibTableColumn
cItpAclGtiNumberingPlan = _CItpAclGtiNumberingPlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 24),
    _CItpAclGtiNumberingPlan_Type()
)
cItpAclGtiNumberingPlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclGtiNumberingPlan.setStatus("current")
_CItpAclGtiNai_Type = CItpTcNAI
_CItpAclGtiNai_Object = MibTableColumn
cItpAclGtiNai = _CItpAclGtiNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 25),
    _CItpAclGtiNai_Type()
)
cItpAclGtiNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclGtiNai.setStatus("current")
_CItpAclGtiEsv_Type = CItpTcEncodingSchemeValue
_CItpAclGtiEsv_Object = MibTableColumn
cItpAclGtiEsv = _CItpAclGtiEsv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 26),
    _CItpAclGtiEsv_Type()
)
cItpAclGtiEsv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclGtiEsv.setStatus("current")
_CItpAclAft_Type = CItpTcPointCode
_CItpAclAft_Object = MibTableColumn
cItpAclAft = _CItpAclAft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 27),
    _CItpAclAft_Type()
)
cItpAclAft.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclAft.setStatus("current")
_CItpAclAftMask_Type = CItpTcPointCodeMask
_CItpAclAftMask_Object = MibTableColumn
cItpAclAftMask = _CItpAclAftMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 28),
    _CItpAclAftMask_Type()
)
cItpAclAftMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclAftMask.setStatus("current")
_CItpAclAftSsn_Type = CItpTcSubSystemNumber
_CItpAclAftSsn_Object = MibTableColumn
cItpAclAftSsn = _CItpAclAftSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 29),
    _CItpAclAftSsn_Type()
)
cItpAclAftSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclAftSsn.setStatus("current")
_CItpAclAftSsnMask_Type = CItpTcSubSystemNumberMask
_CItpAclAftSsnMask_Object = MibTableColumn
cItpAclAftSsnMask = _CItpAclAftSsnMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 30),
    _CItpAclAftSsnMask_Type()
)
cItpAclAftSsnMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclAftSsnMask.setStatus("current")
_CItpAclRowStatus_Type = RowStatus
_CItpAclRowStatus_Object = MibTableColumn
cItpAclRowStatus = _CItpAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 1, 2, 1, 1, 31),
    _CItpAclRowStatus_Type()
)
cItpAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpAclRowStatus.setStatus("current")
_CItpAclMIBConformance_ObjectIdentity = ObjectIdentity
cItpAclMIBConformance = _CItpAclMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 2)
)
_CItpAclMIBCompliances_ObjectIdentity = ObjectIdentity
cItpAclMIBCompliances = _CItpAclMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 2, 1)
)
_CItpAclMIBGroups_ObjectIdentity = ObjectIdentity
cItpAclMIBGroups = _CItpAclMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 2, 2)
)

# Managed Objects groups

cItpAclScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 2, 2, 1)
)
cItpAclScalarGroup.setObjects(
    ("CISCO-ITP-ACL-MIB", "cItpAclConfigLastChanged")
)
if mibBuilder.loadTexts:
    cItpAclScalarGroup.setStatus("current")

cItpAclAccessListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 2, 2, 2)
)
cItpAclAccessListGroup.setObjects(
      *(("CISCO-ITP-ACL-MIB", "cItpAclAction"),
        ("CISCO-ITP-ACL-MIB", "cItpAclParameters"),
        ("CISCO-ITP-ACL-MIB", "cItpAclDpc"),
        ("CISCO-ITP-ACL-MIB", "cItpAclDpcMask"),
        ("CISCO-ITP-ACL-MIB", "cItpAclOpc"),
        ("CISCO-ITP-ACL-MIB", "cItpAclOpcMask"),
        ("CISCO-ITP-ACL-MIB", "cItpAclSi"),
        ("CISCO-ITP-ACL-MIB", "cItpAclPattern"),
        ("CISCO-ITP-ACL-MIB", "cItpAclOffset"),
        ("CISCO-ITP-ACL-MIB", "cItpAclComment"),
        ("CISCO-ITP-ACL-MIB", "cItpAclCgpa"),
        ("CISCO-ITP-ACL-MIB", "cItpAclCgpaMask"),
        ("CISCO-ITP-ACL-MIB", "cItpAclCgpaSsn"),
        ("CISCO-ITP-ACL-MIB", "cItpAclCgpaSsnMask"),
        ("CISCO-ITP-ACL-MIB", "cItpAclCdpa"),
        ("CISCO-ITP-ACL-MIB", "cItpAclCdpaMask"),
        ("CISCO-ITP-ACL-MIB", "cItpAclCdpaSsn"),
        ("CISCO-ITP-ACL-MIB", "cItpAclCdpaSsnMask"),
        ("CISCO-ITP-ACL-MIB", "cItpAclGtiSelector"),
        ("CISCO-ITP-ACL-MIB", "cItpAclGtiTranslateType"),
        ("CISCO-ITP-ACL-MIB", "cItpAclGtiNumberingPlan"),
        ("CISCO-ITP-ACL-MIB", "cItpAclGtiNai"),
        ("CISCO-ITP-ACL-MIB", "cItpAclGtiEsv"),
        ("CISCO-ITP-ACL-MIB", "cItpAclAft"),
        ("CISCO-ITP-ACL-MIB", "cItpAclAftMask"),
        ("CISCO-ITP-ACL-MIB", "cItpAclAftSsn"),
        ("CISCO-ITP-ACL-MIB", "cItpAclAftSsnMask"),
        ("CISCO-ITP-ACL-MIB", "cItpAclRowStatus"))
)
if mibBuilder.loadTexts:
    cItpAclAccessListGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cItpAclMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 227, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cItpAclMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-ACL-MIB",
    **{"CItpAclAction": CItpAclAction,
       "ciscoItpAclMIB": ciscoItpAclMIB,
       "cItpAclMIBNotifs": cItpAclMIBNotifs,
       "cItpAclMIBObjects": cItpAclMIBObjects,
       "cItpAclScalars": cItpAclScalars,
       "cItpAclConfigLastChanged": cItpAclConfigLastChanged,
       "cItpAclConfig": cItpAclConfig,
       "cItpAclTable": cItpAclTable,
       "cItpAclTableEntry": cItpAclTableEntry,
       "cItpAclId": cItpAclId,
       "cItpAclEntryType": cItpAclEntryType,
       "cItpAclEntryNumber": cItpAclEntryNumber,
       "cItpAclAction": cItpAclAction,
       "cItpAclParameters": cItpAclParameters,
       "cItpAclDpc": cItpAclDpc,
       "cItpAclDpcMask": cItpAclDpcMask,
       "cItpAclOpc": cItpAclOpc,
       "cItpAclOpcMask": cItpAclOpcMask,
       "cItpAclSi": cItpAclSi,
       "cItpAclPattern": cItpAclPattern,
       "cItpAclOffset": cItpAclOffset,
       "cItpAclComment": cItpAclComment,
       "cItpAclCgpa": cItpAclCgpa,
       "cItpAclCgpaMask": cItpAclCgpaMask,
       "cItpAclCgpaSsn": cItpAclCgpaSsn,
       "cItpAclCgpaSsnMask": cItpAclCgpaSsnMask,
       "cItpAclCdpa": cItpAclCdpa,
       "cItpAclCdpaMask": cItpAclCdpaMask,
       "cItpAclCdpaSsn": cItpAclCdpaSsn,
       "cItpAclCdpaSsnMask": cItpAclCdpaSsnMask,
       "cItpAclGtiSelector": cItpAclGtiSelector,
       "cItpAclGtiTranslateType": cItpAclGtiTranslateType,
       "cItpAclGtiNumberingPlan": cItpAclGtiNumberingPlan,
       "cItpAclGtiNai": cItpAclGtiNai,
       "cItpAclGtiEsv": cItpAclGtiEsv,
       "cItpAclAft": cItpAclAft,
       "cItpAclAftMask": cItpAclAftMask,
       "cItpAclAftSsn": cItpAclAftSsn,
       "cItpAclAftSsnMask": cItpAclAftSsnMask,
       "cItpAclRowStatus": cItpAclRowStatus,
       "cItpAclMIBConformance": cItpAclMIBConformance,
       "cItpAclMIBCompliances": cItpAclMIBCompliances,
       "cItpAclMIBCompliance": cItpAclMIBCompliance,
       "cItpAclMIBGroups": cItpAclMIBGroups,
       "cItpAclScalarGroup": cItpAclScalarGroup,
       "cItpAclAccessListGroup": cItpAclAccessListGroup}
)
