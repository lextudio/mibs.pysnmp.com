# SNMP MIB module (CHIPMODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHIPMODULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:49 2024
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

(DisplayString,) = mibBuilder.importSymbols(
    "RFC1155-SMI",
    "DisplayString")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Chipcom_ObjectIdentity = ObjectIdentity
chipcom = _Chipcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49)
)
_Chipmib02_ObjectIdentity = ObjectIdentity
chipmib02 = _Chipmib02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2)
)
_ChipGen_ObjectIdentity = ObjectIdentity
chipGen = _ChipGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 1)
)
_ChipEcho_ObjectIdentity = ObjectIdentity
chipEcho = _ChipEcho_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 2)
)
_ChipProducts_ObjectIdentity = ObjectIdentity
chipProducts = _ChipProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3)
)
_Online_ObjectIdentity = ObjectIdentity
online = _Online_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1)
)
_OlAgents_ObjectIdentity = ObjectIdentity
olAgents = _OlAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1)
)
_OlConc_ObjectIdentity = ObjectIdentity
olConc = _OlConc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 2)
)
_OlEnv_ObjectIdentity = ObjectIdentity
olEnv = _OlEnv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3)
)
_OlModules_ObjectIdentity = ObjectIdentity
olModules = _OlModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4)
)
_OlSpecMods_ObjectIdentity = ObjectIdentity
olSpecMods = _OlSpecMods_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4)
)
_Ol50nnMCTL_ObjectIdentity = ObjectIdentity
ol50nnMCTL = _Ol50nnMCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 3)
)
_Ol50nnMCTLModTable_Object = MibTable
ol50nnMCTLModTable = _Ol50nnMCTLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 3, 1)
)
if mibBuilder.loadTexts:
    ol50nnMCTLModTable.setStatus("mandatory")
_Ol50nnMCTLModEntry_Object = MibTableRow
ol50nnMCTLModEntry = _Ol50nnMCTLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 3, 1, 1)
)
ol50nnMCTLModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol50nnMCTLModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol50nnMCTLModEntry.setStatus("mandatory")
_Ol50nnMCTLModSlotIndex_Type = Integer32
_Ol50nnMCTLModSlotIndex_Object = MibTableColumn
ol50nnMCTLModSlotIndex = _Ol50nnMCTLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 3, 1, 1, 1),
    _Ol50nnMCTLModSlotIndex_Type()
)
ol50nnMCTLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMCTLModSlotIndex.setStatus("mandatory")


class _Ol50nnMCTLModTempStatus_Type(Integer32):
    """Custom type ol50nnMCTLModTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extremeTemp", 2),
          ("okay", 1))
    )


_Ol50nnMCTLModTempStatus_Type.__name__ = "Integer32"
_Ol50nnMCTLModTempStatus_Object = MibTableColumn
ol50nnMCTLModTempStatus = _Ol50nnMCTLModTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 3, 1, 1, 2),
    _Ol50nnMCTLModTempStatus_Type()
)
ol50nnMCTLModTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMCTLModTempStatus.setStatus("mandatory")
_Ol51nnMMGT_ObjectIdentity = ObjectIdentity
ol51nnMMGT = _Ol51nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4)
)
_Ol51nnMMGTModTable_Object = MibTable
ol51nnMMGTModTable = _Ol51nnMMGTModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 1)
)
if mibBuilder.loadTexts:
    ol51nnMMGTModTable.setStatus("mandatory")
_Ol51nnMMGTModEntry_Object = MibTableRow
ol51nnMMGTModEntry = _Ol51nnMMGTModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 1, 1)
)
ol51nnMMGTModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMMGTModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMMGTModEntry.setStatus("mandatory")
_Ol51nnMMGTModSlotIndex_Type = Integer32
_Ol51nnMMGTModSlotIndex_Object = MibTableColumn
ol51nnMMGTModSlotIndex = _Ol51nnMMGTModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 1, 1, 1),
    _Ol51nnMMGTModSlotIndex_Type()
)
ol51nnMMGTModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMMGTModSlotIndex.setStatus("mandatory")


class _Ol51nnMMGTModMasterPriority_Type(Integer32):
    """Custom type ol51nnMMGTModMasterPriority based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("four", 4),
          ("nine", 9),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("ten", 10),
          ("three", 3),
          ("two", 2))
    )


_Ol51nnMMGTModMasterPriority_Type.__name__ = "Integer32"
_Ol51nnMMGTModMasterPriority_Object = MibTableColumn
ol51nnMMGTModMasterPriority = _Ol51nnMMGTModMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 1, 1, 2),
    _Ol51nnMMGTModMasterPriority_Type()
)
ol51nnMMGTModMasterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMMGTModMasterPriority.setStatus("mandatory")


class _Ol51nnMMGTModMasterStatus_Type(Integer32):
    """Custom type ol51nnMMGTModMasterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("electing", 3),
          ("master", 1),
          ("non-master", 2))
    )


_Ol51nnMMGTModMasterStatus_Type.__name__ = "Integer32"
_Ol51nnMMGTModMasterStatus_Object = MibTableColumn
ol51nnMMGTModMasterStatus = _Ol51nnMMGTModMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 1, 1, 3),
    _Ol51nnMMGTModMasterStatus_Type()
)
ol51nnMMGTModMasterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMMGTModMasterStatus.setStatus("mandatory")


class _Ol51nnMMGTModStationAddr_Type(OctetString):
    """Custom type ol51nnMMGTModStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol51nnMMGTModStationAddr_Type.__name__ = "OctetString"
_Ol51nnMMGTModStationAddr_Object = MibTableColumn
ol51nnMMGTModStationAddr = _Ol51nnMMGTModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 1, 1, 4),
    _Ol51nnMMGTModStationAddr_Type()
)
ol51nnMMGTModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMMGTModStationAddr.setStatus("mandatory")
_Ol51nnMMGTPortTable_Object = MibTable
ol51nnMMGTPortTable = _Ol51nnMMGTPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 2)
)
if mibBuilder.loadTexts:
    ol51nnMMGTPortTable.setStatus("mandatory")
_Ol51nnMMGTPortEntry_Object = MibTableRow
ol51nnMMGTPortEntry = _Ol51nnMMGTPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 2, 1)
)
ol51nnMMGTPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMMGTPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnMMGTPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMMGTPortEntry.setStatus("mandatory")
_Ol51nnMMGTPortSlotIndex_Type = Integer32
_Ol51nnMMGTPortSlotIndex_Object = MibTableColumn
ol51nnMMGTPortSlotIndex = _Ol51nnMMGTPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 2, 1, 1),
    _Ol51nnMMGTPortSlotIndex_Type()
)
ol51nnMMGTPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMMGTPortSlotIndex.setStatus("mandatory")
_Ol51nnMMGTPortIndex_Type = Integer32
_Ol51nnMMGTPortIndex_Object = MibTableColumn
ol51nnMMGTPortIndex = _Ol51nnMMGTPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 2, 1, 2),
    _Ol51nnMMGTPortIndex_Type()
)
ol51nnMMGTPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMMGTPortIndex.setStatus("mandatory")
_Ol51nnMMGTIpAddress_Type = IpAddress
_Ol51nnMMGTIpAddress_Object = MibTableColumn
ol51nnMMGTIpAddress = _Ol51nnMMGTIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4, 2, 1, 3),
    _Ol51nnMMGTIpAddress_Type()
)
ol51nnMMGTIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMMGTIpAddress.setStatus("mandatory")
_Ol51nnMFIB_ObjectIdentity = ObjectIdentity
ol51nnMFIB = _Ol51nnMFIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5)
)
_Ol51nnMFIBModTable_Object = MibTable
ol51nnMFIBModTable = _Ol51nnMFIBModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 1)
)
if mibBuilder.loadTexts:
    ol51nnMFIBModTable.setStatus("mandatory")
_Ol51nnMFIBModEntry_Object = MibTableRow
ol51nnMFIBModEntry = _Ol51nnMFIBModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 1, 1)
)
ol51nnMFIBModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMFIBModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFIBModEntry.setStatus("mandatory")
_Ol51nnMFIBModSlotIndex_Type = Integer32
_Ol51nnMFIBModSlotIndex_Object = MibTableColumn
ol51nnMFIBModSlotIndex = _Ol51nnMFIBModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 1, 1, 1),
    _Ol51nnMFIBModSlotIndex_Type()
)
ol51nnMFIBModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFIBModSlotIndex.setStatus("mandatory")


class _Ol51nnMFIBModDipNetwork_Type(Integer32):
    """Custom type ol51nnMFIBModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMFIBModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMFIBModDipNetwork_Object = MibTableColumn
ol51nnMFIBModDipNetwork = _Ol51nnMFIBModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 1, 1, 2),
    _Ol51nnMFIBModDipNetwork_Type()
)
ol51nnMFIBModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFIBModDipNetwork.setStatus("mandatory")


class _Ol51nnMFIBModLLW_Type(Integer32):
    """Custom type ol51nnMFIBModLLW based on Integer32"""
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


_Ol51nnMFIBModLLW_Type.__name__ = "Integer32"
_Ol51nnMFIBModLLW_Object = MibTableColumn
ol51nnMFIBModLLW = _Ol51nnMFIBModLLW_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 1, 1, 3),
    _Ol51nnMFIBModLLW_Type()
)
ol51nnMFIBModLLW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFIBModLLW.setStatus("mandatory")


class _Ol51nnMFIBModDipLLW_Type(Integer32):
    """Custom type ol51nnMFIBModDipLLW based on Integer32"""
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


_Ol51nnMFIBModDipLLW_Type.__name__ = "Integer32"
_Ol51nnMFIBModDipLLW_Object = MibTableColumn
ol51nnMFIBModDipLLW = _Ol51nnMFIBModDipLLW_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 1, 1, 4),
    _Ol51nnMFIBModDipLLW_Type()
)
ol51nnMFIBModDipLLW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFIBModDipLLW.setStatus("mandatory")
_Ol51nnMFIBPortTable_Object = MibTable
ol51nnMFIBPortTable = _Ol51nnMFIBPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 2)
)
if mibBuilder.loadTexts:
    ol51nnMFIBPortTable.setStatus("mandatory")
_Ol51nnMFIBPortEntry_Object = MibTableRow
ol51nnMFIBPortEntry = _Ol51nnMFIBPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 2, 1)
)
ol51nnMFIBPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMFIBPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnMFIBPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFIBPortEntry.setStatus("mandatory")
_Ol51nnMFIBPortSlotIndex_Type = Integer32
_Ol51nnMFIBPortSlotIndex_Object = MibTableColumn
ol51nnMFIBPortSlotIndex = _Ol51nnMFIBPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 2, 1, 1),
    _Ol51nnMFIBPortSlotIndex_Type()
)
ol51nnMFIBPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFIBPortSlotIndex.setStatus("mandatory")
_Ol51nnMFIBPortIndex_Type = Integer32
_Ol51nnMFIBPortIndex_Object = MibTableColumn
ol51nnMFIBPortIndex = _Ol51nnMFIBPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 2, 1, 2),
    _Ol51nnMFIBPortIndex_Type()
)
ol51nnMFIBPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFIBPortIndex.setStatus("mandatory")


class _Ol51nnMFIBPortAdminState_Type(Integer32):
    """Custom type ol51nnMFIBPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMFIBPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMFIBPortAdminState_Object = MibTableColumn
ol51nnMFIBPortAdminState = _Ol51nnMFIBPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 2, 1, 3),
    _Ol51nnMFIBPortAdminState_Type()
)
ol51nnMFIBPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFIBPortAdminState.setStatus("mandatory")
_Ol51nnMFIBPortBuddySlot_Type = Integer32
_Ol51nnMFIBPortBuddySlot_Object = MibTableColumn
ol51nnMFIBPortBuddySlot = _Ol51nnMFIBPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 2, 1, 4),
    _Ol51nnMFIBPortBuddySlot_Type()
)
ol51nnMFIBPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFIBPortBuddySlot.setStatus("mandatory")
_Ol51nnMFIBPortBuddyPort_Type = Integer32
_Ol51nnMFIBPortBuddyPort_Object = MibTableColumn
ol51nnMFIBPortBuddyPort = _Ol51nnMFIBPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 2, 1, 5),
    _Ol51nnMFIBPortBuddyPort_Type()
)
ol51nnMFIBPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFIBPortBuddyPort.setStatus("mandatory")


class _Ol51nnMFIBPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMFIBPortDipAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMFIBPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMFIBPortDipAdminState_Object = MibTableColumn
ol51nnMFIBPortDipAdminState = _Ol51nnMFIBPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5, 2, 1, 6),
    _Ol51nnMFIBPortDipAdminState_Type()
)
ol51nnMFIBPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFIBPortDipAdminState.setStatus("mandatory")
_Ol51nnMUTP_ObjectIdentity = ObjectIdentity
ol51nnMUTP = _Ol51nnMUTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6)
)
_Ol51nnMUTPModTable_Object = MibTable
ol51nnMUTPModTable = _Ol51nnMUTPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 1)
)
if mibBuilder.loadTexts:
    ol51nnMUTPModTable.setStatus("mandatory")
_Ol51nnMUTPModEntry_Object = MibTableRow
ol51nnMUTPModEntry = _Ol51nnMUTPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 1, 1)
)
ol51nnMUTPModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMUTPModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMUTPModEntry.setStatus("mandatory")
_Ol51nnMUTPModSlotIndex_Type = Integer32
_Ol51nnMUTPModSlotIndex_Object = MibTableColumn
ol51nnMUTPModSlotIndex = _Ol51nnMUTPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 1, 1, 1),
    _Ol51nnMUTPModSlotIndex_Type()
)
ol51nnMUTPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMUTPModSlotIndex.setStatus("mandatory")


class _Ol51nnMUTPModDipNetwork_Type(Integer32):
    """Custom type ol51nnMUTPModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMUTPModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMUTPModDipNetwork_Object = MibTableColumn
ol51nnMUTPModDipNetwork = _Ol51nnMUTPModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 1, 1, 2),
    _Ol51nnMUTPModDipNetwork_Type()
)
ol51nnMUTPModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMUTPModDipNetwork.setStatus("mandatory")


class _Ol51nnMUTPModCrossover_Type(Integer32):
    """Custom type ol51nnMUTPModCrossover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crossed", 1),
          ("uncrossed", 2))
    )


_Ol51nnMUTPModCrossover_Type.__name__ = "Integer32"
_Ol51nnMUTPModCrossover_Object = MibTableColumn
ol51nnMUTPModCrossover = _Ol51nnMUTPModCrossover_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 1, 1, 3),
    _Ol51nnMUTPModCrossover_Type()
)
ol51nnMUTPModCrossover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMUTPModCrossover.setStatus("mandatory")


class _Ol51nnMUTPModDipCrossover_Type(Integer32):
    """Custom type ol51nnMUTPModDipCrossover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crossed", 1),
          ("uncrossed", 2))
    )


_Ol51nnMUTPModDipCrossover_Type.__name__ = "Integer32"
_Ol51nnMUTPModDipCrossover_Object = MibTableColumn
ol51nnMUTPModDipCrossover = _Ol51nnMUTPModDipCrossover_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 1, 1, 4),
    _Ol51nnMUTPModDipCrossover_Type()
)
ol51nnMUTPModDipCrossover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMUTPModDipCrossover.setStatus("mandatory")


class _Ol51nnMUTPModFFL_Type(Integer32):
    """Custom type ol51nnMUTPModFFL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eight-bits", 1),
          ("seven-bits", 2))
    )


_Ol51nnMUTPModFFL_Type.__name__ = "Integer32"
_Ol51nnMUTPModFFL_Object = MibTableColumn
ol51nnMUTPModFFL = _Ol51nnMUTPModFFL_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 1, 1, 5),
    _Ol51nnMUTPModFFL_Type()
)
ol51nnMUTPModFFL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMUTPModFFL.setStatus("mandatory")


class _Ol51nnMUTPModDipFFL_Type(Integer32):
    """Custom type ol51nnMUTPModDipFFL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eight-bits", 1),
          ("seven-bits", 2))
    )


_Ol51nnMUTPModDipFFL_Type.__name__ = "Integer32"
_Ol51nnMUTPModDipFFL_Object = MibTableColumn
ol51nnMUTPModDipFFL = _Ol51nnMUTPModDipFFL_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 1, 1, 6),
    _Ol51nnMUTPModDipFFL_Type()
)
ol51nnMUTPModDipFFL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMUTPModDipFFL.setStatus("mandatory")
_Ol51nnMUTPPortTable_Object = MibTable
ol51nnMUTPPortTable = _Ol51nnMUTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2)
)
if mibBuilder.loadTexts:
    ol51nnMUTPPortTable.setStatus("mandatory")
_Ol51nnMUTPPortEntry_Object = MibTableRow
ol51nnMUTPPortEntry = _Ol51nnMUTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1)
)
ol51nnMUTPPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMUTPPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnMUTPPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMUTPPortEntry.setStatus("mandatory")
_Ol51nnMUTPPortSlotIndex_Type = Integer32
_Ol51nnMUTPPortSlotIndex_Object = MibTableColumn
ol51nnMUTPPortSlotIndex = _Ol51nnMUTPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 1),
    _Ol51nnMUTPPortSlotIndex_Type()
)
ol51nnMUTPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMUTPPortSlotIndex.setStatus("mandatory")
_Ol51nnMUTPPortIndex_Type = Integer32
_Ol51nnMUTPPortIndex_Object = MibTableColumn
ol51nnMUTPPortIndex = _Ol51nnMUTPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 2),
    _Ol51nnMUTPPortIndex_Type()
)
ol51nnMUTPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMUTPPortIndex.setStatus("mandatory")


class _Ol51nnMUTPPortAdminState_Type(Integer32):
    """Custom type ol51nnMUTPPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMUTPPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMUTPPortAdminState_Object = MibTableColumn
ol51nnMUTPPortAdminState = _Ol51nnMUTPPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 3),
    _Ol51nnMUTPPortAdminState_Type()
)
ol51nnMUTPPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMUTPPortAdminState.setStatus("mandatory")
_Ol51nnMUTPPortBuddySlot_Type = Integer32
_Ol51nnMUTPPortBuddySlot_Object = MibTableColumn
ol51nnMUTPPortBuddySlot = _Ol51nnMUTPPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 4),
    _Ol51nnMUTPPortBuddySlot_Type()
)
ol51nnMUTPPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMUTPPortBuddySlot.setStatus("mandatory")
_Ol51nnMUTPPortBuddyPort_Type = Integer32
_Ol51nnMUTPPortBuddyPort_Object = MibTableColumn
ol51nnMUTPPortBuddyPort = _Ol51nnMUTPPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 5),
    _Ol51nnMUTPPortBuddyPort_Type()
)
ol51nnMUTPPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMUTPPortBuddyPort.setStatus("mandatory")


class _Ol51nnMUTPPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMUTPPortDipAdminState based on Integer32"""
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


_Ol51nnMUTPPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMUTPPortDipAdminState_Object = MibTableColumn
ol51nnMUTPPortDipAdminState = _Ol51nnMUTPPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 6),
    _Ol51nnMUTPPortDipAdminState_Type()
)
ol51nnMUTPPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMUTPPortDipAdminState.setStatus("mandatory")


class _Ol51nnMUTPPortLinkInteg_Type(Integer32):
    """Custom type ol51nnMUTPPortLinkInteg based on Integer32"""
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


_Ol51nnMUTPPortLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMUTPPortLinkInteg_Object = MibTableColumn
ol51nnMUTPPortLinkInteg = _Ol51nnMUTPPortLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 7),
    _Ol51nnMUTPPortLinkInteg_Type()
)
ol51nnMUTPPortLinkInteg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMUTPPortLinkInteg.setStatus("mandatory")


class _Ol51nnMUTPPortDipLinkInteg_Type(Integer32):
    """Custom type ol51nnMUTPPortDipLinkInteg based on Integer32"""
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


_Ol51nnMUTPPortDipLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMUTPPortDipLinkInteg_Object = MibTableColumn
ol51nnMUTPPortDipLinkInteg = _Ol51nnMUTPPortDipLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 8),
    _Ol51nnMUTPPortDipLinkInteg_Type()
)
ol51nnMUTPPortDipLinkInteg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMUTPPortDipLinkInteg.setStatus("mandatory")


class _Ol51nnMUTPPortSquelch_Type(Integer32):
    """Custom type ol51nnMUTPPortSquelch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1))
    )


_Ol51nnMUTPPortSquelch_Type.__name__ = "Integer32"
_Ol51nnMUTPPortSquelch_Object = MibTableColumn
ol51nnMUTPPortSquelch = _Ol51nnMUTPPortSquelch_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 9),
    _Ol51nnMUTPPortSquelch_Type()
)
ol51nnMUTPPortSquelch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMUTPPortSquelch.setStatus("mandatory")


class _Ol51nnMUTPPortDipSquelch_Type(Integer32):
    """Custom type ol51nnMUTPPortDipSquelch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1))
    )


_Ol51nnMUTPPortDipSquelch_Type.__name__ = "Integer32"
_Ol51nnMUTPPortDipSquelch_Object = MibTableColumn
ol51nnMUTPPortDipSquelch = _Ol51nnMUTPPortDipSquelch_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6, 2, 1, 10),
    _Ol51nnMUTPPortDipSquelch_Type()
)
ol51nnMUTPPortDipSquelch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMUTPPortDipSquelch.setStatus("mandatory")
_Ol51nnMTP_ObjectIdentity = ObjectIdentity
ol51nnMTP = _Ol51nnMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7)
)
_Ol51nnMTPModTable_Object = MibTable
ol51nnMTPModTable = _Ol51nnMTPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 1)
)
if mibBuilder.loadTexts:
    ol51nnMTPModTable.setStatus("mandatory")
_Ol51nnMTPModEntry_Object = MibTableRow
ol51nnMTPModEntry = _Ol51nnMTPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 1, 1)
)
ol51nnMTPModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMTPModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPModEntry.setStatus("mandatory")
_Ol51nnMTPModSlotIndex_Type = Integer32
_Ol51nnMTPModSlotIndex_Object = MibTableColumn
ol51nnMTPModSlotIndex = _Ol51nnMTPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 1, 1, 1),
    _Ol51nnMTPModSlotIndex_Type()
)
ol51nnMTPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPModSlotIndex.setStatus("mandatory")


class _Ol51nnMTPModDipNetwork_Type(Integer32):
    """Custom type ol51nnMTPModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMTPModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMTPModDipNetwork_Object = MibTableColumn
ol51nnMTPModDipNetwork = _Ol51nnMTPModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 1, 1, 2),
    _Ol51nnMTPModDipNetwork_Type()
)
ol51nnMTPModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPModDipNetwork.setStatus("mandatory")


class _Ol51nnMTPModCrossover_Type(Integer32):
    """Custom type ol51nnMTPModCrossover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crossed", 1),
          ("uncrossed", 2))
    )


_Ol51nnMTPModCrossover_Type.__name__ = "Integer32"
_Ol51nnMTPModCrossover_Object = MibTableColumn
ol51nnMTPModCrossover = _Ol51nnMTPModCrossover_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 1, 1, 3),
    _Ol51nnMTPModCrossover_Type()
)
ol51nnMTPModCrossover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPModCrossover.setStatus("mandatory")


class _Ol51nnMTPModDipCrossover_Type(Integer32):
    """Custom type ol51nnMTPModDipCrossover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crossed", 1),
          ("uncrossed", 2))
    )


_Ol51nnMTPModDipCrossover_Type.__name__ = "Integer32"
_Ol51nnMTPModDipCrossover_Object = MibTableColumn
ol51nnMTPModDipCrossover = _Ol51nnMTPModDipCrossover_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 1, 1, 4),
    _Ol51nnMTPModDipCrossover_Type()
)
ol51nnMTPModDipCrossover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPModDipCrossover.setStatus("mandatory")
_Ol51nnMTPPortTable_Object = MibTable
ol51nnMTPPortTable = _Ol51nnMTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2)
)
if mibBuilder.loadTexts:
    ol51nnMTPPortTable.setStatus("mandatory")
_Ol51nnMTPPortEntry_Object = MibTableRow
ol51nnMTPPortEntry = _Ol51nnMTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1)
)
ol51nnMTPPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMTPPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnMTPPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPPortEntry.setStatus("mandatory")
_Ol51nnMTPPortSlotIndex_Type = Integer32
_Ol51nnMTPPortSlotIndex_Object = MibTableColumn
ol51nnMTPPortSlotIndex = _Ol51nnMTPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 1),
    _Ol51nnMTPPortSlotIndex_Type()
)
ol51nnMTPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPortSlotIndex.setStatus("mandatory")
_Ol51nnMTPPortIndex_Type = Integer32
_Ol51nnMTPPortIndex_Object = MibTableColumn
ol51nnMTPPortIndex = _Ol51nnMTPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 2),
    _Ol51nnMTPPortIndex_Type()
)
ol51nnMTPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPortIndex.setStatus("mandatory")


class _Ol51nnMTPPortAdminState_Type(Integer32):
    """Custom type ol51nnMTPPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMTPPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPPortAdminState_Object = MibTableColumn
ol51nnMTPPortAdminState = _Ol51nnMTPPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 3),
    _Ol51nnMTPPortAdminState_Type()
)
ol51nnMTPPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPortAdminState.setStatus("mandatory")
_Ol51nnMTPPortBuddySlot_Type = Integer32
_Ol51nnMTPPortBuddySlot_Object = MibTableColumn
ol51nnMTPPortBuddySlot = _Ol51nnMTPPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 4),
    _Ol51nnMTPPortBuddySlot_Type()
)
ol51nnMTPPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPortBuddySlot.setStatus("mandatory")
_Ol51nnMTPPortBuddyPort_Type = Integer32
_Ol51nnMTPPortBuddyPort_Object = MibTableColumn
ol51nnMTPPortBuddyPort = _Ol51nnMTPPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 5),
    _Ol51nnMTPPortBuddyPort_Type()
)
ol51nnMTPPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPortBuddyPort.setStatus("mandatory")


class _Ol51nnMTPPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMTPPortDipAdminState based on Integer32"""
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


_Ol51nnMTPPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPPortDipAdminState_Object = MibTableColumn
ol51nnMTPPortDipAdminState = _Ol51nnMTPPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 6),
    _Ol51nnMTPPortDipAdminState_Type()
)
ol51nnMTPPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPortDipAdminState.setStatus("mandatory")


class _Ol51nnMTPPortLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPPortLinkInteg based on Integer32"""
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


_Ol51nnMTPPortLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPPortLinkInteg_Object = MibTableColumn
ol51nnMTPPortLinkInteg = _Ol51nnMTPPortLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 7),
    _Ol51nnMTPPortLinkInteg_Type()
)
ol51nnMTPPortLinkInteg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPortLinkInteg.setStatus("mandatory")


class _Ol51nnMTPPortDipLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPPortDipLinkInteg based on Integer32"""
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


_Ol51nnMTPPortDipLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPPortDipLinkInteg_Object = MibTableColumn
ol51nnMTPPortDipLinkInteg = _Ol51nnMTPPortDipLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 8),
    _Ol51nnMTPPortDipLinkInteg_Type()
)
ol51nnMTPPortDipLinkInteg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPortDipLinkInteg.setStatus("mandatory")


class _Ol51nnMTPPortSquelch_Type(Integer32):
    """Custom type ol51nnMTPPortSquelch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1))
    )


_Ol51nnMTPPortSquelch_Type.__name__ = "Integer32"
_Ol51nnMTPPortSquelch_Object = MibTableColumn
ol51nnMTPPortSquelch = _Ol51nnMTPPortSquelch_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 9),
    _Ol51nnMTPPortSquelch_Type()
)
ol51nnMTPPortSquelch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPortSquelch.setStatus("mandatory")


class _Ol51nnMTPPortDipSquelch_Type(Integer32):
    """Custom type ol51nnMTPPortDipSquelch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1))
    )


_Ol51nnMTPPortDipSquelch_Type.__name__ = "Integer32"
_Ol51nnMTPPortDipSquelch_Object = MibTableColumn
ol51nnMTPPortDipSquelch = _Ol51nnMTPPortDipSquelch_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7, 2, 1, 10),
    _Ol51nnMTPPortDipSquelch_Type()
)
ol51nnMTPPortDipSquelch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPortDipSquelch.setStatus("mandatory")
_Ol51nnMBNC_ObjectIdentity = ObjectIdentity
ol51nnMBNC = _Ol51nnMBNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8)
)
_Ol51nnMBNCModTable_Object = MibTable
ol51nnMBNCModTable = _Ol51nnMBNCModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 1)
)
if mibBuilder.loadTexts:
    ol51nnMBNCModTable.setStatus("mandatory")
_Ol51nnMBNCModEntry_Object = MibTableRow
ol51nnMBNCModEntry = _Ol51nnMBNCModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 1, 1)
)
ol51nnMBNCModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMBNCModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMBNCModEntry.setStatus("mandatory")
_Ol51nnMBNCModSlotIndex_Type = Integer32
_Ol51nnMBNCModSlotIndex_Object = MibTableColumn
ol51nnMBNCModSlotIndex = _Ol51nnMBNCModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 1, 1, 1),
    _Ol51nnMBNCModSlotIndex_Type()
)
ol51nnMBNCModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMBNCModSlotIndex.setStatus("mandatory")


class _Ol51nnMBNCModDipNetwork_Type(Integer32):
    """Custom type ol51nnMBNCModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMBNCModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMBNCModDipNetwork_Object = MibTableColumn
ol51nnMBNCModDipNetwork = _Ol51nnMBNCModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 1, 1, 2),
    _Ol51nnMBNCModDipNetwork_Type()
)
ol51nnMBNCModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMBNCModDipNetwork.setStatus("mandatory")
_Ol51nnMBNCPortTable_Object = MibTable
ol51nnMBNCPortTable = _Ol51nnMBNCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 2)
)
if mibBuilder.loadTexts:
    ol51nnMBNCPortTable.setStatus("mandatory")
_Ol51nnMBNCPortEntry_Object = MibTableRow
ol51nnMBNCPortEntry = _Ol51nnMBNCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 2, 1)
)
ol51nnMBNCPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMBNCPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnMBNCPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMBNCPortEntry.setStatus("mandatory")
_Ol51nnMBNCPortSlotIndex_Type = Integer32
_Ol51nnMBNCPortSlotIndex_Object = MibTableColumn
ol51nnMBNCPortSlotIndex = _Ol51nnMBNCPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 2, 1, 1),
    _Ol51nnMBNCPortSlotIndex_Type()
)
ol51nnMBNCPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMBNCPortSlotIndex.setStatus("mandatory")
_Ol51nnMBNCPortIndex_Type = Integer32
_Ol51nnMBNCPortIndex_Object = MibTableColumn
ol51nnMBNCPortIndex = _Ol51nnMBNCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 2, 1, 2),
    _Ol51nnMBNCPortIndex_Type()
)
ol51nnMBNCPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMBNCPortIndex.setStatus("mandatory")


class _Ol51nnMBNCPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMBNCPortDipAdminState based on Integer32"""
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


_Ol51nnMBNCPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMBNCPortDipAdminState_Object = MibTableColumn
ol51nnMBNCPortDipAdminState = _Ol51nnMBNCPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 2, 1, 3),
    _Ol51nnMBNCPortDipAdminState_Type()
)
ol51nnMBNCPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMBNCPortDipAdminState.setStatus("mandatory")


class _Ol51nnMBNCPortDipTermination_Type(Integer32):
    """Custom type ol51nnMBNCPortDipTermination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-terminated", 2),
          ("terminated", 1))
    )


_Ol51nnMBNCPortDipTermination_Type.__name__ = "Integer32"
_Ol51nnMBNCPortDipTermination_Object = MibTableColumn
ol51nnMBNCPortDipTermination = _Ol51nnMBNCPortDipTermination_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 2, 1, 4),
    _Ol51nnMBNCPortDipTermination_Type()
)
ol51nnMBNCPortDipTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMBNCPortDipTermination.setStatus("mandatory")


class _Ol51nnMBNCPortDipGround_Type(Integer32):
    """Custom type ol51nnMBNCPortDipGround based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("grounded", 1),
          ("not-grounded", 2))
    )


_Ol51nnMBNCPortDipGround_Type.__name__ = "Integer32"
_Ol51nnMBNCPortDipGround_Object = MibTableColumn
ol51nnMBNCPortDipGround = _Ol51nnMBNCPortDipGround_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8, 2, 1, 5),
    _Ol51nnMBNCPortDipGround_Type()
)
ol51nnMBNCPortDipGround.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMBNCPortDipGround.setStatus("mandatory")
_Ol51nnBEE_ObjectIdentity = ObjectIdentity
ol51nnBEE = _Ol51nnBEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9)
)
_Ol51nnBEEModTable_Object = MibTable
ol51nnBEEModTable = _Ol51nnBEEModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 1)
)
if mibBuilder.loadTexts:
    ol51nnBEEModTable.setStatus("mandatory")
_Ol51nnBEEModEntry_Object = MibTableRow
ol51nnBEEModEntry = _Ol51nnBEEModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 1, 1)
)
ol51nnBEEModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnBEEModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnBEEModEntry.setStatus("mandatory")
_Ol51nnBEEModSlotIndex_Type = Integer32
_Ol51nnBEEModSlotIndex_Object = MibTableColumn
ol51nnBEEModSlotIndex = _Ol51nnBEEModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 1, 1, 1),
    _Ol51nnBEEModSlotIndex_Type()
)
ol51nnBEEModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnBEEModSlotIndex.setStatus("mandatory")


class _Ol51nnBEEModStationAddr_Type(OctetString):
    """Custom type ol51nnBEEModStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol51nnBEEModStationAddr_Type.__name__ = "OctetString"
_Ol51nnBEEModStationAddr_Object = MibTableColumn
ol51nnBEEModStationAddr = _Ol51nnBEEModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 1, 1, 2),
    _Ol51nnBEEModStationAddr_Type()
)
ol51nnBEEModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnBEEModStationAddr.setStatus("mandatory")
_Ol51nnBEEModProtocols_Type = DisplayString
_Ol51nnBEEModProtocols_Object = MibTableColumn
ol51nnBEEModProtocols = _Ol51nnBEEModProtocols_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 1, 1, 3),
    _Ol51nnBEEModProtocols_Type()
)
ol51nnBEEModProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnBEEModProtocols.setStatus("mandatory")
_Ol51nnBEEPortTable_Object = MibTable
ol51nnBEEPortTable = _Ol51nnBEEPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 2)
)
if mibBuilder.loadTexts:
    ol51nnBEEPortTable.setStatus("mandatory")
_Ol51nnBEEPortEntry_Object = MibTableRow
ol51nnBEEPortEntry = _Ol51nnBEEPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 2, 1)
)
ol51nnBEEPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnBEEPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnBEEPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnBEEPortEntry.setStatus("mandatory")
_Ol51nnBEEPortSlotIndex_Type = Integer32
_Ol51nnBEEPortSlotIndex_Object = MibTableColumn
ol51nnBEEPortSlotIndex = _Ol51nnBEEPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 2, 1, 1),
    _Ol51nnBEEPortSlotIndex_Type()
)
ol51nnBEEPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnBEEPortSlotIndex.setStatus("mandatory")
_Ol51nnBEEPortIndex_Type = Integer32
_Ol51nnBEEPortIndex_Object = MibTableColumn
ol51nnBEEPortIndex = _Ol51nnBEEPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 2, 1, 2),
    _Ol51nnBEEPortIndex_Type()
)
ol51nnBEEPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnBEEPortIndex.setStatus("mandatory")
_Ol51nnBEEPortIpAddress_Type = IpAddress
_Ol51nnBEEPortIpAddress_Object = MibTableColumn
ol51nnBEEPortIpAddress = _Ol51nnBEEPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 2, 1, 3),
    _Ol51nnBEEPortIpAddress_Type()
)
ol51nnBEEPortIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnBEEPortIpAddress.setStatus("mandatory")


class _Ol51nnBEEPortDipNetwork_Type(Integer32):
    """Custom type ol51nnBEEPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("front-panel", 5),
          ("isolated", 2))
    )


_Ol51nnBEEPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnBEEPortDipNetwork_Object = MibTableColumn
ol51nnBEEPortDipNetwork = _Ol51nnBEEPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 2, 1, 4),
    _Ol51nnBEEPortDipNetwork_Type()
)
ol51nnBEEPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnBEEPortDipNetwork.setStatus("mandatory")


class _Ol51nnBEEPortDefNetwork_Type(Integer32):
    """Custom type ol51nnBEEPortDefNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("front-panel", 5),
          ("isolated", 2))
    )


_Ol51nnBEEPortDefNetwork_Type.__name__ = "Integer32"
_Ol51nnBEEPortDefNetwork_Object = MibTableColumn
ol51nnBEEPortDefNetwork = _Ol51nnBEEPortDefNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9, 2, 1, 5),
    _Ol51nnBEEPortDefNetwork_Type()
)
ol51nnBEEPortDefNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnBEEPortDefNetwork.setStatus("mandatory")
_Ol51nnRES_ObjectIdentity = ObjectIdentity
ol51nnRES = _Ol51nnRES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10)
)
_Ol51nnRESModTable_Object = MibTable
ol51nnRESModTable = _Ol51nnRESModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 1)
)
if mibBuilder.loadTexts:
    ol51nnRESModTable.setStatus("mandatory")
_Ol51nnRESModEntry_Object = MibTableRow
ol51nnRESModEntry = _Ol51nnRESModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 1, 1)
)
ol51nnRESModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnRESModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnRESModEntry.setStatus("mandatory")
_Ol51nnRESModSlotIndex_Type = Integer32
_Ol51nnRESModSlotIndex_Object = MibTableColumn
ol51nnRESModSlotIndex = _Ol51nnRESModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 1, 1, 1),
    _Ol51nnRESModSlotIndex_Type()
)
ol51nnRESModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnRESModSlotIndex.setStatus("mandatory")


class _Ol51nnRESModStationAddr_Type(OctetString):
    """Custom type ol51nnRESModStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol51nnRESModStationAddr_Type.__name__ = "OctetString"
_Ol51nnRESModStationAddr_Object = MibTableColumn
ol51nnRESModStationAddr = _Ol51nnRESModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 1, 1, 2),
    _Ol51nnRESModStationAddr_Type()
)
ol51nnRESModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnRESModStationAddr.setStatus("mandatory")
_Ol51nnRESModProtocols_Type = DisplayString
_Ol51nnRESModProtocols_Object = MibTableColumn
ol51nnRESModProtocols = _Ol51nnRESModProtocols_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 1, 1, 3),
    _Ol51nnRESModProtocols_Type()
)
ol51nnRESModProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnRESModProtocols.setStatus("mandatory")
_Ol51nnRESPortTable_Object = MibTable
ol51nnRESPortTable = _Ol51nnRESPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 2)
)
if mibBuilder.loadTexts:
    ol51nnRESPortTable.setStatus("mandatory")
_Ol51nnRESPortEntry_Object = MibTableRow
ol51nnRESPortEntry = _Ol51nnRESPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 2, 1)
)
ol51nnRESPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnRESPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnRESPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnRESPortEntry.setStatus("mandatory")
_Ol51nnRESPortSlotIndex_Type = Integer32
_Ol51nnRESPortSlotIndex_Object = MibTableColumn
ol51nnRESPortSlotIndex = _Ol51nnRESPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 2, 1, 1),
    _Ol51nnRESPortSlotIndex_Type()
)
ol51nnRESPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnRESPortSlotIndex.setStatus("mandatory")
_Ol51nnRESPortIndex_Type = Integer32
_Ol51nnRESPortIndex_Object = MibTableColumn
ol51nnRESPortIndex = _Ol51nnRESPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 2, 1, 2),
    _Ol51nnRESPortIndex_Type()
)
ol51nnRESPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnRESPortIndex.setStatus("mandatory")
_Ol51nnRESPortIpAddress_Type = IpAddress
_Ol51nnRESPortIpAddress_Object = MibTableColumn
ol51nnRESPortIpAddress = _Ol51nnRESPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 2, 1, 3),
    _Ol51nnRESPortIpAddress_Type()
)
ol51nnRESPortIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnRESPortIpAddress.setStatus("mandatory")


class _Ol51nnRESPortDipNetwork_Type(Integer32):
    """Custom type ol51nnRESPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("front-panel", 5),
          ("isolated", 2))
    )


_Ol51nnRESPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnRESPortDipNetwork_Object = MibTableColumn
ol51nnRESPortDipNetwork = _Ol51nnRESPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 2, 1, 4),
    _Ol51nnRESPortDipNetwork_Type()
)
ol51nnRESPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnRESPortDipNetwork.setStatus("mandatory")


class _Ol51nnRESPortDefNetwork_Type(Integer32):
    """Custom type ol51nnRESPortDefNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("front-panel", 5),
          ("isolated", 2))
    )


_Ol51nnRESPortDefNetwork_Type.__name__ = "Integer32"
_Ol51nnRESPortDefNetwork_Object = MibTableColumn
ol51nnRESPortDefNetwork = _Ol51nnRESPortDefNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10, 2, 1, 5),
    _Ol51nnRESPortDefNetwork_Type()
)
ol51nnRESPortDefNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnRESPortDefNetwork.setStatus("mandatory")
_Ol51nnREE_ObjectIdentity = ObjectIdentity
ol51nnREE = _Ol51nnREE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11)
)
_Ol51nnREEModTable_Object = MibTable
ol51nnREEModTable = _Ol51nnREEModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 1)
)
if mibBuilder.loadTexts:
    ol51nnREEModTable.setStatus("mandatory")
_Ol51nnREEModEntry_Object = MibTableRow
ol51nnREEModEntry = _Ol51nnREEModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 1, 1)
)
ol51nnREEModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnREEModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnREEModEntry.setStatus("mandatory")
_Ol51nnREEModSlotIndex_Type = Integer32
_Ol51nnREEModSlotIndex_Object = MibTableColumn
ol51nnREEModSlotIndex = _Ol51nnREEModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 1, 1, 1),
    _Ol51nnREEModSlotIndex_Type()
)
ol51nnREEModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnREEModSlotIndex.setStatus("mandatory")


class _Ol51nnREEModStationAddr_Type(OctetString):
    """Custom type ol51nnREEModStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol51nnREEModStationAddr_Type.__name__ = "OctetString"
_Ol51nnREEModStationAddr_Object = MibTableColumn
ol51nnREEModStationAddr = _Ol51nnREEModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 1, 1, 2),
    _Ol51nnREEModStationAddr_Type()
)
ol51nnREEModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnREEModStationAddr.setStatus("mandatory")
_Ol51nnREEModProtocols_Type = DisplayString
_Ol51nnREEModProtocols_Object = MibTableColumn
ol51nnREEModProtocols = _Ol51nnREEModProtocols_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 1, 1, 3),
    _Ol51nnREEModProtocols_Type()
)
ol51nnREEModProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnREEModProtocols.setStatus("mandatory")
_Ol51nnREEPortTable_Object = MibTable
ol51nnREEPortTable = _Ol51nnREEPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 2)
)
if mibBuilder.loadTexts:
    ol51nnREEPortTable.setStatus("mandatory")
_Ol51nnREEPortEntry_Object = MibTableRow
ol51nnREEPortEntry = _Ol51nnREEPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 2, 1)
)
ol51nnREEPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnREEPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnREEPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnREEPortEntry.setStatus("mandatory")
_Ol51nnREEPortSlotIndex_Type = Integer32
_Ol51nnREEPortSlotIndex_Object = MibTableColumn
ol51nnREEPortSlotIndex = _Ol51nnREEPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 2, 1, 1),
    _Ol51nnREEPortSlotIndex_Type()
)
ol51nnREEPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnREEPortSlotIndex.setStatus("mandatory")
_Ol51nnREEPortIndex_Type = Integer32
_Ol51nnREEPortIndex_Object = MibTableColumn
ol51nnREEPortIndex = _Ol51nnREEPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 2, 1, 2),
    _Ol51nnREEPortIndex_Type()
)
ol51nnREEPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnREEPortIndex.setStatus("mandatory")
_Ol51nnREEPortIpAddress_Type = IpAddress
_Ol51nnREEPortIpAddress_Object = MibTableColumn
ol51nnREEPortIpAddress = _Ol51nnREEPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 2, 1, 3),
    _Ol51nnREEPortIpAddress_Type()
)
ol51nnREEPortIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnREEPortIpAddress.setStatus("mandatory")


class _Ol51nnREEPortDipNetwork_Type(Integer32):
    """Custom type ol51nnREEPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("front-panel", 5),
          ("isolated", 2))
    )


_Ol51nnREEPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnREEPortDipNetwork_Object = MibTableColumn
ol51nnREEPortDipNetwork = _Ol51nnREEPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 2, 1, 4),
    _Ol51nnREEPortDipNetwork_Type()
)
ol51nnREEPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnREEPortDipNetwork.setStatus("mandatory")


class _Ol51nnREEPortDefNetwork_Type(Integer32):
    """Custom type ol51nnREEPortDefNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("front-panel", 5),
          ("isolated", 2))
    )


_Ol51nnREEPortDefNetwork_Type.__name__ = "Integer32"
_Ol51nnREEPortDefNetwork_Object = MibTableColumn
ol51nnREEPortDefNetwork = _Ol51nnREEPortDefNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11, 2, 1, 5),
    _Ol51nnREEPortDefNetwork_Type()
)
ol51nnREEPortDefNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnREEPortDefNetwork.setStatus("mandatory")
_Ol51nnMAUIF_ObjectIdentity = ObjectIdentity
ol51nnMAUIF = _Ol51nnMAUIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12)
)
_Ol51nnMAUIFModTable_Object = MibTable
ol51nnMAUIFModTable = _Ol51nnMAUIFModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 1)
)
if mibBuilder.loadTexts:
    ol51nnMAUIFModTable.setStatus("mandatory")
_Ol51nnMAUIFModEntry_Object = MibTableRow
ol51nnMAUIFModEntry = _Ol51nnMAUIFModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 1, 1)
)
ol51nnMAUIFModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMAUIFModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMAUIFModEntry.setStatus("mandatory")
_Ol51nnMAUIFModSlotIndex_Type = Integer32
_Ol51nnMAUIFModSlotIndex_Object = MibTableColumn
ol51nnMAUIFModSlotIndex = _Ol51nnMAUIFModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 1, 1, 1),
    _Ol51nnMAUIFModSlotIndex_Type()
)
ol51nnMAUIFModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIFModSlotIndex.setStatus("mandatory")
_Ol51nnMAUIFPortTable_Object = MibTable
ol51nnMAUIFPortTable = _Ol51nnMAUIFPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2)
)
if mibBuilder.loadTexts:
    ol51nnMAUIFPortTable.setStatus("mandatory")
_Ol51nnMAUIFPortEntry_Object = MibTableRow
ol51nnMAUIFPortEntry = _Ol51nnMAUIFPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2, 1)
)
ol51nnMAUIFPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMAUIFPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnMAUIFPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMAUIFPortEntry.setStatus("mandatory")
_Ol51nnMAUIFPortSlotIndex_Type = Integer32
_Ol51nnMAUIFPortSlotIndex_Object = MibTableColumn
ol51nnMAUIFPortSlotIndex = _Ol51nnMAUIFPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2, 1, 1),
    _Ol51nnMAUIFPortSlotIndex_Type()
)
ol51nnMAUIFPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIFPortSlotIndex.setStatus("mandatory")
_Ol51nnMAUIFPortIndex_Type = Integer32
_Ol51nnMAUIFPortIndex_Object = MibTableColumn
ol51nnMAUIFPortIndex = _Ol51nnMAUIFPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2, 1, 2),
    _Ol51nnMAUIFPortIndex_Type()
)
ol51nnMAUIFPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIFPortIndex.setStatus("mandatory")


class _Ol51nnMAUIFPortAdminState_Type(Integer32):
    """Custom type ol51nnMAUIFPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMAUIFPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMAUIFPortAdminState_Object = MibTableColumn
ol51nnMAUIFPortAdminState = _Ol51nnMAUIFPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2, 1, 3),
    _Ol51nnMAUIFPortAdminState_Type()
)
ol51nnMAUIFPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIFPortAdminState.setStatus("mandatory")
_Ol51nnMAUIFPortBuddySlot_Type = Integer32
_Ol51nnMAUIFPortBuddySlot_Object = MibTableColumn
ol51nnMAUIFPortBuddySlot = _Ol51nnMAUIFPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2, 1, 4),
    _Ol51nnMAUIFPortBuddySlot_Type()
)
ol51nnMAUIFPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIFPortBuddySlot.setStatus("mandatory")
_Ol51nnMAUIFPortBuddyPort_Type = Integer32
_Ol51nnMAUIFPortBuddyPort_Object = MibTableColumn
ol51nnMAUIFPortBuddyPort = _Ol51nnMAUIFPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2, 1, 5),
    _Ol51nnMAUIFPortBuddyPort_Type()
)
ol51nnMAUIFPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIFPortBuddyPort.setStatus("mandatory")


class _Ol51nnMAUIFPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMAUIFPortDipAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMAUIFPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMAUIFPortDipAdminState_Object = MibTableColumn
ol51nnMAUIFPortDipAdminState = _Ol51nnMAUIFPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2, 1, 6),
    _Ol51nnMAUIFPortDipAdminState_Type()
)
ol51nnMAUIFPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIFPortDipAdminState.setStatus("mandatory")


class _Ol51nnMAUIFPortDipNetwork_Type(Integer32):
    """Custom type ol51nnMAUIFPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMAUIFPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMAUIFPortDipNetwork_Object = MibTableColumn
ol51nnMAUIFPortDipNetwork = _Ol51nnMAUIFPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12, 2, 1, 7),
    _Ol51nnMAUIFPortDipNetwork_Type()
)
ol51nnMAUIFPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIFPortDipNetwork.setStatus("mandatory")
_Ol51nnMAUIM_ObjectIdentity = ObjectIdentity
ol51nnMAUIM = _Ol51nnMAUIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13)
)
_Ol51nnMAUIMModTable_Object = MibTable
ol51nnMAUIMModTable = _Ol51nnMAUIMModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 1)
)
if mibBuilder.loadTexts:
    ol51nnMAUIMModTable.setStatus("mandatory")
_Ol51nnMAUIMModEntry_Object = MibTableRow
ol51nnMAUIMModEntry = _Ol51nnMAUIMModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 1, 1)
)
ol51nnMAUIMModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMAUIMModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMAUIMModEntry.setStatus("mandatory")
_Ol51nnMAUIMModSlotIndex_Type = Integer32
_Ol51nnMAUIMModSlotIndex_Object = MibTableColumn
ol51nnMAUIMModSlotIndex = _Ol51nnMAUIMModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 1, 1, 1),
    _Ol51nnMAUIMModSlotIndex_Type()
)
ol51nnMAUIMModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIMModSlotIndex.setStatus("mandatory")
_Ol51nnMAUIMPortTable_Object = MibTable
ol51nnMAUIMPortTable = _Ol51nnMAUIMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2)
)
if mibBuilder.loadTexts:
    ol51nnMAUIMPortTable.setStatus("mandatory")
_Ol51nnMAUIMPortEntry_Object = MibTableRow
ol51nnMAUIMPortEntry = _Ol51nnMAUIMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1)
)
ol51nnMAUIMPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMAUIMPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnMAUIMPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMAUIMPortEntry.setStatus("mandatory")
_Ol51nnMAUIMPortSlotIndex_Type = Integer32
_Ol51nnMAUIMPortSlotIndex_Object = MibTableColumn
ol51nnMAUIMPortSlotIndex = _Ol51nnMAUIMPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 1),
    _Ol51nnMAUIMPortSlotIndex_Type()
)
ol51nnMAUIMPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortSlotIndex.setStatus("mandatory")
_Ol51nnMAUIMPortIndex_Type = Integer32
_Ol51nnMAUIMPortIndex_Object = MibTableColumn
ol51nnMAUIMPortIndex = _Ol51nnMAUIMPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 2),
    _Ol51nnMAUIMPortIndex_Type()
)
ol51nnMAUIMPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortIndex.setStatus("mandatory")


class _Ol51nnMAUIMPortAdminState_Type(Integer32):
    """Custom type ol51nnMAUIMPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMAUIMPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortAdminState_Object = MibTableColumn
ol51nnMAUIMPortAdminState = _Ol51nnMAUIMPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 3),
    _Ol51nnMAUIMPortAdminState_Type()
)
ol51nnMAUIMPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortAdminState.setStatus("mandatory")
_Ol51nnMAUIMPortBuddySlot_Type = Integer32
_Ol51nnMAUIMPortBuddySlot_Object = MibTableColumn
ol51nnMAUIMPortBuddySlot = _Ol51nnMAUIMPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 4),
    _Ol51nnMAUIMPortBuddySlot_Type()
)
ol51nnMAUIMPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortBuddySlot.setStatus("mandatory")
_Ol51nnMAUIMPortBuddyPort_Type = Integer32
_Ol51nnMAUIMPortBuddyPort_Object = MibTableColumn
ol51nnMAUIMPortBuddyPort = _Ol51nnMAUIMPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 5),
    _Ol51nnMAUIMPortBuddyPort_Type()
)
ol51nnMAUIMPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortBuddyPort.setStatus("mandatory")


class _Ol51nnMAUIMPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMAUIMPortDipAdminState based on Integer32"""
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


_Ol51nnMAUIMPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortDipAdminState_Object = MibTableColumn
ol51nnMAUIMPortDipAdminState = _Ol51nnMAUIMPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 6),
    _Ol51nnMAUIMPortDipAdminState_Type()
)
ol51nnMAUIMPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortDipAdminState.setStatus("mandatory")


class _Ol51nnMAUIMPortDipNetwork_Type(Integer32):
    """Custom type ol51nnMAUIMPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMAUIMPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortDipNetwork_Object = MibTableColumn
ol51nnMAUIMPortDipNetwork = _Ol51nnMAUIMPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 7),
    _Ol51nnMAUIMPortDipNetwork_Type()
)
ol51nnMAUIMPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortDipNetwork.setStatus("mandatory")


class _Ol51nnMAUIMPortSQETest_Type(Integer32):
    """Custom type ol51nnMAUIMPortSQETest based on Integer32"""
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


_Ol51nnMAUIMPortSQETest_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortSQETest_Object = MibTableColumn
ol51nnMAUIMPortSQETest = _Ol51nnMAUIMPortSQETest_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 8),
    _Ol51nnMAUIMPortSQETest_Type()
)
ol51nnMAUIMPortSQETest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortSQETest.setStatus("mandatory")


class _Ol51nnMAUIMPortDipSQETest_Type(Integer32):
    """Custom type ol51nnMAUIMPortDipSQETest based on Integer32"""
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


_Ol51nnMAUIMPortDipSQETest_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortDipSQETest_Object = MibTableColumn
ol51nnMAUIMPortDipSQETest = _Ol51nnMAUIMPortDipSQETest_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 9),
    _Ol51nnMAUIMPortDipSQETest_Type()
)
ol51nnMAUIMPortDipSQETest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortDipSQETest.setStatus("mandatory")


class _Ol51nnMAUIMPortCollision_Type(Integer32):
    """Custom type ol51nnMAUIMPortCollision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("normal", 1))
    )


_Ol51nnMAUIMPortCollision_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortCollision_Object = MibTableColumn
ol51nnMAUIMPortCollision = _Ol51nnMAUIMPortCollision_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 10),
    _Ol51nnMAUIMPortCollision_Type()
)
ol51nnMAUIMPortCollision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortCollision.setStatus("mandatory")


class _Ol51nnMAUIMPortDipCollision_Type(Integer32):
    """Custom type ol51nnMAUIMPortDipCollision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("normal", 1))
    )


_Ol51nnMAUIMPortDipCollision_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortDipCollision_Object = MibTableColumn
ol51nnMAUIMPortDipCollision = _Ol51nnMAUIMPortDipCollision_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 11),
    _Ol51nnMAUIMPortDipCollision_Type()
)
ol51nnMAUIMPortDipCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortDipCollision.setStatus("mandatory")


class _Ol51nnMAUIMPortHalfStep_Type(Integer32):
    """Custom type ol51nnMAUIMPortHalfStep based on Integer32"""
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


_Ol51nnMAUIMPortHalfStep_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortHalfStep_Object = MibTableColumn
ol51nnMAUIMPortHalfStep = _Ol51nnMAUIMPortHalfStep_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 12),
    _Ol51nnMAUIMPortHalfStep_Type()
)
ol51nnMAUIMPortHalfStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortHalfStep.setStatus("mandatory")


class _Ol51nnMAUIMPortDipHalfStep_Type(Integer32):
    """Custom type ol51nnMAUIMPortDipHalfStep based on Integer32"""
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


_Ol51nnMAUIMPortDipHalfStep_Type.__name__ = "Integer32"
_Ol51nnMAUIMPortDipHalfStep_Object = MibTableColumn
ol51nnMAUIMPortDipHalfStep = _Ol51nnMAUIMPortDipHalfStep_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13, 2, 1, 13),
    _Ol51nnMAUIMPortDipHalfStep_Type()
)
ol51nnMAUIMPortDipHalfStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMAUIMPortDipHalfStep.setStatus("mandatory")
_Ol5208MTP_ObjectIdentity = ObjectIdentity
ol5208MTP = _Ol5208MTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14)
)
_Ol5208MTPModTable_Object = MibTable
ol5208MTPModTable = _Ol5208MTPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 1)
)
if mibBuilder.loadTexts:
    ol5208MTPModTable.setStatus("mandatory")
_Ol5208MTPModEntry_Object = MibTableRow
ol5208MTPModEntry = _Ol5208MTPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 1, 1)
)
ol5208MTPModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol5208MTPModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol5208MTPModEntry.setStatus("mandatory")
_Ol5208MTPModSlotIndex_Type = Integer32
_Ol5208MTPModSlotIndex_Object = MibTableColumn
ol5208MTPModSlotIndex = _Ol5208MTPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 1, 1, 1),
    _Ol5208MTPModSlotIndex_Type()
)
ol5208MTPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPModSlotIndex.setStatus("mandatory")


class _Ol5208MTPModBypsAdminState_Type(Integer32):
    """Custom type ol5208MTPModBypsAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("insert", 1))
    )


_Ol5208MTPModBypsAdminState_Type.__name__ = "Integer32"
_Ol5208MTPModBypsAdminState_Object = MibTableColumn
ol5208MTPModBypsAdminState = _Ol5208MTPModBypsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 1, 1, 2),
    _Ol5208MTPModBypsAdminState_Type()
)
ol5208MTPModBypsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol5208MTPModBypsAdminState.setStatus("mandatory")


class _Ol5208MTPModBypsOperState_Type(Integer32):
    """Custom type ol5208MTPModBypsOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("insert", 1))
    )


_Ol5208MTPModBypsOperState_Type.__name__ = "Integer32"
_Ol5208MTPModBypsOperState_Object = MibTableColumn
ol5208MTPModBypsOperState = _Ol5208MTPModBypsOperState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 1, 1, 3),
    _Ol5208MTPModBypsOperState_Type()
)
ol5208MTPModBypsOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPModBypsOperState.setStatus("mandatory")


class _Ol5208MTPModDipCableImp_Type(Integer32):
    """Custom type ol5208MTPModDipCableImp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ohm100", 1),
          ("ohm150", 2))
    )


_Ol5208MTPModDipCableImp_Type.__name__ = "Integer32"
_Ol5208MTPModDipCableImp_Object = MibTableColumn
ol5208MTPModDipCableImp = _Ol5208MTPModDipCableImp_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 1, 1, 4),
    _Ol5208MTPModDipCableImp_Type()
)
ol5208MTPModDipCableImp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPModDipCableImp.setStatus("mandatory")
_Ol5208MTPPortTable_Object = MibTable
ol5208MTPPortTable = _Ol5208MTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 2)
)
if mibBuilder.loadTexts:
    ol5208MTPPortTable.setStatus("mandatory")
_Ol5208MTPPortEntry_Object = MibTableRow
ol5208MTPPortEntry = _Ol5208MTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 2, 1)
)
ol5208MTPPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol5208MTPPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol5208MTPPortIndex"),
)
if mibBuilder.loadTexts:
    ol5208MTPPortEntry.setStatus("mandatory")
_Ol5208MTPPortSlotIndex_Type = Integer32
_Ol5208MTPPortSlotIndex_Object = MibTableColumn
ol5208MTPPortSlotIndex = _Ol5208MTPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 2, 1, 1),
    _Ol5208MTPPortSlotIndex_Type()
)
ol5208MTPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPPortSlotIndex.setStatus("mandatory")
_Ol5208MTPPortIndex_Type = Integer32
_Ol5208MTPPortIndex_Object = MibTableColumn
ol5208MTPPortIndex = _Ol5208MTPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 2, 1, 2),
    _Ol5208MTPPortIndex_Type()
)
ol5208MTPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPPortIndex.setStatus("mandatory")


class _Ol5208MTPPortDipAdminState_Type(Integer32):
    """Custom type ol5208MTPPortDipAdminState based on Integer32"""
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


_Ol5208MTPPortDipAdminState_Type.__name__ = "Integer32"
_Ol5208MTPPortDipAdminState_Object = MibTableColumn
ol5208MTPPortDipAdminState = _Ol5208MTPPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 2, 1, 3),
    _Ol5208MTPPortDipAdminState_Type()
)
ol5208MTPPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPPortDipAdminState.setStatus("mandatory")


class _Ol5208MTPPortStationType_Type(Integer32):
    """Custom type ol5208MTPPortStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac-not-present", 2),
          ("mac-present", 1))
    )


_Ol5208MTPPortStationType_Type.__name__ = "Integer32"
_Ol5208MTPPortStationType_Object = MibTableColumn
ol5208MTPPortStationType = _Ol5208MTPPortStationType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 2, 1, 4),
    _Ol5208MTPPortStationType_Type()
)
ol5208MTPPortStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol5208MTPPortStationType.setStatus("mandatory")
_Ol5208MTPTrunkTable_Object = MibTable
ol5208MTPTrunkTable = _Ol5208MTPTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3)
)
if mibBuilder.loadTexts:
    ol5208MTPTrunkTable.setStatus("mandatory")
_Ol5208MTPTrunkEntry_Object = MibTableRow
ol5208MTPTrunkEntry = _Ol5208MTPTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3, 1)
)
ol5208MTPTrunkEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol5208MTPTrunkSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol5208MTPTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol5208MTPTrunkEntry.setStatus("mandatory")
_Ol5208MTPTrunkSlotIndex_Type = Integer32
_Ol5208MTPTrunkSlotIndex_Object = MibTableColumn
ol5208MTPTrunkSlotIndex = _Ol5208MTPTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3, 1, 1),
    _Ol5208MTPTrunkSlotIndex_Type()
)
ol5208MTPTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPTrunkSlotIndex.setStatus("mandatory")
_Ol5208MTPTrunkIndex_Type = Integer32
_Ol5208MTPTrunkIndex_Object = MibTableColumn
ol5208MTPTrunkIndex = _Ol5208MTPTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3, 1, 2),
    _Ol5208MTPTrunkIndex_Type()
)
ol5208MTPTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPTrunkIndex.setStatus("mandatory")


class _Ol5208MTPTrunkDipAdminState_Type(Integer32):
    """Custom type ol5208MTPTrunkDipAdminState based on Integer32"""
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


_Ol5208MTPTrunkDipAdminState_Type.__name__ = "Integer32"
_Ol5208MTPTrunkDipAdminState_Object = MibTableColumn
ol5208MTPTrunkDipAdminState = _Ol5208MTPTrunkDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3, 1, 3),
    _Ol5208MTPTrunkDipAdminState_Type()
)
ol5208MTPTrunkDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPTrunkDipAdminState.setStatus("mandatory")


class _Ol5208MTPTrunkCableMon_Type(Integer32):
    """Custom type ol5208MTPTrunkCableMon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Ol5208MTPTrunkCableMon_Type.__name__ = "Integer32"
_Ol5208MTPTrunkCableMon_Object = MibTableColumn
ol5208MTPTrunkCableMon = _Ol5208MTPTrunkCableMon_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3, 1, 4),
    _Ol5208MTPTrunkCableMon_Type()
)
ol5208MTPTrunkCableMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol5208MTPTrunkCableMon.setStatus("mandatory")


class _Ol5208MTPTrunkDipCableMon_Type(Integer32):
    """Custom type ol5208MTPTrunkDipCableMon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Ol5208MTPTrunkDipCableMon_Type.__name__ = "Integer32"
_Ol5208MTPTrunkDipCableMon_Object = MibTableColumn
ol5208MTPTrunkDipCableMon = _Ol5208MTPTrunkDipCableMon_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3, 1, 5),
    _Ol5208MTPTrunkDipCableMon_Type()
)
ol5208MTPTrunkDipCableMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol5208MTPTrunkDipCableMon.setStatus("mandatory")


class _Ol5208MTPTrunkNetMapState_Type(Integer32):
    """Custom type ol5208MTPTrunkNetMapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("notApplicable", 1))
    )


_Ol5208MTPTrunkNetMapState_Type.__name__ = "Integer32"
_Ol5208MTPTrunkNetMapState_Object = MibTableColumn
ol5208MTPTrunkNetMapState = _Ol5208MTPTrunkNetMapState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3, 1, 6),
    _Ol5208MTPTrunkNetMapState_Type()
)
ol5208MTPTrunkNetMapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol5208MTPTrunkNetMapState.setStatus("mandatory")


class _Ol5208MTPTrunkExtBcnRecovery_Type(Integer32):
    """Custom type ol5208MTPTrunkExtBcnRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exists", 1),
          ("nonExists", 2),
          ("notApplicable", 3))
    )


_Ol5208MTPTrunkExtBcnRecovery_Type.__name__ = "Integer32"
_Ol5208MTPTrunkExtBcnRecovery_Object = MibTableColumn
ol5208MTPTrunkExtBcnRecovery = _Ol5208MTPTrunkExtBcnRecovery_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14, 3, 1, 7),
    _Ol5208MTPTrunkExtBcnRecovery_Type()
)
ol5208MTPTrunkExtBcnRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol5208MTPTrunkExtBcnRecovery.setStatus("mandatory")
_Ol51nnMFP_ObjectIdentity = ObjectIdentity
ol51nnMFP = _Ol51nnMFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15)
)
_Ol51nnMFPModTable_Object = MibTable
ol51nnMFPModTable = _Ol51nnMFPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 1)
)
if mibBuilder.loadTexts:
    ol51nnMFPModTable.setStatus("mandatory")
_Ol51nnMFPModEntry_Object = MibTableRow
ol51nnMFPModEntry = _Ol51nnMFPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 1, 1)
)
ol51nnMFPModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMFPModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFPModEntry.setStatus("mandatory")
_Ol51nnMFPModSlotIndex_Type = Integer32
_Ol51nnMFPModSlotIndex_Object = MibTableColumn
ol51nnMFPModSlotIndex = _Ol51nnMFPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 1, 1, 1),
    _Ol51nnMFPModSlotIndex_Type()
)
ol51nnMFPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFPModSlotIndex.setStatus("mandatory")
_Ol51nnMFPPortTable_Object = MibTable
ol51nnMFPPortTable = _Ol51nnMFPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2)
)
if mibBuilder.loadTexts:
    ol51nnMFPPortTable.setStatus("mandatory")
_Ol51nnMFPPortEntry_Object = MibTableRow
ol51nnMFPPortEntry = _Ol51nnMFPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1)
)
ol51nnMFPPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMFPPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnMFPPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFPPortEntry.setStatus("mandatory")
_Ol51nnMFPPortSlotIndex_Type = Integer32
_Ol51nnMFPPortSlotIndex_Object = MibTableColumn
ol51nnMFPPortSlotIndex = _Ol51nnMFPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 1),
    _Ol51nnMFPPortSlotIndex_Type()
)
ol51nnMFPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFPPortSlotIndex.setStatus("mandatory")
_Ol51nnMFPPortIndex_Type = Integer32
_Ol51nnMFPPortIndex_Object = MibTableColumn
ol51nnMFPPortIndex = _Ol51nnMFPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 2),
    _Ol51nnMFPPortIndex_Type()
)
ol51nnMFPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFPPortIndex.setStatus("mandatory")


class _Ol51nnMFPPortAdminState_Type(Integer32):
    """Custom type ol51nnMFPPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMFPPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMFPPortAdminState_Object = MibTableColumn
ol51nnMFPPortAdminState = _Ol51nnMFPPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 3),
    _Ol51nnMFPPortAdminState_Type()
)
ol51nnMFPPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFPPortAdminState.setStatus("mandatory")
_Ol51nnMFPPortBuddySlot_Type = Integer32
_Ol51nnMFPPortBuddySlot_Object = MibTableColumn
ol51nnMFPPortBuddySlot = _Ol51nnMFPPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 4),
    _Ol51nnMFPPortBuddySlot_Type()
)
ol51nnMFPPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFPPortBuddySlot.setStatus("mandatory")
_Ol51nnMFPPortBuddyPort_Type = Integer32
_Ol51nnMFPPortBuddyPort_Object = MibTableColumn
ol51nnMFPPortBuddyPort = _Ol51nnMFPPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 5),
    _Ol51nnMFPPortBuddyPort_Type()
)
ol51nnMFPPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFPPortBuddyPort.setStatus("mandatory")


class _Ol51nnMFPPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMFPPortDipAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMFPPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMFPPortDipAdminState_Object = MibTableColumn
ol51nnMFPPortDipAdminState = _Ol51nnMFPPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 6),
    _Ol51nnMFPPortDipAdminState_Type()
)
ol51nnMFPPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFPPortDipAdminState.setStatus("mandatory")


class _Ol51nnMFPPortDipNetwork_Type(Integer32):
    """Custom type ol51nnMFPPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMFPPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMFPPortDipNetwork_Object = MibTableColumn
ol51nnMFPPortDipNetwork = _Ol51nnMFPPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 7),
    _Ol51nnMFPPortDipNetwork_Type()
)
ol51nnMFPPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFPPortDipNetwork.setStatus("mandatory")


class _Ol51nnMFPPortLLW_Type(Integer32):
    """Custom type ol51nnMFPPortLLW based on Integer32"""
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


_Ol51nnMFPPortLLW_Type.__name__ = "Integer32"
_Ol51nnMFPPortLLW_Object = MibTableColumn
ol51nnMFPPortLLW = _Ol51nnMFPPortLLW_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 8),
    _Ol51nnMFPPortLLW_Type()
)
ol51nnMFPPortLLW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFPPortLLW.setStatus("mandatory")


class _Ol51nnMFPPortDipLLW_Type(Integer32):
    """Custom type ol51nnMFPPortDipLLW based on Integer32"""
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


_Ol51nnMFPPortDipLLW_Type.__name__ = "Integer32"
_Ol51nnMFPPortDipLLW_Object = MibTableColumn
ol51nnMFPPortDipLLW = _Ol51nnMFPPortDipLLW_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 9),
    _Ol51nnMFPPortDipLLW_Type()
)
ol51nnMFPPortDipLLW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFPPortDipLLW.setStatus("mandatory")


class _Ol51nnMFPPortHipwr_Type(Integer32):
    """Custom type ol51nnMFPPortHipwr based on Integer32"""
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


_Ol51nnMFPPortHipwr_Type.__name__ = "Integer32"
_Ol51nnMFPPortHipwr_Object = MibTableColumn
ol51nnMFPPortHipwr = _Ol51nnMFPPortHipwr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 10),
    _Ol51nnMFPPortHipwr_Type()
)
ol51nnMFPPortHipwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFPPortHipwr.setStatus("mandatory")


class _Ol51nnMFPPortDipHipwr_Type(Integer32):
    """Custom type ol51nnMFPPortDipHipwr based on Integer32"""
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


_Ol51nnMFPPortDipHipwr_Type.__name__ = "Integer32"
_Ol51nnMFPPortDipHipwr_Object = MibTableColumn
ol51nnMFPPortDipHipwr = _Ol51nnMFPPortDipHipwr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15, 2, 1, 11),
    _Ol51nnMFPPortDipHipwr_Type()
)
ol51nnMFPPortDipHipwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFPPortDipHipwr.setStatus("mandatory")
_Ol51nnMFBP_ObjectIdentity = ObjectIdentity
ol51nnMFBP = _Ol51nnMFBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16)
)
_Ol51nnMFBPModTable_Object = MibTable
ol51nnMFBPModTable = _Ol51nnMFBPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 1)
)
if mibBuilder.loadTexts:
    ol51nnMFBPModTable.setStatus("mandatory")
_Ol51nnMFBPModEntry_Object = MibTableRow
ol51nnMFBPModEntry = _Ol51nnMFBPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 1, 1)
)
ol51nnMFBPModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMFBPModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFBPModEntry.setStatus("mandatory")
_Ol51nnMFBPModSlotIndex_Type = Integer32
_Ol51nnMFBPModSlotIndex_Object = MibTableColumn
ol51nnMFBPModSlotIndex = _Ol51nnMFBPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 1, 1, 1),
    _Ol51nnMFBPModSlotIndex_Type()
)
ol51nnMFBPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPModSlotIndex.setStatus("mandatory")
_Ol51nnMFBPPortTable_Object = MibTable
ol51nnMFBPPortTable = _Ol51nnMFBPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2)
)
if mibBuilder.loadTexts:
    ol51nnMFBPPortTable.setStatus("mandatory")
_Ol51nnMFBPPortEntry_Object = MibTableRow
ol51nnMFBPPortEntry = _Ol51nnMFBPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1)
)
ol51nnMFBPPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMFBPPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnMFBPPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFBPPortEntry.setStatus("mandatory")
_Ol51nnMFBPPortSlotIndex_Type = Integer32
_Ol51nnMFBPPortSlotIndex_Object = MibTableColumn
ol51nnMFBPPortSlotIndex = _Ol51nnMFBPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 1),
    _Ol51nnMFBPPortSlotIndex_Type()
)
ol51nnMFBPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPPortSlotIndex.setStatus("mandatory")
_Ol51nnMFBPPortIndex_Type = Integer32
_Ol51nnMFBPPortIndex_Object = MibTableColumn
ol51nnMFBPPortIndex = _Ol51nnMFBPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 2),
    _Ol51nnMFBPPortIndex_Type()
)
ol51nnMFBPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPPortIndex.setStatus("mandatory")


class _Ol51nnMFBPPortAdminState_Type(Integer32):
    """Custom type ol51nnMFBPPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMFBPPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMFBPPortAdminState_Object = MibTableColumn
ol51nnMFBPPortAdminState = _Ol51nnMFBPPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 3),
    _Ol51nnMFBPPortAdminState_Type()
)
ol51nnMFBPPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBPPortAdminState.setStatus("mandatory")
_Ol51nnMFBPPortBuddySlot_Type = Integer32
_Ol51nnMFBPPortBuddySlot_Object = MibTableColumn
ol51nnMFBPPortBuddySlot = _Ol51nnMFBPPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 4),
    _Ol51nnMFBPPortBuddySlot_Type()
)
ol51nnMFBPPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBPPortBuddySlot.setStatus("mandatory")
_Ol51nnMFBPPortBuddyPort_Type = Integer32
_Ol51nnMFBPPortBuddyPort_Object = MibTableColumn
ol51nnMFBPPortBuddyPort = _Ol51nnMFBPPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 5),
    _Ol51nnMFBPPortBuddyPort_Type()
)
ol51nnMFBPPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBPPortBuddyPort.setStatus("mandatory")


class _Ol51nnMFBPPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMFBPPortDipAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMFBPPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMFBPPortDipAdminState_Object = MibTableColumn
ol51nnMFBPPortDipAdminState = _Ol51nnMFBPPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 6),
    _Ol51nnMFBPPortDipAdminState_Type()
)
ol51nnMFBPPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPPortDipAdminState.setStatus("mandatory")


class _Ol51nnMFBPPortDipNetwork_Type(Integer32):
    """Custom type ol51nnMFBPPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMFBPPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMFBPPortDipNetwork_Object = MibTableColumn
ol51nnMFBPPortDipNetwork = _Ol51nnMFBPPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 7),
    _Ol51nnMFBPPortDipNetwork_Type()
)
ol51nnMFBPPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPPortDipNetwork.setStatus("mandatory")


class _Ol51nnMFBPPortLLW_Type(Integer32):
    """Custom type ol51nnMFBPPortLLW based on Integer32"""
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


_Ol51nnMFBPPortLLW_Type.__name__ = "Integer32"
_Ol51nnMFBPPortLLW_Object = MibTableColumn
ol51nnMFBPPortLLW = _Ol51nnMFBPPortLLW_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 8),
    _Ol51nnMFBPPortLLW_Type()
)
ol51nnMFBPPortLLW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBPPortLLW.setStatus("mandatory")


class _Ol51nnMFBPPortDipLLW_Type(Integer32):
    """Custom type ol51nnMFBPPortDipLLW based on Integer32"""
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


_Ol51nnMFBPPortDipLLW_Type.__name__ = "Integer32"
_Ol51nnMFBPPortDipLLW_Object = MibTableColumn
ol51nnMFBPPortDipLLW = _Ol51nnMFBPPortDipLLW_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 9),
    _Ol51nnMFBPPortDipLLW_Type()
)
ol51nnMFBPPortDipLLW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPPortDipLLW.setStatus("mandatory")


class _Ol51nnMFBPPortHipwr_Type(Integer32):
    """Custom type ol51nnMFBPPortHipwr based on Integer32"""
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


_Ol51nnMFBPPortHipwr_Type.__name__ = "Integer32"
_Ol51nnMFBPPortHipwr_Object = MibTableColumn
ol51nnMFBPPortHipwr = _Ol51nnMFBPPortHipwr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 10),
    _Ol51nnMFBPPortHipwr_Type()
)
ol51nnMFBPPortHipwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBPPortHipwr.setStatus("mandatory")


class _Ol51nnMFBPPortDipHipwr_Type(Integer32):
    """Custom type ol51nnMFBPPortDipHipwr based on Integer32"""
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


_Ol51nnMFBPPortDipHipwr_Type.__name__ = "Integer32"
_Ol51nnMFBPPortDipHipwr_Object = MibTableColumn
ol51nnMFBPPortDipHipwr = _Ol51nnMFBPPortDipHipwr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16, 2, 1, 11),
    _Ol51nnMFBPPortDipHipwr_Type()
)
ol51nnMFBPPortDipHipwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPPortDipHipwr.setStatus("mandatory")
_Ol51nnMTPL_ObjectIdentity = ObjectIdentity
ol51nnMTPL = _Ol51nnMTPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17)
)
_Ol51nnMTPLModTable_Object = MibTable
ol51nnMTPLModTable = _Ol51nnMTPLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 1)
)
if mibBuilder.loadTexts:
    ol51nnMTPLModTable.setStatus("mandatory")
_Ol51nnMTPLModEntry_Object = MibTableRow
ol51nnMTPLModEntry = _Ol51nnMTPLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 1, 1)
)
ol51nnMTPLModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMTPLModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPLModEntry.setStatus("mandatory")
_Ol51nnMTPLModSlotIndex_Type = Integer32
_Ol51nnMTPLModSlotIndex_Object = MibTableColumn
ol51nnMTPLModSlotIndex = _Ol51nnMTPLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 1, 1, 1),
    _Ol51nnMTPLModSlotIndex_Type()
)
ol51nnMTPLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLModSlotIndex.setStatus("mandatory")


class _Ol51nnMTPLModDipNetwork_Type(Integer32):
    """Custom type ol51nnMTPLModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMTPLModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMTPLModDipNetwork_Object = MibTableColumn
ol51nnMTPLModDipNetwork = _Ol51nnMTPLModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 1, 1, 2),
    _Ol51nnMTPLModDipNetwork_Type()
)
ol51nnMTPLModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLModDipNetwork.setStatus("mandatory")
_Ol51nnMTPLPortTable_Object = MibTable
ol51nnMTPLPortTable = _Ol51nnMTPLPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2)
)
if mibBuilder.loadTexts:
    ol51nnMTPLPortTable.setStatus("mandatory")
_Ol51nnMTPLPortEntry_Object = MibTableRow
ol51nnMTPLPortEntry = _Ol51nnMTPLPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1)
)
ol51nnMTPLPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMTPLPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnMTPLPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPLPortEntry.setStatus("mandatory")
_Ol51nnMTPLPortSlotIndex_Type = Integer32
_Ol51nnMTPLPortSlotIndex_Object = MibTableColumn
ol51nnMTPLPortSlotIndex = _Ol51nnMTPLPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 1),
    _Ol51nnMTPLPortSlotIndex_Type()
)
ol51nnMTPLPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLPortSlotIndex.setStatus("mandatory")
_Ol51nnMTPLPortIndex_Type = Integer32
_Ol51nnMTPLPortIndex_Object = MibTableColumn
ol51nnMTPLPortIndex = _Ol51nnMTPLPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 2),
    _Ol51nnMTPLPortIndex_Type()
)
ol51nnMTPLPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLPortIndex.setStatus("mandatory")


class _Ol51nnMTPLPortAdminState_Type(Integer32):
    """Custom type ol51nnMTPLPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3),
          ("remote-diagnostics", 8))
    )


_Ol51nnMTPLPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPLPortAdminState_Object = MibTableColumn
ol51nnMTPLPortAdminState = _Ol51nnMTPLPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 3),
    _Ol51nnMTPLPortAdminState_Type()
)
ol51nnMTPLPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLPortAdminState.setStatus("mandatory")
_Ol51nnMTPLPortBuddySlot_Type = Integer32
_Ol51nnMTPLPortBuddySlot_Object = MibTableColumn
ol51nnMTPLPortBuddySlot = _Ol51nnMTPLPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 4),
    _Ol51nnMTPLPortBuddySlot_Type()
)
ol51nnMTPLPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLPortBuddySlot.setStatus("mandatory")
_Ol51nnMTPLPortBuddyPort_Type = Integer32
_Ol51nnMTPLPortBuddyPort_Object = MibTableColumn
ol51nnMTPLPortBuddyPort = _Ol51nnMTPLPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 5),
    _Ol51nnMTPLPortBuddyPort_Type()
)
ol51nnMTPLPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLPortBuddyPort.setStatus("mandatory")


class _Ol51nnMTPLPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMTPLPortDipAdminState based on Integer32"""
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


_Ol51nnMTPLPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPLPortDipAdminState_Object = MibTableColumn
ol51nnMTPLPortDipAdminState = _Ol51nnMTPLPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 6),
    _Ol51nnMTPLPortDipAdminState_Type()
)
ol51nnMTPLPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLPortDipAdminState.setStatus("mandatory")


class _Ol51nnMTPLPortLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPLPortLinkInteg based on Integer32"""
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


_Ol51nnMTPLPortLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPLPortLinkInteg_Object = MibTableColumn
ol51nnMTPLPortLinkInteg = _Ol51nnMTPLPortLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 7),
    _Ol51nnMTPLPortLinkInteg_Type()
)
ol51nnMTPLPortLinkInteg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLPortLinkInteg.setStatus("mandatory")


class _Ol51nnMTPLPortDipLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPLPortDipLinkInteg based on Integer32"""
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


_Ol51nnMTPLPortDipLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPLPortDipLinkInteg_Object = MibTableColumn
ol51nnMTPLPortDipLinkInteg = _Ol51nnMTPLPortDipLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 8),
    _Ol51nnMTPLPortDipLinkInteg_Type()
)
ol51nnMTPLPortDipLinkInteg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLPortDipLinkInteg.setStatus("mandatory")


class _Ol51nnMTPLPortSquelch_Type(Integer32):
    """Custom type ol51nnMTPLPortSquelch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1))
    )


_Ol51nnMTPLPortSquelch_Type.__name__ = "Integer32"
_Ol51nnMTPLPortSquelch_Object = MibTableColumn
ol51nnMTPLPortSquelch = _Ol51nnMTPLPortSquelch_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 9),
    _Ol51nnMTPLPortSquelch_Type()
)
ol51nnMTPLPortSquelch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLPortSquelch.setStatus("mandatory")


class _Ol51nnMTPLPortJabber_Type(Integer32):
    """Custom type ol51nnMTPLPortJabber based on Integer32"""
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


_Ol51nnMTPLPortJabber_Type.__name__ = "Integer32"
_Ol51nnMTPLPortJabber_Object = MibTableColumn
ol51nnMTPLPortJabber = _Ol51nnMTPLPortJabber_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 10),
    _Ol51nnMTPLPortJabber_Type()
)
ol51nnMTPLPortJabber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPLPortJabber.setStatus("mandatory")


class _Ol51nnMTPLPortDipJabber_Type(Integer32):
    """Custom type ol51nnMTPLPortDipJabber based on Integer32"""
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


_Ol51nnMTPLPortDipJabber_Type.__name__ = "Integer32"
_Ol51nnMTPLPortDipJabber_Object = MibTableColumn
ol51nnMTPLPortDipJabber = _Ol51nnMTPLPortDipJabber_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17, 2, 1, 11),
    _Ol51nnMTPLPortDipJabber_Type()
)
ol51nnMTPLPortDipJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPLPortDipJabber.setStatus("mandatory")
_Ol51nnMTPPL_ObjectIdentity = ObjectIdentity
ol51nnMTPPL = _Ol51nnMTPPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18)
)
_Ol51nnMTPPLModTable_Object = MibTable
ol51nnMTPPLModTable = _Ol51nnMTPPLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 1)
)
if mibBuilder.loadTexts:
    ol51nnMTPPLModTable.setStatus("mandatory")
_Ol51nnMTPPLModEntry_Object = MibTableRow
ol51nnMTPPLModEntry = _Ol51nnMTPPLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 1, 1)
)
ol51nnMTPPLModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMTPPLModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPPLModEntry.setStatus("mandatory")
_Ol51nnMTPPLModSlotIndex_Type = Integer32
_Ol51nnMTPPLModSlotIndex_Object = MibTableColumn
ol51nnMTPPLModSlotIndex = _Ol51nnMTPPLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 1, 1, 1),
    _Ol51nnMTPPLModSlotIndex_Type()
)
ol51nnMTPPLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPLModSlotIndex.setStatus("mandatory")
_Ol51nnMTPPLPortTable_Object = MibTable
ol51nnMTPPLPortTable = _Ol51nnMTPPLPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2)
)
if mibBuilder.loadTexts:
    ol51nnMTPPLPortTable.setStatus("mandatory")
_Ol51nnMTPPLPortEntry_Object = MibTableRow
ol51nnMTPPLPortEntry = _Ol51nnMTPPLPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1)
)
ol51nnMTPPLPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMTPPLPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnMTPPLPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPPLPortEntry.setStatus("mandatory")
_Ol51nnMTPPLPortSlotIndex_Type = Integer32
_Ol51nnMTPPLPortSlotIndex_Object = MibTableColumn
ol51nnMTPPLPortSlotIndex = _Ol51nnMTPPLPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 1),
    _Ol51nnMTPPLPortSlotIndex_Type()
)
ol51nnMTPPLPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortSlotIndex.setStatus("mandatory")
_Ol51nnMTPPLPortIndex_Type = Integer32
_Ol51nnMTPPLPortIndex_Object = MibTableColumn
ol51nnMTPPLPortIndex = _Ol51nnMTPPLPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 2),
    _Ol51nnMTPPLPortIndex_Type()
)
ol51nnMTPPLPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortIndex.setStatus("mandatory")


class _Ol51nnMTPPLPortAdminState_Type(Integer32):
    """Custom type ol51nnMTPPLPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3),
          ("remote-diagnostics", 8))
    )


_Ol51nnMTPPLPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPPLPortAdminState_Object = MibTableColumn
ol51nnMTPPLPortAdminState = _Ol51nnMTPPLPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 3),
    _Ol51nnMTPPLPortAdminState_Type()
)
ol51nnMTPPLPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortAdminState.setStatus("mandatory")
_Ol51nnMTPPLPortBuddySlot_Type = Integer32
_Ol51nnMTPPLPortBuddySlot_Object = MibTableColumn
ol51nnMTPPLPortBuddySlot = _Ol51nnMTPPLPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 4),
    _Ol51nnMTPPLPortBuddySlot_Type()
)
ol51nnMTPPLPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortBuddySlot.setStatus("mandatory")
_Ol51nnMTPPLPortBuddyPort_Type = Integer32
_Ol51nnMTPPLPortBuddyPort_Object = MibTableColumn
ol51nnMTPPLPortBuddyPort = _Ol51nnMTPPLPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 5),
    _Ol51nnMTPPLPortBuddyPort_Type()
)
ol51nnMTPPLPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortBuddyPort.setStatus("mandatory")


class _Ol51nnMTPPLPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMTPPLPortDipAdminState based on Integer32"""
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


_Ol51nnMTPPLPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPPLPortDipAdminState_Object = MibTableColumn
ol51nnMTPPLPortDipAdminState = _Ol51nnMTPPLPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 6),
    _Ol51nnMTPPLPortDipAdminState_Type()
)
ol51nnMTPPLPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortDipAdminState.setStatus("mandatory")


class _Ol51nnMTPPLPortDipNetwork_Type(Integer32):
    """Custom type ol51nnMTPPLPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMTPPLPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMTPPLPortDipNetwork_Object = MibTableColumn
ol51nnMTPPLPortDipNetwork = _Ol51nnMTPPLPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 7),
    _Ol51nnMTPPLPortDipNetwork_Type()
)
ol51nnMTPPLPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortDipNetwork.setStatus("mandatory")


class _Ol51nnMTPPLPortLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPPLPortLinkInteg based on Integer32"""
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


_Ol51nnMTPPLPortLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPPLPortLinkInteg_Object = MibTableColumn
ol51nnMTPPLPortLinkInteg = _Ol51nnMTPPLPortLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 8),
    _Ol51nnMTPPLPortLinkInteg_Type()
)
ol51nnMTPPLPortLinkInteg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortLinkInteg.setStatus("mandatory")


class _Ol51nnMTPPLPortDipLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPPLPortDipLinkInteg based on Integer32"""
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


_Ol51nnMTPPLPortDipLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPPLPortDipLinkInteg_Object = MibTableColumn
ol51nnMTPPLPortDipLinkInteg = _Ol51nnMTPPLPortDipLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 9),
    _Ol51nnMTPPLPortDipLinkInteg_Type()
)
ol51nnMTPPLPortDipLinkInteg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortDipLinkInteg.setStatus("mandatory")


class _Ol51nnMTPPLPortSquelch_Type(Integer32):
    """Custom type ol51nnMTPPLPortSquelch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1))
    )


_Ol51nnMTPPLPortSquelch_Type.__name__ = "Integer32"
_Ol51nnMTPPLPortSquelch_Object = MibTableColumn
ol51nnMTPPLPortSquelch = _Ol51nnMTPPLPortSquelch_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 10),
    _Ol51nnMTPPLPortSquelch_Type()
)
ol51nnMTPPLPortSquelch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortSquelch.setStatus("mandatory")


class _Ol51nnMTPPLPortJabber_Type(Integer32):
    """Custom type ol51nnMTPPLPortJabber based on Integer32"""
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


_Ol51nnMTPPLPortJabber_Type.__name__ = "Integer32"
_Ol51nnMTPPLPortJabber_Object = MibTableColumn
ol51nnMTPPLPortJabber = _Ol51nnMTPPLPortJabber_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 11),
    _Ol51nnMTPPLPortJabber_Type()
)
ol51nnMTPPLPortJabber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortJabber.setStatus("mandatory")


class _Ol51nnMTPPLPortDipJabber_Type(Integer32):
    """Custom type ol51nnMTPPLPortDipJabber based on Integer32"""
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


_Ol51nnMTPPLPortDipJabber_Type.__name__ = "Integer32"
_Ol51nnMTPPLPortDipJabber_Object = MibTableColumn
ol51nnMTPPLPortDipJabber = _Ol51nnMTPPLPortDipJabber_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18, 2, 1, 12),
    _Ol51nnMTPPLPortDipJabber_Type()
)
ol51nnMTPPLPortDipJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPPLPortDipJabber.setStatus("mandatory")
_Ol52nnMTP_ObjectIdentity = ObjectIdentity
ol52nnMTP = _Ol52nnMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19)
)
_Ol52nnMTPModTable_Object = MibTable
ol52nnMTPModTable = _Ol52nnMTPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 1)
)
if mibBuilder.loadTexts:
    ol52nnMTPModTable.setStatus("mandatory")
_Ol52nnMTPModEntry_Object = MibTableRow
ol52nnMTPModEntry = _Ol52nnMTPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 1, 1)
)
ol52nnMTPModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol52nnMTPModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMTPModEntry.setStatus("mandatory")
_Ol52nnMTPModSlotIndex_Type = Integer32
_Ol52nnMTPModSlotIndex_Object = MibTableColumn
ol52nnMTPModSlotIndex = _Ol52nnMTPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 1, 1, 1),
    _Ol52nnMTPModSlotIndex_Type()
)
ol52nnMTPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPModSlotIndex.setStatus("mandatory")


class _Ol52nnMTPModRingSpeed_Type(Integer32):
    """Custom type ol52nnMTPModRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 1),
          ("sixteenMegabit", 2))
    )


_Ol52nnMTPModRingSpeed_Type.__name__ = "Integer32"
_Ol52nnMTPModRingSpeed_Object = MibTableColumn
ol52nnMTPModRingSpeed = _Ol52nnMTPModRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 1, 1, 2),
    _Ol52nnMTPModRingSpeed_Type()
)
ol52nnMTPModRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMTPModRingSpeed.setStatus("mandatory")


class _Ol52nnMTPModDipRingSpeed_Type(Integer32):
    """Custom type ol52nnMTPModDipRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 1),
          ("sixteenMegabit", 2))
    )


_Ol52nnMTPModDipRingSpeed_Type.__name__ = "Integer32"
_Ol52nnMTPModDipRingSpeed_Object = MibTableColumn
ol52nnMTPModDipRingSpeed = _Ol52nnMTPModDipRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 1, 1, 3),
    _Ol52nnMTPModDipRingSpeed_Type()
)
ol52nnMTPModDipRingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPModDipRingSpeed.setStatus("mandatory")


class _Ol52nnMTPModCableImp_Type(Integer32):
    """Custom type ol52nnMTPModCableImp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ohm100", 1),
          ("ohm150", 2))
    )


_Ol52nnMTPModCableImp_Type.__name__ = "Integer32"
_Ol52nnMTPModCableImp_Object = MibTableColumn
ol52nnMTPModCableImp = _Ol52nnMTPModCableImp_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 1, 1, 4),
    _Ol52nnMTPModCableImp_Type()
)
ol52nnMTPModCableImp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMTPModCableImp.setStatus("mandatory")


class _Ol52nnMTPModDipCableImp_Type(Integer32):
    """Custom type ol52nnMTPModDipCableImp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ohm100", 1),
          ("ohm150", 2))
    )


_Ol52nnMTPModDipCableImp_Type.__name__ = "Integer32"
_Ol52nnMTPModDipCableImp_Object = MibTableColumn
ol52nnMTPModDipCableImp = _Ol52nnMTPModDipCableImp_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 1, 1, 5),
    _Ol52nnMTPModDipCableImp_Type()
)
ol52nnMTPModDipCableImp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPModDipCableImp.setStatus("mandatory")
_Ol52nnMTPPortTable_Object = MibTable
ol52nnMTPPortTable = _Ol52nnMTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 2)
)
if mibBuilder.loadTexts:
    ol52nnMTPPortTable.setStatus("mandatory")
_Ol52nnMTPPortEntry_Object = MibTableRow
ol52nnMTPPortEntry = _Ol52nnMTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 2, 1)
)
ol52nnMTPPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol52nnMTPPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol52nnMTPPortIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMTPPortEntry.setStatus("mandatory")
_Ol52nnMTPPortSlotIndex_Type = Integer32
_Ol52nnMTPPortSlotIndex_Object = MibTableColumn
ol52nnMTPPortSlotIndex = _Ol52nnMTPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 2, 1, 1),
    _Ol52nnMTPPortSlotIndex_Type()
)
ol52nnMTPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPPortSlotIndex.setStatus("mandatory")
_Ol52nnMTPPortIndex_Type = Integer32
_Ol52nnMTPPortIndex_Object = MibTableColumn
ol52nnMTPPortIndex = _Ol52nnMTPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 2, 1, 2),
    _Ol52nnMTPPortIndex_Type()
)
ol52nnMTPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPPortIndex.setStatus("mandatory")


class _Ol52nnMTPPortDipAdminState_Type(Integer32):
    """Custom type ol52nnMTPPortDipAdminState based on Integer32"""
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


_Ol52nnMTPPortDipAdminState_Type.__name__ = "Integer32"
_Ol52nnMTPPortDipAdminState_Object = MibTableColumn
ol52nnMTPPortDipAdminState = _Ol52nnMTPPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 2, 1, 3),
    _Ol52nnMTPPortDipAdminState_Type()
)
ol52nnMTPPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPPortDipAdminState.setStatus("mandatory")


class _Ol52nnMTPPortStationType_Type(Integer32):
    """Custom type ol52nnMTPPortStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac-not-present", 2),
          ("mac-present", 1))
    )


_Ol52nnMTPPortStationType_Type.__name__ = "Integer32"
_Ol52nnMTPPortStationType_Object = MibTableColumn
ol52nnMTPPortStationType = _Ol52nnMTPPortStationType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 2, 1, 4),
    _Ol52nnMTPPortStationType_Type()
)
ol52nnMTPPortStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMTPPortStationType.setStatus("mandatory")
_Ol52nnMTPTrunkTable_Object = MibTable
ol52nnMTPTrunkTable = _Ol52nnMTPTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 3)
)
if mibBuilder.loadTexts:
    ol52nnMTPTrunkTable.setStatus("mandatory")
_Ol52nnMTPTrunkEntry_Object = MibTableRow
ol52nnMTPTrunkEntry = _Ol52nnMTPTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 3, 1)
)
ol52nnMTPTrunkEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol52nnMTPTrunkSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol52nnMTPTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMTPTrunkEntry.setStatus("mandatory")
_Ol52nnMTPTrunkSlotIndex_Type = Integer32
_Ol52nnMTPTrunkSlotIndex_Object = MibTableColumn
ol52nnMTPTrunkSlotIndex = _Ol52nnMTPTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 3, 1, 1),
    _Ol52nnMTPTrunkSlotIndex_Type()
)
ol52nnMTPTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPTrunkSlotIndex.setStatus("mandatory")
_Ol52nnMTPTrunkIndex_Type = Integer32
_Ol52nnMTPTrunkIndex_Object = MibTableColumn
ol52nnMTPTrunkIndex = _Ol52nnMTPTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 3, 1, 2),
    _Ol52nnMTPTrunkIndex_Type()
)
ol52nnMTPTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPTrunkIndex.setStatus("mandatory")


class _Ol52nnMTPTrunkDipAdminState_Type(Integer32):
    """Custom type ol52nnMTPTrunkDipAdminState based on Integer32"""
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


_Ol52nnMTPTrunkDipAdminState_Type.__name__ = "Integer32"
_Ol52nnMTPTrunkDipAdminState_Object = MibTableColumn
ol52nnMTPTrunkDipAdminState = _Ol52nnMTPTrunkDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19, 3, 1, 3),
    _Ol52nnMTPTrunkDipAdminState_Type()
)
ol52nnMTPTrunkDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMTPTrunkDipAdminState.setStatus("mandatory")
_Ol52nnMFR_ObjectIdentity = ObjectIdentity
ol52nnMFR = _Ol52nnMFR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20)
)
_Ol52nnMFRModTable_Object = MibTable
ol52nnMFRModTable = _Ol52nnMFRModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 1)
)
if mibBuilder.loadTexts:
    ol52nnMFRModTable.setStatus("mandatory")
_Ol52nnMFRModEntry_Object = MibTableRow
ol52nnMFRModEntry = _Ol52nnMFRModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 1, 1)
)
ol52nnMFRModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol52nnMFRModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMFRModEntry.setStatus("mandatory")
_Ol52nnMFRModSlotIndex_Type = Integer32
_Ol52nnMFRModSlotIndex_Object = MibTableColumn
ol52nnMFRModSlotIndex = _Ol52nnMFRModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 1, 1, 1),
    _Ol52nnMFRModSlotIndex_Type()
)
ol52nnMFRModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRModSlotIndex.setStatus("mandatory")


class _Ol52nnMFRModRingSpeed_Type(Integer32):
    """Custom type ol52nnMFRModRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 1),
          ("sixteenMegabit", 2))
    )


_Ol52nnMFRModRingSpeed_Type.__name__ = "Integer32"
_Ol52nnMFRModRingSpeed_Object = MibTableColumn
ol52nnMFRModRingSpeed = _Ol52nnMFRModRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 1, 1, 2),
    _Ol52nnMFRModRingSpeed_Type()
)
ol52nnMFRModRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMFRModRingSpeed.setStatus("mandatory")


class _Ol52nnMFRModDipRingSpeed_Type(Integer32):
    """Custom type ol52nnMFRModDipRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 1),
          ("sixteenMegabit", 2))
    )


_Ol52nnMFRModDipRingSpeed_Type.__name__ = "Integer32"
_Ol52nnMFRModDipRingSpeed_Object = MibTableColumn
ol52nnMFRModDipRingSpeed = _Ol52nnMFRModDipRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 1, 1, 3),
    _Ol52nnMFRModDipRingSpeed_Type()
)
ol52nnMFRModDipRingSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRModDipRingSpeed.setStatus("mandatory")
_Ol52nnMFRPortTable_Object = MibTable
ol52nnMFRPortTable = _Ol52nnMFRPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 2)
)
if mibBuilder.loadTexts:
    ol52nnMFRPortTable.setStatus("mandatory")
_Ol52nnMFRPortEntry_Object = MibTableRow
ol52nnMFRPortEntry = _Ol52nnMFRPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 2, 1)
)
ol52nnMFRPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol52nnMFRPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol52nnMFRPortIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMFRPortEntry.setStatus("mandatory")
_Ol52nnMFRPortSlotIndex_Type = Integer32
_Ol52nnMFRPortSlotIndex_Object = MibTableColumn
ol52nnMFRPortSlotIndex = _Ol52nnMFRPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 2, 1, 1),
    _Ol52nnMFRPortSlotIndex_Type()
)
ol52nnMFRPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRPortSlotIndex.setStatus("mandatory")
_Ol52nnMFRPortIndex_Type = Integer32
_Ol52nnMFRPortIndex_Object = MibTableColumn
ol52nnMFRPortIndex = _Ol52nnMFRPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 2, 1, 2),
    _Ol52nnMFRPortIndex_Type()
)
ol52nnMFRPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRPortIndex.setStatus("mandatory")


class _Ol52nnMFRPortDipAdminState_Type(Integer32):
    """Custom type ol52nnMFRPortDipAdminState based on Integer32"""
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


_Ol52nnMFRPortDipAdminState_Type.__name__ = "Integer32"
_Ol52nnMFRPortDipAdminState_Object = MibTableColumn
ol52nnMFRPortDipAdminState = _Ol52nnMFRPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 2, 1, 3),
    _Ol52nnMFRPortDipAdminState_Type()
)
ol52nnMFRPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRPortDipAdminState.setStatus("mandatory")


class _Ol52nnMFRPortCableImp_Type(Integer32):
    """Custom type ol52nnMFRPortCableImp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ohm100", 1),
          ("ohm150", 2))
    )


_Ol52nnMFRPortCableImp_Type.__name__ = "Integer32"
_Ol52nnMFRPortCableImp_Object = MibTableColumn
ol52nnMFRPortCableImp = _Ol52nnMFRPortCableImp_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 2, 1, 4),
    _Ol52nnMFRPortCableImp_Type()
)
ol52nnMFRPortCableImp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRPortCableImp.setStatus("mandatory")


class _Ol52nnMFRPortStationType_Type(Integer32):
    """Custom type ol52nnMFRPortStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac-not-present", 2),
          ("mac-present", 1))
    )


_Ol52nnMFRPortStationType_Type.__name__ = "Integer32"
_Ol52nnMFRPortStationType_Object = MibTableColumn
ol52nnMFRPortStationType = _Ol52nnMFRPortStationType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 2, 1, 5),
    _Ol52nnMFRPortStationType_Type()
)
ol52nnMFRPortStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMFRPortStationType.setStatus("mandatory")
_Ol52nnMFRTrunkTable_Object = MibTable
ol52nnMFRTrunkTable = _Ol52nnMFRTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3)
)
if mibBuilder.loadTexts:
    ol52nnMFRTrunkTable.setStatus("mandatory")
_Ol52nnMFRTrunkEntry_Object = MibTableRow
ol52nnMFRTrunkEntry = _Ol52nnMFRTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1)
)
ol52nnMFRTrunkEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol52nnMFRTrunkSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol52nnMFRTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMFRTrunkEntry.setStatus("mandatory")
_Ol52nnMFRTrunkSlotIndex_Type = Integer32
_Ol52nnMFRTrunkSlotIndex_Object = MibTableColumn
ol52nnMFRTrunkSlotIndex = _Ol52nnMFRTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 1),
    _Ol52nnMFRTrunkSlotIndex_Type()
)
ol52nnMFRTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkSlotIndex.setStatus("mandatory")
_Ol52nnMFRTrunkIndex_Type = Integer32
_Ol52nnMFRTrunkIndex_Object = MibTableColumn
ol52nnMFRTrunkIndex = _Ol52nnMFRTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 2),
    _Ol52nnMFRTrunkIndex_Type()
)
ol52nnMFRTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkIndex.setStatus("mandatory")


class _Ol52nnMFRTrunkDipAdminState_Type(Integer32):
    """Custom type ol52nnMFRTrunkDipAdminState based on Integer32"""
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


_Ol52nnMFRTrunkDipAdminState_Type.__name__ = "Integer32"
_Ol52nnMFRTrunkDipAdminState_Object = MibTableColumn
ol52nnMFRTrunkDipAdminState = _Ol52nnMFRTrunkDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 3),
    _Ol52nnMFRTrunkDipAdminState_Type()
)
ol52nnMFRTrunkDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkDipAdminState.setStatus("mandatory")


class _Ol52nnMFRTrunkCableMon_Type(Integer32):
    """Custom type ol52nnMFRTrunkCableMon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Ol52nnMFRTrunkCableMon_Type.__name__ = "Integer32"
_Ol52nnMFRTrunkCableMon_Object = MibTableColumn
ol52nnMFRTrunkCableMon = _Ol52nnMFRTrunkCableMon_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 4),
    _Ol52nnMFRTrunkCableMon_Type()
)
ol52nnMFRTrunkCableMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkCableMon.setStatus("mandatory")


class _Ol52nnMFRTrunkDipCableMon_Type(Integer32):
    """Custom type ol52nnMFRTrunkDipCableMon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Ol52nnMFRTrunkDipCableMon_Type.__name__ = "Integer32"
_Ol52nnMFRTrunkDipCableMon_Object = MibTableColumn
ol52nnMFRTrunkDipCableMon = _Ol52nnMFRTrunkDipCableMon_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 5),
    _Ol52nnMFRTrunkDipCableMon_Type()
)
ol52nnMFRTrunkDipCableMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkDipCableMon.setStatus("mandatory")


class _Ol52nnMFRTrunkCompMode_Type(Integer32):
    """Custom type ol52nnMFRTrunkCompMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Ol52nnMFRTrunkCompMode_Type.__name__ = "Integer32"
_Ol52nnMFRTrunkCompMode_Object = MibTableColumn
ol52nnMFRTrunkCompMode = _Ol52nnMFRTrunkCompMode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 6),
    _Ol52nnMFRTrunkCompMode_Type()
)
ol52nnMFRTrunkCompMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkCompMode.setStatus("mandatory")


class _Ol52nnMFRTrunkDipCompMode_Type(Integer32):
    """Custom type ol52nnMFRTrunkDipCompMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_Ol52nnMFRTrunkDipCompMode_Type.__name__ = "Integer32"
_Ol52nnMFRTrunkDipCompMode_Object = MibTableColumn
ol52nnMFRTrunkDipCompMode = _Ol52nnMFRTrunkDipCompMode_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 7),
    _Ol52nnMFRTrunkDipCompMode_Type()
)
ol52nnMFRTrunkDipCompMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkDipCompMode.setStatus("mandatory")


class _Ol52nnMFRTrunkNetMapState_Type(Integer32):
    """Custom type ol52nnMFRTrunkNetMapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("notApplicable", 1))
    )


_Ol52nnMFRTrunkNetMapState_Type.__name__ = "Integer32"
_Ol52nnMFRTrunkNetMapState_Object = MibTableColumn
ol52nnMFRTrunkNetMapState = _Ol52nnMFRTrunkNetMapState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 8),
    _Ol52nnMFRTrunkNetMapState_Type()
)
ol52nnMFRTrunkNetMapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkNetMapState.setStatus("mandatory")


class _Ol52nnMFRTrunkExtBcnRecovery_Type(Integer32):
    """Custom type ol52nnMFRTrunkExtBcnRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exists", 1),
          ("nonExists", 2),
          ("notApplicable", 3))
    )


_Ol52nnMFRTrunkExtBcnRecovery_Type.__name__ = "Integer32"
_Ol52nnMFRTrunkExtBcnRecovery_Object = MibTableColumn
ol52nnMFRTrunkExtBcnRecovery = _Ol52nnMFRTrunkExtBcnRecovery_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20, 3, 1, 9),
    _Ol52nnMFRTrunkExtBcnRecovery_Type()
)
ol52nnMFRTrunkExtBcnRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMFRTrunkExtBcnRecovery.setStatus("mandatory")
_Ol51nnMTS_ObjectIdentity = ObjectIdentity
ol51nnMTS = _Ol51nnMTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21)
)
_Ol51nnMTSModTable_Object = MibTable
ol51nnMTSModTable = _Ol51nnMTSModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1)
)
if mibBuilder.loadTexts:
    ol51nnMTSModTable.setStatus("mandatory")
_Ol51nnMTSModEntry_Object = MibTableRow
ol51nnMTSModEntry = _Ol51nnMTSModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1, 1)
)
ol51nnMTSModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMTSModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTSModEntry.setStatus("mandatory")
_Ol51nnMTSModSlotIndex_Type = Integer32
_Ol51nnMTSModSlotIndex_Object = MibTableColumn
ol51nnMTSModSlotIndex = _Ol51nnMTSModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1, 1, 1),
    _Ol51nnMTSModSlotIndex_Type()
)
ol51nnMTSModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSModSlotIndex.setStatus("mandatory")
_Ol51nnMTSModProtocols_Type = DisplayString
_Ol51nnMTSModProtocols_Object = MibTableColumn
ol51nnMTSModProtocols = _Ol51nnMTSModProtocols_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1, 1, 2),
    _Ol51nnMTSModProtocols_Type()
)
ol51nnMTSModProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSModProtocols.setStatus("mandatory")
_Ol51nnMTSModIpAddress_Type = IpAddress
_Ol51nnMTSModIpAddress_Object = MibTableColumn
ol51nnMTSModIpAddress = _Ol51nnMTSModIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1, 1, 3),
    _Ol51nnMTSModIpAddress_Type()
)
ol51nnMTSModIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSModIpAddress.setStatus("mandatory")
_Ol51nnMTSModTCPPort_Type = Integer32
_Ol51nnMTSModTCPPort_Object = MibTableColumn
ol51nnMTSModTCPPort = _Ol51nnMTSModTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1, 1, 4),
    _Ol51nnMTSModTCPPort_Type()
)
ol51nnMTSModTCPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSModTCPPort.setStatus("mandatory")


class _Ol51nnMTSModStationAddr_Type(OctetString):
    """Custom type ol51nnMTSModStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol51nnMTSModStationAddr_Type.__name__ = "OctetString"
_Ol51nnMTSModStationAddr_Object = MibTableColumn
ol51nnMTSModStationAddr = _Ol51nnMTSModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1, 1, 5),
    _Ol51nnMTSModStationAddr_Type()
)
ol51nnMTSModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSModStationAddr.setStatus("mandatory")


class _Ol51nnMTSModDipNetwork_Type(Integer32):
    """Custom type ol51nnMTSModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMTSModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMTSModDipNetwork_Object = MibTableColumn
ol51nnMTSModDipNetwork = _Ol51nnMTSModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1, 1, 6),
    _Ol51nnMTSModDipNetwork_Type()
)
ol51nnMTSModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSModDipNetwork.setStatus("mandatory")


class _Ol51nnMTSModCPURev_Type(DisplayString):
    """Custom type ol51nnMTSModCPURev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Ol51nnMTSModCPURev_Type.__name__ = "DisplayString"
_Ol51nnMTSModCPURev_Object = MibTableColumn
ol51nnMTSModCPURev = _Ol51nnMTSModCPURev_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 1, 1, 7),
    _Ol51nnMTSModCPURev_Type()
)
ol51nnMTSModCPURev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSModCPURev.setStatus("mandatory")
_Ol51nnMTSPortTable_Object = MibTable
ol51nnMTSPortTable = _Ol51nnMTSPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 2)
)
if mibBuilder.loadTexts:
    ol51nnMTSPortTable.setStatus("mandatory")
_Ol51nnMTSPortEntry_Object = MibTableRow
ol51nnMTSPortEntry = _Ol51nnMTSPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 2, 1)
)
ol51nnMTSPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMTSPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnMTSPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTSPortEntry.setStatus("mandatory")
_Ol51nnMTSPortSlotIndex_Type = Integer32
_Ol51nnMTSPortSlotIndex_Object = MibTableColumn
ol51nnMTSPortSlotIndex = _Ol51nnMTSPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 2, 1, 1),
    _Ol51nnMTSPortSlotIndex_Type()
)
ol51nnMTSPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSPortSlotIndex.setStatus("mandatory")
_Ol51nnMTSPortIndex_Type = Integer32
_Ol51nnMTSPortIndex_Object = MibTableColumn
ol51nnMTSPortIndex = _Ol51nnMTSPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 2, 1, 2),
    _Ol51nnMTSPortIndex_Type()
)
ol51nnMTSPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSPortIndex.setStatus("mandatory")


class _Ol51nnMTSPortAdminState_Type(Integer32):
    """Custom type ol51nnMTSPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("local", 6),
          ("remote", 7))
    )


_Ol51nnMTSPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMTSPortAdminState_Object = MibTableColumn
ol51nnMTSPortAdminState = _Ol51nnMTSPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 2, 1, 3),
    _Ol51nnMTSPortAdminState_Type()
)
ol51nnMTSPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTSPortAdminState.setStatus("mandatory")


class _Ol51nnMTSPortOperState_Type(Integer32):
    """Custom type ol51nnMTSPortOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 3),
          ("idle", 1),
          ("local", 2))
    )


_Ol51nnMTSPortOperState_Type.__name__ = "Integer32"
_Ol51nnMTSPortOperState_Object = MibTableColumn
ol51nnMTSPortOperState = _Ol51nnMTSPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21, 2, 1, 4),
    _Ol51nnMTSPortOperState_Type()
)
ol51nnMTSPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTSPortOperState.setStatus("mandatory")
_Ol51nnMFL_ObjectIdentity = ObjectIdentity
ol51nnMFL = _Ol51nnMFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22)
)
_Ol51nnMFLModTable_Object = MibTable
ol51nnMFLModTable = _Ol51nnMFLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 1)
)
if mibBuilder.loadTexts:
    ol51nnMFLModTable.setStatus("mandatory")
_Ol51nnMFLModEntry_Object = MibTableRow
ol51nnMFLModEntry = _Ol51nnMFLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 1, 1)
)
ol51nnMFLModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMFLModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFLModEntry.setStatus("mandatory")
_Ol51nnMFLModSlotIndex_Type = Integer32
_Ol51nnMFLModSlotIndex_Object = MibTableColumn
ol51nnMFLModSlotIndex = _Ol51nnMFLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 1, 1, 1),
    _Ol51nnMFLModSlotIndex_Type()
)
ol51nnMFLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFLModSlotIndex.setStatus("mandatory")


class _Ol51nnMFLModDipNetwork_Type(Integer32):
    """Custom type ol51nnMFLModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMFLModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMFLModDipNetwork_Object = MibTableColumn
ol51nnMFLModDipNetwork = _Ol51nnMFLModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 1, 1, 2),
    _Ol51nnMFLModDipNetwork_Type()
)
ol51nnMFLModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFLModDipNetwork.setStatus("mandatory")
_Ol51nnMFLPortTable_Object = MibTable
ol51nnMFLPortTable = _Ol51nnMFLPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 2)
)
if mibBuilder.loadTexts:
    ol51nnMFLPortTable.setStatus("mandatory")
_Ol51nnMFLPortEntry_Object = MibTableRow
ol51nnMFLPortEntry = _Ol51nnMFLPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 2, 1)
)
ol51nnMFLPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMFLPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnMFLPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFLPortEntry.setStatus("mandatory")
_Ol51nnMFLPortSlotIndex_Type = Integer32
_Ol51nnMFLPortSlotIndex_Object = MibTableColumn
ol51nnMFLPortSlotIndex = _Ol51nnMFLPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 2, 1, 1),
    _Ol51nnMFLPortSlotIndex_Type()
)
ol51nnMFLPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFLPortSlotIndex.setStatus("mandatory")
_Ol51nnMFLPortIndex_Type = Integer32
_Ol51nnMFLPortIndex_Object = MibTableColumn
ol51nnMFLPortIndex = _Ol51nnMFLPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 2, 1, 2),
    _Ol51nnMFLPortIndex_Type()
)
ol51nnMFLPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFLPortIndex.setStatus("mandatory")


class _Ol51nnMFLPortAdminState_Type(Integer32):
    """Custom type ol51nnMFLPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3),
          ("redundant-rfs", 5))
    )


_Ol51nnMFLPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMFLPortAdminState_Object = MibTableColumn
ol51nnMFLPortAdminState = _Ol51nnMFLPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 2, 1, 3),
    _Ol51nnMFLPortAdminState_Type()
)
ol51nnMFLPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFLPortAdminState.setStatus("mandatory")
_Ol51nnMFLPortBuddySlot_Type = Integer32
_Ol51nnMFLPortBuddySlot_Object = MibTableColumn
ol51nnMFLPortBuddySlot = _Ol51nnMFLPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 2, 1, 4),
    _Ol51nnMFLPortBuddySlot_Type()
)
ol51nnMFLPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFLPortBuddySlot.setStatus("mandatory")
_Ol51nnMFLPortBuddyPort_Type = Integer32
_Ol51nnMFLPortBuddyPort_Object = MibTableColumn
ol51nnMFLPortBuddyPort = _Ol51nnMFLPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 2, 1, 5),
    _Ol51nnMFLPortBuddyPort_Type()
)
ol51nnMFLPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFLPortBuddyPort.setStatus("mandatory")


class _Ol51nnMFLPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMFLPortDipAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3),
          ("redundant-rfs", 5))
    )


_Ol51nnMFLPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMFLPortDipAdminState_Object = MibTableColumn
ol51nnMFLPortDipAdminState = _Ol51nnMFLPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22, 2, 1, 6),
    _Ol51nnMFLPortDipAdminState_Type()
)
ol51nnMFLPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFLPortDipAdminState.setStatus("mandatory")
_Ol50nnMRCTL_ObjectIdentity = ObjectIdentity
ol50nnMRCTL = _Ol50nnMRCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23)
)
_Ol50nnMRCTLModTable_Object = MibTable
ol50nnMRCTLModTable = _Ol50nnMRCTLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23, 1)
)
if mibBuilder.loadTexts:
    ol50nnMRCTLModTable.setStatus("mandatory")
_Ol50nnMRCTLModEntry_Object = MibTableRow
ol50nnMRCTLModEntry = _Ol50nnMRCTLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23, 1, 1)
)
ol50nnMRCTLModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol50nnMRCTLModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol50nnMRCTLModEntry.setStatus("mandatory")
_Ol50nnMRCTLModSlotIndex_Type = Integer32
_Ol50nnMRCTLModSlotIndex_Object = MibTableColumn
ol50nnMRCTLModSlotIndex = _Ol50nnMRCTLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23, 1, 1, 1),
    _Ol50nnMRCTLModSlotIndex_Type()
)
ol50nnMRCTLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMRCTLModSlotIndex.setStatus("mandatory")


class _Ol50nnMRCTLModOperState_Type(Integer32):
    """Custom type ol50nnMRCTLModOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_Ol50nnMRCTLModOperState_Type.__name__ = "Integer32"
_Ol50nnMRCTLModOperState_Object = MibTableColumn
ol50nnMRCTLModOperState = _Ol50nnMRCTLModOperState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23, 1, 1, 2),
    _Ol50nnMRCTLModOperState_Type()
)
ol50nnMRCTLModOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMRCTLModOperState.setStatus("mandatory")


class _Ol50nnMRCTLModClockStatus_Type(Integer32):
    """Custom type ol50nnMRCTLModClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("okay", 1))
    )


_Ol50nnMRCTLModClockStatus_Type.__name__ = "Integer32"
_Ol50nnMRCTLModClockStatus_Object = MibTableColumn
ol50nnMRCTLModClockStatus = _Ol50nnMRCTLModClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23, 1, 1, 3),
    _Ol50nnMRCTLModClockStatus_Type()
)
ol50nnMRCTLModClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMRCTLModClockStatus.setStatus("mandatory")


class _Ol50nnMRCTLModTempStatus_Type(Integer32):
    """Custom type ol50nnMRCTLModTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extremeTemp", 2),
          ("okay", 1))
    )


_Ol50nnMRCTLModTempStatus_Type.__name__ = "Integer32"
_Ol50nnMRCTLModTempStatus_Object = MibTableColumn
ol50nnMRCTLModTempStatus = _Ol50nnMRCTLModTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23, 1, 1, 4),
    _Ol50nnMRCTLModTempStatus_Type()
)
ol50nnMRCTLModTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMRCTLModTempStatus.setStatus("mandatory")
_Ol51nnMFB_ObjectIdentity = ObjectIdentity
ol51nnMFB = _Ol51nnMFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24)
)
_Ol51nnMFBModTable_Object = MibTable
ol51nnMFBModTable = _Ol51nnMFBModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 1)
)
if mibBuilder.loadTexts:
    ol51nnMFBModTable.setStatus("mandatory")
_Ol51nnMFBModEntry_Object = MibTableRow
ol51nnMFBModEntry = _Ol51nnMFBModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 1, 1)
)
ol51nnMFBModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMFBModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFBModEntry.setStatus("mandatory")
_Ol51nnMFBModSlotIndex_Type = Integer32
_Ol51nnMFBModSlotIndex_Object = MibTableColumn
ol51nnMFBModSlotIndex = _Ol51nnMFBModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 1, 1, 1),
    _Ol51nnMFBModSlotIndex_Type()
)
ol51nnMFBModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBModSlotIndex.setStatus("mandatory")


class _Ol51nnMFBModDipNetwork_Type(Integer32):
    """Custom type ol51nnMFBModDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated", 2))
    )


_Ol51nnMFBModDipNetwork_Type.__name__ = "Integer32"
_Ol51nnMFBModDipNetwork_Object = MibTableColumn
ol51nnMFBModDipNetwork = _Ol51nnMFBModDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 1, 1, 2),
    _Ol51nnMFBModDipNetwork_Type()
)
ol51nnMFBModDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBModDipNetwork.setStatus("mandatory")


class _Ol51nnMFBModLLW_Type(Integer32):
    """Custom type ol51nnMFBModLLW based on Integer32"""
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


_Ol51nnMFBModLLW_Type.__name__ = "Integer32"
_Ol51nnMFBModLLW_Object = MibTableColumn
ol51nnMFBModLLW = _Ol51nnMFBModLLW_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 1, 1, 3),
    _Ol51nnMFBModLLW_Type()
)
ol51nnMFBModLLW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBModLLW.setStatus("mandatory")


class _Ol51nnMFBModDipLLW_Type(Integer32):
    """Custom type ol51nnMFBModDipLLW based on Integer32"""
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


_Ol51nnMFBModDipLLW_Type.__name__ = "Integer32"
_Ol51nnMFBModDipLLW_Object = MibTableColumn
ol51nnMFBModDipLLW = _Ol51nnMFBModDipLLW_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 1, 1, 4),
    _Ol51nnMFBModDipLLW_Type()
)
ol51nnMFBModDipLLW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBModDipLLW.setStatus("mandatory")
_Ol51nnMFBPortTable_Object = MibTable
ol51nnMFBPortTable = _Ol51nnMFBPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 2)
)
if mibBuilder.loadTexts:
    ol51nnMFBPortTable.setStatus("mandatory")
_Ol51nnMFBPortEntry_Object = MibTableRow
ol51nnMFBPortEntry = _Ol51nnMFBPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 2, 1)
)
ol51nnMFBPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMFBPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnMFBPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMFBPortEntry.setStatus("mandatory")
_Ol51nnMFBPortSlotIndex_Type = Integer32
_Ol51nnMFBPortSlotIndex_Object = MibTableColumn
ol51nnMFBPortSlotIndex = _Ol51nnMFBPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 2, 1, 1),
    _Ol51nnMFBPortSlotIndex_Type()
)
ol51nnMFBPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPortSlotIndex.setStatus("mandatory")
_Ol51nnMFBPortIndex_Type = Integer32
_Ol51nnMFBPortIndex_Object = MibTableColumn
ol51nnMFBPortIndex = _Ol51nnMFBPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 2, 1, 2),
    _Ol51nnMFBPortIndex_Type()
)
ol51nnMFBPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPortIndex.setStatus("mandatory")


class _Ol51nnMFBPortAdminState_Type(Integer32):
    """Custom type ol51nnMFBPortAdminState based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3))
    )


_Ol51nnMFBPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMFBPortAdminState_Object = MibTableColumn
ol51nnMFBPortAdminState = _Ol51nnMFBPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 2, 1, 3),
    _Ol51nnMFBPortAdminState_Type()
)
ol51nnMFBPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBPortAdminState.setStatus("mandatory")
_Ol51nnMFBPortBuddySlot_Type = Integer32
_Ol51nnMFBPortBuddySlot_Object = MibTableColumn
ol51nnMFBPortBuddySlot = _Ol51nnMFBPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 2, 1, 4),
    _Ol51nnMFBPortBuddySlot_Type()
)
ol51nnMFBPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBPortBuddySlot.setStatus("mandatory")
_Ol51nnMFBPortBuddyPort_Type = Integer32
_Ol51nnMFBPortBuddyPort_Object = MibTableColumn
ol51nnMFBPortBuddyPort = _Ol51nnMFBPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 2, 1, 5),
    _Ol51nnMFBPortBuddyPort_Type()
)
ol51nnMFBPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMFBPortBuddyPort.setStatus("mandatory")


class _Ol51nnMFBPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMFBPortDipAdminState based on Integer32"""
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


_Ol51nnMFBPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMFBPortDipAdminState_Object = MibTableColumn
ol51nnMFBPortDipAdminState = _Ol51nnMFBPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24, 2, 1, 6),
    _Ol51nnMFBPortDipAdminState_Type()
)
ol51nnMFBPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMFBPortDipAdminState.setStatus("mandatory")
_Ol53nnMMGT_ObjectIdentity = ObjectIdentity
ol53nnMMGT = _Ol53nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25)
)
_Ol53nnMMGTModTable_Object = MibTable
ol53nnMMGTModTable = _Ol53nnMMGTModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1)
)
if mibBuilder.loadTexts:
    ol53nnMMGTModTable.setStatus("mandatory")
_Ol53nnMMGTModEntry_Object = MibTableRow
ol53nnMMGTModEntry = _Ol53nnMMGTModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1)
)
ol53nnMMGTModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol53nnMMGTModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMMGTModEntry.setStatus("mandatory")
_Ol53nnMMGTModSlotIndex_Type = Integer32
_Ol53nnMMGTModSlotIndex_Object = MibTableColumn
ol53nnMMGTModSlotIndex = _Ol53nnMMGTModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 1),
    _Ol53nnMMGTModSlotIndex_Type()
)
ol53nnMMGTModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModSlotIndex.setStatus("mandatory")


class _Ol53nnMMGTModMasterPriority_Type(Integer32):
    """Custom type ol53nnMMGTModMasterPriority based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("four", 4),
          ("nine", 9),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("ten", 10),
          ("three", 3),
          ("two", 2))
    )


_Ol53nnMMGTModMasterPriority_Type.__name__ = "Integer32"
_Ol53nnMMGTModMasterPriority_Object = MibTableColumn
ol53nnMMGTModMasterPriority = _Ol53nnMMGTModMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 2),
    _Ol53nnMMGTModMasterPriority_Type()
)
ol53nnMMGTModMasterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol53nnMMGTModMasterPriority.setStatus("mandatory")


class _Ol53nnMMGTModMasterStatus_Type(Integer32):
    """Custom type ol53nnMMGTModMasterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("electing", 3),
          ("master", 1),
          ("non-master", 2))
    )


_Ol53nnMMGTModMasterStatus_Type.__name__ = "Integer32"
_Ol53nnMMGTModMasterStatus_Object = MibTableColumn
ol53nnMMGTModMasterStatus = _Ol53nnMMGTModMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 3),
    _Ol53nnMMGTModMasterStatus_Type()
)
ol53nnMMGTModMasterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModMasterStatus.setStatus("mandatory")


class _Ol53nnMMGTModStationAddr_Type(OctetString):
    """Custom type ol53nnMMGTModStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol53nnMMGTModStationAddr_Type.__name__ = "OctetString"
_Ol53nnMMGTModStationAddr_Object = MibTableColumn
ol53nnMMGTModStationAddr = _Ol53nnMMGTModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 4),
    _Ol53nnMMGTModStationAddr_Type()
)
ol53nnMMGTModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModStationAddr.setStatus("mandatory")
_Ol53nnMMGTModIpAddress_Type = IpAddress
_Ol53nnMMGTModIpAddress_Object = MibTableColumn
ol53nnMMGTModIpAddress = _Ol53nnMMGTModIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 5),
    _Ol53nnMMGTModIpAddress_Type()
)
ol53nnMMGTModIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol53nnMMGTModIpAddress.setStatus("mandatory")


class _Ol53nnMMGTModDownStreamMAC_Type(OctetString):
    """Custom type ol53nnMMGTModDownStreamMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol53nnMMGTModDownStreamMAC_Type.__name__ = "OctetString"
_Ol53nnMMGTModDownStreamMAC_Object = MibTableColumn
ol53nnMMGTModDownStreamMAC = _Ol53nnMMGTModDownStreamMAC_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 6),
    _Ol53nnMMGTModDownStreamMAC_Type()
)
ol53nnMMGTModDownStreamMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModDownStreamMAC.setStatus("mandatory")


class _Ol53nnMMGTModUpStreamMAC_Type(OctetString):
    """Custom type ol53nnMMGTModUpStreamMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol53nnMMGTModUpStreamMAC_Type.__name__ = "OctetString"
_Ol53nnMMGTModUpStreamMAC_Object = MibTableColumn
ol53nnMMGTModUpStreamMAC = _Ol53nnMMGTModUpStreamMAC_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 7),
    _Ol53nnMMGTModUpStreamMAC_Type()
)
ol53nnMMGTModUpStreamMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModUpStreamMAC.setStatus("mandatory")


class _Ol53nnMMGTModfddiMACPath_Type(Integer32):
    """Custom type ol53nnMMGTModfddiMACPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_Ol53nnMMGTModfddiMACPath_Type.__name__ = "Integer32"
_Ol53nnMMGTModfddiMACPath_Object = MibTableColumn
ol53nnMMGTModfddiMACPath = _Ol53nnMMGTModfddiMACPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 8),
    _Ol53nnMMGTModfddiMACPath_Type()
)
ol53nnMMGTModfddiMACPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol53nnMMGTModfddiMACPath.setStatus("mandatory")


class _Ol53nnMMGTModDownStreamModule_Type(Integer32):
    """Custom type ol53nnMMGTModDownStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMMGTModDownStreamModule_Type.__name__ = "Integer32"
_Ol53nnMMGTModDownStreamModule_Object = MibTableColumn
ol53nnMMGTModDownStreamModule = _Ol53nnMMGTModDownStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 9),
    _Ol53nnMMGTModDownStreamModule_Type()
)
ol53nnMMGTModDownStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModDownStreamModule.setStatus("mandatory")


class _Ol53nnMMGTModUpStreamModule_Type(Integer32):
    """Custom type ol53nnMMGTModUpStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMMGTModUpStreamModule_Type.__name__ = "Integer32"
_Ol53nnMMGTModUpStreamModule_Object = MibTableColumn
ol53nnMMGTModUpStreamModule = _Ol53nnMMGTModUpStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 10),
    _Ol53nnMMGTModUpStreamModule_Type()
)
ol53nnMMGTModUpStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModUpStreamModule.setStatus("mandatory")


class _Ol53nnMMGTModDownStreamOperPath_Type(Integer32):
    """Custom type ol53nnMMGTModDownStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMMGTModDownStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMMGTModDownStreamOperPath_Object = MibTableColumn
ol53nnMMGTModDownStreamOperPath = _Ol53nnMMGTModDownStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 11),
    _Ol53nnMMGTModDownStreamOperPath_Type()
)
ol53nnMMGTModDownStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModDownStreamOperPath.setStatus("mandatory")


class _Ol53nnMMGTModUpStreamOperPath_Type(Integer32):
    """Custom type ol53nnMMGTModUpStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMMGTModUpStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMMGTModUpStreamOperPath_Object = MibTableColumn
ol53nnMMGTModUpStreamOperPath = _Ol53nnMMGTModUpStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 12),
    _Ol53nnMMGTModUpStreamOperPath_Type()
)
ol53nnMMGTModUpStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModUpStreamOperPath.setStatus("mandatory")


class _Ol53nnMMGTModRingInfo_Type(OctetString):
    """Custom type ol53nnMMGTModRingInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Ol53nnMMGTModRingInfo_Type.__name__ = "OctetString"
_Ol53nnMMGTModRingInfo_Object = MibTableColumn
ol53nnMMGTModRingInfo = _Ol53nnMMGTModRingInfo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 1, 1, 13),
    _Ol53nnMMGTModRingInfo_Type()
)
ol53nnMMGTModRingInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTModRingInfo.setStatus("mandatory")
_Ol53nnMMGTPortTable_Object = MibTable
ol53nnMMGTPortTable = _Ol53nnMMGTPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2)
)
if mibBuilder.loadTexts:
    ol53nnMMGTPortTable.setStatus("mandatory")
_Ol53nnMMGTPortEntry_Object = MibTableRow
ol53nnMMGTPortEntry = _Ol53nnMMGTPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1)
)
ol53nnMMGTPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol53nnMMGTPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol53nnMMGTPortIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMMGTPortEntry.setStatus("mandatory")
_Ol53nnMMGTPortSlotIndex_Type = Integer32
_Ol53nnMMGTPortSlotIndex_Object = MibTableColumn
ol53nnMMGTPortSlotIndex = _Ol53nnMMGTPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 1),
    _Ol53nnMMGTPortSlotIndex_Type()
)
ol53nnMMGTPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortSlotIndex.setStatus("mandatory")
_Ol53nnMMGTPortIndex_Type = Integer32
_Ol53nnMMGTPortIndex_Object = MibTableColumn
ol53nnMMGTPortIndex = _Ol53nnMMGTPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 2),
    _Ol53nnMMGTPortIndex_Type()
)
ol53nnMMGTPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortIndex.setStatus("mandatory")


class _Ol53nnMMGTPortConfig_Type(Integer32):
    """Custom type ol53nnMMGTPortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )


_Ol53nnMMGTPortConfig_Type.__name__ = "Integer32"
_Ol53nnMMGTPortConfig_Object = MibTableColumn
ol53nnMMGTPortConfig = _Ol53nnMMGTPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 3),
    _Ol53nnMMGTPortConfig_Type()
)
ol53nnMMGTPortConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortConfig.setStatus("mandatory")


class _Ol53nnMMGTPortPcmState_Type(Integer32):
    """Custom type ol53nnMMGTPortPcmState based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("pc0", 1),
          ("pc1", 2),
          ("pc2", 3),
          ("pc3", 4),
          ("pc4", 5),
          ("pc5", 6),
          ("pc6", 7),
          ("pc7", 8),
          ("pc8", 9),
          ("pc9", 10))
    )


_Ol53nnMMGTPortPcmState_Type.__name__ = "Integer32"
_Ol53nnMMGTPortPcmState_Object = MibTableColumn
ol53nnMMGTPortPcmState = _Ol53nnMMGTPortPcmState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 4),
    _Ol53nnMMGTPortPcmState_Type()
)
ol53nnMMGTPortPcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortPcmState.setStatus("mandatory")


class _Ol53nnMMGTPortConnectState_Type(Integer32):
    """Custom type ol53nnMMGTPortConnectState based on Integer32"""
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
        *(("active", 4),
          ("connecting", 2),
          ("disabled", 1),
          ("standby", 3))
    )


_Ol53nnMMGTPortConnectState_Type.__name__ = "Integer32"
_Ol53nnMMGTPortConnectState_Object = MibTableColumn
ol53nnMMGTPortConnectState = _Ol53nnMMGTPortConnectState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 5),
    _Ol53nnMMGTPortConnectState_Type()
)
ol53nnMMGTPortConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortConnectState.setStatus("mandatory")


class _Ol53nnMMGTPortNeighbor_Type(Integer32):
    """Custom type ol53nnMMGTPortNeighbor based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("master", 4),
          ("slave", 3),
          ("unknown", 5))
    )


_Ol53nnMMGTPortNeighbor_Type.__name__ = "Integer32"
_Ol53nnMMGTPortNeighbor_Object = MibTableColumn
ol53nnMMGTPortNeighbor = _Ol53nnMMGTPortNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 6),
    _Ol53nnMMGTPortNeighbor_Type()
)
ol53nnMMGTPortNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortNeighbor.setStatus("mandatory")


class _Ol53nnMMGTPortRemoteMACIndicated_Type(Integer32):
    """Custom type ol53nnMMGTPortRemoteMACIndicated based on Integer32"""
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


_Ol53nnMMGTPortRemoteMACIndicated_Type.__name__ = "Integer32"
_Ol53nnMMGTPortRemoteMACIndicated_Object = MibTableColumn
ol53nnMMGTPortRemoteMACIndicated = _Ol53nnMMGTPortRemoteMACIndicated_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 7),
    _Ol53nnMMGTPortRemoteMACIndicated_Type()
)
ol53nnMMGTPortRemoteMACIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortRemoteMACIndicated.setStatus("mandatory")


class _Ol53nnMMGTPortBSFlag_Type(Integer32):
    """Custom type ol53nnMMGTPortBSFlag based on Integer32"""
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


_Ol53nnMMGTPortBSFlag_Type.__name__ = "Integer32"
_Ol53nnMMGTPortBSFlag_Object = MibTableColumn
ol53nnMMGTPortBSFlag = _Ol53nnMMGTPortBSFlag_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 8),
    _Ol53nnMMGTPortBSFlag_Type()
)
ol53nnMMGTPortBSFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortBSFlag.setStatus("mandatory")


class _Ol53nnMMGTPortPCWithhold_Type(Integer32):
    """Custom type ol53nnMMGTPortPCWithhold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("m-m", 2),
          ("none", 1),
          ("other", 3))
    )


_Ol53nnMMGTPortPCWithhold_Type.__name__ = "Integer32"
_Ol53nnMMGTPortPCWithhold_Object = MibTableColumn
ol53nnMMGTPortPCWithhold = _Ol53nnMMGTPortPCWithhold_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 9),
    _Ol53nnMMGTPortPCWithhold_Type()
)
ol53nnMMGTPortPCWithhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortPCWithhold.setStatus("mandatory")


class _Ol53nnMMGTPortLerCondition_Type(Integer32):
    """Custom type ol53nnMMGTPortLerCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("okay", 2))
    )


_Ol53nnMMGTPortLerCondition_Type.__name__ = "Integer32"
_Ol53nnMMGTPortLerCondition_Object = MibTableColumn
ol53nnMMGTPortLerCondition = _Ol53nnMMGTPortLerCondition_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 2, 1, 10),
    _Ol53nnMMGTPortLerCondition_Type()
)
ol53nnMMGTPortLerCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTPortLerCondition.setStatus("mandatory")
_Ol53nnMMGTTrunkTable_Object = MibTable
ol53nnMMGTTrunkTable = _Ol53nnMMGTTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 3)
)
if mibBuilder.loadTexts:
    ol53nnMMGTTrunkTable.setStatus("mandatory")
_Ol53nnMMGTTrunkEntry_Object = MibTableRow
ol53nnMMGTTrunkEntry = _Ol53nnMMGTTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 3, 1)
)
ol53nnMMGTTrunkEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol53nnMMGTTrunkSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol53nnMMGTTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMMGTTrunkEntry.setStatus("mandatory")
_Ol53nnMMGTTrunkSlotIndex_Type = Integer32
_Ol53nnMMGTTrunkSlotIndex_Object = MibTableColumn
ol53nnMMGTTrunkSlotIndex = _Ol53nnMMGTTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 3, 1, 1),
    _Ol53nnMMGTTrunkSlotIndex_Type()
)
ol53nnMMGTTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTTrunkSlotIndex.setStatus("mandatory")
_Ol53nnMMGTTrunkIndex_Type = Integer32
_Ol53nnMMGTTrunkIndex_Object = MibTableColumn
ol53nnMMGTTrunkIndex = _Ol53nnMMGTTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25, 3, 1, 2),
    _Ol53nnMMGTTrunkIndex_Type()
)
ol53nnMMGTTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMMGTTrunkIndex.setStatus("mandatory")
_Ol53nnMFBMIC_ObjectIdentity = ObjectIdentity
ol53nnMFBMIC = _Ol53nnMFBMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26)
)
_Ol53nnMFBMICModTable_Object = MibTable
ol53nnMFBMICModTable = _Ol53nnMFBMICModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 1)
)
if mibBuilder.loadTexts:
    ol53nnMFBMICModTable.setStatus("mandatory")
_Ol53nnMFBMICModEntry_Object = MibTableRow
ol53nnMFBMICModEntry = _Ol53nnMFBMICModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 1, 1)
)
ol53nnMFBMICModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol53nnMFBMICModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMFBMICModEntry.setStatus("mandatory")
_Ol53nnMFBMICModSlotIndex_Type = Integer32
_Ol53nnMFBMICModSlotIndex_Object = MibTableColumn
ol53nnMFBMICModSlotIndex = _Ol53nnMFBMICModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 1, 1, 1),
    _Ol53nnMFBMICModSlotIndex_Type()
)
ol53nnMFBMICModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICModSlotIndex.setStatus("mandatory")


class _Ol53nnMFBMICModDownStreamModule_Type(Integer32):
    """Custom type ol53nnMFBMICModDownStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMFBMICModDownStreamModule_Type.__name__ = "Integer32"
_Ol53nnMFBMICModDownStreamModule_Object = MibTableColumn
ol53nnMFBMICModDownStreamModule = _Ol53nnMFBMICModDownStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 1, 1, 2),
    _Ol53nnMFBMICModDownStreamModule_Type()
)
ol53nnMFBMICModDownStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICModDownStreamModule.setStatus("mandatory")


class _Ol53nnMFBMICModUpStreamModule_Type(Integer32):
    """Custom type ol53nnMFBMICModUpStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMFBMICModUpStreamModule_Type.__name__ = "Integer32"
_Ol53nnMFBMICModUpStreamModule_Object = MibTableColumn
ol53nnMFBMICModUpStreamModule = _Ol53nnMFBMICModUpStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 1, 1, 3),
    _Ol53nnMFBMICModUpStreamModule_Type()
)
ol53nnMFBMICModUpStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICModUpStreamModule.setStatus("mandatory")


class _Ol53nnMFBMICModDownStreamOperPath_Type(Integer32):
    """Custom type ol53nnMFBMICModDownStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMFBMICModDownStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMFBMICModDownStreamOperPath_Object = MibTableColumn
ol53nnMFBMICModDownStreamOperPath = _Ol53nnMFBMICModDownStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 1, 1, 4),
    _Ol53nnMFBMICModDownStreamOperPath_Type()
)
ol53nnMFBMICModDownStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICModDownStreamOperPath.setStatus("mandatory")


class _Ol53nnMFBMICModUpStreamOperPath_Type(Integer32):
    """Custom type ol53nnMFBMICModUpStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMFBMICModUpStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMFBMICModUpStreamOperPath_Object = MibTableColumn
ol53nnMFBMICModUpStreamOperPath = _Ol53nnMFBMICModUpStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 1, 1, 5),
    _Ol53nnMFBMICModUpStreamOperPath_Type()
)
ol53nnMFBMICModUpStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICModUpStreamOperPath.setStatus("mandatory")


class _Ol53nnMFBMICModRingInfo_Type(OctetString):
    """Custom type ol53nnMFBMICModRingInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Ol53nnMFBMICModRingInfo_Type.__name__ = "OctetString"
_Ol53nnMFBMICModRingInfo_Object = MibTableColumn
ol53nnMFBMICModRingInfo = _Ol53nnMFBMICModRingInfo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 1, 1, 6),
    _Ol53nnMFBMICModRingInfo_Type()
)
ol53nnMFBMICModRingInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICModRingInfo.setStatus("mandatory")
_Ol53nnMFBMICPortTable_Object = MibTable
ol53nnMFBMICPortTable = _Ol53nnMFBMICPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2)
)
if mibBuilder.loadTexts:
    ol53nnMFBMICPortTable.setStatus("mandatory")
_Ol53nnMFBMICPortEntry_Object = MibTableRow
ol53nnMFBMICPortEntry = _Ol53nnMFBMICPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1)
)
ol53nnMFBMICPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol53nnMFBMICPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol53nnMFBMICPortIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMFBMICPortEntry.setStatus("mandatory")
_Ol53nnMFBMICPortSlotIndex_Type = Integer32
_Ol53nnMFBMICPortSlotIndex_Object = MibTableColumn
ol53nnMFBMICPortSlotIndex = _Ol53nnMFBMICPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 1),
    _Ol53nnMFBMICPortSlotIndex_Type()
)
ol53nnMFBMICPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortSlotIndex.setStatus("mandatory")
_Ol53nnMFBMICPortIndex_Type = Integer32
_Ol53nnMFBMICPortIndex_Object = MibTableColumn
ol53nnMFBMICPortIndex = _Ol53nnMFBMICPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 2),
    _Ol53nnMFBMICPortIndex_Type()
)
ol53nnMFBMICPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortIndex.setStatus("mandatory")


class _Ol53nnMFBMICPortConfig_Type(Integer32):
    """Custom type ol53nnMFBMICPortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("master", 4),
          ("slave", 3))
    )


_Ol53nnMFBMICPortConfig_Type.__name__ = "Integer32"
_Ol53nnMFBMICPortConfig_Object = MibTableColumn
ol53nnMFBMICPortConfig = _Ol53nnMFBMICPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 3),
    _Ol53nnMFBMICPortConfig_Type()
)
ol53nnMFBMICPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortConfig.setStatus("mandatory")


class _Ol53nnMFBMICPortPcmState_Type(Integer32):
    """Custom type ol53nnMFBMICPortPcmState based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("pc0", 1),
          ("pc1", 2),
          ("pc2", 3),
          ("pc3", 4),
          ("pc4", 5),
          ("pc5", 6),
          ("pc6", 7),
          ("pc7", 8),
          ("pc8", 9),
          ("pc9", 10))
    )


_Ol53nnMFBMICPortPcmState_Type.__name__ = "Integer32"
_Ol53nnMFBMICPortPcmState_Object = MibTableColumn
ol53nnMFBMICPortPcmState = _Ol53nnMFBMICPortPcmState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 4),
    _Ol53nnMFBMICPortPcmState_Type()
)
ol53nnMFBMICPortPcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortPcmState.setStatus("mandatory")


class _Ol53nnMFBMICPortConnectState_Type(Integer32):
    """Custom type ol53nnMFBMICPortConnectState based on Integer32"""
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
        *(("active", 4),
          ("connecting", 2),
          ("disabled", 1),
          ("standby", 3))
    )


_Ol53nnMFBMICPortConnectState_Type.__name__ = "Integer32"
_Ol53nnMFBMICPortConnectState_Object = MibTableColumn
ol53nnMFBMICPortConnectState = _Ol53nnMFBMICPortConnectState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 5),
    _Ol53nnMFBMICPortConnectState_Type()
)
ol53nnMFBMICPortConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortConnectState.setStatus("mandatory")


class _Ol53nnMFBMICPortNeighbor_Type(Integer32):
    """Custom type ol53nnMFBMICPortNeighbor based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("master", 4),
          ("slave", 3),
          ("unknown", 5))
    )


_Ol53nnMFBMICPortNeighbor_Type.__name__ = "Integer32"
_Ol53nnMFBMICPortNeighbor_Object = MibTableColumn
ol53nnMFBMICPortNeighbor = _Ol53nnMFBMICPortNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 6),
    _Ol53nnMFBMICPortNeighbor_Type()
)
ol53nnMFBMICPortNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortNeighbor.setStatus("mandatory")


class _Ol53nnMFBMICPortRemoteMACIndicated_Type(Integer32):
    """Custom type ol53nnMFBMICPortRemoteMACIndicated based on Integer32"""
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


_Ol53nnMFBMICPortRemoteMACIndicated_Type.__name__ = "Integer32"
_Ol53nnMFBMICPortRemoteMACIndicated_Object = MibTableColumn
ol53nnMFBMICPortRemoteMACIndicated = _Ol53nnMFBMICPortRemoteMACIndicated_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 7),
    _Ol53nnMFBMICPortRemoteMACIndicated_Type()
)
ol53nnMFBMICPortRemoteMACIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortRemoteMACIndicated.setStatus("mandatory")


class _Ol53nnMFBMICPortBSFlag_Type(Integer32):
    """Custom type ol53nnMFBMICPortBSFlag based on Integer32"""
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


_Ol53nnMFBMICPortBSFlag_Type.__name__ = "Integer32"
_Ol53nnMFBMICPortBSFlag_Object = MibTableColumn
ol53nnMFBMICPortBSFlag = _Ol53nnMFBMICPortBSFlag_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 8),
    _Ol53nnMFBMICPortBSFlag_Type()
)
ol53nnMFBMICPortBSFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortBSFlag.setStatus("mandatory")


class _Ol53nnMFBMICPortPCWithhold_Type(Integer32):
    """Custom type ol53nnMFBMICPortPCWithhold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("m-m", 2),
          ("none", 1),
          ("other", 3))
    )


_Ol53nnMFBMICPortPCWithhold_Type.__name__ = "Integer32"
_Ol53nnMFBMICPortPCWithhold_Object = MibTableColumn
ol53nnMFBMICPortPCWithhold = _Ol53nnMFBMICPortPCWithhold_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 9),
    _Ol53nnMFBMICPortPCWithhold_Type()
)
ol53nnMFBMICPortPCWithhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortPCWithhold.setStatus("mandatory")


class _Ol53nnMFBMICPortLerCondition_Type(Integer32):
    """Custom type ol53nnMFBMICPortLerCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("okay", 2))
    )


_Ol53nnMFBMICPortLerCondition_Type.__name__ = "Integer32"
_Ol53nnMFBMICPortLerCondition_Object = MibTableColumn
ol53nnMFBMICPortLerCondition = _Ol53nnMFBMICPortLerCondition_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 2, 1, 10),
    _Ol53nnMFBMICPortLerCondition_Type()
)
ol53nnMFBMICPortLerCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICPortLerCondition.setStatus("mandatory")
_Ol53nnMFBMICTrunkTable_Object = MibTable
ol53nnMFBMICTrunkTable = _Ol53nnMFBMICTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 3)
)
if mibBuilder.loadTexts:
    ol53nnMFBMICTrunkTable.setStatus("mandatory")
_Ol53nnMFBMICTrunkEntry_Object = MibTableRow
ol53nnMFBMICTrunkEntry = _Ol53nnMFBMICTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 3, 1)
)
ol53nnMFBMICTrunkEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol53nnMFBMICTrunkSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol53nnMFBMICTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMFBMICTrunkEntry.setStatus("mandatory")
_Ol53nnMFBMICTrunkSlotIndex_Type = Integer32
_Ol53nnMFBMICTrunkSlotIndex_Object = MibTableColumn
ol53nnMFBMICTrunkSlotIndex = _Ol53nnMFBMICTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 3, 1, 1),
    _Ol53nnMFBMICTrunkSlotIndex_Type()
)
ol53nnMFBMICTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICTrunkSlotIndex.setStatus("mandatory")
_Ol53nnMFBMICTrunkIndex_Type = Integer32
_Ol53nnMFBMICTrunkIndex_Object = MibTableColumn
ol53nnMFBMICTrunkIndex = _Ol53nnMFBMICTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26, 3, 1, 2),
    _Ol53nnMFBMICTrunkIndex_Type()
)
ol53nnMFBMICTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFBMICTrunkIndex.setStatus("mandatory")
_Ol53nnMFIBST_ObjectIdentity = ObjectIdentity
ol53nnMFIBST = _Ol53nnMFIBST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27)
)
_Ol53nnMFIBSTModTable_Object = MibTable
ol53nnMFIBSTModTable = _Ol53nnMFIBSTModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 1)
)
if mibBuilder.loadTexts:
    ol53nnMFIBSTModTable.setStatus("mandatory")
_Ol53nnMFIBSTModEntry_Object = MibTableRow
ol53nnMFIBSTModEntry = _Ol53nnMFIBSTModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 1, 1)
)
ol53nnMFIBSTModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol53nnMFIBSTModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMFIBSTModEntry.setStatus("mandatory")
_Ol53nnMFIBSTModSlotIndex_Type = Integer32
_Ol53nnMFIBSTModSlotIndex_Object = MibTableColumn
ol53nnMFIBSTModSlotIndex = _Ol53nnMFIBSTModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 1, 1, 1),
    _Ol53nnMFIBSTModSlotIndex_Type()
)
ol53nnMFIBSTModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTModSlotIndex.setStatus("mandatory")


class _Ol53nnMFIBSTModDownStreamModule_Type(Integer32):
    """Custom type ol53nnMFIBSTModDownStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMFIBSTModDownStreamModule_Type.__name__ = "Integer32"
_Ol53nnMFIBSTModDownStreamModule_Object = MibTableColumn
ol53nnMFIBSTModDownStreamModule = _Ol53nnMFIBSTModDownStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 1, 1, 2),
    _Ol53nnMFIBSTModDownStreamModule_Type()
)
ol53nnMFIBSTModDownStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTModDownStreamModule.setStatus("mandatory")


class _Ol53nnMFIBSTModUpStreamModule_Type(Integer32):
    """Custom type ol53nnMFIBSTModUpStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMFIBSTModUpStreamModule_Type.__name__ = "Integer32"
_Ol53nnMFIBSTModUpStreamModule_Object = MibTableColumn
ol53nnMFIBSTModUpStreamModule = _Ol53nnMFIBSTModUpStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 1, 1, 3),
    _Ol53nnMFIBSTModUpStreamModule_Type()
)
ol53nnMFIBSTModUpStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTModUpStreamModule.setStatus("mandatory")


class _Ol53nnMFIBSTModDownStreamOperPath_Type(Integer32):
    """Custom type ol53nnMFIBSTModDownStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMFIBSTModDownStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMFIBSTModDownStreamOperPath_Object = MibTableColumn
ol53nnMFIBSTModDownStreamOperPath = _Ol53nnMFIBSTModDownStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 1, 1, 4),
    _Ol53nnMFIBSTModDownStreamOperPath_Type()
)
ol53nnMFIBSTModDownStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTModDownStreamOperPath.setStatus("mandatory")


class _Ol53nnMFIBSTModUpStreamOperPath_Type(Integer32):
    """Custom type ol53nnMFIBSTModUpStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMFIBSTModUpStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMFIBSTModUpStreamOperPath_Object = MibTableColumn
ol53nnMFIBSTModUpStreamOperPath = _Ol53nnMFIBSTModUpStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 1, 1, 5),
    _Ol53nnMFIBSTModUpStreamOperPath_Type()
)
ol53nnMFIBSTModUpStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTModUpStreamOperPath.setStatus("mandatory")


class _Ol53nnMFIBSTModRingInfo_Type(OctetString):
    """Custom type ol53nnMFIBSTModRingInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Ol53nnMFIBSTModRingInfo_Type.__name__ = "OctetString"
_Ol53nnMFIBSTModRingInfo_Object = MibTableColumn
ol53nnMFIBSTModRingInfo = _Ol53nnMFIBSTModRingInfo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 1, 1, 6),
    _Ol53nnMFIBSTModRingInfo_Type()
)
ol53nnMFIBSTModRingInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTModRingInfo.setStatus("mandatory")
_Ol53nnMFIBSTPortTable_Object = MibTable
ol53nnMFIBSTPortTable = _Ol53nnMFIBSTPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2)
)
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortTable.setStatus("mandatory")
_Ol53nnMFIBSTPortEntry_Object = MibTableRow
ol53nnMFIBSTPortEntry = _Ol53nnMFIBSTPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1)
)
ol53nnMFIBSTPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol53nnMFIBSTPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol53nnMFIBSTPortIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortEntry.setStatus("mandatory")
_Ol53nnMFIBSTPortSlotIndex_Type = Integer32
_Ol53nnMFIBSTPortSlotIndex_Object = MibTableColumn
ol53nnMFIBSTPortSlotIndex = _Ol53nnMFIBSTPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 1),
    _Ol53nnMFIBSTPortSlotIndex_Type()
)
ol53nnMFIBSTPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortSlotIndex.setStatus("mandatory")
_Ol53nnMFIBSTPortIndex_Type = Integer32
_Ol53nnMFIBSTPortIndex_Object = MibTableColumn
ol53nnMFIBSTPortIndex = _Ol53nnMFIBSTPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 2),
    _Ol53nnMFIBSTPortIndex_Type()
)
ol53nnMFIBSTPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortIndex.setStatus("mandatory")


class _Ol53nnMFIBSTPortConfig_Type(Integer32):
    """Custom type ol53nnMFIBSTPortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("master", 4),
          ("slave", 3))
    )


_Ol53nnMFIBSTPortConfig_Type.__name__ = "Integer32"
_Ol53nnMFIBSTPortConfig_Object = MibTableColumn
ol53nnMFIBSTPortConfig = _Ol53nnMFIBSTPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 3),
    _Ol53nnMFIBSTPortConfig_Type()
)
ol53nnMFIBSTPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortConfig.setStatus("mandatory")


class _Ol53nnMFIBSTPortPcmState_Type(Integer32):
    """Custom type ol53nnMFIBSTPortPcmState based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("pc0", 1),
          ("pc1", 2),
          ("pc2", 3),
          ("pc3", 4),
          ("pc4", 5),
          ("pc5", 6),
          ("pc6", 7),
          ("pc7", 8),
          ("pc8", 9),
          ("pc9", 10))
    )


_Ol53nnMFIBSTPortPcmState_Type.__name__ = "Integer32"
_Ol53nnMFIBSTPortPcmState_Object = MibTableColumn
ol53nnMFIBSTPortPcmState = _Ol53nnMFIBSTPortPcmState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 4),
    _Ol53nnMFIBSTPortPcmState_Type()
)
ol53nnMFIBSTPortPcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortPcmState.setStatus("mandatory")


class _Ol53nnMFIBSTPortConnectState_Type(Integer32):
    """Custom type ol53nnMFIBSTPortConnectState based on Integer32"""
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
        *(("active", 4),
          ("connecting", 2),
          ("disabled", 1),
          ("standby", 3))
    )


_Ol53nnMFIBSTPortConnectState_Type.__name__ = "Integer32"
_Ol53nnMFIBSTPortConnectState_Object = MibTableColumn
ol53nnMFIBSTPortConnectState = _Ol53nnMFIBSTPortConnectState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 5),
    _Ol53nnMFIBSTPortConnectState_Type()
)
ol53nnMFIBSTPortConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortConnectState.setStatus("mandatory")


class _Ol53nnMFIBSTPortNeighbor_Type(Integer32):
    """Custom type ol53nnMFIBSTPortNeighbor based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("master", 4),
          ("slave", 3),
          ("unknown", 5))
    )


_Ol53nnMFIBSTPortNeighbor_Type.__name__ = "Integer32"
_Ol53nnMFIBSTPortNeighbor_Object = MibTableColumn
ol53nnMFIBSTPortNeighbor = _Ol53nnMFIBSTPortNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 6),
    _Ol53nnMFIBSTPortNeighbor_Type()
)
ol53nnMFIBSTPortNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortNeighbor.setStatus("mandatory")


class _Ol53nnMFIBSTPortRemoteMACIndicated_Type(Integer32):
    """Custom type ol53nnMFIBSTPortRemoteMACIndicated based on Integer32"""
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


_Ol53nnMFIBSTPortRemoteMACIndicated_Type.__name__ = "Integer32"
_Ol53nnMFIBSTPortRemoteMACIndicated_Object = MibTableColumn
ol53nnMFIBSTPortRemoteMACIndicated = _Ol53nnMFIBSTPortRemoteMACIndicated_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 7),
    _Ol53nnMFIBSTPortRemoteMACIndicated_Type()
)
ol53nnMFIBSTPortRemoteMACIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortRemoteMACIndicated.setStatus("mandatory")


class _Ol53nnMFIBSTPortBSFlag_Type(Integer32):
    """Custom type ol53nnMFIBSTPortBSFlag based on Integer32"""
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


_Ol53nnMFIBSTPortBSFlag_Type.__name__ = "Integer32"
_Ol53nnMFIBSTPortBSFlag_Object = MibTableColumn
ol53nnMFIBSTPortBSFlag = _Ol53nnMFIBSTPortBSFlag_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 8),
    _Ol53nnMFIBSTPortBSFlag_Type()
)
ol53nnMFIBSTPortBSFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortBSFlag.setStatus("mandatory")


class _Ol53nnMFIBSTPortPCWithhold_Type(Integer32):
    """Custom type ol53nnMFIBSTPortPCWithhold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("m-m", 2),
          ("none", 1),
          ("other", 3))
    )


_Ol53nnMFIBSTPortPCWithhold_Type.__name__ = "Integer32"
_Ol53nnMFIBSTPortPCWithhold_Object = MibTableColumn
ol53nnMFIBSTPortPCWithhold = _Ol53nnMFIBSTPortPCWithhold_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 9),
    _Ol53nnMFIBSTPortPCWithhold_Type()
)
ol53nnMFIBSTPortPCWithhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortPCWithhold.setStatus("mandatory")


class _Ol53nnMFIBSTPortLerCondition_Type(Integer32):
    """Custom type ol53nnMFIBSTPortLerCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("okay", 2))
    )


_Ol53nnMFIBSTPortLerCondition_Type.__name__ = "Integer32"
_Ol53nnMFIBSTPortLerCondition_Object = MibTableColumn
ol53nnMFIBSTPortLerCondition = _Ol53nnMFIBSTPortLerCondition_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 2, 1, 10),
    _Ol53nnMFIBSTPortLerCondition_Type()
)
ol53nnMFIBSTPortLerCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTPortLerCondition.setStatus("mandatory")
_Ol53nnMFIBSTTrunkTable_Object = MibTable
ol53nnMFIBSTTrunkTable = _Ol53nnMFIBSTTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 3)
)
if mibBuilder.loadTexts:
    ol53nnMFIBSTTrunkTable.setStatus("mandatory")
_Ol53nnMFIBSTTrunkEntry_Object = MibTableRow
ol53nnMFIBSTTrunkEntry = _Ol53nnMFIBSTTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 3, 1)
)
ol53nnMFIBSTTrunkEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol53nnMFIBSTTrunkSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol53nnMFIBSTTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMFIBSTTrunkEntry.setStatus("mandatory")
_Ol53nnMFIBSTTrunkSlotIndex_Type = Integer32
_Ol53nnMFIBSTTrunkSlotIndex_Object = MibTableColumn
ol53nnMFIBSTTrunkSlotIndex = _Ol53nnMFIBSTTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 3, 1, 1),
    _Ol53nnMFIBSTTrunkSlotIndex_Type()
)
ol53nnMFIBSTTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTTrunkSlotIndex.setStatus("mandatory")
_Ol53nnMFIBSTTrunkIndex_Type = Integer32
_Ol53nnMFIBSTTrunkIndex_Object = MibTableColumn
ol53nnMFIBSTTrunkIndex = _Ol53nnMFIBSTTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27, 3, 1, 2),
    _Ol53nnMFIBSTTrunkIndex_Type()
)
ol53nnMFIBSTTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMFIBSTTrunkIndex.setStatus("mandatory")
_Ol53nnMSTP_ObjectIdentity = ObjectIdentity
ol53nnMSTP = _Ol53nnMSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28)
)
_Ol53nnMSTPModTable_Object = MibTable
ol53nnMSTPModTable = _Ol53nnMSTPModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 1)
)
if mibBuilder.loadTexts:
    ol53nnMSTPModTable.setStatus("mandatory")
_Ol53nnMSTPModEntry_Object = MibTableRow
ol53nnMSTPModEntry = _Ol53nnMSTPModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 1, 1)
)
ol53nnMSTPModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol53nnMSTPModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMSTPModEntry.setStatus("mandatory")
_Ol53nnMSTPModSlotIndex_Type = Integer32
_Ol53nnMSTPModSlotIndex_Object = MibTableColumn
ol53nnMSTPModSlotIndex = _Ol53nnMSTPModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 1, 1, 1),
    _Ol53nnMSTPModSlotIndex_Type()
)
ol53nnMSTPModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPModSlotIndex.setStatus("mandatory")


class _Ol53nnMSTPModDownStreamModule_Type(Integer32):
    """Custom type ol53nnMSTPModDownStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMSTPModDownStreamModule_Type.__name__ = "Integer32"
_Ol53nnMSTPModDownStreamModule_Object = MibTableColumn
ol53nnMSTPModDownStreamModule = _Ol53nnMSTPModDownStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 1, 1, 2),
    _Ol53nnMSTPModDownStreamModule_Type()
)
ol53nnMSTPModDownStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPModDownStreamModule.setStatus("mandatory")


class _Ol53nnMSTPModUpStreamModule_Type(Integer32):
    """Custom type ol53nnMSTPModUpStreamModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Ol53nnMSTPModUpStreamModule_Type.__name__ = "Integer32"
_Ol53nnMSTPModUpStreamModule_Object = MibTableColumn
ol53nnMSTPModUpStreamModule = _Ol53nnMSTPModUpStreamModule_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 1, 1, 3),
    _Ol53nnMSTPModUpStreamModule_Type()
)
ol53nnMSTPModUpStreamModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPModUpStreamModule.setStatus("mandatory")


class _Ol53nnMSTPModDownStreamOperPath_Type(Integer32):
    """Custom type ol53nnMSTPModDownStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMSTPModDownStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMSTPModDownStreamOperPath_Object = MibTableColumn
ol53nnMSTPModDownStreamOperPath = _Ol53nnMSTPModDownStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 1, 1, 4),
    _Ol53nnMSTPModDownStreamOperPath_Type()
)
ol53nnMSTPModDownStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPModDownStreamOperPath.setStatus("mandatory")


class _Ol53nnMSTPModUpStreamOperPath_Type(Integer32):
    """Custom type ol53nnMSTPModUpStreamOperPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fddi-path-1", 24),
          ("fddi-path-2", 25),
          ("fddi-path-3", 26),
          ("fddi-path-4", 27),
          ("fddi-path-5", 28),
          ("fddi-path-6", 29),
          ("fddi-path-7", 30),
          ("fddi-path-8", 31),
          ("isolated", 2))
    )


_Ol53nnMSTPModUpStreamOperPath_Type.__name__ = "Integer32"
_Ol53nnMSTPModUpStreamOperPath_Object = MibTableColumn
ol53nnMSTPModUpStreamOperPath = _Ol53nnMSTPModUpStreamOperPath_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 1, 1, 5),
    _Ol53nnMSTPModUpStreamOperPath_Type()
)
ol53nnMSTPModUpStreamOperPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPModUpStreamOperPath.setStatus("mandatory")


class _Ol53nnMSTPModRingInfo_Type(OctetString):
    """Custom type ol53nnMSTPModRingInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Ol53nnMSTPModRingInfo_Type.__name__ = "OctetString"
_Ol53nnMSTPModRingInfo_Object = MibTableColumn
ol53nnMSTPModRingInfo = _Ol53nnMSTPModRingInfo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 1, 1, 6),
    _Ol53nnMSTPModRingInfo_Type()
)
ol53nnMSTPModRingInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPModRingInfo.setStatus("mandatory")
_Ol53nnMSTPPortTable_Object = MibTable
ol53nnMSTPPortTable = _Ol53nnMSTPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2)
)
if mibBuilder.loadTexts:
    ol53nnMSTPPortTable.setStatus("mandatory")
_Ol53nnMSTPPortEntry_Object = MibTableRow
ol53nnMSTPPortEntry = _Ol53nnMSTPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1)
)
ol53nnMSTPPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol53nnMSTPPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol53nnMSTPPortIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMSTPPortEntry.setStatus("mandatory")
_Ol53nnMSTPPortSlotIndex_Type = Integer32
_Ol53nnMSTPPortSlotIndex_Object = MibTableColumn
ol53nnMSTPPortSlotIndex = _Ol53nnMSTPPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 1),
    _Ol53nnMSTPPortSlotIndex_Type()
)
ol53nnMSTPPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortSlotIndex.setStatus("mandatory")
_Ol53nnMSTPPortIndex_Type = Integer32
_Ol53nnMSTPPortIndex_Object = MibTableColumn
ol53nnMSTPPortIndex = _Ol53nnMSTPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 2),
    _Ol53nnMSTPPortIndex_Type()
)
ol53nnMSTPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortIndex.setStatus("mandatory")


class _Ol53nnMSTPPortConfig_Type(Integer32):
    """Custom type ol53nnMSTPPortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("master", 4),
          ("slave", 3))
    )


_Ol53nnMSTPPortConfig_Type.__name__ = "Integer32"
_Ol53nnMSTPPortConfig_Object = MibTableColumn
ol53nnMSTPPortConfig = _Ol53nnMSTPPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 3),
    _Ol53nnMSTPPortConfig_Type()
)
ol53nnMSTPPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol53nnMSTPPortConfig.setStatus("mandatory")


class _Ol53nnMSTPPortPcmState_Type(Integer32):
    """Custom type ol53nnMSTPPortPcmState based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("pc0", 1),
          ("pc1", 2),
          ("pc2", 3),
          ("pc3", 4),
          ("pc4", 5),
          ("pc5", 6),
          ("pc6", 7),
          ("pc7", 8),
          ("pc8", 9),
          ("pc9", 10))
    )


_Ol53nnMSTPPortPcmState_Type.__name__ = "Integer32"
_Ol53nnMSTPPortPcmState_Object = MibTableColumn
ol53nnMSTPPortPcmState = _Ol53nnMSTPPortPcmState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 4),
    _Ol53nnMSTPPortPcmState_Type()
)
ol53nnMSTPPortPcmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortPcmState.setStatus("mandatory")


class _Ol53nnMSTPPortConnectState_Type(Integer32):
    """Custom type ol53nnMSTPPortConnectState based on Integer32"""
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
        *(("active", 4),
          ("connecting", 2),
          ("disabled", 1),
          ("standby", 3))
    )


_Ol53nnMSTPPortConnectState_Type.__name__ = "Integer32"
_Ol53nnMSTPPortConnectState_Object = MibTableColumn
ol53nnMSTPPortConnectState = _Ol53nnMSTPPortConnectState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 5),
    _Ol53nnMSTPPortConnectState_Type()
)
ol53nnMSTPPortConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortConnectState.setStatus("mandatory")


class _Ol53nnMSTPPortNeighbor_Type(Integer32):
    """Custom type ol53nnMSTPPortNeighbor based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("master", 4),
          ("slave", 3),
          ("unknown", 5))
    )


_Ol53nnMSTPPortNeighbor_Type.__name__ = "Integer32"
_Ol53nnMSTPPortNeighbor_Object = MibTableColumn
ol53nnMSTPPortNeighbor = _Ol53nnMSTPPortNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 6),
    _Ol53nnMSTPPortNeighbor_Type()
)
ol53nnMSTPPortNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortNeighbor.setStatus("mandatory")


class _Ol53nnMSTPPortRemoteMACIndicated_Type(Integer32):
    """Custom type ol53nnMSTPPortRemoteMACIndicated based on Integer32"""
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


_Ol53nnMSTPPortRemoteMACIndicated_Type.__name__ = "Integer32"
_Ol53nnMSTPPortRemoteMACIndicated_Object = MibTableColumn
ol53nnMSTPPortRemoteMACIndicated = _Ol53nnMSTPPortRemoteMACIndicated_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 7),
    _Ol53nnMSTPPortRemoteMACIndicated_Type()
)
ol53nnMSTPPortRemoteMACIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortRemoteMACIndicated.setStatus("mandatory")


class _Ol53nnMSTPPortBSFlag_Type(Integer32):
    """Custom type ol53nnMSTPPortBSFlag based on Integer32"""
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


_Ol53nnMSTPPortBSFlag_Type.__name__ = "Integer32"
_Ol53nnMSTPPortBSFlag_Object = MibTableColumn
ol53nnMSTPPortBSFlag = _Ol53nnMSTPPortBSFlag_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 8),
    _Ol53nnMSTPPortBSFlag_Type()
)
ol53nnMSTPPortBSFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortBSFlag.setStatus("mandatory")


class _Ol53nnMSTPPortPCWithhold_Type(Integer32):
    """Custom type ol53nnMSTPPortPCWithhold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("m-m", 2),
          ("none", 1),
          ("other", 3))
    )


_Ol53nnMSTPPortPCWithhold_Type.__name__ = "Integer32"
_Ol53nnMSTPPortPCWithhold_Object = MibTableColumn
ol53nnMSTPPortPCWithhold = _Ol53nnMSTPPortPCWithhold_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 9),
    _Ol53nnMSTPPortPCWithhold_Type()
)
ol53nnMSTPPortPCWithhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortPCWithhold.setStatus("mandatory")


class _Ol53nnMSTPPortLerCondition_Type(Integer32):
    """Custom type ol53nnMSTPPortLerCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("okay", 2))
    )


_Ol53nnMSTPPortLerCondition_Type.__name__ = "Integer32"
_Ol53nnMSTPPortLerCondition_Object = MibTableColumn
ol53nnMSTPPortLerCondition = _Ol53nnMSTPPortLerCondition_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 10),
    _Ol53nnMSTPPortLerCondition_Type()
)
ol53nnMSTPPortLerCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPPortLerCondition.setStatus("mandatory")


class _Ol53nnMSTPPortPersonality_Type(Integer32):
    """Custom type ol53nnMSTPPortPersonality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sddi", 1),
          ("tpddi", 2))
    )


_Ol53nnMSTPPortPersonality_Type.__name__ = "Integer32"
_Ol53nnMSTPPortPersonality_Object = MibTableColumn
ol53nnMSTPPortPersonality = _Ol53nnMSTPPortPersonality_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 2, 1, 11),
    _Ol53nnMSTPPortPersonality_Type()
)
ol53nnMSTPPortPersonality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol53nnMSTPPortPersonality.setStatus("mandatory")
_Ol53nnMSTPTrunkTable_Object = MibTable
ol53nnMSTPTrunkTable = _Ol53nnMSTPTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 3)
)
if mibBuilder.loadTexts:
    ol53nnMSTPTrunkTable.setStatus("mandatory")
_Ol53nnMSTPTrunkEntry_Object = MibTableRow
ol53nnMSTPTrunkEntry = _Ol53nnMSTPTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 3, 1)
)
ol53nnMSTPTrunkEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol53nnMSTPTrunkSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol53nnMSTPTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol53nnMSTPTrunkEntry.setStatus("mandatory")
_Ol53nnMSTPTrunkSlotIndex_Type = Integer32
_Ol53nnMSTPTrunkSlotIndex_Object = MibTableColumn
ol53nnMSTPTrunkSlotIndex = _Ol53nnMSTPTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 3, 1, 1),
    _Ol53nnMSTPTrunkSlotIndex_Type()
)
ol53nnMSTPTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPTrunkSlotIndex.setStatus("mandatory")
_Ol53nnMSTPTrunkIndex_Type = Integer32
_Ol53nnMSTPTrunkIndex_Object = MibTableColumn
ol53nnMSTPTrunkIndex = _Ol53nnMSTPTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28, 3, 1, 2),
    _Ol53nnMSTPTrunkIndex_Type()
)
ol53nnMSTPTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol53nnMSTPTrunkIndex.setStatus("mandatory")
_Ol51nnMTPCL_ObjectIdentity = ObjectIdentity
ol51nnMTPCL = _Ol51nnMTPCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29)
)
_Ol51nnMTPCLModTable_Object = MibTable
ol51nnMTPCLModTable = _Ol51nnMTPCLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1)
)
if mibBuilder.loadTexts:
    ol51nnMTPCLModTable.setStatus("mandatory")
_Ol51nnMTPCLModEntry_Object = MibTableRow
ol51nnMTPCLModEntry = _Ol51nnMTPCLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1, 1)
)
ol51nnMTPCLModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMTPCLModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPCLModEntry.setStatus("mandatory")
_Ol51nnMTPCLModSlotIndex_Type = Integer32
_Ol51nnMTPCLModSlotIndex_Object = MibTableColumn
ol51nnMTPCLModSlotIndex = _Ol51nnMTPCLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1, 1, 1),
    _Ol51nnMTPCLModSlotIndex_Type()
)
ol51nnMTPCLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPCLModSlotIndex.setStatus("mandatory")


class _Ol51nnMTPCLModMonitorConn_Type(Integer32):
    """Custom type ol51nnMTPCLModMonitorConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connector-1", 1),
          ("connector-2", 2))
    )


_Ol51nnMTPCLModMonitorConn_Type.__name__ = "Integer32"
_Ol51nnMTPCLModMonitorConn_Object = MibTableColumn
ol51nnMTPCLModMonitorConn = _Ol51nnMTPCLModMonitorConn_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1, 1, 2),
    _Ol51nnMTPCLModMonitorConn_Type()
)
ol51nnMTPCLModMonitorConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPCLModMonitorConn.setStatus("mandatory")


class _Ol51nnMTPCLModConn1Network_Type(Integer32):
    """Custom type ol51nnMTPCLModConn1Network based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated-1", 21),
          ("isolated-2", 22))
    )


_Ol51nnMTPCLModConn1Network_Type.__name__ = "Integer32"
_Ol51nnMTPCLModConn1Network_Object = MibTableColumn
ol51nnMTPCLModConn1Network = _Ol51nnMTPCLModConn1Network_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1, 1, 3),
    _Ol51nnMTPCLModConn1Network_Type()
)
ol51nnMTPCLModConn1Network.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPCLModConn1Network.setStatus("mandatory")


class _Ol51nnMTPCLModConn2Network_Type(Integer32):
    """Custom type ol51nnMTPCLModConn2Network based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated-1", 21),
          ("isolated-2", 22))
    )


_Ol51nnMTPCLModConn2Network_Type.__name__ = "Integer32"
_Ol51nnMTPCLModConn2Network_Object = MibTableColumn
ol51nnMTPCLModConn2Network = _Ol51nnMTPCLModConn2Network_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1, 1, 4),
    _Ol51nnMTPCLModConn2Network_Type()
)
ol51nnMTPCLModConn2Network.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPCLModConn2Network.setStatus("mandatory")


class _Ol51nnMTPCLModConn1DipNetwork_Type(Integer32):
    """Custom type ol51nnMTPCLModConn1DipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated-1", 21),
          ("isolated-2", 22))
    )


_Ol51nnMTPCLModConn1DipNetwork_Type.__name__ = "Integer32"
_Ol51nnMTPCLModConn1DipNetwork_Object = MibTableColumn
ol51nnMTPCLModConn1DipNetwork = _Ol51nnMTPCLModConn1DipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1, 1, 5),
    _Ol51nnMTPCLModConn1DipNetwork_Type()
)
ol51nnMTPCLModConn1DipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPCLModConn1DipNetwork.setStatus("mandatory")


class _Ol51nnMTPCLModConn2DipNetwork_Type(Integer32):
    """Custom type ol51nnMTPCLModConn2DipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("isolated-1", 21),
          ("isolated-2", 22))
    )


_Ol51nnMTPCLModConn2DipNetwork_Type.__name__ = "Integer32"
_Ol51nnMTPCLModConn2DipNetwork_Object = MibTableColumn
ol51nnMTPCLModConn2DipNetwork = _Ol51nnMTPCLModConn2DipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1, 1, 6),
    _Ol51nnMTPCLModConn2DipNetwork_Type()
)
ol51nnMTPCLModConn2DipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPCLModConn2DipNetwork.setStatus("mandatory")


class _Ol51nnMTPCLModAutoPartition_Type(Integer32):
    """Custom type ol51nnMTPCLModAutoPartition based on Integer32"""
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
        *(("collisions-127", 3),
          ("collisions-255", 4),
          ("collisions-31", 1),
          ("collisions-63", 2))
    )


_Ol51nnMTPCLModAutoPartition_Type.__name__ = "Integer32"
_Ol51nnMTPCLModAutoPartition_Object = MibTableColumn
ol51nnMTPCLModAutoPartition = _Ol51nnMTPCLModAutoPartition_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 1, 1, 7),
    _Ol51nnMTPCLModAutoPartition_Type()
)
ol51nnMTPCLModAutoPartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPCLModAutoPartition.setStatus("mandatory")
_Ol51nnMTPCLPortTable_Object = MibTable
ol51nnMTPCLPortTable = _Ol51nnMTPCLPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2)
)
if mibBuilder.loadTexts:
    ol51nnMTPCLPortTable.setStatus("mandatory")
_Ol51nnMTPCLPortEntry_Object = MibTableRow
ol51nnMTPCLPortEntry = _Ol51nnMTPCLPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1)
)
ol51nnMTPCLPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnMTPCLPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnMTPCLPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnMTPCLPortEntry.setStatus("mandatory")
_Ol51nnMTPCLPortSlotIndex_Type = Integer32
_Ol51nnMTPCLPortSlotIndex_Object = MibTableColumn
ol51nnMTPCLPortSlotIndex = _Ol51nnMTPCLPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1, 1),
    _Ol51nnMTPCLPortSlotIndex_Type()
)
ol51nnMTPCLPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPCLPortSlotIndex.setStatus("mandatory")
_Ol51nnMTPCLPortIndex_Type = Integer32
_Ol51nnMTPCLPortIndex_Object = MibTableColumn
ol51nnMTPCLPortIndex = _Ol51nnMTPCLPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1, 2),
    _Ol51nnMTPCLPortIndex_Type()
)
ol51nnMTPCLPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPCLPortIndex.setStatus("mandatory")


class _Ol51nnMTPCLPortAdminState_Type(Integer32):
    """Custom type ol51nnMTPCLPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("redundant-backup", 4),
          ("redundant-primary", 3),
          ("remote-diagnostics", 8))
    )


_Ol51nnMTPCLPortAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPCLPortAdminState_Object = MibTableColumn
ol51nnMTPCLPortAdminState = _Ol51nnMTPCLPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1, 3),
    _Ol51nnMTPCLPortAdminState_Type()
)
ol51nnMTPCLPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPCLPortAdminState.setStatus("mandatory")
_Ol51nnMTPCLPortBuddySlot_Type = Integer32
_Ol51nnMTPCLPortBuddySlot_Object = MibTableColumn
ol51nnMTPCLPortBuddySlot = _Ol51nnMTPCLPortBuddySlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1, 4),
    _Ol51nnMTPCLPortBuddySlot_Type()
)
ol51nnMTPCLPortBuddySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPCLPortBuddySlot.setStatus("mandatory")
_Ol51nnMTPCLPortBuddyPort_Type = Integer32
_Ol51nnMTPCLPortBuddyPort_Object = MibTableColumn
ol51nnMTPCLPortBuddyPort = _Ol51nnMTPCLPortBuddyPort_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1, 5),
    _Ol51nnMTPCLPortBuddyPort_Type()
)
ol51nnMTPCLPortBuddyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPCLPortBuddyPort.setStatus("mandatory")


class _Ol51nnMTPCLPortDipAdminState_Type(Integer32):
    """Custom type ol51nnMTPCLPortDipAdminState based on Integer32"""
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


_Ol51nnMTPCLPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnMTPCLPortDipAdminState_Object = MibTableColumn
ol51nnMTPCLPortDipAdminState = _Ol51nnMTPCLPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1, 6),
    _Ol51nnMTPCLPortDipAdminState_Type()
)
ol51nnMTPCLPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPCLPortDipAdminState.setStatus("mandatory")


class _Ol51nnMTPCLPortLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPCLPortLinkInteg based on Integer32"""
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


_Ol51nnMTPCLPortLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPCLPortLinkInteg_Object = MibTableColumn
ol51nnMTPCLPortLinkInteg = _Ol51nnMTPCLPortLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1, 7),
    _Ol51nnMTPCLPortLinkInteg_Type()
)
ol51nnMTPCLPortLinkInteg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol51nnMTPCLPortLinkInteg.setStatus("mandatory")


class _Ol51nnMTPCLPortDipLinkInteg_Type(Integer32):
    """Custom type ol51nnMTPCLPortDipLinkInteg based on Integer32"""
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


_Ol51nnMTPCLPortDipLinkInteg_Type.__name__ = "Integer32"
_Ol51nnMTPCLPortDipLinkInteg_Object = MibTableColumn
ol51nnMTPCLPortDipLinkInteg = _Ol51nnMTPCLPortDipLinkInteg_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29, 2, 1, 8),
    _Ol51nnMTPCLPortDipLinkInteg_Type()
)
ol51nnMTPCLPortDipLinkInteg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnMTPCLPortDipLinkInteg.setStatus("mandatory")
_Ol52nnBTT_ObjectIdentity = ObjectIdentity
ol52nnBTT = _Ol52nnBTT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30)
)
_Ol52nnBTTModTable_Object = MibTable
ol52nnBTTModTable = _Ol52nnBTTModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 1)
)
if mibBuilder.loadTexts:
    ol52nnBTTModTable.setStatus("mandatory")
_Ol52nnBTTModEntry_Object = MibTableRow
ol52nnBTTModEntry = _Ol52nnBTTModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 1, 1)
)
ol52nnBTTModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol52nnBTTModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol52nnBTTModEntry.setStatus("mandatory")
_Ol52nnBTTModSlotIndex_Type = Integer32
_Ol52nnBTTModSlotIndex_Object = MibTableColumn
ol52nnBTTModSlotIndex = _Ol52nnBTTModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 1, 1, 1),
    _Ol52nnBTTModSlotIndex_Type()
)
ol52nnBTTModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTModSlotIndex.setStatus("mandatory")


class _Ol52nnBTTModBridgeType_Type(Integer32):
    """Custom type ol52nnBTTModBridgeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge-type-sr", 1),
          ("bridge-type-srt", 2))
    )


_Ol52nnBTTModBridgeType_Type.__name__ = "Integer32"
_Ol52nnBTTModBridgeType_Object = MibTableColumn
ol52nnBTTModBridgeType = _Ol52nnBTTModBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 1, 1, 2),
    _Ol52nnBTTModBridgeType_Type()
)
ol52nnBTTModBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTModBridgeType.setStatus("mandatory")


class _Ol52nnBTTModSoftwareVersion_Type(DisplayString):
    """Custom type ol52nnBTTModSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Ol52nnBTTModSoftwareVersion_Type.__name__ = "DisplayString"
_Ol52nnBTTModSoftwareVersion_Object = MibTableColumn
ol52nnBTTModSoftwareVersion = _Ol52nnBTTModSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 1, 1, 3),
    _Ol52nnBTTModSoftwareVersion_Type()
)
ol52nnBTTModSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTModSoftwareVersion.setStatus("mandatory")
_Ol52nnBTTModSRBridgeNo_Type = Integer32
_Ol52nnBTTModSRBridgeNo_Object = MibTableColumn
ol52nnBTTModSRBridgeNo = _Ol52nnBTTModSRBridgeNo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 1, 1, 4),
    _Ol52nnBTTModSRBridgeNo_Type()
)
ol52nnBTTModSRBridgeNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTModSRBridgeNo.setStatus("mandatory")


class _Ol52nnBTTModNetworkStatus_Type(Integer32):
    """Custom type ol52nnBTTModNetworkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("beaconing", 3),
          ("closed", 2),
          ("okay", 1))
    )


_Ol52nnBTTModNetworkStatus_Type.__name__ = "Integer32"
_Ol52nnBTTModNetworkStatus_Object = MibTableColumn
ol52nnBTTModNetworkStatus = _Ol52nnBTTModNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 1, 1, 5),
    _Ol52nnBTTModNetworkStatus_Type()
)
ol52nnBTTModNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTModNetworkStatus.setStatus("mandatory")
_Ol52nnBTTPortTable_Object = MibTable
ol52nnBTTPortTable = _Ol52nnBTTPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2)
)
if mibBuilder.loadTexts:
    ol52nnBTTPortTable.setStatus("mandatory")
_Ol52nnBTTPortEntry_Object = MibTableRow
ol52nnBTTPortEntry = _Ol52nnBTTPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1)
)
ol52nnBTTPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol52nnBTTPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol52nnBTTPortIndex"),
)
if mibBuilder.loadTexts:
    ol52nnBTTPortEntry.setStatus("mandatory")
_Ol52nnBTTPortSlotIndex_Type = Integer32
_Ol52nnBTTPortSlotIndex_Object = MibTableColumn
ol52nnBTTPortSlotIndex = _Ol52nnBTTPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 1),
    _Ol52nnBTTPortSlotIndex_Type()
)
ol52nnBTTPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTPortSlotIndex.setStatus("mandatory")
_Ol52nnBTTPortIndex_Type = Integer32
_Ol52nnBTTPortIndex_Object = MibTableColumn
ol52nnBTTPortIndex = _Ol52nnBTTPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 2),
    _Ol52nnBTTPortIndex_Type()
)
ol52nnBTTPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTPortIndex.setStatus("mandatory")


class _Ol52nnBTTPortConnector_Type(Integer32):
    """Custom type ol52nnBTTPortConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("backPlane", 1),
          ("db-9", 10),
          ("rj45", 8))
    )


_Ol52nnBTTPortConnector_Type.__name__ = "Integer32"
_Ol52nnBTTPortConnector_Object = MibTableColumn
ol52nnBTTPortConnector = _Ol52nnBTTPortConnector_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 3),
    _Ol52nnBTTPortConnector_Type()
)
ol52nnBTTPortConnector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnBTTPortConnector.setStatus("mandatory")


class _Ol52nnBTTPortSTAPState_Type(Integer32):
    """Custom type ol52nnBTTPortSTAPState based on Integer32"""
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
        *(("blocking", 2),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3),
          ("off", 6))
    )


_Ol52nnBTTPortSTAPState_Type.__name__ = "Integer32"
_Ol52nnBTTPortSTAPState_Object = MibTableColumn
ol52nnBTTPortSTAPState = _Ol52nnBTTPortSTAPState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 4),
    _Ol52nnBTTPortSTAPState_Type()
)
ol52nnBTTPortSTAPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTPortSTAPState.setStatus("mandatory")
_Ol52nnBTTPortIpAddress_Type = IpAddress
_Ol52nnBTTPortIpAddress_Object = MibTableColumn
ol52nnBTTPortIpAddress = _Ol52nnBTTPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 5),
    _Ol52nnBTTPortIpAddress_Type()
)
ol52nnBTTPortIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTPortIpAddress.setStatus("mandatory")


class _Ol52nnBTTPortMACAddress_Type(OctetString):
    """Custom type ol52nnBTTPortMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol52nnBTTPortMACAddress_Type.__name__ = "OctetString"
_Ol52nnBTTPortMACAddress_Object = MibTableColumn
ol52nnBTTPortMACAddress = _Ol52nnBTTPortMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 6),
    _Ol52nnBTTPortMACAddress_Type()
)
ol52nnBTTPortMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTPortMACAddress.setStatus("mandatory")
_Ol52nnBTTPortThroughput_Type = Gauge32
_Ol52nnBTTPortThroughput_Object = MibTableColumn
ol52nnBTTPortThroughput = _Ol52nnBTTPortThroughput_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 7),
    _Ol52nnBTTPortThroughput_Type()
)
ol52nnBTTPortThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTPortThroughput.setStatus("mandatory")
_Ol52nnBTTPortForwarding_Type = Gauge32
_Ol52nnBTTPortForwarding_Object = MibTableColumn
ol52nnBTTPortForwarding = _Ol52nnBTTPortForwarding_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 8),
    _Ol52nnBTTPortForwarding_Type()
)
ol52nnBTTPortForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTPortForwarding.setStatus("mandatory")
_Ol52nnBTTPortSRRingNo_Type = Integer32
_Ol52nnBTTPortSRRingNo_Object = MibTableColumn
ol52nnBTTPortSRRingNo = _Ol52nnBTTPortSRRingNo_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 9),
    _Ol52nnBTTPortSRRingNo_Type()
)
ol52nnBTTPortSRRingNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTPortSRRingNo.setStatus("mandatory")


class _Ol52nnBTTPortRingSpeed_Type(Integer32):
    """Custom type ol52nnBTTPortRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 1),
          ("sixteenMegabit", 2))
    )


_Ol52nnBTTPortRingSpeed_Type.__name__ = "Integer32"
_Ol52nnBTTPortRingSpeed_Object = MibTableColumn
ol52nnBTTPortRingSpeed = _Ol52nnBTTPortRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 2, 1, 10),
    _Ol52nnBTTPortRingSpeed_Type()
)
ol52nnBTTPortRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnBTTPortRingSpeed.setStatus("mandatory")
_Ol52nnBTTTrunkTable_Object = MibTable
ol52nnBTTTrunkTable = _Ol52nnBTTTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 3)
)
if mibBuilder.loadTexts:
    ol52nnBTTTrunkTable.setStatus("mandatory")
_Ol52nnBTTTrunkEntry_Object = MibTableRow
ol52nnBTTTrunkEntry = _Ol52nnBTTTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 3, 1)
)
ol52nnBTTTrunkEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol52nnBTTTrunkSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol52nnBTTTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol52nnBTTTrunkEntry.setStatus("mandatory")
_Ol52nnBTTTrunkSlotIndex_Type = Integer32
_Ol52nnBTTTrunkSlotIndex_Object = MibTableColumn
ol52nnBTTTrunkSlotIndex = _Ol52nnBTTTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 3, 1, 1),
    _Ol52nnBTTTrunkSlotIndex_Type()
)
ol52nnBTTTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTTrunkSlotIndex.setStatus("mandatory")
_Ol52nnBTTTrunkIndex_Type = Integer32
_Ol52nnBTTTrunkIndex_Object = MibTableColumn
ol52nnBTTTrunkIndex = _Ol52nnBTTTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30, 3, 1, 2),
    _Ol52nnBTTTrunkIndex_Type()
)
ol52nnBTTTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnBTTTrunkIndex.setStatus("mandatory")
_Ol51nnIx_ObjectIdentity = ObjectIdentity
ol51nnIx = _Ol51nnIx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31)
)
_Ol51nnIxModTable_Object = MibTable
ol51nnIxModTable = _Ol51nnIxModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 1)
)
if mibBuilder.loadTexts:
    ol51nnIxModTable.setStatus("mandatory")
_Ol51nnIxModEntry_Object = MibTableRow
ol51nnIxModEntry = _Ol51nnIxModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 1, 1)
)
ol51nnIxModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnIxModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol51nnIxModEntry.setStatus("mandatory")
_Ol51nnIxModSlotIndex_Type = Integer32
_Ol51nnIxModSlotIndex_Object = MibTableColumn
ol51nnIxModSlotIndex = _Ol51nnIxModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 1, 1, 1),
    _Ol51nnIxModSlotIndex_Type()
)
ol51nnIxModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxModSlotIndex.setStatus("mandatory")


class _Ol51nnIxModSwType_Type(Integer32):
    """Custom type ol51nnIxModSwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("router", 3),
          ("switch", 2))
    )


_Ol51nnIxModSwType_Type.__name__ = "Integer32"
_Ol51nnIxModSwType_Object = MibTableColumn
ol51nnIxModSwType = _Ol51nnIxModSwType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 1, 1, 2),
    _Ol51nnIxModSwType_Type()
)
ol51nnIxModSwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxModSwType.setStatus("mandatory")


class _Ol51nnIxModStationAddr_Type(OctetString):
    """Custom type ol51nnIxModStationAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Ol51nnIxModStationAddr_Type.__name__ = "OctetString"
_Ol51nnIxModStationAddr_Object = MibTableColumn
ol51nnIxModStationAddr = _Ol51nnIxModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 1, 1, 3),
    _Ol51nnIxModStationAddr_Type()
)
ol51nnIxModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxModStationAddr.setStatus("mandatory")


class _Ol51nnIxModDipPromDefaults_Type(Integer32):
    """Custom type ol51nnIxModDipPromDefaults based on Integer32"""
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


_Ol51nnIxModDipPromDefaults_Type.__name__ = "Integer32"
_Ol51nnIxModDipPromDefaults_Object = MibTableColumn
ol51nnIxModDipPromDefaults = _Ol51nnIxModDipPromDefaults_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 1, 1, 4),
    _Ol51nnIxModDipPromDefaults_Type()
)
ol51nnIxModDipPromDefaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxModDipPromDefaults.setStatus("mandatory")
_Ol51nnIxModProtocols_Type = DisplayString
_Ol51nnIxModProtocols_Object = MibTableColumn
ol51nnIxModProtocols = _Ol51nnIxModProtocols_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 1, 1, 5),
    _Ol51nnIxModProtocols_Type()
)
ol51nnIxModProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxModProtocols.setStatus("mandatory")
_Ol51nnIxPortTable_Object = MibTable
ol51nnIxPortTable = _Ol51nnIxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2)
)
if mibBuilder.loadTexts:
    ol51nnIxPortTable.setStatus("mandatory")
_Ol51nnIxPortEntry_Object = MibTableRow
ol51nnIxPortEntry = _Ol51nnIxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2, 1)
)
ol51nnIxPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol51nnIxPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol51nnIxPortIndex"),
)
if mibBuilder.loadTexts:
    ol51nnIxPortEntry.setStatus("mandatory")
_Ol51nnIxPortSlotIndex_Type = Integer32
_Ol51nnIxPortSlotIndex_Object = MibTableColumn
ol51nnIxPortSlotIndex = _Ol51nnIxPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2, 1, 1),
    _Ol51nnIxPortSlotIndex_Type()
)
ol51nnIxPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxPortSlotIndex.setStatus("mandatory")
_Ol51nnIxPortIndex_Type = Integer32
_Ol51nnIxPortIndex_Object = MibTableColumn
ol51nnIxPortIndex = _Ol51nnIxPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2, 1, 2),
    _Ol51nnIxPortIndex_Type()
)
ol51nnIxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxPortIndex.setStatus("mandatory")


class _Ol51nnIxPortDipAdminState_Type(Integer32):
    """Custom type ol51nnIxPortDipAdminState based on Integer32"""
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


_Ol51nnIxPortDipAdminState_Type.__name__ = "Integer32"
_Ol51nnIxPortDipAdminState_Object = MibTableColumn
ol51nnIxPortDipAdminState = _Ol51nnIxPortDipAdminState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2, 1, 3),
    _Ol51nnIxPortDipAdminState_Type()
)
ol51nnIxPortDipAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxPortDipAdminState.setStatus("mandatory")


class _Ol51nnIxPortSTAPState_Type(Integer32):
    """Custom type ol51nnIxPortSTAPState based on Integer32"""
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
        *(("blocking", 2),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3),
          ("off", 6),
          ("unknown", 7))
    )


_Ol51nnIxPortSTAPState_Type.__name__ = "Integer32"
_Ol51nnIxPortSTAPState_Object = MibTableColumn
ol51nnIxPortSTAPState = _Ol51nnIxPortSTAPState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2, 1, 4),
    _Ol51nnIxPortSTAPState_Type()
)
ol51nnIxPortSTAPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxPortSTAPState.setStatus("mandatory")
_Ol51nnIxPortIpAddress_Type = IpAddress
_Ol51nnIxPortIpAddress_Object = MibTableColumn
ol51nnIxPortIpAddress = _Ol51nnIxPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2, 1, 5),
    _Ol51nnIxPortIpAddress_Type()
)
ol51nnIxPortIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxPortIpAddress.setStatus("mandatory")


class _Ol51nnIxPortDipNetwork_Type(Integer32):
    """Custom type ol51nnIxPortDipNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("front-panel", 5),
          ("isolated", 2))
    )


_Ol51nnIxPortDipNetwork_Type.__name__ = "Integer32"
_Ol51nnIxPortDipNetwork_Object = MibTableColumn
ol51nnIxPortDipNetwork = _Ol51nnIxPortDipNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2, 1, 6),
    _Ol51nnIxPortDipNetwork_Type()
)
ol51nnIxPortDipNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxPortDipNetwork.setStatus("mandatory")


class _Ol51nnIxPortDefNetwork_Type(Integer32):
    """Custom type ol51nnIxPortDefNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-1", 6),
          ("ethernet-2", 7),
          ("ethernet-3", 8),
          ("front-panel", 5),
          ("isolated", 2))
    )


_Ol51nnIxPortDefNetwork_Type.__name__ = "Integer32"
_Ol51nnIxPortDefNetwork_Object = MibTableColumn
ol51nnIxPortDefNetwork = _Ol51nnIxPortDefNetwork_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31, 2, 1, 7),
    _Ol51nnIxPortDefNetwork_Type()
)
ol51nnIxPortDefNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol51nnIxPortDefNetwork.setStatus("mandatory")
_Ol52nnMMGT_ObjectIdentity = ObjectIdentity
ol52nnMMGT = _Ol52nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32)
)
_Ol52nnMMGTModTable_Object = MibTable
ol52nnMMGTModTable = _Ol52nnMMGTModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1)
)
if mibBuilder.loadTexts:
    ol52nnMMGTModTable.setStatus("mandatory")
_Ol52nnMMGTModEntry_Object = MibTableRow
ol52nnMMGTModEntry = _Ol52nnMMGTModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1)
)
ol52nnMMGTModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol52nnMMGTModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMMGTModEntry.setStatus("mandatory")
_Ol52nnMMGTModSlotIndex_Type = Integer32
_Ol52nnMMGTModSlotIndex_Object = MibTableColumn
ol52nnMMGTModSlotIndex = _Ol52nnMMGTModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1, 1),
    _Ol52nnMMGTModSlotIndex_Type()
)
ol52nnMMGTModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTModSlotIndex.setStatus("mandatory")


class _Ol52nnMMGTModMasterPriority_Type(Integer32):
    """Custom type ol52nnMMGTModMasterPriority based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("four", 4),
          ("nine", 9),
          ("one", 1),
          ("seven", 7),
          ("six", 6),
          ("ten", 10),
          ("three", 3),
          ("two", 2))
    )


_Ol52nnMMGTModMasterPriority_Type.__name__ = "Integer32"
_Ol52nnMMGTModMasterPriority_Object = MibTableColumn
ol52nnMMGTModMasterPriority = _Ol52nnMMGTModMasterPriority_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1, 2),
    _Ol52nnMMGTModMasterPriority_Type()
)
ol52nnMMGTModMasterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMMGTModMasterPriority.setStatus("mandatory")


class _Ol52nnMMGTModMasterStatus_Type(Integer32):
    """Custom type ol52nnMMGTModMasterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("electing", 3),
          ("master", 1),
          ("non-master", 2))
    )


_Ol52nnMMGTModMasterStatus_Type.__name__ = "Integer32"
_Ol52nnMMGTModMasterStatus_Object = MibTableColumn
ol52nnMMGTModMasterStatus = _Ol52nnMMGTModMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1, 3),
    _Ol52nnMMGTModMasterStatus_Type()
)
ol52nnMMGTModMasterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTModMasterStatus.setStatus("mandatory")
_Ol52nnMMGTModStationAddr_Type = OctetString
_Ol52nnMMGTModStationAddr_Object = MibTableColumn
ol52nnMMGTModStationAddr = _Ol52nnMMGTModStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1, 4),
    _Ol52nnMMGTModStationAddr_Type()
)
ol52nnMMGTModStationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTModStationAddr.setStatus("mandatory")


class _Ol52nnMMGTModRingSpeed_Type(Integer32):
    """Custom type ol52nnMMGTModRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 1),
          ("sixteenMegabit", 2))
    )


_Ol52nnMMGTModRingSpeed_Type.__name__ = "Integer32"
_Ol52nnMMGTModRingSpeed_Object = MibTableColumn
ol52nnMMGTModRingSpeed = _Ol52nnMMGTModRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1, 5),
    _Ol52nnMMGTModRingSpeed_Type()
)
ol52nnMMGTModRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMMGTModRingSpeed.setStatus("mandatory")


class _Ol52nnMMGTModNetworkStatus_Type(Integer32):
    """Custom type ol52nnMMGTModNetworkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("beaconing", 3),
          ("closed", 2),
          ("okay", 1))
    )


_Ol52nnMMGTModNetworkStatus_Type.__name__ = "Integer32"
_Ol52nnMMGTModNetworkStatus_Object = MibTableColumn
ol52nnMMGTModNetworkStatus = _Ol52nnMMGTModNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 1, 1, 6),
    _Ol52nnMMGTModNetworkStatus_Type()
)
ol52nnMMGTModNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTModNetworkStatus.setStatus("mandatory")
_Ol52nnMMGTPortTable_Object = MibTable
ol52nnMMGTPortTable = _Ol52nnMMGTPortTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 2)
)
if mibBuilder.loadTexts:
    ol52nnMMGTPortTable.setStatus("mandatory")
_Ol52nnMMGTPortEntry_Object = MibTableRow
ol52nnMMGTPortEntry = _Ol52nnMMGTPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 2, 1)
)
ol52nnMMGTPortEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol52nnMMGTPortSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol52nnMMGTPortIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMMGTPortEntry.setStatus("mandatory")
_Ol52nnMMGTPortSlotIndex_Type = Integer32
_Ol52nnMMGTPortSlotIndex_Object = MibTableColumn
ol52nnMMGTPortSlotIndex = _Ol52nnMMGTPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 2, 1, 1),
    _Ol52nnMMGTPortSlotIndex_Type()
)
ol52nnMMGTPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTPortSlotIndex.setStatus("mandatory")
_Ol52nnMMGTPortIndex_Type = Integer32
_Ol52nnMMGTPortIndex_Object = MibTableColumn
ol52nnMMGTPortIndex = _Ol52nnMMGTPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 2, 1, 2),
    _Ol52nnMMGTPortIndex_Type()
)
ol52nnMMGTPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTPortIndex.setStatus("mandatory")
_Ol52nnMMGTPortIpAddress_Type = IpAddress
_Ol52nnMMGTPortIpAddress_Object = MibTableColumn
ol52nnMMGTPortIpAddress = _Ol52nnMMGTPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 2, 1, 3),
    _Ol52nnMMGTPortIpAddress_Type()
)
ol52nnMMGTPortIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMMGTPortIpAddress.setStatus("mandatory")
_Ol52nnMMGTTrunkTable_Object = MibTable
ol52nnMMGTTrunkTable = _Ol52nnMMGTTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 3)
)
if mibBuilder.loadTexts:
    ol52nnMMGTTrunkTable.setStatus("mandatory")
_Ol52nnMMGTTrunkEntry_Object = MibTableRow
ol52nnMMGTTrunkEntry = _Ol52nnMMGTTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 3, 1)
)
ol52nnMMGTTrunkEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol52nnMMGTTrunkSlotIndex"),
    (0, "CHIPMODULE-MIB", "ol52nnMMGTTrunkIndex"),
)
if mibBuilder.loadTexts:
    ol52nnMMGTTrunkEntry.setStatus("mandatory")
_Ol52nnMMGTTrunkSlotIndex_Type = Integer32
_Ol52nnMMGTTrunkSlotIndex_Object = MibTableColumn
ol52nnMMGTTrunkSlotIndex = _Ol52nnMMGTTrunkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 3, 1, 1),
    _Ol52nnMMGTTrunkSlotIndex_Type()
)
ol52nnMMGTTrunkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTTrunkSlotIndex.setStatus("mandatory")
_Ol52nnMMGTTrunkIndex_Type = Integer32
_Ol52nnMMGTTrunkIndex_Object = MibTableColumn
ol52nnMMGTTrunkIndex = _Ol52nnMMGTTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 3, 1, 2),
    _Ol52nnMMGTTrunkIndex_Type()
)
ol52nnMMGTTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol52nnMMGTTrunkIndex.setStatus("mandatory")


class _Ol52nnMMGTTrunkCableMon_Type(Integer32):
    """Custom type ol52nnMMGTTrunkCableMon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notApplicable", 3))
    )


_Ol52nnMMGTTrunkCableMon_Type.__name__ = "Integer32"
_Ol52nnMMGTTrunkCableMon_Object = MibTableColumn
ol52nnMMGTTrunkCableMon = _Ol52nnMMGTTrunkCableMon_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 3, 1, 3),
    _Ol52nnMMGTTrunkCableMon_Type()
)
ol52nnMMGTTrunkCableMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMMGTTrunkCableMon.setStatus("mandatory")


class _Ol52nnMMGTTrunkNetMapState_Type(Integer32):
    """Custom type ol52nnMMGTTrunkNetMapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("notApplicable", 1))
    )


_Ol52nnMMGTTrunkNetMapState_Type.__name__ = "Integer32"
_Ol52nnMMGTTrunkNetMapState_Object = MibTableColumn
ol52nnMMGTTrunkNetMapState = _Ol52nnMMGTTrunkNetMapState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 3, 1, 4),
    _Ol52nnMMGTTrunkNetMapState_Type()
)
ol52nnMMGTTrunkNetMapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMMGTTrunkNetMapState.setStatus("mandatory")


class _Ol52nnMMGTTrunkExtBcnRecovery_Type(Integer32):
    """Custom type ol52nnMMGTTrunkExtBcnRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exists", 1),
          ("nonExists", 2),
          ("notApplicable", 3))
    )


_Ol52nnMMGTTrunkExtBcnRecovery_Type.__name__ = "Integer32"
_Ol52nnMMGTTrunkExtBcnRecovery_Object = MibTableColumn
ol52nnMMGTTrunkExtBcnRecovery = _Ol52nnMMGTTrunkExtBcnRecovery_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32, 3, 1, 5),
    _Ol52nnMMGTTrunkExtBcnRecovery_Type()
)
ol52nnMMGTTrunkExtBcnRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ol52nnMMGTTrunkExtBcnRecovery.setStatus("mandatory")
_Ol50nnMHCTL_ObjectIdentity = ObjectIdentity
ol50nnMHCTL = _Ol50nnMHCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33)
)
_Ol50nnMHCTLModTable_Object = MibTable
ol50nnMHCTLModTable = _Ol50nnMHCTLModTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1)
)
if mibBuilder.loadTexts:
    ol50nnMHCTLModTable.setStatus("mandatory")
_Ol50nnMHCTLModEntry_Object = MibTableRow
ol50nnMHCTLModEntry = _Ol50nnMHCTLModEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1)
)
ol50nnMHCTLModEntry.setIndexNames(
    (0, "CHIPMODULE-MIB", "ol50nnMHCTLModSlotIndex"),
)
if mibBuilder.loadTexts:
    ol50nnMHCTLModEntry.setStatus("mandatory")
_Ol50nnMHCTLModSlotIndex_Type = Integer32
_Ol50nnMHCTLModSlotIndex_Object = MibTableColumn
ol50nnMHCTLModSlotIndex = _Ol50nnMHCTLModSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1, 1),
    _Ol50nnMHCTLModSlotIndex_Type()
)
ol50nnMHCTLModSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMHCTLModSlotIndex.setStatus("mandatory")


class _Ol50nnMHCTLModOperState_Type(Integer32):
    """Custom type ol50nnMHCTLModOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_Ol50nnMHCTLModOperState_Type.__name__ = "Integer32"
_Ol50nnMHCTLModOperState_Object = MibTableColumn
ol50nnMHCTLModOperState = _Ol50nnMHCTLModOperState_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1, 2),
    _Ol50nnMHCTLModOperState_Type()
)
ol50nnMHCTLModOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMHCTLModOperState.setStatus("mandatory")


class _Ol50nnMHCTLModClockStatus_Type(Integer32):
    """Custom type ol50nnMHCTLModClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("okay", 1))
    )


_Ol50nnMHCTLModClockStatus_Type.__name__ = "Integer32"
_Ol50nnMHCTLModClockStatus_Object = MibTableColumn
ol50nnMHCTLModClockStatus = _Ol50nnMHCTLModClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1, 3),
    _Ol50nnMHCTLModClockStatus_Type()
)
ol50nnMHCTLModClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMHCTLModClockStatus.setStatus("mandatory")


class _Ol50nnMHCTLModTempStatus_Type(Integer32):
    """Custom type ol50nnMHCTLModTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extremeTemp", 2),
          ("okay", 1))
    )


_Ol50nnMHCTLModTempStatus_Type.__name__ = "Integer32"
_Ol50nnMHCTLModTempStatus_Object = MibTableColumn
ol50nnMHCTLModTempStatus = _Ol50nnMHCTLModTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1, 4),
    _Ol50nnMHCTLModTempStatus_Type()
)
ol50nnMHCTLModTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMHCTLModTempStatus.setStatus("mandatory")


class _Ol50nnMHCTLModPDBStatus_Type(Integer32):
    """Custom type ol50nnMHCTLModPDBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 2),
          ("present", 1))
    )


_Ol50nnMHCTLModPDBStatus_Type.__name__ = "Integer32"
_Ol50nnMHCTLModPDBStatus_Object = MibTableColumn
ol50nnMHCTLModPDBStatus = _Ol50nnMHCTLModPDBStatus_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1, 5),
    _Ol50nnMHCTLModPDBStatus_Type()
)
ol50nnMHCTLModPDBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMHCTLModPDBStatus.setStatus("mandatory")


class _Ol50nnMHCTLModDipCh1ActCol_Type(Integer32):
    """Custom type ol50nnMHCTLModDipCh1ActCol based on Integer32"""
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


_Ol50nnMHCTLModDipCh1ActCol_Type.__name__ = "Integer32"
_Ol50nnMHCTLModDipCh1ActCol_Object = MibTableColumn
ol50nnMHCTLModDipCh1ActCol = _Ol50nnMHCTLModDipCh1ActCol_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1, 6),
    _Ol50nnMHCTLModDipCh1ActCol_Type()
)
ol50nnMHCTLModDipCh1ActCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMHCTLModDipCh1ActCol.setStatus("mandatory")


class _Ol50nnMHCTLModDipCh2ActCol_Type(Integer32):
    """Custom type ol50nnMHCTLModDipCh2ActCol based on Integer32"""
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


_Ol50nnMHCTLModDipCh2ActCol_Type.__name__ = "Integer32"
_Ol50nnMHCTLModDipCh2ActCol_Object = MibTableColumn
ol50nnMHCTLModDipCh2ActCol = _Ol50nnMHCTLModDipCh2ActCol_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1, 7),
    _Ol50nnMHCTLModDipCh2ActCol_Type()
)
ol50nnMHCTLModDipCh2ActCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMHCTLModDipCh2ActCol.setStatus("mandatory")


class _Ol50nnMHCTLModDipCh3ActCol_Type(Integer32):
    """Custom type ol50nnMHCTLModDipCh3ActCol based on Integer32"""
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


_Ol50nnMHCTLModDipCh3ActCol_Type.__name__ = "Integer32"
_Ol50nnMHCTLModDipCh3ActCol_Object = MibTableColumn
ol50nnMHCTLModDipCh3ActCol = _Ol50nnMHCTLModDipCh3ActCol_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33, 1, 1, 8),
    _Ol50nnMHCTLModDipCh3ActCol_Type()
)
ol50nnMHCTLModDipCh3ActCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ol50nnMHCTLModDipCh3ActCol.setStatus("mandatory")
_OlNets_ObjectIdentity = ObjectIdentity
olNets = _OlNets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5)
)
_OlNet_ObjectIdentity = ObjectIdentity
olNet = _OlNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1)
)
_OlEnet_ObjectIdentity = ObjectIdentity
olEnet = _OlEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2)
)
_OlTRnet_ObjectIdentity = ObjectIdentity
olTRnet = _OlTRnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3)
)
_OlFDDInet_ObjectIdentity = ObjectIdentity
olFDDInet = _OlFDDInet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4)
)
_OlGroups_ObjectIdentity = ObjectIdentity
olGroups = _OlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6)
)
_OlAlarm_ObjectIdentity = ObjectIdentity
olAlarm = _OlAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7)
)
_OlThresh_ObjectIdentity = ObjectIdentity
olThresh = _OlThresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1)
)
_OlThreshControl_ObjectIdentity = ObjectIdentity
olThreshControl = _OlThreshControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 1)
)
_Oebm_ObjectIdentity = ObjectIdentity
oebm = _Oebm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 2)
)
_Midnight_ObjectIdentity = ObjectIdentity
midnight = _Midnight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 3)
)
_WorkGroupHub_ObjectIdentity = ObjectIdentity
workGroupHub = _WorkGroupHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4)
)
_HubSysGroup_ObjectIdentity = ObjectIdentity
hubSysGroup = _HubSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 1)
)
_HardwareGroup_ObjectIdentity = ObjectIdentity
hardwareGroup = _HardwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 2)
)
_SoftwareGroup_ObjectIdentity = ObjectIdentity
softwareGroup = _SoftwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 3)
)
_HubGroup_ObjectIdentity = ObjectIdentity
hubGroup = _HubGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 4)
)
_BoardGroup_ObjectIdentity = ObjectIdentity
boardGroup = _BoardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 5)
)
_PortGroup_ObjectIdentity = ObjectIdentity
portGroup = _PortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 6)
)
_AlarmGroup_ObjectIdentity = ObjectIdentity
alarmGroup = _AlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 7)
)
_Emm_ObjectIdentity = ObjectIdentity
emm = _Emm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 5)
)
_ChipBridge_ObjectIdentity = ObjectIdentity
chipBridge = _ChipBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 6)
)
_Trmm_ObjectIdentity = ObjectIdentity
trmm = _Trmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 7)
)
_Fmm_ObjectIdentity = ObjectIdentity
fmm = _Fmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 8)
)
_Focus1_ObjectIdentity = ObjectIdentity
focus1 = _Focus1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 9)
)
_Oeim_ObjectIdentity = ObjectIdentity
oeim = _Oeim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 10)
)
_ChipExperiment_ObjectIdentity = ObjectIdentity
chipExperiment = _ChipExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4)
)
_ChipExpTokenRing_ObjectIdentity = ObjectIdentity
chipExpTokenRing = _ChipExpTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1)
)
_Dot5_ObjectIdentity = ObjectIdentity
dot5 = _Dot5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1)
)
_Dot1dBridge_ObjectIdentity = ObjectIdentity
dot1dBridge = _Dot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14)
)
_ChipTTY_ObjectIdentity = ObjectIdentity
chipTTY = _ChipTTY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 5)
)
_ChipTFTP_ObjectIdentity = ObjectIdentity
chipTFTP = _ChipTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 6)
)
_ChipDownload_ObjectIdentity = ObjectIdentity
chipDownload = _ChipDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHIPMODULE-MIB",
    **{"chipcom": chipcom,
       "chipmib02": chipmib02,
       "chipGen": chipGen,
       "chipEcho": chipEcho,
       "chipProducts": chipProducts,
       "online": online,
       "olAgents": olAgents,
       "olConc": olConc,
       "olEnv": olEnv,
       "olModules": olModules,
       "olSpecMods": olSpecMods,
       "ol50nnMCTL": ol50nnMCTL,
       "ol50nnMCTLModTable": ol50nnMCTLModTable,
       "ol50nnMCTLModEntry": ol50nnMCTLModEntry,
       "ol50nnMCTLModSlotIndex": ol50nnMCTLModSlotIndex,
       "ol50nnMCTLModTempStatus": ol50nnMCTLModTempStatus,
       "ol51nnMMGT": ol51nnMMGT,
       "ol51nnMMGTModTable": ol51nnMMGTModTable,
       "ol51nnMMGTModEntry": ol51nnMMGTModEntry,
       "ol51nnMMGTModSlotIndex": ol51nnMMGTModSlotIndex,
       "ol51nnMMGTModMasterPriority": ol51nnMMGTModMasterPriority,
       "ol51nnMMGTModMasterStatus": ol51nnMMGTModMasterStatus,
       "ol51nnMMGTModStationAddr": ol51nnMMGTModStationAddr,
       "ol51nnMMGTPortTable": ol51nnMMGTPortTable,
       "ol51nnMMGTPortEntry": ol51nnMMGTPortEntry,
       "ol51nnMMGTPortSlotIndex": ol51nnMMGTPortSlotIndex,
       "ol51nnMMGTPortIndex": ol51nnMMGTPortIndex,
       "ol51nnMMGTIpAddress": ol51nnMMGTIpAddress,
       "ol51nnMFIB": ol51nnMFIB,
       "ol51nnMFIBModTable": ol51nnMFIBModTable,
       "ol51nnMFIBModEntry": ol51nnMFIBModEntry,
       "ol51nnMFIBModSlotIndex": ol51nnMFIBModSlotIndex,
       "ol51nnMFIBModDipNetwork": ol51nnMFIBModDipNetwork,
       "ol51nnMFIBModLLW": ol51nnMFIBModLLW,
       "ol51nnMFIBModDipLLW": ol51nnMFIBModDipLLW,
       "ol51nnMFIBPortTable": ol51nnMFIBPortTable,
       "ol51nnMFIBPortEntry": ol51nnMFIBPortEntry,
       "ol51nnMFIBPortSlotIndex": ol51nnMFIBPortSlotIndex,
       "ol51nnMFIBPortIndex": ol51nnMFIBPortIndex,
       "ol51nnMFIBPortAdminState": ol51nnMFIBPortAdminState,
       "ol51nnMFIBPortBuddySlot": ol51nnMFIBPortBuddySlot,
       "ol51nnMFIBPortBuddyPort": ol51nnMFIBPortBuddyPort,
       "ol51nnMFIBPortDipAdminState": ol51nnMFIBPortDipAdminState,
       "ol51nnMUTP": ol51nnMUTP,
       "ol51nnMUTPModTable": ol51nnMUTPModTable,
       "ol51nnMUTPModEntry": ol51nnMUTPModEntry,
       "ol51nnMUTPModSlotIndex": ol51nnMUTPModSlotIndex,
       "ol51nnMUTPModDipNetwork": ol51nnMUTPModDipNetwork,
       "ol51nnMUTPModCrossover": ol51nnMUTPModCrossover,
       "ol51nnMUTPModDipCrossover": ol51nnMUTPModDipCrossover,
       "ol51nnMUTPModFFL": ol51nnMUTPModFFL,
       "ol51nnMUTPModDipFFL": ol51nnMUTPModDipFFL,
       "ol51nnMUTPPortTable": ol51nnMUTPPortTable,
       "ol51nnMUTPPortEntry": ol51nnMUTPPortEntry,
       "ol51nnMUTPPortSlotIndex": ol51nnMUTPPortSlotIndex,
       "ol51nnMUTPPortIndex": ol51nnMUTPPortIndex,
       "ol51nnMUTPPortAdminState": ol51nnMUTPPortAdminState,
       "ol51nnMUTPPortBuddySlot": ol51nnMUTPPortBuddySlot,
       "ol51nnMUTPPortBuddyPort": ol51nnMUTPPortBuddyPort,
       "ol51nnMUTPPortDipAdminState": ol51nnMUTPPortDipAdminState,
       "ol51nnMUTPPortLinkInteg": ol51nnMUTPPortLinkInteg,
       "ol51nnMUTPPortDipLinkInteg": ol51nnMUTPPortDipLinkInteg,
       "ol51nnMUTPPortSquelch": ol51nnMUTPPortSquelch,
       "ol51nnMUTPPortDipSquelch": ol51nnMUTPPortDipSquelch,
       "ol51nnMTP": ol51nnMTP,
       "ol51nnMTPModTable": ol51nnMTPModTable,
       "ol51nnMTPModEntry": ol51nnMTPModEntry,
       "ol51nnMTPModSlotIndex": ol51nnMTPModSlotIndex,
       "ol51nnMTPModDipNetwork": ol51nnMTPModDipNetwork,
       "ol51nnMTPModCrossover": ol51nnMTPModCrossover,
       "ol51nnMTPModDipCrossover": ol51nnMTPModDipCrossover,
       "ol51nnMTPPortTable": ol51nnMTPPortTable,
       "ol51nnMTPPortEntry": ol51nnMTPPortEntry,
       "ol51nnMTPPortSlotIndex": ol51nnMTPPortSlotIndex,
       "ol51nnMTPPortIndex": ol51nnMTPPortIndex,
       "ol51nnMTPPortAdminState": ol51nnMTPPortAdminState,
       "ol51nnMTPPortBuddySlot": ol51nnMTPPortBuddySlot,
       "ol51nnMTPPortBuddyPort": ol51nnMTPPortBuddyPort,
       "ol51nnMTPPortDipAdminState": ol51nnMTPPortDipAdminState,
       "ol51nnMTPPortLinkInteg": ol51nnMTPPortLinkInteg,
       "ol51nnMTPPortDipLinkInteg": ol51nnMTPPortDipLinkInteg,
       "ol51nnMTPPortSquelch": ol51nnMTPPortSquelch,
       "ol51nnMTPPortDipSquelch": ol51nnMTPPortDipSquelch,
       "ol51nnMBNC": ol51nnMBNC,
       "ol51nnMBNCModTable": ol51nnMBNCModTable,
       "ol51nnMBNCModEntry": ol51nnMBNCModEntry,
       "ol51nnMBNCModSlotIndex": ol51nnMBNCModSlotIndex,
       "ol51nnMBNCModDipNetwork": ol51nnMBNCModDipNetwork,
       "ol51nnMBNCPortTable": ol51nnMBNCPortTable,
       "ol51nnMBNCPortEntry": ol51nnMBNCPortEntry,
       "ol51nnMBNCPortSlotIndex": ol51nnMBNCPortSlotIndex,
       "ol51nnMBNCPortIndex": ol51nnMBNCPortIndex,
       "ol51nnMBNCPortDipAdminState": ol51nnMBNCPortDipAdminState,
       "ol51nnMBNCPortDipTermination": ol51nnMBNCPortDipTermination,
       "ol51nnMBNCPortDipGround": ol51nnMBNCPortDipGround,
       "ol51nnBEE": ol51nnBEE,
       "ol51nnBEEModTable": ol51nnBEEModTable,
       "ol51nnBEEModEntry": ol51nnBEEModEntry,
       "ol51nnBEEModSlotIndex": ol51nnBEEModSlotIndex,
       "ol51nnBEEModStationAddr": ol51nnBEEModStationAddr,
       "ol51nnBEEModProtocols": ol51nnBEEModProtocols,
       "ol51nnBEEPortTable": ol51nnBEEPortTable,
       "ol51nnBEEPortEntry": ol51nnBEEPortEntry,
       "ol51nnBEEPortSlotIndex": ol51nnBEEPortSlotIndex,
       "ol51nnBEEPortIndex": ol51nnBEEPortIndex,
       "ol51nnBEEPortIpAddress": ol51nnBEEPortIpAddress,
       "ol51nnBEEPortDipNetwork": ol51nnBEEPortDipNetwork,
       "ol51nnBEEPortDefNetwork": ol51nnBEEPortDefNetwork,
       "ol51nnRES": ol51nnRES,
       "ol51nnRESModTable": ol51nnRESModTable,
       "ol51nnRESModEntry": ol51nnRESModEntry,
       "ol51nnRESModSlotIndex": ol51nnRESModSlotIndex,
       "ol51nnRESModStationAddr": ol51nnRESModStationAddr,
       "ol51nnRESModProtocols": ol51nnRESModProtocols,
       "ol51nnRESPortTable": ol51nnRESPortTable,
       "ol51nnRESPortEntry": ol51nnRESPortEntry,
       "ol51nnRESPortSlotIndex": ol51nnRESPortSlotIndex,
       "ol51nnRESPortIndex": ol51nnRESPortIndex,
       "ol51nnRESPortIpAddress": ol51nnRESPortIpAddress,
       "ol51nnRESPortDipNetwork": ol51nnRESPortDipNetwork,
       "ol51nnRESPortDefNetwork": ol51nnRESPortDefNetwork,
       "ol51nnREE": ol51nnREE,
       "ol51nnREEModTable": ol51nnREEModTable,
       "ol51nnREEModEntry": ol51nnREEModEntry,
       "ol51nnREEModSlotIndex": ol51nnREEModSlotIndex,
       "ol51nnREEModStationAddr": ol51nnREEModStationAddr,
       "ol51nnREEModProtocols": ol51nnREEModProtocols,
       "ol51nnREEPortTable": ol51nnREEPortTable,
       "ol51nnREEPortEntry": ol51nnREEPortEntry,
       "ol51nnREEPortSlotIndex": ol51nnREEPortSlotIndex,
       "ol51nnREEPortIndex": ol51nnREEPortIndex,
       "ol51nnREEPortIpAddress": ol51nnREEPortIpAddress,
       "ol51nnREEPortDipNetwork": ol51nnREEPortDipNetwork,
       "ol51nnREEPortDefNetwork": ol51nnREEPortDefNetwork,
       "ol51nnMAUIF": ol51nnMAUIF,
       "ol51nnMAUIFModTable": ol51nnMAUIFModTable,
       "ol51nnMAUIFModEntry": ol51nnMAUIFModEntry,
       "ol51nnMAUIFModSlotIndex": ol51nnMAUIFModSlotIndex,
       "ol51nnMAUIFPortTable": ol51nnMAUIFPortTable,
       "ol51nnMAUIFPortEntry": ol51nnMAUIFPortEntry,
       "ol51nnMAUIFPortSlotIndex": ol51nnMAUIFPortSlotIndex,
       "ol51nnMAUIFPortIndex": ol51nnMAUIFPortIndex,
       "ol51nnMAUIFPortAdminState": ol51nnMAUIFPortAdminState,
       "ol51nnMAUIFPortBuddySlot": ol51nnMAUIFPortBuddySlot,
       "ol51nnMAUIFPortBuddyPort": ol51nnMAUIFPortBuddyPort,
       "ol51nnMAUIFPortDipAdminState": ol51nnMAUIFPortDipAdminState,
       "ol51nnMAUIFPortDipNetwork": ol51nnMAUIFPortDipNetwork,
       "ol51nnMAUIM": ol51nnMAUIM,
       "ol51nnMAUIMModTable": ol51nnMAUIMModTable,
       "ol51nnMAUIMModEntry": ol51nnMAUIMModEntry,
       "ol51nnMAUIMModSlotIndex": ol51nnMAUIMModSlotIndex,
       "ol51nnMAUIMPortTable": ol51nnMAUIMPortTable,
       "ol51nnMAUIMPortEntry": ol51nnMAUIMPortEntry,
       "ol51nnMAUIMPortSlotIndex": ol51nnMAUIMPortSlotIndex,
       "ol51nnMAUIMPortIndex": ol51nnMAUIMPortIndex,
       "ol51nnMAUIMPortAdminState": ol51nnMAUIMPortAdminState,
       "ol51nnMAUIMPortBuddySlot": ol51nnMAUIMPortBuddySlot,
       "ol51nnMAUIMPortBuddyPort": ol51nnMAUIMPortBuddyPort,
       "ol51nnMAUIMPortDipAdminState": ol51nnMAUIMPortDipAdminState,
       "ol51nnMAUIMPortDipNetwork": ol51nnMAUIMPortDipNetwork,
       "ol51nnMAUIMPortSQETest": ol51nnMAUIMPortSQETest,
       "ol51nnMAUIMPortDipSQETest": ol51nnMAUIMPortDipSQETest,
       "ol51nnMAUIMPortCollision": ol51nnMAUIMPortCollision,
       "ol51nnMAUIMPortDipCollision": ol51nnMAUIMPortDipCollision,
       "ol51nnMAUIMPortHalfStep": ol51nnMAUIMPortHalfStep,
       "ol51nnMAUIMPortDipHalfStep": ol51nnMAUIMPortDipHalfStep,
       "ol5208MTP": ol5208MTP,
       "ol5208MTPModTable": ol5208MTPModTable,
       "ol5208MTPModEntry": ol5208MTPModEntry,
       "ol5208MTPModSlotIndex": ol5208MTPModSlotIndex,
       "ol5208MTPModBypsAdminState": ol5208MTPModBypsAdminState,
       "ol5208MTPModBypsOperState": ol5208MTPModBypsOperState,
       "ol5208MTPModDipCableImp": ol5208MTPModDipCableImp,
       "ol5208MTPPortTable": ol5208MTPPortTable,
       "ol5208MTPPortEntry": ol5208MTPPortEntry,
       "ol5208MTPPortSlotIndex": ol5208MTPPortSlotIndex,
       "ol5208MTPPortIndex": ol5208MTPPortIndex,
       "ol5208MTPPortDipAdminState": ol5208MTPPortDipAdminState,
       "ol5208MTPPortStationType": ol5208MTPPortStationType,
       "ol5208MTPTrunkTable": ol5208MTPTrunkTable,
       "ol5208MTPTrunkEntry": ol5208MTPTrunkEntry,
       "ol5208MTPTrunkSlotIndex": ol5208MTPTrunkSlotIndex,
       "ol5208MTPTrunkIndex": ol5208MTPTrunkIndex,
       "ol5208MTPTrunkDipAdminState": ol5208MTPTrunkDipAdminState,
       "ol5208MTPTrunkCableMon": ol5208MTPTrunkCableMon,
       "ol5208MTPTrunkDipCableMon": ol5208MTPTrunkDipCableMon,
       "ol5208MTPTrunkNetMapState": ol5208MTPTrunkNetMapState,
       "ol5208MTPTrunkExtBcnRecovery": ol5208MTPTrunkExtBcnRecovery,
       "ol51nnMFP": ol51nnMFP,
       "ol51nnMFPModTable": ol51nnMFPModTable,
       "ol51nnMFPModEntry": ol51nnMFPModEntry,
       "ol51nnMFPModSlotIndex": ol51nnMFPModSlotIndex,
       "ol51nnMFPPortTable": ol51nnMFPPortTable,
       "ol51nnMFPPortEntry": ol51nnMFPPortEntry,
       "ol51nnMFPPortSlotIndex": ol51nnMFPPortSlotIndex,
       "ol51nnMFPPortIndex": ol51nnMFPPortIndex,
       "ol51nnMFPPortAdminState": ol51nnMFPPortAdminState,
       "ol51nnMFPPortBuddySlot": ol51nnMFPPortBuddySlot,
       "ol51nnMFPPortBuddyPort": ol51nnMFPPortBuddyPort,
       "ol51nnMFPPortDipAdminState": ol51nnMFPPortDipAdminState,
       "ol51nnMFPPortDipNetwork": ol51nnMFPPortDipNetwork,
       "ol51nnMFPPortLLW": ol51nnMFPPortLLW,
       "ol51nnMFPPortDipLLW": ol51nnMFPPortDipLLW,
       "ol51nnMFPPortHipwr": ol51nnMFPPortHipwr,
       "ol51nnMFPPortDipHipwr": ol51nnMFPPortDipHipwr,
       "ol51nnMFBP": ol51nnMFBP,
       "ol51nnMFBPModTable": ol51nnMFBPModTable,
       "ol51nnMFBPModEntry": ol51nnMFBPModEntry,
       "ol51nnMFBPModSlotIndex": ol51nnMFBPModSlotIndex,
       "ol51nnMFBPPortTable": ol51nnMFBPPortTable,
       "ol51nnMFBPPortEntry": ol51nnMFBPPortEntry,
       "ol51nnMFBPPortSlotIndex": ol51nnMFBPPortSlotIndex,
       "ol51nnMFBPPortIndex": ol51nnMFBPPortIndex,
       "ol51nnMFBPPortAdminState": ol51nnMFBPPortAdminState,
       "ol51nnMFBPPortBuddySlot": ol51nnMFBPPortBuddySlot,
       "ol51nnMFBPPortBuddyPort": ol51nnMFBPPortBuddyPort,
       "ol51nnMFBPPortDipAdminState": ol51nnMFBPPortDipAdminState,
       "ol51nnMFBPPortDipNetwork": ol51nnMFBPPortDipNetwork,
       "ol51nnMFBPPortLLW": ol51nnMFBPPortLLW,
       "ol51nnMFBPPortDipLLW": ol51nnMFBPPortDipLLW,
       "ol51nnMFBPPortHipwr": ol51nnMFBPPortHipwr,
       "ol51nnMFBPPortDipHipwr": ol51nnMFBPPortDipHipwr,
       "ol51nnMTPL": ol51nnMTPL,
       "ol51nnMTPLModTable": ol51nnMTPLModTable,
       "ol51nnMTPLModEntry": ol51nnMTPLModEntry,
       "ol51nnMTPLModSlotIndex": ol51nnMTPLModSlotIndex,
       "ol51nnMTPLModDipNetwork": ol51nnMTPLModDipNetwork,
       "ol51nnMTPLPortTable": ol51nnMTPLPortTable,
       "ol51nnMTPLPortEntry": ol51nnMTPLPortEntry,
       "ol51nnMTPLPortSlotIndex": ol51nnMTPLPortSlotIndex,
       "ol51nnMTPLPortIndex": ol51nnMTPLPortIndex,
       "ol51nnMTPLPortAdminState": ol51nnMTPLPortAdminState,
       "ol51nnMTPLPortBuddySlot": ol51nnMTPLPortBuddySlot,
       "ol51nnMTPLPortBuddyPort": ol51nnMTPLPortBuddyPort,
       "ol51nnMTPLPortDipAdminState": ol51nnMTPLPortDipAdminState,
       "ol51nnMTPLPortLinkInteg": ol51nnMTPLPortLinkInteg,
       "ol51nnMTPLPortDipLinkInteg": ol51nnMTPLPortDipLinkInteg,
       "ol51nnMTPLPortSquelch": ol51nnMTPLPortSquelch,
       "ol51nnMTPLPortJabber": ol51nnMTPLPortJabber,
       "ol51nnMTPLPortDipJabber": ol51nnMTPLPortDipJabber,
       "ol51nnMTPPL": ol51nnMTPPL,
       "ol51nnMTPPLModTable": ol51nnMTPPLModTable,
       "ol51nnMTPPLModEntry": ol51nnMTPPLModEntry,
       "ol51nnMTPPLModSlotIndex": ol51nnMTPPLModSlotIndex,
       "ol51nnMTPPLPortTable": ol51nnMTPPLPortTable,
       "ol51nnMTPPLPortEntry": ol51nnMTPPLPortEntry,
       "ol51nnMTPPLPortSlotIndex": ol51nnMTPPLPortSlotIndex,
       "ol51nnMTPPLPortIndex": ol51nnMTPPLPortIndex,
       "ol51nnMTPPLPortAdminState": ol51nnMTPPLPortAdminState,
       "ol51nnMTPPLPortBuddySlot": ol51nnMTPPLPortBuddySlot,
       "ol51nnMTPPLPortBuddyPort": ol51nnMTPPLPortBuddyPort,
       "ol51nnMTPPLPortDipAdminState": ol51nnMTPPLPortDipAdminState,
       "ol51nnMTPPLPortDipNetwork": ol51nnMTPPLPortDipNetwork,
       "ol51nnMTPPLPortLinkInteg": ol51nnMTPPLPortLinkInteg,
       "ol51nnMTPPLPortDipLinkInteg": ol51nnMTPPLPortDipLinkInteg,
       "ol51nnMTPPLPortSquelch": ol51nnMTPPLPortSquelch,
       "ol51nnMTPPLPortJabber": ol51nnMTPPLPortJabber,
       "ol51nnMTPPLPortDipJabber": ol51nnMTPPLPortDipJabber,
       "ol52nnMTP": ol52nnMTP,
       "ol52nnMTPModTable": ol52nnMTPModTable,
       "ol52nnMTPModEntry": ol52nnMTPModEntry,
       "ol52nnMTPModSlotIndex": ol52nnMTPModSlotIndex,
       "ol52nnMTPModRingSpeed": ol52nnMTPModRingSpeed,
       "ol52nnMTPModDipRingSpeed": ol52nnMTPModDipRingSpeed,
       "ol52nnMTPModCableImp": ol52nnMTPModCableImp,
       "ol52nnMTPModDipCableImp": ol52nnMTPModDipCableImp,
       "ol52nnMTPPortTable": ol52nnMTPPortTable,
       "ol52nnMTPPortEntry": ol52nnMTPPortEntry,
       "ol52nnMTPPortSlotIndex": ol52nnMTPPortSlotIndex,
       "ol52nnMTPPortIndex": ol52nnMTPPortIndex,
       "ol52nnMTPPortDipAdminState": ol52nnMTPPortDipAdminState,
       "ol52nnMTPPortStationType": ol52nnMTPPortStationType,
       "ol52nnMTPTrunkTable": ol52nnMTPTrunkTable,
       "ol52nnMTPTrunkEntry": ol52nnMTPTrunkEntry,
       "ol52nnMTPTrunkSlotIndex": ol52nnMTPTrunkSlotIndex,
       "ol52nnMTPTrunkIndex": ol52nnMTPTrunkIndex,
       "ol52nnMTPTrunkDipAdminState": ol52nnMTPTrunkDipAdminState,
       "ol52nnMFR": ol52nnMFR,
       "ol52nnMFRModTable": ol52nnMFRModTable,
       "ol52nnMFRModEntry": ol52nnMFRModEntry,
       "ol52nnMFRModSlotIndex": ol52nnMFRModSlotIndex,
       "ol52nnMFRModRingSpeed": ol52nnMFRModRingSpeed,
       "ol52nnMFRModDipRingSpeed": ol52nnMFRModDipRingSpeed,
       "ol52nnMFRPortTable": ol52nnMFRPortTable,
       "ol52nnMFRPortEntry": ol52nnMFRPortEntry,
       "ol52nnMFRPortSlotIndex": ol52nnMFRPortSlotIndex,
       "ol52nnMFRPortIndex": ol52nnMFRPortIndex,
       "ol52nnMFRPortDipAdminState": ol52nnMFRPortDipAdminState,
       "ol52nnMFRPortCableImp": ol52nnMFRPortCableImp,
       "ol52nnMFRPortStationType": ol52nnMFRPortStationType,
       "ol52nnMFRTrunkTable": ol52nnMFRTrunkTable,
       "ol52nnMFRTrunkEntry": ol52nnMFRTrunkEntry,
       "ol52nnMFRTrunkSlotIndex": ol52nnMFRTrunkSlotIndex,
       "ol52nnMFRTrunkIndex": ol52nnMFRTrunkIndex,
       "ol52nnMFRTrunkDipAdminState": ol52nnMFRTrunkDipAdminState,
       "ol52nnMFRTrunkCableMon": ol52nnMFRTrunkCableMon,
       "ol52nnMFRTrunkDipCableMon": ol52nnMFRTrunkDipCableMon,
       "ol52nnMFRTrunkCompMode": ol52nnMFRTrunkCompMode,
       "ol52nnMFRTrunkDipCompMode": ol52nnMFRTrunkDipCompMode,
       "ol52nnMFRTrunkNetMapState": ol52nnMFRTrunkNetMapState,
       "ol52nnMFRTrunkExtBcnRecovery": ol52nnMFRTrunkExtBcnRecovery,
       "ol51nnMTS": ol51nnMTS,
       "ol51nnMTSModTable": ol51nnMTSModTable,
       "ol51nnMTSModEntry": ol51nnMTSModEntry,
       "ol51nnMTSModSlotIndex": ol51nnMTSModSlotIndex,
       "ol51nnMTSModProtocols": ol51nnMTSModProtocols,
       "ol51nnMTSModIpAddress": ol51nnMTSModIpAddress,
       "ol51nnMTSModTCPPort": ol51nnMTSModTCPPort,
       "ol51nnMTSModStationAddr": ol51nnMTSModStationAddr,
       "ol51nnMTSModDipNetwork": ol51nnMTSModDipNetwork,
       "ol51nnMTSModCPURev": ol51nnMTSModCPURev,
       "ol51nnMTSPortTable": ol51nnMTSPortTable,
       "ol51nnMTSPortEntry": ol51nnMTSPortEntry,
       "ol51nnMTSPortSlotIndex": ol51nnMTSPortSlotIndex,
       "ol51nnMTSPortIndex": ol51nnMTSPortIndex,
       "ol51nnMTSPortAdminState": ol51nnMTSPortAdminState,
       "ol51nnMTSPortOperState": ol51nnMTSPortOperState,
       "ol51nnMFL": ol51nnMFL,
       "ol51nnMFLModTable": ol51nnMFLModTable,
       "ol51nnMFLModEntry": ol51nnMFLModEntry,
       "ol51nnMFLModSlotIndex": ol51nnMFLModSlotIndex,
       "ol51nnMFLModDipNetwork": ol51nnMFLModDipNetwork,
       "ol51nnMFLPortTable": ol51nnMFLPortTable,
       "ol51nnMFLPortEntry": ol51nnMFLPortEntry,
       "ol51nnMFLPortSlotIndex": ol51nnMFLPortSlotIndex,
       "ol51nnMFLPortIndex": ol51nnMFLPortIndex,
       "ol51nnMFLPortAdminState": ol51nnMFLPortAdminState,
       "ol51nnMFLPortBuddySlot": ol51nnMFLPortBuddySlot,
       "ol51nnMFLPortBuddyPort": ol51nnMFLPortBuddyPort,
       "ol51nnMFLPortDipAdminState": ol51nnMFLPortDipAdminState,
       "ol50nnMRCTL": ol50nnMRCTL,
       "ol50nnMRCTLModTable": ol50nnMRCTLModTable,
       "ol50nnMRCTLModEntry": ol50nnMRCTLModEntry,
       "ol50nnMRCTLModSlotIndex": ol50nnMRCTLModSlotIndex,
       "ol50nnMRCTLModOperState": ol50nnMRCTLModOperState,
       "ol50nnMRCTLModClockStatus": ol50nnMRCTLModClockStatus,
       "ol50nnMRCTLModTempStatus": ol50nnMRCTLModTempStatus,
       "ol51nnMFB": ol51nnMFB,
       "ol51nnMFBModTable": ol51nnMFBModTable,
       "ol51nnMFBModEntry": ol51nnMFBModEntry,
       "ol51nnMFBModSlotIndex": ol51nnMFBModSlotIndex,
       "ol51nnMFBModDipNetwork": ol51nnMFBModDipNetwork,
       "ol51nnMFBModLLW": ol51nnMFBModLLW,
       "ol51nnMFBModDipLLW": ol51nnMFBModDipLLW,
       "ol51nnMFBPortTable": ol51nnMFBPortTable,
       "ol51nnMFBPortEntry": ol51nnMFBPortEntry,
       "ol51nnMFBPortSlotIndex": ol51nnMFBPortSlotIndex,
       "ol51nnMFBPortIndex": ol51nnMFBPortIndex,
       "ol51nnMFBPortAdminState": ol51nnMFBPortAdminState,
       "ol51nnMFBPortBuddySlot": ol51nnMFBPortBuddySlot,
       "ol51nnMFBPortBuddyPort": ol51nnMFBPortBuddyPort,
       "ol51nnMFBPortDipAdminState": ol51nnMFBPortDipAdminState,
       "ol53nnMMGT": ol53nnMMGT,
       "ol53nnMMGTModTable": ol53nnMMGTModTable,
       "ol53nnMMGTModEntry": ol53nnMMGTModEntry,
       "ol53nnMMGTModSlotIndex": ol53nnMMGTModSlotIndex,
       "ol53nnMMGTModMasterPriority": ol53nnMMGTModMasterPriority,
       "ol53nnMMGTModMasterStatus": ol53nnMMGTModMasterStatus,
       "ol53nnMMGTModStationAddr": ol53nnMMGTModStationAddr,
       "ol53nnMMGTModIpAddress": ol53nnMMGTModIpAddress,
       "ol53nnMMGTModDownStreamMAC": ol53nnMMGTModDownStreamMAC,
       "ol53nnMMGTModUpStreamMAC": ol53nnMMGTModUpStreamMAC,
       "ol53nnMMGTModfddiMACPath": ol53nnMMGTModfddiMACPath,
       "ol53nnMMGTModDownStreamModule": ol53nnMMGTModDownStreamModule,
       "ol53nnMMGTModUpStreamModule": ol53nnMMGTModUpStreamModule,
       "ol53nnMMGTModDownStreamOperPath": ol53nnMMGTModDownStreamOperPath,
       "ol53nnMMGTModUpStreamOperPath": ol53nnMMGTModUpStreamOperPath,
       "ol53nnMMGTModRingInfo": ol53nnMMGTModRingInfo,
       "ol53nnMMGTPortTable": ol53nnMMGTPortTable,
       "ol53nnMMGTPortEntry": ol53nnMMGTPortEntry,
       "ol53nnMMGTPortSlotIndex": ol53nnMMGTPortSlotIndex,
       "ol53nnMMGTPortIndex": ol53nnMMGTPortIndex,
       "ol53nnMMGTPortConfig": ol53nnMMGTPortConfig,
       "ol53nnMMGTPortPcmState": ol53nnMMGTPortPcmState,
       "ol53nnMMGTPortConnectState": ol53nnMMGTPortConnectState,
       "ol53nnMMGTPortNeighbor": ol53nnMMGTPortNeighbor,
       "ol53nnMMGTPortRemoteMACIndicated": ol53nnMMGTPortRemoteMACIndicated,
       "ol53nnMMGTPortBSFlag": ol53nnMMGTPortBSFlag,
       "ol53nnMMGTPortPCWithhold": ol53nnMMGTPortPCWithhold,
       "ol53nnMMGTPortLerCondition": ol53nnMMGTPortLerCondition,
       "ol53nnMMGTTrunkTable": ol53nnMMGTTrunkTable,
       "ol53nnMMGTTrunkEntry": ol53nnMMGTTrunkEntry,
       "ol53nnMMGTTrunkSlotIndex": ol53nnMMGTTrunkSlotIndex,
       "ol53nnMMGTTrunkIndex": ol53nnMMGTTrunkIndex,
       "ol53nnMFBMIC": ol53nnMFBMIC,
       "ol53nnMFBMICModTable": ol53nnMFBMICModTable,
       "ol53nnMFBMICModEntry": ol53nnMFBMICModEntry,
       "ol53nnMFBMICModSlotIndex": ol53nnMFBMICModSlotIndex,
       "ol53nnMFBMICModDownStreamModule": ol53nnMFBMICModDownStreamModule,
       "ol53nnMFBMICModUpStreamModule": ol53nnMFBMICModUpStreamModule,
       "ol53nnMFBMICModDownStreamOperPath": ol53nnMFBMICModDownStreamOperPath,
       "ol53nnMFBMICModUpStreamOperPath": ol53nnMFBMICModUpStreamOperPath,
       "ol53nnMFBMICModRingInfo": ol53nnMFBMICModRingInfo,
       "ol53nnMFBMICPortTable": ol53nnMFBMICPortTable,
       "ol53nnMFBMICPortEntry": ol53nnMFBMICPortEntry,
       "ol53nnMFBMICPortSlotIndex": ol53nnMFBMICPortSlotIndex,
       "ol53nnMFBMICPortIndex": ol53nnMFBMICPortIndex,
       "ol53nnMFBMICPortConfig": ol53nnMFBMICPortConfig,
       "ol53nnMFBMICPortPcmState": ol53nnMFBMICPortPcmState,
       "ol53nnMFBMICPortConnectState": ol53nnMFBMICPortConnectState,
       "ol53nnMFBMICPortNeighbor": ol53nnMFBMICPortNeighbor,
       "ol53nnMFBMICPortRemoteMACIndicated": ol53nnMFBMICPortRemoteMACIndicated,
       "ol53nnMFBMICPortBSFlag": ol53nnMFBMICPortBSFlag,
       "ol53nnMFBMICPortPCWithhold": ol53nnMFBMICPortPCWithhold,
       "ol53nnMFBMICPortLerCondition": ol53nnMFBMICPortLerCondition,
       "ol53nnMFBMICTrunkTable": ol53nnMFBMICTrunkTable,
       "ol53nnMFBMICTrunkEntry": ol53nnMFBMICTrunkEntry,
       "ol53nnMFBMICTrunkSlotIndex": ol53nnMFBMICTrunkSlotIndex,
       "ol53nnMFBMICTrunkIndex": ol53nnMFBMICTrunkIndex,
       "ol53nnMFIBST": ol53nnMFIBST,
       "ol53nnMFIBSTModTable": ol53nnMFIBSTModTable,
       "ol53nnMFIBSTModEntry": ol53nnMFIBSTModEntry,
       "ol53nnMFIBSTModSlotIndex": ol53nnMFIBSTModSlotIndex,
       "ol53nnMFIBSTModDownStreamModule": ol53nnMFIBSTModDownStreamModule,
       "ol53nnMFIBSTModUpStreamModule": ol53nnMFIBSTModUpStreamModule,
       "ol53nnMFIBSTModDownStreamOperPath": ol53nnMFIBSTModDownStreamOperPath,
       "ol53nnMFIBSTModUpStreamOperPath": ol53nnMFIBSTModUpStreamOperPath,
       "ol53nnMFIBSTModRingInfo": ol53nnMFIBSTModRingInfo,
       "ol53nnMFIBSTPortTable": ol53nnMFIBSTPortTable,
       "ol53nnMFIBSTPortEntry": ol53nnMFIBSTPortEntry,
       "ol53nnMFIBSTPortSlotIndex": ol53nnMFIBSTPortSlotIndex,
       "ol53nnMFIBSTPortIndex": ol53nnMFIBSTPortIndex,
       "ol53nnMFIBSTPortConfig": ol53nnMFIBSTPortConfig,
       "ol53nnMFIBSTPortPcmState": ol53nnMFIBSTPortPcmState,
       "ol53nnMFIBSTPortConnectState": ol53nnMFIBSTPortConnectState,
       "ol53nnMFIBSTPortNeighbor": ol53nnMFIBSTPortNeighbor,
       "ol53nnMFIBSTPortRemoteMACIndicated": ol53nnMFIBSTPortRemoteMACIndicated,
       "ol53nnMFIBSTPortBSFlag": ol53nnMFIBSTPortBSFlag,
       "ol53nnMFIBSTPortPCWithhold": ol53nnMFIBSTPortPCWithhold,
       "ol53nnMFIBSTPortLerCondition": ol53nnMFIBSTPortLerCondition,
       "ol53nnMFIBSTTrunkTable": ol53nnMFIBSTTrunkTable,
       "ol53nnMFIBSTTrunkEntry": ol53nnMFIBSTTrunkEntry,
       "ol53nnMFIBSTTrunkSlotIndex": ol53nnMFIBSTTrunkSlotIndex,
       "ol53nnMFIBSTTrunkIndex": ol53nnMFIBSTTrunkIndex,
       "ol53nnMSTP": ol53nnMSTP,
       "ol53nnMSTPModTable": ol53nnMSTPModTable,
       "ol53nnMSTPModEntry": ol53nnMSTPModEntry,
       "ol53nnMSTPModSlotIndex": ol53nnMSTPModSlotIndex,
       "ol53nnMSTPModDownStreamModule": ol53nnMSTPModDownStreamModule,
       "ol53nnMSTPModUpStreamModule": ol53nnMSTPModUpStreamModule,
       "ol53nnMSTPModDownStreamOperPath": ol53nnMSTPModDownStreamOperPath,
       "ol53nnMSTPModUpStreamOperPath": ol53nnMSTPModUpStreamOperPath,
       "ol53nnMSTPModRingInfo": ol53nnMSTPModRingInfo,
       "ol53nnMSTPPortTable": ol53nnMSTPPortTable,
       "ol53nnMSTPPortEntry": ol53nnMSTPPortEntry,
       "ol53nnMSTPPortSlotIndex": ol53nnMSTPPortSlotIndex,
       "ol53nnMSTPPortIndex": ol53nnMSTPPortIndex,
       "ol53nnMSTPPortConfig": ol53nnMSTPPortConfig,
       "ol53nnMSTPPortPcmState": ol53nnMSTPPortPcmState,
       "ol53nnMSTPPortConnectState": ol53nnMSTPPortConnectState,
       "ol53nnMSTPPortNeighbor": ol53nnMSTPPortNeighbor,
       "ol53nnMSTPPortRemoteMACIndicated": ol53nnMSTPPortRemoteMACIndicated,
       "ol53nnMSTPPortBSFlag": ol53nnMSTPPortBSFlag,
       "ol53nnMSTPPortPCWithhold": ol53nnMSTPPortPCWithhold,
       "ol53nnMSTPPortLerCondition": ol53nnMSTPPortLerCondition,
       "ol53nnMSTPPortPersonality": ol53nnMSTPPortPersonality,
       "ol53nnMSTPTrunkTable": ol53nnMSTPTrunkTable,
       "ol53nnMSTPTrunkEntry": ol53nnMSTPTrunkEntry,
       "ol53nnMSTPTrunkSlotIndex": ol53nnMSTPTrunkSlotIndex,
       "ol53nnMSTPTrunkIndex": ol53nnMSTPTrunkIndex,
       "ol51nnMTPCL": ol51nnMTPCL,
       "ol51nnMTPCLModTable": ol51nnMTPCLModTable,
       "ol51nnMTPCLModEntry": ol51nnMTPCLModEntry,
       "ol51nnMTPCLModSlotIndex": ol51nnMTPCLModSlotIndex,
       "ol51nnMTPCLModMonitorConn": ol51nnMTPCLModMonitorConn,
       "ol51nnMTPCLModConn1Network": ol51nnMTPCLModConn1Network,
       "ol51nnMTPCLModConn2Network": ol51nnMTPCLModConn2Network,
       "ol51nnMTPCLModConn1DipNetwork": ol51nnMTPCLModConn1DipNetwork,
       "ol51nnMTPCLModConn2DipNetwork": ol51nnMTPCLModConn2DipNetwork,
       "ol51nnMTPCLModAutoPartition": ol51nnMTPCLModAutoPartition,
       "ol51nnMTPCLPortTable": ol51nnMTPCLPortTable,
       "ol51nnMTPCLPortEntry": ol51nnMTPCLPortEntry,
       "ol51nnMTPCLPortSlotIndex": ol51nnMTPCLPortSlotIndex,
       "ol51nnMTPCLPortIndex": ol51nnMTPCLPortIndex,
       "ol51nnMTPCLPortAdminState": ol51nnMTPCLPortAdminState,
       "ol51nnMTPCLPortBuddySlot": ol51nnMTPCLPortBuddySlot,
       "ol51nnMTPCLPortBuddyPort": ol51nnMTPCLPortBuddyPort,
       "ol51nnMTPCLPortDipAdminState": ol51nnMTPCLPortDipAdminState,
       "ol51nnMTPCLPortLinkInteg": ol51nnMTPCLPortLinkInteg,
       "ol51nnMTPCLPortDipLinkInteg": ol51nnMTPCLPortDipLinkInteg,
       "ol52nnBTT": ol52nnBTT,
       "ol52nnBTTModTable": ol52nnBTTModTable,
       "ol52nnBTTModEntry": ol52nnBTTModEntry,
       "ol52nnBTTModSlotIndex": ol52nnBTTModSlotIndex,
       "ol52nnBTTModBridgeType": ol52nnBTTModBridgeType,
       "ol52nnBTTModSoftwareVersion": ol52nnBTTModSoftwareVersion,
       "ol52nnBTTModSRBridgeNo": ol52nnBTTModSRBridgeNo,
       "ol52nnBTTModNetworkStatus": ol52nnBTTModNetworkStatus,
       "ol52nnBTTPortTable": ol52nnBTTPortTable,
       "ol52nnBTTPortEntry": ol52nnBTTPortEntry,
       "ol52nnBTTPortSlotIndex": ol52nnBTTPortSlotIndex,
       "ol52nnBTTPortIndex": ol52nnBTTPortIndex,
       "ol52nnBTTPortConnector": ol52nnBTTPortConnector,
       "ol52nnBTTPortSTAPState": ol52nnBTTPortSTAPState,
       "ol52nnBTTPortIpAddress": ol52nnBTTPortIpAddress,
       "ol52nnBTTPortMACAddress": ol52nnBTTPortMACAddress,
       "ol52nnBTTPortThroughput": ol52nnBTTPortThroughput,
       "ol52nnBTTPortForwarding": ol52nnBTTPortForwarding,
       "ol52nnBTTPortSRRingNo": ol52nnBTTPortSRRingNo,
       "ol52nnBTTPortRingSpeed": ol52nnBTTPortRingSpeed,
       "ol52nnBTTTrunkTable": ol52nnBTTTrunkTable,
       "ol52nnBTTTrunkEntry": ol52nnBTTTrunkEntry,
       "ol52nnBTTTrunkSlotIndex": ol52nnBTTTrunkSlotIndex,
       "ol52nnBTTTrunkIndex": ol52nnBTTTrunkIndex,
       "ol51nnIx": ol51nnIx,
       "ol51nnIxModTable": ol51nnIxModTable,
       "ol51nnIxModEntry": ol51nnIxModEntry,
       "ol51nnIxModSlotIndex": ol51nnIxModSlotIndex,
       "ol51nnIxModSwType": ol51nnIxModSwType,
       "ol51nnIxModStationAddr": ol51nnIxModStationAddr,
       "ol51nnIxModDipPromDefaults": ol51nnIxModDipPromDefaults,
       "ol51nnIxModProtocols": ol51nnIxModProtocols,
       "ol51nnIxPortTable": ol51nnIxPortTable,
       "ol51nnIxPortEntry": ol51nnIxPortEntry,
       "ol51nnIxPortSlotIndex": ol51nnIxPortSlotIndex,
       "ol51nnIxPortIndex": ol51nnIxPortIndex,
       "ol51nnIxPortDipAdminState": ol51nnIxPortDipAdminState,
       "ol51nnIxPortSTAPState": ol51nnIxPortSTAPState,
       "ol51nnIxPortIpAddress": ol51nnIxPortIpAddress,
       "ol51nnIxPortDipNetwork": ol51nnIxPortDipNetwork,
       "ol51nnIxPortDefNetwork": ol51nnIxPortDefNetwork,
       "ol52nnMMGT": ol52nnMMGT,
       "ol52nnMMGTModTable": ol52nnMMGTModTable,
       "ol52nnMMGTModEntry": ol52nnMMGTModEntry,
       "ol52nnMMGTModSlotIndex": ol52nnMMGTModSlotIndex,
       "ol52nnMMGTModMasterPriority": ol52nnMMGTModMasterPriority,
       "ol52nnMMGTModMasterStatus": ol52nnMMGTModMasterStatus,
       "ol52nnMMGTModStationAddr": ol52nnMMGTModStationAddr,
       "ol52nnMMGTModRingSpeed": ol52nnMMGTModRingSpeed,
       "ol52nnMMGTModNetworkStatus": ol52nnMMGTModNetworkStatus,
       "ol52nnMMGTPortTable": ol52nnMMGTPortTable,
       "ol52nnMMGTPortEntry": ol52nnMMGTPortEntry,
       "ol52nnMMGTPortSlotIndex": ol52nnMMGTPortSlotIndex,
       "ol52nnMMGTPortIndex": ol52nnMMGTPortIndex,
       "ol52nnMMGTPortIpAddress": ol52nnMMGTPortIpAddress,
       "ol52nnMMGTTrunkTable": ol52nnMMGTTrunkTable,
       "ol52nnMMGTTrunkEntry": ol52nnMMGTTrunkEntry,
       "ol52nnMMGTTrunkSlotIndex": ol52nnMMGTTrunkSlotIndex,
       "ol52nnMMGTTrunkIndex": ol52nnMMGTTrunkIndex,
       "ol52nnMMGTTrunkCableMon": ol52nnMMGTTrunkCableMon,
       "ol52nnMMGTTrunkNetMapState": ol52nnMMGTTrunkNetMapState,
       "ol52nnMMGTTrunkExtBcnRecovery": ol52nnMMGTTrunkExtBcnRecovery,
       "ol50nnMHCTL": ol50nnMHCTL,
       "ol50nnMHCTLModTable": ol50nnMHCTLModTable,
       "ol50nnMHCTLModEntry": ol50nnMHCTLModEntry,
       "ol50nnMHCTLModSlotIndex": ol50nnMHCTLModSlotIndex,
       "ol50nnMHCTLModOperState": ol50nnMHCTLModOperState,
       "ol50nnMHCTLModClockStatus": ol50nnMHCTLModClockStatus,
       "ol50nnMHCTLModTempStatus": ol50nnMHCTLModTempStatus,
       "ol50nnMHCTLModPDBStatus": ol50nnMHCTLModPDBStatus,
       "ol50nnMHCTLModDipCh1ActCol": ol50nnMHCTLModDipCh1ActCol,
       "ol50nnMHCTLModDipCh2ActCol": ol50nnMHCTLModDipCh2ActCol,
       "ol50nnMHCTLModDipCh3ActCol": ol50nnMHCTLModDipCh3ActCol,
       "olNets": olNets,
       "olNet": olNet,
       "olEnet": olEnet,
       "olTRnet": olTRnet,
       "olFDDInet": olFDDInet,
       "olGroups": olGroups,
       "olAlarm": olAlarm,
       "olThresh": olThresh,
       "olThreshControl": olThreshControl,
       "oebm": oebm,
       "midnight": midnight,
       "workGroupHub": workGroupHub,
       "hubSysGroup": hubSysGroup,
       "hardwareGroup": hardwareGroup,
       "softwareGroup": softwareGroup,
       "hubGroup": hubGroup,
       "boardGroup": boardGroup,
       "portGroup": portGroup,
       "alarmGroup": alarmGroup,
       "emm": emm,
       "chipBridge": chipBridge,
       "trmm": trmm,
       "fmm": fmm,
       "focus1": focus1,
       "oeim": oeim,
       "chipExperiment": chipExperiment,
       "chipExpTokenRing": chipExpTokenRing,
       "dot5": dot5,
       "dot1dBridge": dot1dBridge,
       "chipTTY": chipTTY,
       "chipTFTP": chipTFTP,
       "chipDownload": chipDownload}
)
