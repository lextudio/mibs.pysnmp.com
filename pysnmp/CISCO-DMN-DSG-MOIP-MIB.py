# SNMP MIB module (CISCO-DMN-DSG-MOIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-MOIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:27 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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

ciscoDSGMOIP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35)
)
ciscoDSGMOIP.setRevisions(
        ("2012-03-20 11:00",
         "2010-08-24 07:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MoipIPOTable_ObjectIdentity = ObjectIdentity
moipIPOTable = _MoipIPOTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1)
)
_MoipIPOConfigTable_Object = MibTable
moipIPOConfigTable = _MoipIPOConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1)
)
if mibBuilder.loadTexts:
    moipIPOConfigTable.setStatus("current")
_MoipIPOConfigEntry_Object = MibTableRow
moipIPOConfigEntry = _MoipIPOConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1)
)
moipIPOConfigEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-MOIP-MIB", "moipIPOConfigID"),
)
if mibBuilder.loadTexts:
    moipIPOConfigEntry.setStatus("current")


class _MoipIPOConfigID_Type(Integer32):
    """Custom type moipIPOConfigID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MoipIPOConfigID_Type.__name__ = "Integer32"
_MoipIPOConfigID_Object = MibTableColumn
moipIPOConfigID = _MoipIPOConfigID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 1),
    _MoipIPOConfigID_Type()
)
moipIPOConfigID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipIPOConfigID.setStatus("current")


class _MoipIPOConfigOutputEnabled_Type(Integer32):
    """Custom type moipIPOConfigOutputEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 3))
    )


_MoipIPOConfigOutputEnabled_Type.__name__ = "Integer32"
_MoipIPOConfigOutputEnabled_Object = MibTableColumn
moipIPOConfigOutputEnabled = _MoipIPOConfigOutputEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 2),
    _MoipIPOConfigOutputEnabled_Type()
)
moipIPOConfigOutputEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigOutputEnabled.setStatus("current")


class _MoipIPOConfigInstanceName_Type(DisplayString):
    """Custom type moipIPOConfigInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MoipIPOConfigInstanceName_Type.__name__ = "DisplayString"
_MoipIPOConfigInstanceName_Object = MibTableColumn
moipIPOConfigInstanceName = _MoipIPOConfigInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 3),
    _MoipIPOConfigInstanceName_Type()
)
moipIPOConfigInstanceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigInstanceName.setStatus("current")


class _MoipIPOConfigTPProtocol_Type(Integer32):
    """Custom type moipIPOConfigTPProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtp", 2),
          ("udp", 1))
    )


_MoipIPOConfigTPProtocol_Type.__name__ = "Integer32"
_MoipIPOConfigTPProtocol_Object = MibTableColumn
moipIPOConfigTPProtocol = _MoipIPOConfigTPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 4),
    _MoipIPOConfigTPProtocol_Type()
)
moipIPOConfigTPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigTPProtocol.setStatus("current")


class _MoipIPOConfigIPVer_Type(DisplayString):
    """Custom type moipIPOConfigIPVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MoipIPOConfigIPVer_Type.__name__ = "DisplayString"
_MoipIPOConfigIPVer_Object = MibTableColumn
moipIPOConfigIPVer = _MoipIPOConfigIPVer_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 5),
    _MoipIPOConfigIPVer_Type()
)
moipIPOConfigIPVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipIPOConfigIPVer.setStatus("current")
_MoipIPOConfigDestIPAddr_Type = IpAddress
_MoipIPOConfigDestIPAddr_Object = MibTableColumn
moipIPOConfigDestIPAddr = _MoipIPOConfigDestIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 6),
    _MoipIPOConfigDestIPAddr_Type()
)
moipIPOConfigDestIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigDestIPAddr.setStatus("current")
_MoipIPOConfigSAPMulticastIPAddr_Type = IpAddress
_MoipIPOConfigSAPMulticastIPAddr_Object = MibTableColumn
moipIPOConfigSAPMulticastIPAddr = _MoipIPOConfigSAPMulticastIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 7),
    _MoipIPOConfigSAPMulticastIPAddr_Type()
)
moipIPOConfigSAPMulticastIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigSAPMulticastIPAddr.setStatus("current")


class _MoipIPOConfigDestPort_Type(Integer32):
    """Custom type moipIPOConfigDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_MoipIPOConfigDestPort_Type.__name__ = "Integer32"
_MoipIPOConfigDestPort_Object = MibTableColumn
moipIPOConfigDestPort = _MoipIPOConfigDestPort_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 8),
    _MoipIPOConfigDestPort_Type()
)
moipIPOConfigDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigDestPort.setStatus("current")


class _MoipIPOConfigSrcPort_Type(Integer32):
    """Custom type moipIPOConfigSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MoipIPOConfigSrcPort_Type.__name__ = "Integer32"
_MoipIPOConfigSrcPort_Object = MibTableColumn
moipIPOConfigSrcPort = _MoipIPOConfigSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 9),
    _MoipIPOConfigSrcPort_Type()
)
moipIPOConfigSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigSrcPort.setStatus("current")


class _MoipIPOConfigMinIPPerSec_Type(Integer32):
    """Custom type moipIPOConfigMinIPPerSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MoipIPOConfigMinIPPerSec_Type.__name__ = "Integer32"
_MoipIPOConfigMinIPPerSec_Object = MibTableColumn
moipIPOConfigMinIPPerSec = _MoipIPOConfigMinIPPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 10),
    _MoipIPOConfigMinIPPerSec_Type()
)
moipIPOConfigMinIPPerSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigMinIPPerSec.setStatus("current")


class _MoipIPOConfigPCRAddition_Type(Integer32):
    """Custom type moipIPOConfigPCRAddition based on Integer32"""
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


_MoipIPOConfigPCRAddition_Type.__name__ = "Integer32"
_MoipIPOConfigPCRAddition_Object = MibTableColumn
moipIPOConfigPCRAddition = _MoipIPOConfigPCRAddition_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 11),
    _MoipIPOConfigPCRAddition_Type()
)
moipIPOConfigPCRAddition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigPCRAddition.setStatus("current")


class _MoipIPOConfigPCRStartNewPkt_Type(Integer32):
    """Custom type moipIPOConfigPCRStartNewPkt based on Integer32"""
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


_MoipIPOConfigPCRStartNewPkt_Type.__name__ = "Integer32"
_MoipIPOConfigPCRStartNewPkt_Object = MibTableColumn
moipIPOConfigPCRStartNewPkt = _MoipIPOConfigPCRStartNewPkt_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 12),
    _MoipIPOConfigPCRStartNewPkt_Type()
)
moipIPOConfigPCRStartNewPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigPCRStartNewPkt.setStatus("current")


class _MoipIPOConfigSendSAP_Type(Integer32):
    """Custom type moipIPOConfigSendSAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rfc2327", 2))
    )


_MoipIPOConfigSendSAP_Type.__name__ = "Integer32"
_MoipIPOConfigSendSAP_Object = MibTableColumn
moipIPOConfigSendSAP = _MoipIPOConfigSendSAP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 13),
    _MoipIPOConfigSendSAP_Type()
)
moipIPOConfigSendSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigSendSAP.setStatus("current")


class _MoipIPOConfigUseSAPStr_Type(Integer32):
    """Custom type moipIPOConfigUseSAPStr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdtChName", 2),
          ("userString", 1))
    )


_MoipIPOConfigUseSAPStr_Type.__name__ = "Integer32"
_MoipIPOConfigUseSAPStr_Object = MibTableColumn
moipIPOConfigUseSAPStr = _MoipIPOConfigUseSAPStr_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 14),
    _MoipIPOConfigUseSAPStr_Type()
)
moipIPOConfigUseSAPStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigUseSAPStr.setStatus("current")


class _MoipIPOConfigMaxTransPktPerIP_Type(Integer32):
    """Custom type moipIPOConfigMaxTransPktPerIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_MoipIPOConfigMaxTransPktPerIP_Type.__name__ = "Integer32"
_MoipIPOConfigMaxTransPktPerIP_Object = MibTableColumn
moipIPOConfigMaxTransPktPerIP = _MoipIPOConfigMaxTransPktPerIP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 15),
    _MoipIPOConfigMaxTransPktPerIP_Type()
)
moipIPOConfigMaxTransPktPerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigMaxTransPktPerIP.setStatus("current")


class _MoipIPOConfigSAPStr_Type(DisplayString):
    """Custom type moipIPOConfigSAPStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MoipIPOConfigSAPStr_Type.__name__ = "DisplayString"
_MoipIPOConfigSAPStr_Object = MibTableColumn
moipIPOConfigSAPStr = _MoipIPOConfigSAPStr_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 16),
    _MoipIPOConfigSAPStr_Type()
)
moipIPOConfigSAPStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigSAPStr.setStatus("current")


class _MoipIPOConfigInterfaceMode_Type(Integer32):
    """Custom type moipIPOConfigInterfaceMode based on Integer32"""
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
        *(("both", 4),
          ("data1", 2),
          ("data2", 3),
          ("none", 1),
          ("redundancy", 5))
    )


_MoipIPOConfigInterfaceMode_Type.__name__ = "Integer32"
_MoipIPOConfigInterfaceMode_Object = MibTableColumn
moipIPOConfigInterfaceMode = _MoipIPOConfigInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 17),
    _MoipIPOConfigInterfaceMode_Type()
)
moipIPOConfigInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigInterfaceMode.setStatus("current")


class _MoipIPOConfigBitRate_Type(Integer32):
    """Custom type moipIPOConfigBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 206000000),
    )


_MoipIPOConfigBitRate_Type.__name__ = "Integer32"
_MoipIPOConfigBitRate_Object = MibTableColumn
moipIPOConfigBitRate = _MoipIPOConfigBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 18),
    _MoipIPOConfigBitRate_Type()
)
moipIPOConfigBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigBitRate.setStatus("current")


class _MoipIPOConfigTOS_Type(Integer32):
    """Custom type moipIPOConfigTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MoipIPOConfigTOS_Type.__name__ = "Integer32"
_MoipIPOConfigTOS_Object = MibTableColumn
moipIPOConfigTOS = _MoipIPOConfigTOS_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 19),
    _MoipIPOConfigTOS_Type()
)
moipIPOConfigTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigTOS.setStatus("current")


class _MoipIPOConfigTTL_Type(Integer32):
    """Custom type moipIPOConfigTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MoipIPOConfigTTL_Type.__name__ = "Integer32"
_MoipIPOConfigTTL_Object = MibTableColumn
moipIPOConfigTTL = _MoipIPOConfigTTL_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 20),
    _MoipIPOConfigTTL_Type()
)
moipIPOConfigTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigTTL.setStatus("current")


class _MoipIPOConfigSAPDestPort_Type(Integer32):
    """Custom type moipIPOConfigSAPDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_MoipIPOConfigSAPDestPort_Type.__name__ = "Integer32"
_MoipIPOConfigSAPDestPort_Object = MibTableColumn
moipIPOConfigSAPDestPort = _MoipIPOConfigSAPDestPort_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 21),
    _MoipIPOConfigSAPDestPort_Type()
)
moipIPOConfigSAPDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOConfigSAPDestPort.setStatus("current")


class _MoipIPOFECMode_Type(Integer32):
    """Custom type moipIPOFECMode based on Integer32"""
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
          ("oneD", 2),
          ("twoD", 3))
    )


_MoipIPOFECMode_Type.__name__ = "Integer32"
_MoipIPOFECMode_Object = MibTableColumn
moipIPOFECMode = _MoipIPOFECMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 22),
    _MoipIPOFECMode_Type()
)
moipIPOFECMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOFECMode.setStatus("current")


class _MoipIPOFECColDepth_Type(Integer32):
    """Custom type moipIPOFECColDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_MoipIPOFECColDepth_Type.__name__ = "Integer32"
_MoipIPOFECColDepth_Object = MibTableColumn
moipIPOFECColDepth = _MoipIPOFECColDepth_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 23),
    _MoipIPOFECColDepth_Type()
)
moipIPOFECColDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOFECColDepth.setStatus("current")


class _MoipIPOFECRowWidth_Type(Integer32):
    """Custom type moipIPOFECRowWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_MoipIPOFECRowWidth_Type.__name__ = "Integer32"
_MoipIPOFECRowWidth_Object = MibTableColumn
moipIPOFECRowWidth = _MoipIPOFECRowWidth_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 24),
    _MoipIPOFECRowWidth_Type()
)
moipIPOFECRowWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOFECRowWidth.setStatus("current")


class _MoipIPOAnnexType_Type(Integer32):
    """Custom type moipIPOAnnexType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 1),
          ("annexB", 2))
    )


_MoipIPOAnnexType_Type.__name__ = "Integer32"
_MoipIPOAnnexType_Object = MibTableColumn
moipIPOAnnexType = _MoipIPOAnnexType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 25),
    _MoipIPOAnnexType_Type()
)
moipIPOAnnexType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOAnnexType.setStatus("current")


class _MoipIPOFEC1UDPPort_Type(Integer32):
    """Custom type moipIPOFEC1UDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65534),
    )


_MoipIPOFEC1UDPPort_Type.__name__ = "Integer32"
_MoipIPOFEC1UDPPort_Object = MibTableColumn
moipIPOFEC1UDPPort = _MoipIPOFEC1UDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 26),
    _MoipIPOFEC1UDPPort_Type()
)
moipIPOFEC1UDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOFEC1UDPPort.setStatus("current")


class _MoipIPOFEC2UDPPort_Type(Integer32):
    """Custom type moipIPOFEC2UDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65534),
    )


_MoipIPOFEC2UDPPort_Type.__name__ = "Integer32"
_MoipIPOFEC2UDPPort_Object = MibTableColumn
moipIPOFEC2UDPPort = _MoipIPOFEC2UDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 1, 1, 27),
    _MoipIPOFEC2UDPPort_Type()
)
moipIPOFEC2UDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipIPOFEC2UDPPort.setStatus("current")
_MoipIPOStreamStatusTable_Object = MibTable
moipIPOStreamStatusTable = _MoipIPOStreamStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 2)
)
if mibBuilder.loadTexts:
    moipIPOStreamStatusTable.setStatus("current")
_MoipIPOStreamStatusEntry_Object = MibTableRow
moipIPOStreamStatusEntry = _MoipIPOStreamStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 2, 1)
)
moipIPOStreamStatusEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-MOIP-MIB", "moipIPOStreamStatusID"),
)
if mibBuilder.loadTexts:
    moipIPOStreamStatusEntry.setStatus("current")


class _MoipIPOStreamStatusID_Type(Integer32):
    """Custom type moipIPOStreamStatusID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_MoipIPOStreamStatusID_Type.__name__ = "Integer32"
_MoipIPOStreamStatusID_Object = MibTableColumn
moipIPOStreamStatusID = _MoipIPOStreamStatusID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 2, 1, 1),
    _MoipIPOStreamStatusID_Type()
)
moipIPOStreamStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipIPOStreamStatusID.setStatus("current")


class _MoipIPOStreamStatusIntf1_Type(Integer32):
    """Custom type moipIPOStreamStatusIntf1 based on Integer32"""
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
        *(("active", 5),
          ("muted", 4),
          ("notInit", 1),
          ("stopped", 2),
          ("suspended", 3))
    )


_MoipIPOStreamStatusIntf1_Type.__name__ = "Integer32"
_MoipIPOStreamStatusIntf1_Object = MibTableColumn
moipIPOStreamStatusIntf1 = _MoipIPOStreamStatusIntf1_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 2, 1, 2),
    _MoipIPOStreamStatusIntf1_Type()
)
moipIPOStreamStatusIntf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipIPOStreamStatusIntf1.setStatus("current")


class _MoipIPOStreamStatusIntf2_Type(Integer32):
    """Custom type moipIPOStreamStatusIntf2 based on Integer32"""
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
        *(("active", 5),
          ("muted", 4),
          ("notInit", 1),
          ("stopped", 2),
          ("suspended", 3))
    )


_MoipIPOStreamStatusIntf2_Type.__name__ = "Integer32"
_MoipIPOStreamStatusIntf2_Object = MibTableColumn
moipIPOStreamStatusIntf2 = _MoipIPOStreamStatusIntf2_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 2, 1, 3),
    _MoipIPOStreamStatusIntf2_Type()
)
moipIPOStreamStatusIntf2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipIPOStreamStatusIntf2.setStatus("current")


class _MoipIPOStreamStatusContentOvfl_Type(Integer32):
    """Custom type moipIPOStreamStatusContentOvfl based on Integer32"""
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


_MoipIPOStreamStatusContentOvfl_Type.__name__ = "Integer32"
_MoipIPOStreamStatusContentOvfl_Object = MibTableColumn
moipIPOStreamStatusContentOvfl = _MoipIPOStreamStatusContentOvfl_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 2, 1, 4),
    _MoipIPOStreamStatusContentOvfl_Type()
)
moipIPOStreamStatusContentOvfl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipIPOStreamStatusContentOvfl.setStatus("current")


class _MoipIPOStreamStatusLinkOvfl_Type(Integer32):
    """Custom type moipIPOStreamStatusLinkOvfl based on Integer32"""
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


_MoipIPOStreamStatusLinkOvfl_Type.__name__ = "Integer32"
_MoipIPOStreamStatusLinkOvfl_Object = MibTableColumn
moipIPOStreamStatusLinkOvfl = _MoipIPOStreamStatusLinkOvfl_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 1, 2, 1, 5),
    _MoipIPOStreamStatusLinkOvfl_Type()
)
moipIPOStreamStatusLinkOvfl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipIPOStreamStatusLinkOvfl.setStatus("current")
_MoipIPOInfo_ObjectIdentity = ObjectIdentity
moipIPOInfo = _MoipIPOInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 2)
)


class _MoipIPOStatsHWGlobalError_Type(Integer32):
    """Custom type moipIPOStatsHWGlobalError based on Integer32"""
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


_MoipIPOStatsHWGlobalError_Type.__name__ = "Integer32"
_MoipIPOStatsHWGlobalError_Object = MibScalar
moipIPOStatsHWGlobalError = _MoipIPOStatsHWGlobalError_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 2, 1),
    _MoipIPOStatsHWGlobalError_Type()
)
moipIPOStatsHWGlobalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipIPOStatsHWGlobalError.setStatus("current")


class _MoipIPOStatsStreamError_Type(Integer32):
    """Custom type moipIPOStatsStreamError based on Integer32"""
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


_MoipIPOStatsStreamError_Type.__name__ = "Integer32"
_MoipIPOStatsStreamError_Object = MibScalar
moipIPOStatsStreamError = _MoipIPOStatsStreamError_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 2, 2),
    _MoipIPOStatsStreamError_Type()
)
moipIPOStatsStreamError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipIPOStatsStreamError.setStatus("current")


class _MoipIPOStatsBandwidthConf_Type(DisplayString):
    """Custom type moipIPOStatsBandwidthConf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MoipIPOStatsBandwidthConf_Type.__name__ = "DisplayString"
_MoipIPOStatsBandwidthConf_Object = MibScalar
moipIPOStatsBandwidthConf = _MoipIPOStatsBandwidthConf_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 2, 3),
    _MoipIPOStatsBandwidthConf_Type()
)
moipIPOStatsBandwidthConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipIPOStatsBandwidthConf.setStatus("current")


class _MoipIPOStatsBandwidthActIntf1_Type(DisplayString):
    """Custom type moipIPOStatsBandwidthActIntf1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MoipIPOStatsBandwidthActIntf1_Type.__name__ = "DisplayString"
_MoipIPOStatsBandwidthActIntf1_Object = MibScalar
moipIPOStatsBandwidthActIntf1 = _MoipIPOStatsBandwidthActIntf1_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 2, 4),
    _MoipIPOStatsBandwidthActIntf1_Type()
)
moipIPOStatsBandwidthActIntf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipIPOStatsBandwidthActIntf1.setStatus("current")


class _MoipIPOStatsBandwidthActIntf2_Type(DisplayString):
    """Custom type moipIPOStatsBandwidthActIntf2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MoipIPOStatsBandwidthActIntf2_Type.__name__ = "DisplayString"
_MoipIPOStatsBandwidthActIntf2_Object = MibScalar
moipIPOStatsBandwidthActIntf2 = _MoipIPOStatsBandwidthActIntf2_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 35, 2, 5),
    _MoipIPOStatsBandwidthActIntf2_Type()
)
moipIPOStatsBandwidthActIntf2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipIPOStatsBandwidthActIntf2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-MOIP-MIB",
    **{"ciscoDSGMOIP": ciscoDSGMOIP,
       "moipIPOTable": moipIPOTable,
       "moipIPOConfigTable": moipIPOConfigTable,
       "moipIPOConfigEntry": moipIPOConfigEntry,
       "moipIPOConfigID": moipIPOConfigID,
       "moipIPOConfigOutputEnabled": moipIPOConfigOutputEnabled,
       "moipIPOConfigInstanceName": moipIPOConfigInstanceName,
       "moipIPOConfigTPProtocol": moipIPOConfigTPProtocol,
       "moipIPOConfigIPVer": moipIPOConfigIPVer,
       "moipIPOConfigDestIPAddr": moipIPOConfigDestIPAddr,
       "moipIPOConfigSAPMulticastIPAddr": moipIPOConfigSAPMulticastIPAddr,
       "moipIPOConfigDestPort": moipIPOConfigDestPort,
       "moipIPOConfigSrcPort": moipIPOConfigSrcPort,
       "moipIPOConfigMinIPPerSec": moipIPOConfigMinIPPerSec,
       "moipIPOConfigPCRAddition": moipIPOConfigPCRAddition,
       "moipIPOConfigPCRStartNewPkt": moipIPOConfigPCRStartNewPkt,
       "moipIPOConfigSendSAP": moipIPOConfigSendSAP,
       "moipIPOConfigUseSAPStr": moipIPOConfigUseSAPStr,
       "moipIPOConfigMaxTransPktPerIP": moipIPOConfigMaxTransPktPerIP,
       "moipIPOConfigSAPStr": moipIPOConfigSAPStr,
       "moipIPOConfigInterfaceMode": moipIPOConfigInterfaceMode,
       "moipIPOConfigBitRate": moipIPOConfigBitRate,
       "moipIPOConfigTOS": moipIPOConfigTOS,
       "moipIPOConfigTTL": moipIPOConfigTTL,
       "moipIPOConfigSAPDestPort": moipIPOConfigSAPDestPort,
       "moipIPOFECMode": moipIPOFECMode,
       "moipIPOFECColDepth": moipIPOFECColDepth,
       "moipIPOFECRowWidth": moipIPOFECRowWidth,
       "moipIPOAnnexType": moipIPOAnnexType,
       "moipIPOFEC1UDPPort": moipIPOFEC1UDPPort,
       "moipIPOFEC2UDPPort": moipIPOFEC2UDPPort,
       "moipIPOStreamStatusTable": moipIPOStreamStatusTable,
       "moipIPOStreamStatusEntry": moipIPOStreamStatusEntry,
       "moipIPOStreamStatusID": moipIPOStreamStatusID,
       "moipIPOStreamStatusIntf1": moipIPOStreamStatusIntf1,
       "moipIPOStreamStatusIntf2": moipIPOStreamStatusIntf2,
       "moipIPOStreamStatusContentOvfl": moipIPOStreamStatusContentOvfl,
       "moipIPOStreamStatusLinkOvfl": moipIPOStreamStatusLinkOvfl,
       "moipIPOInfo": moipIPOInfo,
       "moipIPOStatsHWGlobalError": moipIPOStatsHWGlobalError,
       "moipIPOStatsStreamError": moipIPOStatsStreamError,
       "moipIPOStatsBandwidthConf": moipIPOStatsBandwidthConf,
       "moipIPOStatsBandwidthActIntf1": moipIPOStatsBandwidthActIntf1,
       "moipIPOStatsBandwidthActIntf2": moipIPOStatsBandwidthActIntf2}
)
