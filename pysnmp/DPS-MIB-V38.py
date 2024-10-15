# SNMP MIB module (DPS-MIB-V38) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DPS-MIB-V38
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:22 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpsInc_ObjectIdentity = ObjectIdentity
dpsInc = _DpsInc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682)
)
_DpsAlarmControl_ObjectIdentity = ObjectIdentity
dpsAlarmControl = _DpsAlarmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1)
)
_TmonXM_ObjectIdentity = ObjectIdentity
tmonXM = _TmonXM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1)
)
_TmonIdent_ObjectIdentity = ObjectIdentity
tmonIdent = _TmonIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 1)
)
_TmonIdentManufacturer_Type = DisplayString
_TmonIdentManufacturer_Object = MibScalar
tmonIdentManufacturer = _TmonIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 1, 1),
    _TmonIdentManufacturer_Type()
)
tmonIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonIdentManufacturer.setStatus("mandatory")
_TmonIdentModel_Type = DisplayString
_TmonIdentModel_Object = MibScalar
tmonIdentModel = _TmonIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 1, 2),
    _TmonIdentModel_Type()
)
tmonIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonIdentModel.setStatus("mandatory")
_TmonIdentSoftwareVersion_Type = DisplayString
_TmonIdentSoftwareVersion_Object = MibScalar
tmonIdentSoftwareVersion = _TmonIdentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 1, 3),
    _TmonIdentSoftwareVersion_Type()
)
tmonIdentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonIdentSoftwareVersion.setStatus("mandatory")
_TmonAlarmTable_Object = MibTable
tmonAlarmTable = _TmonAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tmonAlarmTable.setStatus("mandatory")
_TmonAlarmEntry_Object = MibTableRow
tmonAlarmEntry = _TmonAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1)
)
tmonAlarmEntry.setIndexNames(
    (0, "DPS-MIB-V38", "tmonAIndex"),
)
if mibBuilder.loadTexts:
    tmonAlarmEntry.setStatus("mandatory")
_TmonAIndex_Type = Integer32
_TmonAIndex_Object = MibTableColumn
tmonAIndex = _TmonAIndex_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 1),
    _TmonAIndex_Type()
)
tmonAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonAIndex.setStatus("mandatory")


class _TmonASite_Type(DisplayString):
    """Custom type tmonASite based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_TmonASite_Type.__name__ = "DisplayString"
_TmonASite_Object = MibTableColumn
tmonASite = _TmonASite_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 2),
    _TmonASite_Type()
)
tmonASite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonASite.setStatus("mandatory")


class _TmonADesc_Type(DisplayString):
    """Custom type tmonADesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_TmonADesc_Type.__name__ = "DisplayString"
_TmonADesc_Object = MibTableColumn
tmonADesc = _TmonADesc_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 3),
    _TmonADesc_Type()
)
tmonADesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonADesc.setStatus("mandatory")


class _TmonAState_Type(DisplayString):
    """Custom type tmonAState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_TmonAState_Type.__name__ = "DisplayString"
_TmonAState_Object = MibTableColumn
tmonAState = _TmonAState_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 4),
    _TmonAState_Type()
)
tmonAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonAState.setStatus("mandatory")


class _TmonASeverity_Type(DisplayString):
    """Custom type tmonASeverity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_TmonASeverity_Type.__name__ = "DisplayString"
_TmonASeverity_Object = MibTableColumn
tmonASeverity = _TmonASeverity_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 5),
    _TmonASeverity_Type()
)
tmonASeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonASeverity.setStatus("mandatory")


class _TmonAChgDate_Type(DisplayString):
    """Custom type tmonAChgDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_TmonAChgDate_Type.__name__ = "DisplayString"
_TmonAChgDate_Object = MibTableColumn
tmonAChgDate = _TmonAChgDate_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 6),
    _TmonAChgDate_Type()
)
tmonAChgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonAChgDate.setStatus("mandatory")


class _TmonAChgTime_Type(DisplayString):
    """Custom type tmonAChgTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_TmonAChgTime_Type.__name__ = "DisplayString"
_TmonAChgTime_Object = MibTableColumn
tmonAChgTime = _TmonAChgTime_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 7),
    _TmonAChgTime_Type()
)
tmonAChgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonAChgTime.setStatus("mandatory")


class _TmonAAuxDesc_Type(DisplayString):
    """Custom type tmonAAuxDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_TmonAAuxDesc_Type.__name__ = "DisplayString"
_TmonAAuxDesc_Object = MibTableColumn
tmonAAuxDesc = _TmonAAuxDesc_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 8),
    _TmonAAuxDesc_Type()
)
tmonAAuxDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonAAuxDesc.setStatus("mandatory")


class _TmonADispDesc_Type(DisplayString):
    """Custom type tmonADispDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_TmonADispDesc_Type.__name__ = "DisplayString"
_TmonADispDesc_Object = MibTableColumn
tmonADispDesc = _TmonADispDesc_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 9),
    _TmonADispDesc_Type()
)
tmonADispDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonADispDesc.setStatus("mandatory")
_TmonAPntType_Type = Integer32
_TmonAPntType_Object = MibTableColumn
tmonAPntType = _TmonAPntType_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 10),
    _TmonAPntType_Type()
)
tmonAPntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonAPntType.setStatus("mandatory")
_TmonAPort_Type = Integer32
_TmonAPort_Object = MibTableColumn
tmonAPort = _TmonAPort_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 11),
    _TmonAPort_Type()
)
tmonAPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonAPort.setStatus("mandatory")
_TmonAAddress_Type = Integer32
_TmonAAddress_Object = MibTableColumn
tmonAAddress = _TmonAAddress_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 12),
    _TmonAAddress_Type()
)
tmonAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonAAddress.setStatus("mandatory")
_TmonADisplay_Type = Integer32
_TmonADisplay_Object = MibTableColumn
tmonADisplay = _TmonADisplay_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 13),
    _TmonADisplay_Type()
)
tmonADisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonADisplay.setStatus("mandatory")
_TmonAPoint_Type = Integer32
_TmonAPoint_Object = MibTableColumn
tmonAPoint = _TmonAPoint_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 14),
    _TmonAPoint_Type()
)
tmonAPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonAPoint.setStatus("mandatory")
_TmonCommandGrid_ObjectIdentity = ObjectIdentity
tmonCommandGrid = _TmonCommandGrid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 3)
)
_TmonCPType_Type = Integer32
_TmonCPType_Object = MibScalar
tmonCPType = _TmonCPType_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 1),
    _TmonCPType_Type()
)
tmonCPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmonCPType.setStatus("mandatory")
_TmonCPort_Type = Integer32
_TmonCPort_Object = MibScalar
tmonCPort = _TmonCPort_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 2),
    _TmonCPort_Type()
)
tmonCPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmonCPort.setStatus("mandatory")
_TmonCAddress_Type = Integer32
_TmonCAddress_Object = MibScalar
tmonCAddress = _TmonCAddress_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 3),
    _TmonCAddress_Type()
)
tmonCAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmonCAddress.setStatus("mandatory")
_TmonCDisplay_Type = Integer32
_TmonCDisplay_Object = MibScalar
tmonCDisplay = _TmonCDisplay_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 4),
    _TmonCDisplay_Type()
)
tmonCDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmonCDisplay.setStatus("mandatory")


class _TmonCPoint_Type(Integer32):
    """Custom type tmonCPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TmonCPoint_Type.__name__ = "Integer32"
_TmonCPoint_Object = MibScalar
tmonCPoint = _TmonCPoint_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 5),
    _TmonCPoint_Type()
)
tmonCPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmonCPoint.setStatus("mandatory")
_TmonCEvent_Type = Integer32
_TmonCEvent_Object = MibScalar
tmonCEvent = _TmonCEvent_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 6),
    _TmonCEvent_Type()
)
tmonCEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmonCEvent.setStatus("mandatory")


class _TmonCAction_Type(Integer32):
    """Custom type tmonCAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("ack", 17),
          ("latch", 1),
          ("momentary", 3),
          ("release", 2),
          ("tag", 18),
          ("untag", 19))
    )


_TmonCAction_Type.__name__ = "Integer32"
_TmonCAction_Object = MibScalar
tmonCAction = _TmonCAction_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 7),
    _TmonCAction_Type()
)
tmonCAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmonCAction.setStatus("mandatory")


class _TmonCAuxText_Type(DisplayString):
    """Custom type tmonCAuxText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_TmonCAuxText_Type.__name__ = "DisplayString"
_TmonCAuxText_Object = MibScalar
tmonCAuxText = _TmonCAuxText_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 8),
    _TmonCAuxText_Type()
)
tmonCAuxText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmonCAuxText.setStatus("mandatory")


class _TmonCResult_Type(Integer32):
    """Custom type tmonCResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("pending", 3),
          ("success", 1))
    )


_TmonCResult_Type.__name__ = "Integer32"
_TmonCResult_Object = MibScalar
tmonCResult = _TmonCResult_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 9),
    _TmonCResult_Type()
)
tmonCResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonCResult.setStatus("mandatory")
_DpsRTU_ObjectIdentity = ObjectIdentity
dpsRTU = _DpsRTU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2)
)
_DpsRTUIdent_ObjectIdentity = ObjectIdentity
dpsRTUIdent = _DpsRTUIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 1)
)


class _DpsRTUManufacturer_Type(DisplayString):
    """Custom type dpsRTUManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_DpsRTUManufacturer_Type.__name__ = "DisplayString"
_DpsRTUManufacturer_Object = MibScalar
dpsRTUManufacturer = _DpsRTUManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 1, 1),
    _DpsRTUManufacturer_Type()
)
dpsRTUManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUManufacturer.setStatus("mandatory")


class _DpsRTUModel_Type(DisplayString):
    """Custom type dpsRTUModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_DpsRTUModel_Type.__name__ = "DisplayString"
_DpsRTUModel_Object = MibScalar
dpsRTUModel = _DpsRTUModel_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 1, 2),
    _DpsRTUModel_Type()
)
dpsRTUModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUModel.setStatus("mandatory")


class _DpsRTUFirmwareVersion_Type(DisplayString):
    """Custom type dpsRTUFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_DpsRTUFirmwareVersion_Type.__name__ = "DisplayString"
_DpsRTUFirmwareVersion_Object = MibScalar
dpsRTUFirmwareVersion = _DpsRTUFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 1, 3),
    _DpsRTUFirmwareVersion_Type()
)
dpsRTUFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUFirmwareVersion.setStatus("mandatory")


class _DpsRTUDateTime_Type(DisplayString):
    """Custom type dpsRTUDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(23, 23),
    )


_DpsRTUDateTime_Type.__name__ = "DisplayString"
_DpsRTUDateTime_Object = MibScalar
dpsRTUDateTime = _DpsRTUDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 1, 4),
    _DpsRTUDateTime_Type()
)
dpsRTUDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsRTUDateTime.setStatus("mandatory")


class _DpsRTUSyncReq_Type(Integer32):
    """Custom type dpsRTUSyncReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("sync", 1)
    )


_DpsRTUSyncReq_Type.__name__ = "Integer32"
_DpsRTUSyncReq_Object = MibScalar
dpsRTUSyncReq = _DpsRTUSyncReq_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 1, 5),
    _DpsRTUSyncReq_Type()
)
dpsRTUSyncReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsRTUSyncReq.setStatus("mandatory")
_DpsRTUDisplayGrid_Object = MibTable
dpsRTUDisplayGrid = _DpsRTUDisplayGrid_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dpsRTUDisplayGrid.setStatus("mandatory")
_DpsRTUDisplayEntry_Object = MibTableRow
dpsRTUDisplayEntry = _DpsRTUDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1)
)
dpsRTUDisplayEntry.setIndexNames(
    (0, "DPS-MIB-V38", "dpsRTUPort"),
    (0, "DPS-MIB-V38", "dpsRTUAddress"),
    (0, "DPS-MIB-V38", "dpsRTUDisplay"),
)
if mibBuilder.loadTexts:
    dpsRTUDisplayEntry.setStatus("mandatory")
_DpsRTUPort_Type = Integer32
_DpsRTUPort_Object = MibTableColumn
dpsRTUPort = _DpsRTUPort_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1, 1),
    _DpsRTUPort_Type()
)
dpsRTUPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUPort.setStatus("mandatory")
_DpsRTUAddress_Type = Integer32
_DpsRTUAddress_Object = MibTableColumn
dpsRTUAddress = _DpsRTUAddress_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1, 2),
    _DpsRTUAddress_Type()
)
dpsRTUAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUAddress.setStatus("mandatory")
_DpsRTUDisplay_Type = Integer32
_DpsRTUDisplay_Object = MibTableColumn
dpsRTUDisplay = _DpsRTUDisplay_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1, 3),
    _DpsRTUDisplay_Type()
)
dpsRTUDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUDisplay.setStatus("mandatory")


class _DpsRTUDispDesc_Type(DisplayString):
    """Custom type dpsRTUDispDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_DpsRTUDispDesc_Type.__name__ = "DisplayString"
_DpsRTUDispDesc_Object = MibTableColumn
dpsRTUDispDesc = _DpsRTUDispDesc_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1, 4),
    _DpsRTUDispDesc_Type()
)
dpsRTUDispDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUDispDesc.setStatus("mandatory")


class _DpsRTUPntMap_Type(DisplayString):
    """Custom type dpsRTUPntMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(71, 71),
    )


_DpsRTUPntMap_Type.__name__ = "DisplayString"
_DpsRTUPntMap_Object = MibTableColumn
dpsRTUPntMap = _DpsRTUPntMap_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1, 5),
    _DpsRTUPntMap_Type()
)
dpsRTUPntMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUPntMap.setStatus("mandatory")
_DpsRTUControlGrid_ObjectIdentity = ObjectIdentity
dpsRTUControlGrid = _DpsRTUControlGrid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 3)
)
_DpsRTUCPort_Type = Integer32
_DpsRTUCPort_Object = MibScalar
dpsRTUCPort = _DpsRTUCPort_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 3, 1),
    _DpsRTUCPort_Type()
)
dpsRTUCPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsRTUCPort.setStatus("mandatory")
_DpsRTUCAddress_Type = Integer32
_DpsRTUCAddress_Object = MibScalar
dpsRTUCAddress = _DpsRTUCAddress_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 3, 2),
    _DpsRTUCAddress_Type()
)
dpsRTUCAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsRTUCAddress.setStatus("mandatory")
_DpsRTUCDisplay_Type = Integer32
_DpsRTUCDisplay_Object = MibScalar
dpsRTUCDisplay = _DpsRTUCDisplay_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 3, 3),
    _DpsRTUCDisplay_Type()
)
dpsRTUCDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsRTUCDisplay.setStatus("mandatory")


class _DpsRTUCPoint_Type(Integer32):
    """Custom type dpsRTUCPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_DpsRTUCPoint_Type.__name__ = "Integer32"
_DpsRTUCPoint_Object = MibScalar
dpsRTUCPoint = _DpsRTUCPoint_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 3, 4),
    _DpsRTUCPoint_Type()
)
dpsRTUCPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsRTUCPoint.setStatus("mandatory")


class _DpsRTUCAction_Type(Integer32):
    """Custom type dpsRTUCAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("latch", 1),
          ("momentary", 3),
          ("release", 2))
    )


_DpsRTUCAction_Type.__name__ = "Integer32"
_DpsRTUCAction_Object = MibScalar
dpsRTUCAction = _DpsRTUCAction_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 3, 5),
    _DpsRTUCAction_Type()
)
dpsRTUCAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsRTUCAction.setStatus("mandatory")
_DpsRTUAlarmGrid_Object = MibTable
dpsRTUAlarmGrid = _DpsRTUAlarmGrid_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 5)
)
if mibBuilder.loadTexts:
    dpsRTUAlarmGrid.setStatus("mandatory")
_DpsRTUAlarmEntry_Object = MibTableRow
dpsRTUAlarmEntry = _DpsRTUAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1)
)
dpsRTUAlarmEntry.setIndexNames(
    (0, "DPS-MIB-V38", "dpsRTUAPort"),
    (0, "DPS-MIB-V38", "dpsRTUAAddress"),
    (0, "DPS-MIB-V38", "dpsRTUADisplay"),
    (0, "DPS-MIB-V38", "dpsRTUAPoint"),
)
if mibBuilder.loadTexts:
    dpsRTUAlarmEntry.setStatus("mandatory")
_DpsRTUAPort_Type = Integer32
_DpsRTUAPort_Object = MibTableColumn
dpsRTUAPort = _DpsRTUAPort_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 1),
    _DpsRTUAPort_Type()
)
dpsRTUAPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUAPort.setStatus("mandatory")
_DpsRTUAAddress_Type = Integer32
_DpsRTUAAddress_Object = MibTableColumn
dpsRTUAAddress = _DpsRTUAAddress_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 2),
    _DpsRTUAAddress_Type()
)
dpsRTUAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUAAddress.setStatus("mandatory")
_DpsRTUADisplay_Type = Integer32
_DpsRTUADisplay_Object = MibTableColumn
dpsRTUADisplay = _DpsRTUADisplay_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 3),
    _DpsRTUADisplay_Type()
)
dpsRTUADisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUADisplay.setStatus("mandatory")
_DpsRTUAPoint_Type = Integer32
_DpsRTUAPoint_Object = MibTableColumn
dpsRTUAPoint = _DpsRTUAPoint_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 4),
    _DpsRTUAPoint_Type()
)
dpsRTUAPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUAPoint.setStatus("mandatory")


class _DpsRTUAPntDesc_Type(DisplayString):
    """Custom type dpsRTUAPntDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(21, 21),
    )


_DpsRTUAPntDesc_Type.__name__ = "DisplayString"
_DpsRTUAPntDesc_Object = MibTableColumn
dpsRTUAPntDesc = _DpsRTUAPntDesc_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 5),
    _DpsRTUAPntDesc_Type()
)
dpsRTUAPntDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUAPntDesc.setStatus("mandatory")


class _DpsRTUAState_Type(DisplayString):
    """Custom type dpsRTUAState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_DpsRTUAState_Type.__name__ = "DisplayString"
_DpsRTUAState_Object = MibTableColumn
dpsRTUAState = _DpsRTUAState_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 6),
    _DpsRTUAState_Type()
)
dpsRTUAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUAState.setStatus("mandatory")

# Managed Objects groups


# Notification objects

tmonCRalarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 0, 10)
)
tmonCRalarmSet.setObjects(
      *(("DPS-MIB-V38", "tmonASite"),
        ("DPS-MIB-V38", "tmonADesc"),
        ("DPS-MIB-V38", "tmonAState"),
        ("DPS-MIB-V38", "tmonASeverity"),
        ("DPS-MIB-V38", "tmonAChgDate"),
        ("DPS-MIB-V38", "tmonAChgTime"),
        ("DPS-MIB-V38", "tmonAAuxDesc"),
        ("DPS-MIB-V38", "tmonADispDesc"),
        ("DPS-MIB-V38", "tmonAPntType"),
        ("DPS-MIB-V38", "tmonAPort"),
        ("DPS-MIB-V38", "tmonAAddress"),
        ("DPS-MIB-V38", "tmonADisplay"),
        ("DPS-MIB-V38", "tmonAPoint"),
        ("DPS-MIB-V38", "tmonCEvent"))
)
if mibBuilder.loadTexts:
    tmonCRalarmSet.setStatus(
        ""
    )

tmonCRalarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 0, 11)
)
tmonCRalarmClr.setObjects(
      *(("DPS-MIB-V38", "tmonASite"),
        ("DPS-MIB-V38", "tmonADesc"),
        ("DPS-MIB-V38", "tmonAState"),
        ("DPS-MIB-V38", "tmonASeverity"),
        ("DPS-MIB-V38", "tmonAChgDate"),
        ("DPS-MIB-V38", "tmonAChgTime"),
        ("DPS-MIB-V38", "tmonAAuxDesc"),
        ("DPS-MIB-V38", "tmonADispDesc"),
        ("DPS-MIB-V38", "tmonAPntType"),
        ("DPS-MIB-V38", "tmonAPort"),
        ("DPS-MIB-V38", "tmonAAddress"),
        ("DPS-MIB-V38", "tmonADisplay"),
        ("DPS-MIB-V38", "tmonAPoint"),
        ("DPS-MIB-V38", "tmonCEvent"))
)
if mibBuilder.loadTexts:
    tmonCRalarmClr.setStatus(
        ""
    )

tmonMJalarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 0, 12)
)
tmonMJalarmSet.setObjects(
      *(("DPS-MIB-V38", "tmonASite"),
        ("DPS-MIB-V38", "tmonADesc"),
        ("DPS-MIB-V38", "tmonAState"),
        ("DPS-MIB-V38", "tmonASeverity"),
        ("DPS-MIB-V38", "tmonAChgDate"),
        ("DPS-MIB-V38", "tmonAChgTime"),
        ("DPS-MIB-V38", "tmonAAuxDesc"),
        ("DPS-MIB-V38", "tmonADispDesc"),
        ("DPS-MIB-V38", "tmonAPntType"),
        ("DPS-MIB-V38", "tmonAPort"),
        ("DPS-MIB-V38", "tmonAAddress"),
        ("DPS-MIB-V38", "tmonADisplay"),
        ("DPS-MIB-V38", "tmonAPoint"),
        ("DPS-MIB-V38", "tmonCEvent"))
)
if mibBuilder.loadTexts:
    tmonMJalarmSet.setStatus(
        ""
    )

tmonMJalarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 0, 13)
)
tmonMJalarmClr.setObjects(
      *(("DPS-MIB-V38", "tmonASite"),
        ("DPS-MIB-V38", "tmonADesc"),
        ("DPS-MIB-V38", "tmonAState"),
        ("DPS-MIB-V38", "tmonASeverity"),
        ("DPS-MIB-V38", "tmonAChgDate"),
        ("DPS-MIB-V38", "tmonAChgTime"),
        ("DPS-MIB-V38", "tmonAAuxDesc"),
        ("DPS-MIB-V38", "tmonADispDesc"),
        ("DPS-MIB-V38", "tmonAPntType"),
        ("DPS-MIB-V38", "tmonAPort"),
        ("DPS-MIB-V38", "tmonAAddress"),
        ("DPS-MIB-V38", "tmonADisplay"),
        ("DPS-MIB-V38", "tmonAPoint"),
        ("DPS-MIB-V38", "tmonCEvent"))
)
if mibBuilder.loadTexts:
    tmonMJalarmClr.setStatus(
        ""
    )

tmonMNalarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 0, 14)
)
tmonMNalarmSet.setObjects(
      *(("DPS-MIB-V38", "tmonASite"),
        ("DPS-MIB-V38", "tmonADesc"),
        ("DPS-MIB-V38", "tmonAState"),
        ("DPS-MIB-V38", "tmonASeverity"),
        ("DPS-MIB-V38", "tmonAChgDate"),
        ("DPS-MIB-V38", "tmonAChgTime"),
        ("DPS-MIB-V38", "tmonAAuxDesc"),
        ("DPS-MIB-V38", "tmonADispDesc"),
        ("DPS-MIB-V38", "tmonAPntType"),
        ("DPS-MIB-V38", "tmonAPort"),
        ("DPS-MIB-V38", "tmonAAddress"),
        ("DPS-MIB-V38", "tmonADisplay"),
        ("DPS-MIB-V38", "tmonAPoint"),
        ("DPS-MIB-V38", "tmonCEvent"))
)
if mibBuilder.loadTexts:
    tmonMNalarmSet.setStatus(
        ""
    )

tmonMNalarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 0, 15)
)
tmonMNalarmClr.setObjects(
      *(("DPS-MIB-V38", "tmonASite"),
        ("DPS-MIB-V38", "tmonADesc"),
        ("DPS-MIB-V38", "tmonAState"),
        ("DPS-MIB-V38", "tmonASeverity"),
        ("DPS-MIB-V38", "tmonAChgDate"),
        ("DPS-MIB-V38", "tmonAChgTime"),
        ("DPS-MIB-V38", "tmonAAuxDesc"),
        ("DPS-MIB-V38", "tmonADispDesc"),
        ("DPS-MIB-V38", "tmonAPntType"),
        ("DPS-MIB-V38", "tmonAPort"),
        ("DPS-MIB-V38", "tmonAAddress"),
        ("DPS-MIB-V38", "tmonADisplay"),
        ("DPS-MIB-V38", "tmonAPoint"),
        ("DPS-MIB-V38", "tmonCEvent"))
)
if mibBuilder.loadTexts:
    tmonMNalarmClr.setStatus(
        ""
    )

tmonSTalarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 0, 16)
)
tmonSTalarmSet.setObjects(
      *(("DPS-MIB-V38", "tmonASite"),
        ("DPS-MIB-V38", "tmonADesc"),
        ("DPS-MIB-V38", "tmonAState"),
        ("DPS-MIB-V38", "tmonASeverity"),
        ("DPS-MIB-V38", "tmonAChgDate"),
        ("DPS-MIB-V38", "tmonAChgTime"),
        ("DPS-MIB-V38", "tmonAAuxDesc"),
        ("DPS-MIB-V38", "tmonADispDesc"),
        ("DPS-MIB-V38", "tmonAPntType"),
        ("DPS-MIB-V38", "tmonAPort"),
        ("DPS-MIB-V38", "tmonAAddress"),
        ("DPS-MIB-V38", "tmonADisplay"),
        ("DPS-MIB-V38", "tmonAPoint"),
        ("DPS-MIB-V38", "tmonCEvent"))
)
if mibBuilder.loadTexts:
    tmonSTalarmSet.setStatus(
        ""
    )

tmonSTalarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 0, 17)
)
tmonSTalarmClr.setObjects(
      *(("DPS-MIB-V38", "tmonASite"),
        ("DPS-MIB-V38", "tmonADesc"),
        ("DPS-MIB-V38", "tmonAState"),
        ("DPS-MIB-V38", "tmonASeverity"),
        ("DPS-MIB-V38", "tmonAChgDate"),
        ("DPS-MIB-V38", "tmonAChgTime"),
        ("DPS-MIB-V38", "tmonAAuxDesc"),
        ("DPS-MIB-V38", "tmonADispDesc"),
        ("DPS-MIB-V38", "tmonAPntType"),
        ("DPS-MIB-V38", "tmonAPort"),
        ("DPS-MIB-V38", "tmonAAddress"),
        ("DPS-MIB-V38", "tmonADisplay"),
        ("DPS-MIB-V38", "tmonAPoint"),
        ("DPS-MIB-V38", "tmonCEvent"))
)
if mibBuilder.loadTexts:
    tmonSTalarmClr.setStatus(
        ""
    )

dpsRTUPointSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 20)
)
dpsRTUPointSet.setObjects(
      *(("DPS-MIB-V38", "sysDescr"),
        ("DPS-MIB-V38", "sysLocation"),
        ("DPS-MIB-V38", "dpsRTUDateTime"),
        ("DPS-MIB-V38", "dpsRTUAPort"),
        ("DPS-MIB-V38", "dpsRTUAAddress"),
        ("DPS-MIB-V38", "dpsRTUADisplay"),
        ("DPS-MIB-V38", "dpsRTUAPoint"),
        ("DPS-MIB-V38", "dpsRTUAPntDesc"),
        ("DPS-MIB-V38", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUPointSet.setStatus(
        ""
    )

dpsRTUPointClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 21)
)
dpsRTUPointClr.setObjects(
      *(("DPS-MIB-V38", "sysDescr"),
        ("DPS-MIB-V38", "sysLocation"),
        ("DPS-MIB-V38", "dpsRTUDateTime"),
        ("DPS-MIB-V38", "dpsRTUAPort"),
        ("DPS-MIB-V38", "dpsRTUCAddress"),
        ("DPS-MIB-V38", "dpsRTUADisplay"),
        ("DPS-MIB-V38", "dpsRTUAPoint"),
        ("DPS-MIB-V38", "dpsRTUAPntDesc"),
        ("DPS-MIB-V38", "dpsRTUAState"))
)
if mibBuilder.loadTexts:
    dpsRTUPointClr.setStatus(
        ""
    )

dpsRTUsumPSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 101)
)
dpsRTUsumPSet.setObjects(
      *(("DPS-MIB-V38", "sysDescr"),
        ("DPS-MIB-V38", "sysLocation"),
        ("DPS-MIB-V38", "dpsRTUDateTime"))
)
if mibBuilder.loadTexts:
    dpsRTUsumPSet.setStatus(
        ""
    )

dpsRTUsumPClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 102)
)
dpsRTUsumPClr.setObjects(
      *(("DPS-MIB-V38", "sysDescr"),
        ("DPS-MIB-V38", "sysLocation"),
        ("DPS-MIB-V38", "dpsRTUDateTime"))
)
if mibBuilder.loadTexts:
    dpsRTUsumPClr.setStatus(
        ""
    )

dpsRTUcomFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 103)
)
dpsRTUcomFailed.setObjects(
      *(("DPS-MIB-V38", "sysDescr"),
        ("DPS-MIB-V38", "sysLocation"),
        ("DPS-MIB-V38", "dpsRTUDateTime"))
)
if mibBuilder.loadTexts:
    dpsRTUcomFailed.setStatus(
        ""
    )

dpsRTUcomRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 2, 0, 104)
)
dpsRTUcomRestored.setObjects(
      *(("DPS-MIB-V38", "sysDescr"),
        ("DPS-MIB-V38", "sysLocation"),
        ("DPS-MIB-V38", "dpsRTUDateTime"))
)
if mibBuilder.loadTexts:
    dpsRTUcomRestored.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DPS-MIB-V38",
    **{"dpsInc": dpsInc,
       "dpsAlarmControl": dpsAlarmControl,
       "tmonXM": tmonXM,
       "tmonCRalarmSet": tmonCRalarmSet,
       "tmonCRalarmClr": tmonCRalarmClr,
       "tmonMJalarmSet": tmonMJalarmSet,
       "tmonMJalarmClr": tmonMJalarmClr,
       "tmonMNalarmSet": tmonMNalarmSet,
       "tmonMNalarmClr": tmonMNalarmClr,
       "tmonSTalarmSet": tmonSTalarmSet,
       "tmonSTalarmClr": tmonSTalarmClr,
       "tmonIdent": tmonIdent,
       "tmonIdentManufacturer": tmonIdentManufacturer,
       "tmonIdentModel": tmonIdentModel,
       "tmonIdentSoftwareVersion": tmonIdentSoftwareVersion,
       "tmonAlarmTable": tmonAlarmTable,
       "tmonAlarmEntry": tmonAlarmEntry,
       "tmonAIndex": tmonAIndex,
       "tmonASite": tmonASite,
       "tmonADesc": tmonADesc,
       "tmonAState": tmonAState,
       "tmonASeverity": tmonASeverity,
       "tmonAChgDate": tmonAChgDate,
       "tmonAChgTime": tmonAChgTime,
       "tmonAAuxDesc": tmonAAuxDesc,
       "tmonADispDesc": tmonADispDesc,
       "tmonAPntType": tmonAPntType,
       "tmonAPort": tmonAPort,
       "tmonAAddress": tmonAAddress,
       "tmonADisplay": tmonADisplay,
       "tmonAPoint": tmonAPoint,
       "tmonCommandGrid": tmonCommandGrid,
       "tmonCPType": tmonCPType,
       "tmonCPort": tmonCPort,
       "tmonCAddress": tmonCAddress,
       "tmonCDisplay": tmonCDisplay,
       "tmonCPoint": tmonCPoint,
       "tmonCEvent": tmonCEvent,
       "tmonCAction": tmonCAction,
       "tmonCAuxText": tmonCAuxText,
       "tmonCResult": tmonCResult,
       "dpsRTU": dpsRTU,
       "dpsRTUPointSet": dpsRTUPointSet,
       "dpsRTUPointClr": dpsRTUPointClr,
       "dpsRTUsumPSet": dpsRTUsumPSet,
       "dpsRTUsumPClr": dpsRTUsumPClr,
       "dpsRTUcomFailed": dpsRTUcomFailed,
       "dpsRTUcomRestored": dpsRTUcomRestored,
       "dpsRTUIdent": dpsRTUIdent,
       "dpsRTUManufacturer": dpsRTUManufacturer,
       "dpsRTUModel": dpsRTUModel,
       "dpsRTUFirmwareVersion": dpsRTUFirmwareVersion,
       "dpsRTUDateTime": dpsRTUDateTime,
       "dpsRTUSyncReq": dpsRTUSyncReq,
       "dpsRTUDisplayGrid": dpsRTUDisplayGrid,
       "dpsRTUDisplayEntry": dpsRTUDisplayEntry,
       "dpsRTUPort": dpsRTUPort,
       "dpsRTUAddress": dpsRTUAddress,
       "dpsRTUDisplay": dpsRTUDisplay,
       "dpsRTUDispDesc": dpsRTUDispDesc,
       "dpsRTUPntMap": dpsRTUPntMap,
       "dpsRTUControlGrid": dpsRTUControlGrid,
       "dpsRTUCPort": dpsRTUCPort,
       "dpsRTUCAddress": dpsRTUCAddress,
       "dpsRTUCDisplay": dpsRTUCDisplay,
       "dpsRTUCPoint": dpsRTUCPoint,
       "dpsRTUCAction": dpsRTUCAction,
       "dpsRTUAlarmGrid": dpsRTUAlarmGrid,
       "dpsRTUAlarmEntry": dpsRTUAlarmEntry,
       "dpsRTUAPort": dpsRTUAPort,
       "dpsRTUAAddress": dpsRTUAAddress,
       "dpsRTUADisplay": dpsRTUADisplay,
       "dpsRTUAPoint": dpsRTUAPoint,
       "dpsRTUAPntDesc": dpsRTUAPntDesc,
       "dpsRTUAState": dpsRTUAState}
)
