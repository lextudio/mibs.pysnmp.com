# SNMP MIB module (ZHONE-COM-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-PPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:22 2024
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

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
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

(zhoneModules,
 zhonePpp) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneModules",
    "zhonePpp")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

comPpp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 69)
)
comPpp.setRevisions(
        ("2001-06-06 16:00",
         "2001-04-19 15:00",
         "2001-03-20 09:30",
         "2001-03-12 11:00",
         "2001-03-01 11:00",
         "2001-02-08 10:02")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ZhoneAuthenticationProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 2),
          ("pap", 1))
    )



class EnableFlag(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_PppInterfaceTable_Object = MibTable
pppInterfaceTable = _PppInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 1)
)
if mibBuilder.loadTexts:
    pppInterfaceTable.setStatus("current")
_PppInterfaceEntry_Object = MibTableRow
pppInterfaceEntry = _PppInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 1, 1)
)
pppInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppInterfaceEntry.setStatus("current")
_PppIfLowerIfIndex_Type = InterfaceIndex
_PppIfLowerIfIndex_Object = MibTableColumn
pppIfLowerIfIndex = _PppIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 1, 1, 1),
    _PppIfLowerIfIndex_Type()
)
pppIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppIfLowerIfIndex.setStatus("current")


class _PppIfVpi_Type(AtmVpIdentifier):
    """Custom type pppIfVpi based on AtmVpIdentifier"""
    defaultValue = 0


_PppIfVpi_Object = MibTableColumn
pppIfVpi = _PppIfVpi_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 1, 1, 2),
    _PppIfVpi_Type()
)
pppIfVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppIfVpi.setStatus("current")


class _PppIfVci_Type(AtmVcIdentifier):
    """Custom type pppIfVci based on AtmVcIdentifier"""
    defaultValue = 0


_PppIfVci_Object = MibTableColumn
pppIfVci = _PppIfVci_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 1, 1, 3),
    _PppIfVci_Type()
)
pppIfVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppIfVci.setStatus("current")


class _PppIfCallMode_Type(Integer32):
    """Custom type pppIfCallMode based on Integer32"""
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
        *(("inCall", 2),
          ("noCall", 1),
          ("outCall", 3))
    )


_PppIfCallMode_Type.__name__ = "Integer32"
_PppIfCallMode_Object = MibTableColumn
pppIfCallMode = _PppIfCallMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 1, 1, 4),
    _PppIfCallMode_Type()
)
pppIfCallMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppIfCallMode.setStatus("current")


class _PppIfFrameType_Type(Integer32):
    """Custom type pppIfFrameType based on Integer32"""
    defaultValue = 3

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
        *(("atmLLC", 3),
          ("atmVc", 4),
          ("frameRelay", 2),
          ("none", 1))
    )


_PppIfFrameType_Type.__name__ = "Integer32"
_PppIfFrameType_Object = MibTableColumn
pppIfFrameType = _PppIfFrameType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 1, 1, 5),
    _PppIfFrameType_Type()
)
pppIfFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppIfFrameType.setStatus("current")


class _PppIfNumChannels_Type(Integer32):
    """Custom type pppIfNumChannels based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PppIfNumChannels_Type.__name__ = "Integer32"
_PppIfNumChannels_Object = MibTableColumn
pppIfNumChannels = _PppIfNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 1, 1, 6),
    _PppIfNumChannels_Type()
)
pppIfNumChannels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppIfNumChannels.setStatus("current")
_PppIfRowStatus_Type = ZhoneRowStatus
_PppIfRowStatus_Object = MibTableColumn
pppIfRowStatus = _PppIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 1, 1, 7),
    _PppIfRowStatus_Type()
)
pppIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppIfRowStatus.setStatus("current")
_PppLCPExtensionsTable_Object = MibTable
pppLCPExtensionsTable = _PppLCPExtensionsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2)
)
if mibBuilder.loadTexts:
    pppLCPExtensionsTable.setStatus("current")
_PppLCPExtensionsEntry_Object = MibTableRow
pppLCPExtensionsEntry = _PppLCPExtensionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1)
)
if mibBuilder.loadTexts:
    pppLCPExtensionsEntry.setStatus("current")


class _LcpExtReceiveAuthEnable_Type(EnableFlag):
    """Custom type lcpExtReceiveAuthEnable based on EnableFlag"""


_LcpExtReceiveAuthEnable_Object = MibTableColumn
lcpExtReceiveAuthEnable = _LcpExtReceiveAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 1),
    _LcpExtReceiveAuthEnable_Type()
)
lcpExtReceiveAuthEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtReceiveAuthEnable.setStatus("current")


class _LcpExtReceiveAuthProtocol_Type(ZhoneAuthenticationProtocol):
    """Custom type lcpExtReceiveAuthProtocol based on ZhoneAuthenticationProtocol"""


_LcpExtReceiveAuthProtocol_Object = MibTableColumn
lcpExtReceiveAuthProtocol = _LcpExtReceiveAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 2),
    _LcpExtReceiveAuthProtocol_Type()
)
lcpExtReceiveAuthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtReceiveAuthProtocol.setStatus("current")


class _LcpExtSendAuthEnable_Type(EnableFlag):
    """Custom type lcpExtSendAuthEnable based on EnableFlag"""


_LcpExtSendAuthEnable_Object = MibTableColumn
lcpExtSendAuthEnable = _LcpExtSendAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 3),
    _LcpExtSendAuthEnable_Type()
)
lcpExtSendAuthEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtSendAuthEnable.setStatus("current")


class _LcpExtSendAuthProtocol_Type(ZhoneAuthenticationProtocol):
    """Custom type lcpExtSendAuthProtocol based on ZhoneAuthenticationProtocol"""


_LcpExtSendAuthProtocol_Object = MibTableColumn
lcpExtSendAuthProtocol = _LcpExtSendAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 4),
    _LcpExtSendAuthProtocol_Type()
)
lcpExtSendAuthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtSendAuthProtocol.setStatus("current")


class _LcpExtSendAuthIdentity_Type(OctetString):
    """Custom type lcpExtSendAuthIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_LcpExtSendAuthIdentity_Type.__name__ = "OctetString"
_LcpExtSendAuthIdentity_Object = MibTableColumn
lcpExtSendAuthIdentity = _LcpExtSendAuthIdentity_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 5),
    _LcpExtSendAuthIdentity_Type()
)
lcpExtSendAuthIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtSendAuthIdentity.setStatus("current")


class _LcpExtQualityProtocol_Type(Integer32):
    """Custom type lcpExtQualityProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("lqr", 1)
    )


_LcpExtQualityProtocol_Type.__name__ = "Integer32"
_LcpExtQualityProtocol_Object = MibTableColumn
lcpExtQualityProtocol = _LcpExtQualityProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 6),
    _LcpExtQualityProtocol_Type()
)
lcpExtQualityProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtQualityProtocol.setStatus("current")


class _LcpExtMagicNumber_Type(Unsigned32):
    """Custom type lcpExtMagicNumber based on Unsigned32"""
    defaultValue = 0


_LcpExtMagicNumber_Object = MibTableColumn
lcpExtMagicNumber = _LcpExtMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 7),
    _LcpExtMagicNumber_Type()
)
lcpExtMagicNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtMagicNumber.setStatus("current")


class _LcpExtMaxPad_Type(Integer32):
    """Custom type lcpExtMaxPad based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LcpExtMaxPad_Type.__name__ = "Integer32"
_LcpExtMaxPad_Object = MibTableColumn
lcpExtMaxPad = _LcpExtMaxPad_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 8),
    _LcpExtMaxPad_Type()
)
lcpExtMaxPad.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtMaxPad.setStatus("current")


class _LcpExtCallbackEnable_Type(EnableFlag):
    """Custom type lcpExtCallbackEnable based on EnableFlag"""


_LcpExtCallbackEnable_Object = MibTableColumn
lcpExtCallbackEnable = _LcpExtCallbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 9),
    _LcpExtCallbackEnable_Type()
)
lcpExtCallbackEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtCallbackEnable.setStatus("current")


class _LcpExtCallbackType_Type(Integer32):
    """Custom type lcpExtCallbackType based on Integer32"""
    defaultValue = 1

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
        *(("byAuth", 1),
          ("byDialStr", 2),
          ("byE164", 4),
          ("byIdentifier", 3),
          ("byName", 5))
    )


_LcpExtCallbackType_Type.__name__ = "Integer32"
_LcpExtCallbackType_Object = MibTableColumn
lcpExtCallbackType = _LcpExtCallbackType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 10),
    _LcpExtCallbackType_Type()
)
lcpExtCallbackType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtCallbackType.setStatus("current")


class _LcpExtCallbackDialString_Type(OctetString):
    """Custom type lcpExtCallbackDialString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_LcpExtCallbackDialString_Type.__name__ = "OctetString"
_LcpExtCallbackDialString_Object = MibTableColumn
lcpExtCallbackDialString = _LcpExtCallbackDialString_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 11),
    _LcpExtCallbackDialString_Type()
)
lcpExtCallbackDialString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtCallbackDialString.setStatus("current")


class _LcpExtRestartTimer_Type(Integer32):
    """Custom type lcpExtRestartTimer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_LcpExtRestartTimer_Type.__name__ = "Integer32"
_LcpExtRestartTimer_Object = MibTableColumn
lcpExtRestartTimer = _LcpExtRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 12),
    _LcpExtRestartTimer_Type()
)
lcpExtRestartTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtRestartTimer.setStatus("current")
if mibBuilder.loadTexts:
    lcpExtRestartTimer.setUnits("seconds")


class _LcpExtMaxConfigRetries_Type(Integer32):
    """Custom type lcpExtMaxConfigRetries based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_LcpExtMaxConfigRetries_Type.__name__ = "Integer32"
_LcpExtMaxConfigRetries_Object = MibTableColumn
lcpExtMaxConfigRetries = _LcpExtMaxConfigRetries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 13),
    _LcpExtMaxConfigRetries_Type()
)
lcpExtMaxConfigRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtMaxConfigRetries.setStatus("current")


class _LcpExtMaxTerminateRetries_Type(Integer32):
    """Custom type lcpExtMaxTerminateRetries based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_LcpExtMaxTerminateRetries_Type.__name__ = "Integer32"
_LcpExtMaxTerminateRetries_Object = MibTableColumn
lcpExtMaxTerminateRetries = _LcpExtMaxTerminateRetries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 14),
    _LcpExtMaxTerminateRetries_Type()
)
lcpExtMaxTerminateRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtMaxTerminateRetries.setStatus("current")


class _LcpExtMaxFailureRetries_Type(Integer32):
    """Custom type lcpExtMaxFailureRetries based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_LcpExtMaxFailureRetries_Type.__name__ = "Integer32"
_LcpExtMaxFailureRetries_Object = MibTableColumn
lcpExtMaxFailureRetries = _LcpExtMaxFailureRetries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 15),
    _LcpExtMaxFailureRetries_Type()
)
lcpExtMaxFailureRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtMaxFailureRetries.setStatus("current")


class _LcpExtMRUEnable_Type(EnableFlag):
    """Custom type lcpExtMRUEnable based on EnableFlag"""


_LcpExtMRUEnable_Object = MibTableColumn
lcpExtMRUEnable = _LcpExtMRUEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 16),
    _LcpExtMRUEnable_Type()
)
lcpExtMRUEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtMRUEnable.setStatus("current")


class _LcpExtACCMEnable_Type(EnableFlag):
    """Custom type lcpExtACCMEnable based on EnableFlag"""


_LcpExtACCMEnable_Object = MibTableColumn
lcpExtACCMEnable = _LcpExtACCMEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 17),
    _LcpExtACCMEnable_Type()
)
lcpExtACCMEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtACCMEnable.setStatus("current")


class _LcpExtPFCEnable_Type(EnableFlag):
    """Custom type lcpExtPFCEnable based on EnableFlag"""


_LcpExtPFCEnable_Object = MibTableColumn
lcpExtPFCEnable = _LcpExtPFCEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 18),
    _LcpExtPFCEnable_Type()
)
lcpExtPFCEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtPFCEnable.setStatus("current")


class _LcpExtACFCEnable_Type(EnableFlag):
    """Custom type lcpExtACFCEnable based on EnableFlag"""


_LcpExtACFCEnable_Object = MibTableColumn
lcpExtACFCEnable = _LcpExtACFCEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 19),
    _LcpExtACFCEnable_Type()
)
lcpExtACFCEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtACFCEnable.setStatus("current")


class _LcpExtFCSAltEnable_Type(EnableFlag):
    """Custom type lcpExtFCSAltEnable based on EnableFlag"""


_LcpExtFCSAltEnable_Object = MibTableColumn
lcpExtFCSAltEnable = _LcpExtFCSAltEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 20),
    _LcpExtFCSAltEnable_Type()
)
lcpExtFCSAltEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtFCSAltEnable.setStatus("current")


class _LcpExtSDPEnable_Type(EnableFlag):
    """Custom type lcpExtSDPEnable based on EnableFlag"""


_LcpExtSDPEnable_Object = MibTableColumn
lcpExtSDPEnable = _LcpExtSDPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 21),
    _LcpExtSDPEnable_Type()
)
lcpExtSDPEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtSDPEnable.setStatus("current")


class _LcpExtNumModeEnable_Type(EnableFlag):
    """Custom type lcpExtNumModeEnable based on EnableFlag"""


_LcpExtNumModeEnable_Object = MibTableColumn
lcpExtNumModeEnable = _LcpExtNumModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 2, 1, 22),
    _LcpExtNumModeEnable_Type()
)
lcpExtNumModeEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lcpExtNumModeEnable.setStatus("current")
_PppNCPExtensionsTable_Object = MibTable
pppNCPExtensionsTable = _PppNCPExtensionsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 3)
)
if mibBuilder.loadTexts:
    pppNCPExtensionsTable.setStatus("current")
_PppNCPExtensionsEntry_Object = MibTableRow
pppNCPExtensionsEntry = _PppNCPExtensionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 3, 1)
)
pppNCPExtensionsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppNCPExtensionsEntry.setStatus("current")


class _NcpExtVJCompMaxSlotID_Type(Integer32):
    """Custom type ncpExtVJCompMaxSlotID based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_NcpExtVJCompMaxSlotID_Type.__name__ = "Integer32"
_NcpExtVJCompMaxSlotID_Object = MibTableColumn
ncpExtVJCompMaxSlotID = _NcpExtVJCompMaxSlotID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 3, 1, 1),
    _NcpExtVJCompMaxSlotID_Type()
)
ncpExtVJCompMaxSlotID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncpExtVJCompMaxSlotID.setStatus("current")


class _NcpExtVJCompSlotID_Type(EnableFlag):
    """Custom type ncpExtVJCompSlotID based on EnableFlag"""


_NcpExtVJCompSlotID_Object = MibTableColumn
ncpExtVJCompSlotID = _NcpExtVJCompSlotID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 3, 1, 2),
    _NcpExtVJCompSlotID_Type()
)
ncpExtVJCompSlotID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncpExtVJCompSlotID.setStatus("current")


class _NcpExtIpAddrOptionEnable_Type(EnableFlag):
    """Custom type ncpExtIpAddrOptionEnable based on EnableFlag"""


_NcpExtIpAddrOptionEnable_Object = MibTableColumn
ncpExtIpAddrOptionEnable = _NcpExtIpAddrOptionEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 3, 1, 3),
    _NcpExtIpAddrOptionEnable_Type()
)
ncpExtIpAddrOptionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncpExtIpAddrOptionEnable.setStatus("current")


class _NcpExtRestartTimer_Type(Integer32):
    """Custom type ncpExtRestartTimer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_NcpExtRestartTimer_Type.__name__ = "Integer32"
_NcpExtRestartTimer_Object = MibTableColumn
ncpExtRestartTimer = _NcpExtRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 3, 1, 4),
    _NcpExtRestartTimer_Type()
)
ncpExtRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncpExtRestartTimer.setStatus("current")
if mibBuilder.loadTexts:
    ncpExtRestartTimer.setUnits("seconds")


class _NcpExtMaxConfigRetries_Type(Integer32):
    """Custom type ncpExtMaxConfigRetries based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_NcpExtMaxConfigRetries_Type.__name__ = "Integer32"
_NcpExtMaxConfigRetries_Object = MibTableColumn
ncpExtMaxConfigRetries = _NcpExtMaxConfigRetries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 3, 1, 5),
    _NcpExtMaxConfigRetries_Type()
)
ncpExtMaxConfigRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncpExtMaxConfigRetries.setStatus("current")


class _NcpExtMaxTerminateRetries_Type(Integer32):
    """Custom type ncpExtMaxTerminateRetries based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_NcpExtMaxTerminateRetries_Type.__name__ = "Integer32"
_NcpExtMaxTerminateRetries_Object = MibTableColumn
ncpExtMaxTerminateRetries = _NcpExtMaxTerminateRetries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 3, 1, 6),
    _NcpExtMaxTerminateRetries_Type()
)
ncpExtMaxTerminateRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncpExtMaxTerminateRetries.setStatus("current")


class _NcpExtFailureRetries_Type(Integer32):
    """Custom type ncpExtFailureRetries based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_NcpExtFailureRetries_Type.__name__ = "Integer32"
_NcpExtFailureRetries_Object = MibTableColumn
ncpExtFailureRetries = _NcpExtFailureRetries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 3, 1, 7),
    _NcpExtFailureRetries_Type()
)
ncpExtFailureRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncpExtFailureRetries.setStatus("current")


class _PppNextAuthId_Type(Integer32):
    """Custom type pppNextAuthId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PppNextAuthId_Type.__name__ = "Integer32"
_PppNextAuthId_Object = MibScalar
pppNextAuthId = _PppNextAuthId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 4),
    _PppNextAuthId_Type()
)
pppNextAuthId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppNextAuthId.setStatus("current")
_PppAuthenticationTable_Object = MibTable
pppAuthenticationTable = _PppAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 5)
)
if mibBuilder.loadTexts:
    pppAuthenticationTable.setStatus("current")
_PppAuthenticationEntry_Object = MibTableRow
pppAuthenticationEntry = _PppAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1)
)
pppAuthenticationEntry.setIndexNames(
    (0, "ZHONE-COM-PPP-MIB", "pppAuthSubId"),
    (0, "ZHONE-COM-PPP-MIB", "pppAuthId"),
)
if mibBuilder.loadTexts:
    pppAuthenticationEntry.setStatus("current")


class _PppAuthSubId_Type(Integer32):
    """Custom type pppAuthSubId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PppAuthSubId_Type.__name__ = "Integer32"
_PppAuthSubId_Object = MibTableColumn
pppAuthSubId = _PppAuthSubId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 1),
    _PppAuthSubId_Type()
)
pppAuthSubId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pppAuthSubId.setStatus("current")


class _PppAuthId_Type(Integer32):
    """Custom type pppAuthId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PppAuthId_Type.__name__ = "Integer32"
_PppAuthId_Object = MibTableColumn
pppAuthId = _PppAuthId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 2),
    _PppAuthId_Type()
)
pppAuthId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pppAuthId.setStatus("current")


class _PppAuthIpIfIndex_Type(InterfaceIndexOrZero):
    """Custom type pppAuthIpIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_PppAuthIpIfIndex_Object = MibTableColumn
pppAuthIpIfIndex = _PppAuthIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 3),
    _PppAuthIpIfIndex_Type()
)
pppAuthIpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppAuthIpIfIndex.setStatus("current")


class _PppAuthLgId_Type(InterfaceIndexOrZero):
    """Custom type pppAuthLgId based on InterfaceIndexOrZero"""
    defaultBinValue = 0


_PppAuthLgId_Object = MibTableColumn
pppAuthLgId = _PppAuthLgId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 4),
    _PppAuthLgId_Type()
)
pppAuthLgId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppAuthLgId.setStatus("current")


class _PppAuthProtocol_Type(Bits):
    """Custom type pppAuthProtocol based on Bits"""
    namedValues = NamedValues(
        *(("chap", 1),
          ("pap", 0))
    )

_PppAuthProtocol_Type.__name__ = "Bits"
_PppAuthProtocol_Object = MibTableColumn
pppAuthProtocol = _PppAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 5),
    _PppAuthProtocol_Type()
)
pppAuthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppAuthProtocol.setStatus("current")


class _PppAuthPAPPeerID_Type(OctetString):
    """Custom type pppAuthPAPPeerID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_PppAuthPAPPeerID_Type.__name__ = "OctetString"
_PppAuthPAPPeerID_Object = MibTableColumn
pppAuthPAPPeerID = _PppAuthPAPPeerID_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 6),
    _PppAuthPAPPeerID_Type()
)
pppAuthPAPPeerID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppAuthPAPPeerID.setStatus("current")


class _PppAuthPAPPassword_Type(OctetString):
    """Custom type pppAuthPAPPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_PppAuthPAPPassword_Type.__name__ = "OctetString"
_PppAuthPAPPassword_Object = MibTableColumn
pppAuthPAPPassword = _PppAuthPAPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 7),
    _PppAuthPAPPassword_Type()
)
pppAuthPAPPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppAuthPAPPassword.setStatus("current")


class _PppAuthCHAPName_Type(OctetString):
    """Custom type pppAuthCHAPName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_PppAuthCHAPName_Type.__name__ = "OctetString"
_PppAuthCHAPName_Object = MibTableColumn
pppAuthCHAPName = _PppAuthCHAPName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 8),
    _PppAuthCHAPName_Type()
)
pppAuthCHAPName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppAuthCHAPName.setStatus("current")


class _PppAuthCHAPSecret_Type(OctetString):
    """Custom type pppAuthCHAPSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_PppAuthCHAPSecret_Type.__name__ = "OctetString"
_PppAuthCHAPSecret_Object = MibTableColumn
pppAuthCHAPSecret = _PppAuthCHAPSecret_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 9),
    _PppAuthCHAPSecret_Type()
)
pppAuthCHAPSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppAuthCHAPSecret.setStatus("current")


class _PppAuthStatus_Type(Integer32):
    """Custom type pppAuthStatus based on Integer32"""
    defaultValue = 1

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


_PppAuthStatus_Type.__name__ = "Integer32"
_PppAuthStatus_Object = MibTableColumn
pppAuthStatus = _PppAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 10),
    _PppAuthStatus_Type()
)
pppAuthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppAuthStatus.setStatus("current")
_PppAuthRowStatus_Type = ZhoneRowStatus
_PppAuthRowStatus_Object = MibTableColumn
pppAuthRowStatus = _PppAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 5, 5, 1, 12),
    _PppAuthRowStatus_Type()
)
pppAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pppAuthRowStatus.setStatus("current")
pppInterfaceEntry.registerAugmentions(
    ("ZHONE-COM-PPP-MIB",
     "pppLCPExtensionsEntry")
)
pppLCPExtensionsEntry.setIndexNames(*pppInterfaceEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-PPP-MIB",
    **{"ZhoneAuthenticationProtocol": ZhoneAuthenticationProtocol,
       "EnableFlag": EnableFlag,
       "pppInterfaceTable": pppInterfaceTable,
       "pppInterfaceEntry": pppInterfaceEntry,
       "pppIfLowerIfIndex": pppIfLowerIfIndex,
       "pppIfVpi": pppIfVpi,
       "pppIfVci": pppIfVci,
       "pppIfCallMode": pppIfCallMode,
       "pppIfFrameType": pppIfFrameType,
       "pppIfNumChannels": pppIfNumChannels,
       "pppIfRowStatus": pppIfRowStatus,
       "pppLCPExtensionsTable": pppLCPExtensionsTable,
       "pppLCPExtensionsEntry": pppLCPExtensionsEntry,
       "lcpExtReceiveAuthEnable": lcpExtReceiveAuthEnable,
       "lcpExtReceiveAuthProtocol": lcpExtReceiveAuthProtocol,
       "lcpExtSendAuthEnable": lcpExtSendAuthEnable,
       "lcpExtSendAuthProtocol": lcpExtSendAuthProtocol,
       "lcpExtSendAuthIdentity": lcpExtSendAuthIdentity,
       "lcpExtQualityProtocol": lcpExtQualityProtocol,
       "lcpExtMagicNumber": lcpExtMagicNumber,
       "lcpExtMaxPad": lcpExtMaxPad,
       "lcpExtCallbackEnable": lcpExtCallbackEnable,
       "lcpExtCallbackType": lcpExtCallbackType,
       "lcpExtCallbackDialString": lcpExtCallbackDialString,
       "lcpExtRestartTimer": lcpExtRestartTimer,
       "lcpExtMaxConfigRetries": lcpExtMaxConfigRetries,
       "lcpExtMaxTerminateRetries": lcpExtMaxTerminateRetries,
       "lcpExtMaxFailureRetries": lcpExtMaxFailureRetries,
       "lcpExtMRUEnable": lcpExtMRUEnable,
       "lcpExtACCMEnable": lcpExtACCMEnable,
       "lcpExtPFCEnable": lcpExtPFCEnable,
       "lcpExtACFCEnable": lcpExtACFCEnable,
       "lcpExtFCSAltEnable": lcpExtFCSAltEnable,
       "lcpExtSDPEnable": lcpExtSDPEnable,
       "lcpExtNumModeEnable": lcpExtNumModeEnable,
       "pppNCPExtensionsTable": pppNCPExtensionsTable,
       "pppNCPExtensionsEntry": pppNCPExtensionsEntry,
       "ncpExtVJCompMaxSlotID": ncpExtVJCompMaxSlotID,
       "ncpExtVJCompSlotID": ncpExtVJCompSlotID,
       "ncpExtIpAddrOptionEnable": ncpExtIpAddrOptionEnable,
       "ncpExtRestartTimer": ncpExtRestartTimer,
       "ncpExtMaxConfigRetries": ncpExtMaxConfigRetries,
       "ncpExtMaxTerminateRetries": ncpExtMaxTerminateRetries,
       "ncpExtFailureRetries": ncpExtFailureRetries,
       "pppNextAuthId": pppNextAuthId,
       "pppAuthenticationTable": pppAuthenticationTable,
       "pppAuthenticationEntry": pppAuthenticationEntry,
       "pppAuthSubId": pppAuthSubId,
       "pppAuthId": pppAuthId,
       "pppAuthIpIfIndex": pppAuthIpIfIndex,
       "pppAuthLgId": pppAuthLgId,
       "pppAuthProtocol": pppAuthProtocol,
       "pppAuthPAPPeerID": pppAuthPAPPeerID,
       "pppAuthPAPPassword": pppAuthPAPPassword,
       "pppAuthCHAPName": pppAuthCHAPName,
       "pppAuthCHAPSecret": pppAuthCHAPSecret,
       "pppAuthStatus": pppAuthStatus,
       "pppAuthRowStatus": pppAuthRowStatus,
       "comPpp": comPpp}
)
