# SNMP MIB module (RFC1406Ext-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1406Ext-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:29 2024
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

(cxDSX1Ext,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxDSX1Ext")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _Dsx1ExtMibLevel_Type(Integer32):
    """Custom type dsx1ExtMibLevel based on Integer32"""
    defaultValue = 0


_Dsx1ExtMibLevel_Object = MibScalar
dsx1ExtMibLevel = _Dsx1ExtMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 1),
    _Dsx1ExtMibLevel_Type()
)
dsx1ExtMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtMibLevel.setStatus("mandatory")
_Dsx1ExtCfgTable_Object = MibTable
dsx1ExtCfgTable = _Dsx1ExtCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10)
)
if mibBuilder.loadTexts:
    dsx1ExtCfgTable.setStatus("mandatory")
_Dsx1ExtCfgEntry_Object = MibTableRow
dsx1ExtCfgEntry = _Dsx1ExtCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1)
)
dsx1ExtCfgEntry.setIndexNames(
    (0, "RFC1406Ext-MIB", "dsx1ExtCfgLinkIndex"),
)
if mibBuilder.loadTexts:
    dsx1ExtCfgEntry.setStatus("mandatory")


class _Dsx1ExtCfgLinkIndex_Type(Integer32):
    """Custom type dsx1ExtCfgLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Dsx1ExtCfgLinkIndex_Type.__name__ = "Integer32"
_Dsx1ExtCfgLinkIndex_Object = MibTableColumn
dsx1ExtCfgLinkIndex = _Dsx1ExtCfgLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 1),
    _Dsx1ExtCfgLinkIndex_Type()
)
dsx1ExtCfgLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtCfgLinkIndex.setStatus("mandatory")


class _Dsx1ExtCfgPortStatus_Type(Integer32):
    """Custom type dsx1ExtCfgPortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Dsx1ExtCfgPortStatus_Type.__name__ = "Integer32"
_Dsx1ExtCfgPortStatus_Object = MibTableColumn
dsx1ExtCfgPortStatus = _Dsx1ExtCfgPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 10),
    _Dsx1ExtCfgPortStatus_Type()
)
dsx1ExtCfgPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtCfgPortStatus.setStatus("mandatory")


class _Dsx1ExtCfgTraps_Type(Integer32):
    """Custom type dsx1ExtCfgTraps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Dsx1ExtCfgTraps_Type.__name__ = "Integer32"
_Dsx1ExtCfgTraps_Object = MibTableColumn
dsx1ExtCfgTraps = _Dsx1ExtCfgTraps_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 11),
    _Dsx1ExtCfgTraps_Type()
)
dsx1ExtCfgTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtCfgTraps.setStatus("mandatory")


class _Dsx1ExtCfgLineBuildOut_Type(Integer32):
    """Custom type dsx1ExtCfgLineBuildOut based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Dsx1ExtCfgLineBuildOut_Type.__name__ = "Integer32"
_Dsx1ExtCfgLineBuildOut_Object = MibTableColumn
dsx1ExtCfgLineBuildOut = _Dsx1ExtCfgLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 12),
    _Dsx1ExtCfgLineBuildOut_Type()
)
dsx1ExtCfgLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ExtCfgLineBuildOut.setStatus("mandatory")


class _Dsx1ExtCfgCardType_Type(Integer32):
    """Custom type dsx1ExtCfgCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsx1ExtE1Card", 3),
          ("dsx1ExtNoCard", 1),
          ("dsx1ExtT1Card", 2))
    )


_Dsx1ExtCfgCardType_Type.__name__ = "Integer32"
_Dsx1ExtCfgCardType_Object = MibTableColumn
dsx1ExtCfgCardType = _Dsx1ExtCfgCardType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 50),
    _Dsx1ExtCfgCardType_Type()
)
dsx1ExtCfgCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtCfgCardType.setStatus("mandatory")
_Dsx1ExtCfgLossTxClock_Type = TimeTicks
_Dsx1ExtCfgLossTxClock_Object = MibTableColumn
dsx1ExtCfgLossTxClock = _Dsx1ExtCfgLossTxClock_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 51),
    _Dsx1ExtCfgLossTxClock_Type()
)
dsx1ExtCfgLossTxClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtCfgLossTxClock.setStatus("mandatory")
_Dsx1ExtCfgLossSync_Type = TimeTicks
_Dsx1ExtCfgLossSync_Object = MibTableColumn
dsx1ExtCfgLossSync = _Dsx1ExtCfgLossSync_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 52),
    _Dsx1ExtCfgLossSync_Type()
)
dsx1ExtCfgLossSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtCfgLossSync.setStatus("mandatory")
_Dsx1ExtCfgLossCarrier_Type = TimeTicks
_Dsx1ExtCfgLossCarrier_Object = MibTableColumn
dsx1ExtCfgLossCarrier = _Dsx1ExtCfgLossCarrier_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 53),
    _Dsx1ExtCfgLossCarrier_Type()
)
dsx1ExtCfgLossCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtCfgLossCarrier.setStatus("mandatory")
_Dsx1ExtCfgT18ZeroDetect_Type = TimeTicks
_Dsx1ExtCfgT18ZeroDetect_Object = MibTableColumn
dsx1ExtCfgT18ZeroDetect = _Dsx1ExtCfgT18ZeroDetect_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 54),
    _Dsx1ExtCfgT18ZeroDetect_Type()
)
dsx1ExtCfgT18ZeroDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtCfgT18ZeroDetect.setStatus("mandatory")
_Dsx1ExtCfgT116ZeroDetect_Type = TimeTicks
_Dsx1ExtCfgT116ZeroDetect_Object = MibTableColumn
dsx1ExtCfgT116ZeroDetect = _Dsx1ExtCfgT116ZeroDetect_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 55),
    _Dsx1ExtCfgT116ZeroDetect_Type()
)
dsx1ExtCfgT116ZeroDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtCfgT116ZeroDetect.setStatus("mandatory")
_Dsx1ExtCfgT1RxB8ZSCode_Type = TimeTicks
_Dsx1ExtCfgT1RxB8ZSCode_Object = MibTableColumn
dsx1ExtCfgT1RxB8ZSCode = _Dsx1ExtCfgT1RxB8ZSCode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 56),
    _Dsx1ExtCfgT1RxB8ZSCode_Type()
)
dsx1ExtCfgT1RxB8ZSCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtCfgT1RxB8ZSCode.setStatus("mandatory")
_Dsx1ExtCfgT1RxBlueAlarm_Type = TimeTicks
_Dsx1ExtCfgT1RxBlueAlarm_Object = MibTableColumn
dsx1ExtCfgT1RxBlueAlarm = _Dsx1ExtCfgT1RxBlueAlarm_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 57),
    _Dsx1ExtCfgT1RxBlueAlarm_Type()
)
dsx1ExtCfgT1RxBlueAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtCfgT1RxBlueAlarm.setStatus("mandatory")
_Dsx1ExtCfgT1RxYellowAlarm_Type = TimeTicks
_Dsx1ExtCfgT1RxYellowAlarm_Object = MibTableColumn
dsx1ExtCfgT1RxYellowAlarm = _Dsx1ExtCfgT1RxYellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 58),
    _Dsx1ExtCfgT1RxYellowAlarm_Type()
)
dsx1ExtCfgT1RxYellowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtCfgT1RxYellowAlarm.setStatus("mandatory")


class _Dsx1ExtCfgIoRegTest_Type(Integer32):
    """Custom type dsx1ExtCfgIoRegTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_Dsx1ExtCfgIoRegTest_Type.__name__ = "Integer32"
_Dsx1ExtCfgIoRegTest_Object = MibTableColumn
dsx1ExtCfgIoRegTest = _Dsx1ExtCfgIoRegTest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 59),
    _Dsx1ExtCfgIoRegTest_Type()
)
dsx1ExtCfgIoRegTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtCfgIoRegTest.setStatus("mandatory")


class _Dsx1ExtCfgSctRegTest_Type(Integer32):
    """Custom type dsx1ExtCfgSctRegTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_Dsx1ExtCfgSctRegTest_Type.__name__ = "Integer32"
_Dsx1ExtCfgSctRegTest_Object = MibTableColumn
dsx1ExtCfgSctRegTest = _Dsx1ExtCfgSctRegTest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 60),
    _Dsx1ExtCfgSctRegTest_Type()
)
dsx1ExtCfgSctRegTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtCfgSctRegTest.setStatus("mandatory")


class _Dsx1ExtCfgSctLatchRegTest_Type(Integer32):
    """Custom type dsx1ExtCfgSctLatchRegTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_Dsx1ExtCfgSctLatchRegTest_Type.__name__ = "Integer32"
_Dsx1ExtCfgSctLatchRegTest_Object = MibTableColumn
dsx1ExtCfgSctLatchRegTest = _Dsx1ExtCfgSctLatchRegTest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 61),
    _Dsx1ExtCfgSctLatchRegTest_Type()
)
dsx1ExtCfgSctLatchRegTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1ExtCfgSctLatchRegTest.setStatus("mandatory")
_Dsx1ExtCfgReinit_Type = Integer32
_Dsx1ExtCfgReinit_Object = MibTableColumn
dsx1ExtCfgReinit = _Dsx1ExtCfgReinit_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 53, 10, 1, 81),
    _Dsx1ExtCfgReinit_Type()
)
dsx1ExtCfgReinit.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dsx1ExtCfgReinit.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1406Ext-MIB",
    **{"dsx1ExtMibLevel": dsx1ExtMibLevel,
       "dsx1ExtCfgTable": dsx1ExtCfgTable,
       "dsx1ExtCfgEntry": dsx1ExtCfgEntry,
       "dsx1ExtCfgLinkIndex": dsx1ExtCfgLinkIndex,
       "dsx1ExtCfgPortStatus": dsx1ExtCfgPortStatus,
       "dsx1ExtCfgTraps": dsx1ExtCfgTraps,
       "dsx1ExtCfgLineBuildOut": dsx1ExtCfgLineBuildOut,
       "dsx1ExtCfgCardType": dsx1ExtCfgCardType,
       "dsx1ExtCfgLossTxClock": dsx1ExtCfgLossTxClock,
       "dsx1ExtCfgLossSync": dsx1ExtCfgLossSync,
       "dsx1ExtCfgLossCarrier": dsx1ExtCfgLossCarrier,
       "dsx1ExtCfgT18ZeroDetect": dsx1ExtCfgT18ZeroDetect,
       "dsx1ExtCfgT116ZeroDetect": dsx1ExtCfgT116ZeroDetect,
       "dsx1ExtCfgT1RxB8ZSCode": dsx1ExtCfgT1RxB8ZSCode,
       "dsx1ExtCfgT1RxBlueAlarm": dsx1ExtCfgT1RxBlueAlarm,
       "dsx1ExtCfgT1RxYellowAlarm": dsx1ExtCfgT1RxYellowAlarm,
       "dsx1ExtCfgIoRegTest": dsx1ExtCfgIoRegTest,
       "dsx1ExtCfgSctRegTest": dsx1ExtCfgSctRegTest,
       "dsx1ExtCfgSctLatchRegTest": dsx1ExtCfgSctLatchRegTest,
       "dsx1ExtCfgReinit": dsx1ExtCfgReinit}
)
