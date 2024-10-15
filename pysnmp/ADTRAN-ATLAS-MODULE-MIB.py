# SNMP MIB module (ADTRAN-ATLAS-MODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-ATLAS-MODULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:22 2024
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

(adATLASUnitFPStatus,
 adATLASUnitPortAddress,
 adATLASUnitSlotAddress) = mibBuilder.importSymbols(
    "ADTRAN-ATLAS-UNIT-MIB",
    "adATLASUnitFPStatus",
    "adATLASUnitPortAddress",
    "adATLASUnitSlotAddress")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

_Adtran_ObjectIdentity = ObjectIdentity
adtran = _Adtran_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664)
)
_AdMgmt_ObjectIdentity = ObjectIdentity
adMgmt = _AdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2)
)
_AdATLASmg_ObjectIdentity = ObjectIdentity
adATLASmg = _AdATLASmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154)
)
_AdGenATLASmg_ObjectIdentity = ObjectIdentity
adGenATLASmg = _AdGenATLASmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1)
)
_AdATLASModulemg_ObjectIdentity = ObjectIdentity
adATLASModulemg = _AdATLASModulemg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 6)
)
_AdATLASModuleInfoNumber_Type = Integer32
_AdATLASModuleInfoNumber_Object = MibScalar
adATLASModuleInfoNumber = _AdATLASModuleInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 6, 1),
    _AdATLASModuleInfoNumber_Type()
)
adATLASModuleInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASModuleInfoNumber.setStatus("mandatory")
_AdATLASModuleInfoTable_Object = MibTable
adATLASModuleInfoTable = _AdATLASModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 6, 2)
)
if mibBuilder.loadTexts:
    adATLASModuleInfoTable.setStatus("mandatory")
_AdATLASModuleInfoEntry_Object = MibTableRow
adATLASModuleInfoEntry = _AdATLASModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 6, 2, 1)
)
adATLASModuleInfoEntry.setIndexNames(
    (0, "ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoIndex"),
)
if mibBuilder.loadTexts:
    adATLASModuleInfoEntry.setStatus("mandatory")
_AdATLASModuleInfoIndex_Type = Integer32
_AdATLASModuleInfoIndex_Object = MibTableColumn
adATLASModuleInfoIndex = _AdATLASModuleInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 6, 2, 1, 1),
    _AdATLASModuleInfoIndex_Type()
)
adATLASModuleInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASModuleInfoIndex.setStatus("mandatory")
_AdATLASModuleInfoNumIfs_Type = Integer32
_AdATLASModuleInfoNumIfs_Object = MibTableColumn
adATLASModuleInfoNumIfs = _AdATLASModuleInfoNumIfs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 6, 2, 1, 2),
    _AdATLASModuleInfoNumIfs_Type()
)
adATLASModuleInfoNumIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASModuleInfoNumIfs.setStatus("mandatory")
_AdATLASModuleInfoNumRsrcs_Type = Integer32
_AdATLASModuleInfoNumRsrcs_Object = MibTableColumn
adATLASModuleInfoNumRsrcs = _AdATLASModuleInfoNumRsrcs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 6, 2, 1, 3),
    _AdATLASModuleInfoNumRsrcs_Type()
)
adATLASModuleInfoNumRsrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASModuleInfoNumRsrcs.setStatus("mandatory")
_AdATLASModuleInfoOID_Type = ObjectIdentifier
_AdATLASModuleInfoOID_Object = MibTableColumn
adATLASModuleInfoOID = _AdATLASModuleInfoOID_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 6, 2, 1, 4),
    _AdATLASModuleInfoOID_Type()
)
adATLASModuleInfoOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASModuleInfoOID.setStatus("mandatory")
_AdATLASModuleInfoPartNum_Type = DisplayString
_AdATLASModuleInfoPartNum_Object = MibTableColumn
adATLASModuleInfoPartNum = _AdATLASModuleInfoPartNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 6, 2, 1, 5),
    _AdATLASModuleInfoPartNum_Type()
)
adATLASModuleInfoPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASModuleInfoPartNum.setStatus("mandatory")
_AdATLASModuleInfoSerialNum_Type = DisplayString
_AdATLASModuleInfoSerialNum_Object = MibTableColumn
adATLASModuleInfoSerialNum = _AdATLASModuleInfoSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 6, 2, 1, 6),
    _AdATLASModuleInfoSerialNum_Type()
)
adATLASModuleInfoSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASModuleInfoSerialNum.setStatus("mandatory")
_AdATLASModuleInfoHardwareRev_Type = DisplayString
_AdATLASModuleInfoHardwareRev_Object = MibTableColumn
adATLASModuleInfoHardwareRev = _AdATLASModuleInfoHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 6, 2, 1, 7),
    _AdATLASModuleInfoHardwareRev_Type()
)
adATLASModuleInfoHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASModuleInfoHardwareRev.setStatus("mandatory")
_AdATLASModuleInfoFirmwareRev_Type = DisplayString
_AdATLASModuleInfoFirmwareRev_Object = MibTableColumn
adATLASModuleInfoFirmwareRev = _AdATLASModuleInfoFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 6, 2, 1, 8),
    _AdATLASModuleInfoFirmwareRev_Type()
)
adATLASModuleInfoFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASModuleInfoFirmwareRev.setStatus("mandatory")


class _AdATLASModuleInfoState_Type(Integer32):
    """Custom type adATLASModuleInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1))
    )


_AdATLASModuleInfoState_Type.__name__ = "Integer32"
_AdATLASModuleInfoState_Object = MibTableColumn
adATLASModuleInfoState = _AdATLASModuleInfoState_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 6, 2, 1, 9),
    _AdATLASModuleInfoState_Type()
)
adATLASModuleInfoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASModuleInfoState.setStatus("mandatory")


class _AdATLASModuleInfoStatus_Type(Integer32):
    """Custom type adATLASModuleInfoStatus based on Integer32"""
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
        *(("empty", 9),
          ("noResponse", 3),
          ("notReady", 5),
          ("notSupported", 7),
          ("offline", 2),
          ("online", 1),
          ("restarting", 6),
          ("standby", 8),
          ("unResponsiveOffline", 4))
    )


_AdATLASModuleInfoStatus_Type.__name__ = "Integer32"
_AdATLASModuleInfoStatus_Object = MibTableColumn
adATLASModuleInfoStatus = _AdATLASModuleInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 6, 2, 1, 10),
    _AdATLASModuleInfoStatus_Type()
)
adATLASModuleInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASModuleInfoStatus.setStatus("mandatory")


class _AdATLASModuleInfoFPStatus_Type(Integer32):
    """Custom type adATLASModuleInfoFPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdATLASModuleInfoFPStatus_Type.__name__ = "Integer32"
_AdATLASModuleInfoFPStatus_Object = MibTableColumn
adATLASModuleInfoFPStatus = _AdATLASModuleInfoFPStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 6, 2, 1, 11),
    _AdATLASModuleInfoFPStatus_Type()
)
adATLASModuleInfoFPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASModuleInfoFPStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

adATLASModuleOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400600)
)
adATLASModuleOffline.setObjects(
      *(("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoIndex"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"))
)
if mibBuilder.loadTexts:
    adATLASModuleOffline.setStatus(
        ""
    )

adATLASModuleOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400601)
)
adATLASModuleOnline.setObjects(
      *(("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoIndex"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"))
)
if mibBuilder.loadTexts:
    adATLASModuleOnline.setStatus(
        ""
    )

adATLASCbuBackupAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400602)
)
adATLASCbuBackupAttempt.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"))
)
if mibBuilder.loadTexts:
    adATLASCbuBackupAttempt.setStatus(
        ""
    )

adATLASCbuBackupAttemptFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400603)
)
adATLASCbuBackupAttemptFailed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"))
)
if mibBuilder.loadTexts:
    adATLASCbuBackupAttemptFailed.setStatus(
        ""
    )

adATLASCbuBackupActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400604)
)
adATLASCbuBackupActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"))
)
if mibBuilder.loadTexts:
    adATLASCbuBackupActive.setStatus(
        ""
    )

adATLASCbuPrimaryRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400605)
)
adATLASCbuPrimaryRestored.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"))
)
if mibBuilder.loadTexts:
    adATLASCbuPrimaryRestored.setStatus(
        ""
    )

adATLASCbuTestCallOriginated = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400606)
)
adATLASCbuTestCallOriginated.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"))
)
if mibBuilder.loadTexts:
    adATLASCbuTestCallOriginated.setStatus(
        ""
    )

adATLASCbuTestCallConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400607)
)
adATLASCbuTestCallConnected.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"))
)
if mibBuilder.loadTexts:
    adATLASCbuTestCallConnected.setStatus(
        ""
    )

adATLASCbuTestCallPassed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400608)
)
adATLASCbuTestCallPassed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"))
)
if mibBuilder.loadTexts:
    adATLASCbuTestCallPassed.setStatus(
        ""
    )

adATLASCbuTestCallFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400609)
)
adATLASCbuTestCallFailed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"))
)
if mibBuilder.loadTexts:
    adATLASCbuTestCallFailed.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-ATLAS-MODULE-MIB",
    **{"adtran": adtran,
       "adMgmt": adMgmt,
       "adATLASmg": adATLASmg,
       "adATLASModuleOffline": adATLASModuleOffline,
       "adATLASModuleOnline": adATLASModuleOnline,
       "adATLASCbuBackupAttempt": adATLASCbuBackupAttempt,
       "adATLASCbuBackupAttemptFailed": adATLASCbuBackupAttemptFailed,
       "adATLASCbuBackupActive": adATLASCbuBackupActive,
       "adATLASCbuPrimaryRestored": adATLASCbuPrimaryRestored,
       "adATLASCbuTestCallOriginated": adATLASCbuTestCallOriginated,
       "adATLASCbuTestCallConnected": adATLASCbuTestCallConnected,
       "adATLASCbuTestCallPassed": adATLASCbuTestCallPassed,
       "adATLASCbuTestCallFailed": adATLASCbuTestCallFailed,
       "adGenATLASmg": adGenATLASmg,
       "adATLASModulemg": adATLASModulemg,
       "adATLASModuleInfoNumber": adATLASModuleInfoNumber,
       "adATLASModuleInfoTable": adATLASModuleInfoTable,
       "adATLASModuleInfoEntry": adATLASModuleInfoEntry,
       "adATLASModuleInfoIndex": adATLASModuleInfoIndex,
       "adATLASModuleInfoNumIfs": adATLASModuleInfoNumIfs,
       "adATLASModuleInfoNumRsrcs": adATLASModuleInfoNumRsrcs,
       "adATLASModuleInfoOID": adATLASModuleInfoOID,
       "adATLASModuleInfoPartNum": adATLASModuleInfoPartNum,
       "adATLASModuleInfoSerialNum": adATLASModuleInfoSerialNum,
       "adATLASModuleInfoHardwareRev": adATLASModuleInfoHardwareRev,
       "adATLASModuleInfoFirmwareRev": adATLASModuleInfoFirmwareRev,
       "adATLASModuleInfoState": adATLASModuleInfoState,
       "adATLASModuleInfoStatus": adATLASModuleInfoStatus,
       "adATLASModuleInfoFPStatus": adATLASModuleInfoFPStatus}
)
