# SNMP MIB module (HPNSAHOTSWAPSUBSYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPNSAHOTSWAPSUBSYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:22 2024
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

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaHotSwap_ObjectIdentity = ObjectIdentity
hpnsaHotSwap = _HpnsaHotSwap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20)
)
_HpnsaHSMibRev_ObjectIdentity = ObjectIdentity
hpnsaHSMibRev = _HpnsaHSMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 1)
)


class _HpnsaHSMibRevMajor_Type(Integer32):
    """Custom type hpnsaHSMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaHSMibRevMajor_Type.__name__ = "Integer32"
_HpnsaHSMibRevMajor_Object = MibScalar
hpnsaHSMibRevMajor = _HpnsaHSMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 1, 1),
    _HpnsaHSMibRevMajor_Type()
)
hpnsaHSMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSMibRevMajor.setStatus("mandatory")


class _HpnsaHSMibRevMinor_Type(Integer32):
    """Custom type hpnsaHSMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaHSMibRevMinor_Type.__name__ = "Integer32"
_HpnsaHSMibRevMinor_Object = MibScalar
hpnsaHSMibRevMinor = _HpnsaHSMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 1, 2),
    _HpnsaHSMibRevMinor_Type()
)
hpnsaHSMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSMibRevMinor.setStatus("mandatory")
_HpnsaHSAgent_ObjectIdentity = ObjectIdentity
hpnsaHSAgent = _HpnsaHSAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 2)
)
_HpnsaHSAgentTable_Object = MibTable
hpnsaHSAgentTable = _HpnsaHSAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaHSAgentTable.setStatus("mandatory")
_HpnsaHSAgentEntry_Object = MibTableRow
hpnsaHSAgentEntry = _HpnsaHSAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 2, 1, 1)
)
hpnsaHSAgentEntry.setIndexNames(
    (0, "HPNSAHOTSWAPSUBSYSTEM-MIB", "hpnsaHSAgentIndex"),
)
if mibBuilder.loadTexts:
    hpnsaHSAgentEntry.setStatus("mandatory")


class _HpnsaHSAgentIndex_Type(Integer32):
    """Custom type hpnsaHSAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaHSAgentIndex_Type.__name__ = "Integer32"
_HpnsaHSAgentIndex_Object = MibTableColumn
hpnsaHSAgentIndex = _HpnsaHSAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 2, 1, 1, 1),
    _HpnsaHSAgentIndex_Type()
)
hpnsaHSAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSAgentIndex.setStatus("mandatory")


class _HpnsaHSAgentName_Type(DisplayString):
    """Custom type hpnsaHSAgentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaHSAgentName_Type.__name__ = "DisplayString"
_HpnsaHSAgentName_Object = MibTableColumn
hpnsaHSAgentName = _HpnsaHSAgentName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 2, 1, 1, 2),
    _HpnsaHSAgentName_Type()
)
hpnsaHSAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSAgentName.setStatus("mandatory")


class _HpnsaHSAgentVersion_Type(DisplayString):
    """Custom type hpnsaHSAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HpnsaHSAgentVersion_Type.__name__ = "DisplayString"
_HpnsaHSAgentVersion_Object = MibTableColumn
hpnsaHSAgentVersion = _HpnsaHSAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 2, 1, 1, 3),
    _HpnsaHSAgentVersion_Type()
)
hpnsaHSAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSAgentVersion.setStatus("mandatory")


class _HpnsaHSAgentDate_Type(OctetString):
    """Custom type hpnsaHSAgentDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnsaHSAgentDate_Type.__name__ = "OctetString"
_HpnsaHSAgentDate_Object = MibTableColumn
hpnsaHSAgentDate = _HpnsaHSAgentDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 2, 1, 1, 4),
    _HpnsaHSAgentDate_Type()
)
hpnsaHSAgentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSAgentDate.setStatus("mandatory")
_HpnsaHSModule_ObjectIdentity = ObjectIdentity
hpnsaHSModule = _HpnsaHSModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 3)
)
_HpnsaHSModuleTable_Object = MibTable
hpnsaHSModuleTable = _HpnsaHSModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 3, 1)
)
if mibBuilder.loadTexts:
    hpnsaHSModuleTable.setStatus("mandatory")
_HpnsaHSModuleEntry_Object = MibTableRow
hpnsaHSModuleEntry = _HpnsaHSModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 3, 1, 1)
)
hpnsaHSModuleEntry.setIndexNames(
    (0, "HPNSAHOTSWAPSUBSYSTEM-MIB", "hpnsaHSModuleIndex"),
)
if mibBuilder.loadTexts:
    hpnsaHSModuleEntry.setStatus("mandatory")
_HpnsaHSModuleIndex_Type = Integer32
_HpnsaHSModuleIndex_Object = MibTableColumn
hpnsaHSModuleIndex = _HpnsaHSModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 3, 1, 1, 1),
    _HpnsaHSModuleIndex_Type()
)
hpnsaHSModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSModuleIndex.setStatus("mandatory")


class _HpnsaHSModuleScsiCableType_Type(Integer32):
    """Custom type hpnsaHSModuleScsiCableType based on Integer32"""
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
        *(("error", 3),
          ("narrow", 2),
          ("no-cable", 4),
          ("wide", 1))
    )


_HpnsaHSModuleScsiCableType_Type.__name__ = "Integer32"
_HpnsaHSModuleScsiCableType_Object = MibTableColumn
hpnsaHSModuleScsiCableType = _HpnsaHSModuleScsiCableType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 3, 1, 1, 2),
    _HpnsaHSModuleScsiCableType_Type()
)
hpnsaHSModuleScsiCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSModuleScsiCableType.setStatus("mandatory")


class _HpnsaHSModuleTempStatus_Type(Integer32):
    """Custom type hpnsaHSModuleTempStatus based on Integer32"""
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
        *(("emergency", 4),
          ("error", 1),
          ("normal", 2),
          ("warning", 3))
    )


_HpnsaHSModuleTempStatus_Type.__name__ = "Integer32"
_HpnsaHSModuleTempStatus_Object = MibTableColumn
hpnsaHSModuleTempStatus = _HpnsaHSModuleTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 3, 1, 1, 3),
    _HpnsaHSModuleTempStatus_Type()
)
hpnsaHSModuleTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSModuleTempStatus.setStatus("mandatory")


class _HpnsaHSModuleSwitchState_Type(Integer32):
    """Custom type hpnsaHSModuleSwitchState based on Integer32"""
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


_HpnsaHSModuleSwitchState_Type.__name__ = "Integer32"
_HpnsaHSModuleSwitchState_Object = MibTableColumn
hpnsaHSModuleSwitchState = _HpnsaHSModuleSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 3, 1, 1, 4),
    _HpnsaHSModuleSwitchState_Type()
)
hpnsaHSModuleSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSModuleSwitchState.setStatus("mandatory")


class _HpnsaHSModuleDeviceStartup_Type(Integer32):
    """Custom type hpnsaHSModuleDeviceStartup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("at-poweron", 1),
          ("by-start-command", 2))
    )


_HpnsaHSModuleDeviceStartup_Type.__name__ = "Integer32"
_HpnsaHSModuleDeviceStartup_Object = MibTableColumn
hpnsaHSModuleDeviceStartup = _HpnsaHSModuleDeviceStartup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 3, 1, 1, 5),
    _HpnsaHSModuleDeviceStartup_Type()
)
hpnsaHSModuleDeviceStartup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSModuleDeviceStartup.setStatus("mandatory")


class _HpnsaHSModuleMiddleDrvAddr_Type(Integer32):
    """Custom type hpnsaHSModuleMiddleDrvAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 2),
          ("lowest", 1))
    )


_HpnsaHSModuleMiddleDrvAddr_Type.__name__ = "Integer32"
_HpnsaHSModuleMiddleDrvAddr_Object = MibTableColumn
hpnsaHSModuleMiddleDrvAddr = _HpnsaHSModuleMiddleDrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 3, 1, 1, 6),
    _HpnsaHSModuleMiddleDrvAddr_Type()
)
hpnsaHSModuleMiddleDrvAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSModuleMiddleDrvAddr.setStatus("mandatory")


class _HpnsaHSModuleHi8ScsiAddr_Type(Integer32):
    """Custom type hpnsaHSModuleHi8ScsiAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hi-range-9to15", 1),
          ("lo-range-1to7", 2))
    )


_HpnsaHSModuleHi8ScsiAddr_Type.__name__ = "Integer32"
_HpnsaHSModuleHi8ScsiAddr_Object = MibTableColumn
hpnsaHSModuleHi8ScsiAddr = _HpnsaHSModuleHi8ScsiAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 3, 1, 1, 7),
    _HpnsaHSModuleHi8ScsiAddr_Type()
)
hpnsaHSModuleHi8ScsiAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSModuleHi8ScsiAddr.setStatus("mandatory")
_HpnsaHSDev_ObjectIdentity = ObjectIdentity
hpnsaHSDev = _HpnsaHSDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 4)
)
_HpnsaHSDevTable_Object = MibTable
hpnsaHSDevTable = _HpnsaHSDevTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 4, 1)
)
if mibBuilder.loadTexts:
    hpnsaHSDevTable.setStatus("mandatory")
_HpnsaHSDevEntry_Object = MibTableRow
hpnsaHSDevEntry = _HpnsaHSDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 4, 1, 1)
)
hpnsaHSDevEntry.setIndexNames(
    (0, "HPNSAHOTSWAPSUBSYSTEM-MIB", "hpnsaHSDevModuleIndex"),
    (0, "HPNSAHOTSWAPSUBSYSTEM-MIB", "hpnsaHSDevIndex"),
)
if mibBuilder.loadTexts:
    hpnsaHSDevEntry.setStatus("mandatory")


class _HpnsaHSDevModuleIndex_Type(Integer32):
    """Custom type hpnsaHSDevModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaHSDevModuleIndex_Type.__name__ = "Integer32"
_HpnsaHSDevModuleIndex_Object = MibTableColumn
hpnsaHSDevModuleIndex = _HpnsaHSDevModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 4, 1, 1, 1),
    _HpnsaHSDevModuleIndex_Type()
)
hpnsaHSDevModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSDevModuleIndex.setStatus("mandatory")
_HpnsaHSDevIndex_Type = Integer32
_HpnsaHSDevIndex_Object = MibTableColumn
hpnsaHSDevIndex = _HpnsaHSDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 4, 1, 1, 2),
    _HpnsaHSDevIndex_Type()
)
hpnsaHSDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSDevIndex.setStatus("mandatory")


class _HpnsaHSDevExistence_Type(Integer32):
    """Custom type hpnsaHSDevExistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 2),
          ("present", 1))
    )


_HpnsaHSDevExistence_Type.__name__ = "Integer32"
_HpnsaHSDevExistence_Object = MibTableColumn
hpnsaHSDevExistence = _HpnsaHSDevExistence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 4, 1, 1, 3),
    _HpnsaHSDevExistence_Type()
)
hpnsaHSDevExistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSDevExistence.setStatus("mandatory")
_HpnsaHSDevScsiAddr_Type = Integer32
_HpnsaHSDevScsiAddr_Object = MibTableColumn
hpnsaHSDevScsiAddr = _HpnsaHSDevScsiAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 4, 1, 1, 4),
    _HpnsaHSDevScsiAddr_Type()
)
hpnsaHSDevScsiAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSDevScsiAddr.setStatus("mandatory")


class _HpnsaHSDevPowerStatus_Type(Integer32):
    """Custom type hpnsaHSDevPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("not-connected", 1))
    )


_HpnsaHSDevPowerStatus_Type.__name__ = "Integer32"
_HpnsaHSDevPowerStatus_Object = MibTableColumn
hpnsaHSDevPowerStatus = _HpnsaHSDevPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 4, 1, 1, 5),
    _HpnsaHSDevPowerStatus_Type()
)
hpnsaHSDevPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaHSDevPowerStatus.setStatus("mandatory")


class _HpnsaHSPwrAlertDelay_Type(Integer32):
    """Custom type hpnsaHSPwrAlertDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaHSPwrAlertDelay_Type.__name__ = "Integer32"
_HpnsaHSPwrAlertDelay_Object = MibScalar
hpnsaHSPwrAlertDelay = _HpnsaHSPwrAlertDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 20, 4, 2),
    _HpnsaHSPwrAlertDelay_Type()
)
hpnsaHSPwrAlertDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaHSPwrAlertDelay.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSAHOTSWAPSUBSYSTEM-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaHotSwap": hpnsaHotSwap,
       "hpnsaHSMibRev": hpnsaHSMibRev,
       "hpnsaHSMibRevMajor": hpnsaHSMibRevMajor,
       "hpnsaHSMibRevMinor": hpnsaHSMibRevMinor,
       "hpnsaHSAgent": hpnsaHSAgent,
       "hpnsaHSAgentTable": hpnsaHSAgentTable,
       "hpnsaHSAgentEntry": hpnsaHSAgentEntry,
       "hpnsaHSAgentIndex": hpnsaHSAgentIndex,
       "hpnsaHSAgentName": hpnsaHSAgentName,
       "hpnsaHSAgentVersion": hpnsaHSAgentVersion,
       "hpnsaHSAgentDate": hpnsaHSAgentDate,
       "hpnsaHSModule": hpnsaHSModule,
       "hpnsaHSModuleTable": hpnsaHSModuleTable,
       "hpnsaHSModuleEntry": hpnsaHSModuleEntry,
       "hpnsaHSModuleIndex": hpnsaHSModuleIndex,
       "hpnsaHSModuleScsiCableType": hpnsaHSModuleScsiCableType,
       "hpnsaHSModuleTempStatus": hpnsaHSModuleTempStatus,
       "hpnsaHSModuleSwitchState": hpnsaHSModuleSwitchState,
       "hpnsaHSModuleDeviceStartup": hpnsaHSModuleDeviceStartup,
       "hpnsaHSModuleMiddleDrvAddr": hpnsaHSModuleMiddleDrvAddr,
       "hpnsaHSModuleHi8ScsiAddr": hpnsaHSModuleHi8ScsiAddr,
       "hpnsaHSDev": hpnsaHSDev,
       "hpnsaHSDevTable": hpnsaHSDevTable,
       "hpnsaHSDevEntry": hpnsaHSDevEntry,
       "hpnsaHSDevModuleIndex": hpnsaHSDevModuleIndex,
       "hpnsaHSDevIndex": hpnsaHSDevIndex,
       "hpnsaHSDevExistence": hpnsaHSDevExistence,
       "hpnsaHSDevScsiAddr": hpnsaHSDevScsiAddr,
       "hpnsaHSDevPowerStatus": hpnsaHSDevPowerStatus,
       "hpnsaHSPwrAlertDelay": hpnsaHSPwrAlertDelay}
)
