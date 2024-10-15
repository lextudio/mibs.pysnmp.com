# SNMP MIB module (CLEARTRAC7-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CLEARTRAC7-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:45 2024
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

_Lucent_ObjectIdentity = ObjectIdentity
lucent = _Lucent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727)
)
_Cleartrac7_ObjectIdentity = ObjectIdentity
cleartrac7 = _Cleartrac7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1)
)
_SysDesc_Type = DisplayString
_SysDesc_Object = MibScalar
sysDesc = _SysDesc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 1),
    _SysDesc_Type()
)
sysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDesc.setStatus("mandatory")


class _SysContact_Type(DisplayString):
    """Custom type sysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysContact_Type.__name__ = "DisplayString"
_SysContact_Object = MibScalar
sysContact = _SysContact_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 2),
    _SysContact_Type()
)
sysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysContact.setStatus("mandatory")


class _SysName_Type(DisplayString):
    """Custom type sysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysName_Type.__name__ = "DisplayString"
_SysName_Object = MibScalar
sysName = _SysName_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 3),
    _SysName_Type()
)
sysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysName.setStatus("mandatory")


class _SysLocation_Type(DisplayString):
    """Custom type sysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysLocation_Type.__name__ = "DisplayString"
_SysLocation_Object = MibScalar
sysLocation = _SysLocation_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 4),
    _SysLocation_Type()
)
sysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocation.setStatus("mandatory")
_SysDate_Type = DisplayString
_SysDate_Object = MibScalar
sysDate = _SysDate_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 5),
    _SysDate_Type()
)
sysDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDate.setStatus("mandatory")
_SysClock_Type = DisplayString
_SysClock_Object = MibScalar
sysClock = _SysClock_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 6),
    _SysClock_Type()
)
sysClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysClock.setStatus("mandatory")


class _SysDay_Type(Integer32):
    """Custom type sysDay based on Integer32"""
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
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("friday", 6),
          ("monday", 2),
          ("not-applicable", 254),
          ("not-available", 255),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_SysDay_Type.__name__ = "Integer32"
_SysDay_Object = MibScalar
sysDay = _SysDay_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 7),
    _SysDay_Type()
)
sysDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDay.setStatus("mandatory")


class _SysAcceptLoop_Type(Integer32):
    """Custom type sysAcceptLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_SysAcceptLoop_Type.__name__ = "Integer32"
_SysAcceptLoop_Object = MibScalar
sysAcceptLoop = _SysAcceptLoop_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 8),
    _SysAcceptLoop_Type()
)
sysAcceptLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAcceptLoop.setStatus("mandatory")


class _SysLinkTimeout_s_Type(Integer32):
    """Custom type sysLinkTimeout_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SysLinkTimeout_s_Type.__name__ = "Integer32"
_SysLinkTimeout_s_Object = MibScalar
sysLinkTimeout_s = _SysLinkTimeout_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 9),
    _SysLinkTimeout_s_Type()
)
sysLinkTimeout_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLinkTimeout_s.setStatus("mandatory")


class _SysTransitDelay_s_Type(Integer32):
    """Custom type sysTransitDelay_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SysTransitDelay_s_Type.__name__ = "Integer32"
_SysTransitDelay_s_Object = MibScalar
sysTransitDelay_s = _SysTransitDelay_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 10),
    _SysTransitDelay_s_Type()
)
sysTransitDelay_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTransitDelay_s.setStatus("mandatory")
_SysDefaultIpAddr_Type = IpAddress
_SysDefaultIpAddr_Object = MibScalar
sysDefaultIpAddr = _SysDefaultIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 11),
    _SysDefaultIpAddr_Type()
)
sysDefaultIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDefaultIpAddr.setStatus("mandatory")
_SysDefaultIpMask_Type = IpAddress
_SysDefaultIpMask_Object = MibScalar
sysDefaultIpMask = _SysDefaultIpMask_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 12),
    _SysDefaultIpMask_Type()
)
sysDefaultIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDefaultIpMask.setStatus("mandatory")
_SysDefaultGateway_Type = IpAddress
_SysDefaultGateway_Object = MibScalar
sysDefaultGateway = _SysDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 13),
    _SysDefaultGateway_Type()
)
sysDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDefaultGateway.setStatus("mandatory")


class _SysRackId_Type(Integer32):
    """Custom type sysRackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cs-product-only", 0),
          ("not-applicable", 254),
          ("not-available", 255),
          ("rack-1", 1),
          ("rack-2", 2),
          ("rack-3", 3),
          ("rack-4", 4))
    )


_SysRackId_Type.__name__ = "Integer32"
_SysRackId_Object = MibScalar
sysRackId = _SysRackId_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 15),
    _SysRackId_Type()
)
sysRackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRackId.setStatus("mandatory")


class _SysPsAndFansMonitoring_Type(Integer32):
    """Custom type sysPsAndFansMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("cs-product-only", 0),
          ("fans", 3),
          ("none", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("ps", 2))
    )


_SysPsAndFansMonitoring_Type.__name__ = "Integer32"
_SysPsAndFansMonitoring_Object = MibScalar
sysPsAndFansMonitoring = _SysPsAndFansMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 16),
    _SysPsAndFansMonitoring_Type()
)
sysPsAndFansMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPsAndFansMonitoring.setStatus("mandatory")
_SysSnmpTrapIpAddr1_Type = IpAddress
_SysSnmpTrapIpAddr1_Object = MibScalar
sysSnmpTrapIpAddr1 = _SysSnmpTrapIpAddr1_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 17),
    _SysSnmpTrapIpAddr1_Type()
)
sysSnmpTrapIpAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnmpTrapIpAddr1.setStatus("mandatory")
_SysSnmpTrapIpAddr2_Type = IpAddress
_SysSnmpTrapIpAddr2_Object = MibScalar
sysSnmpTrapIpAddr2 = _SysSnmpTrapIpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 18),
    _SysSnmpTrapIpAddr2_Type()
)
sysSnmpTrapIpAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnmpTrapIpAddr2.setStatus("mandatory")
_SysSnmpTrapIpAddr3_Type = IpAddress
_SysSnmpTrapIpAddr3_Object = MibScalar
sysSnmpTrapIpAddr3 = _SysSnmpTrapIpAddr3_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 19),
    _SysSnmpTrapIpAddr3_Type()
)
sysSnmpTrapIpAddr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnmpTrapIpAddr3.setStatus("mandatory")
_SysSnmpTrapIpAddr4_Type = IpAddress
_SysSnmpTrapIpAddr4_Object = MibScalar
sysSnmpTrapIpAddr4 = _SysSnmpTrapIpAddr4_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 20),
    _SysSnmpTrapIpAddr4_Type()
)
sysSnmpTrapIpAddr4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSnmpTrapIpAddr4.setStatus("mandatory")


class _SysUnitRoutingVersion_Type(Integer32):
    """Custom type sysUnitRoutingVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SysUnitRoutingVersion_Type.__name__ = "Integer32"
_SysUnitRoutingVersion_Object = MibScalar
sysUnitRoutingVersion = _SysUnitRoutingVersion_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 21),
    _SysUnitRoutingVersion_Type()
)
sysUnitRoutingVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysUnitRoutingVersion.setStatus("mandatory")


class _SysThisPosId_Type(Integer32):
    """Custom type sysThisPosId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cs-product-only", 0),
          ("not-applicable", 254),
          ("not-available", 255),
          ("pos-1", 1),
          ("pos-2", 2),
          ("pos-3", 3),
          ("pos-4", 4),
          ("pos-5", 5),
          ("pos-6", 6),
          ("pos-7", 7),
          ("pos-8", 8))
    )


_SysThisPosId_Type.__name__ = "Integer32"
_SysThisPosId_Object = MibScalar
sysThisPosId = _SysThisPosId_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 30),
    _SysThisPosId_Type()
)
sysThisPosId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysThisPosId.setStatus("mandatory")


class _SysPosNr_Type(Integer32):
    """Custom type sysPosNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SysPosNr_Type.__name__ = "Integer32"
_SysPosNr_Object = MibScalar
sysPosNr = _SysPosNr_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 31),
    _SysPosNr_Type()
)
sysPosNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPosNr.setStatus("mandatory")
_SysPosTable_Object = MibTable
sysPosTable = _SysPosTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 32)
)
if mibBuilder.loadTexts:
    sysPosTable.setStatus("mandatory")
_SysPosEntry_Object = MibTableRow
sysPosEntry = _SysPosEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 32, 1)
)
sysPosEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "sysPosRackId"),
    (0, "CLEARTRAC7-MIB", "sysPosId"),
)
if mibBuilder.loadTexts:
    sysPosEntry.setStatus("mandatory")


class _SysPosId_Type(Integer32):
    """Custom type sysPosId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cs-product-only", 0),
          ("not-applicable", 254),
          ("not-available", 255),
          ("pos-1", 1),
          ("pos-2", 2),
          ("pos-3", 3),
          ("pos-4", 4),
          ("pos-5", 5),
          ("pos-6", 6),
          ("pos-7", 7),
          ("pos-8", 8))
    )


_SysPosId_Type.__name__ = "Integer32"
_SysPosId_Object = MibTableColumn
sysPosId = _SysPosId_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 32, 1, 2),
    _SysPosId_Type()
)
sysPosId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPosId.setStatus("mandatory")
_SysPosProduct_Type = ObjectIdentifier
_SysPosProduct_Object = MibTableColumn
sysPosProduct = _SysPosProduct_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 32, 1, 3),
    _SysPosProduct_Type()
)
sysPosProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPosProduct.setStatus("mandatory")


class _SysPosRackId_Type(Integer32):
    """Custom type sysPosRackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 254),
          ("not-available", 255),
          ("rack-1", 1),
          ("rack-2", 2),
          ("rack-3", 3),
          ("rack-4", 4),
          ("single-rack", 0))
    )


_SysPosRackId_Type.__name__ = "Integer32"
_SysPosRackId_Object = MibTableColumn
sysPosRackId = _SysPosRackId_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 32, 1, 4),
    _SysPosRackId_Type()
)
sysPosRackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPosRackId.setStatus("mandatory")
_SysPosIpAddr_Type = IpAddress
_SysPosIpAddr_Object = MibTableColumn
sysPosIpAddr = _SysPosIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 32, 1, 5),
    _SysPosIpAddr_Type()
)
sysPosIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPosIpAddr.setStatus("mandatory")


class _SysRacksNr_Type(Integer32):
    """Custom type sysRacksNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SysRacksNr_Type.__name__ = "Integer32"
_SysRacksNr_Object = MibScalar
sysRacksNr = _SysRacksNr_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 33),
    _SysRacksNr_Type()
)
sysRacksNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRacksNr.setStatus("mandatory")
_SysDLCI_Type = Integer32
_SysDLCI_Object = MibScalar
sysDLCI = _SysDLCI_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 34),
    _SysDLCI_Type()
)
sysDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDLCI.setStatus("mandatory")


class _SysExtensionNumLength_Type(Integer32):
    """Custom type sysExtensionNumLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SysExtensionNumLength_Type.__name__ = "Integer32"
_SysExtensionNumLength_Object = MibScalar
sysExtensionNumLength = _SysExtensionNumLength_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 35),
    _SysExtensionNumLength_Type()
)
sysExtensionNumLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysExtensionNumLength.setStatus("mandatory")


class _SysExtendedDigitsLength_Type(Integer32):
    """Custom type sysExtendedDigitsLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_SysExtendedDigitsLength_Type.__name__ = "Integer32"
_SysExtendedDigitsLength_Object = MibScalar
sysExtendedDigitsLength = _SysExtendedDigitsLength_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 36),
    _SysExtendedDigitsLength_Type()
)
sysExtendedDigitsLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysExtendedDigitsLength.setStatus("mandatory")


class _SysDialTimer_Type(Integer32):
    """Custom type sysDialTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SysDialTimer_Type.__name__ = "Integer32"
_SysDialTimer_Object = MibScalar
sysDialTimer = _SysDialTimer_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 37),
    _SysDialTimer_Type()
)
sysDialTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDialTimer.setStatus("mandatory")


class _SysCountry_Type(Integer32):
    """Custom type sysCountry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_SysCountry_Type.__name__ = "Integer32"
_SysCountry_Object = MibScalar
sysCountry = _SysCountry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 38),
    _SysCountry_Type()
)
sysCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCountry.setStatus("mandatory")


class _SysJitterBuf_Type(Integer32):
    """Custom type sysJitterBuf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_SysJitterBuf_Type.__name__ = "Integer32"
_SysJitterBuf_Object = MibScalar
sysJitterBuf = _SysJitterBuf_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 39),
    _SysJitterBuf_Type()
)
sysJitterBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysJitterBuf.setStatus("mandatory")


class _SysRingFreq_Type(Integer32):
    """Custom type sysRingFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hz-17", 1),
          ("hz-20", 2),
          ("hz-25", 3),
          ("hz-50", 4),
          ("not-applicable", 254),
          ("not-available", 255),
          ("voice-data-only", 0))
    )


_SysRingFreq_Type.__name__ = "Integer32"
_SysRingFreq_Object = MibScalar
sysRingFreq = _SysRingFreq_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 40),
    _SysRingFreq_Type()
)
sysRingFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRingFreq.setStatus("mandatory")


class _SysRingVolt_Type(Integer32):
    """Custom type sysRingVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 254),
          ("not-available", 255),
          ("rms-Volts-60", 1),
          ("rms-Volts-80", 2),
          ("voice-data-only", 0))
    )


_SysRingVolt_Type.__name__ = "Integer32"
_SysRingVolt_Object = MibScalar
sysRingVolt = _SysRingVolt_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 41),
    _SysRingVolt_Type()
)
sysRingVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRingVolt.setStatus("mandatory")


class _SysVoiceEncoding_Type(Integer32):
    """Custom type sysVoiceEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("aCode", 1),
          ("bCode", 2),
          ("fp-product-only", 0),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_SysVoiceEncoding_Type.__name__ = "Integer32"
_SysVoiceEncoding_Object = MibScalar
sysVoiceEncoding = _SysVoiceEncoding_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 42),
    _SysVoiceEncoding_Type()
)
sysVoiceEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysVoiceEncoding.setStatus("mandatory")


class _SysVoiceClocking_Type(Integer32):
    """Custom type sysVoiceClocking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("aClock", 1),
          ("bClock", 2),
          ("fp-product-only", 0),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_SysVoiceClocking_Type.__name__ = "Integer32"
_SysVoiceClocking_Object = MibScalar
sysVoiceClocking = _SysVoiceClocking_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 43),
    _SysVoiceClocking_Type()
)
sysVoiceClocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysVoiceClocking.setStatus("mandatory")


class _SysVoiceLog_Type(Integer32):
    """Custom type sysVoiceLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_SysVoiceLog_Type.__name__ = "Integer32"
_SysVoiceLog_Object = MibScalar
sysVoiceLog = _SysVoiceLog_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 44),
    _SysVoiceLog_Type()
)
sysVoiceLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysVoiceLog.setStatus("mandatory")
_SysSpeedDialNumLength_Type = Integer32
_SysSpeedDialNumLength_Object = MibScalar
sysSpeedDialNumLength = _SysSpeedDialNumLength_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 45),
    _SysSpeedDialNumLength_Type()
)
sysSpeedDialNumLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSpeedDialNumLength.setStatus("mandatory")


class _SysAutoSaveDelay_Type(Integer32):
    """Custom type sysAutoSaveDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SysAutoSaveDelay_Type.__name__ = "Integer32"
_SysAutoSaveDelay_Object = MibScalar
sysAutoSaveDelay = _SysAutoSaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 46),
    _SysAutoSaveDelay_Type()
)
sysAutoSaveDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAutoSaveDelay.setStatus("mandatory")


class _SysPsMonitoring_Type(Integer32):
    """Custom type sysPsMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_SysPsMonitoring_Type.__name__ = "Integer32"
_SysPsMonitoring_Object = MibScalar
sysPsMonitoring = _SysPsMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 47),
    _SysPsMonitoring_Type()
)
sysPsMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPsMonitoring.setStatus("mandatory")


class _SysVoiceHighestPriority_Type(Integer32):
    """Custom type sysVoiceHighestPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_SysVoiceHighestPriority_Type.__name__ = "Integer32"
_SysVoiceHighestPriority_Object = MibScalar
sysVoiceHighestPriority = _SysVoiceHighestPriority_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 48),
    _SysVoiceHighestPriority_Type()
)
sysVoiceHighestPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysVoiceHighestPriority.setStatus("mandatory")


class _SysVoiceClass_Type(Integer32):
    """Custom type sysVoiceClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SysVoiceClass_Type.__name__ = "Integer32"
_SysVoiceClass_Object = MibScalar
sysVoiceClass = _SysVoiceClass_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 49),
    _SysVoiceClass_Type()
)
sysVoiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysVoiceClass.setStatus("mandatory")


class _SysHuntForwardingAUnit_Type(DisplayString):
    """Custom type sysHuntForwardingAUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SysHuntForwardingAUnit_Type.__name__ = "DisplayString"
_SysHuntForwardingAUnit_Object = MibScalar
sysHuntForwardingAUnit = _SysHuntForwardingAUnit_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 50),
    _SysHuntForwardingAUnit_Type()
)
sysHuntForwardingAUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysHuntForwardingAUnit.setStatus("mandatory")


class _SysHuntForwardingBUnit_Type(DisplayString):
    """Custom type sysHuntForwardingBUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SysHuntForwardingBUnit_Type.__name__ = "DisplayString"
_SysHuntForwardingBUnit_Object = MibScalar
sysHuntForwardingBUnit = _SysHuntForwardingBUnit_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 51),
    _SysHuntForwardingBUnit_Type()
)
sysHuntForwardingBUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysHuntForwardingBUnit.setStatus("mandatory")
_SysHuntForwardingADLCI_Type = Integer32
_SysHuntForwardingADLCI_Object = MibScalar
sysHuntForwardingADLCI = _SysHuntForwardingADLCI_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 52),
    _SysHuntForwardingADLCI_Type()
)
sysHuntForwardingADLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysHuntForwardingADLCI.setStatus("mandatory")
_SysHuntForwardingBDLCI_Type = Integer32
_SysHuntForwardingBDLCI_Object = MibScalar
sysHuntForwardingBDLCI = _SysHuntForwardingBDLCI_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 53),
    _SysHuntForwardingBDLCI_Type()
)
sysHuntForwardingBDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysHuntForwardingBDLCI.setStatus("mandatory")
_SysHuntForwardingASvcAddress_Type = DisplayString
_SysHuntForwardingASvcAddress_Object = MibScalar
sysHuntForwardingASvcAddress = _SysHuntForwardingASvcAddress_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 54),
    _SysHuntForwardingASvcAddress_Type()
)
sysHuntForwardingASvcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysHuntForwardingASvcAddress.setStatus("mandatory")
_SysHuntForwardingBSvcAddress_Type = DisplayString
_SysHuntForwardingBSvcAddress_Object = MibScalar
sysHuntForwardingBSvcAddress = _SysHuntForwardingBSvcAddress_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 55),
    _SysHuntForwardingBSvcAddress_Type()
)
sysHuntForwardingBSvcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysHuntForwardingBSvcAddress.setStatus("mandatory")


class _SysBackplaneRipVersion_Type(Integer32):
    """Custom type sysBackplaneRipVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("v1", 2),
          ("v2-broadcast", 3),
          ("v2-multicast", 4))
    )


_SysBackplaneRipVersion_Type.__name__ = "Integer32"
_SysBackplaneRipVersion_Object = MibScalar
sysBackplaneRipVersion = _SysBackplaneRipVersion_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 56),
    _SysBackplaneRipVersion_Type()
)
sysBackplaneRipVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBackplaneRipVersion.setStatus("mandatory")
_SysTrapRackandPos_Type = Integer32
_SysTrapRackandPos_Object = MibScalar
sysTrapRackandPos = _SysTrapRackandPos_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 1, 57),
    _SysTrapRackandPos_Type()
)
sysTrapRackandPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTrapRackandPos.setStatus("mandatory")
_Ifwan_ObjectIdentity = ObjectIdentity
ifwan = _Ifwan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2)
)
_IfwanNumber_Type = Integer32
_IfwanNumber_Object = MibScalar
ifwanNumber = _IfwanNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 1),
    _IfwanNumber_Type()
)
ifwanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifwanNumber.setStatus("mandatory")
_IfwanTable_Object = MibTable
ifwanTable = _IfwanTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ifwanTable.setStatus("mandatory")
_IfwanEntry_Object = MibTableRow
ifwanEntry = _IfwanEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1)
)
ifwanEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "ifwanIndex"),
)
if mibBuilder.loadTexts:
    ifwanEntry.setStatus("mandatory")
_IfwanIndex_Type = Integer32
_IfwanIndex_Object = MibTableColumn
ifwanIndex = _IfwanIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 1),
    _IfwanIndex_Type()
)
ifwanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifwanIndex.setStatus("mandatory")
_IfwanDesc_Type = DisplayString
_IfwanDesc_Object = MibTableColumn
ifwanDesc = _IfwanDesc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 2),
    _IfwanDesc_Type()
)
ifwanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifwanDesc.setStatus("mandatory")


class _IfwanProtocol_Type(Integer32):
    """Custom type ifwanProtocol based on Integer32"""
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
              10,
              11,
              12,
              17,
              18,
              19,
              28,
              29,
              31,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bsc", 8),
          ("console", 12),
          ("cop", 9),
          ("ddcmp", 5),
          ("fr-net", 17),
          ("fr-user", 18),
          ("g703", 28),
          ("hdlc", 4),
          ("not-applicable", 254),
          ("not-available", 255),
          ("off", 1),
          ("p-sdlc", 2),
          ("passthru", 11),
          ("ppp", 19),
          ("pvcr", 10),
          ("r-async", 7),
          ("s-sdlc", 3),
          ("sf", 31),
          ("t-async", 6),
          ("x25", 29))
    )


_IfwanProtocol_Type.__name__ = "Integer32"
_IfwanProtocol_Object = MibTableColumn
ifwanProtocol = _IfwanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 3),
    _IfwanProtocol_Type()
)
ifwanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanProtocol.setStatus("mandatory")


class _IfwanSpeed_bps_Type(Integer32):
    """Custom type ifwanSpeed_bps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(110, 2000000),
    )


_IfwanSpeed_bps_Type.__name__ = "Integer32"
_IfwanSpeed_bps_Object = MibScalar
ifwanSpeed_bps = _IfwanSpeed_bps_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 4),
    _IfwanSpeed_bps_Type()
)
ifwanSpeed_bps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSpeed_bps.setStatus("mandatory")


class _IfwanFallBackSpeed_bps_Type(Integer32):
    """Custom type ifwanFallBackSpeed_bps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_IfwanFallBackSpeed_bps_Type.__name__ = "Integer32"
_IfwanFallBackSpeed_bps_Object = MibScalar
ifwanFallBackSpeed_bps = _IfwanFallBackSpeed_bps_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 5),
    _IfwanFallBackSpeed_bps_Type()
)
ifwanFallBackSpeed_bps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanFallBackSpeed_bps.setStatus("mandatory")


class _IfwanInterface_Type(Integer32):
    """Custom type ifwanInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("autom", 16),
          ("dce-rs232", 0),
          ("dce-rs366a", 8),
          ("dce-rs449", 10),
          ("dce-rs530", 6),
          ("dce-undef", 255),
          ("dce-univ", 17),
          ("dce-v35", 2),
          ("dce-x21", 4),
          ("dsu-csu", 23),
          ("dte-aui", 12),
          ("dte-rs232", 1),
          ("dte-rs366a", 9),
          ("dte-rs449", 11),
          ("dte-rs530", 7),
          ("dte-tpe", 13),
          ("dte-undef", 254),
          ("dte-univ", 18),
          ("dte-v35", 3),
          ("dte-x21", 5),
          ("i430s", 19),
          ("i430u", 20),
          ("i431-e1", 22),
          ("i431-t1", 21),
          ("type-undef", 253))
    )


_IfwanInterface_Type.__name__ = "Integer32"
_IfwanInterface_Object = MibTableColumn
ifwanInterface = _IfwanInterface_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 6),
    _IfwanInterface_Type()
)
ifwanInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanInterface.setStatus("mandatory")


class _IfwanClocking_Type(Integer32):
    """Custom type ifwanClocking based on Integer32"""
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
              11,
              12,
              13,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("async", 5),
          ("external", 2),
          ("internal", 1),
          ("ipl", 3),
          ("iso-ext", 7),
          ("iso-int", 6),
          ("itb", 4),
          ("not-applicable", 254),
          ("not-available", 255),
          ("t1-e1-A-Rcvd", 12),
          ("t1-e1-B-Rcvd", 11),
          ("t1-e1-Local", 13))
    )


_IfwanClocking_Type.__name__ = "Integer32"
_IfwanClocking_Object = MibTableColumn
ifwanClocking = _IfwanClocking_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 7),
    _IfwanClocking_Type()
)
ifwanClocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanClocking.setStatus("mandatory")


class _IfwanCoding_Type(Integer32):
    """Custom type ifwanCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 254),
          ("not-available", 255),
          ("nrz", 1),
          ("nrz-crc0", 3),
          ("nrzi", 2),
          ("nrzi-crc0", 4))
    )


_IfwanCoding_Type.__name__ = "Integer32"
_IfwanCoding_Object = MibTableColumn
ifwanCoding = _IfwanCoding_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 8),
    _IfwanCoding_Type()
)
ifwanCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanCoding.setStatus("mandatory")


class _IfwanModem_Type(Integer32):
    """Custom type ifwanModem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dynafix", 6),
          ("dynamic", 2),
          ("dynapass", 4),
          ("not-applicable", 254),
          ("not-available", 255),
          ("statfix", 5),
          ("static", 1),
          ("statpass", 3))
    )


_IfwanModem_Type.__name__ = "Integer32"
_IfwanModem_Object = MibTableColumn
ifwanModem = _IfwanModem_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 9),
    _IfwanModem_Type()
)
ifwanModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanModem.setStatus("mandatory")


class _IfwanTxStart_Type(Integer32):
    """Custom type ifwanTxStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("byte-1024", 8),
          ("byte-144", 4),
          ("byte-16", 11),
          ("byte-192", 5),
          ("byte-2048", 9),
          ("byte-24", 12),
          ("byte-256", 6),
          ("byte-32", 13),
          ("byte-48", 2),
          ("byte-512", 7),
          ("byte-8", 10),
          ("byte-96", 3),
          ("max", 1),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanTxStart_Type.__name__ = "Integer32"
_IfwanTxStart_Object = MibTableColumn
ifwanTxStart = _IfwanTxStart_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 10),
    _IfwanTxStart_Type()
)
ifwanTxStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanTxStart.setStatus("mandatory")


class _IfwanIdle_Type(Integer32):
    """Custom type ifwanIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("flag", 3),
          ("mark", 2),
          ("markd", 4),
          ("not-applicable", 254),
          ("not-available", 255),
          ("space", 1))
    )


_IfwanIdle_Type.__name__ = "Integer32"
_IfwanIdle_Object = MibTableColumn
ifwanIdle = _IfwanIdle_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 11),
    _IfwanIdle_Type()
)
ifwanIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanIdle.setStatus("mandatory")


class _IfwanDuplex_Type(Integer32):
    """Custom type ifwanDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("half", 1),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanDuplex_Type.__name__ = "Integer32"
_IfwanDuplex_Object = MibTableColumn
ifwanDuplex = _IfwanDuplex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 12),
    _IfwanDuplex_Type()
)
ifwanDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanDuplex.setStatus("mandatory")


class _IfwanGroupPoll_Type(Integer32):
    """Custom type ifwanGroupPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfwanGroupPoll_Type.__name__ = "Integer32"
_IfwanGroupPoll_Object = MibTableColumn
ifwanGroupPoll = _IfwanGroupPoll_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 13),
    _IfwanGroupPoll_Type()
)
ifwanGroupPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanGroupPoll.setStatus("mandatory")


class _IfwanGroupAddress_Type(OctetString):
    """Custom type ifwanGroupAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IfwanGroupAddress_Type.__name__ = "OctetString"
_IfwanGroupAddress_Object = MibTableColumn
ifwanGroupAddress = _IfwanGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 14),
    _IfwanGroupAddress_Type()
)
ifwanGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanGroupAddress.setStatus("mandatory")


class _IfwanPollDelay_ms_Type(Integer32):
    """Custom type ifwanPollDelay_ms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_IfwanPollDelay_ms_Type.__name__ = "Integer32"
_IfwanPollDelay_ms_Object = MibScalar
ifwanPollDelay_ms = _IfwanPollDelay_ms_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 15),
    _IfwanPollDelay_ms_Type()
)
ifwanPollDelay_ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPollDelay_ms.setStatus("mandatory")


class _IfwanFrameDelay_Type(Integer32):
    """Custom type ifwanFrameDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("delay-0p0-ms", 1),
          ("delay-0p5-ms", 2),
          ("delay-1p0-ms", 3),
          ("delay-1p5-ms", 4),
          ("delay-2p0-ms", 5),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanFrameDelay_Type.__name__ = "Integer32"
_IfwanFrameDelay_Object = MibTableColumn
ifwanFrameDelay = _IfwanFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 16),
    _IfwanFrameDelay_Type()
)
ifwanFrameDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanFrameDelay.setStatus("mandatory")


class _IfwanFormat_Type(Integer32):
    """Custom type ifwanFormat based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("async", 14),
          ("fmt-6-bits", 12),
          ("fmt-7-even", 4),
          ("fmt-7-ignore", 7),
          ("fmt-7-mark", 6),
          ("fmt-7-none", 2),
          ("fmt-7-odd", 3),
          ("fmt-7-space", 5),
          ("fmt-8-bits", 11),
          ("fmt-8-even", 8),
          ("fmt-8-none", 1),
          ("fmt-8-odd", 9),
          ("fmt-8n-2stop", 10),
          ("not-applicable", 254),
          ("not-available", 255),
          ("sync", 13))
    )


_IfwanFormat_Type.__name__ = "Integer32"
_IfwanFormat_Object = MibTableColumn
ifwanFormat = _IfwanFormat_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 17),
    _IfwanFormat_Type()
)
ifwanFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanFormat.setStatus("mandatory")


class _IfwanSync_Type(OctetString):
    """Custom type ifwanSync based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IfwanSync_Type.__name__ = "OctetString"
_IfwanSync_Object = MibTableColumn
ifwanSync = _IfwanSync_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 18),
    _IfwanSync_Type()
)
ifwanSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSync.setStatus("mandatory")


class _IfwanDropSyncCounter_Type(Integer32):
    """Custom type ifwanDropSyncCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IfwanDropSyncCounter_Type.__name__ = "Integer32"
_IfwanDropSyncCounter_Object = MibTableColumn
ifwanDropSyncCounter = _IfwanDropSyncCounter_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 19),
    _IfwanDropSyncCounter_Type()
)
ifwanDropSyncCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanDropSyncCounter.setStatus("mandatory")


class _IfwanDropSyncCharacter_Type(OctetString):
    """Custom type ifwanDropSyncCharacter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IfwanDropSyncCharacter_Type.__name__ = "OctetString"
_IfwanDropSyncCharacter_Object = MibTableColumn
ifwanDropSyncCharacter = _IfwanDropSyncCharacter_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 20),
    _IfwanDropSyncCharacter_Type()
)
ifwanDropSyncCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanDropSyncCharacter.setStatus("mandatory")


class _IfwanMode_Type(Integer32):
    """Custom type ifwanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("answer", 3),
          ("call-backup", 4),
          ("call-bod", 5),
          ("dedicated", 2),
          ("inactive", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("wait-user", 6))
    )


_IfwanMode_Type.__name__ = "Integer32"
_IfwanMode_Object = MibTableColumn
ifwanMode = _IfwanMode_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 21),
    _IfwanMode_Type()
)
ifwanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanMode.setStatus("mandatory")


class _IfwanBodCall_s_Type(Integer32):
    """Custom type ifwanBodCall_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_IfwanBodCall_s_Type.__name__ = "Integer32"
_IfwanBodCall_s_Object = MibScalar
ifwanBodCall_s = _IfwanBodCall_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 22),
    _IfwanBodCall_s_Type()
)
ifwanBodCall_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanBodCall_s.setStatus("mandatory")


class _IfwanBodHang_s_Type(Integer32):
    """Custom type ifwanBodHang_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_IfwanBodHang_s_Type.__name__ = "Integer32"
_IfwanBodHang_s_Object = MibScalar
ifwanBodHang_s = _IfwanBodHang_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 23),
    _IfwanBodHang_s_Type()
)
ifwanBodHang_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanBodHang_s.setStatus("mandatory")


class _IfwanBodLevel_Type(Integer32):
    """Custom type ifwanBodLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 95),
    )


_IfwanBodLevel_Type.__name__ = "Integer32"
_IfwanBodLevel_Object = MibTableColumn
ifwanBodLevel = _IfwanBodLevel_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 24),
    _IfwanBodLevel_Type()
)
ifwanBodLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanBodLevel.setStatus("mandatory")


class _IfwanBackupCall_s_Type(Integer32):
    """Custom type ifwanBackupCall_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_IfwanBackupCall_s_Type.__name__ = "Integer32"
_IfwanBackupCall_s_Object = MibScalar
ifwanBackupCall_s = _IfwanBackupCall_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 25),
    _IfwanBackupCall_s_Type()
)
ifwanBackupCall_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanBackupCall_s.setStatus("mandatory")


class _IfwanBackupHang_s_Type(Integer32):
    """Custom type ifwanBackupHang_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_IfwanBackupHang_s_Type.__name__ = "Integer32"
_IfwanBackupHang_s_Object = MibScalar
ifwanBackupHang_s = _IfwanBackupHang_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 26),
    _IfwanBackupHang_s_Type()
)
ifwanBackupHang_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanBackupHang_s.setStatus("mandatory")


class _IfwanPortToBack_Type(Integer32):
    """Custom type ifwanPortToBack based on Integer32"""
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
              15,
              16,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("all", 16),
          ("any", 15),
          ("not-applicable", 254),
          ("not-available", 255),
          ("port-1", 1),
          ("port-2", 2),
          ("port-3", 3),
          ("port-4", 4),
          ("port-5", 5),
          ("port-6", 6),
          ("port-7", 7),
          ("port-8", 8))
    )


_IfwanPortToBack_Type.__name__ = "Integer32"
_IfwanPortToBack_Object = MibTableColumn
ifwanPortToBack = _IfwanPortToBack_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 27),
    _IfwanPortToBack_Type()
)
ifwanPortToBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPortToBack.setStatus("mandatory")


class _IfwanDialer_Type(Integer32):
    """Custom type ifwanDialer based on Integer32"""
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
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("aT-19200", 7),
          ("aT-9600", 6),
          ("dTR", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("v25-B", 5),
          ("v25-H", 4),
          ("x21-L1", 2),
          ("x21-L2", 3))
    )


_IfwanDialer_Type.__name__ = "Integer32"
_IfwanDialer_Object = MibTableColumn
ifwanDialer = _IfwanDialer_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 28),
    _IfwanDialer_Type()
)
ifwanDialer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanDialer.setStatus("mandatory")
_IfwanRemoteUnit_Type = DisplayString
_IfwanRemoteUnit_Object = MibTableColumn
ifwanRemoteUnit = _IfwanRemoteUnit_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 29),
    _IfwanRemoteUnit_Type()
)
ifwanRemoteUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanRemoteUnit.setStatus("mandatory")


class _IfwanClassNumber_Type(Integer32):
    """Custom type ifwanClassNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IfwanClassNumber_Type.__name__ = "Integer32"
_IfwanClassNumber_Object = MibTableColumn
ifwanClassNumber = _IfwanClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 30),
    _IfwanClassNumber_Type()
)
ifwanClassNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanClassNumber.setStatus("mandatory")


class _IfwanRingNumber_Type(OctetString):
    """Custom type ifwanRingNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IfwanRingNumber_Type.__name__ = "OctetString"
_IfwanRingNumber_Object = MibTableColumn
ifwanRingNumber = _IfwanRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 31),
    _IfwanRingNumber_Type()
)
ifwanRingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanRingNumber.setStatus("mandatory")
_IfwanIpAddress_Type = IpAddress
_IfwanIpAddress_Object = MibTableColumn
ifwanIpAddress = _IfwanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 32),
    _IfwanIpAddress_Type()
)
ifwanIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanIpAddress.setStatus("mandatory")
_IfwanSubnetMask_Type = IpAddress
_IfwanSubnetMask_Object = MibTableColumn
ifwanSubnetMask = _IfwanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 33),
    _IfwanSubnetMask_Type()
)
ifwanSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSubnetMask.setStatus("mandatory")


class _IfwanMaxFrame_Type(Integer32):
    """Custom type ifwanMaxFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 8192),
    )


_IfwanMaxFrame_Type.__name__ = "Integer32"
_IfwanMaxFrame_Object = MibTableColumn
ifwanMaxFrame = _IfwanMaxFrame_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 34),
    _IfwanMaxFrame_Type()
)
ifwanMaxFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanMaxFrame.setStatus("mandatory")


class _IfwanCompression_Type(Integer32):
    """Custom type ifwanCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfwanCompression_Type.__name__ = "Integer32"
_IfwanCompression_Object = MibTableColumn
ifwanCompression = _IfwanCompression_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 36),
    _IfwanCompression_Type()
)
ifwanCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanCompression.setStatus("mandatory")


class _IfwanPriority_Type(Integer32):
    """Custom type ifwanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IfwanPriority_Type.__name__ = "Integer32"
_IfwanPriority_Object = MibTableColumn
ifwanPriority = _IfwanPriority_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 37),
    _IfwanPriority_Type()
)
ifwanPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifwanPriority.setStatus("mandatory")


class _IfwanTimeout_Type(Integer32):
    """Custom type ifwanTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 30000),
    )


_IfwanTimeout_Type.__name__ = "Integer32"
_IfwanTimeout_Object = MibTableColumn
ifwanTimeout = _IfwanTimeout_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 39),
    _IfwanTimeout_Type()
)
ifwanTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanTimeout.setStatus("mandatory")


class _IfwanRetry_Type(Integer32):
    """Custom type ifwanRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_IfwanRetry_Type.__name__ = "Integer32"
_IfwanRetry_Object = MibTableColumn
ifwanRetry = _IfwanRetry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 40),
    _IfwanRetry_Type()
)
ifwanRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanRetry.setStatus("mandatory")


class _IfwanRemotePort_Type(Integer32):
    """Custom type ifwanRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IfwanRemotePort_Type.__name__ = "Integer32"
_IfwanRemotePort_Object = MibTableColumn
ifwanRemotePort = _IfwanRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 41),
    _IfwanRemotePort_Type()
)
ifwanRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanRemotePort.setStatus("mandatory")


class _IfwanFlowControl_Type(Integer32):
    """Custom type ifwanFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 254),
          ("not-available", 255),
          ("off", 1),
          ("on", 2))
    )


_IfwanFlowControl_Type.__name__ = "Integer32"
_IfwanFlowControl_Object = MibTableColumn
ifwanFlowControl = _IfwanFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 42),
    _IfwanFlowControl_Type()
)
ifwanFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanFlowControl.setStatus("mandatory")


class _IfwanMgmtInterface_Type(Integer32):
    """Custom type ifwanMgmtInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("annex-d", 2),
          ("lmi", 1),
          ("none", 4),
          ("not-applicable", 254),
          ("not-available", 255),
          ("q-933", 3))
    )


_IfwanMgmtInterface_Type.__name__ = "Integer32"
_IfwanMgmtInterface_Object = MibTableColumn
ifwanMgmtInterface = _IfwanMgmtInterface_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 43),
    _IfwanMgmtInterface_Type()
)
ifwanMgmtInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanMgmtInterface.setStatus("mandatory")


class _IfwanEnquiryTimer_s_Type(Integer32):
    """Custom type ifwanEnquiryTimer_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_IfwanEnquiryTimer_s_Type.__name__ = "Integer32"
_IfwanEnquiryTimer_s_Object = MibScalar
ifwanEnquiryTimer_s = _IfwanEnquiryTimer_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 44),
    _IfwanEnquiryTimer_s_Type()
)
ifwanEnquiryTimer_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanEnquiryTimer_s.setStatus("mandatory")


class _IfwanReportCycle_Type(Integer32):
    """Custom type ifwanReportCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_IfwanReportCycle_Type.__name__ = "Integer32"
_IfwanReportCycle_Object = MibTableColumn
ifwanReportCycle = _IfwanReportCycle_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 45),
    _IfwanReportCycle_Type()
)
ifwanReportCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanReportCycle.setStatus("mandatory")


class _IfwanIpRip_Type(Integer32):
    """Custom type ifwanIpRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("v1", 2),
          ("v2-broadcast", 3),
          ("v2-multicast", 4))
    )


_IfwanIpRip_Type.__name__ = "Integer32"
_IfwanIpRip_Object = MibTableColumn
ifwanIpRip = _IfwanIpRip_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 46),
    _IfwanIpRip_Type()
)
ifwanIpRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanIpRip.setStatus("mandatory")


class _IfwanCllm_Type(Integer32):
    """Custom type ifwanCllm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 254),
          ("not-available", 255),
          ("off", 1),
          ("on", 2))
    )


_IfwanCllm_Type.__name__ = "Integer32"
_IfwanCllm_Object = MibTableColumn
ifwanCllm = _IfwanCllm_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 47),
    _IfwanCllm_Type()
)
ifwanCllm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanCllm.setStatus("mandatory")


class _IfwanIpxRip_Type(Integer32):
    """Custom type ifwanIpxRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanIpxRip_Type.__name__ = "Integer32"
_IfwanIpxRip_Object = MibTableColumn
ifwanIpxRip = _IfwanIpxRip_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 48),
    _IfwanIpxRip_Type()
)
ifwanIpxRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanIpxRip.setStatus("mandatory")


class _IfwanIpxSap_Type(Integer32):
    """Custom type ifwanIpxSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanIpxSap_Type.__name__ = "Integer32"
_IfwanIpxSap_Object = MibTableColumn
ifwanIpxSap = _IfwanIpxSap_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 49),
    _IfwanIpxSap_Type()
)
ifwanIpxSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanIpxSap.setStatus("mandatory")


class _IfwanIpxNetNum_Type(OctetString):
    """Custom type ifwanIpxNetNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IfwanIpxNetNum_Type.__name__ = "OctetString"
_IfwanIpxNetNum_Object = MibTableColumn
ifwanIpxNetNum = _IfwanIpxNetNum_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 50),
    _IfwanIpxNetNum_Type()
)
ifwanIpxNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanIpxNetNum.setStatus("mandatory")


class _IfwanRxFlow_Type(Integer32):
    """Custom type ifwanRxFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("none", 5),
          ("not-applicable", 254),
          ("not-available", 255),
          ("xon-Xoff", 1))
    )


_IfwanRxFlow_Type.__name__ = "Integer32"
_IfwanRxFlow_Object = MibTableColumn
ifwanRxFlow = _IfwanRxFlow_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 52),
    _IfwanRxFlow_Type()
)
ifwanRxFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanRxFlow.setStatus("mandatory")


class _IfwanTxFlow_Type(Integer32):
    """Custom type ifwanTxFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("none", 5),
          ("not-applicable", 254),
          ("not-available", 255),
          ("xon-Xoff", 1))
    )


_IfwanTxFlow_Type.__name__ = "Integer32"
_IfwanTxFlow_Object = MibTableColumn
ifwanTxFlow = _IfwanTxFlow_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 53),
    _IfwanTxFlow_Type()
)
ifwanTxFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanTxFlow.setStatus("mandatory")


class _IfwanTxHold_s_Type(Integer32):
    """Custom type ifwanTxHold_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_IfwanTxHold_s_Type.__name__ = "Integer32"
_IfwanTxHold_s_Object = MibScalar
ifwanTxHold_s = _IfwanTxHold_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 54),
    _IfwanTxHold_s_Type()
)
ifwanTxHold_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanTxHold_s.setStatus("mandatory")


class _IfwanDsOSpeed_bps_Type(Integer32):
    """Custom type ifwanDsOSpeed_bps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bps-56000", 2),
          ("bps-64000", 1),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanDsOSpeed_bps_Type.__name__ = "Integer32"
_IfwanDsOSpeed_bps_Object = MibScalar
ifwanDsOSpeed_bps = _IfwanDsOSpeed_bps_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 55),
    _IfwanDsOSpeed_bps_Type()
)
ifwanDsOSpeed_bps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanDsOSpeed_bps.setStatus("mandatory")


class _IfwanFraming_Type(Integer32):
    """Custom type ifwanFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("d4", 3),
          ("esf", 2),
          ("not-applicable", 254),
          ("not-available", 255),
          ("other", 4))
    )


_IfwanFraming_Type.__name__ = "Integer32"
_IfwanFraming_Object = MibTableColumn
ifwanFraming = _IfwanFraming_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 58),
    _IfwanFraming_Type()
)
ifwanFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanFraming.setStatus("mandatory")


class _IfwanTerminating_Type(Integer32):
    """Custom type ifwanTerminating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("nT", 2),
          ("not-applicable", 254),
          ("not-available", 255),
          ("tE", 1))
    )


_IfwanTerminating_Type.__name__ = "Integer32"
_IfwanTerminating_Object = MibTableColumn
ifwanTerminating = _IfwanTerminating_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 59),
    _IfwanTerminating_Type()
)
ifwanTerminating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanTerminating.setStatus("mandatory")


class _IfwanCrc4_Type(Integer32):
    """Custom type ifwanCrc4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanCrc4_Type.__name__ = "Integer32"
_IfwanCrc4_Object = MibTableColumn
ifwanCrc4 = _IfwanCrc4_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 60),
    _IfwanCrc4_Type()
)
ifwanCrc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanCrc4.setStatus("mandatory")


class _IfwanLineCoding_Type(Integer32):
    """Custom type ifwanLineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              7,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ami-e1", 0),
          ("ami-t1", 5),
          ("b7sz-t1", 7),
          ("b8zs-t1", 2),
          ("hdb3-e1", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("other", 4))
    )


_IfwanLineCoding_Type.__name__ = "Integer32"
_IfwanLineCoding_Object = MibTableColumn
ifwanLineCoding = _IfwanLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 61),
    _IfwanLineCoding_Type()
)
ifwanLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanLineCoding.setStatus("mandatory")


class _IfwanBChannels_Type(Integer32):
    """Custom type ifwanBChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("b1", 2),
          ("b1-plus-b2", 4),
          ("b2", 3),
          ("disable", 1),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanBChannels_Type.__name__ = "Integer32"
_IfwanBChannels_Object = MibTableColumn
ifwanBChannels = _IfwanBChannels_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 62),
    _IfwanBChannels_Type()
)
ifwanBChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanBChannels.setStatus("mandatory")


class _IfwanMultiframing_Type(Integer32):
    """Custom type ifwanMultiframing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanMultiframing_Type.__name__ = "Integer32"
_IfwanMultiframing_Object = MibTableColumn
ifwanMultiframing = _IfwanMultiframing_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 63),
    _IfwanMultiframing_Type()
)
ifwanMultiframing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanMultiframing.setStatus("mandatory")


class _IfwanOspfEnable_Type(Integer32):
    """Custom type ifwanOspfEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanOspfEnable_Type.__name__ = "Integer32"
_IfwanOspfEnable_Object = MibTableColumn
ifwanOspfEnable = _IfwanOspfEnable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 64),
    _IfwanOspfEnable_Type()
)
ifwanOspfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanOspfEnable.setStatus("mandatory")
_IfwanOspfAreaId_Type = IpAddress
_IfwanOspfAreaId_Object = MibTableColumn
ifwanOspfAreaId = _IfwanOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 65),
    _IfwanOspfAreaId_Type()
)
ifwanOspfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanOspfAreaId.setStatus("mandatory")


class _IfwanOspfTransitDelay_Type(Integer32):
    """Custom type ifwanOspfTransitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 360),
    )


_IfwanOspfTransitDelay_Type.__name__ = "Integer32"
_IfwanOspfTransitDelay_Object = MibTableColumn
ifwanOspfTransitDelay = _IfwanOspfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 66),
    _IfwanOspfTransitDelay_Type()
)
ifwanOspfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanOspfTransitDelay.setStatus("mandatory")


class _IfwanOspfRetransmitInt_Type(Integer32):
    """Custom type ifwanOspfRetransmitInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 360),
    )


_IfwanOspfRetransmitInt_Type.__name__ = "Integer32"
_IfwanOspfRetransmitInt_Object = MibTableColumn
ifwanOspfRetransmitInt = _IfwanOspfRetransmitInt_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 67),
    _IfwanOspfRetransmitInt_Type()
)
ifwanOspfRetransmitInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanOspfRetransmitInt.setStatus("mandatory")


class _IfwanOspfHelloInt_Type(Integer32):
    """Custom type ifwanOspfHelloInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 360),
    )


_IfwanOspfHelloInt_Type.__name__ = "Integer32"
_IfwanOspfHelloInt_Object = MibTableColumn
ifwanOspfHelloInt = _IfwanOspfHelloInt_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 68),
    _IfwanOspfHelloInt_Type()
)
ifwanOspfHelloInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanOspfHelloInt.setStatus("mandatory")


class _IfwanOspfDeadInt_Type(Integer32):
    """Custom type ifwanOspfDeadInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_IfwanOspfDeadInt_Type.__name__ = "Integer32"
_IfwanOspfDeadInt_Object = MibTableColumn
ifwanOspfDeadInt = _IfwanOspfDeadInt_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 69),
    _IfwanOspfDeadInt_Type()
)
ifwanOspfDeadInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanOspfDeadInt.setStatus("mandatory")
_IfwanOspfPassword_Type = DisplayString
_IfwanOspfPassword_Object = MibTableColumn
ifwanOspfPassword = _IfwanOspfPassword_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 70),
    _IfwanOspfPassword_Type()
)
ifwanOspfPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanOspfPassword.setStatus("mandatory")


class _IfwanOspfMetricCost_Type(Integer32):
    """Custom type ifwanOspfMetricCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_IfwanOspfMetricCost_Type.__name__ = "Integer32"
_IfwanOspfMetricCost_Object = MibTableColumn
ifwanOspfMetricCost = _IfwanOspfMetricCost_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 71),
    _IfwanOspfMetricCost_Type()
)
ifwanOspfMetricCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanOspfMetricCost.setStatus("mandatory")
_IfwanChUse_Type = DisplayString
_IfwanChUse_Object = MibTableColumn
ifwanChUse = _IfwanChUse_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 72),
    _IfwanChUse_Type()
)
ifwanChUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanChUse.setStatus("mandatory")


class _IfwanGainLimit_Type(Integer32):
    """Custom type ifwanGainLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("db-30", 1),
          ("db-36", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanGainLimit_Type.__name__ = "Integer32"
_IfwanGainLimit_Object = MibTableColumn
ifwanGainLimit = _IfwanGainLimit_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 77),
    _IfwanGainLimit_Type()
)
ifwanGainLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanGainLimit.setStatus("mandatory")


class _IfwanSignaling_Type(Integer32):
    """Custom type ifwanSignaling based on Integer32"""
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
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("e1-cas", 3),
          ("e1-ccs", 4),
          ("none", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("qsig", 7),
          ("t1-rob-bit", 2),
          ("trsp-answ", 6),
          ("trsp-orig", 5))
    )


_IfwanSignaling_Type.__name__ = "Integer32"
_IfwanSignaling_Object = MibTableColumn
ifwanSignaling = _IfwanSignaling_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 78),
    _IfwanSignaling_Type()
)
ifwanSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSignaling.setStatus("mandatory")


class _IfwanIdleCode_Type(OctetString):
    """Custom type ifwanIdleCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IfwanIdleCode_Type.__name__ = "OctetString"
_IfwanIdleCode_Object = MibTableColumn
ifwanIdleCode = _IfwanIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 79),
    _IfwanIdleCode_Type()
)
ifwanIdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanIdleCode.setStatus("mandatory")


class _IfwanLineBuild_Type(Integer32):
    """Custom type ifwanLineBuild based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dbMinus15", 6),
          ("dbMinus22point5", 7),
          ("dbMinus7point5", 5),
          ("ft0-to-133", 0),
          ("ft133-to-266", 1),
          ("ft266-to-399", 2),
          ("ft399-to-533", 3),
          ("ft533-to-655", 4),
          ("not-applicable", 254),
          ("not-available", 255),
          ("ohm-120", 9),
          ("ohm-75", 8))
    )


_IfwanLineBuild_Type.__name__ = "Integer32"
_IfwanLineBuild_Object = MibTableColumn
ifwanLineBuild = _IfwanLineBuild_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 80),
    _IfwanLineBuild_Type()
)
ifwanLineBuild.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanLineBuild.setStatus("mandatory")


class _IfwanT1E1Status_Type(Integer32):
    """Custom type ifwanT1E1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanT1E1Status_Type.__name__ = "Integer32"
_IfwanT1E1Status_Object = MibTableColumn
ifwanT1E1Status = _IfwanT1E1Status_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 84),
    _IfwanT1E1Status_Type()
)
ifwanT1E1Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanT1E1Status.setStatus("mandatory")


class _IfwanT1E1LoopBack_Type(Integer32):
    """Custom type ifwanT1E1LoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("echo", 5),
          ("enable", 2),
          ("lev1-local", 3),
          ("lev2-local", 4),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanT1E1LoopBack_Type.__name__ = "Integer32"
_IfwanT1E1LoopBack_Object = MibTableColumn
ifwanT1E1LoopBack = _IfwanT1E1LoopBack_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 85),
    _IfwanT1E1LoopBack_Type()
)
ifwanT1E1LoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanT1E1LoopBack.setStatus("mandatory")
_IfwanChExp_Type = DisplayString
_IfwanChExp_Object = MibTableColumn
ifwanChExp = _IfwanChExp_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 86),
    _IfwanChExp_Type()
)
ifwanChExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanChExp.setStatus("mandatory")


class _IfwanT1E1InterBit_Type(Integer32):
    """Custom type ifwanT1E1InterBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanT1E1InterBit_Type.__name__ = "Integer32"
_IfwanT1E1InterBit_Object = MibTableColumn
ifwanT1E1InterBit = _IfwanT1E1InterBit_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 87),
    _IfwanT1E1InterBit_Type()
)
ifwanT1E1InterBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanT1E1InterBit.setStatus("mandatory")


class _IfwanEncodingLaw_Type(Integer32):
    """Custom type ifwanEncodingLaw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 0),
          ("muLaw", 1),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanEncodingLaw_Type.__name__ = "Integer32"
_IfwanEncodingLaw_Object = MibTableColumn
ifwanEncodingLaw = _IfwanEncodingLaw_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 88),
    _IfwanEncodingLaw_Type()
)
ifwanEncodingLaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanEncodingLaw.setStatus("mandatory")


class _IfwanTxStartCop_Type(Integer32):
    """Custom type ifwanTxStartCop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("byte-1024", 13),
          ("byte-144", 9),
          ("byte-16", 3),
          ("byte-192", 10),
          ("byte-2048", 14),
          ("byte-24", 4),
          ("byte-256", 11),
          ("byte-32", 5),
          ("byte-40", 6),
          ("byte-48", 7),
          ("byte-512", 12),
          ("byte-8", 2),
          ("byte-96", 8),
          ("max", 1),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanTxStartCop_Type.__name__ = "Integer32"
_IfwanTxStartCop_Object = MibTableColumn
ifwanTxStartCop = _IfwanTxStartCop_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 89),
    _IfwanTxStartCop_Type()
)
ifwanTxStartCop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanTxStartCop.setStatus("mandatory")


class _IfwanTxStartPass_Type(Integer32):
    """Custom type ifwanTxStartPass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 12),
    )


_IfwanTxStartPass_Type.__name__ = "Integer32"
_IfwanTxStartPass_Object = MibTableColumn
ifwanTxStartPass = _IfwanTxStartPass_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 90),
    _IfwanTxStartPass_Type()
)
ifwanTxStartPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanTxStartPass.setStatus("mandatory")


class _IfwanFallBackSpeedEnable_Type(Integer32):
    """Custom type ifwanFallBackSpeedEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfwanFallBackSpeedEnable_Type.__name__ = "Integer32"
_IfwanFallBackSpeedEnable_Object = MibTableColumn
ifwanFallBackSpeedEnable = _IfwanFallBackSpeedEnable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 91),
    _IfwanFallBackSpeedEnable_Type()
)
ifwanFallBackSpeedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanFallBackSpeedEnable.setStatus("mandatory")


class _IfwanDialTimeout_s_Type(Integer32):
    """Custom type ifwanDialTimeout_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1000),
    )


_IfwanDialTimeout_s_Type.__name__ = "Integer32"
_IfwanDialTimeout_s_Object = MibScalar
ifwanDialTimeout_s = _IfwanDialTimeout_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 92),
    _IfwanDialTimeout_s_Type()
)
ifwanDialTimeout_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanDialTimeout_s.setStatus("mandatory")


class _IfwanCellPacketization_Type(Integer32):
    """Custom type ifwanCellPacketization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanCellPacketization_Type.__name__ = "Integer32"
_IfwanCellPacketization_Object = MibTableColumn
ifwanCellPacketization = _IfwanCellPacketization_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 93),
    _IfwanCellPacketization_Type()
)
ifwanCellPacketization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanCellPacketization.setStatus("mandatory")


class _IfwanMaxChannels_Type(Integer32):
    """Custom type ifwanMaxChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_IfwanMaxChannels_Type.__name__ = "Integer32"
_IfwanMaxChannels_Object = MibTableColumn
ifwanMaxChannels = _IfwanMaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 94),
    _IfwanMaxChannels_Type()
)
ifwanMaxChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanMaxChannels.setStatus("mandatory")


class _IfwanCondLMIPort_Type(Integer32):
    """Custom type ifwanCondLMIPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanCondLMIPort_Type.__name__ = "Integer32"
_IfwanCondLMIPort_Object = MibTableColumn
ifwanCondLMIPort = _IfwanCondLMIPort_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 95),
    _IfwanCondLMIPort_Type()
)
ifwanCondLMIPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanCondLMIPort.setStatus("mandatory")
_IfwanExtNumber_Type = DisplayString
_IfwanExtNumber_Object = MibTableColumn
ifwanExtNumber = _IfwanExtNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 96),
    _IfwanExtNumber_Type()
)
ifwanExtNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanExtNumber.setStatus("mandatory")
_IfwanDestExtNumber_Type = DisplayString
_IfwanDestExtNumber_Object = MibTableColumn
ifwanDestExtNumber = _IfwanDestExtNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 97),
    _IfwanDestExtNumber_Type()
)
ifwanDestExtNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanDestExtNumber.setStatus("mandatory")


class _IfwanConnTimeout_s_Type(Integer32):
    """Custom type ifwanConnTimeout_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_IfwanConnTimeout_s_Type.__name__ = "Integer32"
_IfwanConnTimeout_s_Object = MibScalar
ifwanConnTimeout_s = _IfwanConnTimeout_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 98),
    _IfwanConnTimeout_s_Type()
)
ifwanConnTimeout_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanConnTimeout_s.setStatus("mandatory")


class _IfwanSvcAddressType_Type(Integer32):
    """Custom type ifwanSvcAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e-164", 2),
          ("none", 1),
          ("x-121", 3))
    )


_IfwanSvcAddressType_Type.__name__ = "Integer32"
_IfwanSvcAddressType_Object = MibTableColumn
ifwanSvcAddressType = _IfwanSvcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 99),
    _IfwanSvcAddressType_Type()
)
ifwanSvcAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSvcAddressType.setStatus("mandatory")
_IfwanSvcNetworkAddress_Type = DisplayString
_IfwanSvcNetworkAddress_Object = MibTableColumn
ifwanSvcNetworkAddress = _IfwanSvcNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 100),
    _IfwanSvcNetworkAddress_Type()
)
ifwanSvcNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSvcNetworkAddress.setStatus("mandatory")


class _IfwanSvcMaxTxTimeoutT200_Type(Integer32):
    """Custom type ifwanSvcMaxTxTimeoutT200 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IfwanSvcMaxTxTimeoutT200_Type.__name__ = "Integer32"
_IfwanSvcMaxTxTimeoutT200_Object = MibTableColumn
ifwanSvcMaxTxTimeoutT200 = _IfwanSvcMaxTxTimeoutT200_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 101),
    _IfwanSvcMaxTxTimeoutT200_Type()
)
ifwanSvcMaxTxTimeoutT200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSvcMaxTxTimeoutT200.setStatus("mandatory")


class _IfwanSvcInactiveTimeoutT203_Type(Integer32):
    """Custom type ifwanSvcInactiveTimeoutT203 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_IfwanSvcInactiveTimeoutT203_Type.__name__ = "Integer32"
_IfwanSvcInactiveTimeoutT203_Object = MibTableColumn
ifwanSvcInactiveTimeoutT203 = _IfwanSvcInactiveTimeoutT203_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 102),
    _IfwanSvcInactiveTimeoutT203_Type()
)
ifwanSvcInactiveTimeoutT203.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSvcInactiveTimeoutT203.setStatus("mandatory")


class _IfwanSvcIframeRetransmissionsN200_Type(Integer32):
    """Custom type ifwanSvcIframeRetransmissionsN200 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IfwanSvcIframeRetransmissionsN200_Type.__name__ = "Integer32"
_IfwanSvcIframeRetransmissionsN200_Object = MibTableColumn
ifwanSvcIframeRetransmissionsN200 = _IfwanSvcIframeRetransmissionsN200_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 103),
    _IfwanSvcIframeRetransmissionsN200_Type()
)
ifwanSvcIframeRetransmissionsN200.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSvcIframeRetransmissionsN200.setStatus("mandatory")


class _IfwanSvcSetupTimeoutT303_Type(Integer32):
    """Custom type ifwanSvcSetupTimeoutT303 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_IfwanSvcSetupTimeoutT303_Type.__name__ = "Integer32"
_IfwanSvcSetupTimeoutT303_Object = MibTableColumn
ifwanSvcSetupTimeoutT303 = _IfwanSvcSetupTimeoutT303_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 104),
    _IfwanSvcSetupTimeoutT303_Type()
)
ifwanSvcSetupTimeoutT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSvcSetupTimeoutT303.setStatus("mandatory")


class _IfwanSvcDisconnectTimeoutT305_Type(Integer32):
    """Custom type ifwanSvcDisconnectTimeoutT305 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_IfwanSvcDisconnectTimeoutT305_Type.__name__ = "Integer32"
_IfwanSvcDisconnectTimeoutT305_Object = MibTableColumn
ifwanSvcDisconnectTimeoutT305 = _IfwanSvcDisconnectTimeoutT305_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 105),
    _IfwanSvcDisconnectTimeoutT305_Type()
)
ifwanSvcDisconnectTimeoutT305.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSvcDisconnectTimeoutT305.setStatus("mandatory")


class _IfwanSvcReleaseTimeoutT308_Type(Integer32):
    """Custom type ifwanSvcReleaseTimeoutT308 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_IfwanSvcReleaseTimeoutT308_Type.__name__ = "Integer32"
_IfwanSvcReleaseTimeoutT308_Object = MibTableColumn
ifwanSvcReleaseTimeoutT308 = _IfwanSvcReleaseTimeoutT308_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 106),
    _IfwanSvcReleaseTimeoutT308_Type()
)
ifwanSvcReleaseTimeoutT308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSvcReleaseTimeoutT308.setStatus("mandatory")


class _IfwanSvcCallProceedingTimeoutT310_Type(Integer32):
    """Custom type ifwanSvcCallProceedingTimeoutT310 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_IfwanSvcCallProceedingTimeoutT310_Type.__name__ = "Integer32"
_IfwanSvcCallProceedingTimeoutT310_Object = MibTableColumn
ifwanSvcCallProceedingTimeoutT310 = _IfwanSvcCallProceedingTimeoutT310_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 107),
    _IfwanSvcCallProceedingTimeoutT310_Type()
)
ifwanSvcCallProceedingTimeoutT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSvcCallProceedingTimeoutT310.setStatus("mandatory")


class _IfwanSvcStatusTimeoutT322_Type(Integer32):
    """Custom type ifwanSvcStatusTimeoutT322 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_IfwanSvcStatusTimeoutT322_Type.__name__ = "Integer32"
_IfwanSvcStatusTimeoutT322_Object = MibTableColumn
ifwanSvcStatusTimeoutT322 = _IfwanSvcStatusTimeoutT322_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 108),
    _IfwanSvcStatusTimeoutT322_Type()
)
ifwanSvcStatusTimeoutT322.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSvcStatusTimeoutT322.setStatus("mandatory")


class _IfwanTeiMode_Type(Integer32):
    """Custom type ifwanTeiMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("fixed", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanTeiMode_Type.__name__ = "Integer32"
_IfwanTeiMode_Object = MibTableColumn
ifwanTeiMode = _IfwanTeiMode_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 109),
    _IfwanTeiMode_Type()
)
ifwanTeiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanTeiMode.setStatus("mandatory")


class _IfwanDigitNumber_Type(Integer32):
    """Custom type ifwanDigitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_IfwanDigitNumber_Type.__name__ = "Integer32"
_IfwanDigitNumber_Object = MibTableColumn
ifwanDigitNumber = _IfwanDigitNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 110),
    _IfwanDigitNumber_Type()
)
ifwanDigitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanDigitNumber.setStatus("mandatory")
_IfwanMsn1_Type = DisplayString
_IfwanMsn1_Object = MibTableColumn
ifwanMsn1 = _IfwanMsn1_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 111),
    _IfwanMsn1_Type()
)
ifwanMsn1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanMsn1.setStatus("mandatory")
_IfwanMsn2_Type = DisplayString
_IfwanMsn2_Object = MibTableColumn
ifwanMsn2 = _IfwanMsn2_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 112),
    _IfwanMsn2_Type()
)
ifwanMsn2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanMsn2.setStatus("mandatory")
_IfwanMsn3_Type = DisplayString
_IfwanMsn3_Object = MibTableColumn
ifwanMsn3 = _IfwanMsn3_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 113),
    _IfwanMsn3_Type()
)
ifwanMsn3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanMsn3.setStatus("mandatory")


class _IfwanX25Encapsulation_Type(Integer32):
    """Custom type ifwanX25Encapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("annex-f", 1),
          ("annex-g", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanX25Encapsulation_Type.__name__ = "Integer32"
_IfwanX25Encapsulation_Object = MibTableColumn
ifwanX25Encapsulation = _IfwanX25Encapsulation_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 114),
    _IfwanX25Encapsulation_Type()
)
ifwanX25Encapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanX25Encapsulation.setStatus("mandatory")
_IfwanPvcNumber_Type = Integer32
_IfwanPvcNumber_Object = MibTableColumn
ifwanPvcNumber = _IfwanPvcNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 115),
    _IfwanPvcNumber_Type()
)
ifwanPvcNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPvcNumber.setStatus("mandatory")


class _IfwanQsigPbxAb_Type(Integer32):
    """Custom type ifwanQsigPbxAb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanQsigPbxAb_Type.__name__ = "Integer32"
_IfwanQsigPbxAb_Object = MibTableColumn
ifwanQsigPbxAb = _IfwanQsigPbxAb_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 116),
    _IfwanQsigPbxAb_Type()
)
ifwanQsigPbxAb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanQsigPbxAb.setStatus("mandatory")


class _IfwanQsigPbxXy_Type(Integer32):
    """Custom type ifwanQsigPbxXy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 254),
          ("not-available", 255),
          ("x", 1),
          ("y", 2))
    )


_IfwanQsigPbxXy_Type.__name__ = "Integer32"
_IfwanQsigPbxXy_Object = MibTableColumn
ifwanQsigPbxXy = _IfwanQsigPbxXy_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 117),
    _IfwanQsigPbxXy_Type()
)
ifwanQsigPbxXy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanQsigPbxXy.setStatus("mandatory")


class _IfwanIpRipTxRx_Type(Integer32):
    """Custom type ifwanIpRipTxRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("duplex", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("rx-only", 3),
          ("tx-only", 2))
    )


_IfwanIpRipTxRx_Type.__name__ = "Integer32"
_IfwanIpRipTxRx_Object = MibTableColumn
ifwanIpRipTxRx = _IfwanIpRipTxRx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 118),
    _IfwanIpRipTxRx_Type()
)
ifwanIpRipTxRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanIpRipTxRx.setStatus("mandatory")


class _IfwanIpRipAuthType_Type(Integer32):
    """Custom type ifwanIpRipAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("simple", 2))
    )


_IfwanIpRipAuthType_Type.__name__ = "Integer32"
_IfwanIpRipAuthType_Object = MibTableColumn
ifwanIpRipAuthType = _IfwanIpRipAuthType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 119),
    _IfwanIpRipAuthType_Type()
)
ifwanIpRipAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanIpRipAuthType.setStatus("mandatory")
_IfwanIpRipPassword_Type = DisplayString
_IfwanIpRipPassword_Object = MibTableColumn
ifwanIpRipPassword = _IfwanIpRipPassword_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 120),
    _IfwanIpRipPassword_Type()
)
ifwanIpRipPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanIpRipPassword.setStatus("mandatory")


class _IfwanPppSilent_Type(Integer32):
    """Custom type ifwanPppSilent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 254),
          ("not-available", 255),
          ("send-request", 1),
          ("wait-for-request", 2))
    )


_IfwanPppSilent_Type.__name__ = "Integer32"
_IfwanPppSilent_Object = MibTableColumn
ifwanPppSilent = _IfwanPppSilent_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 121),
    _IfwanPppSilent_Type()
)
ifwanPppSilent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppSilent.setStatus("mandatory")


class _IfwanPppConfigRestartTimer_Type(Integer32):
    """Custom type ifwanPppConfigRestartTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IfwanPppConfigRestartTimer_Type.__name__ = "Integer32"
_IfwanPppConfigRestartTimer_Object = MibTableColumn
ifwanPppConfigRestartTimer = _IfwanPppConfigRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 122),
    _IfwanPppConfigRestartTimer_Type()
)
ifwanPppConfigRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppConfigRestartTimer.setStatus("mandatory")


class _IfwanPppConfigRetries_Type(Integer32):
    """Custom type ifwanPppConfigRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IfwanPppConfigRetries_Type.__name__ = "Integer32"
_IfwanPppConfigRetries_Object = MibTableColumn
ifwanPppConfigRetries = _IfwanPppConfigRetries_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 123),
    _IfwanPppConfigRetries_Type()
)
ifwanPppConfigRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppConfigRetries.setStatus("mandatory")


class _IfwanPppNegociateLocalMru_Type(Integer32):
    """Custom type ifwanPppNegociateLocalMru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfwanPppNegociateLocalMru_Type.__name__ = "Integer32"
_IfwanPppNegociateLocalMru_Object = MibTableColumn
ifwanPppNegociateLocalMru = _IfwanPppNegociateLocalMru_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 124),
    _IfwanPppNegociateLocalMru_Type()
)
ifwanPppNegociateLocalMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppNegociateLocalMru.setStatus("mandatory")


class _IfwanPppLocalMru_Type(Integer32):
    """Custom type ifwanPppLocalMru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_IfwanPppLocalMru_Type.__name__ = "Integer32"
_IfwanPppLocalMru_Object = MibTableColumn
ifwanPppLocalMru = _IfwanPppLocalMru_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 125),
    _IfwanPppLocalMru_Type()
)
ifwanPppLocalMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppLocalMru.setStatus("mandatory")


class _IfwanPppNegociatePeerMru_Type(Integer32):
    """Custom type ifwanPppNegociatePeerMru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfwanPppNegociatePeerMru_Type.__name__ = "Integer32"
_IfwanPppNegociatePeerMru_Object = MibTableColumn
ifwanPppNegociatePeerMru = _IfwanPppNegociatePeerMru_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 126),
    _IfwanPppNegociatePeerMru_Type()
)
ifwanPppNegociatePeerMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppNegociatePeerMru.setStatus("mandatory")


class _IfwanPppPeerMruUpTo_Type(Integer32):
    """Custom type ifwanPppPeerMruUpTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_IfwanPppPeerMruUpTo_Type.__name__ = "Integer32"
_IfwanPppPeerMruUpTo_Object = MibTableColumn
ifwanPppPeerMruUpTo = _IfwanPppPeerMruUpTo_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 127),
    _IfwanPppPeerMruUpTo_Type()
)
ifwanPppPeerMruUpTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppPeerMruUpTo.setStatus("mandatory")


class _IfwanPppNegociateAccm_Type(Integer32):
    """Custom type ifwanPppNegociateAccm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfwanPppNegociateAccm_Type.__name__ = "Integer32"
_IfwanPppNegociateAccm_Object = MibTableColumn
ifwanPppNegociateAccm = _IfwanPppNegociateAccm_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 128),
    _IfwanPppNegociateAccm_Type()
)
ifwanPppNegociateAccm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppNegociateAccm.setStatus("mandatory")


class _IfwanPppRequestedAccmChar_Type(OctetString):
    """Custom type ifwanPppRequestedAccmChar based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IfwanPppRequestedAccmChar_Type.__name__ = "OctetString"
_IfwanPppRequestedAccmChar_Object = MibTableColumn
ifwanPppRequestedAccmChar = _IfwanPppRequestedAccmChar_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 129),
    _IfwanPppRequestedAccmChar_Type()
)
ifwanPppRequestedAccmChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppRequestedAccmChar.setStatus("mandatory")


class _IfwanPppAcceptAccmPeer_Type(Integer32):
    """Custom type ifwanPppAcceptAccmPeer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfwanPppAcceptAccmPeer_Type.__name__ = "Integer32"
_IfwanPppAcceptAccmPeer_Object = MibTableColumn
ifwanPppAcceptAccmPeer = _IfwanPppAcceptAccmPeer_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 130),
    _IfwanPppAcceptAccmPeer_Type()
)
ifwanPppAcceptAccmPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppAcceptAccmPeer.setStatus("mandatory")


class _IfwanPppAcceptableAccmChar_Type(OctetString):
    """Custom type ifwanPppAcceptableAccmChar based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IfwanPppAcceptableAccmChar_Type.__name__ = "OctetString"
_IfwanPppAcceptableAccmChar_Object = MibTableColumn
ifwanPppAcceptableAccmChar = _IfwanPppAcceptableAccmChar_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 131),
    _IfwanPppAcceptableAccmChar_Type()
)
ifwanPppAcceptableAccmChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppAcceptableAccmChar.setStatus("mandatory")


class _IfwanPppRequestMagicNum_Type(Integer32):
    """Custom type ifwanPppRequestMagicNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfwanPppRequestMagicNum_Type.__name__ = "Integer32"
_IfwanPppRequestMagicNum_Object = MibTableColumn
ifwanPppRequestMagicNum = _IfwanPppRequestMagicNum_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 132),
    _IfwanPppRequestMagicNum_Type()
)
ifwanPppRequestMagicNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppRequestMagicNum.setStatus("mandatory")


class _IfwanPppAcceptMagicNum_Type(Integer32):
    """Custom type ifwanPppAcceptMagicNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfwanPppAcceptMagicNum_Type.__name__ = "Integer32"
_IfwanPppAcceptMagicNum_Object = MibTableColumn
ifwanPppAcceptMagicNum = _IfwanPppAcceptMagicNum_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 133),
    _IfwanPppAcceptMagicNum_Type()
)
ifwanPppAcceptMagicNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppAcceptMagicNum.setStatus("mandatory")


class _IfwanPppAcceptOldIpAddNeg_Type(Integer32):
    """Custom type ifwanPppAcceptOldIpAddNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfwanPppAcceptOldIpAddNeg_Type.__name__ = "Integer32"
_IfwanPppAcceptOldIpAddNeg_Object = MibTableColumn
ifwanPppAcceptOldIpAddNeg = _IfwanPppAcceptOldIpAddNeg_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 134),
    _IfwanPppAcceptOldIpAddNeg_Type()
)
ifwanPppAcceptOldIpAddNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppAcceptOldIpAddNeg.setStatus("mandatory")


class _IfwanPppNegociateIpAddress_Type(Integer32):
    """Custom type ifwanPppNegociateIpAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfwanPppNegociateIpAddress_Type.__name__ = "Integer32"
_IfwanPppNegociateIpAddress_Object = MibTableColumn
ifwanPppNegociateIpAddress = _IfwanPppNegociateIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 135),
    _IfwanPppNegociateIpAddress_Type()
)
ifwanPppNegociateIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppNegociateIpAddress.setStatus("mandatory")


class _IfwanPppAcceptIpAddress_Type(Integer32):
    """Custom type ifwanPppAcceptIpAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfwanPppAcceptIpAddress_Type.__name__ = "Integer32"
_IfwanPppAcceptIpAddress_Object = MibTableColumn
ifwanPppAcceptIpAddress = _IfwanPppAcceptIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 136),
    _IfwanPppAcceptIpAddress_Type()
)
ifwanPppAcceptIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppAcceptIpAddress.setStatus("mandatory")
_IfwanPppRemoteIpAddress_Type = IpAddress
_IfwanPppRemoteIpAddress_Object = MibTableColumn
ifwanPppRemoteIpAddress = _IfwanPppRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 137),
    _IfwanPppRemoteIpAddress_Type()
)
ifwanPppRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppRemoteIpAddress.setStatus("mandatory")
_IfwanPppRemoteSubnetMask_Type = IpAddress
_IfwanPppRemoteSubnetMask_Object = MibTableColumn
ifwanPppRemoteSubnetMask = _IfwanPppRemoteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 138),
    _IfwanPppRemoteSubnetMask_Type()
)
ifwanPppRemoteSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanPppRemoteSubnetMask.setStatus("mandatory")


class _IfwanHighPriorityTransparentClass_Type(Integer32):
    """Custom type ifwanHighPriorityTransparentClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfwanHighPriorityTransparentClass_Type.__name__ = "Integer32"
_IfwanHighPriorityTransparentClass_Object = MibTableColumn
ifwanHighPriorityTransparentClass = _IfwanHighPriorityTransparentClass_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 139),
    _IfwanHighPriorityTransparentClass_Type()
)
ifwanHighPriorityTransparentClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanHighPriorityTransparentClass.setStatus("mandatory")


class _IfwanTransparentClassNumber_Type(Integer32):
    """Custom type ifwanTransparentClassNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IfwanTransparentClassNumber_Type.__name__ = "Integer32"
_IfwanTransparentClassNumber_Object = MibTableColumn
ifwanTransparentClassNumber = _IfwanTransparentClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 140),
    _IfwanTransparentClassNumber_Type()
)
ifwanTransparentClassNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanTransparentClassNumber.setStatus("mandatory")


class _IfwanChannelCompressed_Type(Integer32):
    """Custom type ifwanChannelCompressed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfwanChannelCompressed_Type.__name__ = "Integer32"
_IfwanChannelCompressed_Object = MibTableColumn
ifwanChannelCompressed = _IfwanChannelCompressed_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 141),
    _IfwanChannelCompressed_Type()
)
ifwanChannelCompressed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanChannelCompressed.setStatus("mandatory")


class _IfwanSfType_Type(Integer32):
    """Custom type ifwanSfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("agregate", 4),
          ("demodulator", 1),
          ("expansion", 3),
          ("modulator", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanSfType_Type.__name__ = "Integer32"
_IfwanSfType_Object = MibTableColumn
ifwanSfType = _IfwanSfType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 142),
    _IfwanSfType_Type()
)
ifwanSfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSfType.setStatus("mandatory")


class _IfwanSfMode_Type(Integer32):
    """Custom type ifwanSfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfwanSfMode_Type.__name__ = "Integer32"
_IfwanSfMode_Object = MibTableColumn
ifwanSfMode = _IfwanSfMode_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 143),
    _IfwanSfMode_Type()
)
ifwanSfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSfMode.setStatus("mandatory")
_IfwanSfCarrierId_Type = Integer32
_IfwanSfCarrierId_Object = MibTableColumn
ifwanSfCarrierId = _IfwanSfCarrierId_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 2, 2, 1, 144),
    _IfwanSfCarrierId_Type()
)
ifwanSfCarrierId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifwanSfCarrierId.setStatus("mandatory")
_Iflan_ObjectIdentity = ObjectIdentity
iflan = _Iflan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3)
)
_IflanNumber_Type = Integer32
_IflanNumber_Object = MibScalar
iflanNumber = _IflanNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 1),
    _IflanNumber_Type()
)
iflanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iflanNumber.setStatus("mandatory")
_IflanTable_Object = MibTable
iflanTable = _IflanTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2)
)
if mibBuilder.loadTexts:
    iflanTable.setStatus("mandatory")
_IflanEntry_Object = MibTableRow
iflanEntry = _IflanEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1)
)
iflanEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "iflanIndex"),
)
if mibBuilder.loadTexts:
    iflanEntry.setStatus("mandatory")
_IflanIndex_Type = Integer32
_IflanIndex_Object = MibTableColumn
iflanIndex = _IflanIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 1),
    _IflanIndex_Type()
)
iflanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iflanIndex.setStatus("mandatory")
_IflanDesc_Type = DisplayString
_IflanDesc_Object = MibTableColumn
iflanDesc = _IflanDesc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 2),
    _IflanDesc_Type()
)
iflanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iflanDesc.setStatus("mandatory")


class _IflanProtocol_Type(Integer32):
    """Custom type iflanProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              13,
              14,
              15,
              16,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-802p3", 15),
          ("ethernet-auto", 14),
          ("ethernet-v2", 16),
          ("not-applicable", 254),
          ("not-available", 255),
          ("off", 1),
          ("token-ring", 13))
    )


_IflanProtocol_Type.__name__ = "Integer32"
_IflanProtocol_Object = MibTableColumn
iflanProtocol = _IflanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 3),
    _IflanProtocol_Type()
)
iflanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanProtocol.setStatus("mandatory")


class _IflanSpeed_Type(Integer32):
    """Custom type iflanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("eth-10-Mbps", 3),
          ("not-applicable", 254),
          ("not-available", 255),
          ("tr-16-Mbps", 2),
          ("tr-4-Mbps", 1))
    )


_IflanSpeed_Type.__name__ = "Integer32"
_IflanSpeed_Object = MibTableColumn
iflanSpeed = _IflanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 4),
    _IflanSpeed_Type()
)
iflanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanSpeed.setStatus("mandatory")


class _IflanPriority_Type(Integer32):
    """Custom type iflanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IflanPriority_Type.__name__ = "Integer32"
_IflanPriority_Object = MibTableColumn
iflanPriority = _IflanPriority_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 5),
    _IflanPriority_Type()
)
iflanPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iflanPriority.setStatus("mandatory")


class _IflanCost_Type(Integer32):
    """Custom type iflanCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IflanCost_Type.__name__ = "Integer32"
_IflanCost_Object = MibTableColumn
iflanCost = _IflanCost_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 6),
    _IflanCost_Type()
)
iflanCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iflanCost.setStatus("mandatory")


class _IflanPhysAddr_Type(OctetString):
    """Custom type iflanPhysAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IflanPhysAddr_Type.__name__ = "OctetString"
_IflanPhysAddr_Object = MibTableColumn
iflanPhysAddr = _IflanPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 7),
    _IflanPhysAddr_Type()
)
iflanPhysAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanPhysAddr.setStatus("mandatory")
_IflanIpAddress_Type = IpAddress
_IflanIpAddress_Object = MibTableColumn
iflanIpAddress = _IflanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 8),
    _IflanIpAddress_Type()
)
iflanIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanIpAddress.setStatus("mandatory")
_IflanSubnetMask_Type = IpAddress
_IflanSubnetMask_Object = MibTableColumn
iflanSubnetMask = _IflanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 9),
    _IflanSubnetMask_Type()
)
iflanSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanSubnetMask.setStatus("mandatory")


class _IflanMaxFrame_Type(Integer32):
    """Custom type iflanMaxFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 8192),
    )


_IflanMaxFrame_Type.__name__ = "Integer32"
_IflanMaxFrame_Object = MibTableColumn
iflanMaxFrame = _IflanMaxFrame_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 10),
    _IflanMaxFrame_Type()
)
iflanMaxFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanMaxFrame.setStatus("mandatory")


class _IflanEth_LinkIntegrity_Type(Integer32):
    """Custom type iflanEth_LinkIntegrity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IflanEth_LinkIntegrity_Type.__name__ = "Integer32"
_IflanEth_LinkIntegrity_Object = MibScalar
iflanEth_LinkIntegrity = _IflanEth_LinkIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 12),
    _IflanEth_LinkIntegrity_Type()
)
iflanEth_LinkIntegrity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanEth_LinkIntegrity.setStatus("mandatory")


class _IflanTr_Monitor_Type(Integer32):
    """Custom type iflanTr_Monitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IflanTr_Monitor_Type.__name__ = "Integer32"
_IflanTr_Monitor_Object = MibScalar
iflanTr_Monitor = _IflanTr_Monitor_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 13),
    _IflanTr_Monitor_Type()
)
iflanTr_Monitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanTr_Monitor.setStatus("mandatory")


class _IflanTr_Etr_Type(Integer32):
    """Custom type iflanTr_Etr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IflanTr_Etr_Type.__name__ = "Integer32"
_IflanTr_Etr_Object = MibScalar
iflanTr_Etr = _IflanTr_Etr_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 14),
    _IflanTr_Etr_Type()
)
iflanTr_Etr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanTr_Etr.setStatus("mandatory")


class _IflanTr_RingNumber_Type(OctetString):
    """Custom type iflanTr_RingNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IflanTr_RingNumber_Type.__name__ = "OctetString"
_IflanTr_RingNumber_Object = MibScalar
iflanTr_RingNumber = _IflanTr_RingNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 15),
    _IflanTr_RingNumber_Type()
)
iflanTr_RingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanTr_RingNumber.setStatus("mandatory")


class _IflanIpRip_Type(Integer32):
    """Custom type iflanIpRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("v1", 2),
          ("v2-broadcast", 3),
          ("v2-multicast", 4))
    )


_IflanIpRip_Type.__name__ = "Integer32"
_IflanIpRip_Object = MibTableColumn
iflanIpRip = _IflanIpRip_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 16),
    _IflanIpRip_Type()
)
iflanIpRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanIpRip.setStatus("mandatory")


class _IflanIpxRip_Type(Integer32):
    """Custom type iflanIpxRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IflanIpxRip_Type.__name__ = "Integer32"
_IflanIpxRip_Object = MibTableColumn
iflanIpxRip = _IflanIpxRip_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 17),
    _IflanIpxRip_Type()
)
iflanIpxRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanIpxRip.setStatus("mandatory")


class _IflanIpxSap_Type(Integer32):
    """Custom type iflanIpxSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IflanIpxSap_Type.__name__ = "Integer32"
_IflanIpxSap_Object = MibTableColumn
iflanIpxSap = _IflanIpxSap_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 18),
    _IflanIpxSap_Type()
)
iflanIpxSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanIpxSap.setStatus("mandatory")


class _IflanIpxNetNum_Type(OctetString):
    """Custom type iflanIpxNetNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IflanIpxNetNum_Type.__name__ = "OctetString"
_IflanIpxNetNum_Object = MibTableColumn
iflanIpxNetNum = _IflanIpxNetNum_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 19),
    _IflanIpxNetNum_Type()
)
iflanIpxNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanIpxNetNum.setStatus("mandatory")


class _IflanIpxLanType_Type(Integer32):
    """Custom type iflanIpxLanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-802p2", 1),
          ("ethernet-802p3", 3),
          ("ethernet-ii", 4),
          ("ethernet-snap", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IflanIpxLanType_Type.__name__ = "Integer32"
_IflanIpxLanType_Object = MibTableColumn
iflanIpxLanType = _IflanIpxLanType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 20),
    _IflanIpxLanType_Type()
)
iflanIpxLanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanIpxLanType.setStatus("mandatory")


class _IflanOspfEnable_Type(Integer32):
    """Custom type iflanOspfEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IflanOspfEnable_Type.__name__ = "Integer32"
_IflanOspfEnable_Object = MibTableColumn
iflanOspfEnable = _IflanOspfEnable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 21),
    _IflanOspfEnable_Type()
)
iflanOspfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanOspfEnable.setStatus("mandatory")
_IflanOspfAreaId_Type = IpAddress
_IflanOspfAreaId_Object = MibTableColumn
iflanOspfAreaId = _IflanOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 22),
    _IflanOspfAreaId_Type()
)
iflanOspfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanOspfAreaId.setStatus("mandatory")


class _IflanOspfPriority_Type(Integer32):
    """Custom type iflanOspfPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IflanOspfPriority_Type.__name__ = "Integer32"
_IflanOspfPriority_Object = MibTableColumn
iflanOspfPriority = _IflanOspfPriority_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 23),
    _IflanOspfPriority_Type()
)
iflanOspfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanOspfPriority.setStatus("mandatory")


class _IflanOspfTransitDelay_Type(Integer32):
    """Custom type iflanOspfTransitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 360),
    )


_IflanOspfTransitDelay_Type.__name__ = "Integer32"
_IflanOspfTransitDelay_Object = MibTableColumn
iflanOspfTransitDelay = _IflanOspfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 24),
    _IflanOspfTransitDelay_Type()
)
iflanOspfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanOspfTransitDelay.setStatus("mandatory")


class _IflanOspfRetransmitInt_Type(Integer32):
    """Custom type iflanOspfRetransmitInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 360),
    )


_IflanOspfRetransmitInt_Type.__name__ = "Integer32"
_IflanOspfRetransmitInt_Object = MibTableColumn
iflanOspfRetransmitInt = _IflanOspfRetransmitInt_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 25),
    _IflanOspfRetransmitInt_Type()
)
iflanOspfRetransmitInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanOspfRetransmitInt.setStatus("mandatory")


class _IflanOspfHelloInt_Type(Integer32):
    """Custom type iflanOspfHelloInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 360),
    )


_IflanOspfHelloInt_Type.__name__ = "Integer32"
_IflanOspfHelloInt_Object = MibTableColumn
iflanOspfHelloInt = _IflanOspfHelloInt_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 26),
    _IflanOspfHelloInt_Type()
)
iflanOspfHelloInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanOspfHelloInt.setStatus("mandatory")


class _IflanOspfDeadInt_Type(Integer32):
    """Custom type iflanOspfDeadInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_IflanOspfDeadInt_Type.__name__ = "Integer32"
_IflanOspfDeadInt_Object = MibTableColumn
iflanOspfDeadInt = _IflanOspfDeadInt_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 27),
    _IflanOspfDeadInt_Type()
)
iflanOspfDeadInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanOspfDeadInt.setStatus("mandatory")
_IflanOspfPassword_Type = DisplayString
_IflanOspfPassword_Object = MibTableColumn
iflanOspfPassword = _IflanOspfPassword_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 28),
    _IflanOspfPassword_Type()
)
iflanOspfPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanOspfPassword.setStatus("mandatory")


class _IflanOspfMetricCost_Type(Integer32):
    """Custom type iflanOspfMetricCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_IflanOspfMetricCost_Type.__name__ = "Integer32"
_IflanOspfMetricCost_Object = MibTableColumn
iflanOspfMetricCost = _IflanOspfMetricCost_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 29),
    _IflanOspfMetricCost_Type()
)
iflanOspfMetricCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanOspfMetricCost.setStatus("mandatory")


class _IflanIpRipTxRx_Type(Integer32):
    """Custom type iflanIpRipTxRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("duplex", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("rx-only", 3),
          ("tx-only", 2))
    )


_IflanIpRipTxRx_Type.__name__ = "Integer32"
_IflanIpRipTxRx_Object = MibTableColumn
iflanIpRipTxRx = _IflanIpRipTxRx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 30),
    _IflanIpRipTxRx_Type()
)
iflanIpRipTxRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanIpRipTxRx.setStatus("mandatory")


class _IflanIpRipAuthType_Type(Integer32):
    """Custom type iflanIpRipAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("simple", 2))
    )


_IflanIpRipAuthType_Type.__name__ = "Integer32"
_IflanIpRipAuthType_Object = MibTableColumn
iflanIpRipAuthType = _IflanIpRipAuthType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 31),
    _IflanIpRipAuthType_Type()
)
iflanIpRipAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanIpRipAuthType.setStatus("mandatory")
_IflanIpRipPassword_Type = DisplayString
_IflanIpRipPassword_Object = MibTableColumn
iflanIpRipPassword = _IflanIpRipPassword_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 3, 2, 1, 32),
    _IflanIpRipPassword_Type()
)
iflanIpRipPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iflanIpRipPassword.setStatus("mandatory")
_Pu_ObjectIdentity = ObjectIdentity
pu = _Pu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4)
)
_PuNumber_Type = Integer32
_PuNumber_Object = MibScalar
puNumber = _PuNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 1),
    _PuNumber_Type()
)
puNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puNumber.setStatus("mandatory")
_PuTable_Object = MibTable
puTable = _PuTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2)
)
if mibBuilder.loadTexts:
    puTable.setStatus("mandatory")
_PuEntry_Object = MibTableRow
puEntry = _PuEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1)
)
puEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "puIndex"),
)
if mibBuilder.loadTexts:
    puEntry.setStatus("mandatory")
_PuIndex_Type = Integer32
_PuIndex_Object = MibTableColumn
puIndex = _PuIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 1),
    _PuIndex_Type()
)
puIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    puIndex.setStatus("mandatory")


class _PuMode_Type(Integer32):
    """Custom type puMode based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ban-link", 15),
          ("bnn-link", 16),
          ("dlsw-ban", 13),
          ("dlsw-bnn", 14),
          ("dlsw-links", 8),
          ("llc-ban", 11),
          ("llc-bnn", 12),
          ("llc-dlsw", 6),
          ("llc-links", 7),
          ("not-applicable", 254),
          ("not-available", 255),
          ("off", 1),
          ("sdlc-ban", 9),
          ("sdlc-bnn", 10),
          ("sdlc-dlsw", 4),
          ("sdlc-links", 5),
          ("sdlc-llc", 2),
          ("sdlc-sdlc", 3))
    )


_PuMode_Type.__name__ = "Integer32"
_PuMode_Object = MibTableColumn
puMode = _PuMode_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 2),
    _PuMode_Type()
)
puMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puMode.setStatus("mandatory")


class _PuActive_Type(Integer32):
    """Custom type puActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_PuActive_Type.__name__ = "Integer32"
_PuActive_Object = MibTableColumn
puActive = _PuActive_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 3),
    _PuActive_Type()
)
puActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puActive.setStatus("mandatory")


class _PuDelayBeforeConn_s_Type(Integer32):
    """Custom type puDelayBeforeConn_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PuDelayBeforeConn_s_Type.__name__ = "Integer32"
_PuDelayBeforeConn_s_Object = MibScalar
puDelayBeforeConn_s = _PuDelayBeforeConn_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 4),
    _PuDelayBeforeConn_s_Type()
)
puDelayBeforeConn_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puDelayBeforeConn_s.setStatus("mandatory")


class _PuRole_Type(Integer32):
    """Custom type puRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 254),
          ("not-available", 255),
          ("primary", 2),
          ("secondary", 1))
    )


_PuRole_Type.__name__ = "Integer32"
_PuRole_Object = MibTableColumn
puRole = _PuRole_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 5),
    _PuRole_Type()
)
puRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puRole.setStatus("mandatory")
_PuSdlcPort_Type = Integer32
_PuSdlcPort_Object = MibTableColumn
puSdlcPort = _PuSdlcPort_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 6),
    _PuSdlcPort_Type()
)
puSdlcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puSdlcPort.setStatus("mandatory")


class _PuSdlcAddress_Type(OctetString):
    """Custom type puSdlcAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PuSdlcAddress_Type.__name__ = "OctetString"
_PuSdlcAddress_Object = MibTableColumn
puSdlcAddress = _PuSdlcAddress_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 7),
    _PuSdlcAddress_Type()
)
puSdlcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puSdlcAddress.setStatus("mandatory")
_PuSdlcPort2_Type = Integer32
_PuSdlcPort2_Object = MibTableColumn
puSdlcPort2 = _PuSdlcPort2_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 8),
    _PuSdlcPort2_Type()
)
puSdlcPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puSdlcPort2.setStatus("mandatory")


class _PuSdlcAddress2_Type(OctetString):
    """Custom type puSdlcAddress2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PuSdlcAddress2_Type.__name__ = "OctetString"
_PuSdlcAddress2_Object = MibTableColumn
puSdlcAddress2 = _PuSdlcAddress2_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 9),
    _PuSdlcAddress2_Type()
)
puSdlcAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puSdlcAddress2.setStatus("mandatory")


class _PuSdlcTimeout_ms_Type(Integer32):
    """Custom type puSdlcTimeout_ms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )


_PuSdlcTimeout_ms_Type.__name__ = "Integer32"
_PuSdlcTimeout_ms_Object = MibScalar
puSdlcTimeout_ms = _PuSdlcTimeout_ms_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 10),
    _PuSdlcTimeout_ms_Type()
)
puSdlcTimeout_ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puSdlcTimeout_ms.setStatus("mandatory")


class _PuSdlcRetry_Type(Integer32):
    """Custom type puSdlcRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PuSdlcRetry_Type.__name__ = "Integer32"
_PuSdlcRetry_Object = MibTableColumn
puSdlcRetry = _PuSdlcRetry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 11),
    _PuSdlcRetry_Type()
)
puSdlcRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puSdlcRetry.setStatus("mandatory")


class _PuSdlcWindow_Type(Integer32):
    """Custom type puSdlcWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_PuSdlcWindow_Type.__name__ = "Integer32"
_PuSdlcWindow_Object = MibTableColumn
puSdlcWindow = _PuSdlcWindow_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 12),
    _PuSdlcWindow_Type()
)
puSdlcWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puSdlcWindow.setStatus("mandatory")
_PuSdlcMaxFrame_Type = Integer32
_PuSdlcMaxFrame_Object = MibTableColumn
puSdlcMaxFrame = _PuSdlcMaxFrame_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 13),
    _PuSdlcMaxFrame_Type()
)
puSdlcMaxFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puSdlcMaxFrame.setStatus("mandatory")


class _PuLlcDa_Type(OctetString):
    """Custom type puLlcDa based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PuLlcDa_Type.__name__ = "OctetString"
_PuLlcDa_Object = MibTableColumn
puLlcDa = _PuLlcDa_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 14),
    _PuLlcDa_Type()
)
puLlcDa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puLlcDa.setStatus("mandatory")


class _PuLlcTr_Routing_Type(Integer32):
    """Custom type puLlcTr_Routing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 254),
          ("not-available", 255),
          ("src", 2),
          ("trsp", 1))
    )


_PuLlcTr_Routing_Type.__name__ = "Integer32"
_PuLlcTr_Routing_Object = MibScalar
puLlcTr_Routing = _PuLlcTr_Routing_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 15),
    _PuLlcTr_Routing_Type()
)
puLlcTr_Routing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puLlcTr_Routing.setStatus("mandatory")


class _PuLlcSsap_Type(OctetString):
    """Custom type puLlcSsap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PuLlcSsap_Type.__name__ = "OctetString"
_PuLlcSsap_Object = MibTableColumn
puLlcSsap = _PuLlcSsap_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 16),
    _PuLlcSsap_Type()
)
puLlcSsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puLlcSsap.setStatus("mandatory")


class _PuLlcDsap_Type(OctetString):
    """Custom type puLlcDsap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PuLlcDsap_Type.__name__ = "OctetString"
_PuLlcDsap_Object = MibTableColumn
puLlcDsap = _PuLlcDsap_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 17),
    _PuLlcDsap_Type()
)
puLlcDsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puLlcDsap.setStatus("mandatory")


class _PuLlcTimeout_ms_Type(Integer32):
    """Custom type puLlcTimeout_ms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )


_PuLlcTimeout_ms_Type.__name__ = "Integer32"
_PuLlcTimeout_ms_Object = MibScalar
puLlcTimeout_ms = _PuLlcTimeout_ms_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 18),
    _PuLlcTimeout_ms_Type()
)
puLlcTimeout_ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puLlcTimeout_ms.setStatus("mandatory")


class _PuLlcRetry_Type(Integer32):
    """Custom type puLlcRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PuLlcRetry_Type.__name__ = "Integer32"
_PuLlcRetry_Object = MibTableColumn
puLlcRetry = _PuLlcRetry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 19),
    _PuLlcRetry_Type()
)
puLlcRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puLlcRetry.setStatus("mandatory")


class _PuLlcWindow_Type(Integer32):
    """Custom type puLlcWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_PuLlcWindow_Type.__name__ = "Integer32"
_PuLlcWindow_Object = MibTableColumn
puLlcWindow = _PuLlcWindow_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 20),
    _PuLlcWindow_Type()
)
puLlcWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puLlcWindow.setStatus("mandatory")


class _PuLlcDynamicWindow_Type(Integer32):
    """Custom type puLlcDynamicWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PuLlcDynamicWindow_Type.__name__ = "Integer32"
_PuLlcDynamicWindow_Object = MibTableColumn
puLlcDynamicWindow = _PuLlcDynamicWindow_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 21),
    _PuLlcDynamicWindow_Type()
)
puLlcDynamicWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puLlcDynamicWindow.setStatus("mandatory")
_PuLlcMaxFrame_Type = Integer32
_PuLlcMaxFrame_Object = MibTableColumn
puLlcMaxFrame = _PuLlcMaxFrame_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 23),
    _PuLlcMaxFrame_Type()
)
puLlcMaxFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puLlcMaxFrame.setStatus("mandatory")


class _PuDlsDa_Type(OctetString):
    """Custom type puDlsDa based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PuDlsDa_Type.__name__ = "OctetString"
_PuDlsDa_Object = MibTableColumn
puDlsDa = _PuDlsDa_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 24),
    _PuDlsDa_Type()
)
puDlsDa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puDlsDa.setStatus("mandatory")


class _PuDlsSsap_Type(OctetString):
    """Custom type puDlsSsap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PuDlsSsap_Type.__name__ = "OctetString"
_PuDlsSsap_Object = MibTableColumn
puDlsSsap = _PuDlsSsap_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 25),
    _PuDlsSsap_Type()
)
puDlsSsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puDlsSsap.setStatus("mandatory")


class _PuDlsDsap_Type(OctetString):
    """Custom type puDlsDsap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PuDlsDsap_Type.__name__ = "OctetString"
_PuDlsDsap_Object = MibTableColumn
puDlsDsap = _PuDlsDsap_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 26),
    _PuDlsDsap_Type()
)
puDlsDsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puDlsDsap.setStatus("mandatory")
_PuDlsIpSrc_Type = IpAddress
_PuDlsIpSrc_Object = MibTableColumn
puDlsIpSrc = _PuDlsIpSrc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 27),
    _PuDlsIpSrc_Type()
)
puDlsIpSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puDlsIpSrc.setStatus("mandatory")
_PuDlsIpDst_Type = IpAddress
_PuDlsIpDst_Object = MibTableColumn
puDlsIpDst = _PuDlsIpDst_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 28),
    _PuDlsIpDst_Type()
)
puDlsIpDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puDlsIpDst.setStatus("mandatory")
_PuDlsMaxFrame_Type = Integer32
_PuDlsMaxFrame_Object = MibTableColumn
puDlsMaxFrame = _PuDlsMaxFrame_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 29),
    _PuDlsMaxFrame_Type()
)
puDlsMaxFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puDlsMaxFrame.setStatus("mandatory")
_PuLinkRemoteUnit_Type = DisplayString
_PuLinkRemoteUnit_Object = MibTableColumn
puLinkRemoteUnit = _PuLinkRemoteUnit_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 30),
    _PuLinkRemoteUnit_Type()
)
puLinkRemoteUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puLinkRemoteUnit.setStatus("mandatory")


class _PuLinkClassNumber_Type(Integer32):
    """Custom type puLinkClassNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PuLinkClassNumber_Type.__name__ = "Integer32"
_PuLinkClassNumber_Object = MibTableColumn
puLinkClassNumber = _PuLinkClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 31),
    _PuLinkClassNumber_Type()
)
puLinkClassNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puLinkClassNumber.setStatus("mandatory")


class _PuLinkRemPu_Type(Integer32):
    """Custom type puLinkRemPu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PuLinkRemPu_Type.__name__ = "Integer32"
_PuLinkRemPu_Object = MibTableColumn
puLinkRemPu = _PuLinkRemPu_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 32),
    _PuLinkRemPu_Type()
)
puLinkRemPu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puLinkRemPu.setStatus("mandatory")


class _PuXid_Type(Integer32):
    """Custom type puXid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("manual", 3),
          ("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_PuXid_Type.__name__ = "Integer32"
_PuXid_Object = MibTableColumn
puXid = _PuXid_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 33),
    _PuXid_Type()
)
puXid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puXid.setStatus("mandatory")


class _PuXidId_Type(OctetString):
    """Custom type puXidId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PuXidId_Type.__name__ = "OctetString"
_PuXidId_Object = MibTableColumn
puXidId = _PuXidId_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 34),
    _PuXidId_Type()
)
puXidId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puXidId.setStatus("mandatory")
_PuXidFormat_Type = Integer32
_PuXidFormat_Object = MibTableColumn
puXidFormat = _PuXidFormat_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 35),
    _PuXidFormat_Type()
)
puXidFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puXidFormat.setStatus("mandatory")
_PuXidPuType_Type = Integer32
_PuXidPuType_Object = MibTableColumn
puXidPuType = _PuXidPuType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 36),
    _PuXidPuType_Type()
)
puXidPuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puXidPuType.setStatus("mandatory")
_PuBnnPvc_Type = Integer32
_PuBnnPvc_Object = MibTableColumn
puBnnPvc = _PuBnnPvc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 37),
    _PuBnnPvc_Type()
)
puBnnPvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puBnnPvc.setStatus("mandatory")


class _PuBnnFid_Type(Integer32):
    """Custom type puBnnFid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("aPPN", 3),
          ("fID2", 1),
          ("fID4", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_PuBnnFid_Type.__name__ = "Integer32"
_PuBnnFid_Object = MibTableColumn
puBnnFid = _PuBnnFid_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 38),
    _PuBnnFid_Type()
)
puBnnFid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puBnnFid.setStatus("mandatory")


class _PuBanDa_Type(OctetString):
    """Custom type puBanDa based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PuBanDa_Type.__name__ = "OctetString"
_PuBanDa_Object = MibTableColumn
puBanDa = _PuBanDa_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 39),
    _PuBanDa_Type()
)
puBanDa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puBanDa.setStatus("mandatory")


class _PuBanBnnSsap_Type(OctetString):
    """Custom type puBanBnnSsap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PuBanBnnSsap_Type.__name__ = "OctetString"
_PuBanBnnSsap_Object = MibTableColumn
puBanBnnSsap = _PuBanBnnSsap_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 40),
    _PuBanBnnSsap_Type()
)
puBanBnnSsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puBanBnnSsap.setStatus("mandatory")


class _PuBanBnnDsap_Type(OctetString):
    """Custom type puBanBnnDsap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_PuBanBnnDsap_Type.__name__ = "OctetString"
_PuBanBnnDsap_Object = MibTableColumn
puBanBnnDsap = _PuBanBnnDsap_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 41),
    _PuBanBnnDsap_Type()
)
puBanBnnDsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puBanBnnDsap.setStatus("mandatory")


class _PuBanBnnTimeout_ms_Type(Integer32):
    """Custom type puBanBnnTimeout_ms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )


_PuBanBnnTimeout_ms_Type.__name__ = "Integer32"
_PuBanBnnTimeout_ms_Object = MibScalar
puBanBnnTimeout_ms = _PuBanBnnTimeout_ms_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 42),
    _PuBanBnnTimeout_ms_Type()
)
puBanBnnTimeout_ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puBanBnnTimeout_ms.setStatus("mandatory")


class _PuBanBnnRetry_Type(Integer32):
    """Custom type puBanBnnRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PuBanBnnRetry_Type.__name__ = "Integer32"
_PuBanBnnRetry_Object = MibTableColumn
puBanBnnRetry = _PuBanBnnRetry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 43),
    _PuBanBnnRetry_Type()
)
puBanBnnRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puBanBnnRetry.setStatus("mandatory")


class _PuBanBnnWindow_Type(Integer32):
    """Custom type puBanBnnWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_PuBanBnnWindow_Type.__name__ = "Integer32"
_PuBanBnnWindow_Object = MibTableColumn
puBanBnnWindow = _PuBanBnnWindow_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 44),
    _PuBanBnnWindow_Type()
)
puBanBnnWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puBanBnnWindow.setStatus("mandatory")


class _PuBanBnnNw_Type(Integer32):
    """Custom type puBanBnnNw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PuBanBnnNw_Type.__name__ = "Integer32"
_PuBanBnnNw_Object = MibTableColumn
puBanBnnNw = _PuBanBnnNw_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 45),
    _PuBanBnnNw_Type()
)
puBanBnnNw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puBanBnnNw.setStatus("mandatory")
_PuBanBnnMaxFrame_Type = Integer32
_PuBanBnnMaxFrame_Object = MibTableColumn
puBanBnnMaxFrame = _PuBanBnnMaxFrame_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 46),
    _PuBanBnnMaxFrame_Type()
)
puBanBnnMaxFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puBanBnnMaxFrame.setStatus("mandatory")


class _PuBanRouting_Type(Integer32):
    """Custom type puBanRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 254),
          ("not-available", 255),
          ("source", 2),
          ("source-a", 3),
          ("transparent", 1))
    )


_PuBanRouting_Type.__name__ = "Integer32"
_PuBanRouting_Object = MibTableColumn
puBanRouting = _PuBanRouting_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 4, 2, 1, 47),
    _PuBanRouting_Type()
)
puBanRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    puBanRouting.setStatus("mandatory")
_Schedule_ObjectIdentity = ObjectIdentity
schedule = _Schedule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5)
)
_ScheduleNumber_Type = Integer32
_ScheduleNumber_Object = MibScalar
scheduleNumber = _ScheduleNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5, 1),
    _ScheduleNumber_Type()
)
scheduleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scheduleNumber.setStatus("mandatory")
_ScheduleTable_Object = MibTable
scheduleTable = _ScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5, 2)
)
if mibBuilder.loadTexts:
    scheduleTable.setStatus("mandatory")
_ScheduleEntry_Object = MibTableRow
scheduleEntry = _ScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5, 2, 1)
)
scheduleEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "schedulePeriod"),
)
if mibBuilder.loadTexts:
    scheduleEntry.setStatus("mandatory")
_SchedulePeriod_Type = Integer32
_SchedulePeriod_Object = MibTableColumn
schedulePeriod = _SchedulePeriod_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5, 2, 1, 1),
    _SchedulePeriod_Type()
)
schedulePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulePeriod.setStatus("mandatory")


class _ScheduleEnable_Type(Integer32):
    """Custom type scheduleEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_ScheduleEnable_Type.__name__ = "Integer32"
_ScheduleEnable_Object = MibTableColumn
scheduleEnable = _ScheduleEnable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5, 2, 1, 2),
    _ScheduleEnable_Type()
)
scheduleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleEnable.setStatus("mandatory")


class _ScheduleDay_Type(Integer32):
    """Custom type scheduleDay based on Integer32"""
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
              10,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("friday", 7),
          ("monday", 3),
          ("not-applicable", 254),
          ("not-available", 255),
          ("saturday", 8),
          ("sunday", 2),
          ("thursday", 6),
          ("tuesday", 4),
          ("wednesday", 5),
          ("weekend", 10),
          ("workday", 9))
    )


_ScheduleDay_Type.__name__ = "Integer32"
_ScheduleDay_Object = MibTableColumn
scheduleDay = _ScheduleDay_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5, 2, 1, 3),
    _ScheduleDay_Type()
)
scheduleDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleDay.setStatus("mandatory")
_ScheduleBeginTime_Type = DisplayString
_ScheduleBeginTime_Object = MibTableColumn
scheduleBeginTime = _ScheduleBeginTime_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5, 2, 1, 4),
    _ScheduleBeginTime_Type()
)
scheduleBeginTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleBeginTime.setStatus("mandatory")
_ScheduleEndTime_Type = DisplayString
_ScheduleEndTime_Object = MibTableColumn
scheduleEndTime = _ScheduleEndTime_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5, 2, 1, 5),
    _ScheduleEndTime_Type()
)
scheduleEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scheduleEndTime.setStatus("mandatory")


class _SchedulePort1_Type(Integer32):
    """Custom type schedulePort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("answer", 3),
          ("call-backup", 4),
          ("call-bod", 5),
          ("dedicated", 2),
          ("inactive", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("wait-user", 6))
    )


_SchedulePort1_Type.__name__ = "Integer32"
_SchedulePort1_Object = MibTableColumn
schedulePort1 = _SchedulePort1_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5, 2, 1, 6),
    _SchedulePort1_Type()
)
schedulePort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedulePort1.setStatus("mandatory")


class _SchedulePort2_Type(Integer32):
    """Custom type schedulePort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("answer", 3),
          ("call-backup", 4),
          ("call-bod", 5),
          ("dedicated", 2),
          ("inactive", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("wait-user", 6))
    )


_SchedulePort2_Type.__name__ = "Integer32"
_SchedulePort2_Object = MibTableColumn
schedulePort2 = _SchedulePort2_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5, 2, 1, 7),
    _SchedulePort2_Type()
)
schedulePort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedulePort2.setStatus("mandatory")


class _SchedulePort3_Type(Integer32):
    """Custom type schedulePort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("answer", 3),
          ("call-backup", 4),
          ("call-bod", 5),
          ("dedicated", 2),
          ("inactive", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("wait-user", 6))
    )


_SchedulePort3_Type.__name__ = "Integer32"
_SchedulePort3_Object = MibTableColumn
schedulePort3 = _SchedulePort3_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5, 2, 1, 8),
    _SchedulePort3_Type()
)
schedulePort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedulePort3.setStatus("mandatory")


class _SchedulePort4_Type(Integer32):
    """Custom type schedulePort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("answer", 3),
          ("call-backup", 4),
          ("call-bod", 5),
          ("dedicated", 2),
          ("inactive", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("wait-user", 6))
    )


_SchedulePort4_Type.__name__ = "Integer32"
_SchedulePort4_Object = MibTableColumn
schedulePort4 = _SchedulePort4_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5, 2, 1, 9),
    _SchedulePort4_Type()
)
schedulePort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedulePort4.setStatus("mandatory")


class _SchedulePort5_Type(Integer32):
    """Custom type schedulePort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("answer", 3),
          ("call-backup", 4),
          ("call-bod", 5),
          ("dedicated", 2),
          ("inactive", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("wait-user", 6))
    )


_SchedulePort5_Type.__name__ = "Integer32"
_SchedulePort5_Object = MibTableColumn
schedulePort5 = _SchedulePort5_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5, 2, 1, 10),
    _SchedulePort5_Type()
)
schedulePort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedulePort5.setStatus("mandatory")


class _SchedulePort6_Type(Integer32):
    """Custom type schedulePort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("answer", 3),
          ("call-backup", 4),
          ("call-bod", 5),
          ("dedicated", 2),
          ("inactive", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("wait-user", 6))
    )


_SchedulePort6_Type.__name__ = "Integer32"
_SchedulePort6_Object = MibTableColumn
schedulePort6 = _SchedulePort6_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5, 2, 1, 11),
    _SchedulePort6_Type()
)
schedulePort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedulePort6.setStatus("mandatory")


class _SchedulePort7_Type(Integer32):
    """Custom type schedulePort7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("answer", 3),
          ("call-backup", 4),
          ("call-bod", 5),
          ("dedicated", 2),
          ("inactive", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("wait-user", 6))
    )


_SchedulePort7_Type.__name__ = "Integer32"
_SchedulePort7_Object = MibTableColumn
schedulePort7 = _SchedulePort7_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5, 2, 1, 12),
    _SchedulePort7_Type()
)
schedulePort7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedulePort7.setStatus("mandatory")


class _SchedulePort8_Type(Integer32):
    """Custom type schedulePort8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("answer", 3),
          ("call-backup", 4),
          ("call-bod", 5),
          ("dedicated", 2),
          ("inactive", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("wait-user", 6))
    )


_SchedulePort8_Type.__name__ = "Integer32"
_SchedulePort8_Object = MibTableColumn
schedulePort8 = _SchedulePort8_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 5, 2, 1, 13),
    _SchedulePort8_Type()
)
schedulePort8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedulePort8.setStatus("mandatory")
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 6)
)


class _BridgeEnable_Type(Integer32):
    """Custom type bridgeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_BridgeEnable_Type.__name__ = "Integer32"
_BridgeEnable_Object = MibScalar
bridgeEnable = _BridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 6, 1),
    _BridgeEnable_Type()
)
bridgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeEnable.setStatus("mandatory")


class _BridgeStpEnable_Type(Integer32):
    """Custom type bridgeStpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_BridgeStpEnable_Type.__name__ = "Integer32"
_BridgeStpEnable_Object = MibScalar
bridgeStpEnable = _BridgeStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 6, 2),
    _BridgeStpEnable_Type()
)
bridgeStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeStpEnable.setStatus("mandatory")


class _BridgeLanType_Type(Integer32):
    """Custom type bridgeLanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-802p3", 2),
          ("ethernet-auto", 1),
          ("ethernet-v2", 3),
          ("not-applicable", 254),
          ("not-available", 255),
          ("token-ring", 4))
    )


_BridgeLanType_Type.__name__ = "Integer32"
_BridgeLanType_Object = MibScalar
bridgeLanType = _BridgeLanType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 6, 3),
    _BridgeLanType_Type()
)
bridgeLanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeLanType.setStatus("mandatory")


class _BridgeAgingTime_s_Type(Integer32):
    """Custom type bridgeAgingTime_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_BridgeAgingTime_s_Type.__name__ = "Integer32"
_BridgeAgingTime_s_Object = MibScalar
bridgeAgingTime_s = _BridgeAgingTime_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 6, 4),
    _BridgeAgingTime_s_Type()
)
bridgeAgingTime_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeAgingTime_s.setStatus("mandatory")


class _BridgeHelloTime_s_Type(Integer32):
    """Custom type bridgeHelloTime_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BridgeHelloTime_s_Type.__name__ = "Integer32"
_BridgeHelloTime_s_Object = MibScalar
bridgeHelloTime_s = _BridgeHelloTime_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 6, 5),
    _BridgeHelloTime_s_Type()
)
bridgeHelloTime_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeHelloTime_s.setStatus("mandatory")


class _BridgeMaxAge_s_Type(Integer32):
    """Custom type bridgeMaxAge_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_BridgeMaxAge_s_Type.__name__ = "Integer32"
_BridgeMaxAge_s_Object = MibScalar
bridgeMaxAge_s = _BridgeMaxAge_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 6, 6),
    _BridgeMaxAge_s_Type()
)
bridgeMaxAge_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeMaxAge_s.setStatus("mandatory")


class _BridgeForwardDelay_s_Type(Integer32):
    """Custom type bridgeForwardDelay_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_BridgeForwardDelay_s_Type.__name__ = "Integer32"
_BridgeForwardDelay_s_Object = MibScalar
bridgeForwardDelay_s = _BridgeForwardDelay_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 6, 7),
    _BridgeForwardDelay_s_Type()
)
bridgeForwardDelay_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeForwardDelay_s.setStatus("mandatory")


class _BridgePriority_Type(Integer32):
    """Custom type bridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BridgePriority_Type.__name__ = "Integer32"
_BridgePriority_Object = MibScalar
bridgePriority = _BridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 6, 8),
    _BridgePriority_Type()
)
bridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgePriority.setStatus("mandatory")


class _BridgeTr_Number_Type(OctetString):
    """Custom type bridgeTr_Number based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_BridgeTr_Number_Type.__name__ = "OctetString"
_BridgeTr_Number_Object = MibScalar
bridgeTr_Number = _BridgeTr_Number_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 6, 9),
    _BridgeTr_Number_Type()
)
bridgeTr_Number.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeTr_Number.setStatus("mandatory")


class _BridgeTr_SteSpan_Type(Integer32):
    """Custom type bridgeTr_SteSpan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("disable", 2),
          ("forced", 3),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_BridgeTr_SteSpan_Type.__name__ = "Integer32"
_BridgeTr_SteSpan_Object = MibScalar
bridgeTr_SteSpan = _BridgeTr_SteSpan_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 6, 10),
    _BridgeTr_SteSpan_Type()
)
bridgeTr_SteSpan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeTr_SteSpan.setStatus("mandatory")


class _BridgeTr_MaxHop_Type(Integer32):
    """Custom type bridgeTr_MaxHop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_BridgeTr_MaxHop_Type.__name__ = "Integer32"
_BridgeTr_MaxHop_Object = MibScalar
bridgeTr_MaxHop = _BridgeTr_MaxHop_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 6, 11),
    _BridgeTr_MaxHop_Type()
)
bridgeTr_MaxHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeTr_MaxHop.setStatus("mandatory")
_Phone_ObjectIdentity = ObjectIdentity
phone = _Phone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 7)
)
_PhoneNumber_Type = Integer32
_PhoneNumber_Object = MibScalar
phoneNumber = _PhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 7, 1),
    _PhoneNumber_Type()
)
phoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneNumber.setStatus("mandatory")
_PhoneTable_Object = MibTable
phoneTable = _PhoneTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 7, 2)
)
if mibBuilder.loadTexts:
    phoneTable.setStatus("mandatory")
_PhoneEntry_Object = MibTableRow
phoneEntry = _PhoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 7, 2, 1)
)
phoneEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "phoneIndex"),
)
if mibBuilder.loadTexts:
    phoneEntry.setStatus("mandatory")
_PhoneIndex_Type = Integer32
_PhoneIndex_Object = MibTableColumn
phoneIndex = _PhoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 7, 2, 1, 1),
    _PhoneIndex_Type()
)
phoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phoneIndex.setStatus("mandatory")
_PhoneRemoteUnit_Type = DisplayString
_PhoneRemoteUnit_Object = MibTableColumn
phoneRemoteUnit = _PhoneRemoteUnit_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 7, 2, 1, 2),
    _PhoneRemoteUnit_Type()
)
phoneRemoteUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phoneRemoteUnit.setStatus("mandatory")
_PhonePhoneNumber_Type = DisplayString
_PhonePhoneNumber_Object = MibTableColumn
phonePhoneNumber = _PhonePhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 7, 2, 1, 3),
    _PhonePhoneNumber_Type()
)
phonePhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phonePhoneNumber.setStatus("mandatory")
_PhoneNextHop_Type = DisplayString
_PhoneNextHop_Object = MibTableColumn
phoneNextHop = _PhoneNextHop_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 7, 2, 1, 4),
    _PhoneNextHop_Type()
)
phoneNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phoneNextHop.setStatus("mandatory")


class _PhoneCost_Type(Integer32):
    """Custom type phoneCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_PhoneCost_Type.__name__ = "Integer32"
_PhoneCost_Object = MibTableColumn
phoneCost = _PhoneCost_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 7, 2, 1, 5),
    _PhoneCost_Type()
)
phoneCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phoneCost.setStatus("mandatory")
_Filter_ObjectIdentity = ObjectIdentity
filter = _Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 8)
)
_FilterNumber_Type = Integer32
_FilterNumber_Object = MibScalar
filterNumber = _FilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 8, 1),
    _FilterNumber_Type()
)
filterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterNumber.setStatus("mandatory")
_FilterTable_Object = MibTable
filterTable = _FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 8, 2)
)
if mibBuilder.loadTexts:
    filterTable.setStatus("mandatory")
_FilterEntry_Object = MibTableRow
filterEntry = _FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 8, 2, 1)
)
filterEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "filterIndex"),
)
if mibBuilder.loadTexts:
    filterEntry.setStatus("mandatory")
_FilterIndex_Type = Integer32
_FilterIndex_Object = MibTableColumn
filterIndex = _FilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 8, 2, 1, 1),
    _FilterIndex_Type()
)
filterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterIndex.setStatus("mandatory")


class _FilterActive_Type(Integer32):
    """Custom type filterActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_FilterActive_Type.__name__ = "Integer32"
_FilterActive_Object = MibTableColumn
filterActive = _FilterActive_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 8, 2, 1, 2),
    _FilterActive_Type()
)
filterActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterActive.setStatus("mandatory")
_FilterDefinition_Type = DisplayString
_FilterDefinition_Object = MibTableColumn
filterDefinition = _FilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 8, 2, 1, 3),
    _FilterDefinition_Type()
)
filterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterDefinition.setStatus("mandatory")
__pysmi_class_ObjectIdentity = ObjectIdentity
_pysmi_class = __pysmi_class_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 9)
)
_ClassNumber_Type = Integer32
_ClassNumber_Object = MibScalar
classNumber = _ClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 9, 1),
    _ClassNumber_Type()
)
classNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classNumber.setStatus("mandatory")


class _ClassDefaultClass_Type(Integer32):
    """Custom type classDefaultClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ClassDefaultClass_Type.__name__ = "Integer32"
_ClassDefaultClass_Object = MibScalar
classDefaultClass = _ClassDefaultClass_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 9, 2),
    _ClassDefaultClass_Type()
)
classDefaultClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classDefaultClass.setStatus("mandatory")
_ClassTable_Object = MibTable
classTable = _ClassTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 9, 3)
)
if mibBuilder.loadTexts:
    classTable.setStatus("mandatory")
_ClassEntry_Object = MibTableRow
classEntry = _ClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 9, 3, 1)
)
classEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "classIndex"),
)
if mibBuilder.loadTexts:
    classEntry.setStatus("mandatory")
_ClassIndex_Type = Integer32
_ClassIndex_Object = MibTableColumn
classIndex = _ClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 9, 3, 1, 1),
    _ClassIndex_Type()
)
classIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    classIndex.setStatus("mandatory")


class _ClassWeight_Type(Integer32):
    """Custom type classWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ClassWeight_Type.__name__ = "Integer32"
_ClassWeight_Object = MibTableColumn
classWeight = _ClassWeight_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 9, 3, 1, 2),
    _ClassWeight_Type()
)
classWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classWeight.setStatus("mandatory")
_ClassPrefRoute_Type = DisplayString
_ClassPrefRoute_Object = MibTableColumn
classPrefRoute = _ClassPrefRoute_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 9, 3, 1, 3),
    _ClassPrefRoute_Type()
)
classPrefRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    classPrefRoute.setStatus("mandatory")
_Pvc_ObjectIdentity = ObjectIdentity
pvc = _Pvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10)
)
_PvcNumber_Type = Integer32
_PvcNumber_Object = MibScalar
pvcNumber = _PvcNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 1),
    _PvcNumber_Type()
)
pvcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcNumber.setStatus("mandatory")
_PvcTable_Object = MibTable
pvcTable = _PvcTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2)
)
if mibBuilder.loadTexts:
    pvcTable.setStatus("mandatory")
_PvcEntry_Object = MibTableRow
pvcEntry = _PvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1)
)
pvcEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "pvcIndex"),
)
if mibBuilder.loadTexts:
    pvcEntry.setStatus("mandatory")
_PvcIndex_Type = Integer32
_PvcIndex_Object = MibTableColumn
pvcIndex = _PvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 1),
    _PvcIndex_Type()
)
pvcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcIndex.setStatus("mandatory")


class _PvcMode_Type(Integer32):
    """Custom type pvcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 8),
          ("fp", 7),
          ("fp-multiplex", 9),
          ("multiplex", 3),
          ("not-applicable", 254),
          ("not-available", 255),
          ("off", 1),
          ("pvcr", 2),
          ("rfc-1490", 5),
          ("transp", 4))
    )


_PvcMode_Type.__name__ = "Integer32"
_PvcMode_Object = MibTableColumn
pvcMode = _PvcMode_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 2),
    _PvcMode_Type()
)
pvcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcMode.setStatus("mandatory")


class _PvcDlciAddress_Type(Integer32):
    """Custom type pvcDlciAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1022),
    )


_PvcDlciAddress_Type.__name__ = "Integer32"
_PvcDlciAddress_Object = MibTableColumn
pvcDlciAddress = _PvcDlciAddress_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 3),
    _PvcDlciAddress_Type()
)
pvcDlciAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcDlciAddress.setStatus("mandatory")
_PvcPort_Type = Integer32
_PvcPort_Object = MibTableColumn
pvcPort = _PvcPort_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 4),
    _PvcPort_Type()
)
pvcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcPort.setStatus("mandatory")
_PvcUserPort_Type = Integer32
_PvcUserPort_Object = MibTableColumn
pvcUserPort = _PvcUserPort_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 5),
    _PvcUserPort_Type()
)
pvcUserPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcUserPort.setStatus("mandatory")


class _PvcInfoRate_Type(Integer32):
    """Custom type pvcInfoRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 2000000),
    )


_PvcInfoRate_Type.__name__ = "Integer32"
_PvcInfoRate_Object = MibTableColumn
pvcInfoRate = _PvcInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 6),
    _PvcInfoRate_Type()
)
pvcInfoRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcInfoRate.setStatus("mandatory")


class _PvcPriority_Type(Integer32):
    """Custom type pvcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PvcPriority_Type.__name__ = "Integer32"
_PvcPriority_Object = MibTableColumn
pvcPriority = _PvcPriority_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 9),
    _PvcPriority_Type()
)
pvcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcPriority.setStatus("mandatory")


class _PvcCost_Type(Integer32):
    """Custom type pvcCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PvcCost_Type.__name__ = "Integer32"
_PvcCost_Object = MibTableColumn
pvcCost = _PvcCost_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 10),
    _PvcCost_Type()
)
pvcCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pvcCost.setStatus("mandatory")
_PvcRemoteUnit_Type = DisplayString
_PvcRemoteUnit_Object = MibTableColumn
pvcRemoteUnit = _PvcRemoteUnit_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 11),
    _PvcRemoteUnit_Type()
)
pvcRemoteUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcRemoteUnit.setStatus("mandatory")


class _PvcTimeout_ms_Type(Integer32):
    """Custom type pvcTimeout_ms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 30000),
    )


_PvcTimeout_ms_Type.__name__ = "Integer32"
_PvcTimeout_ms_Object = MibScalar
pvcTimeout_ms = _PvcTimeout_ms_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 12),
    _PvcTimeout_ms_Type()
)
pvcTimeout_ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcTimeout_ms.setStatus("mandatory")


class _PvcRetry_Type(Integer32):
    """Custom type pvcRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_PvcRetry_Type.__name__ = "Integer32"
_PvcRetry_Object = MibTableColumn
pvcRetry = _PvcRetry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 13),
    _PvcRetry_Type()
)
pvcRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcRetry.setStatus("mandatory")


class _PvcCompression_Type(Integer32):
    """Custom type pvcCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_PvcCompression_Type.__name__ = "Integer32"
_PvcCompression_Object = MibTableColumn
pvcCompression = _PvcCompression_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 14),
    _PvcCompression_Type()
)
pvcCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcCompression.setStatus("mandatory")
_PvcIpAddress_Type = IpAddress
_PvcIpAddress_Object = MibTableColumn
pvcIpAddress = _PvcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 15),
    _PvcIpAddress_Type()
)
pvcIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcIpAddress.setStatus("mandatory")
_PvcSubnetMask_Type = IpAddress
_PvcSubnetMask_Object = MibTableColumn
pvcSubnetMask = _PvcSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 16),
    _PvcSubnetMask_Type()
)
pvcSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcSubnetMask.setStatus("mandatory")


class _PvcMaxFrame_Type(Integer32):
    """Custom type pvcMaxFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 8192),
    )


_PvcMaxFrame_Type.__name__ = "Integer32"
_PvcMaxFrame_Object = MibTableColumn
pvcMaxFrame = _PvcMaxFrame_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 17),
    _PvcMaxFrame_Type()
)
pvcMaxFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcMaxFrame.setStatus("mandatory")


class _PvcBroadcastGroup_Type(Integer32):
    """Custom type pvcBroadcastGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_PvcBroadcastGroup_Type.__name__ = "Integer32"
_PvcBroadcastGroup_Object = MibTableColumn
pvcBroadcastGroup = _PvcBroadcastGroup_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 18),
    _PvcBroadcastGroup_Type()
)
pvcBroadcastGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcBroadcastGroup.setStatus("mandatory")


class _PvcBrgConnection_Type(Integer32):
    """Custom type pvcBrgConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_PvcBrgConnection_Type.__name__ = "Integer32"
_PvcBrgConnection_Object = MibTableColumn
pvcBrgConnection = _PvcBrgConnection_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 19),
    _PvcBrgConnection_Type()
)
pvcBrgConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcBrgConnection.setStatus("mandatory")


class _PvcIpConnection_Type(Integer32):
    """Custom type pvcIpConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_PvcIpConnection_Type.__name__ = "Integer32"
_PvcIpConnection_Object = MibTableColumn
pvcIpConnection = _PvcIpConnection_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 20),
    _PvcIpConnection_Type()
)
pvcIpConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcIpConnection.setStatus("mandatory")


class _PvcRemotePvc_Type(Integer32):
    """Custom type pvcRemotePvc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_PvcRemotePvc_Type.__name__ = "Integer32"
_PvcRemotePvc_Object = MibTableColumn
pvcRemotePvc = _PvcRemotePvc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 21),
    _PvcRemotePvc_Type()
)
pvcRemotePvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcRemotePvc.setStatus("mandatory")


class _PvcPvcClass_Type(Integer32):
    """Custom type pvcPvcClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PvcPvcClass_Type.__name__ = "Integer32"
_PvcPvcClass_Object = MibTableColumn
pvcPvcClass = _PvcPvcClass_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 22),
    _PvcPvcClass_Type()
)
pvcPvcClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcPvcClass.setStatus("mandatory")
_PvcNetworkPort_Type = Integer32
_PvcNetworkPort_Object = MibTableColumn
pvcNetworkPort = _PvcNetworkPort_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 23),
    _PvcNetworkPort_Type()
)
pvcNetworkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcNetworkPort.setStatus("mandatory")


class _PvcRingNumber_Type(OctetString):
    """Custom type pvcRingNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_PvcRingNumber_Type.__name__ = "OctetString"
_PvcRingNumber_Object = MibTableColumn
pvcRingNumber = _PvcRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 24),
    _PvcRingNumber_Type()
)
pvcRingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcRingNumber.setStatus("mandatory")


class _PvcIpRip_Type(Integer32):
    """Custom type pvcIpRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("v1", 2),
          ("v2-broadcast", 3),
          ("v2-multicast", 4))
    )


_PvcIpRip_Type.__name__ = "Integer32"
_PvcIpRip_Object = MibTableColumn
pvcIpRip = _PvcIpRip_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 25),
    _PvcIpRip_Type()
)
pvcIpRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcIpRip.setStatus("mandatory")


class _PvcBurstInfoRate_Type(Integer32):
    """Custom type pvcBurstInfoRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 2000000),
    )


_PvcBurstInfoRate_Type.__name__ = "Integer32"
_PvcBurstInfoRate_Object = MibTableColumn
pvcBurstInfoRate = _PvcBurstInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 26),
    _PvcBurstInfoRate_Type()
)
pvcBurstInfoRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcBurstInfoRate.setStatus("mandatory")


class _PvcUserDlci_Type(Integer32):
    """Custom type pvcUserDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1022),
    )


_PvcUserDlci_Type.__name__ = "Integer32"
_PvcUserDlci_Object = MibTableColumn
pvcUserDlci = _PvcUserDlci_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 27),
    _PvcUserDlci_Type()
)
pvcUserDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcUserDlci.setStatus("mandatory")


class _PvcNetworkDlci_Type(Integer32):
    """Custom type pvcNetworkDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_PvcNetworkDlci_Type.__name__ = "Integer32"
_PvcNetworkDlci_Object = MibTableColumn
pvcNetworkDlci = _PvcNetworkDlci_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 28),
    _PvcNetworkDlci_Type()
)
pvcNetworkDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcNetworkDlci.setStatus("mandatory")


class _PvcIpxRip_Type(Integer32):
    """Custom type pvcIpxRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_PvcIpxRip_Type.__name__ = "Integer32"
_PvcIpxRip_Object = MibTableColumn
pvcIpxRip = _PvcIpxRip_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 29),
    _PvcIpxRip_Type()
)
pvcIpxRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcIpxRip.setStatus("mandatory")


class _PvcIpxSap_Type(Integer32):
    """Custom type pvcIpxSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_PvcIpxSap_Type.__name__ = "Integer32"
_PvcIpxSap_Object = MibTableColumn
pvcIpxSap = _PvcIpxSap_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 30),
    _PvcIpxSap_Type()
)
pvcIpxSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcIpxSap.setStatus("mandatory")


class _PvcIpxNetNum_Type(OctetString):
    """Custom type pvcIpxNetNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_PvcIpxNetNum_Type.__name__ = "OctetString"
_PvcIpxNetNum_Object = MibTableColumn
pvcIpxNetNum = _PvcIpxNetNum_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 31),
    _PvcIpxNetNum_Type()
)
pvcIpxNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcIpxNetNum.setStatus("mandatory")


class _PvcIpxConnection_Type(Integer32):
    """Custom type pvcIpxConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_PvcIpxConnection_Type.__name__ = "Integer32"
_PvcIpxConnection_Object = MibTableColumn
pvcIpxConnection = _PvcIpxConnection_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 32),
    _PvcIpxConnection_Type()
)
pvcIpxConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcIpxConnection.setStatus("mandatory")


class _PvcType_Type(Integer32):
    """Custom type pvcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("answer", 3),
          ("call-backup", 4),
          ("dedicated", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_PvcType_Type.__name__ = "Integer32"
_PvcType_Object = MibTableColumn
pvcType = _PvcType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 33),
    _PvcType_Type()
)
pvcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcType.setStatus("mandatory")


class _PvcBackupCall_s_Type(Integer32):
    """Custom type pvcBackupCall_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PvcBackupCall_s_Type.__name__ = "Integer32"
_PvcBackupCall_s_Object = MibScalar
pvcBackupCall_s = _PvcBackupCall_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 34),
    _PvcBackupCall_s_Type()
)
pvcBackupCall_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcBackupCall_s.setStatus("mandatory")


class _PvcBackupHang_s_Type(Integer32):
    """Custom type pvcBackupHang_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PvcBackupHang_s_Type.__name__ = "Integer32"
_PvcBackupHang_s_Object = MibScalar
pvcBackupHang_s = _PvcBackupHang_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 35),
    _PvcBackupHang_s_Type()
)
pvcBackupHang_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcBackupHang_s.setStatus("mandatory")


class _PvcBackup_Type(Integer32):
    """Custom type pvcBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(15,
              16,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("all", 16),
          ("any", 15),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_PvcBackup_Type.__name__ = "Integer32"
_PvcBackup_Object = MibTableColumn
pvcBackup = _PvcBackup_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 36),
    _PvcBackup_Type()
)
pvcBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcBackup.setStatus("mandatory")


class _PvcOspfEnable_Type(Integer32):
    """Custom type pvcOspfEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_PvcOspfEnable_Type.__name__ = "Integer32"
_PvcOspfEnable_Object = MibTableColumn
pvcOspfEnable = _PvcOspfEnable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 37),
    _PvcOspfEnable_Type()
)
pvcOspfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcOspfEnable.setStatus("mandatory")
_PvcOspfAreaId_Type = IpAddress
_PvcOspfAreaId_Object = MibTableColumn
pvcOspfAreaId = _PvcOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 38),
    _PvcOspfAreaId_Type()
)
pvcOspfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcOspfAreaId.setStatus("mandatory")


class _PvcOspfTransitDelay_Type(Integer32):
    """Custom type pvcOspfTransitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 360),
    )


_PvcOspfTransitDelay_Type.__name__ = "Integer32"
_PvcOspfTransitDelay_Object = MibTableColumn
pvcOspfTransitDelay = _PvcOspfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 39),
    _PvcOspfTransitDelay_Type()
)
pvcOspfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcOspfTransitDelay.setStatus("mandatory")


class _PvcOspfRetransmitInt_Type(Integer32):
    """Custom type pvcOspfRetransmitInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 360),
    )


_PvcOspfRetransmitInt_Type.__name__ = "Integer32"
_PvcOspfRetransmitInt_Object = MibTableColumn
pvcOspfRetransmitInt = _PvcOspfRetransmitInt_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 40),
    _PvcOspfRetransmitInt_Type()
)
pvcOspfRetransmitInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcOspfRetransmitInt.setStatus("mandatory")


class _PvcOspfHelloInt_Type(Integer32):
    """Custom type pvcOspfHelloInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 360),
    )


_PvcOspfHelloInt_Type.__name__ = "Integer32"
_PvcOspfHelloInt_Object = MibTableColumn
pvcOspfHelloInt = _PvcOspfHelloInt_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 41),
    _PvcOspfHelloInt_Type()
)
pvcOspfHelloInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcOspfHelloInt.setStatus("mandatory")


class _PvcOspfDeadInt_Type(Integer32):
    """Custom type pvcOspfDeadInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_PvcOspfDeadInt_Type.__name__ = "Integer32"
_PvcOspfDeadInt_Object = MibTableColumn
pvcOspfDeadInt = _PvcOspfDeadInt_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 42),
    _PvcOspfDeadInt_Type()
)
pvcOspfDeadInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcOspfDeadInt.setStatus("mandatory")
_PvcOspfPassword_Type = DisplayString
_PvcOspfPassword_Object = MibTableColumn
pvcOspfPassword = _PvcOspfPassword_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 43),
    _PvcOspfPassword_Type()
)
pvcOspfPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcOspfPassword.setStatus("mandatory")


class _PvcOspfMetricCost_Type(Integer32):
    """Custom type pvcOspfMetricCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_PvcOspfMetricCost_Type.__name__ = "Integer32"
_PvcOspfMetricCost_Object = MibTableColumn
pvcOspfMetricCost = _PvcOspfMetricCost_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 44),
    _PvcOspfMetricCost_Type()
)
pvcOspfMetricCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcOspfMetricCost.setStatus("mandatory")


class _PvcProxyAddr_Type(Integer32):
    """Custom type pvcProxyAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PvcProxyAddr_Type.__name__ = "Integer32"
_PvcProxyAddr_Object = MibTableColumn
pvcProxyAddr = _PvcProxyAddr_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 45),
    _PvcProxyAddr_Type()
)
pvcProxyAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcProxyAddr.setStatus("mandatory")


class _PvcLlcConnection_Type(Integer32):
    """Custom type pvcLlcConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_PvcLlcConnection_Type.__name__ = "Integer32"
_PvcLlcConnection_Object = MibTableColumn
pvcLlcConnection = _PvcLlcConnection_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 46),
    _PvcLlcConnection_Type()
)
pvcLlcConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcLlcConnection.setStatus("mandatory")


class _PvcDialTimeout_Type(Integer32):
    """Custom type pvcDialTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 255),
    )


_PvcDialTimeout_Type.__name__ = "Integer32"
_PvcDialTimeout_Object = MibTableColumn
pvcDialTimeout = _PvcDialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 47),
    _PvcDialTimeout_Type()
)
pvcDialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcDialTimeout.setStatus("mandatory")


class _PvcMaxChannels_Type(Integer32):
    """Custom type pvcMaxChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_PvcMaxChannels_Type.__name__ = "Integer32"
_PvcMaxChannels_Object = MibTableColumn
pvcMaxChannels = _PvcMaxChannels_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 48),
    _PvcMaxChannels_Type()
)
pvcMaxChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcMaxChannels.setStatus("mandatory")


class _PvcHuntForwardingAUnit_Type(DisplayString):
    """Custom type pvcHuntForwardingAUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PvcHuntForwardingAUnit_Type.__name__ = "DisplayString"
_PvcHuntForwardingAUnit_Object = MibTableColumn
pvcHuntForwardingAUnit = _PvcHuntForwardingAUnit_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 49),
    _PvcHuntForwardingAUnit_Type()
)
pvcHuntForwardingAUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcHuntForwardingAUnit.setStatus("mandatory")


class _PvcHuntForwardingBUnit_Type(DisplayString):
    """Custom type pvcHuntForwardingBUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PvcHuntForwardingBUnit_Type.__name__ = "DisplayString"
_PvcHuntForwardingBUnit_Object = MibTableColumn
pvcHuntForwardingBUnit = _PvcHuntForwardingBUnit_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 50),
    _PvcHuntForwardingBUnit_Type()
)
pvcHuntForwardingBUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcHuntForwardingBUnit.setStatus("mandatory")
_PvcRemoteFpUnit_Type = DisplayString
_PvcRemoteFpUnit_Object = MibTableColumn
pvcRemoteFpUnit = _PvcRemoteFpUnit_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 51),
    _PvcRemoteFpUnit_Type()
)
pvcRemoteFpUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcRemoteFpUnit.setStatus("mandatory")


class _PvcIpRipTxRx_Type(Integer32):
    """Custom type pvcIpRipTxRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("duplex", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("rx-only", 3),
          ("tx-only", 2))
    )


_PvcIpRipTxRx_Type.__name__ = "Integer32"
_PvcIpRipTxRx_Object = MibTableColumn
pvcIpRipTxRx = _PvcIpRipTxRx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 52),
    _PvcIpRipTxRx_Type()
)
pvcIpRipTxRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcIpRipTxRx.setStatus("mandatory")


class _PvcIpRipAuthType_Type(Integer32):
    """Custom type pvcIpRipAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("simple", 2))
    )


_PvcIpRipAuthType_Type.__name__ = "Integer32"
_PvcIpRipAuthType_Object = MibTableColumn
pvcIpRipAuthType = _PvcIpRipAuthType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 53),
    _PvcIpRipAuthType_Type()
)
pvcIpRipAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcIpRipAuthType.setStatus("mandatory")
_PvcIpRipPassword_Type = DisplayString
_PvcIpRipPassword_Object = MibTableColumn
pvcIpRipPassword = _PvcIpRipPassword_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 10, 2, 1, 54),
    _PvcIpRipPassword_Type()
)
pvcIpRipPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvcIpRipPassword.setStatus("mandatory")
_Ipx_ObjectIdentity = ObjectIdentity
ipx = _Ipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 11)
)


class _IpxRouterEnable_Type(Integer32):
    """Custom type ipxRouterEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IpxRouterEnable_Type.__name__ = "Integer32"
_IpxRouterEnable_Object = MibScalar
ipxRouterEnable = _IpxRouterEnable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 11, 1),
    _IpxRouterEnable_Type()
)
ipxRouterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxRouterEnable.setStatus("mandatory")


class _IpxInternalNetNum_Type(OctetString):
    """Custom type ipxInternalNetNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxInternalNetNum_Type.__name__ = "OctetString"
_IpxInternalNetNum_Object = MibScalar
ipxInternalNetNum = _IpxInternalNetNum_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 11, 2),
    _IpxInternalNetNum_Type()
)
ipxInternalNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxInternalNetNum.setStatus("mandatory")
_Ipstatic_ObjectIdentity = ObjectIdentity
ipstatic = _Ipstatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 13)
)
_IpstaticNumber_Type = Integer32
_IpstaticNumber_Object = MibScalar
ipstaticNumber = _IpstaticNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 13, 1),
    _IpstaticNumber_Type()
)
ipstaticNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstaticNumber.setStatus("mandatory")
_IpstaticTable_Object = MibTable
ipstaticTable = _IpstaticTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 13, 2)
)
if mibBuilder.loadTexts:
    ipstaticTable.setStatus("mandatory")
_IpstaticEntry_Object = MibTableRow
ipstaticEntry = _IpstaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 13, 2, 1)
)
ipstaticEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "ipstaticIndex"),
)
if mibBuilder.loadTexts:
    ipstaticEntry.setStatus("mandatory")
_IpstaticIndex_Type = Integer32
_IpstaticIndex_Object = MibTableColumn
ipstaticIndex = _IpstaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 13, 2, 1, 1),
    _IpstaticIndex_Type()
)
ipstaticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipstaticIndex.setStatus("mandatory")


class _IpstaticValid_Type(Integer32):
    """Custom type ipstaticValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IpstaticValid_Type.__name__ = "Integer32"
_IpstaticValid_Object = MibTableColumn
ipstaticValid = _IpstaticValid_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 13, 2, 1, 2),
    _IpstaticValid_Type()
)
ipstaticValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipstaticValid.setStatus("mandatory")
_IpstaticIpDest_Type = IpAddress
_IpstaticIpDest_Object = MibTableColumn
ipstaticIpDest = _IpstaticIpDest_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 13, 2, 1, 3),
    _IpstaticIpDest_Type()
)
ipstaticIpDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipstaticIpDest.setStatus("mandatory")
_IpstaticMask_Type = IpAddress
_IpstaticMask_Object = MibTableColumn
ipstaticMask = _IpstaticMask_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 13, 2, 1, 4),
    _IpstaticMask_Type()
)
ipstaticMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipstaticMask.setStatus("mandatory")
_IpstaticNextHop_Type = IpAddress
_IpstaticNextHop_Object = MibTableColumn
ipstaticNextHop = _IpstaticNextHop_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 13, 2, 1, 5),
    _IpstaticNextHop_Type()
)
ipstaticNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipstaticNextHop.setStatus("mandatory")
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 14)
)


class _IpRouterEnable_Type(Integer32):
    """Custom type ipRouterEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IpRouterEnable_Type.__name__ = "Integer32"
_IpRouterEnable_Object = MibScalar
ipRouterEnable = _IpRouterEnable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 14, 1),
    _IpRouterEnable_Type()
)
ipRouterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouterEnable.setStatus("mandatory")
_Ospf_ObjectIdentity = ObjectIdentity
ospf = _Ospf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15)
)
_OspfGlobal_ObjectIdentity = ObjectIdentity
ospfGlobal = _OspfGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 1)
)
_OspfGlobalRouterId_Type = IpAddress
_OspfGlobalRouterId_Object = MibScalar
ospfGlobalRouterId = _OspfGlobalRouterId_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 1, 1),
    _OspfGlobalRouterId_Type()
)
ospfGlobalRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfGlobalRouterId.setStatus("mandatory")


class _OspfGlobalAutoVLink_Type(Integer32):
    """Custom type ospfGlobalAutoVLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_OspfGlobalAutoVLink_Type.__name__ = "Integer32"
_OspfGlobalAutoVLink_Object = MibScalar
ospfGlobalAutoVLink = _OspfGlobalAutoVLink_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 1, 2),
    _OspfGlobalAutoVLink_Type()
)
ospfGlobalAutoVLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfGlobalAutoVLink.setStatus("mandatory")
_OspfGlobalRackAreaId_Type = IpAddress
_OspfGlobalRackAreaId_Object = MibScalar
ospfGlobalRackAreaId = _OspfGlobalRackAreaId_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 1, 3),
    _OspfGlobalRackAreaId_Type()
)
ospfGlobalRackAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfGlobalRackAreaId.setStatus("mandatory")
_OspfGlobalGlobalAreaId_Type = IpAddress
_OspfGlobalGlobalAreaId_Object = MibScalar
ospfGlobalGlobalAreaId = _OspfGlobalGlobalAreaId_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 1, 4),
    _OspfGlobalGlobalAreaId_Type()
)
ospfGlobalGlobalAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfGlobalGlobalAreaId.setStatus("mandatory")
_OspfArea_ObjectIdentity = ObjectIdentity
ospfArea = _OspfArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 2)
)
_OspfAreaNumber_Type = Integer32
_OspfAreaNumber_Object = MibScalar
ospfAreaNumber = _OspfAreaNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 2, 1),
    _OspfAreaNumber_Type()
)
ospfAreaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNumber.setStatus("mandatory")
_OspfAreaTable_Object = MibTable
ospfAreaTable = _OspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 2, 2)
)
if mibBuilder.loadTexts:
    ospfAreaTable.setStatus("mandatory")
_OspfAreaEntry_Object = MibTableRow
ospfAreaEntry = _OspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 2, 2, 1)
)
ospfAreaEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "ospfAreaIndex"),
)
if mibBuilder.loadTexts:
    ospfAreaEntry.setStatus("mandatory")
_OspfAreaIndex_Type = Integer32
_OspfAreaIndex_Object = MibTableColumn
ospfAreaIndex = _OspfAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 2, 2, 1, 1),
    _OspfAreaIndex_Type()
)
ospfAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaIndex.setStatus("mandatory")
_OspfAreaAreaId_Type = IpAddress
_OspfAreaAreaId_Object = MibTableColumn
ospfAreaAreaId = _OspfAreaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 2, 2, 1, 2),
    _OspfAreaAreaId_Type()
)
ospfAreaAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaAreaId.setStatus("mandatory")


class _OspfAreaEnable_Type(Integer32):
    """Custom type ospfAreaEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_OspfAreaEnable_Type.__name__ = "Integer32"
_OspfAreaEnable_Object = MibTableColumn
ospfAreaEnable = _OspfAreaEnable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 2, 2, 1, 3),
    _OspfAreaEnable_Type()
)
ospfAreaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaEnable.setStatus("mandatory")


class _OspfAreaAuthType_Type(Integer32):
    """Custom type ospfAreaAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("simple", 2))
    )


_OspfAreaAuthType_Type.__name__ = "Integer32"
_OspfAreaAuthType_Object = MibTableColumn
ospfAreaAuthType = _OspfAreaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 2, 2, 1, 4),
    _OspfAreaAuthType_Type()
)
ospfAreaAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaAuthType.setStatus("mandatory")


class _OspfAreaImportASExt_Type(Integer32):
    """Custom type ospfAreaImportASExt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_OspfAreaImportASExt_Type.__name__ = "Integer32"
_OspfAreaImportASExt_Object = MibTableColumn
ospfAreaImportASExt = _OspfAreaImportASExt_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 2, 2, 1, 5),
    _OspfAreaImportASExt_Type()
)
ospfAreaImportASExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaImportASExt.setStatus("mandatory")


class _OspfAreaStubMetric_Type(Integer32):
    """Custom type ospfAreaStubMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OspfAreaStubMetric_Type.__name__ = "Integer32"
_OspfAreaStubMetric_Object = MibTableColumn
ospfAreaStubMetric = _OspfAreaStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 2, 2, 1, 6),
    _OspfAreaStubMetric_Type()
)
ospfAreaStubMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaStubMetric.setStatus("mandatory")
_OspfRange_ObjectIdentity = ObjectIdentity
ospfRange = _OspfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 3)
)
_OspfRangeNumber_Type = Integer32
_OspfRangeNumber_Object = MibScalar
ospfRangeNumber = _OspfRangeNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 3, 1),
    _OspfRangeNumber_Type()
)
ospfRangeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRangeNumber.setStatus("mandatory")
_OspfRangeTable_Object = MibTable
ospfRangeTable = _OspfRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 3, 2)
)
if mibBuilder.loadTexts:
    ospfRangeTable.setStatus("mandatory")
_OspfRangeEntry_Object = MibTableRow
ospfRangeEntry = _OspfRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 3, 2, 1)
)
ospfRangeEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "ospfRangeIndex"),
)
if mibBuilder.loadTexts:
    ospfRangeEntry.setStatus("mandatory")
_OspfRangeIndex_Type = Integer32
_OspfRangeIndex_Object = MibTableColumn
ospfRangeIndex = _OspfRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 3, 2, 1, 1),
    _OspfRangeIndex_Type()
)
ospfRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRangeIndex.setStatus("mandatory")
_OspfRangeNet_Type = IpAddress
_OspfRangeNet_Object = MibTableColumn
ospfRangeNet = _OspfRangeNet_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 3, 2, 1, 2),
    _OspfRangeNet_Type()
)
ospfRangeNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRangeNet.setStatus("mandatory")
_OspfRangeMask_Type = IpAddress
_OspfRangeMask_Object = MibTableColumn
ospfRangeMask = _OspfRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 3, 2, 1, 3),
    _OspfRangeMask_Type()
)
ospfRangeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRangeMask.setStatus("mandatory")


class _OspfRangeEnable_Type(Integer32):
    """Custom type ospfRangeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_OspfRangeEnable_Type.__name__ = "Integer32"
_OspfRangeEnable_Object = MibTableColumn
ospfRangeEnable = _OspfRangeEnable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 3, 2, 1, 4),
    _OspfRangeEnable_Type()
)
ospfRangeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRangeEnable.setStatus("mandatory")


class _OspfRangeStatus_Type(Integer32):
    """Custom type ospfRangeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("don-t-adv", 1),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_OspfRangeStatus_Type.__name__ = "Integer32"
_OspfRangeStatus_Object = MibTableColumn
ospfRangeStatus = _OspfRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 3, 2, 1, 5),
    _OspfRangeStatus_Type()
)
ospfRangeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRangeStatus.setStatus("mandatory")
_OspfRangeAddToArea_Type = IpAddress
_OspfRangeAddToArea_Object = MibTableColumn
ospfRangeAddToArea = _OspfRangeAddToArea_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 3, 2, 1, 6),
    _OspfRangeAddToArea_Type()
)
ospfRangeAddToArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRangeAddToArea.setStatus("mandatory")
_OspfVLink_ObjectIdentity = ObjectIdentity
ospfVLink = _OspfVLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 4)
)
_OspfVLinkNumber_Type = Integer32
_OspfVLinkNumber_Object = MibScalar
ospfVLinkNumber = _OspfVLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 4, 1),
    _OspfVLinkNumber_Type()
)
ospfVLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVLinkNumber.setStatus("mandatory")
_OspfVLinkTable_Object = MibTable
ospfVLinkTable = _OspfVLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 4, 2)
)
if mibBuilder.loadTexts:
    ospfVLinkTable.setStatus("mandatory")
_OspfVLinkEntry_Object = MibTableRow
ospfVLinkEntry = _OspfVLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 4, 2, 1)
)
ospfVLinkEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "ospfVLinkIndex"),
)
if mibBuilder.loadTexts:
    ospfVLinkEntry.setStatus("mandatory")
_OspfVLinkIndex_Type = Integer32
_OspfVLinkIndex_Object = MibTableColumn
ospfVLinkIndex = _OspfVLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 4, 2, 1, 1),
    _OspfVLinkIndex_Type()
)
ospfVLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVLinkIndex.setStatus("mandatory")
_OspfVLinkTransitAreaId_Type = IpAddress
_OspfVLinkTransitAreaId_Object = MibTableColumn
ospfVLinkTransitAreaId = _OspfVLinkTransitAreaId_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 4, 2, 1, 2),
    _OspfVLinkTransitAreaId_Type()
)
ospfVLinkTransitAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVLinkTransitAreaId.setStatus("mandatory")
_OspfVLinkNeighborRtrId_Type = IpAddress
_OspfVLinkNeighborRtrId_Object = MibTableColumn
ospfVLinkNeighborRtrId = _OspfVLinkNeighborRtrId_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 4, 2, 1, 3),
    _OspfVLinkNeighborRtrId_Type()
)
ospfVLinkNeighborRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVLinkNeighborRtrId.setStatus("mandatory")


class _OspfVLinkEnable_Type(Integer32):
    """Custom type ospfVLinkEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_OspfVLinkEnable_Type.__name__ = "Integer32"
_OspfVLinkEnable_Object = MibTableColumn
ospfVLinkEnable = _OspfVLinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 4, 2, 1, 4),
    _OspfVLinkEnable_Type()
)
ospfVLinkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVLinkEnable.setStatus("mandatory")


class _OspfVLinkTransitDelay_Type(Integer32):
    """Custom type ospfVLinkTransitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 360),
    )


_OspfVLinkTransitDelay_Type.__name__ = "Integer32"
_OspfVLinkTransitDelay_Object = MibTableColumn
ospfVLinkTransitDelay = _OspfVLinkTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 4, 2, 1, 5),
    _OspfVLinkTransitDelay_Type()
)
ospfVLinkTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVLinkTransitDelay.setStatus("mandatory")


class _OspfVLinkRetransmitInt_Type(Integer32):
    """Custom type ospfVLinkRetransmitInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 360),
    )


_OspfVLinkRetransmitInt_Type.__name__ = "Integer32"
_OspfVLinkRetransmitInt_Object = MibTableColumn
ospfVLinkRetransmitInt = _OspfVLinkRetransmitInt_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 4, 2, 1, 6),
    _OspfVLinkRetransmitInt_Type()
)
ospfVLinkRetransmitInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVLinkRetransmitInt.setStatus("mandatory")


class _OspfVLinkHelloInt_Type(Integer32):
    """Custom type ospfVLinkHelloInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 360),
    )


_OspfVLinkHelloInt_Type.__name__ = "Integer32"
_OspfVLinkHelloInt_Object = MibTableColumn
ospfVLinkHelloInt = _OspfVLinkHelloInt_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 4, 2, 1, 7),
    _OspfVLinkHelloInt_Type()
)
ospfVLinkHelloInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVLinkHelloInt.setStatus("mandatory")


class _OspfVLinkDeadInt_Type(Integer32):
    """Custom type ospfVLinkDeadInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_OspfVLinkDeadInt_Type.__name__ = "Integer32"
_OspfVLinkDeadInt_Object = MibTableColumn
ospfVLinkDeadInt = _OspfVLinkDeadInt_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 4, 2, 1, 8),
    _OspfVLinkDeadInt_Type()
)
ospfVLinkDeadInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVLinkDeadInt.setStatus("mandatory")
_OspfVLinkPassword_Type = DisplayString
_OspfVLinkPassword_Object = MibTableColumn
ospfVLinkPassword = _OspfVLinkPassword_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 15, 4, 2, 1, 9),
    _OspfVLinkPassword_Type()
)
ospfVLinkPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVLinkPassword.setStatus("mandatory")
_Ipxfilter_ObjectIdentity = ObjectIdentity
ipxfilter = _Ipxfilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 16)
)
_IpxfilterNumber_Type = Integer32
_IpxfilterNumber_Object = MibScalar
ipxfilterNumber = _IpxfilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 16, 1),
    _IpxfilterNumber_Type()
)
ipxfilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxfilterNumber.setStatus("mandatory")
_IpxfilterTable_Object = MibTable
ipxfilterTable = _IpxfilterTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 16, 2)
)
if mibBuilder.loadTexts:
    ipxfilterTable.setStatus("mandatory")
_IpxfilterEntry_Object = MibTableRow
ipxfilterEntry = _IpxfilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 16, 2, 1)
)
ipxfilterEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "ipxfilterIndex"),
)
if mibBuilder.loadTexts:
    ipxfilterEntry.setStatus("mandatory")
_IpxfilterIndex_Type = Integer32
_IpxfilterIndex_Object = MibTableColumn
ipxfilterIndex = _IpxfilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 16, 2, 1, 1),
    _IpxfilterIndex_Type()
)
ipxfilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxfilterIndex.setStatus("mandatory")


class _IpxfilterEnable_Type(Integer32):
    """Custom type ipxfilterEnable based on Integer32"""
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


_IpxfilterEnable_Type.__name__ = "Integer32"
_IpxfilterEnable_Object = MibTableColumn
ipxfilterEnable = _IpxfilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 16, 2, 1, 2),
    _IpxfilterEnable_Type()
)
ipxfilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxfilterEnable.setStatus("mandatory")


class _IpxfilterSap_Type(OctetString):
    """Custom type ipxfilterSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_IpxfilterSap_Type.__name__ = "OctetString"
_IpxfilterSap_Object = MibTableColumn
ipxfilterSap = _IpxfilterSap_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 16, 2, 1, 3),
    _IpxfilterSap_Type()
)
ipxfilterSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxfilterSap.setStatus("mandatory")


class _IpxfilterType_Type(Integer32):
    """Custom type ipxfilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reverse", 2),
          ("standard", 1))
    )


_IpxfilterType_Type.__name__ = "Integer32"
_IpxfilterType_Object = MibTableColumn
ipxfilterType = _IpxfilterType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 16, 2, 1, 4),
    _IpxfilterType_Type()
)
ipxfilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxfilterType.setStatus("mandatory")
_Ifvce_ObjectIdentity = ObjectIdentity
ifvce = _Ifvce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18)
)
_IfvceNumber_Type = Integer32
_IfvceNumber_Object = MibScalar
ifvceNumber = _IfvceNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 1),
    _IfvceNumber_Type()
)
ifvceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifvceNumber.setStatus("mandatory")
_IfvceTable_Object = MibTable
ifvceTable = _IfvceTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2)
)
if mibBuilder.loadTexts:
    ifvceTable.setStatus("mandatory")
_IfvceEntry_Object = MibTableRow
ifvceEntry = _IfvceEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1)
)
ifvceEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "ifvceIndex"),
)
if mibBuilder.loadTexts:
    ifvceEntry.setStatus("mandatory")
_IfvceIndex_Type = Integer32
_IfvceIndex_Object = MibTableColumn
ifvceIndex = _IfvceIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 1),
    _IfvceIndex_Type()
)
ifvceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifvceIndex.setStatus("mandatory")
_IfvceDesc_Type = DisplayString
_IfvceDesc_Object = MibTableColumn
ifvceDesc = _IfvceDesc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 2),
    _IfvceDesc_Type()
)
ifvceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifvceDesc.setStatus("mandatory")


class _IfvceProtocol_Type(Integer32):
    """Custom type ifvceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              21,
              22,
              23,
              24,
              26,
              30,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("acelp-4-8-kbs", 22),
          ("acelp-8-kbs", 21),
          ("acelp-cn", 30),
          ("adpcm32k", 24),
          ("atc16k", 26),
          ("not-applicable", 254),
          ("not-available", 255),
          ("off", 1),
          ("pcm64k", 23))
    )


_IfvceProtocol_Type.__name__ = "Integer32"
_IfvceProtocol_Object = MibTableColumn
ifvceProtocol = _IfvceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 3),
    _IfvceProtocol_Type()
)
ifvceProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceProtocol.setStatus("mandatory")


class _IfvceInterface_Type(Integer32):
    """Custom type ifvceInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ac15", 4),
          ("e-and-m", 3),
          ("fx0", 2),
          ("fxs", 1),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfvceInterface_Type.__name__ = "Integer32"
_IfvceInterface_Object = MibTableColumn
ifvceInterface = _IfvceInterface_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 4),
    _IfvceInterface_Type()
)
ifvceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceInterface.setStatus("mandatory")


class _IfvceRemotePort_Type(Integer32):
    """Custom type ifvceRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 899),
    )


_IfvceRemotePort_Type.__name__ = "Integer32"
_IfvceRemotePort_Object = MibTableColumn
ifvceRemotePort = _IfvceRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 5),
    _IfvceRemotePort_Type()
)
ifvceRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceRemotePort.setStatus("mandatory")


class _IfvceActivationType_Type(Integer32):
    """Custom type ifvceActivationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("autodial", 3),
          ("broadcast", 4),
          ("not-applicable", 254),
          ("not-available", 255),
          ("predefined", 1),
          ("switched", 2))
    )


_IfvceActivationType_Type.__name__ = "Integer32"
_IfvceActivationType_Object = MibTableColumn
ifvceActivationType = _IfvceActivationType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 6),
    _IfvceActivationType_Type()
)
ifvceActivationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceActivationType.setStatus("mandatory")
_IfvceRemoteUnit_Type = DisplayString
_IfvceRemoteUnit_Object = MibTableColumn
ifvceRemoteUnit = _IfvceRemoteUnit_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 7),
    _IfvceRemoteUnit_Type()
)
ifvceRemoteUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceRemoteUnit.setStatus("mandatory")


class _IfvceHuntGroup_Type(Integer32):
    """Custom type ifvceHuntGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("a", 2),
          ("b", 3),
          ("no", 1),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfvceHuntGroup_Type.__name__ = "Integer32"
_IfvceHuntGroup_Object = MibTableColumn
ifvceHuntGroup = _IfvceHuntGroup_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 8),
    _IfvceHuntGroup_Type()
)
ifvceHuntGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceHuntGroup.setStatus("mandatory")


class _IfvceToneDetectRegen_s_Type(Integer32):
    """Custom type ifvceToneDetectRegen_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IfvceToneDetectRegen_s_Type.__name__ = "Integer32"
_IfvceToneDetectRegen_s_Object = MibScalar
ifvceToneDetectRegen_s = _IfvceToneDetectRegen_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 9),
    _IfvceToneDetectRegen_s_Type()
)
ifvceToneDetectRegen_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceToneDetectRegen_s.setStatus("mandatory")


class _IfvcePulseMakeBreak_ms_Type(Integer32):
    """Custom type ifvcePulseMakeBreak_ms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 80),
    )


_IfvcePulseMakeBreak_ms_Type.__name__ = "Integer32"
_IfvcePulseMakeBreak_ms_Object = MibScalar
ifvcePulseMakeBreak_ms = _IfvcePulseMakeBreak_ms_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 10),
    _IfvcePulseMakeBreak_ms_Type()
)
ifvcePulseMakeBreak_ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvcePulseMakeBreak_ms.setStatus("mandatory")


class _IfvceToneOn_ms_Type(Integer32):
    """Custom type ifvceToneOn_ms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1000),
    )


_IfvceToneOn_ms_Type.__name__ = "Integer32"
_IfvceToneOn_ms_Object = MibScalar
ifvceToneOn_ms = _IfvceToneOn_ms_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 11),
    _IfvceToneOn_ms_Type()
)
ifvceToneOn_ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceToneOn_ms.setStatus("mandatory")


class _IfvceToneOff_ms_Type(Integer32):
    """Custom type ifvceToneOff_ms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1000),
    )


_IfvceToneOff_ms_Type.__name__ = "Integer32"
_IfvceToneOff_ms_Object = MibScalar
ifvceToneOff_ms = _IfvceToneOff_ms_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 12),
    _IfvceToneOff_ms_Type()
)
ifvceToneOff_ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceToneOff_ms.setStatus("mandatory")


class _IfvceSilenceSuppress_Type(Integer32):
    """Custom type ifvceSilenceSuppress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 20),
    )


_IfvceSilenceSuppress_Type.__name__ = "Integer32"
_IfvceSilenceSuppress_Object = MibTableColumn
ifvceSilenceSuppress = _IfvceSilenceSuppress_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 13),
    _IfvceSilenceSuppress_Type()
)
ifvceSilenceSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceSilenceSuppress.setStatus("mandatory")


class _IfvceSignaling_Type(Integer32):
    """Custom type ifvceSignaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              10,
              11,
              12,
              13,
              14,
              15,
              17,
              18,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              30,
              32,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ab00", 30),
          ("ac15-a", 4),
          ("ac15-c", 6),
          ("e-and-m-2W-colisee", 18),
          ("e-and-m-2W-delay-dial", 15),
          ("e-and-m-2W-imm-start", 2),
          ("e-and-m-2W-timed-e", 11),
          ("e-and-m-2W-wink-start", 13),
          ("e-and-m-4W-colisee", 17),
          ("e-and-m-4W-delay-dial", 14),
          ("e-and-m-4W-wink-start", 12),
          ("e-and-m-4w-imm-start", 1),
          ("e-and-m-4w-timed-e", 10),
          ("fxo", 23),
          ("fxs", 24),
          ("gnd-fxo", 25),
          ("gnd-fxs", 26),
          ("imm-start", 21),
          ("loop-start", 3),
          ("not-applicable", 254),
          ("not-available", 255),
          ("plar", 27),
          ("poi", 28),
          ("r2", 22),
          ("wink-start", 32))
    )


_IfvceSignaling_Type.__name__ = "Integer32"
_IfvceSignaling_Object = MibTableColumn
ifvceSignaling = _IfvceSignaling_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 14),
    _IfvceSignaling_Type()
)
ifvceSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceSignaling.setStatus("mandatory")


class _IfvceLocalInbound_Type(Integer32):
    """Custom type ifvceLocalInbound based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("db-1", 22),
          ("db-10", 13),
          ("db-11", 12),
          ("db-12", 11),
          ("db-13", 10),
          ("db-14", 9),
          ("db-15", 8),
          ("db-16", 7),
          ("db-17", 6),
          ("db-18", 5),
          ("db-19", 4),
          ("db-2", 21),
          ("db-20", 3),
          ("db-21", 2),
          ("db-22", 1),
          ("db-3", 20),
          ("db-4", 19),
          ("db-5", 18),
          ("db-6", 17),
          ("db-7", 16),
          ("db-8", 15),
          ("db-9", 14),
          ("db0", 23),
          ("db1", 24),
          ("db2", 25),
          ("db3", 26),
          ("db4", 27),
          ("db5", 28),
          ("db6", 29),
          ("db7", 30),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfvceLocalInbound_Type.__name__ = "Integer32"
_IfvceLocalInbound_Object = MibTableColumn
ifvceLocalInbound = _IfvceLocalInbound_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 16),
    _IfvceLocalInbound_Type()
)
ifvceLocalInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceLocalInbound.setStatus("mandatory")


class _IfvceLocalOutbound_Type(Integer32):
    """Custom type ifvceLocalOutbound based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("db-1", 22),
          ("db-10", 13),
          ("db-11", 12),
          ("db-12", 11),
          ("db-13", 10),
          ("db-14", 9),
          ("db-15", 8),
          ("db-16", 7),
          ("db-17", 6),
          ("db-18", 5),
          ("db-19", 4),
          ("db-2", 21),
          ("db-20", 3),
          ("db-21", 2),
          ("db-22", 1),
          ("db-3", 20),
          ("db-4", 19),
          ("db-5", 18),
          ("db-6", 17),
          ("db-7", 16),
          ("db-8", 15),
          ("db-9", 14),
          ("db0", 23),
          ("db1", 24),
          ("db2", 25),
          ("db3", 26),
          ("db4", 27),
          ("db5", 28),
          ("db6", 29),
          ("db7", 30),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfvceLocalOutbound_Type.__name__ = "Integer32"
_IfvceLocalOutbound_Object = MibTableColumn
ifvceLocalOutbound = _IfvceLocalOutbound_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 17),
    _IfvceLocalOutbound_Type()
)
ifvceLocalOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceLocalOutbound.setStatus("mandatory")


class _IfvceFaxModemRelay_Type(Integer32):
    """Custom type ifvceFaxModemRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("fax", 2),
          ("none", 1),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfvceFaxModemRelay_Type.__name__ = "Integer32"
_IfvceFaxModemRelay_Object = MibTableColumn
ifvceFaxModemRelay = _IfvceFaxModemRelay_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 18),
    _IfvceFaxModemRelay_Type()
)
ifvceFaxModemRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceFaxModemRelay.setStatus("mandatory")


class _IfvceFxoTimeout_s_Type(Integer32):
    """Custom type ifvceFxoTimeout_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_IfvceFxoTimeout_s_Type.__name__ = "Integer32"
_IfvceFxoTimeout_s_Object = MibScalar
ifvceFxoTimeout_s = _IfvceFxoTimeout_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 19),
    _IfvceFxoTimeout_s_Type()
)
ifvceFxoTimeout_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceFxoTimeout_s.setStatus("mandatory")


class _IfvceTeTimer_s_Type(Integer32):
    """Custom type ifvceTeTimer_s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IfvceTeTimer_s_Type.__name__ = "Integer32"
_IfvceTeTimer_s_Object = MibScalar
ifvceTeTimer_s = _IfvceTeTimer_s_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 20),
    _IfvceTeTimer_s_Type()
)
ifvceTeTimer_s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceTeTimer_s.setStatus("mandatory")


class _IfvceFwdDigits_Type(Integer32):
    """Custom type ifvceFwdDigits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("ext", 3),
          ("none", 1),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfvceFwdDigits_Type.__name__ = "Integer32"
_IfvceFwdDigits_Object = MibTableColumn
ifvceFwdDigits = _IfvceFwdDigits_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 21),
    _IfvceFwdDigits_Type()
)
ifvceFwdDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceFwdDigits.setStatus("mandatory")


class _IfvceFwdType_Type(Integer32):
    """Custom type ifvceFwdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 254),
          ("not-available", 255),
          ("pulse", 2),
          ("tone", 1))
    )


_IfvceFwdType_Type.__name__ = "Integer32"
_IfvceFwdType_Object = MibTableColumn
ifvceFwdType = _IfvceFwdType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 22),
    _IfvceFwdType_Type()
)
ifvceFwdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceFwdType.setStatus("mandatory")


class _IfvceFwdDelay_ms_Type(Integer32):
    """Custom type ifvceFwdDelay_ms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_IfvceFwdDelay_ms_Type.__name__ = "Integer32"
_IfvceFwdDelay_ms_Object = MibScalar
ifvceFwdDelay_ms = _IfvceFwdDelay_ms_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 23),
    _IfvceFwdDelay_ms_Type()
)
ifvceFwdDelay_ms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceFwdDelay_ms.setStatus("mandatory")


class _IfvceDelDigits_Type(Integer32):
    """Custom type ifvceDelDigits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_IfvceDelDigits_Type.__name__ = "Integer32"
_IfvceDelDigits_Object = MibTableColumn
ifvceDelDigits = _IfvceDelDigits_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 24),
    _IfvceDelDigits_Type()
)
ifvceDelDigits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceDelDigits.setStatus("mandatory")
_IfvceExtNumber_Type = DisplayString
_IfvceExtNumber_Object = MibTableColumn
ifvceExtNumber = _IfvceExtNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 25),
    _IfvceExtNumber_Type()
)
ifvceExtNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceExtNumber.setStatus("mandatory")


class _IfvceLinkDwnBusy_Type(Integer32):
    """Custom type ifvceLinkDwnBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 3),
          ("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfvceLinkDwnBusy_Type.__name__ = "Integer32"
_IfvceLinkDwnBusy_Object = MibTableColumn
ifvceLinkDwnBusy = _IfvceLinkDwnBusy_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 27),
    _IfvceLinkDwnBusy_Type()
)
ifvceLinkDwnBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceLinkDwnBusy.setStatus("mandatory")


class _IfvceToneType_Type(Integer32):
    """Custom type ifvceToneType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 0),
          ("mf", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("r2", 2))
    )


_IfvceToneType_Type.__name__ = "Integer32"
_IfvceToneType_Object = MibTableColumn
ifvceToneType = _IfvceToneType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 28),
    _IfvceToneType_Type()
)
ifvceToneType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceToneType.setStatus("mandatory")


class _IfvceRate8kx1_Type(Integer32):
    """Custom type ifvceRate8kx1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfvceRate8kx1_Type.__name__ = "Integer32"
_IfvceRate8kx1_Object = MibTableColumn
ifvceRate8kx1 = _IfvceRate8kx1_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 29),
    _IfvceRate8kx1_Type()
)
ifvceRate8kx1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceRate8kx1.setStatus("mandatory")


class _IfvceRate8kx2_Type(Integer32):
    """Custom type ifvceRate8kx2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfvceRate8kx2_Type.__name__ = "Integer32"
_IfvceRate8kx2_Object = MibTableColumn
ifvceRate8kx2 = _IfvceRate8kx2_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 30),
    _IfvceRate8kx2_Type()
)
ifvceRate8kx2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceRate8kx2.setStatus("mandatory")


class _IfvceRate5k8x1_Type(Integer32):
    """Custom type ifvceRate5k8x1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfvceRate5k8x1_Type.__name__ = "Integer32"
_IfvceRate5k8x1_Object = MibTableColumn
ifvceRate5k8x1 = _IfvceRate5k8x1_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 31),
    _IfvceRate5k8x1_Type()
)
ifvceRate5k8x1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceRate5k8x1.setStatus("mandatory")


class _IfvceRate5k8x2_Type(Integer32):
    """Custom type ifvceRate5k8x2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfvceRate5k8x2_Type.__name__ = "Integer32"
_IfvceRate5k8x2_Object = MibTableColumn
ifvceRate5k8x2 = _IfvceRate5k8x2_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 32),
    _IfvceRate5k8x2_Type()
)
ifvceRate5k8x2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceRate5k8x2.setStatus("mandatory")


class _IfvceDVCSilenceSuppress_Type(Integer32):
    """Custom type ifvceDVCSilenceSuppress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IfvceDVCSilenceSuppress_Type.__name__ = "Integer32"
_IfvceDVCSilenceSuppress_Object = MibTableColumn
ifvceDVCSilenceSuppress = _IfvceDVCSilenceSuppress_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 33),
    _IfvceDVCSilenceSuppress_Type()
)
ifvceDVCSilenceSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceDVCSilenceSuppress.setStatus("mandatory")


class _IfvceDVCLocalInbound_Type(Integer32):
    """Custom type ifvceDVCLocalInbound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("db-1", 20),
          ("db-10", 11),
          ("db-11", 10),
          ("db-12", 9),
          ("db-2", 19),
          ("db-3", 18),
          ("db-4", 17),
          ("db-5", 16),
          ("db-6", 15),
          ("db-7", 14),
          ("db-8", 13),
          ("db-9", 12),
          ("db0", 21),
          ("db1", 22),
          ("db2", 23),
          ("db3", 24),
          ("db4", 25),
          ("db5", 26),
          ("db6", 27),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfvceDVCLocalInbound_Type.__name__ = "Integer32"
_IfvceDVCLocalInbound_Object = MibTableColumn
ifvceDVCLocalInbound = _IfvceDVCLocalInbound_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 34),
    _IfvceDVCLocalInbound_Type()
)
ifvceDVCLocalInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceDVCLocalInbound.setStatus("mandatory")


class _IfvceDVCLocalOutbound_Type(Integer32):
    """Custom type ifvceDVCLocalOutbound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("db-1", 20),
          ("db-10", 11),
          ("db-11", 10),
          ("db-12", 9),
          ("db-2", 19),
          ("db-3", 18),
          ("db-4", 17),
          ("db-5", 16),
          ("db-6", 15),
          ("db-7", 14),
          ("db-8", 13),
          ("db-9", 12),
          ("db0", 21),
          ("db1", 22),
          ("db2", 23),
          ("db3", 24),
          ("db4", 25),
          ("db5", 26),
          ("db6", 27),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfvceDVCLocalOutbound_Type.__name__ = "Integer32"
_IfvceDVCLocalOutbound_Object = MibTableColumn
ifvceDVCLocalOutbound = _IfvceDVCLocalOutbound_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 35),
    _IfvceDVCLocalOutbound_Type()
)
ifvceDVCLocalOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceDVCLocalOutbound.setStatus("mandatory")


class _IfvceBroadcastDir_Type(Integer32):
    """Custom type ifvceBroadcastDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 254),
          ("not-available", 255),
          ("rX", 2),
          ("tX", 1))
    )


_IfvceBroadcastDir_Type.__name__ = "Integer32"
_IfvceBroadcastDir_Object = MibTableColumn
ifvceBroadcastDir = _IfvceBroadcastDir_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 36),
    _IfvceBroadcastDir_Type()
)
ifvceBroadcastDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceBroadcastDir.setStatus("mandatory")


class _IfvceBroadcastPvc_Type(Integer32):
    """Custom type ifvceBroadcastPvc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_IfvceBroadcastPvc_Type.__name__ = "Integer32"
_IfvceBroadcastPvc_Object = MibTableColumn
ifvceBroadcastPvc = _IfvceBroadcastPvc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 37),
    _IfvceBroadcastPvc_Type()
)
ifvceBroadcastPvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceBroadcastPvc.setStatus("mandatory")


class _IfvceAnalogLinkDwnBusy_Type(Integer32):
    """Custom type ifvceAnalogLinkDwnBusy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 3),
          ("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfvceAnalogLinkDwnBusy_Type.__name__ = "Integer32"
_IfvceAnalogLinkDwnBusy_Object = MibTableColumn
ifvceAnalogLinkDwnBusy = _IfvceAnalogLinkDwnBusy_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 38),
    _IfvceAnalogLinkDwnBusy_Type()
)
ifvceAnalogLinkDwnBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceAnalogLinkDwnBusy.setStatus("mandatory")
_IfvceSpeedDialNum_Type = DisplayString
_IfvceSpeedDialNum_Object = MibTableColumn
ifvceSpeedDialNum = _IfvceSpeedDialNum_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 39),
    _IfvceSpeedDialNum_Type()
)
ifvceSpeedDialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceSpeedDialNum.setStatus("mandatory")


class _IfvceR2ExtendedDigitSrc_Type(Integer32):
    """Custom type ifvceR2ExtendedDigitSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("map", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("user", 2))
    )


_IfvceR2ExtendedDigitSrc_Type.__name__ = "Integer32"
_IfvceR2ExtendedDigitSrc_Object = MibTableColumn
ifvceR2ExtendedDigitSrc = _IfvceR2ExtendedDigitSrc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 40),
    _IfvceR2ExtendedDigitSrc_Type()
)
ifvceR2ExtendedDigitSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceR2ExtendedDigitSrc.setStatus("mandatory")


class _IfvceR2Group2Digit_Type(Integer32):
    """Custom type ifvceR2Group2Digit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_IfvceR2Group2Digit_Type.__name__ = "Integer32"
_IfvceR2Group2Digit_Object = MibTableColumn
ifvceR2Group2Digit = _IfvceR2Group2Digit_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 41),
    _IfvceR2Group2Digit_Type()
)
ifvceR2Group2Digit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceR2Group2Digit.setStatus("mandatory")


class _IfvceR2CompleteDigit_Type(Integer32):
    """Custom type ifvceR2CompleteDigit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_IfvceR2CompleteDigit_Type.__name__ = "Integer32"
_IfvceR2CompleteDigit_Object = MibTableColumn
ifvceR2CompleteDigit = _IfvceR2CompleteDigit_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 42),
    _IfvceR2CompleteDigit_Type()
)
ifvceR2CompleteDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceR2CompleteDigit.setStatus("mandatory")


class _IfvceR2BusyDigit_Type(Integer32):
    """Custom type ifvceR2BusyDigit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_IfvceR2BusyDigit_Type.__name__ = "Integer32"
_IfvceR2BusyDigit_Object = MibTableColumn
ifvceR2BusyDigit = _IfvceR2BusyDigit_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 43),
    _IfvceR2BusyDigit_Type()
)
ifvceR2BusyDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceR2BusyDigit.setStatus("mandatory")


class _IfvceMaxFaxModemRate_Type(Integer32):
    """Custom type ifvceMaxFaxModemRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 254),
          ("not-available", 255),
          ("rate-12000", 2),
          ("rate-14400", 1),
          ("rate-4800", 5),
          ("rate-7200", 4),
          ("rate-9600", 3))
    )


_IfvceMaxFaxModemRate_Type.__name__ = "Integer32"
_IfvceMaxFaxModemRate_Object = MibTableColumn
ifvceMaxFaxModemRate = _IfvceMaxFaxModemRate_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 44),
    _IfvceMaxFaxModemRate_Type()
)
ifvceMaxFaxModemRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceMaxFaxModemRate.setStatus("mandatory")


class _IfvceRate8kx3_Type(Integer32):
    """Custom type ifvceRate8kx3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfvceRate8kx3_Type.__name__ = "Integer32"
_IfvceRate8kx3_Object = MibTableColumn
ifvceRate8kx3 = _IfvceRate8kx3_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 45),
    _IfvceRate8kx3_Type()
)
ifvceRate8kx3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceRate8kx3.setStatus("mandatory")


class _IfvceRate6kx1_Type(Integer32):
    """Custom type ifvceRate6kx1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfvceRate6kx1_Type.__name__ = "Integer32"
_IfvceRate6kx1_Object = MibTableColumn
ifvceRate6kx1 = _IfvceRate6kx1_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 46),
    _IfvceRate6kx1_Type()
)
ifvceRate6kx1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceRate6kx1.setStatus("mandatory")


class _IfvceRate6kx2_Type(Integer32):
    """Custom type ifvceRate6kx2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfvceRate6kx2_Type.__name__ = "Integer32"
_IfvceRate6kx2_Object = MibTableColumn
ifvceRate6kx2 = _IfvceRate6kx2_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 47),
    _IfvceRate6kx2_Type()
)
ifvceRate6kx2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceRate6kx2.setStatus("mandatory")


class _IfvceRate6kx3_Type(Integer32):
    """Custom type ifvceRate6kx3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfvceRate6kx3_Type.__name__ = "Integer32"
_IfvceRate6kx3_Object = MibTableColumn
ifvceRate6kx3 = _IfvceRate6kx3_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 48),
    _IfvceRate6kx3_Type()
)
ifvceRate6kx3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceRate6kx3.setStatus("mandatory")


class _IfvceRate4k8x1_Type(Integer32):
    """Custom type ifvceRate4k8x1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfvceRate4k8x1_Type.__name__ = "Integer32"
_IfvceRate4k8x1_Object = MibTableColumn
ifvceRate4k8x1 = _IfvceRate4k8x1_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 49),
    _IfvceRate4k8x1_Type()
)
ifvceRate4k8x1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceRate4k8x1.setStatus("mandatory")


class _IfvceRate4k8x2_Type(Integer32):
    """Custom type ifvceRate4k8x2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfvceRate4k8x2_Type.__name__ = "Integer32"
_IfvceRate4k8x2_Object = MibTableColumn
ifvceRate4k8x2 = _IfvceRate4k8x2_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 50),
    _IfvceRate4k8x2_Type()
)
ifvceRate4k8x2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceRate4k8x2.setStatus("mandatory")


class _IfvceDTalkThreshold_Type(Integer32):
    """Custom type ifvceDTalkThreshold based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("db-1", 19),
          ("db-10", 10),
          ("db-11", 9),
          ("db-12", 8),
          ("db-2", 18),
          ("db-3", 17),
          ("db-4", 16),
          ("db-5", 15),
          ("db-6", 14),
          ("db-7", 13),
          ("db-8", 12),
          ("db-9", 11),
          ("db0", 20),
          ("db1", 21),
          ("db10", 5),
          ("db11", 6),
          ("db12", 7),
          ("db2", 22),
          ("db3", 23),
          ("db4", 24),
          ("db5", 25),
          ("db6", 1),
          ("db7", 2),
          ("db8", 3),
          ("db9", 4),
          ("disabled", 26),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_IfvceDTalkThreshold_Type.__name__ = "Integer32"
_IfvceDTalkThreshold_Object = MibTableColumn
ifvceDTalkThreshold = _IfvceDTalkThreshold_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 51),
    _IfvceDTalkThreshold_Type()
)
ifvceDTalkThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceDTalkThreshold.setStatus("mandatory")


class _IfvceToneEnergyDetec_Type(Integer32):
    """Custom type ifvceToneEnergyDetec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 1))
    )


_IfvceToneEnergyDetec_Type.__name__ = "Integer32"
_IfvceToneEnergyDetec_Object = MibTableColumn
ifvceToneEnergyDetec = _IfvceToneEnergyDetec_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 52),
    _IfvceToneEnergyDetec_Type()
)
ifvceToneEnergyDetec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceToneEnergyDetec.setStatus("mandatory")


class _IfvceExtendedDigitSrc_Type(Integer32):
    """Custom type ifvceExtendedDigitSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("map", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("user", 2))
    )


_IfvceExtendedDigitSrc_Type.__name__ = "Integer32"
_IfvceExtendedDigitSrc_Object = MibTableColumn
ifvceExtendedDigitSrc = _IfvceExtendedDigitSrc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 53),
    _IfvceExtendedDigitSrc_Type()
)
ifvceExtendedDigitSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceExtendedDigitSrc.setStatus("mandatory")


class _IfvceDtmfOnTime_Type(Integer32):
    """Custom type ifvceDtmfOnTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 50),
    )


_IfvceDtmfOnTime_Type.__name__ = "Integer32"
_IfvceDtmfOnTime_Object = MibTableColumn
ifvceDtmfOnTime = _IfvceDtmfOnTime_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 54),
    _IfvceDtmfOnTime_Type()
)
ifvceDtmfOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceDtmfOnTime.setStatus("mandatory")


class _IfvceEnableDtmfOnTime_Type(Integer32):
    """Custom type ifvceEnableDtmfOnTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("not-applicable", 254),
          ("not-available", 255),
          ("yes", 2))
    )


_IfvceEnableDtmfOnTime_Type.__name__ = "Integer32"
_IfvceEnableDtmfOnTime_Object = MibTableColumn
ifvceEnableDtmfOnTime = _IfvceEnableDtmfOnTime_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 18, 2, 1, 55),
    _IfvceEnableDtmfOnTime_Type()
)
ifvceEnableDtmfOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifvceEnableDtmfOnTime.setStatus("mandatory")
_Stat_ObjectIdentity = ObjectIdentity
stat = _Stat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20)
)
_StatAlarmTable_Object = MibTable
statAlarmTable = _StatAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 1)
)
if mibBuilder.loadTexts:
    statAlarmTable.setStatus("mandatory")
_StatAlarmEntry_Object = MibTableRow
statAlarmEntry = _StatAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 1, 1)
)
statAlarmEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "statAlarmIndex"),
)
if mibBuilder.loadTexts:
    statAlarmEntry.setStatus("mandatory")
_StatAlarmIndex_Type = Integer32
_StatAlarmIndex_Object = MibTableColumn
statAlarmIndex = _StatAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 1, 1, 1),
    _StatAlarmIndex_Type()
)
statAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statAlarmIndex.setStatus("mandatory")
_StatAlarmDesc_Type = DisplayString
_StatAlarmDesc_Object = MibTableColumn
statAlarmDesc = _StatAlarmDesc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 1, 1, 2),
    _StatAlarmDesc_Type()
)
statAlarmDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statAlarmDesc.setStatus("mandatory")
_StatAlarmDate_Type = DisplayString
_StatAlarmDate_Object = MibTableColumn
statAlarmDate = _StatAlarmDate_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 1, 1, 3),
    _StatAlarmDate_Type()
)
statAlarmDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statAlarmDate.setStatus("mandatory")
_StatAlarmTime_Type = DisplayString
_StatAlarmTime_Object = MibTableColumn
statAlarmTime = _StatAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 1, 1, 4),
    _StatAlarmTime_Type()
)
statAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statAlarmTime.setStatus("mandatory")
_StatAlarmModule_Type = Integer32
_StatAlarmModule_Object = MibTableColumn
statAlarmModule = _StatAlarmModule_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 1, 1, 5),
    _StatAlarmModule_Type()
)
statAlarmModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statAlarmModule.setStatus("mandatory")
_StatAlarmAlarm_Type = Integer32
_StatAlarmAlarm_Object = MibTableColumn
statAlarmAlarm = _StatAlarmAlarm_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 1, 1, 6),
    _StatAlarmAlarm_Type()
)
statAlarmAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statAlarmAlarm.setStatus("mandatory")
_StatAlarmArg_Type = Integer32
_StatAlarmArg_Object = MibTableColumn
statAlarmArg = _StatAlarmArg_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 1, 1, 7),
    _StatAlarmArg_Type()
)
statAlarmArg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statAlarmArg.setStatus("mandatory")
_StatIfwanTable_Object = MibTable
statIfwanTable = _StatIfwanTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2)
)
if mibBuilder.loadTexts:
    statIfwanTable.setStatus("mandatory")
_StatIfwanEntry_Object = MibTableRow
statIfwanEntry = _StatIfwanEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1)
)
statIfwanEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "statIfwanIndex"),
)
if mibBuilder.loadTexts:
    statIfwanEntry.setStatus("mandatory")
_StatIfwanIndex_Type = Integer32
_StatIfwanIndex_Object = MibTableColumn
statIfwanIndex = _StatIfwanIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 1),
    _StatIfwanIndex_Type()
)
statIfwanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanIndex.setStatus("mandatory")
_StatIfwanDesc_Type = DisplayString
_StatIfwanDesc_Object = MibTableColumn
statIfwanDesc = _StatIfwanDesc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 2),
    _StatIfwanDesc_Type()
)
statIfwanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanDesc.setStatus("mandatory")


class _StatIfwanProtocol_Type(Integer32):
    """Custom type statIfwanProtocol based on Integer32"""
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
              10,
              11,
              12,
              17,
              18,
              19,
              24,
              27,
              28,
              29,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bsc", 8),
          ("console", 12),
          ("cop", 9),
          ("ddcmp", 5),
          ("e1-trsp", 24),
          ("fr-net", 17),
          ("fr-user", 18),
          ("g703", 28),
          ("hdlc", 4),
          ("isdn-bri", 27),
          ("not-applicable", 254),
          ("not-available", 255),
          ("off", 1),
          ("p-sdlc", 2),
          ("passthru", 11),
          ("ppp", 19),
          ("pvcr", 10),
          ("r-async", 7),
          ("s-sdlc", 3),
          ("t-async", 6),
          ("x25", 29))
    )


_StatIfwanProtocol_Type.__name__ = "Integer32"
_StatIfwanProtocol_Object = MibTableColumn
statIfwanProtocol = _StatIfwanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 3),
    _StatIfwanProtocol_Type()
)
statIfwanProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanProtocol.setStatus("mandatory")
_StatIfwanInterface_Type = DisplayString
_StatIfwanInterface_Object = MibTableColumn
statIfwanInterface = _StatIfwanInterface_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 4),
    _StatIfwanInterface_Type()
)
statIfwanInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanInterface.setStatus("mandatory")
_StatIfwanModemSignal_Type = DisplayString
_StatIfwanModemSignal_Object = MibTableColumn
statIfwanModemSignal = _StatIfwanModemSignal_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 5),
    _StatIfwanModemSignal_Type()
)
statIfwanModemSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanModemSignal.setStatus("mandatory")
_StatIfwanSpeed_Type = Integer32
_StatIfwanSpeed_Object = MibTableColumn
statIfwanSpeed = _StatIfwanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 6),
    _StatIfwanSpeed_Type()
)
statIfwanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanSpeed.setStatus("mandatory")
_StatIfwanState_Type = DisplayString
_StatIfwanState_Object = MibTableColumn
statIfwanState = _StatIfwanState_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 7),
    _StatIfwanState_Type()
)
statIfwanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanState.setStatus("mandatory")
_StatIfwanMeanTx_Type = Gauge32
_StatIfwanMeanTx_Object = MibTableColumn
statIfwanMeanTx = _StatIfwanMeanTx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 8),
    _StatIfwanMeanTx_Type()
)
statIfwanMeanTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanMeanTx.setStatus("mandatory")
_StatIfwanMeanRx_Type = Gauge32
_StatIfwanMeanRx_Object = MibTableColumn
statIfwanMeanRx = _StatIfwanMeanRx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 9),
    _StatIfwanMeanRx_Type()
)
statIfwanMeanRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanMeanRx.setStatus("mandatory")
_StatIfwanPeakTx_Type = Gauge32
_StatIfwanPeakTx_Object = MibTableColumn
statIfwanPeakTx = _StatIfwanPeakTx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 10),
    _StatIfwanPeakTx_Type()
)
statIfwanPeakTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanPeakTx.setStatus("mandatory")
_StatIfwanPeakRx_Type = Gauge32
_StatIfwanPeakRx_Object = MibTableColumn
statIfwanPeakRx = _StatIfwanPeakRx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 11),
    _StatIfwanPeakRx_Type()
)
statIfwanPeakRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanPeakRx.setStatus("mandatory")
_StatIfwanBadFrames_Type = Counter32
_StatIfwanBadFrames_Object = MibTableColumn
statIfwanBadFrames = _StatIfwanBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 12),
    _StatIfwanBadFrames_Type()
)
statIfwanBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanBadFrames.setStatus("mandatory")
_StatIfwanBadFlags_Type = DisplayString
_StatIfwanBadFlags_Object = MibTableColumn
statIfwanBadFlags = _StatIfwanBadFlags_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 13),
    _StatIfwanBadFlags_Type()
)
statIfwanBadFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanBadFlags.setStatus("mandatory")
_StatIfwanUnderruns_Type = Counter32
_StatIfwanUnderruns_Object = MibTableColumn
statIfwanUnderruns = _StatIfwanUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 14),
    _StatIfwanUnderruns_Type()
)
statIfwanUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanUnderruns.setStatus("mandatory")
_StatIfwanRetries_Type = Counter32
_StatIfwanRetries_Object = MibTableColumn
statIfwanRetries = _StatIfwanRetries_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 15),
    _StatIfwanRetries_Type()
)
statIfwanRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanRetries.setStatus("mandatory")
_StatIfwanRestart_Type = Counter32
_StatIfwanRestart_Object = MibTableColumn
statIfwanRestart = _StatIfwanRestart_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 16),
    _StatIfwanRestart_Type()
)
statIfwanRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanRestart.setStatus("mandatory")
_StatIfwanFramesTx_Type = Counter32
_StatIfwanFramesTx_Object = MibTableColumn
statIfwanFramesTx = _StatIfwanFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 17),
    _StatIfwanFramesTx_Type()
)
statIfwanFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanFramesTx.setStatus("mandatory")
_StatIfwanFramesRx_Type = Counter32
_StatIfwanFramesRx_Object = MibTableColumn
statIfwanFramesRx = _StatIfwanFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 18),
    _StatIfwanFramesRx_Type()
)
statIfwanFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanFramesRx.setStatus("mandatory")
_StatIfwanOctetsTx_Type = Counter32
_StatIfwanOctetsTx_Object = MibTableColumn
statIfwanOctetsTx = _StatIfwanOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 19),
    _StatIfwanOctetsTx_Type()
)
statIfwanOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanOctetsTx.setStatus("mandatory")
_StatIfwanOctetsRx_Type = Counter32
_StatIfwanOctetsRx_Object = MibTableColumn
statIfwanOctetsRx = _StatIfwanOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 20),
    _StatIfwanOctetsRx_Type()
)
statIfwanOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanOctetsRx.setStatus("mandatory")
_StatIfwanOvrFrames_Type = Counter32
_StatIfwanOvrFrames_Object = MibTableColumn
statIfwanOvrFrames = _StatIfwanOvrFrames_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 21),
    _StatIfwanOvrFrames_Type()
)
statIfwanOvrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanOvrFrames.setStatus("mandatory")
_StatIfwanBadOctets_Type = Counter32
_StatIfwanBadOctets_Object = MibTableColumn
statIfwanBadOctets = _StatIfwanBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 22),
    _StatIfwanBadOctets_Type()
)
statIfwanBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanBadOctets.setStatus("mandatory")
_StatIfwanOvrOctets_Type = Counter32
_StatIfwanOvrOctets_Object = MibTableColumn
statIfwanOvrOctets = _StatIfwanOvrOctets_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 23),
    _StatIfwanOvrOctets_Type()
)
statIfwanOvrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanOvrOctets.setStatus("mandatory")
_StatIfwanT1E1ESS_Type = Counter32
_StatIfwanT1E1ESS_Object = MibTableColumn
statIfwanT1E1ESS = _StatIfwanT1E1ESS_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 24),
    _StatIfwanT1E1ESS_Type()
)
statIfwanT1E1ESS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanT1E1ESS.setStatus("mandatory")
_StatIfwanT1E1SES_Type = Counter32
_StatIfwanT1E1SES_Object = MibTableColumn
statIfwanT1E1SES = _StatIfwanT1E1SES_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 25),
    _StatIfwanT1E1SES_Type()
)
statIfwanT1E1SES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanT1E1SES.setStatus("mandatory")
_StatIfwanT1E1SEF_Type = Counter32
_StatIfwanT1E1SEF_Object = MibTableColumn
statIfwanT1E1SEF = _StatIfwanT1E1SEF_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 26),
    _StatIfwanT1E1SEF_Type()
)
statIfwanT1E1SEF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanT1E1SEF.setStatus("mandatory")
_StatIfwanT1E1UAS_Type = Counter32
_StatIfwanT1E1UAS_Object = MibTableColumn
statIfwanT1E1UAS = _StatIfwanT1E1UAS_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 27),
    _StatIfwanT1E1UAS_Type()
)
statIfwanT1E1UAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanT1E1UAS.setStatus("mandatory")
_StatIfwanT1E1CSS_Type = Counter32
_StatIfwanT1E1CSS_Object = MibTableColumn
statIfwanT1E1CSS = _StatIfwanT1E1CSS_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 28),
    _StatIfwanT1E1CSS_Type()
)
statIfwanT1E1CSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanT1E1CSS.setStatus("mandatory")
_StatIfwanT1E1PCV_Type = Counter32
_StatIfwanT1E1PCV_Object = MibTableColumn
statIfwanT1E1PCV = _StatIfwanT1E1PCV_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 29),
    _StatIfwanT1E1PCV_Type()
)
statIfwanT1E1PCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanT1E1PCV.setStatus("mandatory")
_StatIfwanT1E1LES_Type = Counter32
_StatIfwanT1E1LES_Object = MibTableColumn
statIfwanT1E1LES = _StatIfwanT1E1LES_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 30),
    _StatIfwanT1E1LES_Type()
)
statIfwanT1E1LES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanT1E1LES.setStatus("mandatory")
_StatIfwanT1E1BES_Type = Counter32
_StatIfwanT1E1BES_Object = MibTableColumn
statIfwanT1E1BES = _StatIfwanT1E1BES_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 31),
    _StatIfwanT1E1BES_Type()
)
statIfwanT1E1BES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanT1E1BES.setStatus("mandatory")
_StatIfwanT1E1DM_Type = Counter32
_StatIfwanT1E1DM_Object = MibTableColumn
statIfwanT1E1DM = _StatIfwanT1E1DM_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 32),
    _StatIfwanT1E1DM_Type()
)
statIfwanT1E1DM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanT1E1DM.setStatus("mandatory")
_StatIfwanT1E1LCV_Type = Counter32
_StatIfwanT1E1LCV_Object = MibTableColumn
statIfwanT1E1LCV = _StatIfwanT1E1LCV_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 33),
    _StatIfwanT1E1LCV_Type()
)
statIfwanT1E1LCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanT1E1LCV.setStatus("mandatory")
_StatIfwanCompErrs_Type = Counter32
_StatIfwanCompErrs_Object = MibTableColumn
statIfwanCompErrs = _StatIfwanCompErrs_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 34),
    _StatIfwanCompErrs_Type()
)
statIfwanCompErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanCompErrs.setStatus("mandatory")
_StatIfwanChOverflows_Type = Counter32
_StatIfwanChOverflows_Object = MibTableColumn
statIfwanChOverflows = _StatIfwanChOverflows_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 35),
    _StatIfwanChOverflows_Type()
)
statIfwanChOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanChOverflows.setStatus("mandatory")
_StatIfwanChAborts_Type = Counter32
_StatIfwanChAborts_Object = MibTableColumn
statIfwanChAborts = _StatIfwanChAborts_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 36),
    _StatIfwanChAborts_Type()
)
statIfwanChAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanChAborts.setStatus("mandatory")
_StatIfwanChSeqErrs_Type = Counter32
_StatIfwanChSeqErrs_Object = MibTableColumn
statIfwanChSeqErrs = _StatIfwanChSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 37),
    _StatIfwanChSeqErrs_Type()
)
statIfwanChSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanChSeqErrs.setStatus("mandatory")
_StatIfwanDropInsert_Type = DisplayString
_StatIfwanDropInsert_Object = MibTableColumn
statIfwanDropInsert = _StatIfwanDropInsert_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 38),
    _StatIfwanDropInsert_Type()
)
statIfwanDropInsert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanDropInsert.setStatus("mandatory")
_StatIfwanTrspState_Type = DisplayString
_StatIfwanTrspState_Object = MibTableColumn
statIfwanTrspState = _StatIfwanTrspState_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 39),
    _StatIfwanTrspState_Type()
)
statIfwanTrspState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanTrspState.setStatus("mandatory")
_StatIfwanTrspLastError_Type = DisplayString
_StatIfwanTrspLastError_Object = MibTableColumn
statIfwanTrspLastError = _StatIfwanTrspLastError_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 40),
    _StatIfwanTrspLastError_Type()
)
statIfwanTrspLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanTrspLastError.setStatus("mandatory")
_StatIfwanQ922State_Type = DisplayString
_StatIfwanQ922State_Object = MibTableColumn
statIfwanQ922State = _StatIfwanQ922State_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 2, 1, 41),
    _StatIfwanQ922State_Type()
)
statIfwanQ922State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfwanQ922State.setStatus("mandatory")
_StatIflanTable_Object = MibTable
statIflanTable = _StatIflanTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3)
)
if mibBuilder.loadTexts:
    statIflanTable.setStatus("mandatory")
_StatIflanEntry_Object = MibTableRow
statIflanEntry = _StatIflanEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1)
)
statIflanEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "statIflanIndex"),
)
if mibBuilder.loadTexts:
    statIflanEntry.setStatus("mandatory")
_StatIflanIndex_Type = Integer32
_StatIflanIndex_Object = MibTableColumn
statIflanIndex = _StatIflanIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 1),
    _StatIflanIndex_Type()
)
statIflanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanIndex.setStatus("mandatory")


class _StatIflanProtocol_Type(Integer32):
    """Custom type statIflanProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-802p3", 15),
          ("ethernet-auto", 14),
          ("ethernet-v2", 16),
          ("off", 1),
          ("token-ring", 13))
    )


_StatIflanProtocol_Type.__name__ = "Integer32"
_StatIflanProtocol_Object = MibTableColumn
statIflanProtocol = _StatIflanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 2),
    _StatIflanProtocol_Type()
)
statIflanProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanProtocol.setStatus("mandatory")


class _StatIflanSpeed_Type(Integer32):
    """Custom type statIflanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eth-10-Mbps", 3),
          ("tr-16-Mbps", 2),
          ("tr-4-Mbps", 1))
    )


_StatIflanSpeed_Type.__name__ = "Integer32"
_StatIflanSpeed_Object = MibTableColumn
statIflanSpeed = _StatIflanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 3),
    _StatIflanSpeed_Type()
)
statIflanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanSpeed.setStatus("mandatory")
_StatIflanConnectionStatus_Type = DisplayString
_StatIflanConnectionStatus_Object = MibTableColumn
statIflanConnectionStatus = _StatIflanConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 4),
    _StatIflanConnectionStatus_Type()
)
statIflanConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanConnectionStatus.setStatus("mandatory")
_StatIflanOperatingMode_Type = DisplayString
_StatIflanOperatingMode_Object = MibTableColumn
statIflanOperatingMode = _StatIflanOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 5),
    _StatIflanOperatingMode_Type()
)
statIflanOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanOperatingMode.setStatus("mandatory")
_StatIflanEth_Interface_Type = DisplayString
_StatIflanEth_Interface_Object = MibScalar
statIflanEth_Interface = _StatIflanEth_Interface_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 6),
    _StatIflanEth_Interface_Type()
)
statIflanEth_Interface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanEth_Interface.setStatus("mandatory")
_StatIflanMeanTx_kbps_Type = Gauge32
_StatIflanMeanTx_kbps_Object = MibScalar
statIflanMeanTx_kbps = _StatIflanMeanTx_kbps_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 7),
    _StatIflanMeanTx_kbps_Type()
)
statIflanMeanTx_kbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanMeanTx_kbps.setStatus("mandatory")
_StatIflanMeanRx_kbps_Type = Gauge32
_StatIflanMeanRx_kbps_Object = MibScalar
statIflanMeanRx_kbps = _StatIflanMeanRx_kbps_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 8),
    _StatIflanMeanRx_kbps_Type()
)
statIflanMeanRx_kbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanMeanRx_kbps.setStatus("mandatory")
_StatIflanPeakTx_kbps_Type = Gauge32
_StatIflanPeakTx_kbps_Object = MibScalar
statIflanPeakTx_kbps = _StatIflanPeakTx_kbps_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 9),
    _StatIflanPeakTx_kbps_Type()
)
statIflanPeakTx_kbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanPeakTx_kbps.setStatus("mandatory")
_StatIflanPeakRx_kbps_Type = Gauge32
_StatIflanPeakRx_kbps_Object = MibScalar
statIflanPeakRx_kbps = _StatIflanPeakRx_kbps_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 10),
    _StatIflanPeakRx_kbps_Type()
)
statIflanPeakRx_kbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanPeakRx_kbps.setStatus("mandatory")
_StatIflanRetries_Type = Counter32
_StatIflanRetries_Object = MibTableColumn
statIflanRetries = _StatIflanRetries_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 11),
    _StatIflanRetries_Type()
)
statIflanRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanRetries.setStatus("mandatory")
_StatIflanBadFrames_Type = Counter32
_StatIflanBadFrames_Object = MibTableColumn
statIflanBadFrames = _StatIflanBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 12),
    _StatIflanBadFrames_Type()
)
statIflanBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanBadFrames.setStatus("mandatory")
_StatIflanBadFlags_Type = DisplayString
_StatIflanBadFlags_Object = MibTableColumn
statIflanBadFlags = _StatIflanBadFlags_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 13),
    _StatIflanBadFlags_Type()
)
statIflanBadFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanBadFlags.setStatus("mandatory")
_StatIflanTr_ReceiveCongestion_Type = Counter32
_StatIflanTr_ReceiveCongestion_Object = MibScalar
statIflanTr_ReceiveCongestion = _StatIflanTr_ReceiveCongestion_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 14),
    _StatIflanTr_ReceiveCongestion_Type()
)
statIflanTr_ReceiveCongestion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanTr_ReceiveCongestion.setStatus("mandatory")
_StatIflanEth_OneCollision_Type = Counter32
_StatIflanEth_OneCollision_Object = MibScalar
statIflanEth_OneCollision = _StatIflanEth_OneCollision_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 15),
    _StatIflanEth_OneCollision_Type()
)
statIflanEth_OneCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanEth_OneCollision.setStatus("mandatory")
_StatIflanEth_TwoCollisions_Type = Counter32
_StatIflanEth_TwoCollisions_Object = MibScalar
statIflanEth_TwoCollisions = _StatIflanEth_TwoCollisions_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 16),
    _StatIflanEth_TwoCollisions_Type()
)
statIflanEth_TwoCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanEth_TwoCollisions.setStatus("mandatory")
_StatIflanEth_ThreeAndMoreCol_Type = Counter32
_StatIflanEth_ThreeAndMoreCol_Object = MibScalar
statIflanEth_ThreeAndMoreCol = _StatIflanEth_ThreeAndMoreCol_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 17),
    _StatIflanEth_ThreeAndMoreCol_Type()
)
statIflanEth_ThreeAndMoreCol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanEth_ThreeAndMoreCol.setStatus("mandatory")
_StatIflanEth_DeferredTrans_Type = Counter32
_StatIflanEth_DeferredTrans_Object = MibScalar
statIflanEth_DeferredTrans = _StatIflanEth_DeferredTrans_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 18),
    _StatIflanEth_DeferredTrans_Type()
)
statIflanEth_DeferredTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanEth_DeferredTrans.setStatus("mandatory")
_StatIflanEth_ExcessiveCollision_Type = Counter32
_StatIflanEth_ExcessiveCollision_Object = MibScalar
statIflanEth_ExcessiveCollision = _StatIflanEth_ExcessiveCollision_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 19),
    _StatIflanEth_ExcessiveCollision_Type()
)
statIflanEth_ExcessiveCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanEth_ExcessiveCollision.setStatus("mandatory")
_StatIflanEth_LateCollision_Type = Counter32
_StatIflanEth_LateCollision_Object = MibScalar
statIflanEth_LateCollision = _StatIflanEth_LateCollision_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 20),
    _StatIflanEth_LateCollision_Type()
)
statIflanEth_LateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanEth_LateCollision.setStatus("mandatory")
_StatIflanEth_FrameCheckSeq_Type = Counter32
_StatIflanEth_FrameCheckSeq_Object = MibScalar
statIflanEth_FrameCheckSeq = _StatIflanEth_FrameCheckSeq_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 21),
    _StatIflanEth_FrameCheckSeq_Type()
)
statIflanEth_FrameCheckSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanEth_FrameCheckSeq.setStatus("mandatory")
_StatIflanEth_Align_Type = Counter32
_StatIflanEth_Align_Object = MibScalar
statIflanEth_Align = _StatIflanEth_Align_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 22),
    _StatIflanEth_Align_Type()
)
statIflanEth_Align.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanEth_Align.setStatus("mandatory")
_StatIflanEth_CarrierSense_Type = Counter32
_StatIflanEth_CarrierSense_Object = MibScalar
statIflanEth_CarrierSense = _StatIflanEth_CarrierSense_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 3, 1, 23),
    _StatIflanEth_CarrierSense_Type()
)
statIflanEth_CarrierSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIflanEth_CarrierSense.setStatus("mandatory")
_StatPuTable_Object = MibTable
statPuTable = _StatPuTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 4)
)
if mibBuilder.loadTexts:
    statPuTable.setStatus("mandatory")
_StatPuEntry_Object = MibTableRow
statPuEntry = _StatPuEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 4, 1)
)
statPuEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "statPuIndex"),
)
if mibBuilder.loadTexts:
    statPuEntry.setStatus("mandatory")
_StatPuIndex_Type = Integer32
_StatPuIndex_Object = MibTableColumn
statPuIndex = _StatPuIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 4, 1, 1),
    _StatPuIndex_Type()
)
statPuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPuIndex.setStatus("mandatory")


class _StatPuMode_Type(Integer32):
    """Custom type statPuMode based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ban-link", 15),
          ("bnn-link", 16),
          ("dlsw-ban", 13),
          ("dlsw-bnn", 14),
          ("dlsw-links", 8),
          ("llc-ban", 11),
          ("llc-bnn", 12),
          ("llc-dlsw", 6),
          ("llc-links", 7),
          ("off", 1),
          ("sdlc-ban", 9),
          ("sdlc-bnn", 10),
          ("sdlc-dlsw", 4),
          ("sdlc-links", 5),
          ("sdlc-llc", 2),
          ("sdlc-sdlc", 3))
    )


_StatPuMode_Type.__name__ = "Integer32"
_StatPuMode_Object = MibTableColumn
statPuMode = _StatPuMode_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 4, 1, 2),
    _StatPuMode_Type()
)
statPuMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPuMode.setStatus("mandatory")
_StatPuConnectionStatus_Type = DisplayString
_StatPuConnectionStatus_Object = MibTableColumn
statPuConnectionStatus = _StatPuConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 4, 1, 3),
    _StatPuConnectionStatus_Type()
)
statPuConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPuConnectionStatus.setStatus("mandatory")
_StatPuCompErrs_Type = Counter32
_StatPuCompErrs_Object = MibTableColumn
statPuCompErrs = _StatPuCompErrs_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 4, 1, 4),
    _StatPuCompErrs_Type()
)
statPuCompErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPuCompErrs.setStatus("mandatory")
_StatPuChOverflows_Type = Counter32
_StatPuChOverflows_Object = MibTableColumn
statPuChOverflows = _StatPuChOverflows_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 4, 1, 5),
    _StatPuChOverflows_Type()
)
statPuChOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPuChOverflows.setStatus("mandatory")
_StatPuChAborts_Type = Counter32
_StatPuChAborts_Object = MibTableColumn
statPuChAborts = _StatPuChAborts_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 4, 1, 6),
    _StatPuChAborts_Type()
)
statPuChAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPuChAborts.setStatus("mandatory")
_StatPuChSeqErrs_Type = Counter32
_StatPuChSeqErrs_Object = MibTableColumn
statPuChSeqErrs = _StatPuChSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 4, 1, 7),
    _StatPuChSeqErrs_Type()
)
statPuChSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPuChSeqErrs.setStatus("mandatory")
_StatBridge_ObjectIdentity = ObjectIdentity
statBridge = _StatBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5)
)
_StatBridgeBridge_ObjectIdentity = ObjectIdentity
statBridgeBridge = _StatBridgeBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 1)
)
_StatBridgeBridgeAddressDiscard_Type = DisplayString
_StatBridgeBridgeAddressDiscard_Object = MibScalar
statBridgeBridgeAddressDiscard = _StatBridgeBridgeAddressDiscard_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 1, 1),
    _StatBridgeBridgeAddressDiscard_Type()
)
statBridgeBridgeAddressDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgeBridgeAddressDiscard.setStatus("mandatory")
_StatBridgeBridgeFrameDiscard_Type = DisplayString
_StatBridgeBridgeFrameDiscard_Object = MibScalar
statBridgeBridgeFrameDiscard = _StatBridgeBridgeFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 1, 2),
    _StatBridgeBridgeFrameDiscard_Type()
)
statBridgeBridgeFrameDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgeBridgeFrameDiscard.setStatus("mandatory")
_StatBridgeBridgeDesignatedRoot_Type = DisplayString
_StatBridgeBridgeDesignatedRoot_Object = MibScalar
statBridgeBridgeDesignatedRoot = _StatBridgeBridgeDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 1, 3),
    _StatBridgeBridgeDesignatedRoot_Type()
)
statBridgeBridgeDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgeBridgeDesignatedRoot.setStatus("mandatory")
_StatBridgeBridgeRootCost_Type = DisplayString
_StatBridgeBridgeRootCost_Object = MibScalar
statBridgeBridgeRootCost = _StatBridgeBridgeRootCost_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 1, 4),
    _StatBridgeBridgeRootCost_Type()
)
statBridgeBridgeRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgeBridgeRootCost.setStatus("mandatory")
_StatBridgeBridgeRootPort_Type = DisplayString
_StatBridgeBridgeRootPort_Object = MibScalar
statBridgeBridgeRootPort = _StatBridgeBridgeRootPort_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 1, 5),
    _StatBridgeBridgeRootPort_Type()
)
statBridgeBridgeRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgeBridgeRootPort.setStatus("mandatory")
_StatBridgeBridgeFrameFiltered_Type = DisplayString
_StatBridgeBridgeFrameFiltered_Object = MibScalar
statBridgeBridgeFrameFiltered = _StatBridgeBridgeFrameFiltered_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 1, 6),
    _StatBridgeBridgeFrameFiltered_Type()
)
statBridgeBridgeFrameFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgeBridgeFrameFiltered.setStatus("mandatory")
_StatBridgeBridgeFrameTimeout_Type = DisplayString
_StatBridgeBridgeFrameTimeout_Object = MibScalar
statBridgeBridgeFrameTimeout = _StatBridgeBridgeFrameTimeout_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 1, 7),
    _StatBridgeBridgeFrameTimeout_Type()
)
statBridgeBridgeFrameTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgeBridgeFrameTimeout.setStatus("mandatory")
_StatBridgePort_ObjectIdentity = ObjectIdentity
statBridgePort = _StatBridgePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2)
)
_StatBridgePortTable_Object = MibTable
statBridgePortTable = _StatBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1)
)
if mibBuilder.loadTexts:
    statBridgePortTable.setStatus("mandatory")
_StatBridgePortEntry_Object = MibTableRow
statBridgePortEntry = _StatBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1)
)
statBridgePortEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "statBridgePortIndex"),
)
if mibBuilder.loadTexts:
    statBridgePortEntry.setStatus("mandatory")
_StatBridgePortIndex_Type = Integer32
_StatBridgePortIndex_Object = MibTableColumn
statBridgePortIndex = _StatBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 1),
    _StatBridgePortIndex_Type()
)
statBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortIndex.setStatus("mandatory")
_StatBridgePortDestination_Type = DisplayString
_StatBridgePortDestination_Object = MibTableColumn
statBridgePortDestination = _StatBridgePortDestination_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 2),
    _StatBridgePortDestination_Type()
)
statBridgePortDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortDestination.setStatus("mandatory")
_StatBridgePortState_Type = DisplayString
_StatBridgePortState_Object = MibTableColumn
statBridgePortState = _StatBridgePortState_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 3),
    _StatBridgePortState_Type()
)
statBridgePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortState.setStatus("mandatory")
_StatBridgePortDesignatedRoot_Type = DisplayString
_StatBridgePortDesignatedRoot_Object = MibTableColumn
statBridgePortDesignatedRoot = _StatBridgePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 4),
    _StatBridgePortDesignatedRoot_Type()
)
statBridgePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortDesignatedRoot.setStatus("mandatory")
_StatBridgePortDesignatedCost_Type = DisplayString
_StatBridgePortDesignatedCost_Object = MibTableColumn
statBridgePortDesignatedCost = _StatBridgePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 5),
    _StatBridgePortDesignatedCost_Type()
)
statBridgePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortDesignatedCost.setStatus("mandatory")
_StatBridgePortDesignatedBridge_Type = DisplayString
_StatBridgePortDesignatedBridge_Object = MibTableColumn
statBridgePortDesignatedBridge = _StatBridgePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 6),
    _StatBridgePortDesignatedBridge_Type()
)
statBridgePortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortDesignatedBridge.setStatus("mandatory")
_StatBridgePortDesignatedPort_Type = DisplayString
_StatBridgePortDesignatedPort_Object = MibTableColumn
statBridgePortDesignatedPort = _StatBridgePortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 7),
    _StatBridgePortDesignatedPort_Type()
)
statBridgePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortDesignatedPort.setStatus("mandatory")
_StatBridgePortTrspFrameIn_Type = DisplayString
_StatBridgePortTrspFrameIn_Object = MibTableColumn
statBridgePortTrspFrameIn = _StatBridgePortTrspFrameIn_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 8),
    _StatBridgePortTrspFrameIn_Type()
)
statBridgePortTrspFrameIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortTrspFrameIn.setStatus("mandatory")
_StatBridgePortTrspFrameOut_Type = DisplayString
_StatBridgePortTrspFrameOut_Object = MibTableColumn
statBridgePortTrspFrameOut = _StatBridgePortTrspFrameOut_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 9),
    _StatBridgePortTrspFrameOut_Type()
)
statBridgePortTrspFrameOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortTrspFrameOut.setStatus("mandatory")
_StatBridgePortTr_SpecRteFrameIn_Type = DisplayString
_StatBridgePortTr_SpecRteFrameIn_Object = MibScalar
statBridgePortTr_SpecRteFrameIn = _StatBridgePortTr_SpecRteFrameIn_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 10),
    _StatBridgePortTr_SpecRteFrameIn_Type()
)
statBridgePortTr_SpecRteFrameIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortTr_SpecRteFrameIn.setStatus("mandatory")
_StatBridgePortTr_SpecRteFrameOut_Type = DisplayString
_StatBridgePortTr_SpecRteFrameOut_Object = MibScalar
statBridgePortTr_SpecRteFrameOut = _StatBridgePortTr_SpecRteFrameOut_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 11),
    _StatBridgePortTr_SpecRteFrameOut_Type()
)
statBridgePortTr_SpecRteFrameOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortTr_SpecRteFrameOut.setStatus("mandatory")
_StatBridgePortTr_AllRteFrameIn_Type = DisplayString
_StatBridgePortTr_AllRteFrameIn_Object = MibScalar
statBridgePortTr_AllRteFrameIn = _StatBridgePortTr_AllRteFrameIn_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 12),
    _StatBridgePortTr_AllRteFrameIn_Type()
)
statBridgePortTr_AllRteFrameIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortTr_AllRteFrameIn.setStatus("mandatory")
_StatBridgePortTr_AllRteFrameOut_Type = DisplayString
_StatBridgePortTr_AllRteFrameOut_Object = MibScalar
statBridgePortTr_AllRteFrameOut = _StatBridgePortTr_AllRteFrameOut_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 13),
    _StatBridgePortTr_AllRteFrameOut_Type()
)
statBridgePortTr_AllRteFrameOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortTr_AllRteFrameOut.setStatus("mandatory")
_StatBridgePortTr_SingleRteFrameIn_Type = DisplayString
_StatBridgePortTr_SingleRteFrameIn_Object = MibScalar
statBridgePortTr_SingleRteFrameIn = _StatBridgePortTr_SingleRteFrameIn_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 14),
    _StatBridgePortTr_SingleRteFrameIn_Type()
)
statBridgePortTr_SingleRteFrameIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortTr_SingleRteFrameIn.setStatus("mandatory")
_StatBridgePortTr_SingleRteFrameOut_Type = DisplayString
_StatBridgePortTr_SingleRteFrameOut_Object = MibScalar
statBridgePortTr_SingleRteFrameOut = _StatBridgePortTr_SingleRteFrameOut_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 15),
    _StatBridgePortTr_SingleRteFrameOut_Type()
)
statBridgePortTr_SingleRteFrameOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortTr_SingleRteFrameOut.setStatus("mandatory")
_StatBridgePortTr_SegmentMismatch_Type = DisplayString
_StatBridgePortTr_SegmentMismatch_Object = MibScalar
statBridgePortTr_SegmentMismatch = _StatBridgePortTr_SegmentMismatch_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 16),
    _StatBridgePortTr_SegmentMismatch_Type()
)
statBridgePortTr_SegmentMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortTr_SegmentMismatch.setStatus("mandatory")
_StatBridgePortTr_SegmentDuplicate_Type = DisplayString
_StatBridgePortTr_SegmentDuplicate_Object = MibScalar
statBridgePortTr_SegmentDuplicate = _StatBridgePortTr_SegmentDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 17),
    _StatBridgePortTr_SegmentDuplicate_Type()
)
statBridgePortTr_SegmentDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortTr_SegmentDuplicate.setStatus("mandatory")
_StatBridgePortTr_HopCntExceeded_Type = DisplayString
_StatBridgePortTr_HopCntExceeded_Object = MibScalar
statBridgePortTr_HopCntExceeded = _StatBridgePortTr_HopCntExceeded_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 18),
    _StatBridgePortTr_HopCntExceeded_Type()
)
statBridgePortTr_HopCntExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortTr_HopCntExceeded.setStatus("mandatory")
_StatBridgePortTr_FrmLngExceeded_Type = DisplayString
_StatBridgePortTr_FrmLngExceeded_Object = MibScalar
statBridgePortTr_FrmLngExceeded = _StatBridgePortTr_FrmLngExceeded_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 5, 2, 1, 1, 19),
    _StatBridgePortTr_FrmLngExceeded_Type()
)
statBridgePortTr_FrmLngExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBridgePortTr_FrmLngExceeded.setStatus("mandatory")
_StatPvcTable_Object = MibTable
statPvcTable = _StatPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6)
)
if mibBuilder.loadTexts:
    statPvcTable.setStatus("mandatory")
_StatPvcEntry_Object = MibTableRow
statPvcEntry = _StatPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1)
)
statPvcEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "statPvcIndex"),
)
if mibBuilder.loadTexts:
    statPvcEntry.setStatus("mandatory")
_StatPvcIndex_Type = Integer32
_StatPvcIndex_Object = MibTableColumn
statPvcIndex = _StatPvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 1),
    _StatPvcIndex_Type()
)
statPvcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcIndex.setStatus("mandatory")
_StatPvcProtocol_Type = DisplayString
_StatPvcProtocol_Object = MibTableColumn
statPvcProtocol = _StatPvcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 2),
    _StatPvcProtocol_Type()
)
statPvcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcProtocol.setStatus("mandatory")
_StatPvcMode_Type = DisplayString
_StatPvcMode_Object = MibTableColumn
statPvcMode = _StatPvcMode_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 3),
    _StatPvcMode_Type()
)
statPvcMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcMode.setStatus("mandatory")
_StatPvcInfoSignal_Type = DisplayString
_StatPvcInfoSignal_Object = MibTableColumn
statPvcInfoSignal = _StatPvcInfoSignal_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 4),
    _StatPvcInfoSignal_Type()
)
statPvcInfoSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcInfoSignal.setStatus("mandatory")
_StatPvcSpeed_Type = DisplayString
_StatPvcSpeed_Object = MibTableColumn
statPvcSpeed = _StatPvcSpeed_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 5),
    _StatPvcSpeed_Type()
)
statPvcSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcSpeed.setStatus("mandatory")
_StatPvcState_Type = DisplayString
_StatPvcState_Object = MibTableColumn
statPvcState = _StatPvcState_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 6),
    _StatPvcState_Type()
)
statPvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcState.setStatus("mandatory")
_StatPvcMeanTx_Type = Gauge32
_StatPvcMeanTx_Object = MibTableColumn
statPvcMeanTx = _StatPvcMeanTx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 7),
    _StatPvcMeanTx_Type()
)
statPvcMeanTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcMeanTx.setStatus("mandatory")
_StatPvcMeanRx_Type = Gauge32
_StatPvcMeanRx_Object = MibTableColumn
statPvcMeanRx = _StatPvcMeanRx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 8),
    _StatPvcMeanRx_Type()
)
statPvcMeanRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcMeanRx.setStatus("mandatory")
_StatPvcPeakTx_Type = Gauge32
_StatPvcPeakTx_Object = MibTableColumn
statPvcPeakTx = _StatPvcPeakTx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 9),
    _StatPvcPeakTx_Type()
)
statPvcPeakTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcPeakTx.setStatus("mandatory")
_StatPvcPeakRx_Type = Gauge32
_StatPvcPeakRx_Object = MibTableColumn
statPvcPeakRx = _StatPvcPeakRx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 10),
    _StatPvcPeakRx_Type()
)
statPvcPeakRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcPeakRx.setStatus("mandatory")
_StatPvcError_Type = Counter32
_StatPvcError_Object = MibTableColumn
statPvcError = _StatPvcError_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 11),
    _StatPvcError_Type()
)
statPvcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcError.setStatus("mandatory")
_StatPvcRestart_Type = Counter32
_StatPvcRestart_Object = MibTableColumn
statPvcRestart = _StatPvcRestart_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 12),
    _StatPvcRestart_Type()
)
statPvcRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcRestart.setStatus("mandatory")
_StatPvcFramesTx_Type = Counter32
_StatPvcFramesTx_Object = MibTableColumn
statPvcFramesTx = _StatPvcFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 13),
    _StatPvcFramesTx_Type()
)
statPvcFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcFramesTx.setStatus("mandatory")
_StatPvcFramesRx_Type = Counter32
_StatPvcFramesRx_Object = MibTableColumn
statPvcFramesRx = _StatPvcFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 14),
    _StatPvcFramesRx_Type()
)
statPvcFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcFramesRx.setStatus("mandatory")
_StatPvcOctetsTx_Type = Counter32
_StatPvcOctetsTx_Object = MibTableColumn
statPvcOctetsTx = _StatPvcOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 15),
    _StatPvcOctetsTx_Type()
)
statPvcOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcOctetsTx.setStatus("mandatory")
_StatPvcOctetsRx_Type = Counter32
_StatPvcOctetsRx_Object = MibTableColumn
statPvcOctetsRx = _StatPvcOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 16),
    _StatPvcOctetsRx_Type()
)
statPvcOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcOctetsRx.setStatus("mandatory")
_StatPvcBadFrames_Type = Counter32
_StatPvcBadFrames_Object = MibTableColumn
statPvcBadFrames = _StatPvcBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 17),
    _StatPvcBadFrames_Type()
)
statPvcBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcBadFrames.setStatus("mandatory")
_StatPvcOvrFrames_Type = Counter32
_StatPvcOvrFrames_Object = MibTableColumn
statPvcOvrFrames = _StatPvcOvrFrames_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 18),
    _StatPvcOvrFrames_Type()
)
statPvcOvrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcOvrFrames.setStatus("mandatory")
_StatPvcBadOctets_Type = Counter32
_StatPvcBadOctets_Object = MibTableColumn
statPvcBadOctets = _StatPvcBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 19),
    _StatPvcBadOctets_Type()
)
statPvcBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcBadOctets.setStatus("mandatory")
_StatPvcOvrOctets_Type = Counter32
_StatPvcOvrOctets_Object = MibTableColumn
statPvcOvrOctets = _StatPvcOvrOctets_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 20),
    _StatPvcOvrOctets_Type()
)
statPvcOvrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcOvrOctets.setStatus("mandatory")
_StatPvcDlci_Type = Integer32
_StatPvcDlci_Object = MibTableColumn
statPvcDlci = _StatPvcDlci_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 21),
    _StatPvcDlci_Type()
)
statPvcDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcDlci.setStatus("mandatory")
_StatPvcCompErrs_Type = Counter32
_StatPvcCompErrs_Object = MibTableColumn
statPvcCompErrs = _StatPvcCompErrs_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 28),
    _StatPvcCompErrs_Type()
)
statPvcCompErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcCompErrs.setStatus("mandatory")
_StatPvcChOverflows_Type = Counter32
_StatPvcChOverflows_Object = MibTableColumn
statPvcChOverflows = _StatPvcChOverflows_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 29),
    _StatPvcChOverflows_Type()
)
statPvcChOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcChOverflows.setStatus("mandatory")
_StatPvcChAborts_Type = Counter32
_StatPvcChAborts_Object = MibTableColumn
statPvcChAborts = _StatPvcChAborts_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 30),
    _StatPvcChAborts_Type()
)
statPvcChAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcChAborts.setStatus("mandatory")
_StatPvcChSeqErrs_Type = Counter32
_StatPvcChSeqErrs_Object = MibTableColumn
statPvcChSeqErrs = _StatPvcChSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 6, 1, 31),
    _StatPvcChSeqErrs_Type()
)
statPvcChSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcChSeqErrs.setStatus("mandatory")
_StatPvcrRouteTable_Object = MibTable
statPvcrRouteTable = _StatPvcrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 7)
)
if mibBuilder.loadTexts:
    statPvcrRouteTable.setStatus("mandatory")
_StatPvcrRouteEntry_Object = MibTableRow
statPvcrRouteEntry = _StatPvcrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 7, 1)
)
statPvcrRouteEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "statPvcrRouteName"),
    (0, "CLEARTRAC7-MIB", "statPvcrRouteNextHop"),
)
if mibBuilder.loadTexts:
    statPvcrRouteEntry.setStatus("mandatory")
_StatPvcrRouteName_Type = DisplayString
_StatPvcrRouteName_Object = MibTableColumn
statPvcrRouteName = _StatPvcrRouteName_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 7, 1, 1),
    _StatPvcrRouteName_Type()
)
statPvcrRouteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcrRouteName.setStatus("mandatory")


class _StatPvcrRouteValid_Type(Integer32):
    """Custom type statPvcrRouteValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_StatPvcrRouteValid_Type.__name__ = "Integer32"
_StatPvcrRouteValid_Object = MibTableColumn
statPvcrRouteValid = _StatPvcrRouteValid_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 7, 1, 2),
    _StatPvcrRouteValid_Type()
)
statPvcrRouteValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcrRouteValid.setStatus("mandatory")
_StatPvcrRouteMetric_Type = Gauge32
_StatPvcrRouteMetric_Object = MibTableColumn
statPvcrRouteMetric = _StatPvcrRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 7, 1, 3),
    _StatPvcrRouteMetric_Type()
)
statPvcrRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcrRouteMetric.setStatus("mandatory")
_StatPvcrRouteIntrf_Type = Integer32
_StatPvcrRouteIntrf_Object = MibTableColumn
statPvcrRouteIntrf = _StatPvcrRouteIntrf_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 7, 1, 4),
    _StatPvcrRouteIntrf_Type()
)
statPvcrRouteIntrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcrRouteIntrf.setStatus("mandatory")
_StatPvcrRouteNextHop_Type = DisplayString
_StatPvcrRouteNextHop_Object = MibTableColumn
statPvcrRouteNextHop = _StatPvcrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 7, 1, 5),
    _StatPvcrRouteNextHop_Type()
)
statPvcrRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcrRouteNextHop.setStatus("mandatory")
_StatPvcrRouteAge_Type = Integer32
_StatPvcrRouteAge_Object = MibTableColumn
statPvcrRouteAge = _StatPvcrRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 7, 1, 6),
    _StatPvcrRouteAge_Type()
)
statPvcrRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPvcrRouteAge.setStatus("mandatory")
_StatIfvceTable_Object = MibTable
statIfvceTable = _StatIfvceTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 10)
)
if mibBuilder.loadTexts:
    statIfvceTable.setStatus("mandatory")
_StatIfvceEntry_Object = MibTableRow
statIfvceEntry = _StatIfvceEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 10, 1)
)
statIfvceEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "statIfvceIndex"),
)
if mibBuilder.loadTexts:
    statIfvceEntry.setStatus("mandatory")
_StatIfvceIndex_Type = Integer32
_StatIfvceIndex_Object = MibTableColumn
statIfvceIndex = _StatIfvceIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 10, 1, 1),
    _StatIfvceIndex_Type()
)
statIfvceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfvceIndex.setStatus("mandatory")
_StatIfvceDesc_Type = DisplayString
_StatIfvceDesc_Object = MibTableColumn
statIfvceDesc = _StatIfvceDesc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 10, 1, 2),
    _StatIfvceDesc_Type()
)
statIfvceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfvceDesc.setStatus("mandatory")


class _StatIfvceState_Type(Integer32):
    """Custom type statIfvceState based on Integer32"""
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
        *(("disconnect", 5),
          ("idle", 1),
          ("inactive", 0),
          ("local", 3),
          ("online", 4),
          ("pause", 2))
    )


_StatIfvceState_Type.__name__ = "Integer32"
_StatIfvceState_Object = MibTableColumn
statIfvceState = _StatIfvceState_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 10, 1, 3),
    _StatIfvceState_Type()
)
statIfvceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfvceState.setStatus("mandatory")


class _StatIfvceProtocol_Type(Integer32):
    """Custom type statIfvceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              21,
              22,
              23,
              24,
              26,
              30)
        )
    )
    namedValues = NamedValues(
        *(("acelp-4-8-kbs", 22),
          ("acelp-8-kbs", 21),
          ("acelp-cn", 30),
          ("adpcm32k", 24),
          ("atc16k", 26),
          ("off", 1),
          ("pcm64k", 23))
    )


_StatIfvceProtocol_Type.__name__ = "Integer32"
_StatIfvceProtocol_Object = MibTableColumn
statIfvceProtocol = _StatIfvceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 10, 1, 4),
    _StatIfvceProtocol_Type()
)
statIfvceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfvceProtocol.setStatus("mandatory")


class _StatIfvceLastError_Type(Integer32):
    """Custom type statIfvceLastError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("algo-mismatch", 12),
          ("class-mismatch", 11),
          ("disconnect", 6),
          ("incompatibility", 1),
          ("new-parameters", 2),
          ("no-destination", 8),
          ("none", 0),
          ("port-closure", 7),
          ("pvc-closure", 9),
          ("rerouting", 3),
          ("state-fault", 4),
          ("too-many-calls", 10),
          ("unreachable", 5))
    )


_StatIfvceLastError_Type.__name__ = "Integer32"
_StatIfvceLastError_Object = MibTableColumn
statIfvceLastError = _StatIfvceLastError_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 10, 1, 5),
    _StatIfvceLastError_Type()
)
statIfvceLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfvceLastError.setStatus("mandatory")


class _StatIfvceFaxRate_Type(Integer32):
    """Custom type statIfvceFaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fx-2-4Kbps", 1),
          ("fx-4-8Kbps", 2),
          ("fx-7-2Kbps", 3),
          ("fx-9-6Kbps", 4),
          ("none", 0))
    )


_StatIfvceFaxRate_Type.__name__ = "Integer32"
_StatIfvceFaxRate_Object = MibTableColumn
statIfvceFaxRate = _StatIfvceFaxRate_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 10, 1, 6),
    _StatIfvceFaxRate_Type()
)
statIfvceFaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfvceFaxRate.setStatus("mandatory")


class _StatIfvceFaxMode_Type(Integer32):
    """Custom type statIfvceFaxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("in-fax", 1),
          ("none", 255),
          ("out-of-fax", 0))
    )


_StatIfvceFaxMode_Type.__name__ = "Integer32"
_StatIfvceFaxMode_Object = MibTableColumn
statIfvceFaxMode = _StatIfvceFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 10, 1, 7),
    _StatIfvceFaxMode_Type()
)
statIfvceFaxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfvceFaxMode.setStatus("mandatory")
_StatIfvceOverruns_Type = Counter32
_StatIfvceOverruns_Object = MibTableColumn
statIfvceOverruns = _StatIfvceOverruns_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 10, 1, 8),
    _StatIfvceOverruns_Type()
)
statIfvceOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfvceOverruns.setStatus("mandatory")
_StatIfvceUnderruns_Type = Counter32
_StatIfvceUnderruns_Object = MibTableColumn
statIfvceUnderruns = _StatIfvceUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 10, 1, 9),
    _StatIfvceUnderruns_Type()
)
statIfvceUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfvceUnderruns.setStatus("mandatory")
_StatIfvceDvcPortInUse_Type = DisplayString
_StatIfvceDvcPortInUse_Object = MibTableColumn
statIfvceDvcPortInUse = _StatIfvceDvcPortInUse_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 10, 1, 10),
    _StatIfvceDvcPortInUse_Type()
)
statIfvceDvcPortInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfvceDvcPortInUse.setStatus("mandatory")
_StatSystem_ObjectIdentity = ObjectIdentity
statSystem = _StatSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 20)
)
_StatSystemAlarmNumber_Type = Integer32
_StatSystemAlarmNumber_Object = MibScalar
statSystemAlarmNumber = _StatSystemAlarmNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 20, 1),
    _StatSystemAlarmNumber_Type()
)
statSystemAlarmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSystemAlarmNumber.setStatus("mandatory")
_StatSystemMeanCompRate_Type = DisplayString
_StatSystemMeanCompRate_Object = MibScalar
statSystemMeanCompRate = _StatSystemMeanCompRate_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 20, 2),
    _StatSystemMeanCompRate_Type()
)
statSystemMeanCompRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSystemMeanCompRate.setStatus("mandatory")
_StatSystemMeanDecompRate_Type = DisplayString
_StatSystemMeanDecompRate_Object = MibScalar
statSystemMeanDecompRate = _StatSystemMeanDecompRate_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 20, 3),
    _StatSystemMeanDecompRate_Type()
)
statSystemMeanDecompRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSystemMeanDecompRate.setStatus("mandatory")
_StatSystemPeakCompRate_Type = DisplayString
_StatSystemPeakCompRate_Object = MibScalar
statSystemPeakCompRate = _StatSystemPeakCompRate_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 20, 4),
    _StatSystemPeakCompRate_Type()
)
statSystemPeakCompRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSystemPeakCompRate.setStatus("mandatory")
_StatSystemPeakDecompRate_Type = DisplayString
_StatSystemPeakDecompRate_Object = MibScalar
statSystemPeakDecompRate = _StatSystemPeakDecompRate_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 20, 5),
    _StatSystemPeakDecompRate_Type()
)
statSystemPeakDecompRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSystemPeakDecompRate.setStatus("mandatory")
_StatSystemSa_Type = Gauge32
_StatSystemSa_Object = MibScalar
statSystemSa = _StatSystemSa_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 20, 6),
    _StatSystemSa_Type()
)
statSystemSa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSystemSa.setStatus("mandatory")
_StatSystemSp_Type = Gauge32
_StatSystemSp_Object = MibScalar
statSystemSp = _StatSystemSp_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 20, 7),
    _StatSystemSp_Type()
)
statSystemSp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSystemSp.setStatus("mandatory")


class _StatSystemNa_Type(OctetString):
    """Custom type statSystemNa based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_StatSystemNa_Type.__name__ = "OctetString"
_StatSystemNa_Object = MibScalar
statSystemNa = _StatSystemNa_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 20, 8),
    _StatSystemNa_Type()
)
statSystemNa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSystemNa.setStatus("mandatory")


class _StatSystemBia_Type(OctetString):
    """Custom type statSystemBia based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_StatSystemBia_Type.__name__ = "OctetString"
_StatSystemBia_Object = MibScalar
statSystemBia = _StatSystemBia_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 20, 9),
    _StatSystemBia_Type()
)
statSystemBia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSystemBia.setStatus("mandatory")


class _StatSystemTr_Nan_Type(OctetString):
    """Custom type statSystemTr_Nan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_StatSystemTr_Nan_Type.__name__ = "OctetString"
_StatSystemTr_Nan_Object = MibScalar
statSystemTr_Nan = _StatSystemTr_Nan_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 20, 10),
    _StatSystemTr_Nan_Type()
)
statSystemTr_Nan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSystemTr_Nan.setStatus("mandatory")


class _StatSystemResetCounters_Type(Integer32):
    """Custom type statSystemResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_StatSystemResetCounters_Type.__name__ = "Integer32"
_StatSystemResetCounters_Object = MibScalar
statSystemResetCounters = _StatSystemResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 20, 11),
    _StatSystemResetCounters_Type()
)
statSystemResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statSystemResetCounters.setStatus("mandatory")


class _StatSystemClearAlarms_Type(Integer32):
    """Custom type statSystemClearAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_StatSystemClearAlarms_Type.__name__ = "Integer32"
_StatSystemClearAlarms_Object = MibScalar
statSystemClearAlarms = _StatSystemClearAlarms_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 20, 12),
    _StatSystemClearAlarms_Type()
)
statSystemClearAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statSystemClearAlarms.setStatus("mandatory")


class _StatSystemClearErrorLed_Type(Integer32):
    """Custom type statSystemClearErrorLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_StatSystemClearErrorLed_Type.__name__ = "Integer32"
_StatSystemClearErrorLed_Object = MibScalar
statSystemClearErrorLed = _StatSystemClearErrorLed_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 20, 13),
    _StatSystemClearErrorLed_Type()
)
statSystemClearErrorLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statSystemClearErrorLed.setStatus("mandatory")
_StatBootp_ObjectIdentity = ObjectIdentity
statBootp = _StatBootp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 21)
)
_StatBootpNbRequestReceived_Type = Integer32
_StatBootpNbRequestReceived_Object = MibScalar
statBootpNbRequestReceived = _StatBootpNbRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 21, 1),
    _StatBootpNbRequestReceived_Type()
)
statBootpNbRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBootpNbRequestReceived.setStatus("mandatory")
_StatBootpNbRequestSend_Type = Integer32
_StatBootpNbRequestSend_Object = MibScalar
statBootpNbRequestSend = _StatBootpNbRequestSend_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 21, 2),
    _StatBootpNbRequestSend_Type()
)
statBootpNbRequestSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBootpNbRequestSend.setStatus("mandatory")
_StatBootpNbReplyReceived_Type = Integer32
_StatBootpNbReplyReceived_Object = MibScalar
statBootpNbReplyReceived = _StatBootpNbReplyReceived_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 21, 3),
    _StatBootpNbReplyReceived_Type()
)
statBootpNbReplyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBootpNbReplyReceived.setStatus("mandatory")
_StatBootpNbReplySend_Type = Integer32
_StatBootpNbReplySend_Object = MibScalar
statBootpNbReplySend = _StatBootpNbReplySend_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 21, 4),
    _StatBootpNbReplySend_Type()
)
statBootpNbReplySend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBootpNbReplySend.setStatus("mandatory")
_StatBootpReplyWithInvalidGiaddr_Type = Integer32
_StatBootpReplyWithInvalidGiaddr_Object = MibScalar
statBootpReplyWithInvalidGiaddr = _StatBootpReplyWithInvalidGiaddr_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 21, 5),
    _StatBootpReplyWithInvalidGiaddr_Type()
)
statBootpReplyWithInvalidGiaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBootpReplyWithInvalidGiaddr.setStatus("mandatory")
_StatBootpHopsLimitExceed_Type = Integer32
_StatBootpHopsLimitExceed_Object = MibScalar
statBootpHopsLimitExceed = _StatBootpHopsLimitExceed_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 21, 6),
    _StatBootpHopsLimitExceed_Type()
)
statBootpHopsLimitExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBootpHopsLimitExceed.setStatus("mandatory")
_StatBootpRequestReceivedOnPortBootpc_Type = Integer32
_StatBootpRequestReceivedOnPortBootpc_Object = MibScalar
statBootpRequestReceivedOnPortBootpc = _StatBootpRequestReceivedOnPortBootpc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 21, 7),
    _StatBootpRequestReceivedOnPortBootpc_Type()
)
statBootpRequestReceivedOnPortBootpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBootpRequestReceivedOnPortBootpc.setStatus("mandatory")
_StatBootpReplyReceivedOnPortBootpc_Type = Integer32
_StatBootpReplyReceivedOnPortBootpc_Object = MibScalar
statBootpReplyReceivedOnPortBootpc = _StatBootpReplyReceivedOnPortBootpc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 21, 8),
    _StatBootpReplyReceivedOnPortBootpc_Type()
)
statBootpReplyReceivedOnPortBootpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBootpReplyReceivedOnPortBootpc.setStatus("mandatory")
_StatBootpInvalidOpCodeField_Type = Integer32
_StatBootpInvalidOpCodeField_Object = MibScalar
statBootpInvalidOpCodeField = _StatBootpInvalidOpCodeField_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 21, 9),
    _StatBootpInvalidOpCodeField_Type()
)
statBootpInvalidOpCodeField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBootpInvalidOpCodeField.setStatus("mandatory")
_StatBootpCannotRouteFrame_Type = Integer32
_StatBootpCannotRouteFrame_Object = MibScalar
statBootpCannotRouteFrame = _StatBootpCannotRouteFrame_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 21, 10),
    _StatBootpCannotRouteFrame_Type()
)
statBootpCannotRouteFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBootpCannotRouteFrame.setStatus("mandatory")
_StatBootpFrameTooSmallToBeABootpFrame_Type = Integer32
_StatBootpFrameTooSmallToBeABootpFrame_Object = MibScalar
statBootpFrameTooSmallToBeABootpFrame = _StatBootpFrameTooSmallToBeABootpFrame_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 21, 11),
    _StatBootpFrameTooSmallToBeABootpFrame_Type()
)
statBootpFrameTooSmallToBeABootpFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBootpFrameTooSmallToBeABootpFrame.setStatus("mandatory")
_StatBootpCannotReceiveAndForwardOnTheSamePort_Type = Integer32
_StatBootpCannotReceiveAndForwardOnTheSamePort_Object = MibScalar
statBootpCannotReceiveAndForwardOnTheSamePort = _StatBootpCannotReceiveAndForwardOnTheSamePort_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 21, 12),
    _StatBootpCannotReceiveAndForwardOnTheSamePort_Type()
)
statBootpCannotReceiveAndForwardOnTheSamePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statBootpCannotReceiveAndForwardOnTheSamePort.setStatus("mandatory")
_StatGrp_ObjectIdentity = ObjectIdentity
statGrp = _StatGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 22)
)
_StatGrpNumber_Type = Integer32
_StatGrpNumber_Object = MibScalar
statGrpNumber = _StatGrpNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 22, 1),
    _StatGrpNumber_Type()
)
statGrpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statGrpNumber.setStatus("mandatory")
_StatGrpTable_Object = MibTable
statGrpTable = _StatGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 22, 2)
)
if mibBuilder.loadTexts:
    statGrpTable.setStatus("mandatory")
_StatGrpEntry_Object = MibTableRow
statGrpEntry = _StatGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 22, 2, 1)
)
statGrpEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "statGrpIndex"),
)
if mibBuilder.loadTexts:
    statGrpEntry.setStatus("mandatory")
_StatGrpIndex_Type = Integer32
_StatGrpIndex_Object = MibTableColumn
statGrpIndex = _StatGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 22, 2, 1, 1),
    _StatGrpIndex_Type()
)
statGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statGrpIndex.setStatus("mandatory")
_StatGrpDestName_Type = DisplayString
_StatGrpDestName_Object = MibTableColumn
statGrpDestName = _StatGrpDestName_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 22, 2, 1, 2),
    _StatGrpDestName_Type()
)
statGrpDestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statGrpDestName.setStatus("mandatory")
_StatGrpOutOfSeqErrs_Type = Integer32
_StatGrpOutOfSeqErrs_Object = MibTableColumn
statGrpOutOfSeqErrs = _StatGrpOutOfSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 22, 2, 1, 3),
    _StatGrpOutOfSeqErrs_Type()
)
statGrpOutOfSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statGrpOutOfSeqErrs.setStatus("mandatory")
_StatGrpSorterTimeouts_Type = Integer32
_StatGrpSorterTimeouts_Object = MibTableColumn
statGrpSorterTimeouts = _StatGrpSorterTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 22, 2, 1, 4),
    _StatGrpSorterTimeouts_Type()
)
statGrpSorterTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statGrpSorterTimeouts.setStatus("mandatory")
_StatGrpSorterOverruns_Type = Integer32
_StatGrpSorterOverruns_Object = MibTableColumn
statGrpSorterOverruns = _StatGrpSorterOverruns_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 22, 2, 1, 5),
    _StatGrpSorterOverruns_Type()
)
statGrpSorterOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statGrpSorterOverruns.setStatus("mandatory")
_StatTimep_ObjectIdentity = ObjectIdentity
statTimep = _StatTimep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 23)
)
_StatTimeNbFrameReceived_Type = Integer32
_StatTimeNbFrameReceived_Object = MibScalar
statTimeNbFrameReceived = _StatTimeNbFrameReceived_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 23, 1),
    _StatTimeNbFrameReceived_Type()
)
statTimeNbFrameReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTimeNbFrameReceived.setStatus("mandatory")
_StatTimeNbFrameSent_Type = Integer32
_StatTimeNbFrameSent_Object = MibScalar
statTimeNbFrameSent = _StatTimeNbFrameSent_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 23, 2),
    _StatTimeNbFrameSent_Type()
)
statTimeNbFrameSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTimeNbFrameSent.setStatus("mandatory")
_StatTimeNbRequestReceived_Type = Integer32
_StatTimeNbRequestReceived_Object = MibScalar
statTimeNbRequestReceived = _StatTimeNbRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 23, 3),
    _StatTimeNbRequestReceived_Type()
)
statTimeNbRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTimeNbRequestReceived.setStatus("mandatory")
_StatTimeNbReplySent_Type = Integer32
_StatTimeNbReplySent_Object = MibScalar
statTimeNbReplySent = _StatTimeNbReplySent_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 23, 4),
    _StatTimeNbReplySent_Type()
)
statTimeNbReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTimeNbReplySent.setStatus("mandatory")
_StatTimeNbRequestSent_Type = Integer32
_StatTimeNbRequestSent_Object = MibScalar
statTimeNbRequestSent = _StatTimeNbRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 23, 5),
    _StatTimeNbRequestSent_Type()
)
statTimeNbRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTimeNbRequestSent.setStatus("mandatory")
_StatTimeNbReplyReceived_Type = Integer32
_StatTimeNbReplyReceived_Object = MibScalar
statTimeNbReplyReceived = _StatTimeNbReplyReceived_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 23, 6),
    _StatTimeNbReplyReceived_Type()
)
statTimeNbReplyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTimeNbReplyReceived.setStatus("mandatory")
_StatTimeClientRetransmissions_Type = Integer32
_StatTimeClientRetransmissions_Object = MibScalar
statTimeClientRetransmissions = _StatTimeClientRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 23, 7),
    _StatTimeClientRetransmissions_Type()
)
statTimeClientRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTimeClientRetransmissions.setStatus("mandatory")
_StatTimeClientSyncFailures_Type = Integer32
_StatTimeClientSyncFailures_Object = MibScalar
statTimeClientSyncFailures = _StatTimeClientSyncFailures_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 23, 8),
    _StatTimeClientSyncFailures_Type()
)
statTimeClientSyncFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTimeClientSyncFailures.setStatus("mandatory")
_StatTimeInvalidLocalIpAddress_Type = Integer32
_StatTimeInvalidLocalIpAddress_Object = MibScalar
statTimeInvalidLocalIpAddress = _StatTimeInvalidLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 23, 9),
    _StatTimeInvalidLocalIpAddress_Type()
)
statTimeInvalidLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTimeInvalidLocalIpAddress.setStatus("mandatory")
_StatTimeInvalidPortNumbers_Type = Integer32
_StatTimeInvalidPortNumbers_Object = MibScalar
statTimeInvalidPortNumbers = _StatTimeInvalidPortNumbers_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 23, 10),
    _StatTimeInvalidPortNumbers_Type()
)
statTimeInvalidPortNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTimeInvalidPortNumbers.setStatus("mandatory")
_StatQ922counters_ObjectIdentity = ObjectIdentity
statQ922counters = _StatQ922counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 24)
)
_StatTxRetransmissions_Type = Integer32
_StatTxRetransmissions_Object = MibScalar
statTxRetransmissions = _StatTxRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 24, 1),
    _StatTxRetransmissions_Type()
)
statTxRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTxRetransmissions.setStatus("mandatory")
_StatReleaseIndications_Type = Integer32
_StatReleaseIndications_Object = MibScalar
statReleaseIndications = _StatReleaseIndications_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 24, 2),
    _StatReleaseIndications_Type()
)
statReleaseIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statReleaseIndications.setStatus("mandatory")
_StatEstablishIndications_Type = Integer32
_StatEstablishIndications_Object = MibScalar
statEstablishIndications = _StatEstablishIndications_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 24, 3),
    _StatEstablishIndications_Type()
)
statEstablishIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statEstablishIndications.setStatus("mandatory")
_StatLinkEstablished_Type = Integer32
_StatLinkEstablished_Object = MibScalar
statLinkEstablished = _StatLinkEstablished_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 24, 4),
    _StatLinkEstablished_Type()
)
statLinkEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statLinkEstablished.setStatus("mandatory")
_StatTxIframeQdiscards_Type = Integer32
_StatTxIframeQdiscards_Object = MibScalar
statTxIframeQdiscards = _StatTxIframeQdiscards_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 24, 5),
    _StatTxIframeQdiscards_Type()
)
statTxIframeQdiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTxIframeQdiscards.setStatus("mandatory")
_StatRxframes_Type = Integer32
_StatRxframes_Object = MibScalar
statRxframes = _StatRxframes_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 24, 6),
    _StatRxframes_Type()
)
statRxframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statRxframes.setStatus("mandatory")
_StatTxframes_Type = Integer32
_StatTxframes_Object = MibScalar
statTxframes = _StatTxframes_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 24, 7),
    _StatTxframes_Type()
)
statTxframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTxframes.setStatus("mandatory")
_StatRxBytes_Type = Integer32
_StatRxBytes_Object = MibScalar
statRxBytes = _StatRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 24, 8),
    _StatRxBytes_Type()
)
statRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statRxBytes.setStatus("mandatory")
_StatTxBytes_Type = Integer32
_StatTxBytes_Object = MibScalar
statTxBytes = _StatTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 24, 9),
    _StatTxBytes_Type()
)
statTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTxBytes.setStatus("mandatory")
_StatQ922errors_ObjectIdentity = ObjectIdentity
statQ922errors = _StatQ922errors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 25)
)
_StatInvalidRxSizes_Type = Integer32
_StatInvalidRxSizes_Object = MibScalar
statInvalidRxSizes = _StatInvalidRxSizes_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 25, 1),
    _StatInvalidRxSizes_Type()
)
statInvalidRxSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statInvalidRxSizes.setStatus("mandatory")
_StatMissingControlBlocks_Type = Integer32
_StatMissingControlBlocks_Object = MibScalar
statMissingControlBlocks = _StatMissingControlBlocks_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 25, 2),
    _StatMissingControlBlocks_Type()
)
statMissingControlBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statMissingControlBlocks.setStatus("mandatory")
_StatRxAcknowledgeExpiry_Type = Integer32
_StatRxAcknowledgeExpiry_Object = MibScalar
statRxAcknowledgeExpiry = _StatRxAcknowledgeExpiry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 25, 3),
    _StatRxAcknowledgeExpiry_Type()
)
statRxAcknowledgeExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statRxAcknowledgeExpiry.setStatus("mandatory")
_StatTxAcknowledgeExpiry_Type = Integer32
_StatTxAcknowledgeExpiry_Object = MibScalar
statTxAcknowledgeExpiry = _StatTxAcknowledgeExpiry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 25, 4),
    _StatTxAcknowledgeExpiry_Type()
)
statTxAcknowledgeExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTxAcknowledgeExpiry.setStatus("mandatory")
_StatQ933counters_ObjectIdentity = ObjectIdentity
statQ933counters = _StatQ933counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26)
)
_StatTxSetupMessages_Type = Integer32
_StatTxSetupMessages_Object = MibScalar
statTxSetupMessages = _StatTxSetupMessages_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 1),
    _StatTxSetupMessages_Type()
)
statTxSetupMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTxSetupMessages.setStatus("mandatory")
_StatRxSetupMessages_Type = Integer32
_StatRxSetupMessages_Object = MibScalar
statRxSetupMessages = _StatRxSetupMessages_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 2),
    _StatRxSetupMessages_Type()
)
statRxSetupMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statRxSetupMessages.setStatus("mandatory")
_StatTxCallProceedingMessages_Type = Integer32
_StatTxCallProceedingMessages_Object = MibScalar
statTxCallProceedingMessages = _StatTxCallProceedingMessages_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 3),
    _StatTxCallProceedingMessages_Type()
)
statTxCallProceedingMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTxCallProceedingMessages.setStatus("mandatory")
_StatRxCallProceedingMessages_Type = Integer32
_StatRxCallProceedingMessages_Object = MibScalar
statRxCallProceedingMessages = _StatRxCallProceedingMessages_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 4),
    _StatRxCallProceedingMessages_Type()
)
statRxCallProceedingMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statRxCallProceedingMessages.setStatus("mandatory")
_StatTxConnectMessages_Type = Integer32
_StatTxConnectMessages_Object = MibScalar
statTxConnectMessages = _StatTxConnectMessages_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 5),
    _StatTxConnectMessages_Type()
)
statTxConnectMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTxConnectMessages.setStatus("mandatory")
_StatRxConnectMessages_Type = Integer32
_StatRxConnectMessages_Object = MibScalar
statRxConnectMessages = _StatRxConnectMessages_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 6),
    _StatRxConnectMessages_Type()
)
statRxConnectMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statRxConnectMessages.setStatus("mandatory")
_StatTxReleaseMessages_Type = Integer32
_StatTxReleaseMessages_Object = MibScalar
statTxReleaseMessages = _StatTxReleaseMessages_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 7),
    _StatTxReleaseMessages_Type()
)
statTxReleaseMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTxReleaseMessages.setStatus("mandatory")
_StatRxReleaseMessages_Type = Integer32
_StatRxReleaseMessages_Object = MibScalar
statRxReleaseMessages = _StatRxReleaseMessages_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 8),
    _StatRxReleaseMessages_Type()
)
statRxReleaseMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statRxReleaseMessages.setStatus("mandatory")
_StatTxReleaseCompleteMessages_Type = Integer32
_StatTxReleaseCompleteMessages_Object = MibScalar
statTxReleaseCompleteMessages = _StatTxReleaseCompleteMessages_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 9),
    _StatTxReleaseCompleteMessages_Type()
)
statTxReleaseCompleteMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTxReleaseCompleteMessages.setStatus("mandatory")
_StatRxReleaseCompleteMessages_Type = Integer32
_StatRxReleaseCompleteMessages_Object = MibScalar
statRxReleaseCompleteMessages = _StatRxReleaseCompleteMessages_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 10),
    _StatRxReleaseCompleteMessages_Type()
)
statRxReleaseCompleteMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statRxReleaseCompleteMessages.setStatus("mandatory")
_StatTxDisconnectMessages_Type = Integer32
_StatTxDisconnectMessages_Object = MibScalar
statTxDisconnectMessages = _StatTxDisconnectMessages_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 11),
    _StatTxDisconnectMessages_Type()
)
statTxDisconnectMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTxDisconnectMessages.setStatus("mandatory")
_StatRxDisconnectMessages_Type = Integer32
_StatRxDisconnectMessages_Object = MibScalar
statRxDisconnectMessages = _StatRxDisconnectMessages_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 12),
    _StatRxDisconnectMessages_Type()
)
statRxDisconnectMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statRxDisconnectMessages.setStatus("mandatory")
_StatTxStatusMessages_Type = Integer32
_StatTxStatusMessages_Object = MibScalar
statTxStatusMessages = _StatTxStatusMessages_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 13),
    _StatTxStatusMessages_Type()
)
statTxStatusMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTxStatusMessages.setStatus("mandatory")
_StatRxStatusMessages_Type = Integer32
_StatRxStatusMessages_Object = MibScalar
statRxStatusMessages = _StatRxStatusMessages_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 14),
    _StatRxStatusMessages_Type()
)
statRxStatusMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statRxStatusMessages.setStatus("mandatory")
_StatTxStatusEnquiryMessages_Type = Integer32
_StatTxStatusEnquiryMessages_Object = MibScalar
statTxStatusEnquiryMessages = _StatTxStatusEnquiryMessages_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 15),
    _StatTxStatusEnquiryMessages_Type()
)
statTxStatusEnquiryMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTxStatusEnquiryMessages.setStatus("mandatory")
_StatRxStatusEnquiryMessages_Type = Integer32
_StatRxStatusEnquiryMessages_Object = MibScalar
statRxStatusEnquiryMessages = _StatRxStatusEnquiryMessages_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 16),
    _StatRxStatusEnquiryMessages_Type()
)
statRxStatusEnquiryMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statRxStatusEnquiryMessages.setStatus("mandatory")
_StatProtocolTimeouts_Type = Integer32
_StatProtocolTimeouts_Object = MibScalar
statProtocolTimeouts = _StatProtocolTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 26, 17),
    _StatProtocolTimeouts_Type()
)
statProtocolTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statProtocolTimeouts.setStatus("mandatory")
_StatSvcTable_Object = MibTable
statSvcTable = _StatSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27)
)
if mibBuilder.loadTexts:
    statSvcTable.setStatus("mandatory")
_StatSvcEntry_Object = MibTableRow
statSvcEntry = _StatSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1)
)
statSvcEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "statSvcIndex"),
)
if mibBuilder.loadTexts:
    statSvcEntry.setStatus("mandatory")
_StatSvcIndex_Type = Integer32
_StatSvcIndex_Object = MibTableColumn
statSvcIndex = _StatSvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 1),
    _StatSvcIndex_Type()
)
statSvcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcIndex.setStatus("mandatory")
_StatSvcProtocol_Type = DisplayString
_StatSvcProtocol_Object = MibTableColumn
statSvcProtocol = _StatSvcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 2),
    _StatSvcProtocol_Type()
)
statSvcProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcProtocol.setStatus("mandatory")
_StatSvcMode_Type = DisplayString
_StatSvcMode_Object = MibTableColumn
statSvcMode = _StatSvcMode_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 3),
    _StatSvcMode_Type()
)
statSvcMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcMode.setStatus("mandatory")
_StatSvcInfoSignal_Type = DisplayString
_StatSvcInfoSignal_Object = MibTableColumn
statSvcInfoSignal = _StatSvcInfoSignal_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 4),
    _StatSvcInfoSignal_Type()
)
statSvcInfoSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcInfoSignal.setStatus("mandatory")
_StatSvcSpeed_Type = DisplayString
_StatSvcSpeed_Object = MibTableColumn
statSvcSpeed = _StatSvcSpeed_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 5),
    _StatSvcSpeed_Type()
)
statSvcSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcSpeed.setStatus("mandatory")
_StatSvcState_Type = DisplayString
_StatSvcState_Object = MibTableColumn
statSvcState = _StatSvcState_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 6),
    _StatSvcState_Type()
)
statSvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcState.setStatus("mandatory")
_StatSvcMeanTx_Type = Gauge32
_StatSvcMeanTx_Object = MibTableColumn
statSvcMeanTx = _StatSvcMeanTx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 7),
    _StatSvcMeanTx_Type()
)
statSvcMeanTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcMeanTx.setStatus("mandatory")
_StatSvcMeanRx_Type = Gauge32
_StatSvcMeanRx_Object = MibTableColumn
statSvcMeanRx = _StatSvcMeanRx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 8),
    _StatSvcMeanRx_Type()
)
statSvcMeanRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcMeanRx.setStatus("mandatory")
_StatSvcPeakTx_Type = Gauge32
_StatSvcPeakTx_Object = MibTableColumn
statSvcPeakTx = _StatSvcPeakTx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 9),
    _StatSvcPeakTx_Type()
)
statSvcPeakTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcPeakTx.setStatus("mandatory")
_StatSvcPeakRx_Type = Gauge32
_StatSvcPeakRx_Object = MibTableColumn
statSvcPeakRx = _StatSvcPeakRx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 10),
    _StatSvcPeakRx_Type()
)
statSvcPeakRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcPeakRx.setStatus("mandatory")
_StatSvcError_Type = Counter32
_StatSvcError_Object = MibTableColumn
statSvcError = _StatSvcError_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 11),
    _StatSvcError_Type()
)
statSvcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcError.setStatus("mandatory")
_StatSvcRestart_Type = Counter32
_StatSvcRestart_Object = MibTableColumn
statSvcRestart = _StatSvcRestart_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 12),
    _StatSvcRestart_Type()
)
statSvcRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcRestart.setStatus("mandatory")
_StatSvcFramesTx_Type = Counter32
_StatSvcFramesTx_Object = MibTableColumn
statSvcFramesTx = _StatSvcFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 13),
    _StatSvcFramesTx_Type()
)
statSvcFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcFramesTx.setStatus("mandatory")
_StatSvcFramesRx_Type = Counter32
_StatSvcFramesRx_Object = MibTableColumn
statSvcFramesRx = _StatSvcFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 14),
    _StatSvcFramesRx_Type()
)
statSvcFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcFramesRx.setStatus("mandatory")
_StatSvcOctetsTx_Type = Counter32
_StatSvcOctetsTx_Object = MibTableColumn
statSvcOctetsTx = _StatSvcOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 15),
    _StatSvcOctetsTx_Type()
)
statSvcOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcOctetsTx.setStatus("mandatory")
_StatSvcOctetsRx_Type = Counter32
_StatSvcOctetsRx_Object = MibTableColumn
statSvcOctetsRx = _StatSvcOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 16),
    _StatSvcOctetsRx_Type()
)
statSvcOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcOctetsRx.setStatus("mandatory")
_StatSvcBadFrames_Type = Counter32
_StatSvcBadFrames_Object = MibTableColumn
statSvcBadFrames = _StatSvcBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 17),
    _StatSvcBadFrames_Type()
)
statSvcBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcBadFrames.setStatus("mandatory")
_StatSvcOvrFrames_Type = Counter32
_StatSvcOvrFrames_Object = MibTableColumn
statSvcOvrFrames = _StatSvcOvrFrames_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 18),
    _StatSvcOvrFrames_Type()
)
statSvcOvrFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcOvrFrames.setStatus("mandatory")
_StatSvcBadOctets_Type = Counter32
_StatSvcBadOctets_Object = MibTableColumn
statSvcBadOctets = _StatSvcBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 19),
    _StatSvcBadOctets_Type()
)
statSvcBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcBadOctets.setStatus("mandatory")
_StatSvcOvrOctets_Type = Counter32
_StatSvcOvrOctets_Object = MibTableColumn
statSvcOvrOctets = _StatSvcOvrOctets_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 20),
    _StatSvcOvrOctets_Type()
)
statSvcOvrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcOvrOctets.setStatus("mandatory")
_StatSvcDlci_Type = Integer32
_StatSvcDlci_Object = MibTableColumn
statSvcDlci = _StatSvcDlci_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 27, 1, 21),
    _StatSvcDlci_Type()
)
statSvcDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statSvcDlci.setStatus("mandatory")
_StatIfcemTable_Object = MibTable
statIfcemTable = _StatIfcemTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 28)
)
if mibBuilder.loadTexts:
    statIfcemTable.setStatus("mandatory")
_StatIfcemEntry_Object = MibTableRow
statIfcemEntry = _StatIfcemEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 28, 1)
)
statIfcemEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "statIfcemIndex"),
)
if mibBuilder.loadTexts:
    statIfcemEntry.setStatus("mandatory")
_StatIfcemIndex_Type = Integer32
_StatIfcemIndex_Object = MibTableColumn
statIfcemIndex = _StatIfcemIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 28, 1, 1),
    _StatIfcemIndex_Type()
)
statIfcemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfcemIndex.setStatus("mandatory")
_StatIfcemDesc_Type = DisplayString
_StatIfcemDesc_Object = MibTableColumn
statIfcemDesc = _StatIfcemDesc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 28, 1, 2),
    _StatIfcemDesc_Type()
)
statIfcemDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfcemDesc.setStatus("mandatory")
_StatIfcemClockState_Type = DisplayString
_StatIfcemClockState_Object = MibTableColumn
statIfcemClockState = _StatIfcemClockState_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 20, 28, 1, 3),
    _StatIfcemClockState_Type()
)
statIfcemClockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statIfcemClockState.setStatus("mandatory")
_Intf_ObjectIdentity = ObjectIdentity
intf = _Intf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 30)
)
_IntfNumber_Type = Integer32
_IntfNumber_Object = MibScalar
intfNumber = _IntfNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 30, 1),
    _IntfNumber_Type()
)
intfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfNumber.setStatus("mandatory")
_IntfTable_Object = MibTable
intfTable = _IntfTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 30, 2)
)
if mibBuilder.loadTexts:
    intfTable.setStatus("mandatory")
_IntfEntry_Object = MibTableRow
intfEntry = _IntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 30, 2, 1)
)
intfEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "intfIndex"),
)
if mibBuilder.loadTexts:
    intfEntry.setStatus("mandatory")
_IntfIndex_Type = Integer32
_IntfIndex_Object = MibTableColumn
intfIndex = _IntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 30, 2, 1, 1),
    _IntfIndex_Type()
)
intfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfIndex.setStatus("mandatory")
_IntfDesc_Type = DisplayString
_IntfDesc_Object = MibTableColumn
intfDesc = _IntfDesc_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 30, 2, 1, 2),
    _IntfDesc_Type()
)
intfDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfDesc.setStatus("mandatory")


class _IntfType_Type(Integer32):
    """Custom type intfType based on Integer32"""
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
              99,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("clock-extract-module", 9),
          ("lan-on-baseCard", 5),
          ("lan-on-slot", 6),
          ("not-applicable", 254),
          ("not-available", 255),
          ("other", 99),
          ("proxy-on-slot", 7),
          ("voice-control-on-slot", 8),
          ("voice-on-baseCard", 2),
          ("voice-on-slot", 4),
          ("wan-on-baseCard", 1),
          ("wan-on-slot", 3))
    )


_IntfType_Type.__name__ = "Integer32"
_IntfType_Object = MibTableColumn
intfType = _IntfType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 30, 2, 1, 3),
    _IntfType_Type()
)
intfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfType.setStatus("mandatory")


class _IntfNumInType_Type(Integer32):
    """Custom type intfNumInType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_IntfNumInType_Type.__name__ = "Integer32"
_IntfNumInType_Object = MibTableColumn
intfNumInType = _IntfNumInType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 30, 2, 1, 4),
    _IntfNumInType_Type()
)
intfNumInType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfNumInType.setStatus("mandatory")


class _IntfSlot_Type(Integer32):
    """Custom type intfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("baseCard", 0),
          ("not-applicable", 254),
          ("not-available", 255),
          ("slot-1", 1),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-A", 9),
          ("slot-B", 10),
          ("slot-C", 11),
          ("slot-D", 12))
    )


_IntfSlot_Type.__name__ = "Integer32"
_IntfSlot_Object = MibTableColumn
intfSlot = _IntfSlot_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 30, 2, 1, 5),
    _IntfSlot_Type()
)
intfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfSlot.setStatus("mandatory")


class _IntfSlotType_Type(Integer32):
    """Custom type intfSlotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              9,
              16,
              17,
              18,
              19,
              21,
              22,
              23,
              36,
              51,
              254,
              255,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("baseCard", 0),
          ("cem", 23),
          ("dvc", 18),
          ("eic", 21),
          ("eic-120", 22),
          ("ethernet", 1),
          ("g703-E1", 3),
          ("g703-E1-ii", 5),
          ("g703-T1", 4),
          ("g703-T1-ii", 6),
          ("isdn-bri-voice", 19),
          ("not-applicable", 254),
          ("not-available", 255),
          ("proxy", 36),
          ("tic", 16),
          ("tic-75", 17),
          ("tokenring", 7),
          ("unkown", 9999),
          ("vcf03", 2),
          ("vfc03r", 51),
          ("voice", 9))
    )


_IntfSlotType_Type.__name__ = "Integer32"
_IntfSlotType_Object = MibTableColumn
intfSlotType = _IntfSlotType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 30, 2, 1, 6),
    _IntfSlotType_Type()
)
intfSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfSlotType.setStatus("mandatory")


class _IntfNumInSlot_Type(Integer32):
    """Custom type intfNumInSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_IntfNumInSlot_Type.__name__ = "Integer32"
_IntfNumInSlot_Object = MibTableColumn
intfNumInSlot = _IntfNumInSlot_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 30, 2, 1, 7),
    _IntfNumInSlot_Type()
)
intfNumInSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfNumInSlot.setStatus("mandatory")


class _IntfModuleType_Type(Integer32):
    """Custom type intfModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              252,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("module-dsucsu", 23),
          ("module-i430s-dte", 19),
          ("module-i430u-dte", 20),
          ("module-i431-E1-dte", 22),
          ("module-i431-T1-dte", 21),
          ("module-rs232-dce", 0),
          ("module-rs232-dte", 1),
          ("module-rs366A-dce", 8),
          ("module-rs366A-dte", 9),
          ("module-rs449-dce", 10),
          ("module-rs449-dte", 11),
          ("module-rs530-dce", 6),
          ("module-rs530-dte", 7),
          ("module-undef", 253),
          ("module-undef-dce", 255),
          ("module-undef-dte", 254),
          ("module-univ-dce", 17),
          ("module-univ-dte", 18),
          ("module-v35-dce", 2),
          ("module-v35-dte", 3),
          ("module-x21-dce", 4),
          ("module-x21-dte", 5),
          ("not-applicable", 252))
    )


_IntfModuleType_Type.__name__ = "Integer32"
_IntfModuleType_Object = MibTableColumn
intfModuleType = _IntfModuleType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 30, 2, 1, 8),
    _IntfModuleType_Type()
)
intfModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfModuleType.setStatus("mandatory")
_Slot_ObjectIdentity = ObjectIdentity
slot = _Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 31)
)
_IntfSlotNumber_Type = Integer32
_IntfSlotNumber_Object = MibScalar
intfSlotNumber = _IntfSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 31, 1),
    _IntfSlotNumber_Type()
)
intfSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfSlotNumber.setStatus("mandatory")
_SlotPortInSlotTable_Object = MibTable
slotPortInSlotTable = _SlotPortInSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 31, 2)
)
if mibBuilder.loadTexts:
    slotPortInSlotTable.setStatus("mandatory")
_SlotPortInSlotEntry_Object = MibTableRow
slotPortInSlotEntry = _SlotPortInSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 31, 2, 1)
)
slotPortInSlotEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "slotSlot"),
    (0, "CLEARTRAC7-MIB", "slotPortInSlot"),
)
if mibBuilder.loadTexts:
    slotPortInSlotEntry.setStatus("mandatory")


class _SlotSlot_Type(Integer32):
    """Custom type slotSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("baseCard", 0),
          ("not-applicable", 254),
          ("not-available", 255),
          ("slot-1", 1),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-A", 9),
          ("slot-B", 10),
          ("slot-C", 11),
          ("slot-D", 12))
    )


_SlotSlot_Type.__name__ = "Integer32"
_SlotSlot_Object = MibTableColumn
slotSlot = _SlotSlot_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 31, 2, 1, 1),
    _SlotSlot_Type()
)
slotSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotSlot.setStatus("mandatory")


class _SlotPortInSlot_Type(Integer32):
    """Custom type slotPortInSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_SlotPortInSlot_Type.__name__ = "Integer32"
_SlotPortInSlot_Object = MibTableColumn
slotPortInSlot = _SlotPortInSlot_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 31, 2, 1, 2),
    _SlotPortInSlot_Type()
)
slotPortInSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotPortInSlot.setStatus("mandatory")
_SlotIfIndex_Type = Integer32
_SlotIfIndex_Object = MibTableColumn
slotIfIndex = _SlotIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 31, 2, 1, 3),
    _SlotIfIndex_Type()
)
slotIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotIfIndex.setStatus("mandatory")
_Ipaddr_ObjectIdentity = ObjectIdentity
ipaddr = _Ipaddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 32)
)
_IpaddrNr_Type = Integer32
_IpaddrNr_Object = MibScalar
ipaddrNr = _IpaddrNr_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 32, 1),
    _IpaddrNr_Type()
)
ipaddrNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddrNr.setStatus("mandatory")
_IpaddrTable_Object = MibTable
ipaddrTable = _IpaddrTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 32, 2)
)
if mibBuilder.loadTexts:
    ipaddrTable.setStatus("mandatory")
_IpaddrEntry_Object = MibTableRow
ipaddrEntry = _IpaddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 32, 2, 1)
)
ipaddrEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "ipaddrIndex"),
)
if mibBuilder.loadTexts:
    ipaddrEntry.setStatus("mandatory")
_IpaddrIndex_Type = Integer32
_IpaddrIndex_Object = MibTableColumn
ipaddrIndex = _IpaddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 32, 2, 1, 1),
    _IpaddrIndex_Type()
)
ipaddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddrIndex.setStatus("mandatory")
_IpaddrAddr_Type = IpAddress
_IpaddrAddr_Object = MibTableColumn
ipaddrAddr = _IpaddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 32, 2, 1, 2),
    _IpaddrAddr_Type()
)
ipaddrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipaddrAddr.setStatus("mandatory")


class _IpaddrType_Type(Integer32):
    """Custom type ipaddrType based on Integer32"""
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
        *(("global", 1),
          ("lan", 3),
          ("proxy", 4),
          ("pvc", 5),
          ("undef", 0),
          ("wan", 2))
    )


_IpaddrType_Type.__name__ = "Integer32"
_IpaddrType_Object = MibTableColumn
ipaddrType = _IpaddrType_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 32, 2, 1, 3),
    _IpaddrType_Type()
)
ipaddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddrType.setStatus("mandatory")
_IpaddrIfIndex_Type = Integer32
_IpaddrIfIndex_Object = MibTableColumn
ipaddrIfIndex = _IpaddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 32, 2, 1, 4),
    _IpaddrIfIndex_Type()
)
ipaddrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddrIfIndex.setStatus("mandatory")
_Bootp_ObjectIdentity = ObjectIdentity
bootp = _Bootp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 33)
)


class _BootpEnable_Type(Integer32):
    """Custom type bootpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("not-applicable", 254),
          ("not-available", 255))
    )


_BootpEnable_Type.__name__ = "Integer32"
_BootpEnable_Object = MibScalar
bootpEnable = _BootpEnable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 33, 1),
    _BootpEnable_Type()
)
bootpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpEnable.setStatus("mandatory")


class _BootpMaxHops_Type(Integer32):
    """Custom type bootpMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_BootpMaxHops_Type.__name__ = "Integer32"
_BootpMaxHops_Object = MibScalar
bootpMaxHops = _BootpMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 33, 2),
    _BootpMaxHops_Type()
)
bootpMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpMaxHops.setStatus("mandatory")
_BootpIpDestAddr1_Type = IpAddress
_BootpIpDestAddr1_Object = MibScalar
bootpIpDestAddr1 = _BootpIpDestAddr1_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 33, 3),
    _BootpIpDestAddr1_Type()
)
bootpIpDestAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpIpDestAddr1.setStatus("mandatory")
_BootpIpDestAddr2_Type = IpAddress
_BootpIpDestAddr2_Object = MibScalar
bootpIpDestAddr2 = _BootpIpDestAddr2_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 33, 4),
    _BootpIpDestAddr2_Type()
)
bootpIpDestAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpIpDestAddr2.setStatus("mandatory")
_BootpIpDestAddr3_Type = IpAddress
_BootpIpDestAddr3_Object = MibScalar
bootpIpDestAddr3 = _BootpIpDestAddr3_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 33, 5),
    _BootpIpDestAddr3_Type()
)
bootpIpDestAddr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpIpDestAddr3.setStatus("mandatory")
_BootpIpDestAddr4_Type = IpAddress
_BootpIpDestAddr4_Object = MibScalar
bootpIpDestAddr4 = _BootpIpDestAddr4_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 33, 6),
    _BootpIpDestAddr4_Type()
)
bootpIpDestAddr4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpIpDestAddr4.setStatus("mandatory")
_Proxy_ObjectIdentity = ObjectIdentity
proxy = _Proxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 34)
)
_ProxyNumber_Type = Integer32
_ProxyNumber_Object = MibScalar
proxyNumber = _ProxyNumber_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 34, 1),
    _ProxyNumber_Type()
)
proxyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyNumber.setStatus("mandatory")
_ProxyTable_Object = MibTable
proxyTable = _ProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 34, 2)
)
if mibBuilder.loadTexts:
    proxyTable.setStatus("mandatory")
_ProxyEntry_Object = MibTableRow
proxyEntry = _ProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 34, 2, 1)
)
proxyEntry.setIndexNames(
    (0, "CLEARTRAC7-MIB", "proxyIndex"),
)
if mibBuilder.loadTexts:
    proxyEntry.setStatus("mandatory")
_ProxyIndex_Type = Integer32
_ProxyIndex_Object = MibTableColumn
proxyIndex = _ProxyIndex_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 34, 2, 1, 1),
    _ProxyIndex_Type()
)
proxyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyIndex.setStatus("mandatory")


class _ProxyComm_Type(DisplayString):
    """Custom type proxyComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProxyComm_Type.__name__ = "DisplayString"
_ProxyComm_Object = MibTableColumn
proxyComm = _ProxyComm_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 34, 2, 1, 2),
    _ProxyComm_Type()
)
proxyComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyComm.setStatus("mandatory")
_ProxyIpAddr_Type = IpAddress
_ProxyIpAddr_Object = MibTableColumn
proxyIpAddr = _ProxyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 34, 2, 1, 3),
    _ProxyIpAddr_Type()
)
proxyIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyIpAddr.setStatus("mandatory")
_ProxyIpMask_Type = IpAddress
_ProxyIpMask_Object = MibTableColumn
proxyIpMask = _ProxyIpMask_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 34, 2, 1, 4),
    _ProxyIpMask_Type()
)
proxyIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyIpMask.setStatus("mandatory")
_ProxyTrapIpAddr_Type = IpAddress
_ProxyTrapIpAddr_Object = MibTableColumn
proxyTrapIpAddr = _ProxyTrapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 34, 2, 1, 5),
    _ProxyTrapIpAddr_Type()
)
proxyTrapIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyTrapIpAddr.setStatus("mandatory")
_ProxyDefaultGateway_Type = IpAddress
_ProxyDefaultGateway_Object = MibTableColumn
proxyDefaultGateway = _ProxyDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 34, 2, 1, 6),
    _ProxyDefaultGateway_Type()
)
proxyDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    proxyDefaultGateway.setStatus("mandatory")
_Timep_ObjectIdentity = ObjectIdentity
timep = _Timep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 35)
)


class _TimepTimeZoneSign_Type(Integer32):
    """Custom type timepTimeZoneSign based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TimepTimeZoneSign_Type.__name__ = "Integer32"
_TimepTimeZoneSign_Object = MibScalar
timepTimeZoneSign = _TimepTimeZoneSign_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 35, 1),
    _TimepTimeZoneSign_Type()
)
timepTimeZoneSign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timepTimeZoneSign.setStatus("mandatory")


class _TimepTimeZone_Type(Integer32):
    """Custom type timepTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_TimepTimeZone_Type.__name__ = "Integer32"
_TimepTimeZone_Object = MibScalar
timepTimeZone = _TimepTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 35, 2),
    _TimepTimeZone_Type()
)
timepTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timepTimeZone.setStatus("mandatory")


class _TimepDaylightSaving_Type(Integer32):
    """Custom type timepDaylightSaving based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TimepDaylightSaving_Type.__name__ = "Integer32"
_TimepDaylightSaving_Object = MibScalar
timepDaylightSaving = _TimepDaylightSaving_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 35, 3),
    _TimepDaylightSaving_Type()
)
timepDaylightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timepDaylightSaving.setStatus("mandatory")


class _TimepServerProtocol_Type(Integer32):
    """Custom type timepServerProtocol based on Integer32"""
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
        *(("both", 4),
          ("none", 1),
          ("tcp", 3),
          ("udp", 2))
    )


_TimepServerProtocol_Type.__name__ = "Integer32"
_TimepServerProtocol_Object = MibScalar
timepServerProtocol = _TimepServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 35, 4),
    _TimepServerProtocol_Type()
)
timepServerProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timepServerProtocol.setStatus("mandatory")


class _TimepClientProtocol_Type(Integer32):
    """Custom type timepClientProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tcp", 3),
          ("udp", 2))
    )


_TimepClientProtocol_Type.__name__ = "Integer32"
_TimepClientProtocol_Object = MibScalar
timepClientProtocol = _TimepClientProtocol_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 35, 5),
    _TimepClientProtocol_Type()
)
timepClientProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timepClientProtocol.setStatus("mandatory")
_TimepServerIpAddress_Type = IpAddress
_TimepServerIpAddress_Object = MibScalar
timepServerIpAddress = _TimepServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 35, 6),
    _TimepServerIpAddress_Type()
)
timepServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timepServerIpAddress.setStatus("mandatory")


class _TimepClientUpdateInterval_Type(Integer32):
    """Custom type timepClientUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_TimepClientUpdateInterval_Type.__name__ = "Integer32"
_TimepClientUpdateInterval_Object = MibScalar
timepClientUpdateInterval = _TimepClientUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 35, 7),
    _TimepClientUpdateInterval_Type()
)
timepClientUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timepClientUpdateInterval.setStatus("mandatory")


class _TimepClientUdpTimeout_Type(Integer32):
    """Custom type timepClientUdpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_TimepClientUdpTimeout_Type.__name__ = "Integer32"
_TimepClientUdpTimeout_Object = MibScalar
timepClientUdpTimeout = _TimepClientUdpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 35, 8),
    _TimepClientUdpTimeout_Type()
)
timepClientUdpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timepClientUdpTimeout.setStatus("mandatory")


class _TimepClientUdpRetransmissions_Type(Integer32):
    """Custom type timepClientUdpRetransmissions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_TimepClientUdpRetransmissions_Type.__name__ = "Integer32"
_TimepClientUdpRetransmissions_Object = MibScalar
timepClientUdpRetransmissions = _TimepClientUdpRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 35, 9),
    _TimepClientUdpRetransmissions_Type()
)
timepClientUdpRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timepClientUdpRetransmissions.setStatus("mandatory")


class _TimepGetServerTimeNow_Type(Integer32):
    """Custom type timepGetServerTimeNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TimepGetServerTimeNow_Type.__name__ = "Integer32"
_TimepGetServerTimeNow_Object = MibScalar
timepGetServerTimeNow = _TimepGetServerTimeNow_Object(
    (1, 3, 6, 1, 4, 1, 727, 7, 2, 35, 10),
    _TimepGetServerTimeNow_Type()
)
timepGetServerTimeNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timepGetServerTimeNow.setStatus("mandatory")

# Managed Objects groups


# Notification objects

connectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 600)
)
connectionDown.setObjects(
    ("CLEARTRAC7-MIB", "puIndex")
)
if mibBuilder.loadTexts:
    connectionDown.setStatus(
        ""
    )

linkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 601)
)
linkDown.setObjects(
    ("CLEARTRAC7-MIB", "ifwanIndex")
)
if mibBuilder.loadTexts:
    linkDown.setStatus(
        ""
    )

pvcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 602)
)
pvcDown.setObjects(
    ("CLEARTRAC7-MIB", "pvcIndex")
)
if mibBuilder.loadTexts:
    pvcDown.setStatus(
        ""
    )

cardDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 603)
)
cardDown.setObjects(
    ("CLEARTRAC7-MIB", "sysTrapRackandPos")
)
if mibBuilder.loadTexts:
    cardDown.setStatus(
        ""
    )

connectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 604)
)
connectionUp.setObjects(
    ("CLEARTRAC7-MIB", "puIndex")
)
if mibBuilder.loadTexts:
    connectionUp.setStatus(
        ""
    )

linkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 605)
)
linkUp.setObjects(
    ("CLEARTRAC7-MIB", "ifwanIndex")
)
if mibBuilder.loadTexts:
    linkUp.setStatus(
        ""
    )

pvcUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 606)
)
pvcUp.setObjects(
    ("CLEARTRAC7-MIB", "pvcIndex")
)
if mibBuilder.loadTexts:
    pvcUp.setStatus(
        ""
    )

cardup = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 607)
)
cardup.setObjects(
    ("CLEARTRAC7-MIB", "sysTrapRackandPos")
)
if mibBuilder.loadTexts:
    cardup.setStatus(
        ""
    )

periodStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 608)
)
periodStarted.setObjects(
    ("CLEARTRAC7-MIB", "schedulePeriod")
)
if mibBuilder.loadTexts:
    periodStarted.setStatus(
        ""
    )

periodEnded = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 609)
)
periodEnded.setObjects(
    ("CLEARTRAC7-MIB", "schedulePeriod")
)
if mibBuilder.loadTexts:
    periodEnded.setStatus(
        ""
    )

badDestPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 610)
)
badDestPort.setObjects(
    ("CLEARTRAC7-MIB", "ifwanIndex")
)
if mibBuilder.loadTexts:
    badDestPort.setStatus(
        ""
    )

badDestPvc = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 611)
)
badDestPvc.setObjects(
    ("CLEARTRAC7-MIB", "ifwanIndex")
)
if mibBuilder.loadTexts:
    badDestPvc.setStatus(
        ""
    )

backupCall = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 612)
)
if mibBuilder.loadTexts:
    backupCall.setStatus(
        ""
    )

backupHang = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 613)
)
if mibBuilder.loadTexts:
    backupHang.setStatus(
        ""
    )

manualCall = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 614)
)
if mibBuilder.loadTexts:
    manualCall.setStatus(
        ""
    )

manualHang = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 615)
)
if mibBuilder.loadTexts:
    manualHang.setStatus(
        ""
    )

bondTrig = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 616)
)
if mibBuilder.loadTexts:
    bondTrig.setStatus(
        ""
    )

bondDeTrig = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 617)
)
if mibBuilder.loadTexts:
    bondDeTrig.setStatus(
        ""
    )

firmwareStored = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 618)
)
if mibBuilder.loadTexts:
    firmwareStored.setStatus(
        ""
    )

cfgStored = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 619)
)
if mibBuilder.loadTexts:
    cfgStored.setStatus(
        ""
    )

noTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 620)
)
if mibBuilder.loadTexts:
    noTrap.setStatus(
        ""
    )

fatalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 621)
)
if mibBuilder.loadTexts:
    fatalTrap.setStatus(
        ""
    )

notMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 622)
)
if mibBuilder.loadTexts:
    notMemory.setStatus(
        ""
    )

setupReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 623)
)
if mibBuilder.loadTexts:
    setupReset.setStatus(
        ""
    )

badChecksum = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 624)
)
if mibBuilder.loadTexts:
    badChecksum.setStatus(
        ""
    )

fatalMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 625)
)
if mibBuilder.loadTexts:
    fatalMsg.setStatus(
        ""
    )

noMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 626)
)
if mibBuilder.loadTexts:
    noMsg.setStatus(
        ""
    )

bothPsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 627)
)
if mibBuilder.loadTexts:
    bothPsUp.setStatus(
        ""
    )

onePsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 628)
)
if mibBuilder.loadTexts:
    onePsDown.setStatus(
        ""
    )

bothFansUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 629)
)
if mibBuilder.loadTexts:
    bothFansUp.setStatus(
        ""
    )

oneOrMoreFanDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 630)
)
if mibBuilder.loadTexts:
    oneOrMoreFanDown.setStatus(
        ""
    )

accountingFileFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 631)
)
if mibBuilder.loadTexts:
    accountingFileFull.setStatus(
        ""
    )

frLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 665)
)
frLinkUp.setObjects(
    ("CLEARTRAC7-MIB", "ifwanIndex")
)
if mibBuilder.loadTexts:
    frLinkUp.setStatus(
        ""
    )

frLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 666)
)
frLinkDown.setObjects(
    ("CLEARTRAC7-MIB", "ifwanIndex")
)
if mibBuilder.loadTexts:
    frLinkDown.setStatus(
        ""
    )

q922Up = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 667)
)
q922Up.setObjects(
    ("CLEARTRAC7-MIB", "ifwanIndex")
)
if mibBuilder.loadTexts:
    q922Up.setStatus(
        ""
    )

q922Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 668)
)
q922Down.setObjects(
    ("CLEARTRAC7-MIB", "ifwanIndex")
)
if mibBuilder.loadTexts:
    q922Down.setStatus(
        ""
    )

accountingFileOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 727, 0, 669)
)
if mibBuilder.loadTexts:
    accountingFileOverflow.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLEARTRAC7-MIB",
    **{"lucent": lucent,
       "connectionDown": connectionDown,
       "linkDown": linkDown,
       "pvcDown": pvcDown,
       "cardDown": cardDown,
       "connectionUp": connectionUp,
       "linkUp": linkUp,
       "pvcUp": pvcUp,
       "cardup": cardup,
       "periodStarted": periodStarted,
       "periodEnded": periodEnded,
       "badDestPort": badDestPort,
       "badDestPvc": badDestPvc,
       "backupCall": backupCall,
       "backupHang": backupHang,
       "manualCall": manualCall,
       "manualHang": manualHang,
       "bondTrig": bondTrig,
       "bondDeTrig": bondDeTrig,
       "firmwareStored": firmwareStored,
       "cfgStored": cfgStored,
       "noTrap": noTrap,
       "fatalTrap": fatalTrap,
       "notMemory": notMemory,
       "setupReset": setupReset,
       "badChecksum": badChecksum,
       "fatalMsg": fatalMsg,
       "noMsg": noMsg,
       "bothPsUp": bothPsUp,
       "onePsDown": onePsDown,
       "bothFansUp": bothFansUp,
       "oneOrMoreFanDown": oneOrMoreFanDown,
       "accountingFileFull": accountingFileFull,
       "frLinkUp": frLinkUp,
       "frLinkDown": frLinkDown,
       "q922Up": q922Up,
       "q922Down": q922Down,
       "accountingFileOverflow": accountingFileOverflow,
       "cleartrac7": cleartrac7,
       "mgmt": mgmt,
       "system": system,
       "sysDesc": sysDesc,
       "sysContact": sysContact,
       "sysName": sysName,
       "sysLocation": sysLocation,
       "sysDate": sysDate,
       "sysClock": sysClock,
       "sysDay": sysDay,
       "sysAcceptLoop": sysAcceptLoop,
       "sysLinkTimeout-s": sysLinkTimeout_s,
       "sysTransitDelay-s": sysTransitDelay_s,
       "sysDefaultIpAddr": sysDefaultIpAddr,
       "sysDefaultIpMask": sysDefaultIpMask,
       "sysDefaultGateway": sysDefaultGateway,
       "sysRackId": sysRackId,
       "sysPsAndFansMonitoring": sysPsAndFansMonitoring,
       "sysSnmpTrapIpAddr1": sysSnmpTrapIpAddr1,
       "sysSnmpTrapIpAddr2": sysSnmpTrapIpAddr2,
       "sysSnmpTrapIpAddr3": sysSnmpTrapIpAddr3,
       "sysSnmpTrapIpAddr4": sysSnmpTrapIpAddr4,
       "sysUnitRoutingVersion": sysUnitRoutingVersion,
       "sysThisPosId": sysThisPosId,
       "sysPosNr": sysPosNr,
       "sysPosTable": sysPosTable,
       "sysPosEntry": sysPosEntry,
       "sysPosId": sysPosId,
       "sysPosProduct": sysPosProduct,
       "sysPosRackId": sysPosRackId,
       "sysPosIpAddr": sysPosIpAddr,
       "sysRacksNr": sysRacksNr,
       "sysDLCI": sysDLCI,
       "sysExtensionNumLength": sysExtensionNumLength,
       "sysExtendedDigitsLength": sysExtendedDigitsLength,
       "sysDialTimer": sysDialTimer,
       "sysCountry": sysCountry,
       "sysJitterBuf": sysJitterBuf,
       "sysRingFreq": sysRingFreq,
       "sysRingVolt": sysRingVolt,
       "sysVoiceEncoding": sysVoiceEncoding,
       "sysVoiceClocking": sysVoiceClocking,
       "sysVoiceLog": sysVoiceLog,
       "sysSpeedDialNumLength": sysSpeedDialNumLength,
       "sysAutoSaveDelay": sysAutoSaveDelay,
       "sysPsMonitoring": sysPsMonitoring,
       "sysVoiceHighestPriority": sysVoiceHighestPriority,
       "sysVoiceClass": sysVoiceClass,
       "sysHuntForwardingAUnit": sysHuntForwardingAUnit,
       "sysHuntForwardingBUnit": sysHuntForwardingBUnit,
       "sysHuntForwardingADLCI": sysHuntForwardingADLCI,
       "sysHuntForwardingBDLCI": sysHuntForwardingBDLCI,
       "sysHuntForwardingASvcAddress": sysHuntForwardingASvcAddress,
       "sysHuntForwardingBSvcAddress": sysHuntForwardingBSvcAddress,
       "sysBackplaneRipVersion": sysBackplaneRipVersion,
       "sysTrapRackandPos": sysTrapRackandPos,
       "ifwan": ifwan,
       "ifwanNumber": ifwanNumber,
       "ifwanTable": ifwanTable,
       "ifwanEntry": ifwanEntry,
       "ifwanIndex": ifwanIndex,
       "ifwanDesc": ifwanDesc,
       "ifwanProtocol": ifwanProtocol,
       "ifwanSpeed-bps": ifwanSpeed_bps,
       "ifwanFallBackSpeed-bps": ifwanFallBackSpeed_bps,
       "ifwanInterface": ifwanInterface,
       "ifwanClocking": ifwanClocking,
       "ifwanCoding": ifwanCoding,
       "ifwanModem": ifwanModem,
       "ifwanTxStart": ifwanTxStart,
       "ifwanIdle": ifwanIdle,
       "ifwanDuplex": ifwanDuplex,
       "ifwanGroupPoll": ifwanGroupPoll,
       "ifwanGroupAddress": ifwanGroupAddress,
       "ifwanPollDelay-ms": ifwanPollDelay_ms,
       "ifwanFrameDelay": ifwanFrameDelay,
       "ifwanFormat": ifwanFormat,
       "ifwanSync": ifwanSync,
       "ifwanDropSyncCounter": ifwanDropSyncCounter,
       "ifwanDropSyncCharacter": ifwanDropSyncCharacter,
       "ifwanMode": ifwanMode,
       "ifwanBodCall-s": ifwanBodCall_s,
       "ifwanBodHang-s": ifwanBodHang_s,
       "ifwanBodLevel": ifwanBodLevel,
       "ifwanBackupCall-s": ifwanBackupCall_s,
       "ifwanBackupHang-s": ifwanBackupHang_s,
       "ifwanPortToBack": ifwanPortToBack,
       "ifwanDialer": ifwanDialer,
       "ifwanRemoteUnit": ifwanRemoteUnit,
       "ifwanClassNumber": ifwanClassNumber,
       "ifwanRingNumber": ifwanRingNumber,
       "ifwanIpAddress": ifwanIpAddress,
       "ifwanSubnetMask": ifwanSubnetMask,
       "ifwanMaxFrame": ifwanMaxFrame,
       "ifwanCompression": ifwanCompression,
       "ifwanPriority": ifwanPriority,
       "ifwanTimeout": ifwanTimeout,
       "ifwanRetry": ifwanRetry,
       "ifwanRemotePort": ifwanRemotePort,
       "ifwanFlowControl": ifwanFlowControl,
       "ifwanMgmtInterface": ifwanMgmtInterface,
       "ifwanEnquiryTimer-s": ifwanEnquiryTimer_s,
       "ifwanReportCycle": ifwanReportCycle,
       "ifwanIpRip": ifwanIpRip,
       "ifwanCllm": ifwanCllm,
       "ifwanIpxRip": ifwanIpxRip,
       "ifwanIpxSap": ifwanIpxSap,
       "ifwanIpxNetNum": ifwanIpxNetNum,
       "ifwanRxFlow": ifwanRxFlow,
       "ifwanTxFlow": ifwanTxFlow,
       "ifwanTxHold-s": ifwanTxHold_s,
       "ifwanDsOSpeed-bps": ifwanDsOSpeed_bps,
       "ifwanFraming": ifwanFraming,
       "ifwanTerminating": ifwanTerminating,
       "ifwanCrc4": ifwanCrc4,
       "ifwanLineCoding": ifwanLineCoding,
       "ifwanBChannels": ifwanBChannels,
       "ifwanMultiframing": ifwanMultiframing,
       "ifwanOspfEnable": ifwanOspfEnable,
       "ifwanOspfAreaId": ifwanOspfAreaId,
       "ifwanOspfTransitDelay": ifwanOspfTransitDelay,
       "ifwanOspfRetransmitInt": ifwanOspfRetransmitInt,
       "ifwanOspfHelloInt": ifwanOspfHelloInt,
       "ifwanOspfDeadInt": ifwanOspfDeadInt,
       "ifwanOspfPassword": ifwanOspfPassword,
       "ifwanOspfMetricCost": ifwanOspfMetricCost,
       "ifwanChUse": ifwanChUse,
       "ifwanGainLimit": ifwanGainLimit,
       "ifwanSignaling": ifwanSignaling,
       "ifwanIdleCode": ifwanIdleCode,
       "ifwanLineBuild": ifwanLineBuild,
       "ifwanT1E1Status": ifwanT1E1Status,
       "ifwanT1E1LoopBack": ifwanT1E1LoopBack,
       "ifwanChExp": ifwanChExp,
       "ifwanT1E1InterBit": ifwanT1E1InterBit,
       "ifwanEncodingLaw": ifwanEncodingLaw,
       "ifwanTxStartCop": ifwanTxStartCop,
       "ifwanTxStartPass": ifwanTxStartPass,
       "ifwanFallBackSpeedEnable": ifwanFallBackSpeedEnable,
       "ifwanDialTimeout-s": ifwanDialTimeout_s,
       "ifwanCellPacketization": ifwanCellPacketization,
       "ifwanMaxChannels": ifwanMaxChannels,
       "ifwanCondLMIPort": ifwanCondLMIPort,
       "ifwanExtNumber": ifwanExtNumber,
       "ifwanDestExtNumber": ifwanDestExtNumber,
       "ifwanConnTimeout-s": ifwanConnTimeout_s,
       "ifwanSvcAddressType": ifwanSvcAddressType,
       "ifwanSvcNetworkAddress": ifwanSvcNetworkAddress,
       "ifwanSvcMaxTxTimeoutT200": ifwanSvcMaxTxTimeoutT200,
       "ifwanSvcInactiveTimeoutT203": ifwanSvcInactiveTimeoutT203,
       "ifwanSvcIframeRetransmissionsN200": ifwanSvcIframeRetransmissionsN200,
       "ifwanSvcSetupTimeoutT303": ifwanSvcSetupTimeoutT303,
       "ifwanSvcDisconnectTimeoutT305": ifwanSvcDisconnectTimeoutT305,
       "ifwanSvcReleaseTimeoutT308": ifwanSvcReleaseTimeoutT308,
       "ifwanSvcCallProceedingTimeoutT310": ifwanSvcCallProceedingTimeoutT310,
       "ifwanSvcStatusTimeoutT322": ifwanSvcStatusTimeoutT322,
       "ifwanTeiMode": ifwanTeiMode,
       "ifwanDigitNumber": ifwanDigitNumber,
       "ifwanMsn1": ifwanMsn1,
       "ifwanMsn2": ifwanMsn2,
       "ifwanMsn3": ifwanMsn3,
       "ifwanX25Encapsulation": ifwanX25Encapsulation,
       "ifwanPvcNumber": ifwanPvcNumber,
       "ifwanQsigPbxAb": ifwanQsigPbxAb,
       "ifwanQsigPbxXy": ifwanQsigPbxXy,
       "ifwanIpRipTxRx": ifwanIpRipTxRx,
       "ifwanIpRipAuthType": ifwanIpRipAuthType,
       "ifwanIpRipPassword": ifwanIpRipPassword,
       "ifwanPppSilent": ifwanPppSilent,
       "ifwanPppConfigRestartTimer": ifwanPppConfigRestartTimer,
       "ifwanPppConfigRetries": ifwanPppConfigRetries,
       "ifwanPppNegociateLocalMru": ifwanPppNegociateLocalMru,
       "ifwanPppLocalMru": ifwanPppLocalMru,
       "ifwanPppNegociatePeerMru": ifwanPppNegociatePeerMru,
       "ifwanPppPeerMruUpTo": ifwanPppPeerMruUpTo,
       "ifwanPppNegociateAccm": ifwanPppNegociateAccm,
       "ifwanPppRequestedAccmChar": ifwanPppRequestedAccmChar,
       "ifwanPppAcceptAccmPeer": ifwanPppAcceptAccmPeer,
       "ifwanPppAcceptableAccmChar": ifwanPppAcceptableAccmChar,
       "ifwanPppRequestMagicNum": ifwanPppRequestMagicNum,
       "ifwanPppAcceptMagicNum": ifwanPppAcceptMagicNum,
       "ifwanPppAcceptOldIpAddNeg": ifwanPppAcceptOldIpAddNeg,
       "ifwanPppNegociateIpAddress": ifwanPppNegociateIpAddress,
       "ifwanPppAcceptIpAddress": ifwanPppAcceptIpAddress,
       "ifwanPppRemoteIpAddress": ifwanPppRemoteIpAddress,
       "ifwanPppRemoteSubnetMask": ifwanPppRemoteSubnetMask,
       "ifwanHighPriorityTransparentClass": ifwanHighPriorityTransparentClass,
       "ifwanTransparentClassNumber": ifwanTransparentClassNumber,
       "ifwanChannelCompressed": ifwanChannelCompressed,
       "ifwanSfType": ifwanSfType,
       "ifwanSfMode": ifwanSfMode,
       "ifwanSfCarrierId": ifwanSfCarrierId,
       "iflan": iflan,
       "iflanNumber": iflanNumber,
       "iflanTable": iflanTable,
       "iflanEntry": iflanEntry,
       "iflanIndex": iflanIndex,
       "iflanDesc": iflanDesc,
       "iflanProtocol": iflanProtocol,
       "iflanSpeed": iflanSpeed,
       "iflanPriority": iflanPriority,
       "iflanCost": iflanCost,
       "iflanPhysAddr": iflanPhysAddr,
       "iflanIpAddress": iflanIpAddress,
       "iflanSubnetMask": iflanSubnetMask,
       "iflanMaxFrame": iflanMaxFrame,
       "iflanEth-LinkIntegrity": iflanEth_LinkIntegrity,
       "iflanTr-Monitor": iflanTr_Monitor,
       "iflanTr-Etr": iflanTr_Etr,
       "iflanTr-RingNumber": iflanTr_RingNumber,
       "iflanIpRip": iflanIpRip,
       "iflanIpxRip": iflanIpxRip,
       "iflanIpxSap": iflanIpxSap,
       "iflanIpxNetNum": iflanIpxNetNum,
       "iflanIpxLanType": iflanIpxLanType,
       "iflanOspfEnable": iflanOspfEnable,
       "iflanOspfAreaId": iflanOspfAreaId,
       "iflanOspfPriority": iflanOspfPriority,
       "iflanOspfTransitDelay": iflanOspfTransitDelay,
       "iflanOspfRetransmitInt": iflanOspfRetransmitInt,
       "iflanOspfHelloInt": iflanOspfHelloInt,
       "iflanOspfDeadInt": iflanOspfDeadInt,
       "iflanOspfPassword": iflanOspfPassword,
       "iflanOspfMetricCost": iflanOspfMetricCost,
       "iflanIpRipTxRx": iflanIpRipTxRx,
       "iflanIpRipAuthType": iflanIpRipAuthType,
       "iflanIpRipPassword": iflanIpRipPassword,
       "pu": pu,
       "puNumber": puNumber,
       "puTable": puTable,
       "puEntry": puEntry,
       "puIndex": puIndex,
       "puMode": puMode,
       "puActive": puActive,
       "puDelayBeforeConn-s": puDelayBeforeConn_s,
       "puRole": puRole,
       "puSdlcPort": puSdlcPort,
       "puSdlcAddress": puSdlcAddress,
       "puSdlcPort2": puSdlcPort2,
       "puSdlcAddress2": puSdlcAddress2,
       "puSdlcTimeout-ms": puSdlcTimeout_ms,
       "puSdlcRetry": puSdlcRetry,
       "puSdlcWindow": puSdlcWindow,
       "puSdlcMaxFrame": puSdlcMaxFrame,
       "puLlcDa": puLlcDa,
       "puLlcTr-Routing": puLlcTr_Routing,
       "puLlcSsap": puLlcSsap,
       "puLlcDsap": puLlcDsap,
       "puLlcTimeout-ms": puLlcTimeout_ms,
       "puLlcRetry": puLlcRetry,
       "puLlcWindow": puLlcWindow,
       "puLlcDynamicWindow": puLlcDynamicWindow,
       "puLlcMaxFrame": puLlcMaxFrame,
       "puDlsDa": puDlsDa,
       "puDlsSsap": puDlsSsap,
       "puDlsDsap": puDlsDsap,
       "puDlsIpSrc": puDlsIpSrc,
       "puDlsIpDst": puDlsIpDst,
       "puDlsMaxFrame": puDlsMaxFrame,
       "puLinkRemoteUnit": puLinkRemoteUnit,
       "puLinkClassNumber": puLinkClassNumber,
       "puLinkRemPu": puLinkRemPu,
       "puXid": puXid,
       "puXidId": puXidId,
       "puXidFormat": puXidFormat,
       "puXidPuType": puXidPuType,
       "puBnnPvc": puBnnPvc,
       "puBnnFid": puBnnFid,
       "puBanDa": puBanDa,
       "puBanBnnSsap": puBanBnnSsap,
       "puBanBnnDsap": puBanBnnDsap,
       "puBanBnnTimeout-ms": puBanBnnTimeout_ms,
       "puBanBnnRetry": puBanBnnRetry,
       "puBanBnnWindow": puBanBnnWindow,
       "puBanBnnNw": puBanBnnNw,
       "puBanBnnMaxFrame": puBanBnnMaxFrame,
       "puBanRouting": puBanRouting,
       "schedule": schedule,
       "scheduleNumber": scheduleNumber,
       "scheduleTable": scheduleTable,
       "scheduleEntry": scheduleEntry,
       "schedulePeriod": schedulePeriod,
       "scheduleEnable": scheduleEnable,
       "scheduleDay": scheduleDay,
       "scheduleBeginTime": scheduleBeginTime,
       "scheduleEndTime": scheduleEndTime,
       "schedulePort1": schedulePort1,
       "schedulePort2": schedulePort2,
       "schedulePort3": schedulePort3,
       "schedulePort4": schedulePort4,
       "schedulePort5": schedulePort5,
       "schedulePort6": schedulePort6,
       "schedulePort7": schedulePort7,
       "schedulePort8": schedulePort8,
       "bridge": bridge,
       "bridgeEnable": bridgeEnable,
       "bridgeStpEnable": bridgeStpEnable,
       "bridgeLanType": bridgeLanType,
       "bridgeAgingTime-s": bridgeAgingTime_s,
       "bridgeHelloTime-s": bridgeHelloTime_s,
       "bridgeMaxAge-s": bridgeMaxAge_s,
       "bridgeForwardDelay-s": bridgeForwardDelay_s,
       "bridgePriority": bridgePriority,
       "bridgeTr-Number": bridgeTr_Number,
       "bridgeTr-SteSpan": bridgeTr_SteSpan,
       "bridgeTr-MaxHop": bridgeTr_MaxHop,
       "phone": phone,
       "phoneNumber": phoneNumber,
       "phoneTable": phoneTable,
       "phoneEntry": phoneEntry,
       "phoneIndex": phoneIndex,
       "phoneRemoteUnit": phoneRemoteUnit,
       "phonePhoneNumber": phonePhoneNumber,
       "phoneNextHop": phoneNextHop,
       "phoneCost": phoneCost,
       "filter": filter,
       "filterNumber": filterNumber,
       "filterTable": filterTable,
       "filterEntry": filterEntry,
       "filterIndex": filterIndex,
       "filterActive": filterActive,
       "filterDefinition": filterDefinition,
       "class": _pysmi_class,
       "classNumber": classNumber,
       "classDefaultClass": classDefaultClass,
       "classTable": classTable,
       "classEntry": classEntry,
       "classIndex": classIndex,
       "classWeight": classWeight,
       "classPrefRoute": classPrefRoute,
       "pvc": pvc,
       "pvcNumber": pvcNumber,
       "pvcTable": pvcTable,
       "pvcEntry": pvcEntry,
       "pvcIndex": pvcIndex,
       "pvcMode": pvcMode,
       "pvcDlciAddress": pvcDlciAddress,
       "pvcPort": pvcPort,
       "pvcUserPort": pvcUserPort,
       "pvcInfoRate": pvcInfoRate,
       "pvcPriority": pvcPriority,
       "pvcCost": pvcCost,
       "pvcRemoteUnit": pvcRemoteUnit,
       "pvcTimeout-ms": pvcTimeout_ms,
       "pvcRetry": pvcRetry,
       "pvcCompression": pvcCompression,
       "pvcIpAddress": pvcIpAddress,
       "pvcSubnetMask": pvcSubnetMask,
       "pvcMaxFrame": pvcMaxFrame,
       "pvcBroadcastGroup": pvcBroadcastGroup,
       "pvcBrgConnection": pvcBrgConnection,
       "pvcIpConnection": pvcIpConnection,
       "pvcRemotePvc": pvcRemotePvc,
       "pvcPvcClass": pvcPvcClass,
       "pvcNetworkPort": pvcNetworkPort,
       "pvcRingNumber": pvcRingNumber,
       "pvcIpRip": pvcIpRip,
       "pvcBurstInfoRate": pvcBurstInfoRate,
       "pvcUserDlci": pvcUserDlci,
       "pvcNetworkDlci": pvcNetworkDlci,
       "pvcIpxRip": pvcIpxRip,
       "pvcIpxSap": pvcIpxSap,
       "pvcIpxNetNum": pvcIpxNetNum,
       "pvcIpxConnection": pvcIpxConnection,
       "pvcType": pvcType,
       "pvcBackupCall-s": pvcBackupCall_s,
       "pvcBackupHang-s": pvcBackupHang_s,
       "pvcBackup": pvcBackup,
       "pvcOspfEnable": pvcOspfEnable,
       "pvcOspfAreaId": pvcOspfAreaId,
       "pvcOspfTransitDelay": pvcOspfTransitDelay,
       "pvcOspfRetransmitInt": pvcOspfRetransmitInt,
       "pvcOspfHelloInt": pvcOspfHelloInt,
       "pvcOspfDeadInt": pvcOspfDeadInt,
       "pvcOspfPassword": pvcOspfPassword,
       "pvcOspfMetricCost": pvcOspfMetricCost,
       "pvcProxyAddr": pvcProxyAddr,
       "pvcLlcConnection": pvcLlcConnection,
       "pvcDialTimeout": pvcDialTimeout,
       "pvcMaxChannels": pvcMaxChannels,
       "pvcHuntForwardingAUnit": pvcHuntForwardingAUnit,
       "pvcHuntForwardingBUnit": pvcHuntForwardingBUnit,
       "pvcRemoteFpUnit": pvcRemoteFpUnit,
       "pvcIpRipTxRx": pvcIpRipTxRx,
       "pvcIpRipAuthType": pvcIpRipAuthType,
       "pvcIpRipPassword": pvcIpRipPassword,
       "ipx": ipx,
       "ipxRouterEnable": ipxRouterEnable,
       "ipxInternalNetNum": ipxInternalNetNum,
       "ipstatic": ipstatic,
       "ipstaticNumber": ipstaticNumber,
       "ipstaticTable": ipstaticTable,
       "ipstaticEntry": ipstaticEntry,
       "ipstaticIndex": ipstaticIndex,
       "ipstaticValid": ipstaticValid,
       "ipstaticIpDest": ipstaticIpDest,
       "ipstaticMask": ipstaticMask,
       "ipstaticNextHop": ipstaticNextHop,
       "ip": ip,
       "ipRouterEnable": ipRouterEnable,
       "ospf": ospf,
       "ospfGlobal": ospfGlobal,
       "ospfGlobalRouterId": ospfGlobalRouterId,
       "ospfGlobalAutoVLink": ospfGlobalAutoVLink,
       "ospfGlobalRackAreaId": ospfGlobalRackAreaId,
       "ospfGlobalGlobalAreaId": ospfGlobalGlobalAreaId,
       "ospfArea": ospfArea,
       "ospfAreaNumber": ospfAreaNumber,
       "ospfAreaTable": ospfAreaTable,
       "ospfAreaEntry": ospfAreaEntry,
       "ospfAreaIndex": ospfAreaIndex,
       "ospfAreaAreaId": ospfAreaAreaId,
       "ospfAreaEnable": ospfAreaEnable,
       "ospfAreaAuthType": ospfAreaAuthType,
       "ospfAreaImportASExt": ospfAreaImportASExt,
       "ospfAreaStubMetric": ospfAreaStubMetric,
       "ospfRange": ospfRange,
       "ospfRangeNumber": ospfRangeNumber,
       "ospfRangeTable": ospfRangeTable,
       "ospfRangeEntry": ospfRangeEntry,
       "ospfRangeIndex": ospfRangeIndex,
       "ospfRangeNet": ospfRangeNet,
       "ospfRangeMask": ospfRangeMask,
       "ospfRangeEnable": ospfRangeEnable,
       "ospfRangeStatus": ospfRangeStatus,
       "ospfRangeAddToArea": ospfRangeAddToArea,
       "ospfVLink": ospfVLink,
       "ospfVLinkNumber": ospfVLinkNumber,
       "ospfVLinkTable": ospfVLinkTable,
       "ospfVLinkEntry": ospfVLinkEntry,
       "ospfVLinkIndex": ospfVLinkIndex,
       "ospfVLinkTransitAreaId": ospfVLinkTransitAreaId,
       "ospfVLinkNeighborRtrId": ospfVLinkNeighborRtrId,
       "ospfVLinkEnable": ospfVLinkEnable,
       "ospfVLinkTransitDelay": ospfVLinkTransitDelay,
       "ospfVLinkRetransmitInt": ospfVLinkRetransmitInt,
       "ospfVLinkHelloInt": ospfVLinkHelloInt,
       "ospfVLinkDeadInt": ospfVLinkDeadInt,
       "ospfVLinkPassword": ospfVLinkPassword,
       "ipxfilter": ipxfilter,
       "ipxfilterNumber": ipxfilterNumber,
       "ipxfilterTable": ipxfilterTable,
       "ipxfilterEntry": ipxfilterEntry,
       "ipxfilterIndex": ipxfilterIndex,
       "ipxfilterEnable": ipxfilterEnable,
       "ipxfilterSap": ipxfilterSap,
       "ipxfilterType": ipxfilterType,
       "ifvce": ifvce,
       "ifvceNumber": ifvceNumber,
       "ifvceTable": ifvceTable,
       "ifvceEntry": ifvceEntry,
       "ifvceIndex": ifvceIndex,
       "ifvceDesc": ifvceDesc,
       "ifvceProtocol": ifvceProtocol,
       "ifvceInterface": ifvceInterface,
       "ifvceRemotePort": ifvceRemotePort,
       "ifvceActivationType": ifvceActivationType,
       "ifvceRemoteUnit": ifvceRemoteUnit,
       "ifvceHuntGroup": ifvceHuntGroup,
       "ifvceToneDetectRegen-s": ifvceToneDetectRegen_s,
       "ifvcePulseMakeBreak-ms": ifvcePulseMakeBreak_ms,
       "ifvceToneOn-ms": ifvceToneOn_ms,
       "ifvceToneOff-ms": ifvceToneOff_ms,
       "ifvceSilenceSuppress": ifvceSilenceSuppress,
       "ifvceSignaling": ifvceSignaling,
       "ifvceLocalInbound": ifvceLocalInbound,
       "ifvceLocalOutbound": ifvceLocalOutbound,
       "ifvceFaxModemRelay": ifvceFaxModemRelay,
       "ifvceFxoTimeout-s": ifvceFxoTimeout_s,
       "ifvceTeTimer-s": ifvceTeTimer_s,
       "ifvceFwdDigits": ifvceFwdDigits,
       "ifvceFwdType": ifvceFwdType,
       "ifvceFwdDelay-ms": ifvceFwdDelay_ms,
       "ifvceDelDigits": ifvceDelDigits,
       "ifvceExtNumber": ifvceExtNumber,
       "ifvceLinkDwnBusy": ifvceLinkDwnBusy,
       "ifvceToneType": ifvceToneType,
       "ifvceRate8kx1": ifvceRate8kx1,
       "ifvceRate8kx2": ifvceRate8kx2,
       "ifvceRate5k8x1": ifvceRate5k8x1,
       "ifvceRate5k8x2": ifvceRate5k8x2,
       "ifvceDVCSilenceSuppress": ifvceDVCSilenceSuppress,
       "ifvceDVCLocalInbound": ifvceDVCLocalInbound,
       "ifvceDVCLocalOutbound": ifvceDVCLocalOutbound,
       "ifvceBroadcastDir": ifvceBroadcastDir,
       "ifvceBroadcastPvc": ifvceBroadcastPvc,
       "ifvceAnalogLinkDwnBusy": ifvceAnalogLinkDwnBusy,
       "ifvceSpeedDialNum": ifvceSpeedDialNum,
       "ifvceR2ExtendedDigitSrc": ifvceR2ExtendedDigitSrc,
       "ifvceR2Group2Digit": ifvceR2Group2Digit,
       "ifvceR2CompleteDigit": ifvceR2CompleteDigit,
       "ifvceR2BusyDigit": ifvceR2BusyDigit,
       "ifvceMaxFaxModemRate": ifvceMaxFaxModemRate,
       "ifvceRate8kx3": ifvceRate8kx3,
       "ifvceRate6kx1": ifvceRate6kx1,
       "ifvceRate6kx2": ifvceRate6kx2,
       "ifvceRate6kx3": ifvceRate6kx3,
       "ifvceRate4k8x1": ifvceRate4k8x1,
       "ifvceRate4k8x2": ifvceRate4k8x2,
       "ifvceDTalkThreshold": ifvceDTalkThreshold,
       "ifvceToneEnergyDetec": ifvceToneEnergyDetec,
       "ifvceExtendedDigitSrc": ifvceExtendedDigitSrc,
       "ifvceDtmfOnTime": ifvceDtmfOnTime,
       "ifvceEnableDtmfOnTime": ifvceEnableDtmfOnTime,
       "stat": stat,
       "statAlarmTable": statAlarmTable,
       "statAlarmEntry": statAlarmEntry,
       "statAlarmIndex": statAlarmIndex,
       "statAlarmDesc": statAlarmDesc,
       "statAlarmDate": statAlarmDate,
       "statAlarmTime": statAlarmTime,
       "statAlarmModule": statAlarmModule,
       "statAlarmAlarm": statAlarmAlarm,
       "statAlarmArg": statAlarmArg,
       "statIfwanTable": statIfwanTable,
       "statIfwanEntry": statIfwanEntry,
       "statIfwanIndex": statIfwanIndex,
       "statIfwanDesc": statIfwanDesc,
       "statIfwanProtocol": statIfwanProtocol,
       "statIfwanInterface": statIfwanInterface,
       "statIfwanModemSignal": statIfwanModemSignal,
       "statIfwanSpeed": statIfwanSpeed,
       "statIfwanState": statIfwanState,
       "statIfwanMeanTx": statIfwanMeanTx,
       "statIfwanMeanRx": statIfwanMeanRx,
       "statIfwanPeakTx": statIfwanPeakTx,
       "statIfwanPeakRx": statIfwanPeakRx,
       "statIfwanBadFrames": statIfwanBadFrames,
       "statIfwanBadFlags": statIfwanBadFlags,
       "statIfwanUnderruns": statIfwanUnderruns,
       "statIfwanRetries": statIfwanRetries,
       "statIfwanRestart": statIfwanRestart,
       "statIfwanFramesTx": statIfwanFramesTx,
       "statIfwanFramesRx": statIfwanFramesRx,
       "statIfwanOctetsTx": statIfwanOctetsTx,
       "statIfwanOctetsRx": statIfwanOctetsRx,
       "statIfwanOvrFrames": statIfwanOvrFrames,
       "statIfwanBadOctets": statIfwanBadOctets,
       "statIfwanOvrOctets": statIfwanOvrOctets,
       "statIfwanT1E1ESS": statIfwanT1E1ESS,
       "statIfwanT1E1SES": statIfwanT1E1SES,
       "statIfwanT1E1SEF": statIfwanT1E1SEF,
       "statIfwanT1E1UAS": statIfwanT1E1UAS,
       "statIfwanT1E1CSS": statIfwanT1E1CSS,
       "statIfwanT1E1PCV": statIfwanT1E1PCV,
       "statIfwanT1E1LES": statIfwanT1E1LES,
       "statIfwanT1E1BES": statIfwanT1E1BES,
       "statIfwanT1E1DM": statIfwanT1E1DM,
       "statIfwanT1E1LCV": statIfwanT1E1LCV,
       "statIfwanCompErrs": statIfwanCompErrs,
       "statIfwanChOverflows": statIfwanChOverflows,
       "statIfwanChAborts": statIfwanChAborts,
       "statIfwanChSeqErrs": statIfwanChSeqErrs,
       "statIfwanDropInsert": statIfwanDropInsert,
       "statIfwanTrspState": statIfwanTrspState,
       "statIfwanTrspLastError": statIfwanTrspLastError,
       "statIfwanQ922State": statIfwanQ922State,
       "statIflanTable": statIflanTable,
       "statIflanEntry": statIflanEntry,
       "statIflanIndex": statIflanIndex,
       "statIflanProtocol": statIflanProtocol,
       "statIflanSpeed": statIflanSpeed,
       "statIflanConnectionStatus": statIflanConnectionStatus,
       "statIflanOperatingMode": statIflanOperatingMode,
       "statIflanEth-Interface": statIflanEth_Interface,
       "statIflanMeanTx-kbps": statIflanMeanTx_kbps,
       "statIflanMeanRx-kbps": statIflanMeanRx_kbps,
       "statIflanPeakTx-kbps": statIflanPeakTx_kbps,
       "statIflanPeakRx-kbps": statIflanPeakRx_kbps,
       "statIflanRetries": statIflanRetries,
       "statIflanBadFrames": statIflanBadFrames,
       "statIflanBadFlags": statIflanBadFlags,
       "statIflanTr-ReceiveCongestion": statIflanTr_ReceiveCongestion,
       "statIflanEth-OneCollision": statIflanEth_OneCollision,
       "statIflanEth-TwoCollisions": statIflanEth_TwoCollisions,
       "statIflanEth-ThreeAndMoreCol": statIflanEth_ThreeAndMoreCol,
       "statIflanEth-DeferredTrans": statIflanEth_DeferredTrans,
       "statIflanEth-ExcessiveCollision": statIflanEth_ExcessiveCollision,
       "statIflanEth-LateCollision": statIflanEth_LateCollision,
       "statIflanEth-FrameCheckSeq": statIflanEth_FrameCheckSeq,
       "statIflanEth-Align": statIflanEth_Align,
       "statIflanEth-CarrierSense": statIflanEth_CarrierSense,
       "statPuTable": statPuTable,
       "statPuEntry": statPuEntry,
       "statPuIndex": statPuIndex,
       "statPuMode": statPuMode,
       "statPuConnectionStatus": statPuConnectionStatus,
       "statPuCompErrs": statPuCompErrs,
       "statPuChOverflows": statPuChOverflows,
       "statPuChAborts": statPuChAborts,
       "statPuChSeqErrs": statPuChSeqErrs,
       "statBridge": statBridge,
       "statBridgeBridge": statBridgeBridge,
       "statBridgeBridgeAddressDiscard": statBridgeBridgeAddressDiscard,
       "statBridgeBridgeFrameDiscard": statBridgeBridgeFrameDiscard,
       "statBridgeBridgeDesignatedRoot": statBridgeBridgeDesignatedRoot,
       "statBridgeBridgeRootCost": statBridgeBridgeRootCost,
       "statBridgeBridgeRootPort": statBridgeBridgeRootPort,
       "statBridgeBridgeFrameFiltered": statBridgeBridgeFrameFiltered,
       "statBridgeBridgeFrameTimeout": statBridgeBridgeFrameTimeout,
       "statBridgePort": statBridgePort,
       "statBridgePortTable": statBridgePortTable,
       "statBridgePortEntry": statBridgePortEntry,
       "statBridgePortIndex": statBridgePortIndex,
       "statBridgePortDestination": statBridgePortDestination,
       "statBridgePortState": statBridgePortState,
       "statBridgePortDesignatedRoot": statBridgePortDesignatedRoot,
       "statBridgePortDesignatedCost": statBridgePortDesignatedCost,
       "statBridgePortDesignatedBridge": statBridgePortDesignatedBridge,
       "statBridgePortDesignatedPort": statBridgePortDesignatedPort,
       "statBridgePortTrspFrameIn": statBridgePortTrspFrameIn,
       "statBridgePortTrspFrameOut": statBridgePortTrspFrameOut,
       "statBridgePortTr-SpecRteFrameIn": statBridgePortTr_SpecRteFrameIn,
       "statBridgePortTr-SpecRteFrameOut": statBridgePortTr_SpecRteFrameOut,
       "statBridgePortTr-AllRteFrameIn": statBridgePortTr_AllRteFrameIn,
       "statBridgePortTr-AllRteFrameOut": statBridgePortTr_AllRteFrameOut,
       "statBridgePortTr-SingleRteFrameIn": statBridgePortTr_SingleRteFrameIn,
       "statBridgePortTr-SingleRteFrameOut": statBridgePortTr_SingleRteFrameOut,
       "statBridgePortTr-SegmentMismatch": statBridgePortTr_SegmentMismatch,
       "statBridgePortTr-SegmentDuplicate": statBridgePortTr_SegmentDuplicate,
       "statBridgePortTr-HopCntExceeded": statBridgePortTr_HopCntExceeded,
       "statBridgePortTr-FrmLngExceeded": statBridgePortTr_FrmLngExceeded,
       "statPvcTable": statPvcTable,
       "statPvcEntry": statPvcEntry,
       "statPvcIndex": statPvcIndex,
       "statPvcProtocol": statPvcProtocol,
       "statPvcMode": statPvcMode,
       "statPvcInfoSignal": statPvcInfoSignal,
       "statPvcSpeed": statPvcSpeed,
       "statPvcState": statPvcState,
       "statPvcMeanTx": statPvcMeanTx,
       "statPvcMeanRx": statPvcMeanRx,
       "statPvcPeakTx": statPvcPeakTx,
       "statPvcPeakRx": statPvcPeakRx,
       "statPvcError": statPvcError,
       "statPvcRestart": statPvcRestart,
       "statPvcFramesTx": statPvcFramesTx,
       "statPvcFramesRx": statPvcFramesRx,
       "statPvcOctetsTx": statPvcOctetsTx,
       "statPvcOctetsRx": statPvcOctetsRx,
       "statPvcBadFrames": statPvcBadFrames,
       "statPvcOvrFrames": statPvcOvrFrames,
       "statPvcBadOctets": statPvcBadOctets,
       "statPvcOvrOctets": statPvcOvrOctets,
       "statPvcDlci": statPvcDlci,
       "statPvcCompErrs": statPvcCompErrs,
       "statPvcChOverflows": statPvcChOverflows,
       "statPvcChAborts": statPvcChAborts,
       "statPvcChSeqErrs": statPvcChSeqErrs,
       "statPvcrRouteTable": statPvcrRouteTable,
       "statPvcrRouteEntry": statPvcrRouteEntry,
       "statPvcrRouteName": statPvcrRouteName,
       "statPvcrRouteValid": statPvcrRouteValid,
       "statPvcrRouteMetric": statPvcrRouteMetric,
       "statPvcrRouteIntrf": statPvcrRouteIntrf,
       "statPvcrRouteNextHop": statPvcrRouteNextHop,
       "statPvcrRouteAge": statPvcrRouteAge,
       "statIfvceTable": statIfvceTable,
       "statIfvceEntry": statIfvceEntry,
       "statIfvceIndex": statIfvceIndex,
       "statIfvceDesc": statIfvceDesc,
       "statIfvceState": statIfvceState,
       "statIfvceProtocol": statIfvceProtocol,
       "statIfvceLastError": statIfvceLastError,
       "statIfvceFaxRate": statIfvceFaxRate,
       "statIfvceFaxMode": statIfvceFaxMode,
       "statIfvceOverruns": statIfvceOverruns,
       "statIfvceUnderruns": statIfvceUnderruns,
       "statIfvceDvcPortInUse": statIfvceDvcPortInUse,
       "statSystem": statSystem,
       "statSystemAlarmNumber": statSystemAlarmNumber,
       "statSystemMeanCompRate": statSystemMeanCompRate,
       "statSystemMeanDecompRate": statSystemMeanDecompRate,
       "statSystemPeakCompRate": statSystemPeakCompRate,
       "statSystemPeakDecompRate": statSystemPeakDecompRate,
       "statSystemSa": statSystemSa,
       "statSystemSp": statSystemSp,
       "statSystemNa": statSystemNa,
       "statSystemBia": statSystemBia,
       "statSystemTr-Nan": statSystemTr_Nan,
       "statSystemResetCounters": statSystemResetCounters,
       "statSystemClearAlarms": statSystemClearAlarms,
       "statSystemClearErrorLed": statSystemClearErrorLed,
       "statBootp": statBootp,
       "statBootpNbRequestReceived": statBootpNbRequestReceived,
       "statBootpNbRequestSend": statBootpNbRequestSend,
       "statBootpNbReplyReceived": statBootpNbReplyReceived,
       "statBootpNbReplySend": statBootpNbReplySend,
       "statBootpReplyWithInvalidGiaddr": statBootpReplyWithInvalidGiaddr,
       "statBootpHopsLimitExceed": statBootpHopsLimitExceed,
       "statBootpRequestReceivedOnPortBootpc": statBootpRequestReceivedOnPortBootpc,
       "statBootpReplyReceivedOnPortBootpc": statBootpReplyReceivedOnPortBootpc,
       "statBootpInvalidOpCodeField": statBootpInvalidOpCodeField,
       "statBootpCannotRouteFrame": statBootpCannotRouteFrame,
       "statBootpFrameTooSmallToBeABootpFrame": statBootpFrameTooSmallToBeABootpFrame,
       "statBootpCannotReceiveAndForwardOnTheSamePort": statBootpCannotReceiveAndForwardOnTheSamePort,
       "statGrp": statGrp,
       "statGrpNumber": statGrpNumber,
       "statGrpTable": statGrpTable,
       "statGrpEntry": statGrpEntry,
       "statGrpIndex": statGrpIndex,
       "statGrpDestName": statGrpDestName,
       "statGrpOutOfSeqErrs": statGrpOutOfSeqErrs,
       "statGrpSorterTimeouts": statGrpSorterTimeouts,
       "statGrpSorterOverruns": statGrpSorterOverruns,
       "statTimep": statTimep,
       "statTimeNbFrameReceived": statTimeNbFrameReceived,
       "statTimeNbFrameSent": statTimeNbFrameSent,
       "statTimeNbRequestReceived": statTimeNbRequestReceived,
       "statTimeNbReplySent": statTimeNbReplySent,
       "statTimeNbRequestSent": statTimeNbRequestSent,
       "statTimeNbReplyReceived": statTimeNbReplyReceived,
       "statTimeClientRetransmissions": statTimeClientRetransmissions,
       "statTimeClientSyncFailures": statTimeClientSyncFailures,
       "statTimeInvalidLocalIpAddress": statTimeInvalidLocalIpAddress,
       "statTimeInvalidPortNumbers": statTimeInvalidPortNumbers,
       "statQ922counters": statQ922counters,
       "statTxRetransmissions": statTxRetransmissions,
       "statReleaseIndications": statReleaseIndications,
       "statEstablishIndications": statEstablishIndications,
       "statLinkEstablished": statLinkEstablished,
       "statTxIframeQdiscards": statTxIframeQdiscards,
       "statRxframes": statRxframes,
       "statTxframes": statTxframes,
       "statRxBytes": statRxBytes,
       "statTxBytes": statTxBytes,
       "statQ922errors": statQ922errors,
       "statInvalidRxSizes": statInvalidRxSizes,
       "statMissingControlBlocks": statMissingControlBlocks,
       "statRxAcknowledgeExpiry": statRxAcknowledgeExpiry,
       "statTxAcknowledgeExpiry": statTxAcknowledgeExpiry,
       "statQ933counters": statQ933counters,
       "statTxSetupMessages": statTxSetupMessages,
       "statRxSetupMessages": statRxSetupMessages,
       "statTxCallProceedingMessages": statTxCallProceedingMessages,
       "statRxCallProceedingMessages": statRxCallProceedingMessages,
       "statTxConnectMessages": statTxConnectMessages,
       "statRxConnectMessages": statRxConnectMessages,
       "statTxReleaseMessages": statTxReleaseMessages,
       "statRxReleaseMessages": statRxReleaseMessages,
       "statTxReleaseCompleteMessages": statTxReleaseCompleteMessages,
       "statRxReleaseCompleteMessages": statRxReleaseCompleteMessages,
       "statTxDisconnectMessages": statTxDisconnectMessages,
       "statRxDisconnectMessages": statRxDisconnectMessages,
       "statTxStatusMessages": statTxStatusMessages,
       "statRxStatusMessages": statRxStatusMessages,
       "statTxStatusEnquiryMessages": statTxStatusEnquiryMessages,
       "statRxStatusEnquiryMessages": statRxStatusEnquiryMessages,
       "statProtocolTimeouts": statProtocolTimeouts,
       "statSvcTable": statSvcTable,
       "statSvcEntry": statSvcEntry,
       "statSvcIndex": statSvcIndex,
       "statSvcProtocol": statSvcProtocol,
       "statSvcMode": statSvcMode,
       "statSvcInfoSignal": statSvcInfoSignal,
       "statSvcSpeed": statSvcSpeed,
       "statSvcState": statSvcState,
       "statSvcMeanTx": statSvcMeanTx,
       "statSvcMeanRx": statSvcMeanRx,
       "statSvcPeakTx": statSvcPeakTx,
       "statSvcPeakRx": statSvcPeakRx,
       "statSvcError": statSvcError,
       "statSvcRestart": statSvcRestart,
       "statSvcFramesTx": statSvcFramesTx,
       "statSvcFramesRx": statSvcFramesRx,
       "statSvcOctetsTx": statSvcOctetsTx,
       "statSvcOctetsRx": statSvcOctetsRx,
       "statSvcBadFrames": statSvcBadFrames,
       "statSvcOvrFrames": statSvcOvrFrames,
       "statSvcBadOctets": statSvcBadOctets,
       "statSvcOvrOctets": statSvcOvrOctets,
       "statSvcDlci": statSvcDlci,
       "statIfcemTable": statIfcemTable,
       "statIfcemEntry": statIfcemEntry,
       "statIfcemIndex": statIfcemIndex,
       "statIfcemDesc": statIfcemDesc,
       "statIfcemClockState": statIfcemClockState,
       "intf": intf,
       "intfNumber": intfNumber,
       "intfTable": intfTable,
       "intfEntry": intfEntry,
       "intfIndex": intfIndex,
       "intfDesc": intfDesc,
       "intfType": intfType,
       "intfNumInType": intfNumInType,
       "intfSlot": intfSlot,
       "intfSlotType": intfSlotType,
       "intfNumInSlot": intfNumInSlot,
       "intfModuleType": intfModuleType,
       "slot": slot,
       "intfSlotNumber": intfSlotNumber,
       "slotPortInSlotTable": slotPortInSlotTable,
       "slotPortInSlotEntry": slotPortInSlotEntry,
       "slotSlot": slotSlot,
       "slotPortInSlot": slotPortInSlot,
       "slotIfIndex": slotIfIndex,
       "ipaddr": ipaddr,
       "ipaddrNr": ipaddrNr,
       "ipaddrTable": ipaddrTable,
       "ipaddrEntry": ipaddrEntry,
       "ipaddrIndex": ipaddrIndex,
       "ipaddrAddr": ipaddrAddr,
       "ipaddrType": ipaddrType,
       "ipaddrIfIndex": ipaddrIfIndex,
       "bootp": bootp,
       "bootpEnable": bootpEnable,
       "bootpMaxHops": bootpMaxHops,
       "bootpIpDestAddr1": bootpIpDestAddr1,
       "bootpIpDestAddr2": bootpIpDestAddr2,
       "bootpIpDestAddr3": bootpIpDestAddr3,
       "bootpIpDestAddr4": bootpIpDestAddr4,
       "proxy": proxy,
       "proxyNumber": proxyNumber,
       "proxyTable": proxyTable,
       "proxyEntry": proxyEntry,
       "proxyIndex": proxyIndex,
       "proxyComm": proxyComm,
       "proxyIpAddr": proxyIpAddr,
       "proxyIpMask": proxyIpMask,
       "proxyTrapIpAddr": proxyTrapIpAddr,
       "proxyDefaultGateway": proxyDefaultGateway,
       "timep": timep,
       "timepTimeZoneSign": timepTimeZoneSign,
       "timepTimeZone": timepTimeZone,
       "timepDaylightSaving": timepDaylightSaving,
       "timepServerProtocol": timepServerProtocol,
       "timepClientProtocol": timepClientProtocol,
       "timepServerIpAddress": timepServerIpAddress,
       "timepClientUpdateInterval": timepClientUpdateInterval,
       "timepClientUdpTimeout": timepClientUdpTimeout,
       "timepClientUdpRetransmissions": timepClientUdpRetransmissions,
       "timepGetServerTimeNow": timepGetServerTimeNow}
)
