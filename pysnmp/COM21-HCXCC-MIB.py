# SNMP MIB module (COM21-HCXCC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COM21-HCXCC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:34 2024
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

(com21,
 com21Hcx,
 com21Traps) = mibBuilder.importSymbols(
    "COM21-HCX-MIB",
    "com21",
    "com21Hcx",
    "com21Traps")

(hcxAlmSeverity,
 hcxEventLogTime) = mibBuilder.importSymbols(
    "COM21-HCXALM-MIB",
    "hcxAlmSeverity",
    "hcxEventLogTime")

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

com21HcxCc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 60)
)


# Types definitions



class PrimServiceState(Integer32):
    """Custom type PrimServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oos", 2))
    )





class Com21RowStatus(Integer32):
    """Custom type Com21RowStatus based on Integer32"""
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
        *(("active", 1),
          ("create", 2),
          ("deactive", 4),
          ("destroy", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Com21HcxCcUnitGroup_ObjectIdentity = ObjectIdentity
com21HcxCcUnitGroup = _Com21HcxCcUnitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61)
)


class _HcxCcShelfId_Type(Integer32):
    """Custom type hcxCcShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxCcShelfId_Type.__name__ = "Integer32"
_HcxCcShelfId_Object = MibScalar
hcxCcShelfId = _HcxCcShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 1),
    _HcxCcShelfId_Type()
)
hcxCcShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxCcShelfId.setStatus("current")
_HcxCcSlotId_Type = Integer32
_HcxCcSlotId_Object = MibScalar
hcxCcSlotId = _HcxCcSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 2),
    _HcxCcSlotId_Type()
)
hcxCcSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxCcSlotId.setStatus("current")


class _HcxCcHardwareVersion_Type(DisplayString):
    """Custom type hcxCcHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxCcHardwareVersion_Type.__name__ = "DisplayString"
_HcxCcHardwareVersion_Object = MibScalar
hcxCcHardwareVersion = _HcxCcHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 3),
    _HcxCcHardwareVersion_Type()
)
hcxCcHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxCcHardwareVersion.setStatus("current")


class _HcxCcBootVersion_Type(DisplayString):
    """Custom type hcxCcBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxCcBootVersion_Type.__name__ = "DisplayString"
_HcxCcBootVersion_Object = MibScalar
hcxCcBootVersion = _HcxCcBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 4),
    _HcxCcBootVersion_Type()
)
hcxCcBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxCcBootVersion.setStatus("current")


class _HcxSoftwareRevision_Type(DisplayString):
    """Custom type hcxSoftwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxSoftwareRevision_Type.__name__ = "DisplayString"
_HcxSoftwareRevision_Object = MibScalar
hcxSoftwareRevision = _HcxSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 6),
    _HcxSoftwareRevision_Type()
)
hcxSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxSoftwareRevision.setStatus("current")
_HcxControlPrimServState_Type = PrimServiceState
_HcxControlPrimServState_Object = MibScalar
hcxControlPrimServState = _HcxControlPrimServState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 7),
    _HcxControlPrimServState_Type()
)
hcxControlPrimServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxControlPrimServState.setStatus("current")


class _HcxControlSecServState_Type(DisplayString):
    """Custom type hcxControlSecServState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxControlSecServState_Type.__name__ = "DisplayString"
_HcxControlSecServState_Object = MibScalar
hcxControlSecServState = _HcxControlSecServState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 8),
    _HcxControlSecServState_Type()
)
hcxControlSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxControlSecServState.setStatus("current")


class _HcxCcDiagTestAction_Type(Integer32):
    """Custom type hcxCcDiagTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("nil", 1))
    )


_HcxCcDiagTestAction_Type.__name__ = "Integer32"
_HcxCcDiagTestAction_Object = MibScalar
hcxCcDiagTestAction = _HcxCcDiagTestAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 9),
    _HcxCcDiagTestAction_Type()
)
hcxCcDiagTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxCcDiagTestAction.setStatus("current")


class _HcxCcDiagTestResult_Type(Integer32):
    """Custom type hcxCcDiagTestResult based on Integer32"""
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
        *(("failure", 3),
          ("inprogress", 1),
          ("invalidState", 4),
          ("success", 2))
    )


_HcxCcDiagTestResult_Type.__name__ = "Integer32"
_HcxCcDiagTestResult_Object = MibScalar
hcxCcDiagTestResult = _HcxCcDiagTestResult_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 10),
    _HcxCcDiagTestResult_Type()
)
hcxCcDiagTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxCcDiagTestResult.setStatus("current")


class _HcxCcTestStatusLed_Type(Integer32):
    """Custom type hcxCcTestStatusLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_HcxCcTestStatusLed_Type.__name__ = "Integer32"
_HcxCcTestStatusLed_Object = MibScalar
hcxCcTestStatusLed = _HcxCcTestStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 11),
    _HcxCcTestStatusLed_Type()
)
hcxCcTestStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxCcTestStatusLed.setStatus("current")


class _HcxCcFaultStatusLed_Type(Integer32):
    """Custom type hcxCcFaultStatusLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_HcxCcFaultStatusLed_Type.__name__ = "Integer32"
_HcxCcFaultStatusLed_Object = MibScalar
hcxCcFaultStatusLed = _HcxCcFaultStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 12),
    _HcxCcFaultStatusLed_Type()
)
hcxCcFaultStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxCcFaultStatusLed.setStatus("current")


class _HcxCcEtherLinkStatusLed_Type(Integer32):
    """Custom type hcxCcEtherLinkStatusLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_HcxCcEtherLinkStatusLed_Type.__name__ = "Integer32"
_HcxCcEtherLinkStatusLed_Object = MibScalar
hcxCcEtherLinkStatusLed = _HcxCcEtherLinkStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 13),
    _HcxCcEtherLinkStatusLed_Type()
)
hcxCcEtherLinkStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxCcEtherLinkStatusLed.setStatus("current")


class _HcxCcFlashBackupPeriod_Type(Integer32):
    """Custom type hcxCcFlashBackupPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 900),
    )


_HcxCcFlashBackupPeriod_Type.__name__ = "Integer32"
_HcxCcFlashBackupPeriod_Object = MibScalar
hcxCcFlashBackupPeriod = _HcxCcFlashBackupPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 14),
    _HcxCcFlashBackupPeriod_Type()
)
hcxCcFlashBackupPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxCcFlashBackupPeriod.setStatus("current")


class _HcxCcFlashBackupAction_Type(Integer32):
    """Custom type hcxCcFlashBackupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("nil", 1))
    )


_HcxCcFlashBackupAction_Type.__name__ = "Integer32"
_HcxCcFlashBackupAction_Object = MibScalar
hcxCcFlashBackupAction = _HcxCcFlashBackupAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 15),
    _HcxCcFlashBackupAction_Type()
)
hcxCcFlashBackupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxCcFlashBackupAction.setStatus("current")


class _HcxCcFlashBackupResult_Type(Integer32):
    """Custom type hcxCcFlashBackupResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("inprogress", 1),
          ("success", 2))
    )


_HcxCcFlashBackupResult_Type.__name__ = "Integer32"
_HcxCcFlashBackupResult_Object = MibScalar
hcxCcFlashBackupResult = _HcxCcFlashBackupResult_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 16),
    _HcxCcFlashBackupResult_Type()
)
hcxCcFlashBackupResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxCcFlashBackupResult.setStatus("current")


class _HcxSwitchSoftwareRevision_Type(DisplayString):
    """Custom type hcxSwitchSoftwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxSwitchSoftwareRevision_Type.__name__ = "DisplayString"
_HcxSwitchSoftwareRevision_Object = MibScalar
hcxSwitchSoftwareRevision = _HcxSwitchSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 17),
    _HcxSwitchSoftwareRevision_Type()
)
hcxSwitchSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxSwitchSoftwareRevision.setStatus("current")


class _HcxSwitchHardwareRevision_Type(DisplayString):
    """Custom type hcxSwitchHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxSwitchHardwareRevision_Type.__name__ = "DisplayString"
_HcxSwitchHardwareRevision_Object = MibScalar
hcxSwitchHardwareRevision = _HcxSwitchHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 18),
    _HcxSwitchHardwareRevision_Type()
)
hcxSwitchHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxSwitchHardwareRevision.setStatus("current")


class _HcxSwitchSerialNumber_Type(DisplayString):
    """Custom type hcxSwitchSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxSwitchSerialNumber_Type.__name__ = "DisplayString"
_HcxSwitchSerialNumber_Object = MibScalar
hcxSwitchSerialNumber = _HcxSwitchSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 19),
    _HcxSwitchSerialNumber_Type()
)
hcxSwitchSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxSwitchSerialNumber.setStatus("current")


class _HcxNtpv3Control_Type(Integer32):
    """Custom type hcxNtpv3Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HcxNtpv3Control_Type.__name__ = "Integer32"
_HcxNtpv3Control_Object = MibScalar
hcxNtpv3Control = _HcxNtpv3Control_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 20),
    _HcxNtpv3Control_Type()
)
hcxNtpv3Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxNtpv3Control.setStatus("current")


class _HcxDiskFaultState_Type(Integer32):
    """Custom type hcxDiskFaultState based on Integer32"""
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
        *(("failed", 4),
          ("noFault", 1),
          ("notInstalled", 2),
          ("notMounted", 3))
    )


_HcxDiskFaultState_Type.__name__ = "Integer32"
_HcxDiskFaultState_Object = MibScalar
hcxDiskFaultState = _HcxDiskFaultState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 21),
    _HcxDiskFaultState_Type()
)
hcxDiskFaultState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxDiskFaultState.setStatus("current")


class _HcxDiskIdentifier_Type(DisplayString):
    """Custom type hcxDiskIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_HcxDiskIdentifier_Type.__name__ = "DisplayString"
_HcxDiskIdentifier_Object = MibScalar
hcxDiskIdentifier = _HcxDiskIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 22),
    _HcxDiskIdentifier_Type()
)
hcxDiskIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxDiskIdentifier.setStatus("current")
_HcxMibVersion_Type = Integer32
_HcxMibVersion_Object = MibScalar
hcxMibVersion = _HcxMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 61, 23),
    _HcxMibVersion_Type()
)
hcxMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxMibVersion.setStatus("current")
_Com21HcxCcNtpGroup_ObjectIdentity = ObjectIdentity
com21HcxCcNtpGroup = _Com21HcxCcNtpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 62)
)
_Com21HcxCcNtpTable_Object = MibTable
com21HcxCcNtpTable = _Com21HcxCcNtpTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 62, 1)
)
if mibBuilder.loadTexts:
    com21HcxCcNtpTable.setStatus("current")
_Com21HcxCcNtpEntry_Object = MibTableRow
com21HcxCcNtpEntry = _Com21HcxCcNtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 62, 1, 1)
)
com21HcxCcNtpEntry.setIndexNames(
    (0, "COM21-HCXCC-MIB", "hcxCcNtpServerIndex"),
)
if mibBuilder.loadTexts:
    com21HcxCcNtpEntry.setStatus("current")


class _HcxCcNtpServerIndex_Type(Integer32):
    """Custom type hcxCcNtpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_HcxCcNtpServerIndex_Type.__name__ = "Integer32"
_HcxCcNtpServerIndex_Object = MibTableColumn
hcxCcNtpServerIndex = _HcxCcNtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 62, 1, 1, 1),
    _HcxCcNtpServerIndex_Type()
)
hcxCcNtpServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxCcNtpServerIndex.setStatus("current")
_HcxCcNtpServerAddress_Type = IpAddress
_HcxCcNtpServerAddress_Object = MibTableColumn
hcxCcNtpServerAddress = _HcxCcNtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 62, 1, 1, 2),
    _HcxCcNtpServerAddress_Type()
)
hcxCcNtpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxCcNtpServerAddress.setStatus("current")
_HcxCcNtpServerAddrStatus_Type = Com21RowStatus
_HcxCcNtpServerAddrStatus_Object = MibTableColumn
hcxCcNtpServerAddrStatus = _HcxCcNtpServerAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 62, 1, 1, 3),
    _HcxCcNtpServerAddrStatus_Type()
)
hcxCcNtpServerAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcxCcNtpServerAddrStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hcxControlPrimServStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 10)
)
hcxControlPrimServStateChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXCC-MIB", "hcxCcShelfId"),
        ("COM21-HCXCC-MIB", "hcxCcSlotId"),
        ("COM21-HCXCC-MIB", "hcxControlPrimServState"))
)
if mibBuilder.loadTexts:
    hcxControlPrimServStateChange.setStatus(
        "current"
    )

hcxControlSecServStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 11)
)
hcxControlSecServStateChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXCC-MIB", "hcxCcShelfId"),
        ("COM21-HCXCC-MIB", "hcxCcSlotId"),
        ("COM21-HCXCC-MIB", "hcxControlSecServState"))
)
if mibBuilder.loadTexts:
    hcxControlSecServStateChange.setStatus(
        "current"
    )

hcxCcDiagTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 12)
)
hcxCcDiagTestComplete.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXCC-MIB", "hcxCcShelfId"),
        ("COM21-HCXCC-MIB", "hcxCcSlotId"),
        ("COM21-HCXCC-MIB", "hcxCcDiagTestResult"))
)
if mibBuilder.loadTexts:
    hcxCcDiagTestComplete.setStatus(
        "current"
    )

hcxCcTestStatusLedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 13)
)
hcxCcTestStatusLedChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXCC-MIB", "hcxCcShelfId"),
        ("COM21-HCXCC-MIB", "hcxCcSlotId"),
        ("COM21-HCXCC-MIB", "hcxCcTestStatusLed"))
)
if mibBuilder.loadTexts:
    hcxCcTestStatusLedChange.setStatus(
        "current"
    )

hcxCcFaultStatusLedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 14)
)
hcxCcFaultStatusLedChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXCC-MIB", "hcxCcShelfId"),
        ("COM21-HCXCC-MIB", "hcxCcSlotId"),
        ("COM21-HCXCC-MIB", "hcxCcFaultStatusLed"))
)
if mibBuilder.loadTexts:
    hcxCcFaultStatusLedChange.setStatus(
        "current"
    )

hcxCcEtherLinkStatusLedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 15)
)
hcxCcEtherLinkStatusLedChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXCC-MIB", "hcxCcShelfId"),
        ("COM21-HCXCC-MIB", "hcxCcSlotId"),
        ("COM21-HCXCC-MIB", "hcxCcEtherLinkStatusLed"))
)
if mibBuilder.loadTexts:
    hcxCcEtherLinkStatusLedChange.setStatus(
        "current"
    )

hcxCcFlashBackupComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 16)
)
hcxCcFlashBackupComplete.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXCC-MIB", "hcxCcShelfId"),
        ("COM21-HCXCC-MIB", "hcxCcSlotId"),
        ("COM21-HCXCC-MIB", "hcxCcFlashBackupResult"))
)
if mibBuilder.loadTexts:
    hcxCcFlashBackupComplete.setStatus(
        "current"
    )

hcxDiskAccessFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 17)
)
hcxDiskAccessFailure.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXCC-MIB", "hcxCcShelfId"),
        ("COM21-HCXCC-MIB", "hcxCcSlotId"),
        ("COM21-HCXCC-MIB", "hcxDiskFaultState"))
)
if mibBuilder.loadTexts:
    hcxDiskAccessFailure.setStatus(
        "current"
    )

hcxDiskAccessFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 18)
)
hcxDiskAccessFailClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXCC-MIB", "hcxCcShelfId"),
        ("COM21-HCXCC-MIB", "hcxCcSlotId"))
)
if mibBuilder.loadTexts:
    hcxDiskAccessFailClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COM21-HCXCC-MIB",
    **{"PrimServiceState": PrimServiceState,
       "Com21RowStatus": Com21RowStatus,
       "com21HcxCc": com21HcxCc,
       "com21HcxCcUnitGroup": com21HcxCcUnitGroup,
       "hcxCcShelfId": hcxCcShelfId,
       "hcxCcSlotId": hcxCcSlotId,
       "hcxCcHardwareVersion": hcxCcHardwareVersion,
       "hcxCcBootVersion": hcxCcBootVersion,
       "hcxSoftwareRevision": hcxSoftwareRevision,
       "hcxControlPrimServState": hcxControlPrimServState,
       "hcxControlSecServState": hcxControlSecServState,
       "hcxCcDiagTestAction": hcxCcDiagTestAction,
       "hcxCcDiagTestResult": hcxCcDiagTestResult,
       "hcxCcTestStatusLed": hcxCcTestStatusLed,
       "hcxCcFaultStatusLed": hcxCcFaultStatusLed,
       "hcxCcEtherLinkStatusLed": hcxCcEtherLinkStatusLed,
       "hcxCcFlashBackupPeriod": hcxCcFlashBackupPeriod,
       "hcxCcFlashBackupAction": hcxCcFlashBackupAction,
       "hcxCcFlashBackupResult": hcxCcFlashBackupResult,
       "hcxSwitchSoftwareRevision": hcxSwitchSoftwareRevision,
       "hcxSwitchHardwareRevision": hcxSwitchHardwareRevision,
       "hcxSwitchSerialNumber": hcxSwitchSerialNumber,
       "hcxNtpv3Control": hcxNtpv3Control,
       "hcxDiskFaultState": hcxDiskFaultState,
       "hcxDiskIdentifier": hcxDiskIdentifier,
       "hcxMibVersion": hcxMibVersion,
       "com21HcxCcNtpGroup": com21HcxCcNtpGroup,
       "com21HcxCcNtpTable": com21HcxCcNtpTable,
       "com21HcxCcNtpEntry": com21HcxCcNtpEntry,
       "hcxCcNtpServerIndex": hcxCcNtpServerIndex,
       "hcxCcNtpServerAddress": hcxCcNtpServerAddress,
       "hcxCcNtpServerAddrStatus": hcxCcNtpServerAddrStatus,
       "hcxControlPrimServStateChange": hcxControlPrimServStateChange,
       "hcxControlSecServStateChange": hcxControlSecServStateChange,
       "hcxCcDiagTestComplete": hcxCcDiagTestComplete,
       "hcxCcTestStatusLedChange": hcxCcTestStatusLedChange,
       "hcxCcFaultStatusLedChange": hcxCcFaultStatusLedChange,
       "hcxCcEtherLinkStatusLedChange": hcxCcEtherLinkStatusLedChange,
       "hcxCcFlashBackupComplete": hcxCcFlashBackupComplete,
       "hcxDiskAccessFailure": hcxDiskAccessFailure,
       "hcxDiskAccessFailClear": hcxDiskAccessFailClear}
)
