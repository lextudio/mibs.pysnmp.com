# SNMP MIB module (ATT-CNM-SMDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATT-CNM-SMDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:19 2024
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



class SMDSAddress(OctetString):
    """Custom type SMDSAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Att_2_ObjectIdentity = ObjectIdentity
att_2 = _Att_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74)
)
_Att_products_ObjectIdentity = ObjectIdentity
att_products = _Att_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 1)
)
_Att_cnmAgent_ObjectIdentity = ObjectIdentity
att_cnmAgent = _Att_cnmAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 1, 9)
)
_Att_mgmt_ObjectIdentity = ObjectIdentity
att_mgmt = _Att_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2)
)
_Att_cnm_ObjectIdentity = ObjectIdentity
att_cnm = _Att_cnm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 15)
)
_Att_cnm_smds_ObjectIdentity = ObjectIdentity
att_cnm_smds = _Att_cnm_smds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6)
)
_AttCNMsmdsConfigTable_Object = MibTable
attCNMsmdsConfigTable = _AttCNMsmdsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1)
)
if mibBuilder.loadTexts:
    attCNMsmdsConfigTable.setStatus("mandatory")
_AttCNMsmdsConfigEntry_Object = MibTableRow
attCNMsmdsConfigEntry = _AttCNMsmdsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1)
)
attCNMsmdsConfigEntry.setIndexNames(
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsConfigIndex"),
)
if mibBuilder.loadTexts:
    attCNMsmdsConfigEntry.setStatus("mandatory")
_AttCNMsmdsConfigIndex_Type = Integer32
_AttCNMsmdsConfigIndex_Object = MibTableColumn
attCNMsmdsConfigIndex = _AttCNMsmdsConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 1),
    _AttCNMsmdsConfigIndex_Type()
)
attCNMsmdsConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsConfigIndex.setStatus("mandatory")


class _AttCNMsmdsAccessClass_Type(Integer32):
    """Custom type attCNMsmdsAccessClass based on Integer32"""
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
        *(("accessClass1", 2),
          ("accessClass2", 3),
          ("accessClass3", 4),
          ("accessClass4", 5),
          ("accessClass5", 6),
          ("noClass", 1))
    )


_AttCNMsmdsAccessClass_Type.__name__ = "Integer32"
_AttCNMsmdsAccessClass_Object = MibTableColumn
attCNMsmdsAccessClass = _AttCNMsmdsAccessClass_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 2),
    _AttCNMsmdsAccessClass_Type()
)
attCNMsmdsAccessClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsAccessClass.setStatus("mandatory")


class _AttCNMsmdsMCDUsIn_Type(Integer32):
    """Custom type attCNMsmdsMCDUsIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mcdusIn1", 1),
          ("mcdusIn16", 2))
    )


_AttCNMsmdsMCDUsIn_Type.__name__ = "Integer32"
_AttCNMsmdsMCDUsIn_Object = MibTableColumn
attCNMsmdsMCDUsIn = _AttCNMsmdsMCDUsIn_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 3),
    _AttCNMsmdsMCDUsIn_Type()
)
attCNMsmdsMCDUsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsMCDUsIn.setStatus("mandatory")


class _AttCNMsmdsMCDUsOut_Type(Integer32):
    """Custom type attCNMsmdsMCDUsOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mcdusOut1", 1),
          ("mcdusOut16", 2))
    )


_AttCNMsmdsMCDUsOut_Type.__name__ = "Integer32"
_AttCNMsmdsMCDUsOut_Object = MibTableColumn
attCNMsmdsMCDUsOut = _AttCNMsmdsMCDUsOut_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 4),
    _AttCNMsmdsMCDUsOut_Type()
)
attCNMsmdsMCDUsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsMCDUsOut.setStatus("mandatory")


class _AttCNMsmdsIndivScreenMode_Type(Integer32):
    """Custom type attCNMsmdsIndivScreenMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 2))
    )


_AttCNMsmdsIndivScreenMode_Type.__name__ = "Integer32"
_AttCNMsmdsIndivScreenMode_Object = MibTableColumn
attCNMsmdsIndivScreenMode = _AttCNMsmdsIndivScreenMode_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 5),
    _AttCNMsmdsIndivScreenMode_Type()
)
attCNMsmdsIndivScreenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsIndivScreenMode.setStatus("mandatory")


class _AttCNMsmdsGroupScreenMode_Type(Integer32):
    """Custom type attCNMsmdsGroupScreenMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 2))
    )


_AttCNMsmdsGroupScreenMode_Type.__name__ = "Integer32"
_AttCNMsmdsGroupScreenMode_Object = MibTableColumn
attCNMsmdsGroupScreenMode = _AttCNMsmdsGroupScreenMode_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 6),
    _AttCNMsmdsGroupScreenMode_Type()
)
attCNMsmdsGroupScreenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsGroupScreenMode.setStatus("mandatory")


class _AttCNMsmdsAddrIndexDescr_Type(DisplayString):
    """Custom type attCNMsmdsAddrIndexDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMsmdsAddrIndexDescr_Type.__name__ = "DisplayString"
_AttCNMsmdsAddrIndexDescr_Object = MibTableColumn
attCNMsmdsAddrIndexDescr = _AttCNMsmdsAddrIndexDescr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 7),
    _AttCNMsmdsAddrIndexDescr_Type()
)
attCNMsmdsAddrIndexDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsAddrIndexDescr.setStatus("mandatory")
_AttCNMsmdsDisagreeMaxIntervals_Type = Integer32
_AttCNMsmdsDisagreeMaxIntervals_Object = MibTableColumn
attCNMsmdsDisagreeMaxIntervals = _AttCNMsmdsDisagreeMaxIntervals_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 8),
    _AttCNMsmdsDisagreeMaxIntervals_Type()
)
attCNMsmdsDisagreeMaxIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsDisagreeMaxIntervals.setStatus("mandatory")
_AttCNMsmdsDisagreeIntervalLen_Type = Integer32
_AttCNMsmdsDisagreeIntervalLen_Object = MibTableColumn
attCNMsmdsDisagreeIntervalLen = _AttCNMsmdsDisagreeIntervalLen_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 1, 1, 9),
    _AttCNMsmdsDisagreeIntervalLen_Type()
)
attCNMsmdsDisagreeIntervalLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsDisagreeIntervalLen.setStatus("mandatory")
_AttCNMsmdsAddrTable_Object = MibTable
attCNMsmdsAddrTable = _AttCNMsmdsAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 2)
)
if mibBuilder.loadTexts:
    attCNMsmdsAddrTable.setStatus("mandatory")
_AttCNMsmdsAddrEntry_Object = MibTableRow
attCNMsmdsAddrEntry = _AttCNMsmdsAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 2, 1)
)
attCNMsmdsAddrEntry.setIndexNames(
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsAddrCountryIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsAddrAreaIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsAddrSubscriberIndex"),
)
if mibBuilder.loadTexts:
    attCNMsmdsAddrEntry.setStatus("mandatory")
_AttCNMsmdsAddrCountryIndex_Type = Integer32
_AttCNMsmdsAddrCountryIndex_Object = MibTableColumn
attCNMsmdsAddrCountryIndex = _AttCNMsmdsAddrCountryIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 2, 1, 1),
    _AttCNMsmdsAddrCountryIndex_Type()
)
attCNMsmdsAddrCountryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsAddrCountryIndex.setStatus("mandatory")
_AttCNMsmdsAddrAreaIndex_Type = Integer32
_AttCNMsmdsAddrAreaIndex_Object = MibTableColumn
attCNMsmdsAddrAreaIndex = _AttCNMsmdsAddrAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 2, 1, 2),
    _AttCNMsmdsAddrAreaIndex_Type()
)
attCNMsmdsAddrAreaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsAddrAreaIndex.setStatus("mandatory")
_AttCNMsmdsAddrSubscriberIndex_Type = Integer32
_AttCNMsmdsAddrSubscriberIndex_Object = MibTableColumn
attCNMsmdsAddrSubscriberIndex = _AttCNMsmdsAddrSubscriberIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 2, 1, 3),
    _AttCNMsmdsAddrSubscriberIndex_Type()
)
attCNMsmdsAddrSubscriberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsAddrSubscriberIndex.setStatus("mandatory")
_AttCNMsmdsAddressOnSNI_Type = SMDSAddress
_AttCNMsmdsAddressOnSNI_Object = MibTableColumn
attCNMsmdsAddressOnSNI = _AttCNMsmdsAddressOnSNI_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 2, 1, 4),
    _AttCNMsmdsAddressOnSNI_Type()
)
attCNMsmdsAddressOnSNI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsAddressOnSNI.setStatus("mandatory")
_AttCNMsmdsInterfaceIndex_Type = Integer32
_AttCNMsmdsInterfaceIndex_Object = MibTableColumn
attCNMsmdsInterfaceIndex = _AttCNMsmdsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 2, 1, 5),
    _AttCNMsmdsInterfaceIndex_Type()
)
attCNMsmdsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsInterfaceIndex.setStatus("mandatory")
_AttCNMsmdsIndScrTable_Object = MibTable
attCNMsmdsIndScrTable = _AttCNMsmdsIndScrTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 3)
)
if mibBuilder.loadTexts:
    attCNMsmdsIndScrTable.setStatus("mandatory")
_AttCNMsmdsIndScrEntry_Object = MibTableRow
attCNMsmdsIndScrEntry = _AttCNMsmdsIndScrEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 3, 1)
)
attCNMsmdsIndScrEntry.setIndexNames(
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsIndScrIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsIndScrCountryIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsIndScrAreaIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsIndScrSubscriberIndex"),
)
if mibBuilder.loadTexts:
    attCNMsmdsIndScrEntry.setStatus("mandatory")
_AttCNMsmdsIndScrIndex_Type = Integer32
_AttCNMsmdsIndScrIndex_Object = MibTableColumn
attCNMsmdsIndScrIndex = _AttCNMsmdsIndScrIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 3, 1, 1),
    _AttCNMsmdsIndScrIndex_Type()
)
attCNMsmdsIndScrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsIndScrIndex.setStatus("mandatory")
_AttCNMsmdsIndScrCountryIndex_Type = Integer32
_AttCNMsmdsIndScrCountryIndex_Object = MibTableColumn
attCNMsmdsIndScrCountryIndex = _AttCNMsmdsIndScrCountryIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 3, 1, 2),
    _AttCNMsmdsIndScrCountryIndex_Type()
)
attCNMsmdsIndScrCountryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsIndScrCountryIndex.setStatus("mandatory")
_AttCNMsmdsIndScrAreaIndex_Type = Integer32
_AttCNMsmdsIndScrAreaIndex_Object = MibTableColumn
attCNMsmdsIndScrAreaIndex = _AttCNMsmdsIndScrAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 3, 1, 3),
    _AttCNMsmdsIndScrAreaIndex_Type()
)
attCNMsmdsIndScrAreaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsIndScrAreaIndex.setStatus("mandatory")
_AttCNMsmdsIndScrSubscriberIndex_Type = Integer32
_AttCNMsmdsIndScrSubscriberIndex_Object = MibTableColumn
attCNMsmdsIndScrSubscriberIndex = _AttCNMsmdsIndScrSubscriberIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 3, 1, 4),
    _AttCNMsmdsIndScrSubscriberIndex_Type()
)
attCNMsmdsIndScrSubscriberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsIndScrSubscriberIndex.setStatus("mandatory")
_AttCNMsmdsIndivScreenAddress_Type = SMDSAddress
_AttCNMsmdsIndivScreenAddress_Object = MibTableColumn
attCNMsmdsIndivScreenAddress = _AttCNMsmdsIndivScreenAddress_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 3, 1, 5),
    _AttCNMsmdsIndivScreenAddress_Type()
)
attCNMsmdsIndivScreenAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsIndivScreenAddress.setStatus("mandatory")
_AttCNMsmdsGrpScrTable_Object = MibTable
attCNMsmdsGrpScrTable = _AttCNMsmdsGrpScrTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 4)
)
if mibBuilder.loadTexts:
    attCNMsmdsGrpScrTable.setStatus("mandatory")
_AttCNMsmdsGrpScrEntry_Object = MibTableRow
attCNMsmdsGrpScrEntry = _AttCNMsmdsGrpScrEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 4, 1)
)
attCNMsmdsGrpScrEntry.setIndexNames(
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpScrIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpScrCountryIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpScrAreaIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpScrSubscriberIndex"),
)
if mibBuilder.loadTexts:
    attCNMsmdsGrpScrEntry.setStatus("mandatory")
_AttCNMsmdsGrpScrIndex_Type = Integer32
_AttCNMsmdsGrpScrIndex_Object = MibTableColumn
attCNMsmdsGrpScrIndex = _AttCNMsmdsGrpScrIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 4, 1, 1),
    _AttCNMsmdsGrpScrIndex_Type()
)
attCNMsmdsGrpScrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsGrpScrIndex.setStatus("mandatory")
_AttCNMsmdsGrpScrCountryIndex_Type = Integer32
_AttCNMsmdsGrpScrCountryIndex_Object = MibTableColumn
attCNMsmdsGrpScrCountryIndex = _AttCNMsmdsGrpScrCountryIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 4, 1, 2),
    _AttCNMsmdsGrpScrCountryIndex_Type()
)
attCNMsmdsGrpScrCountryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsGrpScrCountryIndex.setStatus("mandatory")
_AttCNMsmdsGrpScrAreaIndex_Type = Integer32
_AttCNMsmdsGrpScrAreaIndex_Object = MibTableColumn
attCNMsmdsGrpScrAreaIndex = _AttCNMsmdsGrpScrAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 4, 1, 3),
    _AttCNMsmdsGrpScrAreaIndex_Type()
)
attCNMsmdsGrpScrAreaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsGrpScrAreaIndex.setStatus("mandatory")
_AttCNMsmdsGrpScrSubscriberIndex_Type = Integer32
_AttCNMsmdsGrpScrSubscriberIndex_Object = MibTableColumn
attCNMsmdsGrpScrSubscriberIndex = _AttCNMsmdsGrpScrSubscriberIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 4, 1, 4),
    _AttCNMsmdsGrpScrSubscriberIndex_Type()
)
attCNMsmdsGrpScrSubscriberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsGrpScrSubscriberIndex.setStatus("mandatory")
_AttCNMsmdsGroupScreenAddress_Type = SMDSAddress
_AttCNMsmdsGroupScreenAddress_Object = MibTableColumn
attCNMsmdsGroupScreenAddress = _AttCNMsmdsGroupScreenAddress_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 4, 1, 5),
    _AttCNMsmdsGroupScreenAddress_Type()
)
attCNMsmdsGroupScreenAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsGroupScreenAddress.setStatus("mandatory")
_AttCNMsmdsMemGrpTable_Object = MibTable
attCNMsmdsMemGrpTable = _AttCNMsmdsMemGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5)
)
if mibBuilder.loadTexts:
    attCNMsmdsMemGrpTable.setStatus("mandatory")
_AttCNMsmdsMemGrpEntry_Object = MibTableRow
attCNMsmdsMemGrpEntry = _AttCNMsmdsMemGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1)
)
attCNMsmdsMemGrpEntry.setIndexNames(
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsMemGrpMemberCountryIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsMemGrpMemberAreaIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsMemGrpMemberSubscriberIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsMemGrpGroupCountryIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsMemGrpGroupAreaIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsMemGrpGroupSubscriberIndex"),
)
if mibBuilder.loadTexts:
    attCNMsmdsMemGrpEntry.setStatus("mandatory")
_AttCNMsmdsMemGrpMemberCountryIndex_Type = Integer32
_AttCNMsmdsMemGrpMemberCountryIndex_Object = MibTableColumn
attCNMsmdsMemGrpMemberCountryIndex = _AttCNMsmdsMemGrpMemberCountryIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1, 1),
    _AttCNMsmdsMemGrpMemberCountryIndex_Type()
)
attCNMsmdsMemGrpMemberCountryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsMemGrpMemberCountryIndex.setStatus("mandatory")
_AttCNMsmdsMemGrpMemberAreaIndex_Type = Integer32
_AttCNMsmdsMemGrpMemberAreaIndex_Object = MibTableColumn
attCNMsmdsMemGrpMemberAreaIndex = _AttCNMsmdsMemGrpMemberAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1, 2),
    _AttCNMsmdsMemGrpMemberAreaIndex_Type()
)
attCNMsmdsMemGrpMemberAreaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsMemGrpMemberAreaIndex.setStatus("mandatory")
_AttCNMsmdsMemGrpMemberSubscriberIndex_Type = Integer32
_AttCNMsmdsMemGrpMemberSubscriberIndex_Object = MibTableColumn
attCNMsmdsMemGrpMemberSubscriberIndex = _AttCNMsmdsMemGrpMemberSubscriberIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1, 3),
    _AttCNMsmdsMemGrpMemberSubscriberIndex_Type()
)
attCNMsmdsMemGrpMemberSubscriberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsMemGrpMemberSubscriberIndex.setStatus("mandatory")
_AttCNMsmdsMemGrpGroupCountryIndex_Type = Integer32
_AttCNMsmdsMemGrpGroupCountryIndex_Object = MibTableColumn
attCNMsmdsMemGrpGroupCountryIndex = _AttCNMsmdsMemGrpGroupCountryIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1, 4),
    _AttCNMsmdsMemGrpGroupCountryIndex_Type()
)
attCNMsmdsMemGrpGroupCountryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsMemGrpGroupCountryIndex.setStatus("mandatory")
_AttCNMsmdsMemGrpGroupAreaIndex_Type = Integer32
_AttCNMsmdsMemGrpGroupAreaIndex_Object = MibTableColumn
attCNMsmdsMemGrpGroupAreaIndex = _AttCNMsmdsMemGrpGroupAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1, 5),
    _AttCNMsmdsMemGrpGroupAreaIndex_Type()
)
attCNMsmdsMemGrpGroupAreaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsMemGrpGroupAreaIndex.setStatus("mandatory")
_AttCNMsmdsMemGrpGroupSubscriberIndex_Type = Integer32
_AttCNMsmdsMemGrpGroupSubscriberIndex_Object = MibTableColumn
attCNMsmdsMemGrpGroupSubscriberIndex = _AttCNMsmdsMemGrpGroupSubscriberIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1, 6),
    _AttCNMsmdsMemGrpGroupSubscriberIndex_Type()
)
attCNMsmdsMemGrpGroupSubscriberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsMemGrpGroupSubscriberIndex.setStatus("mandatory")
_AttCNMsmdsMemberAddress_Type = SMDSAddress
_AttCNMsmdsMemberAddress_Object = MibTableColumn
attCNMsmdsMemberAddress = _AttCNMsmdsMemberAddress_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1, 7),
    _AttCNMsmdsMemberAddress_Type()
)
attCNMsmdsMemberAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsMemberAddress.setStatus("mandatory")
_AttCNMsmdsAssociatedGroup_Type = SMDSAddress
_AttCNMsmdsAssociatedGroup_Object = MibTableColumn
attCNMsmdsAssociatedGroup = _AttCNMsmdsAssociatedGroup_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 5, 1, 8),
    _AttCNMsmdsAssociatedGroup_Type()
)
attCNMsmdsAssociatedGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsAssociatedGroup.setStatus("mandatory")
_AttCNMsmdsGrpMemTable_Object = MibTable
attCNMsmdsGrpMemTable = _AttCNMsmdsGrpMemTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6)
)
if mibBuilder.loadTexts:
    attCNMsmdsGrpMemTable.setStatus("mandatory")
_AttCNMsmdsGrpMemEntry_Object = MibTableRow
attCNMsmdsGrpMemEntry = _AttCNMsmdsGrpMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1)
)
attCNMsmdsGrpMemEntry.setIndexNames(
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpMemGroupCountryIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpMemGroupAreaIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpMemGroupSubscriberIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpMemMemberCountryIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpMemMemberAreaIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsGrpMemMemberSubscriberIndex"),
)
if mibBuilder.loadTexts:
    attCNMsmdsGrpMemEntry.setStatus("mandatory")
_AttCNMsmdsGrpMemGroupCountryIndex_Type = Integer32
_AttCNMsmdsGrpMemGroupCountryIndex_Object = MibTableColumn
attCNMsmdsGrpMemGroupCountryIndex = _AttCNMsmdsGrpMemGroupCountryIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1, 1),
    _AttCNMsmdsGrpMemGroupCountryIndex_Type()
)
attCNMsmdsGrpMemGroupCountryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsGrpMemGroupCountryIndex.setStatus("mandatory")
_AttCNMsmdsGrpMemGroupAreaIndex_Type = Integer32
_AttCNMsmdsGrpMemGroupAreaIndex_Object = MibTableColumn
attCNMsmdsGrpMemGroupAreaIndex = _AttCNMsmdsGrpMemGroupAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1, 2),
    _AttCNMsmdsGrpMemGroupAreaIndex_Type()
)
attCNMsmdsGrpMemGroupAreaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsGrpMemGroupAreaIndex.setStatus("mandatory")
_AttCNMsmdsGrpMemGroupSubscriberIndex_Type = Integer32
_AttCNMsmdsGrpMemGroupSubscriberIndex_Object = MibTableColumn
attCNMsmdsGrpMemGroupSubscriberIndex = _AttCNMsmdsGrpMemGroupSubscriberIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1, 3),
    _AttCNMsmdsGrpMemGroupSubscriberIndex_Type()
)
attCNMsmdsGrpMemGroupSubscriberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsGrpMemGroupSubscriberIndex.setStatus("mandatory")
_AttCNMsmdsGrpMemMemberCountryIndex_Type = Integer32
_AttCNMsmdsGrpMemMemberCountryIndex_Object = MibTableColumn
attCNMsmdsGrpMemMemberCountryIndex = _AttCNMsmdsGrpMemMemberCountryIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1, 4),
    _AttCNMsmdsGrpMemMemberCountryIndex_Type()
)
attCNMsmdsGrpMemMemberCountryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsGrpMemMemberCountryIndex.setStatus("mandatory")
_AttCNMsmdsGrpMemMemberAreaIndex_Type = Integer32
_AttCNMsmdsGrpMemMemberAreaIndex_Object = MibTableColumn
attCNMsmdsGrpMemMemberAreaIndex = _AttCNMsmdsGrpMemMemberAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1, 5),
    _AttCNMsmdsGrpMemMemberAreaIndex_Type()
)
attCNMsmdsGrpMemMemberAreaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsGrpMemMemberAreaIndex.setStatus("mandatory")
_AttCNMsmdsGrpMemMemberSubscriberIndex_Type = Integer32
_AttCNMsmdsGrpMemMemberSubscriberIndex_Object = MibTableColumn
attCNMsmdsGrpMemMemberSubscriberIndex = _AttCNMsmdsGrpMemMemberSubscriberIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1, 6),
    _AttCNMsmdsGrpMemMemberSubscriberIndex_Type()
)
attCNMsmdsGrpMemMemberSubscriberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    attCNMsmdsGrpMemMemberSubscriberIndex.setStatus("mandatory")
_AttCNMsmdsGroupAddress_Type = SMDSAddress
_AttCNMsmdsGroupAddress_Object = MibTableColumn
attCNMsmdsGroupAddress = _AttCNMsmdsGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1, 7),
    _AttCNMsmdsGroupAddress_Type()
)
attCNMsmdsGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsGroupAddress.setStatus("mandatory")
_AttCNMsmdsGroupMember_Type = SMDSAddress
_AttCNMsmdsGroupMember_Object = MibTableColumn
attCNMsmdsGroupMember = _AttCNMsmdsGroupMember_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 6, 1, 8),
    _AttCNMsmdsGroupMember_Type()
)
attCNMsmdsGroupMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsGroupMember.setStatus("mandatory")
_AttCNMsmdsDisagreeTable_Object = MibTable
attCNMsmdsDisagreeTable = _AttCNMsmdsDisagreeTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7)
)
if mibBuilder.loadTexts:
    attCNMsmdsDisagreeTable.setStatus("mandatory")
_AttCNMsmdsDisagreeEntry_Object = MibTableRow
attCNMsmdsDisagreeEntry = _AttCNMsmdsDisagreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1)
)
attCNMsmdsDisagreeEntry.setIndexNames(
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsDisagreeIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsDisagreeInterval"),
)
if mibBuilder.loadTexts:
    attCNMsmdsDisagreeEntry.setStatus("mandatory")
_AttCNMsmdsDisagreeIndex_Type = Integer32
_AttCNMsmdsDisagreeIndex_Object = MibTableColumn
attCNMsmdsDisagreeIndex = _AttCNMsmdsDisagreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 1),
    _AttCNMsmdsDisagreeIndex_Type()
)
attCNMsmdsDisagreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsDisagreeIndex.setStatus("mandatory")
_AttCNMsmdsDisagreeInterval_Type = Integer32
_AttCNMsmdsDisagreeInterval_Object = MibTableColumn
attCNMsmdsDisagreeInterval = _AttCNMsmdsDisagreeInterval_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 2),
    _AttCNMsmdsDisagreeInterval_Type()
)
attCNMsmdsDisagreeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsDisagreeInterval.setStatus("mandatory")
_AttCNMsmdsDisagreeTimeStamp_Type = Integer32
_AttCNMsmdsDisagreeTimeStamp_Object = MibTableColumn
attCNMsmdsDisagreeTimeStamp = _AttCNMsmdsDisagreeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 3),
    _AttCNMsmdsDisagreeTimeStamp_Type()
)
attCNMsmdsDisagreeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsDisagreeTimeStamp.setStatus("mandatory")


class _AttCNMsmdsDisagreeLocalTime_Type(DisplayString):
    """Custom type attCNMsmdsDisagreeLocalTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMsmdsDisagreeLocalTime_Type.__name__ = "DisplayString"
_AttCNMsmdsDisagreeLocalTime_Object = MibTableColumn
attCNMsmdsDisagreeLocalTime = _AttCNMsmdsDisagreeLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 4),
    _AttCNMsmdsDisagreeLocalTime_Type()
)
attCNMsmdsDisagreeLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsDisagreeLocalTime.setStatus("mandatory")
_AttCNMsmdsAccessClassExceededCounts_Type = Gauge32
_AttCNMsmdsAccessClassExceededCounts_Object = MibTableColumn
attCNMsmdsAccessClassExceededCounts = _AttCNMsmdsAccessClassExceededCounts_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 5),
    _AttCNMsmdsAccessClassExceededCounts_Type()
)
attCNMsmdsAccessClassExceededCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsAccessClassExceededCounts.setStatus("mandatory")
_AttCNMsmdsMCDUsExceededAtIngressCounts_Type = Gauge32
_AttCNMsmdsMCDUsExceededAtIngressCounts_Object = MibTableColumn
attCNMsmdsMCDUsExceededAtIngressCounts = _AttCNMsmdsMCDUsExceededAtIngressCounts_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 6),
    _AttCNMsmdsMCDUsExceededAtIngressCounts_Type()
)
attCNMsmdsMCDUsExceededAtIngressCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsMCDUsExceededAtIngressCounts.setStatus("mandatory")
_AttCNMsmdsMCDUsExceededAtEgressCounts_Type = Gauge32
_AttCNMsmdsMCDUsExceededAtEgressCounts_Object = MibTableColumn
attCNMsmdsMCDUsExceededAtEgressCounts = _AttCNMsmdsMCDUsExceededAtEgressCounts_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 7),
    _AttCNMsmdsMCDUsExceededAtEgressCounts_Type()
)
attCNMsmdsMCDUsExceededAtEgressCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsMCDUsExceededAtEgressCounts.setStatus("mandatory")
_AttCNMsmdsSAScreenViolations_Type = Gauge32
_AttCNMsmdsSAScreenViolations_Object = MibTableColumn
attCNMsmdsSAScreenViolations = _AttCNMsmdsSAScreenViolations_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 8),
    _AttCNMsmdsSAScreenViolations_Type()
)
attCNMsmdsSAScreenViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsSAScreenViolations.setStatus("mandatory")
_AttCNMsmdsDAScreenViolations_Type = Gauge32
_AttCNMsmdsDAScreenViolations_Object = MibTableColumn
attCNMsmdsDAScreenViolations = _AttCNMsmdsDAScreenViolations_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 9),
    _AttCNMsmdsDAScreenViolations_Type()
)
attCNMsmdsDAScreenViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsDAScreenViolations.setStatus("mandatory")
_AttCNMsmdsUnassignedSAs_Type = Gauge32
_AttCNMsmdsUnassignedSAs_Object = MibTableColumn
attCNMsmdsUnassignedSAs = _AttCNMsmdsUnassignedSAs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 10),
    _AttCNMsmdsUnassignedSAs_Type()
)
attCNMsmdsUnassignedSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsUnassignedSAs.setStatus("mandatory")
_AttCNMsmdsDestinationSNIUnavailableCounts_Type = Gauge32
_AttCNMsmdsDestinationSNIUnavailableCounts_Object = MibTableColumn
attCNMsmdsDestinationSNIUnavailableCounts = _AttCNMsmdsDestinationSNIUnavailableCounts_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 7, 1, 11),
    _AttCNMsmdsDestinationSNIUnavailableCounts_Type()
)
attCNMsmdsDestinationSNIUnavailableCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsDestinationSNIUnavailableCounts.setStatus("mandatory")
_AttCNMsmdsDisagreeLogTable_Object = MibTable
attCNMsmdsDisagreeLogTable = _AttCNMsmdsDisagreeLogTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 8)
)
if mibBuilder.loadTexts:
    attCNMsmdsDisagreeLogTable.setStatus("mandatory")
_AttCNMsmdsDisagreeLogEntry_Object = MibTableRow
attCNMsmdsDisagreeLogEntry = _AttCNMsmdsDisagreeLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 8, 1)
)
attCNMsmdsDisagreeLogEntry.setIndexNames(
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsDisagreeLogIndex"),
    (0, "ATT-CNM-SMDS-MIB", "attCNMsmdsDisagreeLogType"),
)
if mibBuilder.loadTexts:
    attCNMsmdsDisagreeLogEntry.setStatus("mandatory")
_AttCNMsmdsDisagreeLogIndex_Type = Integer32
_AttCNMsmdsDisagreeLogIndex_Object = MibTableColumn
attCNMsmdsDisagreeLogIndex = _AttCNMsmdsDisagreeLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 8, 1, 1),
    _AttCNMsmdsDisagreeLogIndex_Type()
)
attCNMsmdsDisagreeLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsDisagreeLogIndex.setStatus("mandatory")


class _AttCNMsmdsDisagreeLogType_Type(Integer32):
    """Custom type attCNMsmdsDisagreeLogType based on Integer32"""
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
        *(("accessClassExceeded", 5),
          ("destSNInotAvailable", 4),
          ("destinationAddressScreenViolation", 2),
          ("invalidSourceAddressForSNI", 3),
          ("mcduExceededAtEgress", 7),
          ("mcduExceededAtIngress", 6),
          ("sourceAddressScreenViolation", 1))
    )


_AttCNMsmdsDisagreeLogType_Type.__name__ = "Integer32"
_AttCNMsmdsDisagreeLogType_Object = MibTableColumn
attCNMsmdsDisagreeLogType = _AttCNMsmdsDisagreeLogType_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 8, 1, 2),
    _AttCNMsmdsDisagreeLogType_Type()
)
attCNMsmdsDisagreeLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsDisagreeLogType.setStatus("mandatory")
_AttCNMsmdsDisagreeLogSA_Type = SMDSAddress
_AttCNMsmdsDisagreeLogSA_Object = MibTableColumn
attCNMsmdsDisagreeLogSA = _AttCNMsmdsDisagreeLogSA_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 8, 1, 3),
    _AttCNMsmdsDisagreeLogSA_Type()
)
attCNMsmdsDisagreeLogSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsDisagreeLogSA.setStatus("mandatory")
_AttCNMsmdsDisagreeLogDA_Type = SMDSAddress
_AttCNMsmdsDisagreeLogDA_Object = MibTableColumn
attCNMsmdsDisagreeLogDA = _AttCNMsmdsDisagreeLogDA_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 8, 1, 4),
    _AttCNMsmdsDisagreeLogDA_Type()
)
attCNMsmdsDisagreeLogDA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsDisagreeLogDA.setStatus("mandatory")
_AttCNMsmdsDisagreeLogTimeStamp_Type = TimeTicks
_AttCNMsmdsDisagreeLogTimeStamp_Object = MibTableColumn
attCNMsmdsDisagreeLogTimeStamp = _AttCNMsmdsDisagreeLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 8, 1, 5),
    _AttCNMsmdsDisagreeLogTimeStamp_Type()
)
attCNMsmdsDisagreeLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsDisagreeLogTimeStamp.setStatus("mandatory")


class _AttCNMsmdsDisagreeLogLocalTime_Type(DisplayString):
    """Custom type attCNMsmdsDisagreeLogLocalTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AttCNMsmdsDisagreeLogLocalTime_Type.__name__ = "DisplayString"
_AttCNMsmdsDisagreeLogLocalTime_Object = MibTableColumn
attCNMsmdsDisagreeLogLocalTime = _AttCNMsmdsDisagreeLogLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 15, 6, 8, 1, 6),
    _AttCNMsmdsDisagreeLogLocalTime_Type()
)
attCNMsmdsDisagreeLogLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    attCNMsmdsDisagreeLogLocalTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATT-CNM-SMDS-MIB",
    **{"SMDSAddress": SMDSAddress,
       "att-2": att_2,
       "att-products": att_products,
       "att-cnmAgent": att_cnmAgent,
       "att-mgmt": att_mgmt,
       "att-cnm": att_cnm,
       "att-cnm-smds": att_cnm_smds,
       "attCNMsmdsConfigTable": attCNMsmdsConfigTable,
       "attCNMsmdsConfigEntry": attCNMsmdsConfigEntry,
       "attCNMsmdsConfigIndex": attCNMsmdsConfigIndex,
       "attCNMsmdsAccessClass": attCNMsmdsAccessClass,
       "attCNMsmdsMCDUsIn": attCNMsmdsMCDUsIn,
       "attCNMsmdsMCDUsOut": attCNMsmdsMCDUsOut,
       "attCNMsmdsIndivScreenMode": attCNMsmdsIndivScreenMode,
       "attCNMsmdsGroupScreenMode": attCNMsmdsGroupScreenMode,
       "attCNMsmdsAddrIndexDescr": attCNMsmdsAddrIndexDescr,
       "attCNMsmdsDisagreeMaxIntervals": attCNMsmdsDisagreeMaxIntervals,
       "attCNMsmdsDisagreeIntervalLen": attCNMsmdsDisagreeIntervalLen,
       "attCNMsmdsAddrTable": attCNMsmdsAddrTable,
       "attCNMsmdsAddrEntry": attCNMsmdsAddrEntry,
       "attCNMsmdsAddrCountryIndex": attCNMsmdsAddrCountryIndex,
       "attCNMsmdsAddrAreaIndex": attCNMsmdsAddrAreaIndex,
       "attCNMsmdsAddrSubscriberIndex": attCNMsmdsAddrSubscriberIndex,
       "attCNMsmdsAddressOnSNI": attCNMsmdsAddressOnSNI,
       "attCNMsmdsInterfaceIndex": attCNMsmdsInterfaceIndex,
       "attCNMsmdsIndScrTable": attCNMsmdsIndScrTable,
       "attCNMsmdsIndScrEntry": attCNMsmdsIndScrEntry,
       "attCNMsmdsIndScrIndex": attCNMsmdsIndScrIndex,
       "attCNMsmdsIndScrCountryIndex": attCNMsmdsIndScrCountryIndex,
       "attCNMsmdsIndScrAreaIndex": attCNMsmdsIndScrAreaIndex,
       "attCNMsmdsIndScrSubscriberIndex": attCNMsmdsIndScrSubscriberIndex,
       "attCNMsmdsIndivScreenAddress": attCNMsmdsIndivScreenAddress,
       "attCNMsmdsGrpScrTable": attCNMsmdsGrpScrTable,
       "attCNMsmdsGrpScrEntry": attCNMsmdsGrpScrEntry,
       "attCNMsmdsGrpScrIndex": attCNMsmdsGrpScrIndex,
       "attCNMsmdsGrpScrCountryIndex": attCNMsmdsGrpScrCountryIndex,
       "attCNMsmdsGrpScrAreaIndex": attCNMsmdsGrpScrAreaIndex,
       "attCNMsmdsGrpScrSubscriberIndex": attCNMsmdsGrpScrSubscriberIndex,
       "attCNMsmdsGroupScreenAddress": attCNMsmdsGroupScreenAddress,
       "attCNMsmdsMemGrpTable": attCNMsmdsMemGrpTable,
       "attCNMsmdsMemGrpEntry": attCNMsmdsMemGrpEntry,
       "attCNMsmdsMemGrpMemberCountryIndex": attCNMsmdsMemGrpMemberCountryIndex,
       "attCNMsmdsMemGrpMemberAreaIndex": attCNMsmdsMemGrpMemberAreaIndex,
       "attCNMsmdsMemGrpMemberSubscriberIndex": attCNMsmdsMemGrpMemberSubscriberIndex,
       "attCNMsmdsMemGrpGroupCountryIndex": attCNMsmdsMemGrpGroupCountryIndex,
       "attCNMsmdsMemGrpGroupAreaIndex": attCNMsmdsMemGrpGroupAreaIndex,
       "attCNMsmdsMemGrpGroupSubscriberIndex": attCNMsmdsMemGrpGroupSubscriberIndex,
       "attCNMsmdsMemberAddress": attCNMsmdsMemberAddress,
       "attCNMsmdsAssociatedGroup": attCNMsmdsAssociatedGroup,
       "attCNMsmdsGrpMemTable": attCNMsmdsGrpMemTable,
       "attCNMsmdsGrpMemEntry": attCNMsmdsGrpMemEntry,
       "attCNMsmdsGrpMemGroupCountryIndex": attCNMsmdsGrpMemGroupCountryIndex,
       "attCNMsmdsGrpMemGroupAreaIndex": attCNMsmdsGrpMemGroupAreaIndex,
       "attCNMsmdsGrpMemGroupSubscriberIndex": attCNMsmdsGrpMemGroupSubscriberIndex,
       "attCNMsmdsGrpMemMemberCountryIndex": attCNMsmdsGrpMemMemberCountryIndex,
       "attCNMsmdsGrpMemMemberAreaIndex": attCNMsmdsGrpMemMemberAreaIndex,
       "attCNMsmdsGrpMemMemberSubscriberIndex": attCNMsmdsGrpMemMemberSubscriberIndex,
       "attCNMsmdsGroupAddress": attCNMsmdsGroupAddress,
       "attCNMsmdsGroupMember": attCNMsmdsGroupMember,
       "attCNMsmdsDisagreeTable": attCNMsmdsDisagreeTable,
       "attCNMsmdsDisagreeEntry": attCNMsmdsDisagreeEntry,
       "attCNMsmdsDisagreeIndex": attCNMsmdsDisagreeIndex,
       "attCNMsmdsDisagreeInterval": attCNMsmdsDisagreeInterval,
       "attCNMsmdsDisagreeTimeStamp": attCNMsmdsDisagreeTimeStamp,
       "attCNMsmdsDisagreeLocalTime": attCNMsmdsDisagreeLocalTime,
       "attCNMsmdsAccessClassExceededCounts": attCNMsmdsAccessClassExceededCounts,
       "attCNMsmdsMCDUsExceededAtIngressCounts": attCNMsmdsMCDUsExceededAtIngressCounts,
       "attCNMsmdsMCDUsExceededAtEgressCounts": attCNMsmdsMCDUsExceededAtEgressCounts,
       "attCNMsmdsSAScreenViolations": attCNMsmdsSAScreenViolations,
       "attCNMsmdsDAScreenViolations": attCNMsmdsDAScreenViolations,
       "attCNMsmdsUnassignedSAs": attCNMsmdsUnassignedSAs,
       "attCNMsmdsDestinationSNIUnavailableCounts": attCNMsmdsDestinationSNIUnavailableCounts,
       "attCNMsmdsDisagreeLogTable": attCNMsmdsDisagreeLogTable,
       "attCNMsmdsDisagreeLogEntry": attCNMsmdsDisagreeLogEntry,
       "attCNMsmdsDisagreeLogIndex": attCNMsmdsDisagreeLogIndex,
       "attCNMsmdsDisagreeLogType": attCNMsmdsDisagreeLogType,
       "attCNMsmdsDisagreeLogSA": attCNMsmdsDisagreeLogSA,
       "attCNMsmdsDisagreeLogDA": attCNMsmdsDisagreeLogDA,
       "attCNMsmdsDisagreeLogTimeStamp": attCNMsmdsDisagreeLogTimeStamp,
       "attCNMsmdsDisagreeLogLocalTime": attCNMsmdsDisagreeLogLocalTime}
)
