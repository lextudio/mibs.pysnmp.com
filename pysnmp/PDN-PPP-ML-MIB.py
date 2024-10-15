# SNMP MIB module (PDN-PPP-ML-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-PPP-ML-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:02 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(pdn_interfaces,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-interfaces")

(PdnPPPState,
 SwitchState) = mibBuilder.importSymbols(
    "PDN-TC",
    "PdnPPPState",
    "SwitchState")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

pdnPppMlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30)
)
pdnPppMlMIB.setRevisions(
        ("2004-09-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MRRU(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class SSNHF(Integer32, TextualConvention):
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
        *(("ssnhf12BitSeqNbrs", 2),
          ("ssnhf24BitSeqNbrs", 3),
          ("ssnhfUnknown", 1))
    )



class EDClass(Integer32, TextualConvention):
    status = "current"
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
        *(("ieee802", 3),
          ("ipAddr", 2),
          ("locallyAssigned", 1),
          ("nullClass", 0),
          ("pppMagicNbrBlk", 4),
          ("publicSwNetDirNbr", 5))
    )



# MIB Managed Objects in the order of their OIDs

_PdnPppMlNotifications_ObjectIdentity = ObjectIdentity
pdnPppMlNotifications = _PdnPppMlNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 0)
)
_PdnPppMlObjects_ObjectIdentity = ObjectIdentity
pdnPppMlObjects = _PdnPppMlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1)
)
_PdnPppMlBundleNumber_Type = Unsigned32
_PdnPppMlBundleNumber_Object = MibScalar
pdnPppMlBundleNumber = _PdnPppMlBundleNumber_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 1),
    _PdnPppMlBundleNumber_Type()
)
pdnPppMlBundleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppMlBundleNumber.setStatus("current")
_PdnPppMlBundleConfigTable_Object = MibTable
pdnPppMlBundleConfigTable = _PdnPppMlBundleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 2)
)
if mibBuilder.loadTexts:
    pdnPppMlBundleConfigTable.setStatus("current")
_PdnPppMlBundleConfigEntry_Object = MibTableRow
pdnPppMlBundleConfigEntry = _PdnPppMlBundleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 2, 1)
)
pdnPppMlBundleConfigEntry.setIndexNames(
    (0, "PDN-PPP-ML-MIB", "pdnPppMlBundleIfIndex"),
)
if mibBuilder.loadTexts:
    pdnPppMlBundleConfigEntry.setStatus("current")
_PdnPppMlBundleIfIndex_Type = InterfaceIndex
_PdnPppMlBundleIfIndex_Object = MibTableColumn
pdnPppMlBundleIfIndex = _PdnPppMlBundleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 2, 1, 1),
    _PdnPppMlBundleIfIndex_Type()
)
pdnPppMlBundleIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnPppMlBundleIfIndex.setStatus("current")
_PdnPppMlBundleConfigRowStatus_Type = RowStatus
_PdnPppMlBundleConfigRowStatus_Object = MibTableColumn
pdnPppMlBundleConfigRowStatus = _PdnPppMlBundleConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 2, 1, 2),
    _PdnPppMlBundleConfigRowStatus_Type()
)
pdnPppMlBundleConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnPppMlBundleConfigRowStatus.setStatus("current")
_PdnPppMlBundleConfigMRRU_Type = MRRU
_PdnPppMlBundleConfigMRRU_Object = MibTableColumn
pdnPppMlBundleConfigMRRU = _PdnPppMlBundleConfigMRRU_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 2, 1, 3),
    _PdnPppMlBundleConfigMRRU_Type()
)
pdnPppMlBundleConfigMRRU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnPppMlBundleConfigMRRU.setStatus("current")
if mibBuilder.loadTexts:
    pdnPppMlBundleConfigMRRU.setUnits("Number of octets")
_PdnPppMlBundleConfigSSNHF_Type = SwitchState
_PdnPppMlBundleConfigSSNHF_Object = MibTableColumn
pdnPppMlBundleConfigSSNHF = _PdnPppMlBundleConfigSSNHF_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 2, 1, 4),
    _PdnPppMlBundleConfigSSNHF_Type()
)
pdnPppMlBundleConfigSSNHF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnPppMlBundleConfigSSNHF.setStatus("current")


class _PdnPppMlBundleConfigFragmentSize_Type(Unsigned32):
    """Custom type pdnPppMlBundleConfigFragmentSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967296),
    )


_PdnPppMlBundleConfigFragmentSize_Type.__name__ = "Unsigned32"
_PdnPppMlBundleConfigFragmentSize_Object = MibTableColumn
pdnPppMlBundleConfigFragmentSize = _PdnPppMlBundleConfigFragmentSize_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 2, 1, 5),
    _PdnPppMlBundleConfigFragmentSize_Type()
)
pdnPppMlBundleConfigFragmentSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnPppMlBundleConfigFragmentSize.setStatus("current")
_PdnPppMlBundleMappingTable_Object = MibTable
pdnPppMlBundleMappingTable = _PdnPppMlBundleMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 3)
)
if mibBuilder.loadTexts:
    pdnPppMlBundleMappingTable.setStatus("current")
_PdnPppMlBundleMappingEntry_Object = MibTableRow
pdnPppMlBundleMappingEntry = _PdnPppMlBundleMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 3, 1)
)
pdnPppMlBundleMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnPppMlBundleMappingEntry.setStatus("current")
_PdnPppMlBundleMappingRowStatus_Type = RowStatus
_PdnPppMlBundleMappingRowStatus_Object = MibTableColumn
pdnPppMlBundleMappingRowStatus = _PdnPppMlBundleMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 3, 1, 1),
    _PdnPppMlBundleMappingRowStatus_Type()
)
pdnPppMlBundleMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnPppMlBundleMappingRowStatus.setStatus("current")
_PdnPppMlBundleMappingBundleIfIndex_Type = InterfaceIndex
_PdnPppMlBundleMappingBundleIfIndex_Object = MibTableColumn
pdnPppMlBundleMappingBundleIfIndex = _PdnPppMlBundleMappingBundleIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 3, 1, 2),
    _PdnPppMlBundleMappingBundleIfIndex_Type()
)
pdnPppMlBundleMappingBundleIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnPppMlBundleMappingBundleIfIndex.setStatus("current")
_PdnPppMlBundleStatusTable_Object = MibTable
pdnPppMlBundleStatusTable = _PdnPppMlBundleStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4)
)
if mibBuilder.loadTexts:
    pdnPppMlBundleStatusTable.setStatus("current")
_PdnPppMlBundleStatusEntry_Object = MibTableRow
pdnPppMlBundleStatusEntry = _PdnPppMlBundleStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1)
)
pdnPppMlBundleStatusEntry.setIndexNames(
    (0, "PDN-PPP-ML-MIB", "pdnPppMlBundleIfIndex"),
)
if mibBuilder.loadTexts:
    pdnPppMlBundleStatusEntry.setStatus("current")
_PdnPppMlBundleStatusCurrState_Type = PdnPPPState
_PdnPppMlBundleStatusCurrState_Object = MibTableColumn
pdnPppMlBundleStatusCurrState = _PdnPppMlBundleStatusCurrState_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 1),
    _PdnPppMlBundleStatusCurrState_Type()
)
pdnPppMlBundleStatusCurrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppMlBundleStatusCurrState.setStatus("current")
_PdnPppMlBundleStatusLocalToRemoteMRRU_Type = MRRU
_PdnPppMlBundleStatusLocalToRemoteMRRU_Object = MibTableColumn
pdnPppMlBundleStatusLocalToRemoteMRRU = _PdnPppMlBundleStatusLocalToRemoteMRRU_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 2),
    _PdnPppMlBundleStatusLocalToRemoteMRRU_Type()
)
pdnPppMlBundleStatusLocalToRemoteMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppMlBundleStatusLocalToRemoteMRRU.setStatus("current")
if mibBuilder.loadTexts:
    pdnPppMlBundleStatusLocalToRemoteMRRU.setUnits("Number of octets")
_PdnPppMlBundleStatusRemoteToLocalMRRU_Type = MRRU
_PdnPppMlBundleStatusRemoteToLocalMRRU_Object = MibTableColumn
pdnPppMlBundleStatusRemoteToLocalMRRU = _PdnPppMlBundleStatusRemoteToLocalMRRU_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 3),
    _PdnPppMlBundleStatusRemoteToLocalMRRU_Type()
)
pdnPppMlBundleStatusRemoteToLocalMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppMlBundleStatusRemoteToLocalMRRU.setStatus("current")
if mibBuilder.loadTexts:
    pdnPppMlBundleStatusRemoteToLocalMRRU.setUnits("Number of octets")
_PdnPppMlBundleStatusLocalToRemoteSSNHF_Type = SSNHF
_PdnPppMlBundleStatusLocalToRemoteSSNHF_Object = MibTableColumn
pdnPppMlBundleStatusLocalToRemoteSSNHF = _PdnPppMlBundleStatusLocalToRemoteSSNHF_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 4),
    _PdnPppMlBundleStatusLocalToRemoteSSNHF_Type()
)
pdnPppMlBundleStatusLocalToRemoteSSNHF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppMlBundleStatusLocalToRemoteSSNHF.setStatus("current")
_PdnPppMlBundleStatusRemoteToLocalSSNHF_Type = SSNHF
_PdnPppMlBundleStatusRemoteToLocalSSNHF_Object = MibTableColumn
pdnPppMlBundleStatusRemoteToLocalSSNHF = _PdnPppMlBundleStatusRemoteToLocalSSNHF_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 5),
    _PdnPppMlBundleStatusRemoteToLocalSSNHF_Type()
)
pdnPppMlBundleStatusRemoteToLocalSSNHF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppMlBundleStatusRemoteToLocalSSNHF.setStatus("current")
_PdnPppMlBundleStatusLocalToRemoteEDClass_Type = EDClass
_PdnPppMlBundleStatusLocalToRemoteEDClass_Object = MibTableColumn
pdnPppMlBundleStatusLocalToRemoteEDClass = _PdnPppMlBundleStatusLocalToRemoteEDClass_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 6),
    _PdnPppMlBundleStatusLocalToRemoteEDClass_Type()
)
pdnPppMlBundleStatusLocalToRemoteEDClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppMlBundleStatusLocalToRemoteEDClass.setStatus("current")
_PdnPppMlBundleStatusLocalToRemoteEDAddr_Type = DisplayString
_PdnPppMlBundleStatusLocalToRemoteEDAddr_Object = MibTableColumn
pdnPppMlBundleStatusLocalToRemoteEDAddr = _PdnPppMlBundleStatusLocalToRemoteEDAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 7),
    _PdnPppMlBundleStatusLocalToRemoteEDAddr_Type()
)
pdnPppMlBundleStatusLocalToRemoteEDAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppMlBundleStatusLocalToRemoteEDAddr.setStatus("current")
_PdnPppMlBundleStatusRemoteToLocalEDClass_Type = EDClass
_PdnPppMlBundleStatusRemoteToLocalEDClass_Object = MibTableColumn
pdnPppMlBundleStatusRemoteToLocalEDClass = _PdnPppMlBundleStatusRemoteToLocalEDClass_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 8),
    _PdnPppMlBundleStatusRemoteToLocalEDClass_Type()
)
pdnPppMlBundleStatusRemoteToLocalEDClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppMlBundleStatusRemoteToLocalEDClass.setStatus("current")
_PdnPppMlBundleStatusRemoteToLocalEDAddr_Type = DisplayString
_PdnPppMlBundleStatusRemoteToLocalEDAddr_Object = MibTableColumn
pdnPppMlBundleStatusRemoteToLocalEDAddr = _PdnPppMlBundleStatusRemoteToLocalEDAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 1, 4, 1, 9),
    _PdnPppMlBundleStatusRemoteToLocalEDAddr_Type()
)
pdnPppMlBundleStatusRemoteToLocalEDAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPppMlBundleStatusRemoteToLocalEDAddr.setStatus("current")
_PdnPppMlAFNs_ObjectIdentity = ObjectIdentity
pdnPppMlAFNs = _PdnPppMlAFNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 2)
)
_PdnPppMlConformance_ObjectIdentity = ObjectIdentity
pdnPppMlConformance = _PdnPppMlConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3)
)
_PdnPppMlCompliances_ObjectIdentity = ObjectIdentity
pdnPppMlCompliances = _PdnPppMlCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 1)
)
_PdnPppMlGroups_ObjectIdentity = ObjectIdentity
pdnPppMlGroups = _PdnPppMlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2)
)
_PdnPppMlObjGroups_ObjectIdentity = ObjectIdentity
pdnPppMlObjGroups = _PdnPppMlObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 1)
)
_PdnPppMlAfnGroups_ObjectIdentity = ObjectIdentity
pdnPppMlAfnGroups = _PdnPppMlAfnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 2)
)
_PdnPppmlNtfyGroups_ObjectIdentity = ObjectIdentity
pdnPppmlNtfyGroups = _PdnPppmlNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 3)
)

# Managed Objects groups

pdnPppMlBundleDefinitionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 1, 1)
)
pdnPppMlBundleDefinitionGroup.setObjects(
      *(("PDN-PPP-ML-MIB", "pdnPppMlBundleNumber"),
        ("PDN-PPP-ML-MIB", "pdnPppMlBundleConfigRowStatus"),
        ("PDN-PPP-ML-MIB", "pdnPppMlBundleMappingBundleIfIndex"),
        ("PDN-PPP-ML-MIB", "pdnPppMlBundleMappingRowStatus"))
)
if mibBuilder.loadTexts:
    pdnPppMlBundleDefinitionGroup.setStatus("current")

pdnPppMlBundleStateMachineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 1, 2)
)
pdnPppMlBundleStateMachineGroup.setObjects(
    ("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusCurrState")
)
if mibBuilder.loadTexts:
    pdnPppMlBundleStateMachineGroup.setStatus("current")

pdnPppMlBundleMRRUGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 1, 3)
)
pdnPppMlBundleMRRUGroup.setObjects(
      *(("PDN-PPP-ML-MIB", "pdnPppMlBundleConfigRowStatus"),
        ("PDN-PPP-ML-MIB", "pdnPppMlBundleConfigMRRU"),
        ("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusLocalToRemoteMRRU"),
        ("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusRemoteToLocalMRRU"))
)
if mibBuilder.loadTexts:
    pdnPppMlBundleMRRUGroup.setStatus("current")

pdnPppMlBundleSSNHFGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 1, 4)
)
pdnPppMlBundleSSNHFGroup.setObjects(
      *(("PDN-PPP-ML-MIB", "pdnPppMlBundleConfigRowStatus"),
        ("PDN-PPP-ML-MIB", "pdnPppMlBundleConfigSSNHF"),
        ("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusLocalToRemoteSSNHF"),
        ("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusRemoteToLocalSSNHF"))
)
if mibBuilder.loadTexts:
    pdnPppMlBundleSSNHFGroup.setStatus("current")

pdnPppMlBundleEDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 1, 5)
)
pdnPppMlBundleEDGroup.setObjects(
      *(("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusLocalToRemoteEDClass"),
        ("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusLocalToRemoteEDAddr"),
        ("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusRemoteToLocalEDClass"),
        ("PDN-PPP-ML-MIB", "pdnPppMlBundleStatusRemoteToLocalEDAddr"))
)
if mibBuilder.loadTexts:
    pdnPppMlBundleEDGroup.setStatus("current")

pdnPppMlBundleFragmentSizeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 2, 1, 6)
)
pdnPppMlBundleFragmentSizeGroup.setObjects(
      *(("PDN-PPP-ML-MIB", "pdnPppMlBundleConfigRowStatus"),
        ("PDN-PPP-ML-MIB", "pdnPppMlBundleConfigFragmentSize"))
)
if mibBuilder.loadTexts:
    pdnPppMlBundleFragmentSizeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnPppMlCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 30, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnPppMlCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-PPP-ML-MIB",
    **{"MRRU": MRRU,
       "SSNHF": SSNHF,
       "EDClass": EDClass,
       "pdnPppMlMIB": pdnPppMlMIB,
       "pdnPppMlNotifications": pdnPppMlNotifications,
       "pdnPppMlObjects": pdnPppMlObjects,
       "pdnPppMlBundleNumber": pdnPppMlBundleNumber,
       "pdnPppMlBundleConfigTable": pdnPppMlBundleConfigTable,
       "pdnPppMlBundleConfigEntry": pdnPppMlBundleConfigEntry,
       "pdnPppMlBundleIfIndex": pdnPppMlBundleIfIndex,
       "pdnPppMlBundleConfigRowStatus": pdnPppMlBundleConfigRowStatus,
       "pdnPppMlBundleConfigMRRU": pdnPppMlBundleConfigMRRU,
       "pdnPppMlBundleConfigSSNHF": pdnPppMlBundleConfigSSNHF,
       "pdnPppMlBundleConfigFragmentSize": pdnPppMlBundleConfigFragmentSize,
       "pdnPppMlBundleMappingTable": pdnPppMlBundleMappingTable,
       "pdnPppMlBundleMappingEntry": pdnPppMlBundleMappingEntry,
       "pdnPppMlBundleMappingRowStatus": pdnPppMlBundleMappingRowStatus,
       "pdnPppMlBundleMappingBundleIfIndex": pdnPppMlBundleMappingBundleIfIndex,
       "pdnPppMlBundleStatusTable": pdnPppMlBundleStatusTable,
       "pdnPppMlBundleStatusEntry": pdnPppMlBundleStatusEntry,
       "pdnPppMlBundleStatusCurrState": pdnPppMlBundleStatusCurrState,
       "pdnPppMlBundleStatusLocalToRemoteMRRU": pdnPppMlBundleStatusLocalToRemoteMRRU,
       "pdnPppMlBundleStatusRemoteToLocalMRRU": pdnPppMlBundleStatusRemoteToLocalMRRU,
       "pdnPppMlBundleStatusLocalToRemoteSSNHF": pdnPppMlBundleStatusLocalToRemoteSSNHF,
       "pdnPppMlBundleStatusRemoteToLocalSSNHF": pdnPppMlBundleStatusRemoteToLocalSSNHF,
       "pdnPppMlBundleStatusLocalToRemoteEDClass": pdnPppMlBundleStatusLocalToRemoteEDClass,
       "pdnPppMlBundleStatusLocalToRemoteEDAddr": pdnPppMlBundleStatusLocalToRemoteEDAddr,
       "pdnPppMlBundleStatusRemoteToLocalEDClass": pdnPppMlBundleStatusRemoteToLocalEDClass,
       "pdnPppMlBundleStatusRemoteToLocalEDAddr": pdnPppMlBundleStatusRemoteToLocalEDAddr,
       "pdnPppMlAFNs": pdnPppMlAFNs,
       "pdnPppMlConformance": pdnPppMlConformance,
       "pdnPppMlCompliances": pdnPppMlCompliances,
       "pdnPppMlCompliance": pdnPppMlCompliance,
       "pdnPppMlGroups": pdnPppMlGroups,
       "pdnPppMlObjGroups": pdnPppMlObjGroups,
       "pdnPppMlBundleDefinitionGroup": pdnPppMlBundleDefinitionGroup,
       "pdnPppMlBundleStateMachineGroup": pdnPppMlBundleStateMachineGroup,
       "pdnPppMlBundleMRRUGroup": pdnPppMlBundleMRRUGroup,
       "pdnPppMlBundleSSNHFGroup": pdnPppMlBundleSSNHFGroup,
       "pdnPppMlBundleEDGroup": pdnPppMlBundleEDGroup,
       "pdnPppMlBundleFragmentSizeGroup": pdnPppMlBundleFragmentSizeGroup,
       "pdnPppMlAfnGroups": pdnPppMlAfnGroups,
       "pdnPppmlNtfyGroups": pdnPppmlNtfyGroups}
)
