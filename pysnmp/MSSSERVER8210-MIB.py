# SNMP MIB module (MSSSERVER8210-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MSSSERVER8210-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:02 2024
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
_MssServer8210_ObjectIdentity = ObjectIdentity
mssServer8210 = _MssServer8210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2)
)
_Mss8210Prod_ObjectIdentity = ObjectIdentity
mss8210Prod = _Mss8210Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 1)
)


class _Mss8210ResetFlag_Type(Integer32):
    """Custom type mss8210ResetFlag based on Integer32"""
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


_Mss8210ResetFlag_Type.__name__ = "Integer32"
_Mss8210ResetFlag_Object = MibScalar
mss8210ResetFlag = _Mss8210ResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 1, 1),
    _Mss8210ResetFlag_Type()
)
mss8210ResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mss8210ResetFlag.setStatus("mandatory")
_Mss8210DRAMinstalled_Type = Integer32
_Mss8210DRAMinstalled_Object = MibScalar
mss8210DRAMinstalled = _Mss8210DRAMinstalled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 1, 2),
    _Mss8210DRAMinstalled_Type()
)
mss8210DRAMinstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8210DRAMinstalled.setStatus("mandatory")


class _Mss8210NotifyStatus_Type(Integer32):
    """Custom type mss8210NotifyStatus based on Integer32"""
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


_Mss8210NotifyStatus_Type.__name__ = "Integer32"
_Mss8210NotifyStatus_Object = MibScalar
mss8210NotifyStatus = _Mss8210NotifyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 1, 3),
    _Mss8210NotifyStatus_Type()
)
mss8210NotifyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mss8210NotifyStatus.setStatus("mandatory")


class _Mss8210TempThresholdStatus_Type(Integer32):
    """Custom type mss8210TempThresholdStatus based on Integer32"""
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


_Mss8210TempThresholdStatus_Type.__name__ = "Integer32"
_Mss8210TempThresholdStatus_Object = MibScalar
mss8210TempThresholdStatus = _Mss8210TempThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 1, 4),
    _Mss8210TempThresholdStatus_Type()
)
mss8210TempThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8210TempThresholdStatus.setStatus("mandatory")
_Mss8210PCAdapter_ObjectIdentity = ObjectIdentity
mss8210PCAdapter = _Mss8210PCAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2)
)
_Mss8210PCAdapNumSlot_Type = Integer32
_Mss8210PCAdapNumSlot_Object = MibScalar
mss8210PCAdapNumSlot = _Mss8210PCAdapNumSlot_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2, 1),
    _Mss8210PCAdapNumSlot_Type()
)
mss8210PCAdapNumSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8210PCAdapNumSlot.setStatus("mandatory")
_Mss8210PCAdapTable_Object = MibTable
mss8210PCAdapTable = _Mss8210PCAdapTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mss8210PCAdapTable.setStatus("mandatory")
_Mss8210PCAdapEntry_Object = MibTableRow
mss8210PCAdapEntry = _Mss8210PCAdapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2, 2, 1)
)
mss8210PCAdapEntry.setIndexNames(
    (0, "MSSSERVER8210-MIB", "mss8210PCAdapSlotNum"),
)
if mibBuilder.loadTexts:
    mss8210PCAdapEntry.setStatus("mandatory")
_Mss8210PCAdapSlotNum_Type = Integer32
_Mss8210PCAdapSlotNum_Object = MibTableColumn
mss8210PCAdapSlotNum = _Mss8210PCAdapSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2, 2, 1, 1),
    _Mss8210PCAdapSlotNum_Type()
)
mss8210PCAdapSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8210PCAdapSlotNum.setStatus("mandatory")


class _Mss8210PCAdapType_Type(Integer32):
    """Custom type mss8210PCAdapType based on Integer32"""
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


_Mss8210PCAdapType_Type.__name__ = "Integer32"
_Mss8210PCAdapType_Object = MibTableColumn
mss8210PCAdapType = _Mss8210PCAdapType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 2, 2, 1, 2),
    _Mss8210PCAdapType_Type()
)
mss8210PCAdapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8210PCAdapType.setStatus("mandatory")
_Mss8210PCIAdapter_ObjectIdentity = ObjectIdentity
mss8210PCIAdapter = _Mss8210PCIAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3)
)
_Mss8210PCIAdapNumSlot_Type = Integer32
_Mss8210PCIAdapNumSlot_Object = MibScalar
mss8210PCIAdapNumSlot = _Mss8210PCIAdapNumSlot_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 1),
    _Mss8210PCIAdapNumSlot_Type()
)
mss8210PCIAdapNumSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8210PCIAdapNumSlot.setStatus("mandatory")
_Mss8210PCIAdapTable_Object = MibTable
mss8210PCIAdapTable = _Mss8210PCIAdapTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2)
)
if mibBuilder.loadTexts:
    mss8210PCIAdapTable.setStatus("mandatory")
_Mss8210PCIAdapEntry_Object = MibTableRow
mss8210PCIAdapEntry = _Mss8210PCIAdapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1)
)
mss8210PCIAdapEntry.setIndexNames(
    (0, "MSSSERVER8210-MIB", "mss8210PCIAdapSlotNum"),
)
if mibBuilder.loadTexts:
    mss8210PCIAdapEntry.setStatus("mandatory")
_Mss8210PCIAdapSlotNum_Type = Integer32
_Mss8210PCIAdapSlotNum_Object = MibTableColumn
mss8210PCIAdapSlotNum = _Mss8210PCIAdapSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 1),
    _Mss8210PCIAdapSlotNum_Type()
)
mss8210PCIAdapSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8210PCIAdapSlotNum.setStatus("mandatory")


class _Mss8210PCIAdapType_Type(Integer32):
    """Custom type mss8210PCIAdapType based on Integer32"""
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
        *(("atm", 2),
          ("fddi", 3),
          ("notPresent", 4),
          ("unknown", 1))
    )


_Mss8210PCIAdapType_Type.__name__ = "Integer32"
_Mss8210PCIAdapType_Object = MibTableColumn
mss8210PCIAdapType = _Mss8210PCIAdapType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 2),
    _Mss8210PCIAdapType_Type()
)
mss8210PCIAdapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8210PCIAdapType.setStatus("mandatory")


class _Mss8210PCIAdapConfigType_Type(Integer32):
    """Custom type mss8210PCIAdapConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atm", 2),
          ("fddi", 3),
          ("not-configured", 1))
    )


_Mss8210PCIAdapConfigType_Type.__name__ = "Integer32"
_Mss8210PCIAdapConfigType_Object = MibTableColumn
mss8210PCIAdapConfigType = _Mss8210PCIAdapConfigType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 3),
    _Mss8210PCIAdapConfigType_Type()
)
mss8210PCIAdapConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8210PCIAdapConfigType.setStatus("mandatory")


class _Mss8210PCIAdapOperStatus_Type(Integer32):
    """Custom type mss8210PCIAdapOperStatus based on Integer32"""
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
        *(("disable-pending", 8),
          ("disabled", 9),
          ("does-not-apply", 5),
          ("enable-pending", 6),
          ("enabled", 7),
          ("miss-configured", 10),
          ("not-configured", 2),
          ("not-present", 3),
          ("unavailable", 4),
          ("unknown", 1))
    )


_Mss8210PCIAdapOperStatus_Type.__name__ = "Integer32"
_Mss8210PCIAdapOperStatus_Object = MibTableColumn
mss8210PCIAdapOperStatus = _Mss8210PCIAdapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 4),
    _Mss8210PCIAdapOperStatus_Type()
)
mss8210PCIAdapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8210PCIAdapOperStatus.setStatus("mandatory")


class _Mss8210PCIAdapDiagStatus_Type(Integer32):
    """Custom type mss8210PCIAdapDiagStatus based on Integer32"""
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
          ("auto", 1),
          ("idle", 3),
          ("inactive", 2))
    )


_Mss8210PCIAdapDiagStatus_Type.__name__ = "Integer32"
_Mss8210PCIAdapDiagStatus_Object = MibTableColumn
mss8210PCIAdapDiagStatus = _Mss8210PCIAdapDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 5),
    _Mss8210PCIAdapDiagStatus_Type()
)
mss8210PCIAdapDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8210PCIAdapDiagStatus.setStatus("mandatory")


class _Mss8210PCIAdapNetworkStatus_Type(Integer32):
    """Custom type mss8210PCIAdapNetworkStatus based on Integer32"""
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
        *(("does-not-apply", 5),
          ("down", 3),
          ("testing", 4),
          ("unknown", 1),
          ("up", 2))
    )


_Mss8210PCIAdapNetworkStatus_Type.__name__ = "Integer32"
_Mss8210PCIAdapNetworkStatus_Object = MibTableColumn
mss8210PCIAdapNetworkStatus = _Mss8210PCIAdapNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 6),
    _Mss8210PCIAdapNetworkStatus_Type()
)
mss8210PCIAdapNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8210PCIAdapNetworkStatus.setStatus("mandatory")


class _Mss8210PCIAdapFaultStatus_Type(Integer32):
    """Custom type mss8210PCIAdapFaultStatus based on Integer32"""
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
        *(("isolated", 3),
          ("no-fault", 2),
          ("non-isolated", 4),
          ("unknown", 1))
    )


_Mss8210PCIAdapFaultStatus_Type.__name__ = "Integer32"
_Mss8210PCIAdapFaultStatus_Object = MibTableColumn
mss8210PCIAdapFaultStatus = _Mss8210PCIAdapFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 3, 2, 1, 7),
    _Mss8210PCIAdapFaultStatus_Type()
)
mss8210PCIAdapFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mss8210PCIAdapFaultStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mssServer8210ELSTrapV2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 0, 2)
)
mssServer8210ELSTrapV2.setObjects(
    ("PROTEON-MIB", "proElsSubSysEventMsg")
)
if mibBuilder.loadTexts:
    mssServer8210ELSTrapV2.setStatus(
        ""
    )

mss8210PCAdapTypeChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 0, 3)
)
mss8210PCAdapTypeChg.setObjects(
    ("MSSSERVER8210-MIB", "mss8210PCAdapType")
)
if mibBuilder.loadTexts:
    mss8210PCAdapTypeChg.setStatus(
        ""
    )

mss8210TempThresholdChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 0, 4)
)
mss8210TempThresholdChg.setObjects(
    ("MSSSERVER8210-MIB", "mss8210TempThresholdStatus")
)
if mibBuilder.loadTexts:
    mss8210TempThresholdChg.setStatus(
        ""
    )

mss8210PCIAdapStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 2, 0, 5)
)
mss8210PCIAdapStatusChg.setObjects(
      *(("MSSSERVER8210-MIB", "mss8210PCIAdapConfigType"),
        ("MSSSERVER8210-MIB", "mss8210PCIAdapOperStatus"),
        ("MSSSERVER8210-MIB", "mss8210PCIAdapDiagStatus"),
        ("MSSSERVER8210-MIB", "mss8210PCIAdapNetworkStatus"),
        ("MSSSERVER8210-MIB", "mss8210PCIAdapFaultStatus"))
)
if mibBuilder.loadTexts:
    mss8210PCIAdapStatusChg.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MSSSERVER8210-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "nwaysMSS": nwaysMSS,
       "mssServer8210": mssServer8210,
       "mssServer8210ELSTrapV2": mssServer8210ELSTrapV2,
       "mss8210PCAdapTypeChg": mss8210PCAdapTypeChg,
       "mss8210TempThresholdChg": mss8210TempThresholdChg,
       "mss8210PCIAdapStatusChg": mss8210PCIAdapStatusChg,
       "mss8210Prod": mss8210Prod,
       "mss8210ResetFlag": mss8210ResetFlag,
       "mss8210DRAMinstalled": mss8210DRAMinstalled,
       "mss8210NotifyStatus": mss8210NotifyStatus,
       "mss8210TempThresholdStatus": mss8210TempThresholdStatus,
       "mss8210PCAdapter": mss8210PCAdapter,
       "mss8210PCAdapNumSlot": mss8210PCAdapNumSlot,
       "mss8210PCAdapTable": mss8210PCAdapTable,
       "mss8210PCAdapEntry": mss8210PCAdapEntry,
       "mss8210PCAdapSlotNum": mss8210PCAdapSlotNum,
       "mss8210PCAdapType": mss8210PCAdapType,
       "mss8210PCIAdapter": mss8210PCIAdapter,
       "mss8210PCIAdapNumSlot": mss8210PCIAdapNumSlot,
       "mss8210PCIAdapTable": mss8210PCIAdapTable,
       "mss8210PCIAdapEntry": mss8210PCIAdapEntry,
       "mss8210PCIAdapSlotNum": mss8210PCIAdapSlotNum,
       "mss8210PCIAdapType": mss8210PCIAdapType,
       "mss8210PCIAdapConfigType": mss8210PCIAdapConfigType,
       "mss8210PCIAdapOperStatus": mss8210PCIAdapOperStatus,
       "mss8210PCIAdapDiagStatus": mss8210PCIAdapDiagStatus,
       "mss8210PCIAdapNetworkStatus": mss8210PCIAdapNetworkStatus,
       "mss8210PCIAdapFaultStatus": mss8210PCIAdapFaultStatus}
)
