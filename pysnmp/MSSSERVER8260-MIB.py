# SNMP MIB module (MSSSERVER8260-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MSSSERVER8260-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:03 2024
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

(proElsSubSysEventMsg,) = mibBuilder.importSymbols(
    "PROTEON-MIB",
    "proElsSubSysEventMsg")

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
 NotificationType,
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
    "NotificationType",
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

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_NwaysMSS_ObjectIdentity = ObjectIdentity
nwaysMSS = _NwaysMSS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118)
)
_MssServer8260_ObjectIdentity = ObjectIdentity
mssServer8260 = _MssServer8260_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 3)
)
_Mss8260Prod_ObjectIdentity = ObjectIdentity
mss8260Prod = _Mss8260Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 1)
)


class _Mss8260ResetFlag_Type(Integer32):
    """Custom type mss8260ResetFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 1),
          ("reboot", 2))
    )


_Mss8260ResetFlag_Type.__name__ = "Integer32"
_Mss8260ResetFlag_Object = MibScalar
mss8260ResetFlag = _Mss8260ResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 1, 1),
    _Mss8260ResetFlag_Type()
)
mss8260ResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mss8260ResetFlag.setStatus("mandatory")
_Mss8260DRAMinstalled_Type = Integer32
_Mss8260DRAMinstalled_Object = MibScalar
mss8260DRAMinstalled = _Mss8260DRAMinstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 1, 2),
    _Mss8260DRAMinstalled_Type()
)
mss8260DRAMinstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8260DRAMinstalled.setStatus("mandatory")


class _Mss8260NotifyStatus_Type(Integer32):
    """Custom type mss8260NotifyStatus based on Integer32"""
    defaultValue = 1

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


_Mss8260NotifyStatus_Type.__name__ = "Integer32"
_Mss8260NotifyStatus_Object = MibScalar
mss8260NotifyStatus = _Mss8260NotifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 1, 3),
    _Mss8260NotifyStatus_Type()
)
mss8260NotifyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mss8260NotifyStatus.setStatus("mandatory")


class _Mss8260TempThresholdStatus_Type(Integer32):
    """Custom type mss8260TempThresholdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("shutdown", 3),
          ("warning", 2))
    )


_Mss8260TempThresholdStatus_Type.__name__ = "Integer32"
_Mss8260TempThresholdStatus_Object = MibScalar
mss8260TempThresholdStatus = _Mss8260TempThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 1, 4),
    _Mss8260TempThresholdStatus_Type()
)
mss8260TempThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8260TempThresholdStatus.setStatus("mandatory")
_Mss8260PCAdapter_ObjectIdentity = ObjectIdentity
mss8260PCAdapter = _Mss8260PCAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 2)
)
_Mss8260PCAdapNumSlot_Type = Integer32
_Mss8260PCAdapNumSlot_Object = MibScalar
mss8260PCAdapNumSlot = _Mss8260PCAdapNumSlot_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 2, 1),
    _Mss8260PCAdapNumSlot_Type()
)
mss8260PCAdapNumSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8260PCAdapNumSlot.setStatus("mandatory")
_Mss8260PCAdapTable_Object = MibTable
mss8260PCAdapTable = _Mss8260PCAdapTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 2, 2)
)
if mibBuilder.loadTexts:
    mss8260PCAdapTable.setStatus("mandatory")
_Mss8260PCAdapEntry_Object = MibTableRow
mss8260PCAdapEntry = _Mss8260PCAdapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 2, 2, 1)
)
mss8260PCAdapEntry.setIndexNames(
    (0, "MSSSERVER8260-MIB", "mss8260PCAdapSlotNum"),
)
if mibBuilder.loadTexts:
    mss8260PCAdapEntry.setStatus("mandatory")
_Mss8260PCAdapSlotNum_Type = Integer32
_Mss8260PCAdapSlotNum_Object = MibTableColumn
mss8260PCAdapSlotNum = _Mss8260PCAdapSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 2, 2, 1, 1),
    _Mss8260PCAdapSlotNum_Type()
)
mss8260PCAdapSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8260PCAdapSlotNum.setStatus("mandatory")


class _Mss8260PCAdapType_Type(Integer32):
    """Custom type mss8260PCAdapType based on Integer32"""
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
        *(("flashcard", 5),
          ("harddrive", 2),
          ("modem", 3),
          ("notPresent", 4),
          ("unknown", 1))
    )


_Mss8260PCAdapType_Type.__name__ = "Integer32"
_Mss8260PCAdapType_Object = MibTableColumn
mss8260PCAdapType = _Mss8260PCAdapType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 2, 2, 1, 2),
    _Mss8260PCAdapType_Type()
)
mss8260PCAdapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8260PCAdapType.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mssServer8260ELSTrapV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 0, 2)
)
mssServer8260ELSTrapV2.setObjects(
    ("PROTEON-MIB", "proElsSubSysEventMsg")
)
if mibBuilder.loadTexts:
    mssServer8260ELSTrapV2.setStatus(
        ""
    )

mss8260PCAdapTypeChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 0, 3)
)
mss8260PCAdapTypeChg.setObjects(
    ("MSSSERVER8260-MIB", "mss8260PCAdapType")
)
if mibBuilder.loadTexts:
    mss8260PCAdapTypeChg.setStatus(
        ""
    )

mss8260TempThresholdChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 3, 0, 4)
)
mss8260TempThresholdChg.setObjects(
    ("MSSSERVER8260-MIB", "mss8260TempThresholdStatus")
)
if mibBuilder.loadTexts:
    mss8260TempThresholdChg.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MSSSERVER8260-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "nwaysMSS": nwaysMSS,
       "mssServer8260": mssServer8260,
       "mssServer8260ELSTrapV2": mssServer8260ELSTrapV2,
       "mss8260PCAdapTypeChg": mss8260PCAdapTypeChg,
       "mss8260TempThresholdChg": mss8260TempThresholdChg,
       "mss8260Prod": mss8260Prod,
       "mss8260ResetFlag": mss8260ResetFlag,
       "mss8260DRAMinstalled": mss8260DRAMinstalled,
       "mss8260NotifyStatus": mss8260NotifyStatus,
       "mss8260TempThresholdStatus": mss8260TempThresholdStatus,
       "mss8260PCAdapter": mss8260PCAdapter,
       "mss8260PCAdapNumSlot": mss8260PCAdapNumSlot,
       "mss8260PCAdapTable": mss8260PCAdapTable,
       "mss8260PCAdapEntry": mss8260PCAdapEntry,
       "mss8260PCAdapSlotNum": mss8260PCAdapSlotNum,
       "mss8260PCAdapType": mss8260PCAdapType}
)
