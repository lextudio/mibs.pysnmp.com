# SNMP MIB module (CAT2600-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CAT2600-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:43 2024
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



class MacAddr(OctetString):
    """Custom type MacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cisco_ObjectIdentity = ObjectIdentity
cisco = _Cisco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9)
)
_CatProd_ObjectIdentity = ObjectIdentity
catProd = _CatProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1)
)
_Cat2600_ObjectIdentity = ObjectIdentity
cat2600 = _Cat2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111)
)
_Cat2600Ts_ObjectIdentity = ObjectIdentity
cat2600Ts = _Cat2600Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1)
)
_Cat2600TsObjectID_ObjectIdentity = ObjectIdentity
cat2600TsObjectID = _Cat2600TsObjectID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 1)
)
_Cat2600TsSysObjectID_ObjectIdentity = ObjectIdentity
cat2600TsSysObjectID = _Cat2600TsSysObjectID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 1, 1)
)
_Cat2600TsObjects_ObjectIdentity = ObjectIdentity
cat2600TsObjects = _Cat2600TsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2)
)
_Cat2600TsMain_ObjectIdentity = ObjectIdentity
cat2600TsMain = _Cat2600TsMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1)
)
_Cat2600TsConfig_ObjectIdentity = ObjectIdentity
cat2600TsConfig = _Cat2600TsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1)
)


class _Cat2600TsFwVer_Type(DisplayString):
    """Custom type cat2600TsFwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Cat2600TsFwVer_Type.__name__ = "DisplayString"
_Cat2600TsFwVer_Object = MibScalar
cat2600TsFwVer = _Cat2600TsFwVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 1),
    _Cat2600TsFwVer_Type()
)
cat2600TsFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsFwVer.setStatus("mandatory")


class _Cat2600TsHwVer_Type(DisplayString):
    """Custom type cat2600TsHwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Cat2600TsHwVer_Type.__name__ = "DisplayString"
_Cat2600TsHwVer_Object = MibScalar
cat2600TsHwVer = _Cat2600TsHwVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 2),
    _Cat2600TsHwVer_Type()
)
cat2600TsHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsHwVer.setStatus("mandatory")


class _Cat2600TsSerialNumber_Type(DisplayString):
    """Custom type cat2600TsSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Cat2600TsSerialNumber_Type.__name__ = "DisplayString"
_Cat2600TsSerialNumber_Object = MibScalar
cat2600TsSerialNumber = _Cat2600TsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 3),
    _Cat2600TsSerialNumber_Type()
)
cat2600TsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsSerialNumber.setStatus("mandatory")


class _Cat2600TsInstallationDate_Type(DisplayString):
    """Custom type cat2600TsInstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_Cat2600TsInstallationDate_Type.__name__ = "DisplayString"
_Cat2600TsInstallationDate_Object = MibScalar
cat2600TsInstallationDate = _Cat2600TsInstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 4),
    _Cat2600TsInstallationDate_Type()
)
cat2600TsInstallationDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsInstallationDate.setStatus("mandatory")
_Cat2600TsFwSize_Type = Integer32
_Cat2600TsFwSize_Object = MibScalar
cat2600TsFwSize = _Cat2600TsFwSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 5),
    _Cat2600TsFwSize_Type()
)
cat2600TsFwSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsFwSize.setStatus("mandatory")
_Cat2600TsFwCRC_Type = Integer32
_Cat2600TsFwCRC_Object = MibScalar
cat2600TsFwCRC = _Cat2600TsFwCRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 6),
    _Cat2600TsFwCRC_Type()
)
cat2600TsFwCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsFwCRC.setStatus("mandatory")


class _Cat2600TsFwManufacturer_Type(DisplayString):
    """Custom type cat2600TsFwManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Cat2600TsFwManufacturer_Type.__name__ = "DisplayString"
_Cat2600TsFwManufacturer_Object = MibScalar
cat2600TsFwManufacturer = _Cat2600TsFwManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 7),
    _Cat2600TsFwManufacturer_Type()
)
cat2600TsFwManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsFwManufacturer.setStatus("mandatory")
_Cat2600TsIpAddr_Type = IpAddress
_Cat2600TsIpAddr_Object = MibScalar
cat2600TsIpAddr = _Cat2600TsIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 8),
    _Cat2600TsIpAddr_Type()
)
cat2600TsIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsIpAddr.setStatus("mandatory")
_Cat2600TsNetMask_Type = IpAddress
_Cat2600TsNetMask_Object = MibScalar
cat2600TsNetMask = _Cat2600TsNetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 9),
    _Cat2600TsNetMask_Type()
)
cat2600TsNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsNetMask.setStatus("mandatory")
_Cat2600TsDefaultGateway_Type = IpAddress
_Cat2600TsDefaultGateway_Object = MibScalar
cat2600TsDefaultGateway = _Cat2600TsDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 10),
    _Cat2600TsDefaultGateway_Type()
)
cat2600TsDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsDefaultGateway.setStatus("mandatory")
_Cat2600TsTrapRcvrTable_Object = MibTable
cat2600TsTrapRcvrTable = _Cat2600TsTrapRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 14)
)
if mibBuilder.loadTexts:
    cat2600TsTrapRcvrTable.setStatus("mandatory")
_Cat2600TsTrapRcvrEntry_Object = MibTableRow
cat2600TsTrapRcvrEntry = _Cat2600TsTrapRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 14, 1)
)
cat2600TsTrapRcvrEntry.setIndexNames(
    (0, "CAT2600-MIB", "cat2600TsTrapRcvrIndex"),
)
if mibBuilder.loadTexts:
    cat2600TsTrapRcvrEntry.setStatus("mandatory")


class _Cat2600TsTrapRcvrIndex_Type(Integer32):
    """Custom type cat2600TsTrapRcvrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cat2600TsTrapRcvrIndex_Type.__name__ = "Integer32"
_Cat2600TsTrapRcvrIndex_Object = MibTableColumn
cat2600TsTrapRcvrIndex = _Cat2600TsTrapRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 14, 1, 1),
    _Cat2600TsTrapRcvrIndex_Type()
)
cat2600TsTrapRcvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsTrapRcvrIndex.setStatus("mandatory")


class _Cat2600TsTrapRcvrStatus_Type(Integer32):
    """Custom type cat2600TsTrapRcvrStatus based on Integer32"""
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
        *(("create", 4),
          ("invalid", 3),
          ("other", 1),
          ("valid", 2))
    )


_Cat2600TsTrapRcvrStatus_Type.__name__ = "Integer32"
_Cat2600TsTrapRcvrStatus_Object = MibTableColumn
cat2600TsTrapRcvrStatus = _Cat2600TsTrapRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 14, 1, 2),
    _Cat2600TsTrapRcvrStatus_Type()
)
cat2600TsTrapRcvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsTrapRcvrStatus.setStatus("mandatory")
_Cat2600TsTrapRcvrIpAddress_Type = IpAddress
_Cat2600TsTrapRcvrIpAddress_Object = MibTableColumn
cat2600TsTrapRcvrIpAddress = _Cat2600TsTrapRcvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 14, 1, 3),
    _Cat2600TsTrapRcvrIpAddress_Type()
)
cat2600TsTrapRcvrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsTrapRcvrIpAddress.setStatus("mandatory")


class _Cat2600TsTrapRcvrComm_Type(DisplayString):
    """Custom type cat2600TsTrapRcvrComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cat2600TsTrapRcvrComm_Type.__name__ = "DisplayString"
_Cat2600TsTrapRcvrComm_Object = MibTableColumn
cat2600TsTrapRcvrComm = _Cat2600TsTrapRcvrComm_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 14, 1, 4),
    _Cat2600TsTrapRcvrComm_Type()
)
cat2600TsTrapRcvrComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsTrapRcvrComm.setStatus("mandatory")


class _Cat2600TsTrapRcvrDmns_Type(OctetString):
    """Custom type cat2600TsTrapRcvrDmns based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Cat2600TsTrapRcvrDmns_Type.__name__ = "OctetString"
_Cat2600TsTrapRcvrDmns_Object = MibTableColumn
cat2600TsTrapRcvrDmns = _Cat2600TsTrapRcvrDmns_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 14, 1, 5),
    _Cat2600TsTrapRcvrDmns_Type()
)
cat2600TsTrapRcvrDmns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsTrapRcvrDmns.setStatus("mandatory")


class _Cat2600TsPingInterval_Type(Integer32):
    """Custom type cat2600TsPingInterval based on Integer32"""
    defaultValue = 600


_Cat2600TsPingInterval_Object = MibScalar
cat2600TsPingInterval = _Cat2600TsPingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 19),
    _Cat2600TsPingInterval_Type()
)
cat2600TsPingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsPingInterval.setStatus("mandatory")
_Cat2600TsTapPort_Type = Integer32
_Cat2600TsTapPort_Object = MibScalar
cat2600TsTapPort = _Cat2600TsTapPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 20),
    _Cat2600TsTapPort_Type()
)
cat2600TsTapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsTapPort.setStatus("mandatory")
_Cat2600TsTapMonitoredPort_Type = Integer32
_Cat2600TsTapMonitoredPort_Object = MibScalar
cat2600TsTapMonitoredPort = _Cat2600TsTapMonitoredPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 21),
    _Cat2600TsTapMonitoredPort_Type()
)
cat2600TsTapMonitoredPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsTapMonitoredPort.setStatus("mandatory")
_Cat2600TsCrcThresholdHi_Type = Integer32
_Cat2600TsCrcThresholdHi_Object = MibScalar
cat2600TsCrcThresholdHi = _Cat2600TsCrcThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 22),
    _Cat2600TsCrcThresholdHi_Type()
)
cat2600TsCrcThresholdHi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsCrcThresholdHi.setStatus("mandatory")
_Cat2600TsCrcThresholdLow_Type = Integer32
_Cat2600TsCrcThresholdLow_Object = MibScalar
cat2600TsCrcThresholdLow = _Cat2600TsCrcThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 23),
    _Cat2600TsCrcThresholdLow_Type()
)
cat2600TsCrcThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsCrcThresholdLow.setStatus("mandatory")


class _Cat2600TsPortSwitchModeChangeTrapEnable_Type(Integer32):
    """Custom type cat2600TsPortSwitchModeChangeTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Cat2600TsPortSwitchModeChangeTrapEnable_Type.__name__ = "Integer32"
_Cat2600TsPortSwitchModeChangeTrapEnable_Object = MibScalar
cat2600TsPortSwitchModeChangeTrapEnable = _Cat2600TsPortSwitchModeChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 24),
    _Cat2600TsPortSwitchModeChangeTrapEnable_Type()
)
cat2600TsPortSwitchModeChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsPortSwitchModeChangeTrapEnable.setStatus("mandatory")
_Cat2600TsTrendThreshold_Type = Integer32
_Cat2600TsTrendThreshold_Object = MibScalar
cat2600TsTrendThreshold = _Cat2600TsTrendThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 25),
    _Cat2600TsTrendThreshold_Type()
)
cat2600TsTrendThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsTrendThreshold.setStatus("mandatory")


class _Cat2600TsSamplingPeriod_Type(Integer32):
    """Custom type cat2600TsSamplingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_Cat2600TsSamplingPeriod_Type.__name__ = "Integer32"
_Cat2600TsSamplingPeriod_Object = MibScalar
cat2600TsSamplingPeriod = _Cat2600TsSamplingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 26),
    _Cat2600TsSamplingPeriod_Type()
)
cat2600TsSamplingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsSamplingPeriod.setStatus("mandatory")
_Cat2600TsNumberUFC_Type = Integer32
_Cat2600TsNumberUFC_Object = MibScalar
cat2600TsNumberUFC = _Cat2600TsNumberUFC_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 1, 27),
    _Cat2600TsNumberUFC_Type()
)
cat2600TsNumberUFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsNumberUFC.setStatus("mandatory")
_Cat2600TsSys_ObjectIdentity = ObjectIdentity
cat2600TsSys = _Cat2600TsSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 2)
)
_Cat2600TsNumPorts_Type = Integer32
_Cat2600TsNumPorts_Object = MibScalar
cat2600TsNumPorts = _Cat2600TsNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 2, 1),
    _Cat2600TsNumPorts_Type()
)
cat2600TsNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsNumPorts.setStatus("mandatory")
_Cat2600TsNumStations_Type = Integer32
_Cat2600TsNumStations_Object = MibScalar
cat2600TsNumStations = _Cat2600TsNumStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 2, 2),
    _Cat2600TsNumStations_Type()
)
cat2600TsNumStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsNumStations.setStatus("mandatory")
_Cat2600TsMostStations_Type = Integer32
_Cat2600TsMostStations_Object = MibScalar
cat2600TsMostStations = _Cat2600TsMostStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 2, 3),
    _Cat2600TsMostStations_Type()
)
cat2600TsMostStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsMostStations.setStatus("mandatory")
_Cat2600TsMaxStations_Type = Integer32
_Cat2600TsMaxStations_Object = MibScalar
cat2600TsMaxStations = _Cat2600TsMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 2, 4),
    _Cat2600TsMaxStations_Type()
)
cat2600TsMaxStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsMaxStations.setStatus("mandatory")


class _Cat2600TsReset_Type(Integer32):
    """Custom type cat2600TsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hardReset", 2),
          ("running", 1),
          ("softReset", 3))
    )


_Cat2600TsReset_Type.__name__ = "Integer32"
_Cat2600TsReset_Object = MibScalar
cat2600TsReset = _Cat2600TsReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 2, 5),
    _Cat2600TsReset_Type()
)
cat2600TsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsReset.setStatus("mandatory")
_Cat2600TsNumResets_Type = Counter32
_Cat2600TsNumResets_Object = MibScalar
cat2600TsNumResets = _Cat2600TsNumResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 2, 6),
    _Cat2600TsNumResets_Type()
)
cat2600TsNumResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsNumResets.setStatus("mandatory")


class _Cat2600TsAddrAgingTime_Type(Integer32):
    """Custom type cat2600TsAddrAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Cat2600TsAddrAgingTime_Type.__name__ = "Integer32"
_Cat2600TsAddrAgingTime_Object = MibScalar
cat2600TsAddrAgingTime = _Cat2600TsAddrAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 2, 7),
    _Cat2600TsAddrAgingTime_Type()
)
cat2600TsAddrAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsAddrAgingTime.setStatus("mandatory")


class _Cat2600TsSysTemperature_Type(Integer32):
    """Custom type cat2600TsSysTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("toohigh", 2))
    )


_Cat2600TsSysTemperature_Type.__name__ = "Integer32"
_Cat2600TsSysTemperature_Object = MibScalar
cat2600TsSysTemperature = _Cat2600TsSysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 2, 11),
    _Cat2600TsSysTemperature_Type()
)
cat2600TsSysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsSysTemperature.setStatus("mandatory")
_Cat2600TsInstalledMemory_Type = Integer32
_Cat2600TsInstalledMemory_Object = MibScalar
cat2600TsInstalledMemory = _Cat2600TsInstalledMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 2, 12),
    _Cat2600TsInstalledMemory_Type()
)
cat2600TsInstalledMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsInstalledMemory.setStatus("mandatory")


class _Cat2600TsSysCurTime_Type(DisplayString):
    """Custom type cat2600TsSysCurTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Cat2600TsSysCurTime_Type.__name__ = "DisplayString"
_Cat2600TsSysCurTime_Object = MibScalar
cat2600TsSysCurTime = _Cat2600TsSysCurTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 1, 2, 13),
    _Cat2600TsSysCurTime_Type()
)
cat2600TsSysCurTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsSysCurTime.setStatus("mandatory")
_Cat2600TsPort_ObjectIdentity = ObjectIdentity
cat2600TsPort = _Cat2600TsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2)
)
_Cat2600TsPortTable_Object = MibTable
cat2600TsPortTable = _Cat2600TsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cat2600TsPortTable.setStatus("mandatory")
_Cat2600TsPortEntry_Object = MibTableRow
cat2600TsPortEntry = _Cat2600TsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1)
)
cat2600TsPortEntry.setIndexNames(
    (0, "CAT2600-MIB", "cat2600TsPortIndex"),
)
if mibBuilder.loadTexts:
    cat2600TsPortEntry.setStatus("mandatory")


class _Cat2600TsPortIndex_Type(Integer32):
    """Custom type cat2600TsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Cat2600TsPortIndex_Type.__name__ = "Integer32"
_Cat2600TsPortIndex_Object = MibTableColumn
cat2600TsPortIndex = _Cat2600TsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 1),
    _Cat2600TsPortIndex_Type()
)
cat2600TsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortIndex.setStatus("mandatory")
_Cat2600TsPortRcvLocalFrames_Type = Counter32
_Cat2600TsPortRcvLocalFrames_Object = MibTableColumn
cat2600TsPortRcvLocalFrames = _Cat2600TsPortRcvLocalFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 2),
    _Cat2600TsPortRcvLocalFrames_Type()
)
cat2600TsPortRcvLocalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortRcvLocalFrames.setStatus("mandatory")
_Cat2600TsPortForwardedFrames_Type = Counter32
_Cat2600TsPortForwardedFrames_Object = MibTableColumn
cat2600TsPortForwardedFrames = _Cat2600TsPortForwardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 3),
    _Cat2600TsPortForwardedFrames_Type()
)
cat2600TsPortForwardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortForwardedFrames.setStatus("mandatory")
_Cat2600TsPortMostStations_Type = Counter32
_Cat2600TsPortMostStations_Object = MibTableColumn
cat2600TsPortMostStations = _Cat2600TsPortMostStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 4),
    _Cat2600TsPortMostStations_Type()
)
cat2600TsPortMostStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortMostStations.setStatus("mandatory")
_Cat2600TsPortMaxStations_Type = Counter32
_Cat2600TsPortMaxStations_Object = MibTableColumn
cat2600TsPortMaxStations = _Cat2600TsPortMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 5),
    _Cat2600TsPortMaxStations_Type()
)
cat2600TsPortMaxStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortMaxStations.setStatus("mandatory")
_Cat2600TsPortSWHandledFrames_Type = Counter32
_Cat2600TsPortSWHandledFrames_Object = MibTableColumn
cat2600TsPortSWHandledFrames = _Cat2600TsPortSWHandledFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 6),
    _Cat2600TsPortSWHandledFrames_Type()
)
cat2600TsPortSWHandledFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortSWHandledFrames.setStatus("mandatory")
_Cat2600TsPortLocalStations_Type = Counter32
_Cat2600TsPortLocalStations_Object = MibTableColumn
cat2600TsPortLocalStations = _Cat2600TsPortLocalStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 7),
    _Cat2600TsPortLocalStations_Type()
)
cat2600TsPortLocalStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortLocalStations.setStatus("mandatory")
_Cat2600TsPortRemoteStations_Type = Counter32
_Cat2600TsPortRemoteStations_Object = MibTableColumn
cat2600TsPortRemoteStations = _Cat2600TsPortRemoteStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 8),
    _Cat2600TsPortRemoteStations_Type()
)
cat2600TsPortRemoteStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortRemoteStations.setStatus("mandatory")
_Cat2600TsPortUnknownStaFrames_Type = Counter32
_Cat2600TsPortUnknownStaFrames_Object = MibTableColumn
cat2600TsPortUnknownStaFrames = _Cat2600TsPortUnknownStaFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 9),
    _Cat2600TsPortUnknownStaFrames_Type()
)
cat2600TsPortUnknownStaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortUnknownStaFrames.setStatus("mandatory")


class _Cat2600TsPortResetStats_Type(Integer32):
    """Custom type cat2600TsPortResetStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 3),
          ("running", 2))
    )


_Cat2600TsPortResetStats_Type.__name__ = "Integer32"
_Cat2600TsPortResetStats_Object = MibTableColumn
cat2600TsPortResetStats = _Cat2600TsPortResetStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 10),
    _Cat2600TsPortResetStats_Type()
)
cat2600TsPortResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsPortResetStats.setStatus("mandatory")
_Cat2600TsPortResetTimer_Type = TimeTicks
_Cat2600TsPortResetTimer_Object = MibTableColumn
cat2600TsPortResetTimer = _Cat2600TsPortResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 11),
    _Cat2600TsPortResetTimer_Type()
)
cat2600TsPortResetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortResetTimer.setStatus("mandatory")


class _Cat2600TsPortResetAddrs_Type(Integer32):
    """Custom type cat2600TsPortResetAddrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 3),
          ("running", 2))
    )


_Cat2600TsPortResetAddrs_Type.__name__ = "Integer32"
_Cat2600TsPortResetAddrs_Object = MibTableColumn
cat2600TsPortResetAddrs = _Cat2600TsPortResetAddrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 12),
    _Cat2600TsPortResetAddrs_Type()
)
cat2600TsPortResetAddrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsPortResetAddrs.setStatus("mandatory")
_Cat2600TsPortRcvBcasts_Type = Counter32
_Cat2600TsPortRcvBcasts_Object = MibTableColumn
cat2600TsPortRcvBcasts = _Cat2600TsPortRcvBcasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 13),
    _Cat2600TsPortRcvBcasts_Type()
)
cat2600TsPortRcvBcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortRcvBcasts.setStatus("mandatory")
_Cat2600TsPortSwitchedFrames_Type = Counter32
_Cat2600TsPortSwitchedFrames_Object = MibTableColumn
cat2600TsPortSwitchedFrames = _Cat2600TsPortSwitchedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 14),
    _Cat2600TsPortSwitchedFrames_Type()
)
cat2600TsPortSwitchedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortSwitchedFrames.setStatus("mandatory")


class _Cat2600TsPortLinkState_Type(Integer32):
    """Custom type cat2600TsPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Cat2600TsPortLinkState_Type.__name__ = "Integer32"
_Cat2600TsPortLinkState_Object = MibTableColumn
cat2600TsPortLinkState = _Cat2600TsPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 15),
    _Cat2600TsPortLinkState_Type()
)
cat2600TsPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortLinkState.setStatus("mandatory")
_Cat2600TsPortHashOverflows_Type = Counter32
_Cat2600TsPortHashOverflows_Object = MibTableColumn
cat2600TsPortHashOverflows = _Cat2600TsPortHashOverflows_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 16),
    _Cat2600TsPortHashOverflows_Type()
)
cat2600TsPortHashOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortHashOverflows.setStatus("mandatory")
_Cat2600TsPortAddrAgingTime_Type = Integer32
_Cat2600TsPortAddrAgingTime_Object = MibTableColumn
cat2600TsPortAddrAgingTime = _Cat2600TsPortAddrAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 17),
    _Cat2600TsPortAddrAgingTime_Type()
)
cat2600TsPortAddrAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsPortAddrAgingTime.setStatus("mandatory")


class _Cat2600TsPortSwitchMode_Type(Integer32):
    """Custom type cat2600TsPortSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("cutthru", 2),
          ("storeandforward", 1))
    )


_Cat2600TsPortSwitchMode_Type.__name__ = "Integer32"
_Cat2600TsPortSwitchMode_Object = MibTableColumn
cat2600TsPortSwitchMode = _Cat2600TsPortSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 18),
    _Cat2600TsPortSwitchMode_Type()
)
cat2600TsPortSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsPortSwitchMode.setStatus("mandatory")


class _Cat2600TsPortFixedCfg_Type(Integer32):
    """Custom type cat2600TsPortFixedCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto-detect", 1),
          ("fixed", 2))
    )


_Cat2600TsPortFixedCfg_Type.__name__ = "Integer32"
_Cat2600TsPortFixedCfg_Object = MibTableColumn
cat2600TsPortFixedCfg = _Cat2600TsPortFixedCfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 19),
    _Cat2600TsPortFixedCfg_Type()
)
cat2600TsPortFixedCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsPortFixedCfg.setStatus("mandatory")


class _Cat2600TsPortMode_Type(Integer32):
    """Custom type cat2600TsPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adapter", 1),
          ("port", 2))
    )


_Cat2600TsPortMode_Type.__name__ = "Integer32"
_Cat2600TsPortMode_Object = MibTableColumn
cat2600TsPortMode = _Cat2600TsPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 20),
    _Cat2600TsPortMode_Type()
)
cat2600TsPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsPortMode.setStatus("mandatory")


class _Cat2600TsPortDuplex_Type(Integer32):
    """Custom type cat2600TsPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 2),
          ("half-duplex", 1))
    )


_Cat2600TsPortDuplex_Type.__name__ = "Integer32"
_Cat2600TsPortDuplex_Object = MibTableColumn
cat2600TsPortDuplex = _Cat2600TsPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 21),
    _Cat2600TsPortDuplex_Type()
)
cat2600TsPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsPortDuplex.setStatus("mandatory")
_Cat2600TsPortCfgLoss_Type = Integer32
_Cat2600TsPortCfgLoss_Object = MibTableColumn
cat2600TsPortCfgLoss = _Cat2600TsPortCfgLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 22),
    _Cat2600TsPortCfgLoss_Type()
)
cat2600TsPortCfgLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortCfgLoss.setStatus("mandatory")


class _Cat2600TsPortCfgLossRC_Type(Integer32):
    """Custom type cat2600TsPortCfgLossRC based on Integer32"""
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
        *(("adapter-check", 5),
          ("beacon-auto-removal", 2),
          ("close-srb", 6),
          ("connection-lost", 4),
          ("fdx-protocol-failure", 7),
          ("force-remove-macaddr", 3),
          ("wire-fault", 1))
    )


_Cat2600TsPortCfgLossRC_Type.__name__ = "Integer32"
_Cat2600TsPortCfgLossRC_Object = MibTableColumn
cat2600TsPortCfgLossRC = _Cat2600TsPortCfgLossRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 23),
    _Cat2600TsPortCfgLossRC_Type()
)
cat2600TsPortCfgLossRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortCfgLossRC.setStatus("mandatory")
_Cat2600TsPortCRCCount_Type = Counter32
_Cat2600TsPortCRCCount_Object = MibTableColumn
cat2600TsPortCRCCount = _Cat2600TsPortCRCCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 24),
    _Cat2600TsPortCRCCount_Type()
)
cat2600TsPortCRCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortCRCCount.setStatus("mandatory")
_Cat2600TsPortHPChannelFrames_Type = Counter32
_Cat2600TsPortHPChannelFrames_Object = MibTableColumn
cat2600TsPortHPChannelFrames = _Cat2600TsPortHPChannelFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 25),
    _Cat2600TsPortHPChannelFrames_Type()
)
cat2600TsPortHPChannelFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortHPChannelFrames.setStatus("mandatory")
_Cat2600TsPortLPChannelFrames_Type = Counter32
_Cat2600TsPortLPChannelFrames_Object = MibTableColumn
cat2600TsPortLPChannelFrames = _Cat2600TsPortLPChannelFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 26),
    _Cat2600TsPortLPChannelFrames_Type()
)
cat2600TsPortLPChannelFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortLPChannelFrames.setStatus("mandatory")


class _Cat2600TsPortHPThreshold_Type(Integer32):
    """Custom type cat2600TsPortHPThreshold based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Cat2600TsPortHPThreshold_Type.__name__ = "Integer32"
_Cat2600TsPortHPThreshold_Object = MibTableColumn
cat2600TsPortHPThreshold = _Cat2600TsPortHPThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 27),
    _Cat2600TsPortHPThreshold_Type()
)
cat2600TsPortHPThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortHPThreshold.setStatus("mandatory")


class _Cat2600TsPortCfgRingSpeed_Type(Integer32):
    """Custom type cat2600TsPortCfgRingSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed-16megabit", 1),
          ("speed-4megabit", 2))
    )


_Cat2600TsPortCfgRingSpeed_Type.__name__ = "Integer32"
_Cat2600TsPortCfgRingSpeed_Object = MibTableColumn
cat2600TsPortCfgRingSpeed = _Cat2600TsPortCfgRingSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 28),
    _Cat2600TsPortCfgRingSpeed_Type()
)
cat2600TsPortCfgRingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsPortCfgRingSpeed.setStatus("mandatory")


class _Cat2600TsPortCfgRSA_Type(Integer32):
    """Custom type cat2600TsPortCfgRSA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("rsa", 1))
    )


_Cat2600TsPortCfgRSA_Type.__name__ = "Integer32"
_Cat2600TsPortCfgRSA_Object = MibTableColumn
cat2600TsPortCfgRSA = _Cat2600TsPortCfgRSA_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 29),
    _Cat2600TsPortCfgRSA_Type()
)
cat2600TsPortCfgRSA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsPortCfgRSA.setStatus("mandatory")
_Cat2600TsPortDomain_Type = Integer32
_Cat2600TsPortDomain_Object = MibTableColumn
cat2600TsPortDomain = _Cat2600TsPortDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 30),
    _Cat2600TsPortDomain_Type()
)
cat2600TsPortDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortDomain.setStatus("mandatory")
_Cat2600TsPortCfgLossThreshold_Type = Integer32
_Cat2600TsPortCfgLossThreshold_Object = MibTableColumn
cat2600TsPortCfgLossThreshold = _Cat2600TsPortCfgLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 31),
    _Cat2600TsPortCfgLossThreshold_Type()
)
cat2600TsPortCfgLossThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsPortCfgLossThreshold.setStatus("mandatory")
_Cat2600TsPortCfgLossSamplingPeriod_Type = Integer32
_Cat2600TsPortCfgLossSamplingPeriod_Object = MibTableColumn
cat2600TsPortCfgLossSamplingPeriod = _Cat2600TsPortCfgLossSamplingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 32),
    _Cat2600TsPortCfgLossSamplingPeriod_Type()
)
cat2600TsPortCfgLossSamplingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsPortCfgLossSamplingPeriod.setStatus("mandatory")
_Cat2600TsPortBeaconStationAddress_Type = MacAddr
_Cat2600TsPortBeaconStationAddress_Object = MibTableColumn
cat2600TsPortBeaconStationAddress = _Cat2600TsPortBeaconStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 33),
    _Cat2600TsPortBeaconStationAddress_Type()
)
cat2600TsPortBeaconStationAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cat2600TsPortBeaconStationAddress.setStatus("mandatory")
_Cat2600TsPortBeaconNAUN_Type = MacAddr
_Cat2600TsPortBeaconNAUN_Object = MibTableColumn
cat2600TsPortBeaconNAUN = _Cat2600TsPortBeaconNAUN_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 34),
    _Cat2600TsPortBeaconNAUN_Type()
)
cat2600TsPortBeaconNAUN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cat2600TsPortBeaconNAUN.setStatus("mandatory")
_Cat2600TsPortBeaconType_Type = Integer32
_Cat2600TsPortBeaconType_Object = MibTableColumn
cat2600TsPortBeaconType = _Cat2600TsPortBeaconType_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 1, 1, 35),
    _Cat2600TsPortBeaconType_Type()
)
cat2600TsPortBeaconType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cat2600TsPortBeaconType.setStatus("mandatory")
_Cat2600TsOptPortStaTable_Object = MibTable
cat2600TsOptPortStaTable = _Cat2600TsOptPortStaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cat2600TsOptPortStaTable.setStatus("mandatory")
_Cat2600TsOptPortStaEntry_Object = MibTableRow
cat2600TsOptPortStaEntry = _Cat2600TsOptPortStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 2, 1)
)
cat2600TsOptPortStaEntry.setIndexNames(
    (0, "CAT2600-MIB", "cat2600TsPortIndex"),
    (0, "CAT2600-MIB", "cat2600TsOptPortStaPos"),
)
if mibBuilder.loadTexts:
    cat2600TsOptPortStaEntry.setStatus("mandatory")


class _Cat2600TsOptPortStaPos_Type(Integer32):
    """Custom type cat2600TsOptPortStaPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cat2600TsOptPortStaPos_Type.__name__ = "Integer32"
_Cat2600TsOptPortStaPos_Object = MibTableColumn
cat2600TsOptPortStaPos = _Cat2600TsOptPortStaPos_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 2, 1, 1),
    _Cat2600TsOptPortStaPos_Type()
)
cat2600TsOptPortStaPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsOptPortStaPos.setStatus("mandatory")
_Cat2600TsOptPortStaVal_Type = OctetString
_Cat2600TsOptPortStaVal_Object = MibTableColumn
cat2600TsOptPortStaVal = _Cat2600TsOptPortStaVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 2, 1, 2),
    _Cat2600TsOptPortStaVal_Type()
)
cat2600TsOptPortStaVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsOptPortStaVal.setStatus("mandatory")
_Cat2600TsPortStnTable_Object = MibTable
cat2600TsPortStnTable = _Cat2600TsPortStnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cat2600TsPortStnTable.setStatus("mandatory")
_Cat2600TsPortStnEntry_Object = MibTableRow
cat2600TsPortStnEntry = _Cat2600TsPortStnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 3, 1)
)
cat2600TsPortStnEntry.setIndexNames(
    (0, "CAT2600-MIB", "cat2600TsPortStnPortNum"),
    (0, "CAT2600-MIB", "cat2600TsPortStnAddress"),
)
if mibBuilder.loadTexts:
    cat2600TsPortStnEntry.setStatus("mandatory")
_Cat2600TsPortStnPortNum_Type = Integer32
_Cat2600TsPortStnPortNum_Object = MibTableColumn
cat2600TsPortStnPortNum = _Cat2600TsPortStnPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 3, 1, 1),
    _Cat2600TsPortStnPortNum_Type()
)
cat2600TsPortStnPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortStnPortNum.setStatus("mandatory")
_Cat2600TsPortStnAddress_Type = MacAddr
_Cat2600TsPortStnAddress_Object = MibTableColumn
cat2600TsPortStnAddress = _Cat2600TsPortStnAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 3, 1, 2),
    _Cat2600TsPortStnAddress_Type()
)
cat2600TsPortStnAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortStnAddress.setStatus("mandatory")


class _Cat2600TsPortStnLocation_Type(Integer32):
    """Custom type cat2600TsPortStnLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_Cat2600TsPortStnLocation_Type.__name__ = "Integer32"
_Cat2600TsPortStnLocation_Object = MibTableColumn
cat2600TsPortStnLocation = _Cat2600TsPortStnLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 3, 1, 3),
    _Cat2600TsPortStnLocation_Type()
)
cat2600TsPortStnLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortStnLocation.setStatus("mandatory")
_Cat2600TsPortStnSrcFrames_Type = Counter32
_Cat2600TsPortStnSrcFrames_Object = MibTableColumn
cat2600TsPortStnSrcFrames = _Cat2600TsPortStnSrcFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 3, 1, 4),
    _Cat2600TsPortStnSrcFrames_Type()
)
cat2600TsPortStnSrcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortStnSrcFrames.setStatus("mandatory")
_Cat2600TsPortStnSrcBytes_Type = Counter32
_Cat2600TsPortStnSrcBytes_Object = MibTableColumn
cat2600TsPortStnSrcBytes = _Cat2600TsPortStnSrcBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 3, 1, 5),
    _Cat2600TsPortStnSrcBytes_Type()
)
cat2600TsPortStnSrcBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortStnSrcBytes.setStatus("mandatory")
_Cat2600TsPortStnDestnFrames_Type = Counter32
_Cat2600TsPortStnDestnFrames_Object = MibTableColumn
cat2600TsPortStnDestnFrames = _Cat2600TsPortStnDestnFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 3, 1, 6),
    _Cat2600TsPortStnDestnFrames_Type()
)
cat2600TsPortStnDestnFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortStnDestnFrames.setStatus("mandatory")
_Cat2600TsPortStnDestnBytes_Type = Counter32
_Cat2600TsPortStnDestnBytes_Object = MibTableColumn
cat2600TsPortStnDestnBytes = _Cat2600TsPortStnDestnBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 2, 3, 1, 7),
    _Cat2600TsPortStnDestnBytes_Type()
)
cat2600TsPortStnDestnBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPortStnDestnBytes.setStatus("mandatory")
_Cat2600TsDmns_ObjectIdentity = ObjectIdentity
cat2600TsDmns = _Cat2600TsDmns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3)
)
_Cat2600TsDmnTable_Object = MibTable
cat2600TsDmnTable = _Cat2600TsDmnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cat2600TsDmnTable.setStatus("mandatory")
_Cat2600TsDmnEntry_Object = MibTableRow
cat2600TsDmnEntry = _Cat2600TsDmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 1, 1)
)
cat2600TsDmnEntry.setIndexNames(
    (0, "CAT2600-MIB", "cat2600TsDmnIndex"),
)
if mibBuilder.loadTexts:
    cat2600TsDmnEntry.setStatus("mandatory")


class _Cat2600TsDmnIndex_Type(Integer32):
    """Custom type cat2600TsDmnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cat2600TsDmnIndex_Type.__name__ = "Integer32"
_Cat2600TsDmnIndex_Object = MibTableColumn
cat2600TsDmnIndex = _Cat2600TsDmnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 1, 1, 1),
    _Cat2600TsDmnIndex_Type()
)
cat2600TsDmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsDmnIndex.setStatus("mandatory")
_Cat2600TsDmnPorts_Type = OctetString
_Cat2600TsDmnPorts_Object = MibTableColumn
cat2600TsDmnPorts = _Cat2600TsDmnPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 1, 1, 2),
    _Cat2600TsDmnPorts_Type()
)
cat2600TsDmnPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsDmnPorts.setStatus("mandatory")


class _Cat2600TsDmnIpState_Type(Integer32):
    """Custom type cat2600TsDmnIpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always-bootp", 3),
          ("auto-bootp", 2),
          ("disabled", 1))
    )


_Cat2600TsDmnIpState_Type.__name__ = "Integer32"
_Cat2600TsDmnIpState_Object = MibTableColumn
cat2600TsDmnIpState = _Cat2600TsDmnIpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 1, 1, 3),
    _Cat2600TsDmnIpState_Type()
)
cat2600TsDmnIpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsDmnIpState.setStatus("mandatory")
_Cat2600TsDmnIpAddress_Type = IpAddress
_Cat2600TsDmnIpAddress_Object = MibTableColumn
cat2600TsDmnIpAddress = _Cat2600TsDmnIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 1, 1, 4),
    _Cat2600TsDmnIpAddress_Type()
)
cat2600TsDmnIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsDmnIpAddress.setStatus("mandatory")
_Cat2600TsDmnIpSubnetMask_Type = IpAddress
_Cat2600TsDmnIpSubnetMask_Object = MibTableColumn
cat2600TsDmnIpSubnetMask = _Cat2600TsDmnIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 1, 1, 5),
    _Cat2600TsDmnIpSubnetMask_Type()
)
cat2600TsDmnIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsDmnIpSubnetMask.setStatus("mandatory")
_Cat2600TsDmnIpDefaultGateway_Type = IpAddress
_Cat2600TsDmnIpDefaultGateway_Object = MibTableColumn
cat2600TsDmnIpDefaultGateway = _Cat2600TsDmnIpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 1, 1, 6),
    _Cat2600TsDmnIpDefaultGateway_Type()
)
cat2600TsDmnIpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsDmnIpDefaultGateway.setStatus("mandatory")


class _Cat2600TsDmnStp_Type(Integer32):
    """Custom type cat2600TsDmnStp based on Integer32"""
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


_Cat2600TsDmnStp_Type.__name__ = "Integer32"
_Cat2600TsDmnStp_Object = MibTableColumn
cat2600TsDmnStp = _Cat2600TsDmnStp_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 1, 1, 7),
    _Cat2600TsDmnStp_Type()
)
cat2600TsDmnStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsDmnStp.setStatus("mandatory")


class _Cat2600TsDmnName_Type(DisplayString):
    """Custom type cat2600TsDmnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_Cat2600TsDmnName_Type.__name__ = "DisplayString"
_Cat2600TsDmnName_Object = MibTableColumn
cat2600TsDmnName = _Cat2600TsDmnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 1, 1, 8),
    _Cat2600TsDmnName_Type()
)
cat2600TsDmnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsDmnName.setStatus("mandatory")


class _Cat2600TsDmnIfIndex_Type(Integer32):
    """Custom type cat2600TsDmnIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Cat2600TsDmnIfIndex_Type.__name__ = "Integer32"
_Cat2600TsDmnIfIndex_Object = MibTableColumn
cat2600TsDmnIfIndex = _Cat2600TsDmnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 1, 1, 9),
    _Cat2600TsDmnIfIndex_Type()
)
cat2600TsDmnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsDmnIfIndex.setStatus("mandatory")
_Cat2600TsDmnBaseBridgeAddr_Type = MacAddr
_Cat2600TsDmnBaseBridgeAddr_Object = MibTableColumn
cat2600TsDmnBaseBridgeAddr = _Cat2600TsDmnBaseBridgeAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 1, 1, 10),
    _Cat2600TsDmnBaseBridgeAddr_Type()
)
cat2600TsDmnBaseBridgeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsDmnBaseBridgeAddr.setStatus("mandatory")
_Cat2600TsDmnNumStations_Type = Integer32
_Cat2600TsDmnNumStations_Object = MibTableColumn
cat2600TsDmnNumStations = _Cat2600TsDmnNumStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 1, 1, 11),
    _Cat2600TsDmnNumStations_Type()
)
cat2600TsDmnNumStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsDmnNumStations.setStatus("mandatory")
_Cat2600TsDmnMostStations_Type = Integer32
_Cat2600TsDmnMostStations_Object = MibTableColumn
cat2600TsDmnMostStations = _Cat2600TsDmnMostStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 1, 1, 12),
    _Cat2600TsDmnMostStations_Type()
)
cat2600TsDmnMostStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsDmnMostStations.setStatus("mandatory")
_Cat2600TsDmnStationTable_Object = MibTable
cat2600TsDmnStationTable = _Cat2600TsDmnStationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    cat2600TsDmnStationTable.setStatus("mandatory")
_Cat2600TsDmnStationEntry_Object = MibTableRow
cat2600TsDmnStationEntry = _Cat2600TsDmnStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 5, 1)
)
cat2600TsDmnStationEntry.setIndexNames(
    (0, "CAT2600-MIB", "cat2600TsDmnIndex"),
    (0, "CAT2600-MIB", "cat2600TsDmnStationAddress"),
)
if mibBuilder.loadTexts:
    cat2600TsDmnStationEntry.setStatus("mandatory")


class _Cat2600TsDmnStationDmnIndex_Type(Integer32):
    """Custom type cat2600TsDmnStationDmnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cat2600TsDmnStationDmnIndex_Type.__name__ = "Integer32"
_Cat2600TsDmnStationDmnIndex_Object = MibTableColumn
cat2600TsDmnStationDmnIndex = _Cat2600TsDmnStationDmnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 5, 1, 1),
    _Cat2600TsDmnStationDmnIndex_Type()
)
cat2600TsDmnStationDmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsDmnStationDmnIndex.setStatus("mandatory")


class _Cat2600TsDmnStationAddress_Type(OctetString):
    """Custom type cat2600TsDmnStationAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Cat2600TsDmnStationAddress_Type.__name__ = "OctetString"
_Cat2600TsDmnStationAddress_Object = MibTableColumn
cat2600TsDmnStationAddress = _Cat2600TsDmnStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 5, 1, 2),
    _Cat2600TsDmnStationAddress_Type()
)
cat2600TsDmnStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsDmnStationAddress.setStatus("mandatory")
_Cat2600TsDmnStationPort_Type = Integer32
_Cat2600TsDmnStationPort_Object = MibTableColumn
cat2600TsDmnStationPort = _Cat2600TsDmnStationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 5, 1, 3),
    _Cat2600TsDmnStationPort_Type()
)
cat2600TsDmnStationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsDmnStationPort.setStatus("mandatory")
_Cat2600TsDmnStationTraffic_Type = OctetString
_Cat2600TsDmnStationTraffic_Object = MibTableColumn
cat2600TsDmnStationTraffic = _Cat2600TsDmnStationTraffic_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 5, 1, 4),
    _Cat2600TsDmnStationTraffic_Type()
)
cat2600TsDmnStationTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsDmnStationTraffic.setStatus("mandatory")
_Cat2600TsOptDmnStaTable_Object = MibTable
cat2600TsOptDmnStaTable = _Cat2600TsOptDmnStaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    cat2600TsOptDmnStaTable.setStatus("mandatory")
_Cat2600TsOptDmnStaEntry_Object = MibTableRow
cat2600TsOptDmnStaEntry = _Cat2600TsOptDmnStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 6, 1)
)
cat2600TsOptDmnStaEntry.setIndexNames(
    (0, "CAT2600-MIB", "cat2600TsDmnStationDmnIndex"),
    (0, "CAT2600-MIB", "cat2600TsOptDmnStaPos"),
)
if mibBuilder.loadTexts:
    cat2600TsOptDmnStaEntry.setStatus("mandatory")


class _Cat2600TsOptDmnStaPos_Type(Integer32):
    """Custom type cat2600TsOptDmnStaPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cat2600TsOptDmnStaPos_Type.__name__ = "Integer32"
_Cat2600TsOptDmnStaPos_Object = MibTableColumn
cat2600TsOptDmnStaPos = _Cat2600TsOptDmnStaPos_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 6, 1, 1),
    _Cat2600TsOptDmnStaPos_Type()
)
cat2600TsOptDmnStaPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsOptDmnStaPos.setStatus("mandatory")
_Cat2600TsOptDmnStaVal_Type = OctetString
_Cat2600TsOptDmnStaVal_Object = MibTableColumn
cat2600TsOptDmnStaVal = _Cat2600TsOptDmnStaVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 3, 6, 1, 2),
    _Cat2600TsOptDmnStaVal_Type()
)
cat2600TsOptDmnStaVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsOptDmnStaVal.setStatus("mandatory")
_Cat2600TsPipe_ObjectIdentity = ObjectIdentity
cat2600TsPipe = _Cat2600TsPipe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 4)
)
_Cat2600TsPipeTable_Object = MibTable
cat2600TsPipeTable = _Cat2600TsPipeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cat2600TsPipeTable.setStatus("mandatory")
_Cat2600TsPipeEntry_Object = MibTableRow
cat2600TsPipeEntry = _Cat2600TsPipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 4, 1, 1)
)
cat2600TsPipeEntry.setIndexNames(
    (0, "CAT2600-MIB", "cat2600TsPipeNumber"),
)
if mibBuilder.loadTexts:
    cat2600TsPipeEntry.setStatus("mandatory")


class _Cat2600TsPipeNumber_Type(Integer32):
    """Custom type cat2600TsPipeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Cat2600TsPipeNumber_Type.__name__ = "Integer32"
_Cat2600TsPipeNumber_Object = MibTableColumn
cat2600TsPipeNumber = _Cat2600TsPipeNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 4, 1, 1, 1),
    _Cat2600TsPipeNumber_Type()
)
cat2600TsPipeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsPipeNumber.setStatus("mandatory")


class _Cat2600TsPipePorts_Type(OctetString):
    """Custom type cat2600TsPipePorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cat2600TsPipePorts_Type.__name__ = "OctetString"
_Cat2600TsPipePorts_Object = MibTableColumn
cat2600TsPipePorts = _Cat2600TsPipePorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 4, 1, 1, 2),
    _Cat2600TsPipePorts_Type()
)
cat2600TsPipePorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsPipePorts.setStatus("mandatory")
_Cat2600TsFilter_ObjectIdentity = ObjectIdentity
cat2600TsFilter = _Cat2600TsFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 5)
)
_Cat2600TsFilterTable_Object = MibTable
cat2600TsFilterTable = _Cat2600TsFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cat2600TsFilterTable.setStatus("mandatory")
_Cat2600TsFilterEntry_Object = MibTableRow
cat2600TsFilterEntry = _Cat2600TsFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 5, 1, 1)
)
cat2600TsFilterEntry.setIndexNames(
    (0, "CAT2600-MIB", "cat2600TsFilterStationAddress"),
    (0, "CAT2600-MIB", "cat2600TsFilterType"),
)
if mibBuilder.loadTexts:
    cat2600TsFilterEntry.setStatus("mandatory")
_Cat2600TsFilterStationAddress_Type = MacAddr
_Cat2600TsFilterStationAddress_Object = MibTableColumn
cat2600TsFilterStationAddress = _Cat2600TsFilterStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 5, 1, 1, 1),
    _Cat2600TsFilterStationAddress_Type()
)
cat2600TsFilterStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsFilterStationAddress.setStatus("mandatory")


class _Cat2600TsFilterType_Type(Integer32):
    """Custom type cat2600TsFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination-filter", 2),
          ("source-filter", 1))
    )


_Cat2600TsFilterType_Type.__name__ = "Integer32"
_Cat2600TsFilterType_Object = MibTableColumn
cat2600TsFilterType = _Cat2600TsFilterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 5, 1, 1, 2),
    _Cat2600TsFilterType_Type()
)
cat2600TsFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsFilterType.setStatus("mandatory")


class _Cat2600TsFilterStatus_Type(Integer32):
    """Custom type cat2600TsFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_Cat2600TsFilterStatus_Type.__name__ = "Integer32"
_Cat2600TsFilterStatus_Object = MibTableColumn
cat2600TsFilterStatus = _Cat2600TsFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 5, 1, 1, 3),
    _Cat2600TsFilterStatus_Type()
)
cat2600TsFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsFilterStatus.setStatus("mandatory")
_Cat2600TsFilterPorts_Type = OctetString
_Cat2600TsFilterPorts_Object = MibTableColumn
cat2600TsFilterPorts = _Cat2600TsFilterPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 5, 1, 1, 4),
    _Cat2600TsFilterPorts_Type()
)
cat2600TsFilterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsFilterPorts.setStatus("mandatory")


class _Cat2600TsFilterMask_Type(OctetString):
    """Custom type cat2600TsFilterMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cat2600TsFilterMask_Type.__name__ = "OctetString"
_Cat2600TsFilterMask_Object = MibTableColumn
cat2600TsFilterMask = _Cat2600TsFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 5, 1, 1, 5),
    _Cat2600TsFilterMask_Type()
)
cat2600TsFilterMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsFilterMask.setStatus("mandatory")
_Cat2600TsUFC_ObjectIdentity = ObjectIdentity
cat2600TsUFC = _Cat2600TsUFC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 6)
)
_Cat2600TsUFCTable_Object = MibTable
cat2600TsUFCTable = _Cat2600TsUFCTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cat2600TsUFCTable.setStatus("mandatory")
_Cat2600TsUFCEntry_Object = MibTableRow
cat2600TsUFCEntry = _Cat2600TsUFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 6, 1, 1)
)
cat2600TsUFCEntry.setIndexNames(
    (0, "CAT2600-MIB", "cat2600TsUFCSlotNum"),
)
if mibBuilder.loadTexts:
    cat2600TsUFCEntry.setStatus("mandatory")


class _Cat2600TsUFCSlotNum_Type(Integer32):
    """Custom type cat2600TsUFCSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cat2600TsUFCSlotNum_Type.__name__ = "Integer32"
_Cat2600TsUFCSlotNum_Object = MibTableColumn
cat2600TsUFCSlotNum = _Cat2600TsUFCSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 6, 1, 1, 1),
    _Cat2600TsUFCSlotNum_Type()
)
cat2600TsUFCSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsUFCSlotNum.setStatus("mandatory")


class _Cat2600TsUFCNumPhysIfs_Type(Integer32):
    """Custom type cat2600TsUFCNumPhysIfs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cat2600TsUFCNumPhysIfs_Type.__name__ = "Integer32"
_Cat2600TsUFCNumPhysIfs_Object = MibTableColumn
cat2600TsUFCNumPhysIfs = _Cat2600TsUFCNumPhysIfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 6, 1, 1, 2),
    _Cat2600TsUFCNumPhysIfs_Type()
)
cat2600TsUFCNumPhysIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsUFCNumPhysIfs.setStatus("mandatory")


class _Cat2600TsUFCManufacturer_Type(DisplayString):
    """Custom type cat2600TsUFCManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Cat2600TsUFCManufacturer_Type.__name__ = "DisplayString"
_Cat2600TsUFCManufacturer_Object = MibTableColumn
cat2600TsUFCManufacturer = _Cat2600TsUFCManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 6, 1, 1, 3),
    _Cat2600TsUFCManufacturer_Type()
)
cat2600TsUFCManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsUFCManufacturer.setStatus("mandatory")


class _Cat2600TsUFCType_Type(OctetString):
    """Custom type cat2600TsUFCType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Cat2600TsUFCType_Type.__name__ = "OctetString"
_Cat2600TsUFCType_Object = MibTableColumn
cat2600TsUFCType = _Cat2600TsUFCType_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 6, 1, 1, 4),
    _Cat2600TsUFCType_Type()
)
cat2600TsUFCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsUFCType.setStatus("mandatory")


class _Cat2600TsUFCTypeDesc_Type(DisplayString):
    """Custom type cat2600TsUFCTypeDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Cat2600TsUFCTypeDesc_Type.__name__ = "DisplayString"
_Cat2600TsUFCTypeDesc_Object = MibTableColumn
cat2600TsUFCTypeDesc = _Cat2600TsUFCTypeDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 6, 1, 1, 5),
    _Cat2600TsUFCTypeDesc_Type()
)
cat2600TsUFCTypeDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsUFCTypeDesc.setStatus("mandatory")


class _Cat2600TsUFCHwVer_Type(DisplayString):
    """Custom type cat2600TsUFCHwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cat2600TsUFCHwVer_Type.__name__ = "DisplayString"
_Cat2600TsUFCHwVer_Object = MibTableColumn
cat2600TsUFCHwVer = _Cat2600TsUFCHwVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 6, 1, 1, 6),
    _Cat2600TsUFCHwVer_Type()
)
cat2600TsUFCHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsUFCHwVer.setStatus("mandatory")


class _Cat2600TsUFCFwVer_Type(DisplayString):
    """Custom type cat2600TsUFCFwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Cat2600TsUFCFwVer_Type.__name__ = "DisplayString"
_Cat2600TsUFCFwVer_Object = MibTableColumn
cat2600TsUFCFwVer = _Cat2600TsUFCFwVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 6, 1, 1, 7),
    _Cat2600TsUFCFwVer_Type()
)
cat2600TsUFCFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsUFCFwVer.setStatus("mandatory")


class _Cat2600TsUFCStatus_Type(Integer32):
    """Custom type cat2600TsUFCStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("other", 3),
          ("up", 1))
    )


_Cat2600TsUFCStatus_Type.__name__ = "Integer32"
_Cat2600TsUFCStatus_Object = MibTableColumn
cat2600TsUFCStatus = _Cat2600TsUFCStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 6, 1, 1, 8),
    _Cat2600TsUFCStatus_Type()
)
cat2600TsUFCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cat2600TsUFCStatus.setStatus("mandatory")


class _Cat2600TsUFCReset_Type(Integer32):
    """Custom type cat2600TsUFCReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hardReset", 2),
          ("running", 1),
          ("softReset", 3))
    )


_Cat2600TsUFCReset_Type.__name__ = "Integer32"
_Cat2600TsUFCReset_Object = MibTableColumn
cat2600TsUFCReset = _Cat2600TsUFCReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 2, 6, 1, 1, 9),
    _Cat2600TsUFCReset_Type()
)
cat2600TsUFCReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cat2600TsUFCReset.setStatus("mandatory")
_DtrMIBs_ObjectIdentity = ObjectIdentity
dtrMIBs = _DtrMIBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 3)
)
_DtrConcMIB_ObjectIdentity = ObjectIdentity
dtrConcMIB = _DtrConcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 3, 1)
)
_DtrMacMIB_ObjectIdentity = ObjectIdentity
dtrMacMIB = _DtrMacMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 111, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAT2600-MIB",
    **{"MacAddr": MacAddr,
       "cisco": cisco,
       "catProd": catProd,
       "cat2600": cat2600,
       "cat2600Ts": cat2600Ts,
       "cat2600TsObjectID": cat2600TsObjectID,
       "cat2600TsSysObjectID": cat2600TsSysObjectID,
       "cat2600TsObjects": cat2600TsObjects,
       "cat2600TsMain": cat2600TsMain,
       "cat2600TsConfig": cat2600TsConfig,
       "cat2600TsFwVer": cat2600TsFwVer,
       "cat2600TsHwVer": cat2600TsHwVer,
       "cat2600TsSerialNumber": cat2600TsSerialNumber,
       "cat2600TsInstallationDate": cat2600TsInstallationDate,
       "cat2600TsFwSize": cat2600TsFwSize,
       "cat2600TsFwCRC": cat2600TsFwCRC,
       "cat2600TsFwManufacturer": cat2600TsFwManufacturer,
       "cat2600TsIpAddr": cat2600TsIpAddr,
       "cat2600TsNetMask": cat2600TsNetMask,
       "cat2600TsDefaultGateway": cat2600TsDefaultGateway,
       "cat2600TsTrapRcvrTable": cat2600TsTrapRcvrTable,
       "cat2600TsTrapRcvrEntry": cat2600TsTrapRcvrEntry,
       "cat2600TsTrapRcvrIndex": cat2600TsTrapRcvrIndex,
       "cat2600TsTrapRcvrStatus": cat2600TsTrapRcvrStatus,
       "cat2600TsTrapRcvrIpAddress": cat2600TsTrapRcvrIpAddress,
       "cat2600TsTrapRcvrComm": cat2600TsTrapRcvrComm,
       "cat2600TsTrapRcvrDmns": cat2600TsTrapRcvrDmns,
       "cat2600TsPingInterval": cat2600TsPingInterval,
       "cat2600TsTapPort": cat2600TsTapPort,
       "cat2600TsTapMonitoredPort": cat2600TsTapMonitoredPort,
       "cat2600TsCrcThresholdHi": cat2600TsCrcThresholdHi,
       "cat2600TsCrcThresholdLow": cat2600TsCrcThresholdLow,
       "cat2600TsPortSwitchModeChangeTrapEnable": cat2600TsPortSwitchModeChangeTrapEnable,
       "cat2600TsTrendThreshold": cat2600TsTrendThreshold,
       "cat2600TsSamplingPeriod": cat2600TsSamplingPeriod,
       "cat2600TsNumberUFC": cat2600TsNumberUFC,
       "cat2600TsSys": cat2600TsSys,
       "cat2600TsNumPorts": cat2600TsNumPorts,
       "cat2600TsNumStations": cat2600TsNumStations,
       "cat2600TsMostStations": cat2600TsMostStations,
       "cat2600TsMaxStations": cat2600TsMaxStations,
       "cat2600TsReset": cat2600TsReset,
       "cat2600TsNumResets": cat2600TsNumResets,
       "cat2600TsAddrAgingTime": cat2600TsAddrAgingTime,
       "cat2600TsSysTemperature": cat2600TsSysTemperature,
       "cat2600TsInstalledMemory": cat2600TsInstalledMemory,
       "cat2600TsSysCurTime": cat2600TsSysCurTime,
       "cat2600TsPort": cat2600TsPort,
       "cat2600TsPortTable": cat2600TsPortTable,
       "cat2600TsPortEntry": cat2600TsPortEntry,
       "cat2600TsPortIndex": cat2600TsPortIndex,
       "cat2600TsPortRcvLocalFrames": cat2600TsPortRcvLocalFrames,
       "cat2600TsPortForwardedFrames": cat2600TsPortForwardedFrames,
       "cat2600TsPortMostStations": cat2600TsPortMostStations,
       "cat2600TsPortMaxStations": cat2600TsPortMaxStations,
       "cat2600TsPortSWHandledFrames": cat2600TsPortSWHandledFrames,
       "cat2600TsPortLocalStations": cat2600TsPortLocalStations,
       "cat2600TsPortRemoteStations": cat2600TsPortRemoteStations,
       "cat2600TsPortUnknownStaFrames": cat2600TsPortUnknownStaFrames,
       "cat2600TsPortResetStats": cat2600TsPortResetStats,
       "cat2600TsPortResetTimer": cat2600TsPortResetTimer,
       "cat2600TsPortResetAddrs": cat2600TsPortResetAddrs,
       "cat2600TsPortRcvBcasts": cat2600TsPortRcvBcasts,
       "cat2600TsPortSwitchedFrames": cat2600TsPortSwitchedFrames,
       "cat2600TsPortLinkState": cat2600TsPortLinkState,
       "cat2600TsPortHashOverflows": cat2600TsPortHashOverflows,
       "cat2600TsPortAddrAgingTime": cat2600TsPortAddrAgingTime,
       "cat2600TsPortSwitchMode": cat2600TsPortSwitchMode,
       "cat2600TsPortFixedCfg": cat2600TsPortFixedCfg,
       "cat2600TsPortMode": cat2600TsPortMode,
       "cat2600TsPortDuplex": cat2600TsPortDuplex,
       "cat2600TsPortCfgLoss": cat2600TsPortCfgLoss,
       "cat2600TsPortCfgLossRC": cat2600TsPortCfgLossRC,
       "cat2600TsPortCRCCount": cat2600TsPortCRCCount,
       "cat2600TsPortHPChannelFrames": cat2600TsPortHPChannelFrames,
       "cat2600TsPortLPChannelFrames": cat2600TsPortLPChannelFrames,
       "cat2600TsPortHPThreshold": cat2600TsPortHPThreshold,
       "cat2600TsPortCfgRingSpeed": cat2600TsPortCfgRingSpeed,
       "cat2600TsPortCfgRSA": cat2600TsPortCfgRSA,
       "cat2600TsPortDomain": cat2600TsPortDomain,
       "cat2600TsPortCfgLossThreshold": cat2600TsPortCfgLossThreshold,
       "cat2600TsPortCfgLossSamplingPeriod": cat2600TsPortCfgLossSamplingPeriod,
       "cat2600TsPortBeaconStationAddress": cat2600TsPortBeaconStationAddress,
       "cat2600TsPortBeaconNAUN": cat2600TsPortBeaconNAUN,
       "cat2600TsPortBeaconType": cat2600TsPortBeaconType,
       "cat2600TsOptPortStaTable": cat2600TsOptPortStaTable,
       "cat2600TsOptPortStaEntry": cat2600TsOptPortStaEntry,
       "cat2600TsOptPortStaPos": cat2600TsOptPortStaPos,
       "cat2600TsOptPortStaVal": cat2600TsOptPortStaVal,
       "cat2600TsPortStnTable": cat2600TsPortStnTable,
       "cat2600TsPortStnEntry": cat2600TsPortStnEntry,
       "cat2600TsPortStnPortNum": cat2600TsPortStnPortNum,
       "cat2600TsPortStnAddress": cat2600TsPortStnAddress,
       "cat2600TsPortStnLocation": cat2600TsPortStnLocation,
       "cat2600TsPortStnSrcFrames": cat2600TsPortStnSrcFrames,
       "cat2600TsPortStnSrcBytes": cat2600TsPortStnSrcBytes,
       "cat2600TsPortStnDestnFrames": cat2600TsPortStnDestnFrames,
       "cat2600TsPortStnDestnBytes": cat2600TsPortStnDestnBytes,
       "cat2600TsDmns": cat2600TsDmns,
       "cat2600TsDmnTable": cat2600TsDmnTable,
       "cat2600TsDmnEntry": cat2600TsDmnEntry,
       "cat2600TsDmnIndex": cat2600TsDmnIndex,
       "cat2600TsDmnPorts": cat2600TsDmnPorts,
       "cat2600TsDmnIpState": cat2600TsDmnIpState,
       "cat2600TsDmnIpAddress": cat2600TsDmnIpAddress,
       "cat2600TsDmnIpSubnetMask": cat2600TsDmnIpSubnetMask,
       "cat2600TsDmnIpDefaultGateway": cat2600TsDmnIpDefaultGateway,
       "cat2600TsDmnStp": cat2600TsDmnStp,
       "cat2600TsDmnName": cat2600TsDmnName,
       "cat2600TsDmnIfIndex": cat2600TsDmnIfIndex,
       "cat2600TsDmnBaseBridgeAddr": cat2600TsDmnBaseBridgeAddr,
       "cat2600TsDmnNumStations": cat2600TsDmnNumStations,
       "cat2600TsDmnMostStations": cat2600TsDmnMostStations,
       "cat2600TsDmnStationTable": cat2600TsDmnStationTable,
       "cat2600TsDmnStationEntry": cat2600TsDmnStationEntry,
       "cat2600TsDmnStationDmnIndex": cat2600TsDmnStationDmnIndex,
       "cat2600TsDmnStationAddress": cat2600TsDmnStationAddress,
       "cat2600TsDmnStationPort": cat2600TsDmnStationPort,
       "cat2600TsDmnStationTraffic": cat2600TsDmnStationTraffic,
       "cat2600TsOptDmnStaTable": cat2600TsOptDmnStaTable,
       "cat2600TsOptDmnStaEntry": cat2600TsOptDmnStaEntry,
       "cat2600TsOptDmnStaPos": cat2600TsOptDmnStaPos,
       "cat2600TsOptDmnStaVal": cat2600TsOptDmnStaVal,
       "cat2600TsPipe": cat2600TsPipe,
       "cat2600TsPipeTable": cat2600TsPipeTable,
       "cat2600TsPipeEntry": cat2600TsPipeEntry,
       "cat2600TsPipeNumber": cat2600TsPipeNumber,
       "cat2600TsPipePorts": cat2600TsPipePorts,
       "cat2600TsFilter": cat2600TsFilter,
       "cat2600TsFilterTable": cat2600TsFilterTable,
       "cat2600TsFilterEntry": cat2600TsFilterEntry,
       "cat2600TsFilterStationAddress": cat2600TsFilterStationAddress,
       "cat2600TsFilterType": cat2600TsFilterType,
       "cat2600TsFilterStatus": cat2600TsFilterStatus,
       "cat2600TsFilterPorts": cat2600TsFilterPorts,
       "cat2600TsFilterMask": cat2600TsFilterMask,
       "cat2600TsUFC": cat2600TsUFC,
       "cat2600TsUFCTable": cat2600TsUFCTable,
       "cat2600TsUFCEntry": cat2600TsUFCEntry,
       "cat2600TsUFCSlotNum": cat2600TsUFCSlotNum,
       "cat2600TsUFCNumPhysIfs": cat2600TsUFCNumPhysIfs,
       "cat2600TsUFCManufacturer": cat2600TsUFCManufacturer,
       "cat2600TsUFCType": cat2600TsUFCType,
       "cat2600TsUFCTypeDesc": cat2600TsUFCTypeDesc,
       "cat2600TsUFCHwVer": cat2600TsUFCHwVer,
       "cat2600TsUFCFwVer": cat2600TsUFCFwVer,
       "cat2600TsUFCStatus": cat2600TsUFCStatus,
       "cat2600TsUFCReset": cat2600TsUFCReset,
       "dtrMIBs": dtrMIBs,
       "dtrConcMIB": dtrConcMIB,
       "dtrMacMIB": dtrMacMIB}
)
