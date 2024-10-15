# SNMP MIB module (CPIWF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPIWF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:10 2024
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

cpIwfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfLoopEmulationService_ObjectIdentity = ObjectIdentity
atmfLoopEmulationService = _AtmfLoopEmulationService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 10)
)
_CpIwfMIBObjects_ObjectIdentity = ObjectIdentity
cpIwfMIBObjects = _CpIwfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1)
)
_CpIwf_ObjectIdentity = ObjectIdentity
cpIwf = _CpIwf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1)
)
_CpIwfVpi_Type = Integer32
_CpIwfVpi_Object = MibScalar
cpIwfVpi = _CpIwfVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 1),
    _CpIwfVpi_Type()
)
cpIwfVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfVpi.setStatus("current")
_CpIwfVci_Type = Integer32
_CpIwfVci_Object = MibScalar
cpIwfVci = _CpIwfVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 2),
    _CpIwfVci_Type()
)
cpIwfVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfVci.setStatus("current")


class _CpIwfEchoCancellationSupport_Type(Integer32):
    """Custom type cpIwfEchoCancellationSupport based on Integer32"""
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


_CpIwfEchoCancellationSupport_Type.__name__ = "Integer32"
_CpIwfEchoCancellationSupport_Object = MibScalar
cpIwfEchoCancellationSupport = _CpIwfEchoCancellationSupport_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 3),
    _CpIwfEchoCancellationSupport_Type()
)
cpIwfEchoCancellationSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfEchoCancellationSupport.setStatus("current")
_CpIwfNumPotsPorts_Type = Integer32
_CpIwfNumPotsPorts_Object = MibScalar
cpIwfNumPotsPorts = _CpIwfNumPotsPorts_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 4),
    _CpIwfNumPotsPorts_Type()
)
cpIwfNumPotsPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfNumPotsPorts.setStatus("current")
_CpIwfNumIsdnBriPorts_Type = Integer32
_CpIwfNumIsdnBriPorts_Object = MibScalar
cpIwfNumIsdnBriPorts = _CpIwfNumIsdnBriPorts_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 5),
    _CpIwfNumIsdnBriPorts_Type()
)
cpIwfNumIsdnBriPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfNumIsdnBriPorts.setStatus("current")


class _CpIwfTimingReference_Type(Integer32):
    """Custom type cpIwfTimingReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptiveVoice", 2),
          ("freeRun", 3),
          ("ntr", 1))
    )


_CpIwfTimingReference_Type.__name__ = "Integer32"
_CpIwfTimingReference_Object = MibScalar
cpIwfTimingReference = _CpIwfTimingReference_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 6),
    _CpIwfTimingReference_Type()
)
cpIwfTimingReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfTimingReference.setStatus("current")


class _CpIwfPotsPortEncodingSelectionMode_Type(Integer32):
    """Custom type cpIwfPotsPortEncodingSelectionMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 1),
          ("masterSlave", 2))
    )


_CpIwfPotsPortEncodingSelectionMode_Type.__name__ = "Integer32"
_CpIwfPotsPortEncodingSelectionMode_Object = MibScalar
cpIwfPotsPortEncodingSelectionMode = _CpIwfPotsPortEncodingSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 7),
    _CpIwfPotsPortEncodingSelectionMode_Type()
)
cpIwfPotsPortEncodingSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfPotsPortEncodingSelectionMode.setStatus("current")


class _CpIwfIsdnBriPortEncodingSelectionMode_Type(Integer32):
    """Custom type cpIwfIsdnBriPortEncodingSelectionMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 1),
          ("masterSlave", 2))
    )


_CpIwfIsdnBriPortEncodingSelectionMode_Type.__name__ = "Integer32"
_CpIwfIsdnBriPortEncodingSelectionMode_Object = MibScalar
cpIwfIsdnBriPortEncodingSelectionMode = _CpIwfIsdnBriPortEncodingSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 8),
    _CpIwfIsdnBriPortEncodingSelectionMode_Type()
)
cpIwfIsdnBriPortEncodingSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortEncodingSelectionMode.setStatus("current")


class _CpIwfElcpAndPstnChannelBandwidth_Type(Integer32):
    """Custom type cpIwfElcpAndPstnChannelBandwidth based on Integer32"""
    defaultValue = 64000


_CpIwfElcpAndPstnChannelBandwidth_Object = MibScalar
cpIwfElcpAndPstnChannelBandwidth = _CpIwfElcpAndPstnChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 9),
    _CpIwfElcpAndPstnChannelBandwidth_Type()
)
cpIwfElcpAndPstnChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfElcpAndPstnChannelBandwidth.setStatus("current")


class _CpIwfAdminStatus_Type(Integer32):
    """Custom type cpIwfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("shuttingDown", 3),
          ("testing", 4),
          ("up", 1))
    )


_CpIwfAdminStatus_Type.__name__ = "Integer32"
_CpIwfAdminStatus_Object = MibScalar
cpIwfAdminStatus = _CpIwfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 10),
    _CpIwfAdminStatus_Type()
)
cpIwfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfAdminStatus.setStatus("current")


class _CpIwfOperStatus_Type(Integer32):
    """Custom type cpIwfOperStatus based on Integer32"""
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
          ("testing", 3),
          ("up", 1))
    )


_CpIwfOperStatus_Type.__name__ = "Integer32"
_CpIwfOperStatus_Object = MibScalar
cpIwfOperStatus = _CpIwfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 11),
    _CpIwfOperStatus_Type()
)
cpIwfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfOperStatus.setStatus("current")


class _CpIwfRestart_Type(Integer32):
    """Custom type cpIwfRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coldStart", 3),
          ("started", 1),
          ("warmStart", 2))
    )


_CpIwfRestart_Type.__name__ = "Integer32"
_CpIwfRestart_Object = MibScalar
cpIwfRestart = _CpIwfRestart_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 12),
    _CpIwfRestart_Type()
)
cpIwfRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfRestart.setStatus("current")


class _CpIwfTestType_Type(Integer32):
    """Custom type cpIwfTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("selfTest", 1)
    )


_CpIwfTestType_Type.__name__ = "Integer32"
_CpIwfTestType_Object = MibScalar
cpIwfTestType = _CpIwfTestType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 13),
    _CpIwfTestType_Type()
)
cpIwfTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfTestType.setStatus("current")


class _CpIwfTestResult_Type(Integer32):
    """Custom type cpIwfTestResult based on Integer32"""
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
          ("inProgress", 4),
          ("null", 1),
          ("success", 2))
    )


_CpIwfTestResult_Type.__name__ = "Integer32"
_CpIwfTestResult_Object = MibScalar
cpIwfTestResult = _CpIwfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 14),
    _CpIwfTestResult_Type()
)
cpIwfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfTestResult.setStatus("current")


class _CpIwfTestResultText_Type(OctetString):
    """Custom type cpIwfTestResultText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpIwfTestResultText_Type.__name__ = "OctetString"
_CpIwfTestResultText_Object = MibScalar
cpIwfTestResultText = _CpIwfTestResultText_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 15),
    _CpIwfTestResultText_Type()
)
cpIwfTestResultText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfTestResultText.setStatus("current")


class _CpIwfPlayoutBufferDepth_Type(Integer32):
    """Custom type cpIwfPlayoutBufferDepth based on Integer32"""
    defaultValue = 20


_CpIwfPlayoutBufferDepth_Object = MibScalar
cpIwfPlayoutBufferDepth = _CpIwfPlayoutBufferDepth_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 16),
    _CpIwfPlayoutBufferDepth_Type()
)
cpIwfPlayoutBufferDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfPlayoutBufferDepth.setStatus("current")


class _CpIwfImpairmentInterval_Type(Integer32):
    """Custom type cpIwfImpairmentInterval based on Integer32"""
    defaultValue = 15


_CpIwfImpairmentInterval_Object = MibScalar
cpIwfImpairmentInterval = _CpIwfImpairmentInterval_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 17),
    _CpIwfImpairmentInterval_Type()
)
cpIwfImpairmentInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfImpairmentInterval.setStatus("current")


class _CpIwfImpairmentThreshold_Type(Integer32):
    """Custom type cpIwfImpairmentThreshold based on Integer32"""
    defaultValue = 0


_CpIwfImpairmentThreshold_Object = MibScalar
cpIwfImpairmentThreshold = _CpIwfImpairmentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 18),
    _CpIwfImpairmentThreshold_Type()
)
cpIwfImpairmentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfImpairmentThreshold.setStatus("current")


class _CpIwfV5PSTNProtocolVariant_Type(Integer32):
    """Custom type cpIwfV5PSTNProtocolVariant based on Integer32"""
    defaultValue = 44


_CpIwfV5PSTNProtocolVariant_Object = MibScalar
cpIwfV5PSTNProtocolVariant = _CpIwfV5PSTNProtocolVariant_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 19),
    _CpIwfV5PSTNProtocolVariant_Type()
)
cpIwfV5PSTNProtocolVariant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfV5PSTNProtocolVariant.setStatus("current")


class _CpIwfMwdForRestart_Type(Integer32):
    """Custom type cpIwfMwdForRestart based on Integer32"""
    defaultValue = 600


_CpIwfMwdForRestart_Object = MibScalar
cpIwfMwdForRestart = _CpIwfMwdForRestart_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 20),
    _CpIwfMwdForRestart_Type()
)
cpIwfMwdForRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfMwdForRestart.setStatus("current")


class _CpIwfEocBandwidth_Type(Integer32):
    """Custom type cpIwfEocBandwidth based on Integer32"""
    defaultValue = 32000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 640000),
    )


_CpIwfEocBandwidth_Type.__name__ = "Integer32"
_CpIwfEocBandwidth_Object = MibScalar
cpIwfEocBandwidth = _CpIwfEocBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 21),
    _CpIwfEocBandwidth_Type()
)
cpIwfEocBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfEocBandwidth.setStatus("current")


class _CpIwfCurrentConfig_Type(Integer32):
    """Custom type cpIwfCurrentConfig based on Integer32"""
    defaultValue = 0


_CpIwfCurrentConfig_Object = MibScalar
cpIwfCurrentConfig = _CpIwfCurrentConfig_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 22),
    _CpIwfCurrentConfig_Type()
)
cpIwfCurrentConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfCurrentConfig.setStatus("current")


class _CpIwfTrapGeneration_Type(Integer32):
    """Custom type cpIwfTrapGeneration based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled-all", 2),
          ("disabled-except-coldStart", 3),
          ("enabled", 1))
    )


_CpIwfTrapGeneration_Type.__name__ = "Integer32"
_CpIwfTrapGeneration_Object = MibScalar
cpIwfTrapGeneration = _CpIwfTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 23),
    _CpIwfTrapGeneration_Type()
)
cpIwfTrapGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpIwfTrapGeneration.setStatus("current")


class _CpIwfVendorName_Type(OctetString):
    """Custom type cpIwfVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpIwfVendorName_Type.__name__ = "OctetString"
_CpIwfVendorName_Object = MibScalar
cpIwfVendorName = _CpIwfVendorName_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 24),
    _CpIwfVendorName_Type()
)
cpIwfVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfVendorName.setStatus("current")


class _CpIwfDeviceType_Type(OctetString):
    """Custom type cpIwfDeviceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpIwfDeviceType_Type.__name__ = "OctetString"
_CpIwfDeviceType_Object = MibScalar
cpIwfDeviceType = _CpIwfDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 25),
    _CpIwfDeviceType_Type()
)
cpIwfDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfDeviceType.setStatus("current")


class _CpIwfHardwareVersion_Type(OctetString):
    """Custom type cpIwfHardwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpIwfHardwareVersion_Type.__name__ = "OctetString"
_CpIwfHardwareVersion_Object = MibScalar
cpIwfHardwareVersion = _CpIwfHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 26),
    _CpIwfHardwareVersion_Type()
)
cpIwfHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfHardwareVersion.setStatus("current")


class _CpIwfSoftwareVersion_Type(OctetString):
    """Custom type cpIwfSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpIwfSoftwareVersion_Type.__name__ = "OctetString"
_CpIwfSoftwareVersion_Object = MibScalar
cpIwfSoftwareVersion = _CpIwfSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 1, 27),
    _CpIwfSoftwareVersion_Type()
)
cpIwfSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfSoftwareVersion.setStatus("current")
_CpIwfAal2Profile_ObjectIdentity = ObjectIdentity
cpIwfAal2Profile = _CpIwfAal2Profile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 2)
)


class _Aal2ApplicationIdentifier_Type(Integer32):
    """Custom type aal2ApplicationIdentifier based on Integer32"""
    defaultHexValue = 10


_Aal2ApplicationIdentifier_Object = MibScalar
aal2ApplicationIdentifier = _Aal2ApplicationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 2, 1),
    _Aal2ApplicationIdentifier_Type()
)
aal2ApplicationIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2ApplicationIdentifier.setStatus("current")


class _Aal2CpsMaxMultiplexedChannels_Type(Integer32):
    """Custom type aal2CpsMaxMultiplexedChannels based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Aal2CpsMaxMultiplexedChannels_Type.__name__ = "Integer32"
_Aal2CpsMaxMultiplexedChannels_Object = MibScalar
aal2CpsMaxMultiplexedChannels = _Aal2CpsMaxMultiplexedChannels_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 2, 2),
    _Aal2CpsMaxMultiplexedChannels_Type()
)
aal2CpsMaxMultiplexedChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2CpsMaxMultiplexedChannels.setStatus("current")


class _Aal2CpsMaxSDULength_Type(Integer32):
    """Custom type aal2CpsMaxSDULength based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45, 45),
        ValueRangeConstraint(64, 64),
    )


_Aal2CpsMaxSDULength_Type.__name__ = "Integer32"
_Aal2CpsMaxSDULength_Object = MibScalar
aal2CpsMaxSDULength = _Aal2CpsMaxSDULength_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 2, 3),
    _Aal2CpsMaxSDULength_Type()
)
aal2CpsMaxSDULength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2CpsMaxSDULength.setStatus("current")


class _Aal2CpsCIDLowerLimit_Type(Integer32):
    """Custom type aal2CpsCIDLowerLimit based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 223),
    )


_Aal2CpsCIDLowerLimit_Type.__name__ = "Integer32"
_Aal2CpsCIDLowerLimit_Object = MibScalar
aal2CpsCIDLowerLimit = _Aal2CpsCIDLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 2, 4),
    _Aal2CpsCIDLowerLimit_Type()
)
aal2CpsCIDLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2CpsCIDLowerLimit.setStatus("current")


class _Aal2CpsCIDUpperLimit_Type(Integer32):
    """Custom type aal2CpsCIDUpperLimit based on Integer32"""
    defaultValue = 223

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 223),
    )


_Aal2CpsCIDUpperLimit_Type.__name__ = "Integer32"
_Aal2CpsCIDUpperLimit_Object = MibScalar
aal2CpsCIDUpperLimit = _Aal2CpsCIDUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 2, 5),
    _Aal2CpsCIDUpperLimit_Type()
)
aal2CpsCIDUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2CpsCIDUpperLimit.setStatus("current")


class _Aal2CpsOptimisation_Type(Integer32):
    """Custom type aal2CpsOptimisation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multipleCpsPacketsPerCpsPduWithOverlap", 2),
          ("singleCpsPacketPerCpsPduNoOverlap", 1))
    )


_Aal2CpsOptimisation_Type.__name__ = "Integer32"
_Aal2CpsOptimisation_Object = MibScalar
aal2CpsOptimisation = _Aal2CpsOptimisation_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 2, 6),
    _Aal2CpsOptimisation_Type()
)
aal2CpsOptimisation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2CpsOptimisation.setStatus("current")


class _Aal2CpsTimerCuValue_Type(Integer32):
    """Custom type aal2CpsTimerCuValue based on Integer32"""
    defaultValue = 0


_Aal2CpsTimerCuValue_Object = MibScalar
aal2CpsTimerCuValue = _Aal2CpsTimerCuValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 2, 7),
    _Aal2CpsTimerCuValue_Type()
)
aal2CpsTimerCuValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2CpsTimerCuValue.setStatus("current")


class _Aal2SscsFaxDemodulationTransport_Type(Integer32):
    """Custom type aal2SscsFaxDemodulationTransport based on Integer32"""
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


_Aal2SscsFaxDemodulationTransport_Type.__name__ = "Integer32"
_Aal2SscsFaxDemodulationTransport_Object = MibScalar
aal2SscsFaxDemodulationTransport = _Aal2SscsFaxDemodulationTransport_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 2, 8),
    _Aal2SscsFaxDemodulationTransport_Type()
)
aal2SscsFaxDemodulationTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2SscsFaxDemodulationTransport.setStatus("current")


class _Aal2SscsDtmfDigitPacketTransport_Type(Integer32):
    """Custom type aal2SscsDtmfDigitPacketTransport based on Integer32"""
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


_Aal2SscsDtmfDigitPacketTransport_Type.__name__ = "Integer32"
_Aal2SscsDtmfDigitPacketTransport_Object = MibScalar
aal2SscsDtmfDigitPacketTransport = _Aal2SscsDtmfDigitPacketTransport_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 2, 9),
    _Aal2SscsDtmfDigitPacketTransport_Type()
)
aal2SscsDtmfDigitPacketTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2SscsDtmfDigitPacketTransport.setStatus("current")


class _Aal2SscsPcmEncoding_Type(Integer32):
    """Custom type aal2SscsPcmEncoding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 1),
          ("uLaw", 2))
    )


_Aal2SscsPcmEncoding_Type.__name__ = "Integer32"
_Aal2SscsPcmEncoding_Object = MibScalar
aal2SscsPcmEncoding = _Aal2SscsPcmEncoding_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 2, 10),
    _Aal2SscsPcmEncoding_Type()
)
aal2SscsPcmEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2SscsPcmEncoding.setStatus("current")


class _Aal2SscsMaxSssarSduLength_Type(Integer32):
    """Custom type aal2SscsMaxSssarSduLength based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(493, 65568),
    )


_Aal2SscsMaxSssarSduLength_Type.__name__ = "Integer32"
_Aal2SscsMaxSssarSduLength_Object = MibScalar
aal2SscsMaxSssarSduLength = _Aal2SscsMaxSssarSduLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 2, 11),
    _Aal2SscsMaxSssarSduLength_Type()
)
aal2SscsMaxSssarSduLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2SscsMaxSssarSduLength.setStatus("current")


class _Aal2SscsProfileSource_Type(Integer32):
    """Custom type aal2SscsProfileSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ituT", 1),
          ("other", 2))
    )


_Aal2SscsProfileSource_Type.__name__ = "Integer32"
_Aal2SscsProfileSource_Object = MibScalar
aal2SscsProfileSource = _Aal2SscsProfileSource_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 2, 12),
    _Aal2SscsProfileSource_Type()
)
aal2SscsProfileSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2SscsProfileSource.setStatus("current")


class _Aal2SscsPredefinedProfileIdentifier_Type(Integer32):
    """Custom type aal2SscsPredefinedProfileIdentifier based on Integer32"""
    defaultValue = 9


_Aal2SscsPredefinedProfileIdentifier_Object = MibScalar
aal2SscsPredefinedProfileIdentifier = _Aal2SscsPredefinedProfileIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 2, 13),
    _Aal2SscsPredefinedProfileIdentifier_Type()
)
aal2SscsPredefinedProfileIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2SscsPredefinedProfileIdentifier.setStatus("current")


class _Aal2SscsIeeeOui_Type(Integer32):
    """Custom type aal2SscsIeeeOui based on Integer32"""
    defaultHexValue = 41022


_Aal2SscsIeeeOui_Object = MibScalar
aal2SscsIeeeOui = _Aal2SscsIeeeOui_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 2, 14),
    _Aal2SscsIeeeOui_Type()
)
aal2SscsIeeeOui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2SscsIeeeOui.setStatus("current")


class _Aal2SscsSsSarAssemblyTimerValue_Type(Integer32):
    """Custom type aal2SscsSsSarAssemblyTimerValue based on Integer32"""
    defaultValue = 2147483647


_Aal2SscsSsSarAssemblyTimerValue_Object = MibScalar
aal2SscsSsSarAssemblyTimerValue = _Aal2SscsSsSarAssemblyTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 2, 15),
    _Aal2SscsSsSarAssemblyTimerValue_Type()
)
aal2SscsSsSarAssemblyTimerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2SscsSsSarAssemblyTimerValue.setStatus("current")
_CpIwfPotsPortTable_Object = MibTable
cpIwfPotsPortTable = _CpIwfPotsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cpIwfPotsPortTable.setStatus("current")
_CpIwfPotsPortEntry_Object = MibTableRow
cpIwfPotsPortEntry = _CpIwfPotsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 3, 1)
)
cpIwfPotsPortEntry.setIndexNames(
    (0, "CPIWF-MIB", "potsPortNumber"),
)
if mibBuilder.loadTexts:
    cpIwfPotsPortEntry.setStatus("current")
_PotsPortNumber_Type = Integer32
_PotsPortNumber_Object = MibTableColumn
potsPortNumber = _PotsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 3, 1, 1),
    _PotsPortNumber_Type()
)
potsPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    potsPortNumber.setStatus("current")
_PotsPhysicalPort_Type = Integer32
_PotsPhysicalPort_Object = MibTableColumn
potsPhysicalPort = _PotsPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 3, 1, 2),
    _PotsPhysicalPort_Type()
)
potsPhysicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    potsPhysicalPort.setStatus("current")


class _Aal2ChannelId_Type(Integer32):
    """Custom type aal2ChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_Aal2ChannelId_Type.__name__ = "Integer32"
_Aal2ChannelId_Object = MibTableColumn
aal2ChannelId = _Aal2ChannelId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 3, 1, 3),
    _Aal2ChannelId_Type()
)
aal2ChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2ChannelId.setStatus("current")


class _PotsPortTestType_Type(Integer32):
    """Custom type potsPortTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aal2Loopback", 3),
          ("codecLoopback", 2),
          ("none", 1))
    )


_PotsPortTestType_Type.__name__ = "Integer32"
_PotsPortTestType_Object = MibTableColumn
potsPortTestType = _PotsPortTestType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 3, 1, 4),
    _PotsPortTestType_Type()
)
potsPortTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    potsPortTestType.setStatus("current")


class _SignalingMethod_Type(Integer32):
    """Custom type signalingMethod based on Integer32"""
    defaultValue = 1

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
        *(("ddiPbxStart", 4),
          ("groundStart", 3),
          ("loopReverseBattery", 2),
          ("loopStart", 1))
    )


_SignalingMethod_Type.__name__ = "Integer32"
_SignalingMethod_Object = MibTableColumn
signalingMethod = _SignalingMethod_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 3, 1, 5),
    _SignalingMethod_Type()
)
signalingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingMethod.setStatus("current")


class _PotsPortLabel_Type(OctetString):
    """Custom type potsPortLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PotsPortLabel_Type.__name__ = "OctetString"
_PotsPortLabel_Object = MibTableColumn
potsPortLabel = _PotsPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 3, 1, 6),
    _PotsPortLabel_Type()
)
potsPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    potsPortLabel.setStatus("current")
_CpIwfIsdnBriPortTable_Object = MibTable
cpIwfIsdnBriPortTable = _CpIwfIsdnBriPortTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortTable.setStatus("current")
_CpIwfIsdnBriPortEntry_Object = MibTableRow
cpIwfIsdnBriPortEntry = _CpIwfIsdnBriPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 4, 1)
)
cpIwfIsdnBriPortEntry.setIndexNames(
    (0, "CPIWF-MIB", "isdnBriPortNumber"),
)
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortEntry.setStatus("current")
_IsdnBriPortNumber_Type = Integer32
_IsdnBriPortNumber_Object = MibTableColumn
isdnBriPortNumber = _IsdnBriPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 4, 1, 1),
    _IsdnBriPortNumber_Type()
)
isdnBriPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    isdnBriPortNumber.setStatus("current")
_IsdnBriPhysicalPort_Type = Integer32
_IsdnBriPhysicalPort_Object = MibTableColumn
isdnBriPhysicalPort = _IsdnBriPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 4, 1, 2),
    _IsdnBriPhysicalPort_Type()
)
isdnBriPhysicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnBriPhysicalPort.setStatus("current")


class _Aal2ChannelIdD_Type(Integer32):
    """Custom type aal2ChannelIdD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_Aal2ChannelIdD_Type.__name__ = "Integer32"
_Aal2ChannelIdD_Object = MibTableColumn
aal2ChannelIdD = _Aal2ChannelIdD_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 4, 1, 3),
    _Aal2ChannelIdD_Type()
)
aal2ChannelIdD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2ChannelIdD.setStatus("current")


class _Aal2ChannelIdB1_Type(Integer32):
    """Custom type aal2ChannelIdB1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_Aal2ChannelIdB1_Type.__name__ = "Integer32"
_Aal2ChannelIdB1_Object = MibTableColumn
aal2ChannelIdB1 = _Aal2ChannelIdB1_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 4, 1, 4),
    _Aal2ChannelIdB1_Type()
)
aal2ChannelIdB1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2ChannelIdB1.setStatus("current")


class _Aal2ChannelIdB2_Type(Integer32):
    """Custom type aal2ChannelIdB2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_Aal2ChannelIdB2_Type.__name__ = "Integer32"
_Aal2ChannelIdB2_Object = MibTableColumn
aal2ChannelIdB2 = _Aal2ChannelIdB2_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 4, 1, 5),
    _Aal2ChannelIdB2_Type()
)
aal2ChannelIdB2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aal2ChannelIdB2.setStatus("current")


class _IsdnBriPortLabel_Type(OctetString):
    """Custom type isdnBriPortLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IsdnBriPortLabel_Type.__name__ = "OctetString"
_IsdnBriPortLabel_Object = MibTableColumn
isdnBriPortLabel = _IsdnBriPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 4, 1, 6),
    _IsdnBriPortLabel_Type()
)
isdnBriPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnBriPortLabel.setStatus("current")


class _IsdnBriPortTestType_Type(Integer32):
    """Custom type isdnBriPortTestType based on Integer32"""
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
        *(("b1ChannelAal2Loopback", 6),
          ("b1ChannelPhysicalPortLoopback", 3),
          ("b2ChannelAal2Loopback", 7),
          ("b2ChannelPhysicalPortLoopback", 4),
          ("dChannelAal2Loopback", 5),
          ("dChannelPhysicalPortLoopback", 2),
          ("physicalPortLoopback", 1))
    )


_IsdnBriPortTestType_Type.__name__ = "Integer32"
_IsdnBriPortTestType_Object = MibTableColumn
isdnBriPortTestType = _IsdnBriPortTestType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 4, 1, 7),
    _IsdnBriPortTestType_Type()
)
isdnBriPortTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnBriPortTestType.setStatus("current")
_CpIwfAal2Stats_ObjectIdentity = ObjectIdentity
cpIwfAal2Stats = _CpIwfAal2Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6)
)
_Aal2CpsInPkts_Type = Counter32
_Aal2CpsInPkts_Object = MibScalar
aal2CpsInPkts = _Aal2CpsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 1),
    _Aal2CpsInPkts_Type()
)
aal2CpsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2CpsInPkts.setStatus("current")
_Aal2CpsOutPkts_Type = Counter32
_Aal2CpsOutPkts_Object = MibScalar
aal2CpsOutPkts = _Aal2CpsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 2),
    _Aal2CpsOutPkts_Type()
)
aal2CpsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2CpsOutPkts.setStatus("current")
_Aal2CpsParityErrors_Type = Counter32
_Aal2CpsParityErrors_Object = MibScalar
aal2CpsParityErrors = _Aal2CpsParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 3),
    _Aal2CpsParityErrors_Type()
)
aal2CpsParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2CpsParityErrors.setStatus("current")
_Aal2CpsSeqNumErrors_Type = Counter32
_Aal2CpsSeqNumErrors_Object = MibScalar
aal2CpsSeqNumErrors = _Aal2CpsSeqNumErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 4),
    _Aal2CpsSeqNumErrors_Type()
)
aal2CpsSeqNumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2CpsSeqNumErrors.setStatus("current")
_Aal2CpsOsfMismatchErrors_Type = Counter32
_Aal2CpsOsfMismatchErrors_Object = MibScalar
aal2CpsOsfMismatchErrors = _Aal2CpsOsfMismatchErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 5),
    _Aal2CpsOsfMismatchErrors_Type()
)
aal2CpsOsfMismatchErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2CpsOsfMismatchErrors.setStatus("current")
_Aal2CpsOsfErrors_Type = Counter32
_Aal2CpsOsfErrors_Object = MibScalar
aal2CpsOsfErrors = _Aal2CpsOsfErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 6),
    _Aal2CpsOsfErrors_Type()
)
aal2CpsOsfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2CpsOsfErrors.setStatus("current")
_Aal2CpsHecErrors_Type = Counter32
_Aal2CpsHecErrors_Object = MibScalar
aal2CpsHecErrors = _Aal2CpsHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 7),
    _Aal2CpsHecErrors_Type()
)
aal2CpsHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2CpsHecErrors.setStatus("current")
_Aal2CpsOversizedSduErrors_Type = Counter32
_Aal2CpsOversizedSduErrors_Object = MibScalar
aal2CpsOversizedSduErrors = _Aal2CpsOversizedSduErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 8),
    _Aal2CpsOversizedSduErrors_Type()
)
aal2CpsOversizedSduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2CpsOversizedSduErrors.setStatus("current")
_Aal2CpsReassemblyErrors_Type = Counter32
_Aal2CpsReassemblyErrors_Object = MibScalar
aal2CpsReassemblyErrors = _Aal2CpsReassemblyErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 9),
    _Aal2CpsReassemblyErrors_Type()
)
aal2CpsReassemblyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2CpsReassemblyErrors.setStatus("current")
_Aal2CpsHecOverlapErrors_Type = Counter32
_Aal2CpsHecOverlapErrors_Object = MibScalar
aal2CpsHecOverlapErrors = _Aal2CpsHecOverlapErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 10),
    _Aal2CpsHecOverlapErrors_Type()
)
aal2CpsHecOverlapErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2CpsHecOverlapErrors.setStatus("current")
_Aal2CpsUuiErrors_Type = Counter32
_Aal2CpsUuiErrors_Object = MibScalar
aal2CpsUuiErrors = _Aal2CpsUuiErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 11),
    _Aal2CpsUuiErrors_Type()
)
aal2CpsUuiErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2CpsUuiErrors.setStatus("current")
_Aal2CpsCidErrors_Type = Counter32
_Aal2CpsCidErrors_Object = MibScalar
aal2CpsCidErrors = _Aal2CpsCidErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 12),
    _Aal2CpsCidErrors_Type()
)
aal2CpsCidErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2CpsCidErrors.setStatus("current")
_Aal2SscsOversizedSssarSduErrors_Type = Counter32
_Aal2SscsOversizedSssarSduErrors_Object = MibScalar
aal2SscsOversizedSssarSduErrors = _Aal2SscsOversizedSssarSduErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 13),
    _Aal2SscsOversizedSssarSduErrors_Type()
)
aal2SscsOversizedSssarSduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2SscsOversizedSssarSduErrors.setStatus("current")
_Aal2SscsSssarRasTimerExpiryErrors_Type = Counter32
_Aal2SscsSssarRasTimerExpiryErrors_Object = MibScalar
aal2SscsSssarRasTimerExpiryErrors = _Aal2SscsSssarRasTimerExpiryErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 14),
    _Aal2SscsSssarRasTimerExpiryErrors_Type()
)
aal2SscsSssarRasTimerExpiryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2SscsSssarRasTimerExpiryErrors.setStatus("current")
_Aal2SscsUndersizedSstedPduErrors_Type = Counter32
_Aal2SscsUndersizedSstedPduErrors_Object = MibScalar
aal2SscsUndersizedSstedPduErrors = _Aal2SscsUndersizedSstedPduErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 15),
    _Aal2SscsUndersizedSstedPduErrors_Type()
)
aal2SscsUndersizedSstedPduErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2SscsUndersizedSstedPduErrors.setStatus("current")
_Aal2SscsSstedPduLengthMismatchErrors_Type = Counter32
_Aal2SscsSstedPduLengthMismatchErrors_Object = MibScalar
aal2SscsSstedPduLengthMismatchErrors = _Aal2SscsSstedPduLengthMismatchErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 16),
    _Aal2SscsSstedPduLengthMismatchErrors_Type()
)
aal2SscsSstedPduLengthMismatchErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2SscsSstedPduLengthMismatchErrors.setStatus("current")
_Aal2SscsSstedCrcMismatchErrors_Type = Counter32
_Aal2SscsSstedCrcMismatchErrors_Object = MibScalar
aal2SscsSstedCrcMismatchErrors = _Aal2SscsSstedCrcMismatchErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 6, 17),
    _Aal2SscsSstedCrcMismatchErrors_Type()
)
aal2SscsSstedCrcMismatchErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal2SscsSstedCrcMismatchErrors.setStatus("current")
_CpIwfPotsPortStatsTable_Object = MibTable
cpIwfPotsPortStatsTable = _CpIwfPotsPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cpIwfPotsPortStatsTable.setStatus("current")
_CpIwfPotsPortStatsEntry_Object = MibTableRow
cpIwfPotsPortStatsEntry = _CpIwfPotsPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 7, 1)
)
cpIwfPotsPortStatsEntry.setIndexNames(
    (0, "CPIWF-MIB", "potsPortNumber"),
)
if mibBuilder.loadTexts:
    cpIwfPotsPortStatsEntry.setStatus("current")
_CpIwfPotsPortActiveSeconds_Type = Counter32
_CpIwfPotsPortActiveSeconds_Object = MibTableColumn
cpIwfPotsPortActiveSeconds = _CpIwfPotsPortActiveSeconds_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 7, 1, 1),
    _CpIwfPotsPortActiveSeconds_Type()
)
cpIwfPotsPortActiveSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfPotsPortActiveSeconds.setStatus("current")
_CpIwfPotsPortFillerOctets_Type = Counter32
_CpIwfPotsPortFillerOctets_Object = MibTableColumn
cpIwfPotsPortFillerOctets = _CpIwfPotsPortFillerOctets_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 7, 1, 2),
    _CpIwfPotsPortFillerOctets_Type()
)
cpIwfPotsPortFillerOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfPotsPortFillerOctets.setStatus("current")
_CpIwfPotsPortDroppedOctets_Type = Counter32
_CpIwfPotsPortDroppedOctets_Object = MibTableColumn
cpIwfPotsPortDroppedOctets = _CpIwfPotsPortDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 7, 1, 3),
    _CpIwfPotsPortDroppedOctets_Type()
)
cpIwfPotsPortDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfPotsPortDroppedOctets.setStatus("current")
_CpIwfIsdnBriPortStatsTable_Object = MibTable
cpIwfIsdnBriPortStatsTable = _CpIwfIsdnBriPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortStatsTable.setStatus("current")
_CpIwfIsdnBriPortStatsEntry_Object = MibTableRow
cpIwfIsdnBriPortStatsEntry = _CpIwfIsdnBriPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 8, 1)
)
cpIwfIsdnBriPortStatsEntry.setIndexNames(
    (0, "CPIWF-MIB", "isdnBriPortNumber"),
)
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortStatsEntry.setStatus("current")
_CpIwfIsdnBriPortB1ActiveSeconds_Type = Counter32
_CpIwfIsdnBriPortB1ActiveSeconds_Object = MibTableColumn
cpIwfIsdnBriPortB1ActiveSeconds = _CpIwfIsdnBriPortB1ActiveSeconds_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 8, 1, 1),
    _CpIwfIsdnBriPortB1ActiveSeconds_Type()
)
cpIwfIsdnBriPortB1ActiveSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortB1ActiveSeconds.setStatus("current")
_CpIwfIsdnBriPortB1FillerOctets_Type = Counter32
_CpIwfIsdnBriPortB1FillerOctets_Object = MibTableColumn
cpIwfIsdnBriPortB1FillerOctets = _CpIwfIsdnBriPortB1FillerOctets_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 8, 1, 2),
    _CpIwfIsdnBriPortB1FillerOctets_Type()
)
cpIwfIsdnBriPortB1FillerOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortB1FillerOctets.setStatus("current")
_CpIwfIsdnBriPortB1DroppedOctets_Type = Counter32
_CpIwfIsdnBriPortB1DroppedOctets_Object = MibTableColumn
cpIwfIsdnBriPortB1DroppedOctets = _CpIwfIsdnBriPortB1DroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 8, 1, 3),
    _CpIwfIsdnBriPortB1DroppedOctets_Type()
)
cpIwfIsdnBriPortB1DroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortB1DroppedOctets.setStatus("current")
_CpIwfIsdnBriPortB2ActiveSeconds_Type = Counter32
_CpIwfIsdnBriPortB2ActiveSeconds_Object = MibTableColumn
cpIwfIsdnBriPortB2ActiveSeconds = _CpIwfIsdnBriPortB2ActiveSeconds_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 8, 1, 4),
    _CpIwfIsdnBriPortB2ActiveSeconds_Type()
)
cpIwfIsdnBriPortB2ActiveSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortB2ActiveSeconds.setStatus("current")
_CpIwfIsdnBriPortB2FillerOctets_Type = Counter32
_CpIwfIsdnBriPortB2FillerOctets_Object = MibTableColumn
cpIwfIsdnBriPortB2FillerOctets = _CpIwfIsdnBriPortB2FillerOctets_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 8, 1, 5),
    _CpIwfIsdnBriPortB2FillerOctets_Type()
)
cpIwfIsdnBriPortB2FillerOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortB2FillerOctets.setStatus("current")
_CpIwfIsdnBriPortB2DroppedOctets_Type = Counter32
_CpIwfIsdnBriPortB2DroppedOctets_Object = MibTableColumn
cpIwfIsdnBriPortB2DroppedOctets = _CpIwfIsdnBriPortB2DroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 8, 1, 6),
    _CpIwfIsdnBriPortB2DroppedOctets_Type()
)
cpIwfIsdnBriPortB2DroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortB2DroppedOctets.setStatus("current")
_CpIwfUpstreamPhysicalBandwidth_Type = Integer32
_CpIwfUpstreamPhysicalBandwidth_Object = MibScalar
cpIwfUpstreamPhysicalBandwidth = _CpIwfUpstreamPhysicalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 9),
    _CpIwfUpstreamPhysicalBandwidth_Type()
)
cpIwfUpstreamPhysicalBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfUpstreamPhysicalBandwidth.setStatus("current")
_CpIwfDownstreamPhysicalBandwidth_Type = Integer32
_CpIwfDownstreamPhysicalBandwidth_Object = MibScalar
cpIwfDownstreamPhysicalBandwidth = _CpIwfDownstreamPhysicalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 10),
    _CpIwfDownstreamPhysicalBandwidth_Type()
)
cpIwfDownstreamPhysicalBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfDownstreamPhysicalBandwidth.setStatus("current")


class _CpIwfImpairmentPortType_Type(Integer32):
    """Custom type cpIwfImpairmentPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("isdnBriB1", 2),
          ("isdnBriB2", 3),
          ("pots", 1))
    )


_CpIwfImpairmentPortType_Type.__name__ = "Integer32"
_CpIwfImpairmentPortType_Object = MibScalar
cpIwfImpairmentPortType = _CpIwfImpairmentPortType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 11),
    _CpIwfImpairmentPortType_Type()
)
cpIwfImpairmentPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfImpairmentPortType.setStatus("current")


class _CpIwfPortNumber_Type(Integer32):
    """Custom type cpIwfPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_CpIwfPortNumber_Type.__name__ = "Integer32"
_CpIwfPortNumber_Object = MibScalar
cpIwfPortNumber = _CpIwfPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 1, 12),
    _CpIwfPortNumber_Type()
)
cpIwfPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIwfPortNumber.setStatus("current")
_CpIwfMIBNotifications_ObjectIdentity = ObjectIdentity
cpIwfMIBNotifications = _CpIwfMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 2)
)
_CpIwfMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cpIwfMIBNotificationPrefix = _CpIwfMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 2, 0)
)
_CpIwfMIBConformance_ObjectIdentity = ObjectIdentity
cpIwfMIBConformance = _CpIwfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3)
)
_CpIwfMIBCompliances_ObjectIdentity = ObjectIdentity
cpIwfMIBCompliances = _CpIwfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3, 1)
)
_CpIwfMIBGroups_ObjectIdentity = ObjectIdentity
cpIwfMIBGroups = _CpIwfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3, 2)
)

# Managed Objects groups

cpIwfGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3, 2, 1)
)
cpIwfGeneralGroup.setObjects(
      *(("CPIWF-MIB", "cpIwfVpi"),
        ("CPIWF-MIB", "cpIwfVci"),
        ("CPIWF-MIB", "cpIwfTimingReference"),
        ("CPIWF-MIB", "cpIwfEchoCancellationSupport"),
        ("CPIWF-MIB", "cpIwfAdminStatus"),
        ("CPIWF-MIB", "cpIwfOperStatus"),
        ("CPIWF-MIB", "cpIwfRestart"),
        ("CPIWF-MIB", "cpIwfTestType"),
        ("CPIWF-MIB", "cpIwfTestResult"),
        ("CPIWF-MIB", "cpIwfTestResultText"),
        ("CPIWF-MIB", "cpIwfMwdForRestart"),
        ("CPIWF-MIB", "cpIwfEocBandwidth"),
        ("CPIWF-MIB", "cpIwfCurrentConfig"),
        ("CPIWF-MIB", "cpIwfTrapGeneration"),
        ("CPIWF-MIB", "cpIwfVendorName"),
        ("CPIWF-MIB", "cpIwfDeviceType"),
        ("CPIWF-MIB", "cpIwfHardwareVersion"),
        ("CPIWF-MIB", "cpIwfSoftwareVersion"),
        ("CPIWF-MIB", "cpIwfUpstreamPhysicalBandwidth"),
        ("CPIWF-MIB", "cpIwfDownstreamPhysicalBandwidth"),
        ("CPIWF-MIB", "cpIwfPortNumber"))
)
if mibBuilder.loadTexts:
    cpIwfGeneralGroup.setStatus("current")

cpIwfAal2ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3, 2, 2)
)
cpIwfAal2ConfigGroup.setObjects(
      *(("CPIWF-MIB", "aal2ApplicationIdentifier"),
        ("CPIWF-MIB", "aal2CpsMaxMultiplexedChannels"),
        ("CPIWF-MIB", "aal2CpsMaxSDULength"),
        ("CPIWF-MIB", "aal2CpsCIDLowerLimit"),
        ("CPIWF-MIB", "aal2CpsCIDUpperLimit"),
        ("CPIWF-MIB", "aal2CpsOptimisation"),
        ("CPIWF-MIB", "aal2CpsTimerCuValue"),
        ("CPIWF-MIB", "aal2SscsMaxSssarSduLength"),
        ("CPIWF-MIB", "aal2SscsFaxDemodulationTransport"),
        ("CPIWF-MIB", "aal2SscsDtmfDigitPacketTransport"),
        ("CPIWF-MIB", "aal2SscsPcmEncoding"),
        ("CPIWF-MIB", "aal2SscsProfileSource"),
        ("CPIWF-MIB", "aal2SscsPredefinedProfileIdentifier"),
        ("CPIWF-MIB", "aal2SscsIeeeOui"),
        ("CPIWF-MIB", "aal2SscsSsSarAssemblyTimerValue"))
)
if mibBuilder.loadTexts:
    cpIwfAal2ConfigGroup.setStatus("current")

cpIwfPotsPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3, 2, 3)
)
cpIwfPotsPortConfigGroup.setObjects(
      *(("CPIWF-MIB", "cpIwfNumPotsPorts"),
        ("CPIWF-MIB", "cpIwfPotsPortEncodingSelectionMode"),
        ("CPIWF-MIB", "potsPhysicalPort"),
        ("CPIWF-MIB", "potsPortTestType"),
        ("CPIWF-MIB", "signalingMethod"),
        ("CPIWF-MIB", "potsPortLabel"))
)
if mibBuilder.loadTexts:
    cpIwfPotsPortConfigGroup.setStatus("current")

cpIwfIsdnBriPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3, 2, 4)
)
cpIwfIsdnBriPortConfigGroup.setObjects(
      *(("CPIWF-MIB", "cpIwfNumIsdnBriPorts"),
        ("CPIWF-MIB", "cpIwfIsdnBriPortEncodingSelectionMode"),
        ("CPIWF-MIB", "isdnBriPhysicalPort"),
        ("CPIWF-MIB", "isdnBriPortLabel"),
        ("CPIWF-MIB", "isdnBriPortTestType"))
)
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortConfigGroup.setStatus("current")

cpIwfPotsPortCidConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3, 2, 5)
)
cpIwfPotsPortCidConfigGroup.setObjects(
    ("CPIWF-MIB", "aal2ChannelId")
)
if mibBuilder.loadTexts:
    cpIwfPotsPortCidConfigGroup.setStatus("current")

cpIwfIsdnBriPortCidConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3, 2, 6)
)
cpIwfIsdnBriPortCidConfigGroup.setObjects(
      *(("CPIWF-MIB", "aal2ChannelIdD"),
        ("CPIWF-MIB", "aal2ChannelIdB1"),
        ("CPIWF-MIB", "aal2ChannelIdB2"))
)
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortCidConfigGroup.setStatus("current")

cpIwfAal2StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3, 2, 7)
)
cpIwfAal2StatsGroup.setObjects(
      *(("CPIWF-MIB", "aal2CpsInPkts"),
        ("CPIWF-MIB", "aal2CpsOutPkts"),
        ("CPIWF-MIB", "aal2CpsParityErrors"),
        ("CPIWF-MIB", "aal2CpsSeqNumErrors"),
        ("CPIWF-MIB", "aal2CpsOsfMismatchErrors"),
        ("CPIWF-MIB", "aal2CpsOsfErrors"),
        ("CPIWF-MIB", "aal2CpsHecOverlapErrors"),
        ("CPIWF-MIB", "aal2CpsHecErrors"),
        ("CPIWF-MIB", "aal2CpsOversizedSduErrors"),
        ("CPIWF-MIB", "aal2CpsReassemblyErrors"),
        ("CPIWF-MIB", "aal2CpsUuiErrors"),
        ("CPIWF-MIB", "aal2CpsCidErrors"),
        ("CPIWF-MIB", "aal2SscsOversizedSssarSduErrors"),
        ("CPIWF-MIB", "aal2SscsSssarRasTimerExpiryErrors"),
        ("CPIWF-MIB", "aal2SscsUndersizedSstedPduErrors"),
        ("CPIWF-MIB", "aal2SscsSstedPduLengthMismatchErrors"),
        ("CPIWF-MIB", "aal2SscsSstedCrcMismatchErrors"))
)
if mibBuilder.loadTexts:
    cpIwfAal2StatsGroup.setStatus("current")

cpIwfPotsPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3, 2, 8)
)
cpIwfPotsPortStatsGroup.setObjects(
      *(("CPIWF-MIB", "cpIwfPotsPortActiveSeconds"),
        ("CPIWF-MIB", "cpIwfPotsPortFillerOctets"),
        ("CPIWF-MIB", "cpIwfPotsPortDroppedOctets"))
)
if mibBuilder.loadTexts:
    cpIwfPotsPortStatsGroup.setStatus("current")

cpIwfIsdnBriPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3, 2, 9)
)
cpIwfIsdnBriPortStatsGroup.setObjects(
      *(("CPIWF-MIB", "cpIwfIsdnBriPortB1ActiveSeconds"),
        ("CPIWF-MIB", "cpIwfIsdnBriPortB1FillerOctets"),
        ("CPIWF-MIB", "cpIwfIsdnBriPortB1DroppedOctets"),
        ("CPIWF-MIB", "cpIwfIsdnBriPortB2ActiveSeconds"),
        ("CPIWF-MIB", "cpIwfIsdnBriPortB2FillerOctets"),
        ("CPIWF-MIB", "cpIwfIsdnBriPortB2DroppedOctets"))
)
if mibBuilder.loadTexts:
    cpIwfIsdnBriPortStatsGroup.setStatus("current")

cpIwfElcpPstnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3, 2, 10)
)
cpIwfElcpPstnGroup.setObjects(
      *(("CPIWF-MIB", "cpIwfV5PSTNProtocolVariant"),
        ("CPIWF-MIB", "cpIwfElcpAndPstnChannelBandwidth"))
)
if mibBuilder.loadTexts:
    cpIwfElcpPstnGroup.setStatus("current")

cpIwfPlayoutBufferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3, 2, 11)
)
cpIwfPlayoutBufferGroup.setObjects(
      *(("CPIWF-MIB", "cpIwfPlayoutBufferDepth"),
        ("CPIWF-MIB", "cpIwfImpairmentInterval"),
        ("CPIWF-MIB", "cpIwfImpairmentThreshold"),
        ("CPIWF-MIB", "cpIwfImpairmentPortType"))
)
if mibBuilder.loadTexts:
    cpIwfPlayoutBufferGroup.setStatus("current")


# Notification objects

cpIwfInsufficientPhysicalBandwidth = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 2, 0, 1)
)
cpIwfInsufficientPhysicalBandwidth.setObjects(
      *(("CPIWF-MIB", "cpIwfUpstreamPhysicalBandwidth"),
        ("CPIWF-MIB", "cpIwfDownstreamPhysicalBandwidth"))
)
if mibBuilder.loadTexts:
    cpIwfInsufficientPhysicalBandwidth.setStatus(
        "current"
    )

cpIwfExcessImpairment = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 2, 0, 2)
)
cpIwfExcessImpairment.setObjects(
      *(("CPIWF-MIB", "cpIwfImpairmentPortType"),
        ("CPIWF-MIB", "cpIwfPortNumber"))
)
if mibBuilder.loadTexts:
    cpIwfExcessImpairment.setStatus(
        "current"
    )


# Notifications groups

cpIwfNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3, 2, 12)
)
cpIwfNotificationsGroup.setObjects(
    ("CPIWF-MIB", "cpIwfInsufficientPhysicalBandwidth")
)
if mibBuilder.loadTexts:
    cpIwfNotificationsGroup.setStatus(
        "current"
    )

cpIwfImpairmentNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3, 2, 13)
)
cpIwfImpairmentNotificationsGroup.setObjects(
    ("CPIWF-MIB", "cpIwfExcessImpairment")
)
if mibBuilder.loadTexts:
    cpIwfImpairmentNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cpIwfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 10, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cpIwfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPIWF-MIB",
    **{"atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfLoopEmulationService": atmfLoopEmulationService,
       "cpIwfMIB": cpIwfMIB,
       "cpIwfMIBObjects": cpIwfMIBObjects,
       "cpIwf": cpIwf,
       "cpIwfVpi": cpIwfVpi,
       "cpIwfVci": cpIwfVci,
       "cpIwfEchoCancellationSupport": cpIwfEchoCancellationSupport,
       "cpIwfNumPotsPorts": cpIwfNumPotsPorts,
       "cpIwfNumIsdnBriPorts": cpIwfNumIsdnBriPorts,
       "cpIwfTimingReference": cpIwfTimingReference,
       "cpIwfPotsPortEncodingSelectionMode": cpIwfPotsPortEncodingSelectionMode,
       "cpIwfIsdnBriPortEncodingSelectionMode": cpIwfIsdnBriPortEncodingSelectionMode,
       "cpIwfElcpAndPstnChannelBandwidth": cpIwfElcpAndPstnChannelBandwidth,
       "cpIwfAdminStatus": cpIwfAdminStatus,
       "cpIwfOperStatus": cpIwfOperStatus,
       "cpIwfRestart": cpIwfRestart,
       "cpIwfTestType": cpIwfTestType,
       "cpIwfTestResult": cpIwfTestResult,
       "cpIwfTestResultText": cpIwfTestResultText,
       "cpIwfPlayoutBufferDepth": cpIwfPlayoutBufferDepth,
       "cpIwfImpairmentInterval": cpIwfImpairmentInterval,
       "cpIwfImpairmentThreshold": cpIwfImpairmentThreshold,
       "cpIwfV5PSTNProtocolVariant": cpIwfV5PSTNProtocolVariant,
       "cpIwfMwdForRestart": cpIwfMwdForRestart,
       "cpIwfEocBandwidth": cpIwfEocBandwidth,
       "cpIwfCurrentConfig": cpIwfCurrentConfig,
       "cpIwfTrapGeneration": cpIwfTrapGeneration,
       "cpIwfVendorName": cpIwfVendorName,
       "cpIwfDeviceType": cpIwfDeviceType,
       "cpIwfHardwareVersion": cpIwfHardwareVersion,
       "cpIwfSoftwareVersion": cpIwfSoftwareVersion,
       "cpIwfAal2Profile": cpIwfAal2Profile,
       "aal2ApplicationIdentifier": aal2ApplicationIdentifier,
       "aal2CpsMaxMultiplexedChannels": aal2CpsMaxMultiplexedChannels,
       "aal2CpsMaxSDULength": aal2CpsMaxSDULength,
       "aal2CpsCIDLowerLimit": aal2CpsCIDLowerLimit,
       "aal2CpsCIDUpperLimit": aal2CpsCIDUpperLimit,
       "aal2CpsOptimisation": aal2CpsOptimisation,
       "aal2CpsTimerCuValue": aal2CpsTimerCuValue,
       "aal2SscsFaxDemodulationTransport": aal2SscsFaxDemodulationTransport,
       "aal2SscsDtmfDigitPacketTransport": aal2SscsDtmfDigitPacketTransport,
       "aal2SscsPcmEncoding": aal2SscsPcmEncoding,
       "aal2SscsMaxSssarSduLength": aal2SscsMaxSssarSduLength,
       "aal2SscsProfileSource": aal2SscsProfileSource,
       "aal2SscsPredefinedProfileIdentifier": aal2SscsPredefinedProfileIdentifier,
       "aal2SscsIeeeOui": aal2SscsIeeeOui,
       "aal2SscsSsSarAssemblyTimerValue": aal2SscsSsSarAssemblyTimerValue,
       "cpIwfPotsPortTable": cpIwfPotsPortTable,
       "cpIwfPotsPortEntry": cpIwfPotsPortEntry,
       "potsPortNumber": potsPortNumber,
       "potsPhysicalPort": potsPhysicalPort,
       "aal2ChannelId": aal2ChannelId,
       "potsPortTestType": potsPortTestType,
       "signalingMethod": signalingMethod,
       "potsPortLabel": potsPortLabel,
       "cpIwfIsdnBriPortTable": cpIwfIsdnBriPortTable,
       "cpIwfIsdnBriPortEntry": cpIwfIsdnBriPortEntry,
       "isdnBriPortNumber": isdnBriPortNumber,
       "isdnBriPhysicalPort": isdnBriPhysicalPort,
       "aal2ChannelIdD": aal2ChannelIdD,
       "aal2ChannelIdB1": aal2ChannelIdB1,
       "aal2ChannelIdB2": aal2ChannelIdB2,
       "isdnBriPortLabel": isdnBriPortLabel,
       "isdnBriPortTestType": isdnBriPortTestType,
       "cpIwfAal2Stats": cpIwfAal2Stats,
       "aal2CpsInPkts": aal2CpsInPkts,
       "aal2CpsOutPkts": aal2CpsOutPkts,
       "aal2CpsParityErrors": aal2CpsParityErrors,
       "aal2CpsSeqNumErrors": aal2CpsSeqNumErrors,
       "aal2CpsOsfMismatchErrors": aal2CpsOsfMismatchErrors,
       "aal2CpsOsfErrors": aal2CpsOsfErrors,
       "aal2CpsHecErrors": aal2CpsHecErrors,
       "aal2CpsOversizedSduErrors": aal2CpsOversizedSduErrors,
       "aal2CpsReassemblyErrors": aal2CpsReassemblyErrors,
       "aal2CpsHecOverlapErrors": aal2CpsHecOverlapErrors,
       "aal2CpsUuiErrors": aal2CpsUuiErrors,
       "aal2CpsCidErrors": aal2CpsCidErrors,
       "aal2SscsOversizedSssarSduErrors": aal2SscsOversizedSssarSduErrors,
       "aal2SscsSssarRasTimerExpiryErrors": aal2SscsSssarRasTimerExpiryErrors,
       "aal2SscsUndersizedSstedPduErrors": aal2SscsUndersizedSstedPduErrors,
       "aal2SscsSstedPduLengthMismatchErrors": aal2SscsSstedPduLengthMismatchErrors,
       "aal2SscsSstedCrcMismatchErrors": aal2SscsSstedCrcMismatchErrors,
       "cpIwfPotsPortStatsTable": cpIwfPotsPortStatsTable,
       "cpIwfPotsPortStatsEntry": cpIwfPotsPortStatsEntry,
       "cpIwfPotsPortActiveSeconds": cpIwfPotsPortActiveSeconds,
       "cpIwfPotsPortFillerOctets": cpIwfPotsPortFillerOctets,
       "cpIwfPotsPortDroppedOctets": cpIwfPotsPortDroppedOctets,
       "cpIwfIsdnBriPortStatsTable": cpIwfIsdnBriPortStatsTable,
       "cpIwfIsdnBriPortStatsEntry": cpIwfIsdnBriPortStatsEntry,
       "cpIwfIsdnBriPortB1ActiveSeconds": cpIwfIsdnBriPortB1ActiveSeconds,
       "cpIwfIsdnBriPortB1FillerOctets": cpIwfIsdnBriPortB1FillerOctets,
       "cpIwfIsdnBriPortB1DroppedOctets": cpIwfIsdnBriPortB1DroppedOctets,
       "cpIwfIsdnBriPortB2ActiveSeconds": cpIwfIsdnBriPortB2ActiveSeconds,
       "cpIwfIsdnBriPortB2FillerOctets": cpIwfIsdnBriPortB2FillerOctets,
       "cpIwfIsdnBriPortB2DroppedOctets": cpIwfIsdnBriPortB2DroppedOctets,
       "cpIwfUpstreamPhysicalBandwidth": cpIwfUpstreamPhysicalBandwidth,
       "cpIwfDownstreamPhysicalBandwidth": cpIwfDownstreamPhysicalBandwidth,
       "cpIwfImpairmentPortType": cpIwfImpairmentPortType,
       "cpIwfPortNumber": cpIwfPortNumber,
       "cpIwfMIBNotifications": cpIwfMIBNotifications,
       "cpIwfMIBNotificationPrefix": cpIwfMIBNotificationPrefix,
       "cpIwfInsufficientPhysicalBandwidth": cpIwfInsufficientPhysicalBandwidth,
       "cpIwfExcessImpairment": cpIwfExcessImpairment,
       "cpIwfMIBConformance": cpIwfMIBConformance,
       "cpIwfMIBCompliances": cpIwfMIBCompliances,
       "cpIwfMIBCompliance": cpIwfMIBCompliance,
       "cpIwfMIBGroups": cpIwfMIBGroups,
       "cpIwfGeneralGroup": cpIwfGeneralGroup,
       "cpIwfAal2ConfigGroup": cpIwfAal2ConfigGroup,
       "cpIwfPotsPortConfigGroup": cpIwfPotsPortConfigGroup,
       "cpIwfIsdnBriPortConfigGroup": cpIwfIsdnBriPortConfigGroup,
       "cpIwfPotsPortCidConfigGroup": cpIwfPotsPortCidConfigGroup,
       "cpIwfIsdnBriPortCidConfigGroup": cpIwfIsdnBriPortCidConfigGroup,
       "cpIwfAal2StatsGroup": cpIwfAal2StatsGroup,
       "cpIwfPotsPortStatsGroup": cpIwfPotsPortStatsGroup,
       "cpIwfIsdnBriPortStatsGroup": cpIwfIsdnBriPortStatsGroup,
       "cpIwfElcpPstnGroup": cpIwfElcpPstnGroup,
       "cpIwfPlayoutBufferGroup": cpIwfPlayoutBufferGroup,
       "cpIwfNotificationsGroup": cpIwfNotificationsGroup,
       "cpIwfImpairmentNotificationsGroup": cpIwfImpairmentNotificationsGroup}
)
