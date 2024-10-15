# SNMP MIB module (IEEE8021-CN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-CN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:16 2024
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

(IEEE8021PbbComponentIdentifier,
 IEEE8021PriorityValue,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PbbComponentIdentifier",
    "IEEE8021PriorityValue",
    "ieee802dot1mibs")

(InterfaceIndex,
 ifGeneralInformationGroup) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifGeneralInformationGroup")

(LldpV2DestAddressTableIndex,) = mibBuilder.importSymbols(
    "LLDP-V2-TC-MIB",
    "LldpV2DestAddressTableIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(systemGroup,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "systemGroup")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ieee8021CnMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 18)
)
ieee8021CnMib.setRevisions(
        ("2018-06-28 00:00",
         "2014-12-15 00:00",
         "2011-02-27 00:00",
         "2009-12-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Ieee8021CnControlChoice(Integer32, TextualConvention):
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
        *(("cpcAdmin", 1),
          ("cpcAuto", 2),
          ("cpcComp", 3))
    )



class Ieee8021CnDefenseMode(Integer32, TextualConvention):
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
        *(("cptDisabled", 1),
          ("cptEdge", 4),
          ("cptInterior", 2),
          ("cptInteriorReady", 3))
    )



class Ieee8021CnLldpChoice(Integer32, TextualConvention):
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
        *(("cnlAdmin", 2),
          ("cnlComponent", 3),
          ("cnlNone", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Ieee8021CnMIBObjects_ObjectIdentity = ObjectIdentity
ieee8021CnMIBObjects = _Ieee8021CnMIBObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 18, 1)
)
_Ieee8021CnGlobalTable_Object = MibTable
ieee8021CnGlobalTable = _Ieee8021CnGlobalTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021CnGlobalTable.setStatus("current")
_Ieee8021CnGlobalEntry_Object = MibTableRow
ieee8021CnGlobalEntry = _Ieee8021CnGlobalEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 1, 1)
)
ieee8021CnGlobalEntry.setIndexNames(
    (0, "IEEE8021-CN-MIB", "ieee8021CnGlobalComponentId"),
)
if mibBuilder.loadTexts:
    ieee8021CnGlobalEntry.setStatus("current")
_Ieee8021CnGlobalComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021CnGlobalComponentId_Object = MibTableColumn
ieee8021CnGlobalComponentId = _Ieee8021CnGlobalComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 1, 1, 1),
    _Ieee8021CnGlobalComponentId_Type()
)
ieee8021CnGlobalComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnGlobalComponentId.setStatus("current")
_Ieee8021CnGlobalMasterEnable_Type = TruthValue
_Ieee8021CnGlobalMasterEnable_Object = MibTableColumn
ieee8021CnGlobalMasterEnable = _Ieee8021CnGlobalMasterEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 1, 1, 2),
    _Ieee8021CnGlobalMasterEnable_Type()
)
ieee8021CnGlobalMasterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnGlobalMasterEnable.setStatus("current")
_Ieee8021CnGlobalCnmTransmitPriority_Type = IEEE8021PriorityValue
_Ieee8021CnGlobalCnmTransmitPriority_Object = MibTableColumn
ieee8021CnGlobalCnmTransmitPriority = _Ieee8021CnGlobalCnmTransmitPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 1, 1, 3),
    _Ieee8021CnGlobalCnmTransmitPriority_Type()
)
ieee8021CnGlobalCnmTransmitPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnGlobalCnmTransmitPriority.setStatus("current")
_Ieee8021CnGlobalDiscardedFrames_Type = Counter64
_Ieee8021CnGlobalDiscardedFrames_Object = MibTableColumn
ieee8021CnGlobalDiscardedFrames = _Ieee8021CnGlobalDiscardedFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 1, 1, 4),
    _Ieee8021CnGlobalDiscardedFrames_Type()
)
ieee8021CnGlobalDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CnGlobalDiscardedFrames.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021CnGlobalDiscardedFrames.setUnits("frames")
_Ieee8021CnErroredPortTable_Object = MibTable
ieee8021CnErroredPortTable = _Ieee8021CnErroredPortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021CnErroredPortTable.setStatus("current")
_Ieee8021CnErroredPortEntry_Object = MibTableRow
ieee8021CnErroredPortEntry = _Ieee8021CnErroredPortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 2, 1)
)
ieee8021CnErroredPortEntry.setIndexNames(
    (0, "IEEE8021-CN-MIB", "ieee8021CnEpComponentId"),
    (0, "IEEE8021-CN-MIB", "ieee8021CnEpPriority"),
    (0, "IEEE8021-CN-MIB", "ieee8021CnEpIfIndex"),
)
if mibBuilder.loadTexts:
    ieee8021CnErroredPortEntry.setStatus("current")
_Ieee8021CnEpComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021CnEpComponentId_Object = MibTableColumn
ieee8021CnEpComponentId = _Ieee8021CnEpComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 2, 1, 1),
    _Ieee8021CnEpComponentId_Type()
)
ieee8021CnEpComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnEpComponentId.setStatus("current")
_Ieee8021CnEpPriority_Type = IEEE8021PriorityValue
_Ieee8021CnEpPriority_Object = MibTableColumn
ieee8021CnEpPriority = _Ieee8021CnEpPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 2, 1, 2),
    _Ieee8021CnEpPriority_Type()
)
ieee8021CnEpPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnEpPriority.setStatus("current")
_Ieee8021CnEpIfIndex_Type = InterfaceIndex
_Ieee8021CnEpIfIndex_Object = MibTableColumn
ieee8021CnEpIfIndex = _Ieee8021CnEpIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 2, 1, 3),
    _Ieee8021CnEpIfIndex_Type()
)
ieee8021CnEpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CnEpIfIndex.setStatus("current")
_Ieee8021CnCompntPriTable_Object = MibTable
ieee8021CnCompntPriTable = _Ieee8021CnCompntPriTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 3)
)
if mibBuilder.loadTexts:
    ieee8021CnCompntPriTable.setStatus("current")
_Ieee8021CnCompntPriEntry_Object = MibTableRow
ieee8021CnCompntPriEntry = _Ieee8021CnCompntPriEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 3, 1)
)
ieee8021CnCompntPriEntry.setIndexNames(
    (0, "IEEE8021-CN-MIB", "ieee8021CnComPriComponentId"),
    (0, "IEEE8021-CN-MIB", "ieee8021CnComPriPriority"),
)
if mibBuilder.loadTexts:
    ieee8021CnCompntPriEntry.setStatus("current")
_Ieee8021CnComPriComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021CnComPriComponentId_Object = MibTableColumn
ieee8021CnComPriComponentId = _Ieee8021CnComPriComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 3, 1, 1),
    _Ieee8021CnComPriComponentId_Type()
)
ieee8021CnComPriComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnComPriComponentId.setStatus("current")
_Ieee8021CnComPriPriority_Type = IEEE8021PriorityValue
_Ieee8021CnComPriPriority_Object = MibTableColumn
ieee8021CnComPriPriority = _Ieee8021CnComPriPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 3, 1, 2),
    _Ieee8021CnComPriPriority_Type()
)
ieee8021CnComPriPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnComPriPriority.setStatus("current")


class _Ieee8021CnComPriDefModeChoice_Type(Ieee8021CnControlChoice):
    """Custom type ieee8021CnComPriDefModeChoice based on Ieee8021CnControlChoice"""
    defaultValue = 2

    subtypeSpec = Ieee8021CnControlChoice.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpcAdmin", 1),
          ("cpcAuto", 2))
    )


_Ieee8021CnComPriDefModeChoice_Type.__name__ = "Ieee8021CnControlChoice"
_Ieee8021CnComPriDefModeChoice_Object = MibTableColumn
ieee8021CnComPriDefModeChoice = _Ieee8021CnComPriDefModeChoice_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 3, 1, 3),
    _Ieee8021CnComPriDefModeChoice_Type()
)
ieee8021CnComPriDefModeChoice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021CnComPriDefModeChoice.setStatus("current")


class _Ieee8021CnComPriAlternatePriority_Type(IEEE8021PriorityValue):
    """Custom type ieee8021CnComPriAlternatePriority based on IEEE8021PriorityValue"""
    defaultValue = 0


_Ieee8021CnComPriAlternatePriority_Object = MibTableColumn
ieee8021CnComPriAlternatePriority = _Ieee8021CnComPriAlternatePriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 3, 1, 4),
    _Ieee8021CnComPriAlternatePriority_Type()
)
ieee8021CnComPriAlternatePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021CnComPriAlternatePriority.setStatus("current")
_Ieee8021CnComPriAutoAltPri_Type = IEEE8021PriorityValue
_Ieee8021CnComPriAutoAltPri_Object = MibTableColumn
ieee8021CnComPriAutoAltPri = _Ieee8021CnComPriAutoAltPri_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 3, 1, 5),
    _Ieee8021CnComPriAutoAltPri_Type()
)
ieee8021CnComPriAutoAltPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CnComPriAutoAltPri.setStatus("current")


class _Ieee8021CnComPriAdminDefenseMode_Type(Ieee8021CnDefenseMode):
    """Custom type ieee8021CnComPriAdminDefenseMode based on Ieee8021CnDefenseMode"""


_Ieee8021CnComPriAdminDefenseMode_Object = MibTableColumn
ieee8021CnComPriAdminDefenseMode = _Ieee8021CnComPriAdminDefenseMode_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 3, 1, 6),
    _Ieee8021CnComPriAdminDefenseMode_Type()
)
ieee8021CnComPriAdminDefenseMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021CnComPriAdminDefenseMode.setStatus("current")


class _Ieee8021CnComPriCreation_Type(Integer32):
    """Custom type ieee8021CnComPriCreation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cncpAutoDisable", 2),
          ("cncpAutoEnable", 1))
    )


_Ieee8021CnComPriCreation_Type.__name__ = "Integer32"
_Ieee8021CnComPriCreation_Object = MibTableColumn
ieee8021CnComPriCreation = _Ieee8021CnComPriCreation_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 3, 1, 7),
    _Ieee8021CnComPriCreation_Type()
)
ieee8021CnComPriCreation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021CnComPriCreation.setStatus("current")


class _Ieee8021CnComPriLldpInstanceChoice_Type(Ieee8021CnLldpChoice):
    """Custom type ieee8021CnComPriLldpInstanceChoice based on Ieee8021CnLldpChoice"""
    defaultValue = 2

    subtypeSpec = Ieee8021CnLldpChoice.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cnlAdmin", 2),
          ("cnlNone", 1))
    )


_Ieee8021CnComPriLldpInstanceChoice_Type.__name__ = "Ieee8021CnLldpChoice"
_Ieee8021CnComPriLldpInstanceChoice_Object = MibTableColumn
ieee8021CnComPriLldpInstanceChoice = _Ieee8021CnComPriLldpInstanceChoice_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 3, 1, 8),
    _Ieee8021CnComPriLldpInstanceChoice_Type()
)
ieee8021CnComPriLldpInstanceChoice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021CnComPriLldpInstanceChoice.setStatus("current")


class _Ieee8021CnComPriLldpInstanceSelector_Type(LldpV2DestAddressTableIndex):
    """Custom type ieee8021CnComPriLldpInstanceSelector based on LldpV2DestAddressTableIndex"""
    defaultValue = 1


_Ieee8021CnComPriLldpInstanceSelector_Object = MibTableColumn
ieee8021CnComPriLldpInstanceSelector = _Ieee8021CnComPriLldpInstanceSelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 3, 1, 9),
    _Ieee8021CnComPriLldpInstanceSelector_Type()
)
ieee8021CnComPriLldpInstanceSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021CnComPriLldpInstanceSelector.setStatus("current")
_Ieee8021CnComPriRowStatus_Type = RowStatus
_Ieee8021CnComPriRowStatus_Object = MibTableColumn
ieee8021CnComPriRowStatus = _Ieee8021CnComPriRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 3, 1, 10),
    _Ieee8021CnComPriRowStatus_Type()
)
ieee8021CnComPriRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021CnComPriRowStatus.setStatus("current")
_Ieee8021CnPortPriTable_Object = MibTable
ieee8021CnPortPriTable = _Ieee8021CnPortPriTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 4)
)
if mibBuilder.loadTexts:
    ieee8021CnPortPriTable.setStatus("current")
_Ieee8021CnPortPriEntry_Object = MibTableRow
ieee8021CnPortPriEntry = _Ieee8021CnPortPriEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 4, 1)
)
ieee8021CnPortPriEntry.setIndexNames(
    (0, "IEEE8021-CN-MIB", "ieee8021CnPortPriComponentId"),
    (0, "IEEE8021-CN-MIB", "ieee8021CnPortPriority"),
    (0, "IEEE8021-CN-MIB", "ieee8021CnPortPriIfIndex"),
)
if mibBuilder.loadTexts:
    ieee8021CnPortPriEntry.setStatus("current")
_Ieee8021CnPortPriComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021CnPortPriComponentId_Object = MibTableColumn
ieee8021CnPortPriComponentId = _Ieee8021CnPortPriComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 4, 1, 1),
    _Ieee8021CnPortPriComponentId_Type()
)
ieee8021CnPortPriComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnPortPriComponentId.setStatus("current")
_Ieee8021CnPortPriority_Type = IEEE8021PriorityValue
_Ieee8021CnPortPriority_Object = MibTableColumn
ieee8021CnPortPriority = _Ieee8021CnPortPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 4, 1, 2),
    _Ieee8021CnPortPriority_Type()
)
ieee8021CnPortPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnPortPriority.setStatus("current")
_Ieee8021CnPortPriIfIndex_Type = InterfaceIndex
_Ieee8021CnPortPriIfIndex_Object = MibTableColumn
ieee8021CnPortPriIfIndex = _Ieee8021CnPortPriIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 4, 1, 3),
    _Ieee8021CnPortPriIfIndex_Type()
)
ieee8021CnPortPriIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnPortPriIfIndex.setStatus("current")


class _Ieee8021CnPortPriDefModeChoice_Type(Ieee8021CnControlChoice):
    """Custom type ieee8021CnPortPriDefModeChoice based on Ieee8021CnControlChoice"""


_Ieee8021CnPortPriDefModeChoice_Object = MibTableColumn
ieee8021CnPortPriDefModeChoice = _Ieee8021CnPortPriDefModeChoice_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 4, 1, 4),
    _Ieee8021CnPortPriDefModeChoice_Type()
)
ieee8021CnPortPriDefModeChoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnPortPriDefModeChoice.setStatus("current")


class _Ieee8021CnPortPriAdminDefenseMode_Type(Ieee8021CnDefenseMode):
    """Custom type ieee8021CnPortPriAdminDefenseMode based on Ieee8021CnDefenseMode"""


_Ieee8021CnPortPriAdminDefenseMode_Object = MibTableColumn
ieee8021CnPortPriAdminDefenseMode = _Ieee8021CnPortPriAdminDefenseMode_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 4, 1, 5),
    _Ieee8021CnPortPriAdminDefenseMode_Type()
)
ieee8021CnPortPriAdminDefenseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnPortPriAdminDefenseMode.setStatus("current")


class _Ieee8021CnPortPriAutoDefenseMode_Type(Ieee8021CnDefenseMode):
    """Custom type ieee8021CnPortPriAutoDefenseMode based on Ieee8021CnDefenseMode"""
    subtypeSpec = Ieee8021CnDefenseMode.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cptEdge", 4),
          ("cptInterior", 2),
          ("cptInteriorReady", 3))
    )


_Ieee8021CnPortPriAutoDefenseMode_Type.__name__ = "Ieee8021CnDefenseMode"
_Ieee8021CnPortPriAutoDefenseMode_Object = MibTableColumn
ieee8021CnPortPriAutoDefenseMode = _Ieee8021CnPortPriAutoDefenseMode_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 4, 1, 6),
    _Ieee8021CnPortPriAutoDefenseMode_Type()
)
ieee8021CnPortPriAutoDefenseMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CnPortPriAutoDefenseMode.setStatus("current")


class _Ieee8021CnPortPriLldpInstanceChoice_Type(Ieee8021CnLldpChoice):
    """Custom type ieee8021CnPortPriLldpInstanceChoice based on Ieee8021CnLldpChoice"""


_Ieee8021CnPortPriLldpInstanceChoice_Object = MibTableColumn
ieee8021CnPortPriLldpInstanceChoice = _Ieee8021CnPortPriLldpInstanceChoice_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 4, 1, 7),
    _Ieee8021CnPortPriLldpInstanceChoice_Type()
)
ieee8021CnPortPriLldpInstanceChoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnPortPriLldpInstanceChoice.setStatus("current")


class _Ieee8021CnPortPriLldpInstanceSelector_Type(LldpV2DestAddressTableIndex):
    """Custom type ieee8021CnPortPriLldpInstanceSelector based on LldpV2DestAddressTableIndex"""
    defaultValue = 3


_Ieee8021CnPortPriLldpInstanceSelector_Object = MibTableColumn
ieee8021CnPortPriLldpInstanceSelector = _Ieee8021CnPortPriLldpInstanceSelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 4, 1, 8),
    _Ieee8021CnPortPriLldpInstanceSelector_Type()
)
ieee8021CnPortPriLldpInstanceSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnPortPriLldpInstanceSelector.setStatus("current")


class _Ieee8021CnPortPriAlternatePriority_Type(IEEE8021PriorityValue):
    """Custom type ieee8021CnPortPriAlternatePriority based on IEEE8021PriorityValue"""
    defaultValue = 0


_Ieee8021CnPortPriAlternatePriority_Object = MibTableColumn
ieee8021CnPortPriAlternatePriority = _Ieee8021CnPortPriAlternatePriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 4, 1, 9),
    _Ieee8021CnPortPriAlternatePriority_Type()
)
ieee8021CnPortPriAlternatePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnPortPriAlternatePriority.setStatus("current")
_Ieee8021CnCpTable_Object = MibTable
ieee8021CnCpTable = _Ieee8021CnCpTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 5)
)
if mibBuilder.loadTexts:
    ieee8021CnCpTable.setStatus("current")
_Ieee8021CnCpEntry_Object = MibTableRow
ieee8021CnCpEntry = _Ieee8021CnCpEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 5, 1)
)
ieee8021CnCpEntry.setIndexNames(
    (0, "IEEE8021-CN-MIB", "ieee8021CnCpComponentId"),
    (0, "IEEE8021-CN-MIB", "ieee8021CnCpIfIndex"),
    (0, "IEEE8021-CN-MIB", "ieee8021CnCpIndex"),
)
if mibBuilder.loadTexts:
    ieee8021CnCpEntry.setStatus("current")
_Ieee8021CnCpComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021CnCpComponentId_Object = MibTableColumn
ieee8021CnCpComponentId = _Ieee8021CnCpComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 5, 1, 1),
    _Ieee8021CnCpComponentId_Type()
)
ieee8021CnCpComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnCpComponentId.setStatus("current")
_Ieee8021CnCpIfIndex_Type = InterfaceIndex
_Ieee8021CnCpIfIndex_Object = MibTableColumn
ieee8021CnCpIfIndex = _Ieee8021CnCpIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 5, 1, 2),
    _Ieee8021CnCpIfIndex_Type()
)
ieee8021CnCpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnCpIfIndex.setStatus("current")


class _Ieee8021CnCpIndex_Type(Unsigned32):
    """Custom type ieee8021CnCpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Ieee8021CnCpIndex_Type.__name__ = "Unsigned32"
_Ieee8021CnCpIndex_Object = MibTableColumn
ieee8021CnCpIndex = _Ieee8021CnCpIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 5, 1, 3),
    _Ieee8021CnCpIndex_Type()
)
ieee8021CnCpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnCpIndex.setStatus("current")
_Ieee8021CnCpPriority_Type = IEEE8021PriorityValue
_Ieee8021CnCpPriority_Object = MibTableColumn
ieee8021CnCpPriority = _Ieee8021CnCpPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 5, 1, 4),
    _Ieee8021CnCpPriority_Type()
)
ieee8021CnCpPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CnCpPriority.setStatus("current")
_Ieee8021CnCpMacAddress_Type = MacAddress
_Ieee8021CnCpMacAddress_Object = MibTableColumn
ieee8021CnCpMacAddress = _Ieee8021CnCpMacAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 5, 1, 5),
    _Ieee8021CnCpMacAddress_Type()
)
ieee8021CnCpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CnCpMacAddress.setStatus("current")


class _Ieee8021CnCpIdentifier_Type(OctetString):
    """Custom type ieee8021CnCpIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ieee8021CnCpIdentifier_Type.__name__ = "OctetString"
_Ieee8021CnCpIdentifier_Object = MibTableColumn
ieee8021CnCpIdentifier = _Ieee8021CnCpIdentifier_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 5, 1, 6),
    _Ieee8021CnCpIdentifier_Type()
)
ieee8021CnCpIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CnCpIdentifier.setStatus("current")


class _Ieee8021CnCpQueueSizeSetPoint_Type(Unsigned32):
    """Custom type ieee8021CnCpQueueSizeSetPoint based on Unsigned32"""
    defaultValue = 26000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4294967295),
    )


_Ieee8021CnCpQueueSizeSetPoint_Type.__name__ = "Unsigned32"
_Ieee8021CnCpQueueSizeSetPoint_Object = MibTableColumn
ieee8021CnCpQueueSizeSetPoint = _Ieee8021CnCpQueueSizeSetPoint_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 5, 1, 7),
    _Ieee8021CnCpQueueSizeSetPoint_Type()
)
ieee8021CnCpQueueSizeSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnCpQueueSizeSetPoint.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021CnCpQueueSizeSetPoint.setUnits("octets")


class _Ieee8021CnCpFeedbackWeight_Type(Integer32):
    """Custom type ieee8021CnCpFeedbackWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
    )


_Ieee8021CnCpFeedbackWeight_Type.__name__ = "Integer32"
_Ieee8021CnCpFeedbackWeight_Object = MibTableColumn
ieee8021CnCpFeedbackWeight = _Ieee8021CnCpFeedbackWeight_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 5, 1, 8),
    _Ieee8021CnCpFeedbackWeight_Type()
)
ieee8021CnCpFeedbackWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnCpFeedbackWeight.setStatus("current")


class _Ieee8021CnCpMinSampleBase_Type(Unsigned32):
    """Custom type ieee8021CnCpMinSampleBase based on Unsigned32"""
    defaultValue = 150000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 4294967295),
    )


_Ieee8021CnCpMinSampleBase_Type.__name__ = "Unsigned32"
_Ieee8021CnCpMinSampleBase_Object = MibTableColumn
ieee8021CnCpMinSampleBase = _Ieee8021CnCpMinSampleBase_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 5, 1, 9),
    _Ieee8021CnCpMinSampleBase_Type()
)
ieee8021CnCpMinSampleBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnCpMinSampleBase.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021CnCpMinSampleBase.setUnits("octets")
_Ieee8021CnCpDiscardedFrames_Type = Counter64
_Ieee8021CnCpDiscardedFrames_Object = MibTableColumn
ieee8021CnCpDiscardedFrames = _Ieee8021CnCpDiscardedFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 5, 1, 10),
    _Ieee8021CnCpDiscardedFrames_Type()
)
ieee8021CnCpDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CnCpDiscardedFrames.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021CnCpDiscardedFrames.setUnits("frames")
_Ieee8021CnCpTransmittedFrames_Type = Counter64
_Ieee8021CnCpTransmittedFrames_Object = MibTableColumn
ieee8021CnCpTransmittedFrames = _Ieee8021CnCpTransmittedFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 5, 1, 11),
    _Ieee8021CnCpTransmittedFrames_Type()
)
ieee8021CnCpTransmittedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CnCpTransmittedFrames.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021CnCpTransmittedFrames.setUnits("frames")
_Ieee8021CnCpTransmittedCnms_Type = Counter64
_Ieee8021CnCpTransmittedCnms_Object = MibTableColumn
ieee8021CnCpTransmittedCnms = _Ieee8021CnCpTransmittedCnms_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 5, 1, 12),
    _Ieee8021CnCpTransmittedCnms_Type()
)
ieee8021CnCpTransmittedCnms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CnCpTransmittedCnms.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021CnCpTransmittedCnms.setUnits("frames")


class _Ieee8021CnCpMinHeaderOctets_Type(Unsigned32):
    """Custom type ieee8021CnCpMinHeaderOctets based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Ieee8021CnCpMinHeaderOctets_Type.__name__ = "Unsigned32"
_Ieee8021CnCpMinHeaderOctets_Object = MibTableColumn
ieee8021CnCpMinHeaderOctets = _Ieee8021CnCpMinHeaderOctets_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 5, 1, 13),
    _Ieee8021CnCpMinHeaderOctets_Type()
)
ieee8021CnCpMinHeaderOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnCpMinHeaderOctets.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021CnCpMinHeaderOctets.setUnits("octets")
_Ieee8021CnCpidToInterfaceTable_Object = MibTable
ieee8021CnCpidToInterfaceTable = _Ieee8021CnCpidToInterfaceTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 6)
)
if mibBuilder.loadTexts:
    ieee8021CnCpidToInterfaceTable.setStatus("current")
_Ieee8021CnCpidToInterfaceEntry_Object = MibTableRow
ieee8021CnCpidToInterfaceEntry = _Ieee8021CnCpidToInterfaceEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 6, 1)
)
ieee8021CnCpidToInterfaceEntry.setIndexNames(
    (0, "IEEE8021-CN-MIB", "ieee8021CnCpidToIfCpid"),
)
if mibBuilder.loadTexts:
    ieee8021CnCpidToInterfaceEntry.setStatus("current")


class _Ieee8021CnCpidToIfCpid_Type(OctetString):
    """Custom type ieee8021CnCpidToIfCpid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ieee8021CnCpidToIfCpid_Type.__name__ = "OctetString"
_Ieee8021CnCpidToIfCpid_Object = MibTableColumn
ieee8021CnCpidToIfCpid = _Ieee8021CnCpidToIfCpid_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 6, 1, 1),
    _Ieee8021CnCpidToIfCpid_Type()
)
ieee8021CnCpidToIfCpid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnCpidToIfCpid.setStatus("current")
_Ieee8021CnCpidToIfComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021CnCpidToIfComponentId_Object = MibTableColumn
ieee8021CnCpidToIfComponentId = _Ieee8021CnCpidToIfComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 6, 1, 2),
    _Ieee8021CnCpidToIfComponentId_Type()
)
ieee8021CnCpidToIfComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CnCpidToIfComponentId.setStatus("current")
_Ieee8021CnCpidToIfIfIndex_Type = InterfaceIndex
_Ieee8021CnCpidToIfIfIndex_Object = MibTableColumn
ieee8021CnCpidToIfIfIndex = _Ieee8021CnCpidToIfIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 6, 1, 3),
    _Ieee8021CnCpidToIfIfIndex_Type()
)
ieee8021CnCpidToIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CnCpidToIfIfIndex.setStatus("current")


class _Ieee8021CnCpidToIfCpIndex_Type(Unsigned32):
    """Custom type ieee8021CnCpidToIfCpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Ieee8021CnCpidToIfCpIndex_Type.__name__ = "Unsigned32"
_Ieee8021CnCpidToIfCpIndex_Object = MibTableColumn
ieee8021CnCpidToIfCpIndex = _Ieee8021CnCpidToIfCpIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 6, 1, 4),
    _Ieee8021CnCpidToIfCpIndex_Type()
)
ieee8021CnCpidToIfCpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CnCpidToIfCpIndex.setStatus("current")
_Ieee8021CnRpPortPriTable_Object = MibTable
ieee8021CnRpPortPriTable = _Ieee8021CnRpPortPriTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 7)
)
if mibBuilder.loadTexts:
    ieee8021CnRpPortPriTable.setStatus("current")
_Ieee8021CnRpPortPriEntry_Object = MibTableRow
ieee8021CnRpPortPriEntry = _Ieee8021CnRpPortPriEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 7, 1)
)
ieee8021CnRpPortPriEntry.setIndexNames(
    (0, "IEEE8021-CN-MIB", "ieee8021CnRpPortPriComponentId"),
    (0, "IEEE8021-CN-MIB", "ieee8021CnRpPortPriPriority"),
    (0, "IEEE8021-CN-MIB", "ieee8021CnRpPortPriIfIndex"),
)
if mibBuilder.loadTexts:
    ieee8021CnRpPortPriEntry.setStatus("current")
_Ieee8021CnRpPortPriComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021CnRpPortPriComponentId_Object = MibTableColumn
ieee8021CnRpPortPriComponentId = _Ieee8021CnRpPortPriComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 7, 1, 1),
    _Ieee8021CnRpPortPriComponentId_Type()
)
ieee8021CnRpPortPriComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnRpPortPriComponentId.setStatus("current")
_Ieee8021CnRpPortPriPriority_Type = IEEE8021PriorityValue
_Ieee8021CnRpPortPriPriority_Object = MibTableColumn
ieee8021CnRpPortPriPriority = _Ieee8021CnRpPortPriPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 7, 1, 2),
    _Ieee8021CnRpPortPriPriority_Type()
)
ieee8021CnRpPortPriPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnRpPortPriPriority.setStatus("current")
_Ieee8021CnRpPortPriIfIndex_Type = InterfaceIndex
_Ieee8021CnRpPortPriIfIndex_Object = MibTableColumn
ieee8021CnRpPortPriIfIndex = _Ieee8021CnRpPortPriIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 7, 1, 3),
    _Ieee8021CnRpPortPriIfIndex_Type()
)
ieee8021CnRpPortPriIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnRpPortPriIfIndex.setStatus("current")


class _Ieee8021CnRpPortPriMaxRps_Type(Unsigned32):
    """Custom type ieee8021CnRpPortPriMaxRps based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Ieee8021CnRpPortPriMaxRps_Type.__name__ = "Unsigned32"
_Ieee8021CnRpPortPriMaxRps_Object = MibTableColumn
ieee8021CnRpPortPriMaxRps = _Ieee8021CnRpPortPriMaxRps_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 7, 1, 4),
    _Ieee8021CnRpPortPriMaxRps_Type()
)
ieee8021CnRpPortPriMaxRps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnRpPortPriMaxRps.setStatus("current")
_Ieee8021CnRpPortPriCreatedRps_Type = Counter32
_Ieee8021CnRpPortPriCreatedRps_Object = MibTableColumn
ieee8021CnRpPortPriCreatedRps = _Ieee8021CnRpPortPriCreatedRps_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 7, 1, 5),
    _Ieee8021CnRpPortPriCreatedRps_Type()
)
ieee8021CnRpPortPriCreatedRps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CnRpPortPriCreatedRps.setStatus("current")
_Ieee8021CnRpPortPriCentiseconds_Type = Counter64
_Ieee8021CnRpPortPriCentiseconds_Object = MibTableColumn
ieee8021CnRpPortPriCentiseconds = _Ieee8021CnRpPortPriCentiseconds_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 7, 1, 6),
    _Ieee8021CnRpPortPriCentiseconds_Type()
)
ieee8021CnRpPortPriCentiseconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021CnRpPortPriCentiseconds.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021CnRpPortPriCentiseconds.setUnits("centiseconds")
_Ieee8021CnRpGroupTable_Object = MibTable
ieee8021CnRpGroupTable = _Ieee8021CnRpGroupTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 8)
)
if mibBuilder.loadTexts:
    ieee8021CnRpGroupTable.setStatus("current")
_Ieee8021CnRpGroupEntry_Object = MibTableRow
ieee8021CnRpGroupEntry = _Ieee8021CnRpGroupEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 8, 1)
)
ieee8021CnRpGroupEntry.setIndexNames(
    (0, "IEEE8021-CN-MIB", "ieee8021CnRpgComponentId"),
    (0, "IEEE8021-CN-MIB", "ieee8021CnRpgPriority"),
    (0, "IEEE8021-CN-MIB", "ieee8021CnRpgIfIndex"),
    (0, "IEEE8021-CN-MIB", "ieee8021CnRpgIdentifier"),
)
if mibBuilder.loadTexts:
    ieee8021CnRpGroupEntry.setStatus("current")
_Ieee8021CnRpgComponentId_Type = IEEE8021PbbComponentIdentifier
_Ieee8021CnRpgComponentId_Object = MibTableColumn
ieee8021CnRpgComponentId = _Ieee8021CnRpgComponentId_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 8, 1, 1),
    _Ieee8021CnRpgComponentId_Type()
)
ieee8021CnRpgComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnRpgComponentId.setStatus("current")
_Ieee8021CnRpgPriority_Type = IEEE8021PriorityValue
_Ieee8021CnRpgPriority_Object = MibTableColumn
ieee8021CnRpgPriority = _Ieee8021CnRpgPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 8, 1, 2),
    _Ieee8021CnRpgPriority_Type()
)
ieee8021CnRpgPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnRpgPriority.setStatus("current")
_Ieee8021CnRpgIfIndex_Type = InterfaceIndex
_Ieee8021CnRpgIfIndex_Object = MibTableColumn
ieee8021CnRpgIfIndex = _Ieee8021CnRpgIfIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 8, 1, 3),
    _Ieee8021CnRpgIfIndex_Type()
)
ieee8021CnRpgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnRpgIfIndex.setStatus("current")


class _Ieee8021CnRpgIdentifier_Type(Unsigned32):
    """Custom type ieee8021CnRpgIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Ieee8021CnRpgIdentifier_Type.__name__ = "Unsigned32"
_Ieee8021CnRpgIdentifier_Object = MibTableColumn
ieee8021CnRpgIdentifier = _Ieee8021CnRpgIdentifier_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 8, 1, 4),
    _Ieee8021CnRpgIdentifier_Type()
)
ieee8021CnRpgIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021CnRpgIdentifier.setStatus("current")


class _Ieee8021CnRpgEnable_Type(TruthValue):
    """Custom type ieee8021CnRpgEnable based on TruthValue"""


_Ieee8021CnRpgEnable_Object = MibTableColumn
ieee8021CnRpgEnable = _Ieee8021CnRpgEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 8, 1, 5),
    _Ieee8021CnRpgEnable_Type()
)
ieee8021CnRpgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnRpgEnable.setStatus("current")


class _Ieee8021CnRpgTimeReset_Type(TimeInterval):
    """Custom type ieee8021CnRpgTimeReset based on TimeInterval"""
    defaultValue = 15


_Ieee8021CnRpgTimeReset_Object = MibTableColumn
ieee8021CnRpgTimeReset = _Ieee8021CnRpgTimeReset_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 8, 1, 6),
    _Ieee8021CnRpgTimeReset_Type()
)
ieee8021CnRpgTimeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnRpgTimeReset.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021CnRpgTimeReset.setUnits("milliseconds")


class _Ieee8021CnRpgByteReset_Type(Unsigned32):
    """Custom type ieee8021CnRpgByteReset based on Unsigned32"""
    defaultValue = 150000


_Ieee8021CnRpgByteReset_Object = MibTableColumn
ieee8021CnRpgByteReset = _Ieee8021CnRpgByteReset_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 8, 1, 7),
    _Ieee8021CnRpgByteReset_Type()
)
ieee8021CnRpgByteReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnRpgByteReset.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021CnRpgByteReset.setUnits("octets")


class _Ieee8021CnRpgThreshold_Type(Unsigned32):
    """Custom type ieee8021CnRpgThreshold based on Unsigned32"""
    defaultValue = 5


_Ieee8021CnRpgThreshold_Object = MibTableColumn
ieee8021CnRpgThreshold = _Ieee8021CnRpgThreshold_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 8, 1, 8),
    _Ieee8021CnRpgThreshold_Type()
)
ieee8021CnRpgThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnRpgThreshold.setStatus("current")
_Ieee8021CnRpgMaxRate_Type = Unsigned32
_Ieee8021CnRpgMaxRate_Object = MibTableColumn
ieee8021CnRpgMaxRate = _Ieee8021CnRpgMaxRate_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 8, 1, 9),
    _Ieee8021CnRpgMaxRate_Type()
)
ieee8021CnRpgMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnRpgMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021CnRpgMaxRate.setUnits("Mb/s")


class _Ieee8021CnRpgAiRate_Type(Unsigned32):
    """Custom type ieee8021CnRpgAiRate based on Unsigned32"""
    defaultValue = 5


_Ieee8021CnRpgAiRate_Object = MibTableColumn
ieee8021CnRpgAiRate = _Ieee8021CnRpgAiRate_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 8, 1, 10),
    _Ieee8021CnRpgAiRate_Type()
)
ieee8021CnRpgAiRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnRpgAiRate.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021CnRpgAiRate.setUnits("Mb/s")


class _Ieee8021CnRpgHaiRate_Type(Unsigned32):
    """Custom type ieee8021CnRpgHaiRate based on Unsigned32"""
    defaultValue = 50


_Ieee8021CnRpgHaiRate_Object = MibTableColumn
ieee8021CnRpgHaiRate = _Ieee8021CnRpgHaiRate_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 8, 1, 11),
    _Ieee8021CnRpgHaiRate_Type()
)
ieee8021CnRpgHaiRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnRpgHaiRate.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021CnRpgHaiRate.setUnits("Mb/s")


class _Ieee8021CnRpgGd_Type(Integer32):
    """Custom type ieee8021CnRpgGd based on Integer32"""
    defaultValue = 7


_Ieee8021CnRpgGd_Object = MibTableColumn
ieee8021CnRpgGd = _Ieee8021CnRpgGd_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 8, 1, 12),
    _Ieee8021CnRpgGd_Type()
)
ieee8021CnRpgGd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnRpgGd.setStatus("current")


class _Ieee8021CnRpgMinDecFac_Type(Unsigned32):
    """Custom type ieee8021CnRpgMinDecFac based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Ieee8021CnRpgMinDecFac_Type.__name__ = "Unsigned32"
_Ieee8021CnRpgMinDecFac_Object = MibTableColumn
ieee8021CnRpgMinDecFac = _Ieee8021CnRpgMinDecFac_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 8, 1, 13),
    _Ieee8021CnRpgMinDecFac_Type()
)
ieee8021CnRpgMinDecFac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnRpgMinDecFac.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021CnRpgMinDecFac.setUnits("percent")


class _Ieee8021CnRpgMinRate_Type(Unsigned32):
    """Custom type ieee8021CnRpgMinRate based on Unsigned32"""
    defaultValue = 5


_Ieee8021CnRpgMinRate_Object = MibTableColumn
ieee8021CnRpgMinRate = _Ieee8021CnRpgMinRate_Object(
    (1, 3, 111, 2, 802, 1, 1, 18, 1, 8, 1, 14),
    _Ieee8021CnRpgMinRate_Type()
)
ieee8021CnRpgMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021CnRpgMinRate.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021CnRpgMinRate.setUnits("Mb/s")
_Ieee8021CnConformance_ObjectIdentity = ObjectIdentity
ieee8021CnConformance = _Ieee8021CnConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 18, 2)
)
_Ieee8021CnCompliances_ObjectIdentity = ObjectIdentity
ieee8021CnCompliances = _Ieee8021CnCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 18, 2, 1)
)
_Ieee8021CnGroups_ObjectIdentity = ObjectIdentity
ieee8021CnGroups = _Ieee8021CnGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 18, 2, 2)
)

# Managed Objects groups

ieee8021CnGlobalReqdGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 18, 2, 2, 1)
)
ieee8021CnGlobalReqdGroup.setObjects(
      *(("IEEE8021-CN-MIB", "ieee8021CnGlobalMasterEnable"),
        ("IEEE8021-CN-MIB", "ieee8021CnComPriLldpInstanceChoice"),
        ("IEEE8021-CN-MIB", "ieee8021CnComPriLldpInstanceSelector"))
)
if mibBuilder.loadTexts:
    ieee8021CnGlobalReqdGroup.setStatus("current")

ieee8021CnCpGlobalGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 18, 2, 2, 2)
)
ieee8021CnCpGlobalGroup.setObjects(
      *(("IEEE8021-CN-MIB", "ieee8021CnGlobalCnmTransmitPriority"),
        ("IEEE8021-CN-MIB", "ieee8021CnGlobalDiscardedFrames"))
)
if mibBuilder.loadTexts:
    ieee8021CnCpGlobalGroup.setStatus("current")

ieee8021CnCpidTranslateGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 18, 2, 2, 3)
)
ieee8021CnCpidTranslateGroup.setObjects(
      *(("IEEE8021-CN-MIB", "ieee8021CnCpidToIfComponentId"),
        ("IEEE8021-CN-MIB", "ieee8021CnCpidToIfIfIndex"),
        ("IEEE8021-CN-MIB", "ieee8021CnCpidToIfCpIndex"))
)
if mibBuilder.loadTexts:
    ieee8021CnCpidTranslateGroup.setStatus("current")

ieee8021CnEplGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 18, 2, 2, 4)
)
ieee8021CnEplGroup.setObjects(
    ("IEEE8021-CN-MIB", "ieee8021CnEpIfIndex")
)
if mibBuilder.loadTexts:
    ieee8021CnEplGroup.setStatus("current")

ieee8021CnComPriGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 18, 2, 2, 5)
)
ieee8021CnComPriGroup.setObjects(
      *(("IEEE8021-CN-MIB", "ieee8021CnComPriDefModeChoice"),
        ("IEEE8021-CN-MIB", "ieee8021CnComPriAdminDefenseMode"),
        ("IEEE8021-CN-MIB", "ieee8021CnComPriCreation"),
        ("IEEE8021-CN-MIB", "ieee8021CnComPriRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021CnComPriGroup.setStatus("current")

ieee8021CnCpPriGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 18, 2, 2, 6)
)
ieee8021CnCpPriGroup.setObjects(
      *(("IEEE8021-CN-MIB", "ieee8021CnComPriAlternatePriority"),
        ("IEEE8021-CN-MIB", "ieee8021CnComPriAutoAltPri"))
)
if mibBuilder.loadTexts:
    ieee8021CnCpPriGroup.setStatus("current")

ieee8021CnGlobalPriPortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 18, 2, 2, 7)
)
ieee8021CnGlobalPriPortGroup.setObjects(
      *(("IEEE8021-CN-MIB", "ieee8021CnPortPriDefModeChoice"),
        ("IEEE8021-CN-MIB", "ieee8021CnPortPriAdminDefenseMode"),
        ("IEEE8021-CN-MIB", "ieee8021CnPortPriAutoDefenseMode"),
        ("IEEE8021-CN-MIB", "ieee8021CnPortPriLldpInstanceChoice"),
        ("IEEE8021-CN-MIB", "ieee8021CnPortPriLldpInstanceSelector"))
)
if mibBuilder.loadTexts:
    ieee8021CnGlobalPriPortGroup.setStatus("current")

ieee8021CnCpPriPortGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 18, 2, 2, 8)
)
ieee8021CnCpPriPortGroup.setObjects(
    ("IEEE8021-CN-MIB", "ieee8021CnPortPriAlternatePriority")
)
if mibBuilder.loadTexts:
    ieee8021CnCpPriPortGroup.setStatus("current")

ieee8021CnCpGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 18, 2, 2, 9)
)
ieee8021CnCpGroup.setObjects(
      *(("IEEE8021-CN-MIB", "ieee8021CnCpPriority"),
        ("IEEE8021-CN-MIB", "ieee8021CnCpMacAddress"),
        ("IEEE8021-CN-MIB", "ieee8021CnCpIdentifier"),
        ("IEEE8021-CN-MIB", "ieee8021CnCpQueueSizeSetPoint"),
        ("IEEE8021-CN-MIB", "ieee8021CnCpFeedbackWeight"),
        ("IEEE8021-CN-MIB", "ieee8021CnCpMinSampleBase"),
        ("IEEE8021-CN-MIB", "ieee8021CnCpDiscardedFrames"),
        ("IEEE8021-CN-MIB", "ieee8021CnCpTransmittedFrames"),
        ("IEEE8021-CN-MIB", "ieee8021CnCpTransmittedCnms"),
        ("IEEE8021-CN-MIB", "ieee8021CnCpMinHeaderOctets"))
)
if mibBuilder.loadTexts:
    ieee8021CnCpGroup.setStatus("current")

ieee8021CnRpppGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 18, 2, 2, 10)
)
ieee8021CnRpppGroup.setObjects(
      *(("IEEE8021-CN-MIB", "ieee8021CnRpPortPriMaxRps"),
        ("IEEE8021-CN-MIB", "ieee8021CnRpPortPriCreatedRps"),
        ("IEEE8021-CN-MIB", "ieee8021CnRpPortPriCentiseconds"))
)
if mibBuilder.loadTexts:
    ieee8021CnRpppGroup.setStatus("current")

ieee8021CnRpGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 18, 2, 2, 11)
)
ieee8021CnRpGroup.setObjects(
      *(("IEEE8021-CN-MIB", "ieee8021CnRpgEnable"),
        ("IEEE8021-CN-MIB", "ieee8021CnRpgTimeReset"),
        ("IEEE8021-CN-MIB", "ieee8021CnRpgByteReset"),
        ("IEEE8021-CN-MIB", "ieee8021CnRpgThreshold"),
        ("IEEE8021-CN-MIB", "ieee8021CnRpgMaxRate"),
        ("IEEE8021-CN-MIB", "ieee8021CnRpgAiRate"),
        ("IEEE8021-CN-MIB", "ieee8021CnRpgHaiRate"),
        ("IEEE8021-CN-MIB", "ieee8021CnRpgGd"),
        ("IEEE8021-CN-MIB", "ieee8021CnRpgMinDecFac"),
        ("IEEE8021-CN-MIB", "ieee8021CnRpgMinRate"))
)
if mibBuilder.loadTexts:
    ieee8021CnRpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021CnBridgeCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 18, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021CnBridgeCompliance.setStatus(
        "current"
    )

ieee8021CnStationCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 18, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021CnStationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-CN-MIB",
    **{"Ieee8021CnControlChoice": Ieee8021CnControlChoice,
       "Ieee8021CnDefenseMode": Ieee8021CnDefenseMode,
       "Ieee8021CnLldpChoice": Ieee8021CnLldpChoice,
       "ieee8021CnMib": ieee8021CnMib,
       "ieee8021CnMIBObjects": ieee8021CnMIBObjects,
       "ieee8021CnGlobalTable": ieee8021CnGlobalTable,
       "ieee8021CnGlobalEntry": ieee8021CnGlobalEntry,
       "ieee8021CnGlobalComponentId": ieee8021CnGlobalComponentId,
       "ieee8021CnGlobalMasterEnable": ieee8021CnGlobalMasterEnable,
       "ieee8021CnGlobalCnmTransmitPriority": ieee8021CnGlobalCnmTransmitPriority,
       "ieee8021CnGlobalDiscardedFrames": ieee8021CnGlobalDiscardedFrames,
       "ieee8021CnErroredPortTable": ieee8021CnErroredPortTable,
       "ieee8021CnErroredPortEntry": ieee8021CnErroredPortEntry,
       "ieee8021CnEpComponentId": ieee8021CnEpComponentId,
       "ieee8021CnEpPriority": ieee8021CnEpPriority,
       "ieee8021CnEpIfIndex": ieee8021CnEpIfIndex,
       "ieee8021CnCompntPriTable": ieee8021CnCompntPriTable,
       "ieee8021CnCompntPriEntry": ieee8021CnCompntPriEntry,
       "ieee8021CnComPriComponentId": ieee8021CnComPriComponentId,
       "ieee8021CnComPriPriority": ieee8021CnComPriPriority,
       "ieee8021CnComPriDefModeChoice": ieee8021CnComPriDefModeChoice,
       "ieee8021CnComPriAlternatePriority": ieee8021CnComPriAlternatePriority,
       "ieee8021CnComPriAutoAltPri": ieee8021CnComPriAutoAltPri,
       "ieee8021CnComPriAdminDefenseMode": ieee8021CnComPriAdminDefenseMode,
       "ieee8021CnComPriCreation": ieee8021CnComPriCreation,
       "ieee8021CnComPriLldpInstanceChoice": ieee8021CnComPriLldpInstanceChoice,
       "ieee8021CnComPriLldpInstanceSelector": ieee8021CnComPriLldpInstanceSelector,
       "ieee8021CnComPriRowStatus": ieee8021CnComPriRowStatus,
       "ieee8021CnPortPriTable": ieee8021CnPortPriTable,
       "ieee8021CnPortPriEntry": ieee8021CnPortPriEntry,
       "ieee8021CnPortPriComponentId": ieee8021CnPortPriComponentId,
       "ieee8021CnPortPriority": ieee8021CnPortPriority,
       "ieee8021CnPortPriIfIndex": ieee8021CnPortPriIfIndex,
       "ieee8021CnPortPriDefModeChoice": ieee8021CnPortPriDefModeChoice,
       "ieee8021CnPortPriAdminDefenseMode": ieee8021CnPortPriAdminDefenseMode,
       "ieee8021CnPortPriAutoDefenseMode": ieee8021CnPortPriAutoDefenseMode,
       "ieee8021CnPortPriLldpInstanceChoice": ieee8021CnPortPriLldpInstanceChoice,
       "ieee8021CnPortPriLldpInstanceSelector": ieee8021CnPortPriLldpInstanceSelector,
       "ieee8021CnPortPriAlternatePriority": ieee8021CnPortPriAlternatePriority,
       "ieee8021CnCpTable": ieee8021CnCpTable,
       "ieee8021CnCpEntry": ieee8021CnCpEntry,
       "ieee8021CnCpComponentId": ieee8021CnCpComponentId,
       "ieee8021CnCpIfIndex": ieee8021CnCpIfIndex,
       "ieee8021CnCpIndex": ieee8021CnCpIndex,
       "ieee8021CnCpPriority": ieee8021CnCpPriority,
       "ieee8021CnCpMacAddress": ieee8021CnCpMacAddress,
       "ieee8021CnCpIdentifier": ieee8021CnCpIdentifier,
       "ieee8021CnCpQueueSizeSetPoint": ieee8021CnCpQueueSizeSetPoint,
       "ieee8021CnCpFeedbackWeight": ieee8021CnCpFeedbackWeight,
       "ieee8021CnCpMinSampleBase": ieee8021CnCpMinSampleBase,
       "ieee8021CnCpDiscardedFrames": ieee8021CnCpDiscardedFrames,
       "ieee8021CnCpTransmittedFrames": ieee8021CnCpTransmittedFrames,
       "ieee8021CnCpTransmittedCnms": ieee8021CnCpTransmittedCnms,
       "ieee8021CnCpMinHeaderOctets": ieee8021CnCpMinHeaderOctets,
       "ieee8021CnCpidToInterfaceTable": ieee8021CnCpidToInterfaceTable,
       "ieee8021CnCpidToInterfaceEntry": ieee8021CnCpidToInterfaceEntry,
       "ieee8021CnCpidToIfCpid": ieee8021CnCpidToIfCpid,
       "ieee8021CnCpidToIfComponentId": ieee8021CnCpidToIfComponentId,
       "ieee8021CnCpidToIfIfIndex": ieee8021CnCpidToIfIfIndex,
       "ieee8021CnCpidToIfCpIndex": ieee8021CnCpidToIfCpIndex,
       "ieee8021CnRpPortPriTable": ieee8021CnRpPortPriTable,
       "ieee8021CnRpPortPriEntry": ieee8021CnRpPortPriEntry,
       "ieee8021CnRpPortPriComponentId": ieee8021CnRpPortPriComponentId,
       "ieee8021CnRpPortPriPriority": ieee8021CnRpPortPriPriority,
       "ieee8021CnRpPortPriIfIndex": ieee8021CnRpPortPriIfIndex,
       "ieee8021CnRpPortPriMaxRps": ieee8021CnRpPortPriMaxRps,
       "ieee8021CnRpPortPriCreatedRps": ieee8021CnRpPortPriCreatedRps,
       "ieee8021CnRpPortPriCentiseconds": ieee8021CnRpPortPriCentiseconds,
       "ieee8021CnRpGroupTable": ieee8021CnRpGroupTable,
       "ieee8021CnRpGroupEntry": ieee8021CnRpGroupEntry,
       "ieee8021CnRpgComponentId": ieee8021CnRpgComponentId,
       "ieee8021CnRpgPriority": ieee8021CnRpgPriority,
       "ieee8021CnRpgIfIndex": ieee8021CnRpgIfIndex,
       "ieee8021CnRpgIdentifier": ieee8021CnRpgIdentifier,
       "ieee8021CnRpgEnable": ieee8021CnRpgEnable,
       "ieee8021CnRpgTimeReset": ieee8021CnRpgTimeReset,
       "ieee8021CnRpgByteReset": ieee8021CnRpgByteReset,
       "ieee8021CnRpgThreshold": ieee8021CnRpgThreshold,
       "ieee8021CnRpgMaxRate": ieee8021CnRpgMaxRate,
       "ieee8021CnRpgAiRate": ieee8021CnRpgAiRate,
       "ieee8021CnRpgHaiRate": ieee8021CnRpgHaiRate,
       "ieee8021CnRpgGd": ieee8021CnRpgGd,
       "ieee8021CnRpgMinDecFac": ieee8021CnRpgMinDecFac,
       "ieee8021CnRpgMinRate": ieee8021CnRpgMinRate,
       "ieee8021CnConformance": ieee8021CnConformance,
       "ieee8021CnCompliances": ieee8021CnCompliances,
       "ieee8021CnBridgeCompliance": ieee8021CnBridgeCompliance,
       "ieee8021CnStationCompliance": ieee8021CnStationCompliance,
       "ieee8021CnGroups": ieee8021CnGroups,
       "ieee8021CnGlobalReqdGroup": ieee8021CnGlobalReqdGroup,
       "ieee8021CnCpGlobalGroup": ieee8021CnCpGlobalGroup,
       "ieee8021CnCpidTranslateGroup": ieee8021CnCpidTranslateGroup,
       "ieee8021CnEplGroup": ieee8021CnEplGroup,
       "ieee8021CnComPriGroup": ieee8021CnComPriGroup,
       "ieee8021CnCpPriGroup": ieee8021CnCpPriGroup,
       "ieee8021CnGlobalPriPortGroup": ieee8021CnGlobalPriPortGroup,
       "ieee8021CnCpPriPortGroup": ieee8021CnCpPriPortGroup,
       "ieee8021CnCpGroup": ieee8021CnCpGroup,
       "ieee8021CnRpppGroup": ieee8021CnRpppGroup,
       "ieee8021CnRpGroup": ieee8021CnRpGroup}
)
