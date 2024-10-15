# SNMP MIB module (FLOWPOINT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FLOWPOINT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:10 2024
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



class IpxNetAddress(OctetString):
    """Custom type IpxNetAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class ConnectionType(Integer32):
    """Custom type ConnectionType based on Integer32"""
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
        *(("async", 1),
          ("dds", 4),
          ("fr", 3),
          ("isdn", 2),
          ("x25", 5))
    )





class AuthenProtoType(Integer32):
    """Custom type AuthenProtoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 3),
          ("none", 1),
          ("pap", 2))
    )





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )





class DhcpOptionType(Integer32):
    """Custom type DhcpOptionType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("binary", 6),
          ("byte", 2),
          ("ipaddress", 7),
          ("long", 4),
          ("longint", 5),
          ("none", 1),
          ("string", 8),
          ("word", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Flowpoint_ObjectIdentity = ObjectIdentity
flowpoint = _Flowpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1548)
)
_Fpdod_ObjectIdentity = ObjectIdentity
fpdod = _Fpdod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1548, 1)
)
_DodTable_Object = MibTable
dodTable = _DodTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1)
)
if mibBuilder.loadTexts:
    dodTable.setStatus("mandatory")
_DodEntry_Object = MibTableRow
dodEntry = _DodEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1)
)
dodEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dodDestinationName"),
)
if mibBuilder.loadTexts:
    dodEntry.setStatus("mandatory")
_DodTableID_Type = Integer32
_DodTableID_Object = MibTableColumn
dodTableID = _DodTableID_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 1),
    _DodTableID_Type()
)
dodTableID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodTableID.setStatus("obsolete")


class _DodDestinationName_Type(DisplayString):
    """Custom type dodDestinationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DodDestinationName_Type.__name__ = "DisplayString"
_DodDestinationName_Object = MibTableColumn
dodDestinationName = _DodDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 2),
    _DodDestinationName_Type()
)
dodDestinationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodDestinationName.setStatus("mandatory")


class _DodPassword_Type(DisplayString):
    """Custom type dodPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DodPassword_Type.__name__ = "DisplayString"
_DodPassword_Object = MibTableColumn
dodPassword = _DodPassword_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 3),
    _DodPassword_Type()
)
dodPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodPassword.setStatus("mandatory")
_DodAuthenProtocol_Type = AuthenProtoType
_DodAuthenProtocol_Object = MibTableColumn
dodAuthenProtocol = _DodAuthenProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 4),
    _DodAuthenProtocol_Type()
)
dodAuthenProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodAuthenProtocol.setStatus("mandatory")


class _DodMaxLinks_Type(Integer32):
    """Custom type dodMaxLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DodMaxLinks_Type.__name__ = "Integer32"
_DodMaxLinks_Object = MibTableColumn
dodMaxLinks = _DodMaxLinks_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 5),
    _DodMaxLinks_Type()
)
dodMaxLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodMaxLinks.setStatus("mandatory")


class _DodBWThreshold_Type(Integer32):
    """Custom type dodBWThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DodBWThreshold_Type.__name__ = "Integer32"
_DodBWThreshold_Object = MibTableColumn
dodBWThreshold = _DodBWThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 6),
    _DodBWThreshold_Type()
)
dodBWThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodBWThreshold.setStatus("mandatory")
_DodPreferType_Type = ConnectionType
_DodPreferType_Object = MibTableColumn
dodPreferType = _DodPreferType_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 7),
    _DodPreferType_Type()
)
dodPreferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodPreferType.setStatus("mandatory")
_DodTearDownTimer_Type = Integer32
_DodTearDownTimer_Object = MibTableColumn
dodTearDownTimer = _DodTearDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 8),
    _DodTearDownTimer_Type()
)
dodTearDownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodTearDownTimer.setStatus("mandatory")
_DodSourceIPAddress_Type = IpAddress
_DodSourceIPAddress_Object = MibTableColumn
dodSourceIPAddress = _DodSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 9),
    _DodSourceIPAddress_Type()
)
dodSourceIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodSourceIPAddress.setStatus("mandatory")
_DodRemoteIPAddress_Type = IpAddress
_DodRemoteIPAddress_Object = MibTableColumn
dodRemoteIPAddress = _DodRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 10),
    _DodRemoteIPAddress_Type()
)
dodRemoteIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodRemoteIPAddress.setStatus("mandatory")
_DodSourceIPMask_Type = IpAddress
_DodSourceIPMask_Object = MibTableColumn
dodSourceIPMask = _DodSourceIPMask_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 11),
    _DodSourceIPMask_Type()
)
dodSourceIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodSourceIPMask.setStatus("mandatory")
_DodRemoteIPMask_Type = IpAddress
_DodRemoteIPMask_Object = MibTableColumn
dodRemoteIPMask = _DodRemoteIPMask_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 12),
    _DodRemoteIPMask_Type()
)
dodRemoteIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodRemoteIPMask.setStatus("mandatory")
_DodIPXNetAddress_Type = IpxNetAddress
_DodIPXNetAddress_Object = MibTableColumn
dodIPXNetAddress = _DodIPXNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 13),
    _DodIPXNetAddress_Type()
)
dodIPXNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIPXNetAddress.setStatus("mandatory")
_DodIPFilters_Type = Counter32
_DodIPFilters_Object = MibTableColumn
dodIPFilters = _DodIPFilters_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 14),
    _DodIPFilters_Type()
)
dodIPFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodIPFilters.setStatus("mandatory")
_DodIPXFilters_Type = Counter32
_DodIPXFilters_Object = MibTableColumn
dodIPXFilters = _DodIPXFilters_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 15),
    _DodIPXFilters_Type()
)
dodIPXFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodIPXFilters.setStatus("mandatory")
_DodRemoteIPNets_Type = Counter32
_DodRemoteIPNets_Object = MibTableColumn
dodRemoteIPNets = _DodRemoteIPNets_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 16),
    _DodRemoteIPNets_Type()
)
dodRemoteIPNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodRemoteIPNets.setStatus("mandatory")
_DodRemoteIPXNets_Type = Counter32
_DodRemoteIPXNets_Object = MibTableColumn
dodRemoteIPXNets = _DodRemoteIPXNets_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 17),
    _DodRemoteIPXNets_Type()
)
dodRemoteIPXNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodRemoteIPXNets.setStatus("mandatory")
_DodRemoteIPXSAPs_Type = Counter32
_DodRemoteIPXSAPs_Object = MibTableColumn
dodRemoteIPXSAPs = _DodRemoteIPXSAPs_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 18),
    _DodRemoteIPXSAPs_Type()
)
dodRemoteIPXSAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodRemoteIPXSAPs.setStatus("mandatory")


class _DodRemoteMacState_Type(Integer32):
    """Custom type dodRemoteMacState based on Integer32"""
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


_DodRemoteMacState_Type.__name__ = "Integer32"
_DodRemoteMacState_Object = MibTableColumn
dodRemoteMacState = _DodRemoteMacState_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 19),
    _DodRemoteMacState_Type()
)
dodRemoteMacState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodRemoteMacState.setStatus("mandatory")
_DodRemoteMacs_Type = Counter32
_DodRemoteMacs_Object = MibTableColumn
dodRemoteMacs = _DodRemoteMacs_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 20),
    _DodRemoteMacs_Type()
)
dodRemoteMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodRemoteMacs.setStatus("mandatory")
_DodLastActivityTime_Type = Integer32
_DodLastActivityTime_Object = MibTableColumn
dodLastActivityTime = _DodLastActivityTime_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 21),
    _DodLastActivityTime_Type()
)
dodLastActivityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodLastActivityTime.setStatus("mandatory")


class _DodTableOperation_Type(Integer32):
    """Custom type dodTableOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("remove", 2))
    )


_DodTableOperation_Type.__name__ = "Integer32"
_DodTableOperation_Object = MibTableColumn
dodTableOperation = _DodTableOperation_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 22),
    _DodTableOperation_Type()
)
dodTableOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dodTableOperation.setStatus("mandatory")


class _DodMinLinks_Type(Integer32):
    """Custom type dodMinLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_DodMinLinks_Type.__name__ = "Integer32"
_DodMinLinks_Object = MibTableColumn
dodMinLinks = _DodMinLinks_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 23),
    _DodMinLinks_Type()
)
dodMinLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodMinLinks.setStatus("mandatory")


class _DodBODType_Type(Integer32):
    """Custom type dodBODType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("input", 3),
          ("output", 2))
    )


_DodBODType_Type.__name__ = "Integer32"
_DodBODType_Object = MibTableColumn
dodBODType = _DodBODType_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 24),
    _DodBODType_Type()
)
dodBODType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodBODType.setStatus("mandatory")


class _DodIpOptRecvRIP_Type(Integer32):
    """Custom type dodIpOptRecvRIP based on Integer32"""
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


_DodIpOptRecvRIP_Type.__name__ = "Integer32"
_DodIpOptRecvRIP_Object = MibTableColumn
dodIpOptRecvRIP = _DodIpOptRecvRIP_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 25),
    _DodIpOptRecvRIP_Type()
)
dodIpOptRecvRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIpOptRecvRIP.setStatus("mandatory")


class _DodIpOptSendRIP_Type(Integer32):
    """Custom type dodIpOptSendRIP based on Integer32"""
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


_DodIpOptSendRIP_Type.__name__ = "Integer32"
_DodIpOptSendRIP_Object = MibTableColumn
dodIpOptSendRIP = _DodIpOptSendRIP_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 26),
    _DodIpOptSendRIP_Type()
)
dodIpOptSendRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIpOptSendRIP.setStatus("mandatory")


class _DodIpOptRecvRIPDefault_Type(Integer32):
    """Custom type dodIpOptRecvRIPDefault based on Integer32"""
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


_DodIpOptRecvRIPDefault_Type.__name__ = "Integer32"
_DodIpOptRecvRIPDefault_Object = MibTableColumn
dodIpOptRecvRIPDefault = _DodIpOptRecvRIPDefault_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 27),
    _DodIpOptRecvRIPDefault_Type()
)
dodIpOptRecvRIPDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIpOptRecvRIPDefault.setStatus("mandatory")


class _DodIpOptSendRIPDefault_Type(Integer32):
    """Custom type dodIpOptSendRIPDefault based on Integer32"""
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


_DodIpOptSendRIPDefault_Type.__name__ = "Integer32"
_DodIpOptSendRIPDefault_Object = MibTableColumn
dodIpOptSendRIPDefault = _DodIpOptSendRIPDefault_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 28),
    _DodIpOptSendRIPDefault_Type()
)
dodIpOptSendRIPDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIpOptSendRIPDefault.setStatus("mandatory")


class _DodIpOptKeepPrivate_Type(Integer32):
    """Custom type dodIpOptKeepPrivate based on Integer32"""
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


_DodIpOptKeepPrivate_Type.__name__ = "Integer32"
_DodIpOptKeepPrivate_Object = MibTableColumn
dodIpOptKeepPrivate = _DodIpOptKeepPrivate_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 29),
    _DodIpOptKeepPrivate_Type()
)
dodIpOptKeepPrivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIpOptKeepPrivate.setStatus("mandatory")


class _DodBrOptUseStp_Type(Integer32):
    """Custom type dodBrOptUseStp based on Integer32"""
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


_DodBrOptUseStp_Type.__name__ = "Integer32"
_DodBrOptUseStp_Object = MibTableColumn
dodBrOptUseStp = _DodBrOptUseStp_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 30),
    _DodBrOptUseStp_Type()
)
dodBrOptUseStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodBrOptUseStp.setStatus("mandatory")


class _DodPPPOptUseLCPEcho_Type(Integer32):
    """Custom type dodPPPOptUseLCPEcho based on Integer32"""
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


_DodPPPOptUseLCPEcho_Type.__name__ = "Integer32"
_DodPPPOptUseLCPEcho_Object = MibTableColumn
dodPPPOptUseLCPEcho = _DodPPPOptUseLCPEcho_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 31),
    _DodPPPOptUseLCPEcho_Type()
)
dodPPPOptUseLCPEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodPPPOptUseLCPEcho.setStatus("mandatory")


class _DodEntryIsDisabled_Type(Integer32):
    """Custom type dodEntryIsDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_DodEntryIsDisabled_Type.__name__ = "Integer32"
_DodEntryIsDisabled_Object = MibTableColumn
dodEntryIsDisabled = _DodEntryIsDisabled_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 32),
    _DodEntryIsDisabled_Type()
)
dodEntryIsDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodEntryIsDisabled.setStatus("mandatory")


class _DodCallbackOption_Type(Integer32):
    """Custom type dodCallbackOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("callback-only", 3),
          ("disable", 2),
          ("enable", 1))
    )


_DodCallbackOption_Type.__name__ = "Integer32"
_DodCallbackOption_Object = MibTableColumn
dodCallbackOption = _DodCallbackOption_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 33),
    _DodCallbackOption_Type()
)
dodCallbackOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodCallbackOption.setStatus("mandatory")


class _DodSendDataAsVoice_Type(Integer32):
    """Custom type dodSendDataAsVoice based on Integer32"""
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


_DodSendDataAsVoice_Type.__name__ = "Integer32"
_DodSendDataAsVoice_Object = MibTableColumn
dodSendDataAsVoice = _DodSendDataAsVoice_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 34),
    _DodSendDataAsVoice_Type()
)
dodSendDataAsVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodSendDataAsVoice.setStatus("mandatory")


class _DodIPXNetStrAddress_Type(DisplayString):
    """Custom type dodIPXNetStrAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_DodIPXNetStrAddress_Type.__name__ = "DisplayString"
_DodIPXNetStrAddress_Object = MibTableColumn
dodIPXNetStrAddress = _DodIPXNetStrAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 35),
    _DodIPXNetStrAddress_Type()
)
dodIPXNetStrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIPXNetStrAddress.setStatus("mandatory")


class _DodOurSystemName_Type(DisplayString):
    """Custom type dodOurSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DodOurSystemName_Type.__name__ = "DisplayString"
_DodOurSystemName_Object = MibTableColumn
dodOurSystemName = _DodOurSystemName_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 36),
    _DodOurSystemName_Type()
)
dodOurSystemName.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dodOurSystemName.setStatus("mandatory")


class _DodOurPassword_Type(DisplayString):
    """Custom type dodOurPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DodOurPassword_Type.__name__ = "DisplayString"
_DodOurPassword_Object = MibTableColumn
dodOurPassword = _DodOurPassword_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 37),
    _DodOurPassword_Type()
)
dodOurPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodOurPassword.setStatus("mandatory")


class _DodPPPCallbackOption_Type(Integer32):
    """Custom type dodPPPCallbackOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("authentication", 2),
          ("dial-string", 3),
          ("e164-string", 5),
          ("location-string", 4),
          ("name-string", 6),
          ("none", 1))
    )


_DodPPPCallbackOption_Type.__name__ = "Integer32"
_DodPPPCallbackOption_Object = MibTableColumn
dodPPPCallbackOption = _DodPPPCallbackOption_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 38),
    _DodPPPCallbackOption_Type()
)
dodPPPCallbackOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodPPPCallbackOption.setStatus("mandatory")


class _DodPPPCallbackInfo_Type(DisplayString):
    """Custom type dodPPPCallbackInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DodPPPCallbackInfo_Type.__name__ = "DisplayString"
_DodPPPCallbackInfo_Object = MibTableColumn
dodPPPCallbackInfo = _DodPPPCallbackInfo_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 39),
    _DodPPPCallbackInfo_Type()
)
dodPPPCallbackInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodPPPCallbackInfo.setStatus("mandatory")


class _DodDontAuthenticate_Type(Integer32):
    """Custom type dodDontAuthenticate based on Integer32"""
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


_DodDontAuthenticate_Type.__name__ = "Integer32"
_DodDontAuthenticate_Object = MibTableColumn
dodDontAuthenticate = _DodDontAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 40),
    _DodDontAuthenticate_Type()
)
dodDontAuthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodDontAuthenticate.setStatus("mandatory")


class _DodIPAddressTranslation_Type(Integer32):
    """Custom type dodIPAddressTranslation based on Integer32"""
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


_DodIPAddressTranslation_Type.__name__ = "Integer32"
_DodIPAddressTranslation_Object = MibTableColumn
dodIPAddressTranslation = _DodIPAddressTranslation_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 41),
    _DodIPAddressTranslation_Type()
)
dodIPAddressTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIPAddressTranslation.setStatus("mandatory")


class _DodIpOptRecvRIP1_Type(Integer32):
    """Custom type dodIpOptRecvRIP1 based on Integer32"""
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


_DodIpOptRecvRIP1_Type.__name__ = "Integer32"
_DodIpOptRecvRIP1_Object = MibTableColumn
dodIpOptRecvRIP1 = _DodIpOptRecvRIP1_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 42),
    _DodIpOptRecvRIP1_Type()
)
dodIpOptRecvRIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIpOptRecvRIP1.setStatus("mandatory")


class _DodIpOptSendRIP1_Type(Integer32):
    """Custom type dodIpOptSendRIP1 based on Integer32"""
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


_DodIpOptSendRIP1_Type.__name__ = "Integer32"
_DodIpOptSendRIP1_Object = MibTableColumn
dodIpOptSendRIP1 = _DodIpOptSendRIP1_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 43),
    _DodIpOptSendRIP1_Type()
)
dodIpOptSendRIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIpOptSendRIP1.setStatus("mandatory")


class _DodIpOptRecvRIP2_Type(Integer32):
    """Custom type dodIpOptRecvRIP2 based on Integer32"""
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


_DodIpOptRecvRIP2_Type.__name__ = "Integer32"
_DodIpOptRecvRIP2_Object = MibTableColumn
dodIpOptRecvRIP2 = _DodIpOptRecvRIP2_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 44),
    _DodIpOptRecvRIP2_Type()
)
dodIpOptRecvRIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIpOptRecvRIP2.setStatus("mandatory")


class _DodIpOptSendRIP2_Type(Integer32):
    """Custom type dodIpOptSendRIP2 based on Integer32"""
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


_DodIpOptSendRIP2_Type.__name__ = "Integer32"
_DodIpOptSendRIP2_Object = MibTableColumn
dodIpOptSendRIP2 = _DodIpOptSendRIP2_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 45),
    _DodIpOptSendRIP2_Type()
)
dodIpOptSendRIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIpOptSendRIP2.setStatus("mandatory")


class _DodProtocol_Type(Integer32):
    """Custom type dodProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("protocol1483pppllc", 2),
          ("protocol1483snap", 3),
          ("protocol1483snapfr", 5),
          ("protocol1483snapmer", 4),
          ("protocolppp", 1),
          ("protocolrawip", 6))
    )


_DodProtocol_Type.__name__ = "Integer32"
_DodProtocol_Object = MibTableColumn
dodProtocol = _DodProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 46),
    _DodProtocol_Type()
)
dodProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodProtocol.setStatus("mandatory")


class _DodCompression_Type(Integer32):
    """Custom type dodCompression based on Integer32"""
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


_DodCompression_Type.__name__ = "Integer32"
_DodCompression_Object = MibTableColumn
dodCompression = _DodCompression_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 47),
    _DodCompression_Type()
)
dodCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodCompression.setStatus("mandatory")


class _DodPasswordSpecified_Type(Integer32):
    """Custom type dodPasswordSpecified based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_DodPasswordSpecified_Type.__name__ = "Integer32"
_DodPasswordSpecified_Object = MibTableColumn
dodPasswordSpecified = _DodPasswordSpecified_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 48),
    _DodPasswordSpecified_Type()
)
dodPasswordSpecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodPasswordSpecified.setStatus("mandatory")


class _DodOurPasswordSpecified_Type(Integer32):
    """Custom type dodOurPasswordSpecified based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_DodOurPasswordSpecified_Type.__name__ = "Integer32"
_DodOurPasswordSpecified_Object = MibTableColumn
dodOurPasswordSpecified = _DodOurPasswordSpecified_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 49),
    _DodOurPasswordSpecified_Type()
)
dodOurPasswordSpecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodOurPasswordSpecified.setStatus("mandatory")


class _DodBlockNetBIOS_Type(Integer32):
    """Custom type dodBlockNetBIOS based on Integer32"""
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


_DodBlockNetBIOS_Type.__name__ = "Integer32"
_DodBlockNetBIOS_Object = MibTableColumn
dodBlockNetBIOS = _DodBlockNetBIOS_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 50),
    _DodBlockNetBIOS_Type()
)
dodBlockNetBIOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodBlockNetBIOS.setStatus("mandatory")
_DodMtu_Type = Integer32
_DodMtu_Object = MibTableColumn
dodMtu = _DodMtu_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 51),
    _DodMtu_Type()
)
dodMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodMtu.setStatus("mandatory")


class _DodIpSlaveMode_Type(Integer32):
    """Custom type dodIpSlaveMode based on Integer32"""
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


_DodIpSlaveMode_Type.__name__ = "Integer32"
_DodIpSlaveMode_Object = MibTableColumn
dodIpSlaveMode = _DodIpSlaveMode_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 52),
    _DodIpSlaveMode_Type()
)
dodIpSlaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIpSlaveMode.setStatus("mandatory")


class _DodReacquireIpAddr_Type(Integer32):
    """Custom type dodReacquireIpAddr based on Integer32"""
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


_DodReacquireIpAddr_Type.__name__ = "Integer32"
_DodReacquireIpAddr_Object = MibTableColumn
dodReacquireIpAddr = _DodReacquireIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 53),
    _DodReacquireIpAddr_Type()
)
dodReacquireIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodReacquireIpAddr.setStatus("mandatory")


class _DodIpxOptRIPSAP_Type(Integer32):
    """Custom type dodIpxOptRIPSAP based on Integer32"""
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


_DodIpxOptRIPSAP_Type.__name__ = "Integer32"
_DodIpxOptRIPSAP_Object = MibTableColumn
dodIpxOptRIPSAP = _DodIpxOptRIPSAP_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 1, 1, 54),
    _DodIpxOptRIPSAP_Type()
)
dodIpxOptRIPSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIpxOptRIPSAP.setStatus("mandatory")
_DodCallIDTable_Object = MibTable
dodCallIDTable = _DodCallIDTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 2)
)
if mibBuilder.loadTexts:
    dodCallIDTable.setStatus("mandatory")
_DodCallIDEntry_Object = MibTableRow
dodCallIDEntry = _DodCallIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 2, 1)
)
dodCallIDEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dodDestinationName"),
    (0, "FLOWPOINT-MIB", "dodCallIDType"),
)
if mibBuilder.loadTexts:
    dodCallIDEntry.setStatus("mandatory")
_DodCallIDType_Type = ConnectionType
_DodCallIDType_Object = MibTableColumn
dodCallIDType = _DodCallIDType_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 2, 1, 1),
    _DodCallIDType_Type()
)
dodCallIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodCallIDType.setStatus("mandatory")
_DodCallIDPhones_Type = Counter32
_DodCallIDPhones_Object = MibTableColumn
dodCallIDPhones = _DodCallIDPhones_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 2, 1, 2),
    _DodCallIDPhones_Type()
)
dodCallIDPhones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodCallIDPhones.setStatus("mandatory")
_DodPhoneTable_Object = MibTable
dodPhoneTable = _DodPhoneTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 3)
)
if mibBuilder.loadTexts:
    dodPhoneTable.setStatus("mandatory")
_DodPhoneEntry_Object = MibTableRow
dodPhoneEntry = _DodPhoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 3, 1)
)
dodPhoneEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dodDestinationName"),
    (0, "FLOWPOINT-MIB", "dodCallIDType"),
    (0, "FLOWPOINT-MIB", "dodPhoneIndex"),
)
if mibBuilder.loadTexts:
    dodPhoneEntry.setStatus("mandatory")


class _DodPhoneIndex_Type(Integer32):
    """Custom type dodPhoneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DodPhoneIndex_Type.__name__ = "Integer32"
_DodPhoneIndex_Object = MibTableColumn
dodPhoneIndex = _DodPhoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 3, 1, 1),
    _DodPhoneIndex_Type()
)
dodPhoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodPhoneIndex.setStatus("mandatory")
_DodPhoneSpeed_Type = Integer32
_DodPhoneSpeed_Object = MibTableColumn
dodPhoneSpeed = _DodPhoneSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 3, 1, 2),
    _DodPhoneSpeed_Type()
)
dodPhoneSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodPhoneSpeed.setStatus("mandatory")


class _DodPhoneNumber_Type(DisplayString):
    """Custom type dodPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DodPhoneNumber_Type.__name__ = "DisplayString"
_DodPhoneNumber_Object = MibTableColumn
dodPhoneNumber = _DodPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 3, 1, 3),
    _DodPhoneNumber_Type()
)
dodPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodPhoneNumber.setStatus("mandatory")
_DodRemoteMacTable_Object = MibTable
dodRemoteMacTable = _DodRemoteMacTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 4)
)
if mibBuilder.loadTexts:
    dodRemoteMacTable.setStatus("mandatory")
_DodRemoteMacEntry_Object = MibTableRow
dodRemoteMacEntry = _DodRemoteMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 4, 1)
)
dodRemoteMacEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dodDestinationName"),
    (0, "FLOWPOINT-MIB", "dodRemoteMacAddress"),
)
if mibBuilder.loadTexts:
    dodRemoteMacEntry.setStatus("mandatory")
_DodRemoteMacIndex_Type = Integer32
_DodRemoteMacIndex_Object = MibTableColumn
dodRemoteMacIndex = _DodRemoteMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 4, 1, 1),
    _DodRemoteMacIndex_Type()
)
dodRemoteMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodRemoteMacIndex.setStatus("obsolete")
_DodRemoteMacAddress_Type = MacAddress
_DodRemoteMacAddress_Object = MibTableColumn
dodRemoteMacAddress = _DodRemoteMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 4, 1, 2),
    _DodRemoteMacAddress_Type()
)
dodRemoteMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodRemoteMacAddress.setStatus("mandatory")


class _DodRemoteMacOperation_Type(Integer32):
    """Custom type dodRemoteMacOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("remove", 2))
    )


_DodRemoteMacOperation_Type.__name__ = "Integer32"
_DodRemoteMacOperation_Object = MibTableColumn
dodRemoteMacOperation = _DodRemoteMacOperation_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 4, 1, 3),
    _DodRemoteMacOperation_Type()
)
dodRemoteMacOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dodRemoteMacOperation.setStatus("mandatory")
_DodRemoteIPNetTable_Object = MibTable
dodRemoteIPNetTable = _DodRemoteIPNetTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 5)
)
if mibBuilder.loadTexts:
    dodRemoteIPNetTable.setStatus("mandatory")
_DodRemoteIPNetEntry_Object = MibTableRow
dodRemoteIPNetEntry = _DodRemoteIPNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 5, 1)
)
dodRemoteIPNetEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dodDestinationName"),
    (0, "FLOWPOINT-MIB", "dodRemoteIPNetAddress"),
)
if mibBuilder.loadTexts:
    dodRemoteIPNetEntry.setStatus("mandatory")
_DodRemoteIPNetIndex_Type = Integer32
_DodRemoteIPNetIndex_Object = MibTableColumn
dodRemoteIPNetIndex = _DodRemoteIPNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 5, 1, 1),
    _DodRemoteIPNetIndex_Type()
)
dodRemoteIPNetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodRemoteIPNetIndex.setStatus("obsolete")
_DodRemoteIPNetAddress_Type = IpAddress
_DodRemoteIPNetAddress_Object = MibTableColumn
dodRemoteIPNetAddress = _DodRemoteIPNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 5, 1, 2),
    _DodRemoteIPNetAddress_Type()
)
dodRemoteIPNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodRemoteIPNetAddress.setStatus("mandatory")
_DodRemoteIPNetMask_Type = IpAddress
_DodRemoteIPNetMask_Object = MibTableColumn
dodRemoteIPNetMask = _DodRemoteIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 5, 1, 3),
    _DodRemoteIPNetMask_Type()
)
dodRemoteIPNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodRemoteIPNetMask.setStatus("mandatory")


class _DodRemoteIPNetHops_Type(Integer32):
    """Custom type dodRemoteIPNetHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_DodRemoteIPNetHops_Type.__name__ = "Integer32"
_DodRemoteIPNetHops_Object = MibTableColumn
dodRemoteIPNetHops = _DodRemoteIPNetHops_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 5, 1, 4),
    _DodRemoteIPNetHops_Type()
)
dodRemoteIPNetHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodRemoteIPNetHops.setStatus("mandatory")


class _DodRemoteIPNetOperation_Type(Integer32):
    """Custom type dodRemoteIPNetOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("remove", 2))
    )


_DodRemoteIPNetOperation_Type.__name__ = "Integer32"
_DodRemoteIPNetOperation_Object = MibTableColumn
dodRemoteIPNetOperation = _DodRemoteIPNetOperation_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 5, 1, 5),
    _DodRemoteIPNetOperation_Type()
)
dodRemoteIPNetOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dodRemoteIPNetOperation.setStatus("mandatory")
_DodRemoteIPNetGateway_Type = IpAddress
_DodRemoteIPNetGateway_Object = MibTableColumn
dodRemoteIPNetGateway = _DodRemoteIPNetGateway_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 5, 1, 6),
    _DodRemoteIPNetGateway_Type()
)
dodRemoteIPNetGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodRemoteIPNetGateway.setStatus("mandatory")
_DodRemoteIPXNetTable_Object = MibTable
dodRemoteIPXNetTable = _DodRemoteIPXNetTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 6)
)
if mibBuilder.loadTexts:
    dodRemoteIPXNetTable.setStatus("mandatory")
_DodRemoteIPXNetEntry_Object = MibTableRow
dodRemoteIPXNetEntry = _DodRemoteIPXNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 6, 1)
)
dodRemoteIPXNetEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dodDestinationName"),
    (0, "FLOWPOINT-MIB", "dodRemoteIPXNetAddress"),
)
if mibBuilder.loadTexts:
    dodRemoteIPXNetEntry.setStatus("mandatory")
_DodRemoteIPXNetIndex_Type = Integer32
_DodRemoteIPXNetIndex_Object = MibTableColumn
dodRemoteIPXNetIndex = _DodRemoteIPXNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 6, 1, 1),
    _DodRemoteIPXNetIndex_Type()
)
dodRemoteIPXNetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodRemoteIPXNetIndex.setStatus("obsolete")
_DodRemoteIPXNetAddress_Type = IpxNetAddress
_DodRemoteIPXNetAddress_Object = MibTableColumn
dodRemoteIPXNetAddress = _DodRemoteIPXNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 6, 1, 2),
    _DodRemoteIPXNetAddress_Type()
)
dodRemoteIPXNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodRemoteIPXNetAddress.setStatus("mandatory")


class _DodRemoteIPXNetMetric_Type(Integer32):
    """Custom type dodRemoteIPXNetMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_DodRemoteIPXNetMetric_Type.__name__ = "Integer32"
_DodRemoteIPXNetMetric_Object = MibTableColumn
dodRemoteIPXNetMetric = _DodRemoteIPXNetMetric_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 6, 1, 3),
    _DodRemoteIPXNetMetric_Type()
)
dodRemoteIPXNetMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodRemoteIPXNetMetric.setStatus("mandatory")
_DodRemoteIPXNetTicks_Type = Integer32
_DodRemoteIPXNetTicks_Object = MibTableColumn
dodRemoteIPXNetTicks = _DodRemoteIPXNetTicks_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 6, 1, 4),
    _DodRemoteIPXNetTicks_Type()
)
dodRemoteIPXNetTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodRemoteIPXNetTicks.setStatus("mandatory")


class _DodRemoteIPXNetOperation_Type(Integer32):
    """Custom type dodRemoteIPXNetOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("remove", 2))
    )


_DodRemoteIPXNetOperation_Type.__name__ = "Integer32"
_DodRemoteIPXNetOperation_Object = MibTableColumn
dodRemoteIPXNetOperation = _DodRemoteIPXNetOperation_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 6, 1, 5),
    _DodRemoteIPXNetOperation_Type()
)
dodRemoteIPXNetOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dodRemoteIPXNetOperation.setStatus("mandatory")


class _DodRemoteIPXNetStrAddress_Type(DisplayString):
    """Custom type dodRemoteIPXNetStrAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_DodRemoteIPXNetStrAddress_Type.__name__ = "DisplayString"
_DodRemoteIPXNetStrAddress_Object = MibTableColumn
dodRemoteIPXNetStrAddress = _DodRemoteIPXNetStrAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 6, 1, 6),
    _DodRemoteIPXNetStrAddress_Type()
)
dodRemoteIPXNetStrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodRemoteIPXNetStrAddress.setStatus("mandatory")
_DodRemoteIPXSAPTable_Object = MibTable
dodRemoteIPXSAPTable = _DodRemoteIPXSAPTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 7)
)
if mibBuilder.loadTexts:
    dodRemoteIPXSAPTable.setStatus("mandatory")
_DodRemoteIPXSAPEntry_Object = MibTableRow
dodRemoteIPXSAPEntry = _DodRemoteIPXSAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 7, 1)
)
dodRemoteIPXSAPEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dodDestinationName"),
    (0, "FLOWPOINT-MIB", "dodRemoteIPXSAPNetAddress"),
    (0, "FLOWPOINT-MIB", "dodRemoteIPXSAPNodeAddress"),
    (0, "FLOWPOINT-MIB", "dodRemoteIPXSAPSocket"),
)
if mibBuilder.loadTexts:
    dodRemoteIPXSAPEntry.setStatus("mandatory")
_DodRemoteIPXSAPIndex_Type = Integer32
_DodRemoteIPXSAPIndex_Object = MibTableColumn
dodRemoteIPXSAPIndex = _DodRemoteIPXSAPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 7, 1, 1),
    _DodRemoteIPXSAPIndex_Type()
)
dodRemoteIPXSAPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodRemoteIPXSAPIndex.setStatus("obsolete")


class _DodRemoteIPXSAPName_Type(DisplayString):
    """Custom type dodRemoteIPXSAPName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_DodRemoteIPXSAPName_Type.__name__ = "DisplayString"
_DodRemoteIPXSAPName_Object = MibTableColumn
dodRemoteIPXSAPName = _DodRemoteIPXSAPName_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 7, 1, 2),
    _DodRemoteIPXSAPName_Type()
)
dodRemoteIPXSAPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodRemoteIPXSAPName.setStatus("mandatory")
_DodRemoteIPXSAPNetAddress_Type = IpxNetAddress
_DodRemoteIPXSAPNetAddress_Object = MibTableColumn
dodRemoteIPXSAPNetAddress = _DodRemoteIPXSAPNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 7, 1, 3),
    _DodRemoteIPXSAPNetAddress_Type()
)
dodRemoteIPXSAPNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodRemoteIPXSAPNetAddress.setStatus("mandatory")
_DodRemoteIPXSAPNodeAddress_Type = MacAddress
_DodRemoteIPXSAPNodeAddress_Object = MibTableColumn
dodRemoteIPXSAPNodeAddress = _DodRemoteIPXSAPNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 7, 1, 4),
    _DodRemoteIPXSAPNodeAddress_Type()
)
dodRemoteIPXSAPNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodRemoteIPXSAPNodeAddress.setStatus("mandatory")


class _DodRemoteIPXSAPSocket_Type(OctetString):
    """Custom type dodRemoteIPXSAPSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DodRemoteIPXSAPSocket_Type.__name__ = "OctetString"
_DodRemoteIPXSAPSocket_Object = MibTableColumn
dodRemoteIPXSAPSocket = _DodRemoteIPXSAPSocket_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 7, 1, 5),
    _DodRemoteIPXSAPSocket_Type()
)
dodRemoteIPXSAPSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodRemoteIPXSAPSocket.setStatus("mandatory")


class _DodRemoteIPXSAPType_Type(OctetString):
    """Custom type dodRemoteIPXSAPType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DodRemoteIPXSAPType_Type.__name__ = "OctetString"
_DodRemoteIPXSAPType_Object = MibTableColumn
dodRemoteIPXSAPType = _DodRemoteIPXSAPType_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 7, 1, 6),
    _DodRemoteIPXSAPType_Type()
)
dodRemoteIPXSAPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodRemoteIPXSAPType.setStatus("mandatory")


class _DodRemoteIPXSAPHops_Type(Integer32):
    """Custom type dodRemoteIPXSAPHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_DodRemoteIPXSAPHops_Type.__name__ = "Integer32"
_DodRemoteIPXSAPHops_Object = MibTableColumn
dodRemoteIPXSAPHops = _DodRemoteIPXSAPHops_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 7, 1, 7),
    _DodRemoteIPXSAPHops_Type()
)
dodRemoteIPXSAPHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodRemoteIPXSAPHops.setStatus("mandatory")


class _DodRemoteIPXSAPOperation_Type(Integer32):
    """Custom type dodRemoteIPXSAPOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("remove", 2))
    )


_DodRemoteIPXSAPOperation_Type.__name__ = "Integer32"
_DodRemoteIPXSAPOperation_Object = MibTableColumn
dodRemoteIPXSAPOperation = _DodRemoteIPXSAPOperation_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 7, 1, 9),
    _DodRemoteIPXSAPOperation_Type()
)
dodRemoteIPXSAPOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dodRemoteIPXSAPOperation.setStatus("mandatory")


class _DodRemoteIPXSAPStrNetAddress_Type(DisplayString):
    """Custom type dodRemoteIPXSAPStrNetAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_DodRemoteIPXSAPStrNetAddress_Type.__name__ = "DisplayString"
_DodRemoteIPXSAPStrNetAddress_Object = MibTableColumn
dodRemoteIPXSAPStrNetAddress = _DodRemoteIPXSAPStrNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 7, 1, 10),
    _DodRemoteIPXSAPStrNetAddress_Type()
)
dodRemoteIPXSAPStrNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodRemoteIPXSAPStrNetAddress.setStatus("mandatory")


class _DodRemoteIPXSAPStrSocket_Type(DisplayString):
    """Custom type dodRemoteIPXSAPStrSocket based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_DodRemoteIPXSAPStrSocket_Type.__name__ = "DisplayString"
_DodRemoteIPXSAPStrSocket_Object = MibTableColumn
dodRemoteIPXSAPStrSocket = _DodRemoteIPXSAPStrSocket_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 7, 1, 11),
    _DodRemoteIPXSAPStrSocket_Type()
)
dodRemoteIPXSAPStrSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodRemoteIPXSAPStrSocket.setStatus("mandatory")


class _DodRemoteIPXSAPStrType_Type(DisplayString):
    """Custom type dodRemoteIPXSAPStrType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_DodRemoteIPXSAPStrType_Type.__name__ = "DisplayString"
_DodRemoteIPXSAPStrType_Object = MibTableColumn
dodRemoteIPXSAPStrType = _DodRemoteIPXSAPStrType_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 7, 1, 12),
    _DodRemoteIPXSAPStrType_Type()
)
dodRemoteIPXSAPStrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodRemoteIPXSAPStrType.setStatus("mandatory")
_DodIPFilterTable_Object = MibTable
dodIPFilterTable = _DodIPFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 8)
)
if mibBuilder.loadTexts:
    dodIPFilterTable.setStatus("mandatory")
_DodIPFilterEntry_Object = MibTableRow
dodIPFilterEntry = _DodIPFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 8, 1)
)
dodIPFilterEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dodDestinationName"),
    (0, "FLOWPOINT-MIB", "dodIPFilterIndex"),
)
if mibBuilder.loadTexts:
    dodIPFilterEntry.setStatus("mandatory")


class _DodIPFilterIndex_Type(Integer32):
    """Custom type dodIPFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_DodIPFilterIndex_Type.__name__ = "Integer32"
_DodIPFilterIndex_Object = MibTableColumn
dodIPFilterIndex = _DodIPFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 8, 1, 1),
    _DodIPFilterIndex_Type()
)
dodIPFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodIPFilterIndex.setStatus("mandatory")
_DodIPFilterDstNetAddr_Type = IpAddress
_DodIPFilterDstNetAddr_Object = MibTableColumn
dodIPFilterDstNetAddr = _DodIPFilterDstNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 8, 1, 2),
    _DodIPFilterDstNetAddr_Type()
)
dodIPFilterDstNetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIPFilterDstNetAddr.setStatus("mandatory")
_DodIPFilterSrcNetAddr_Type = IpAddress
_DodIPFilterSrcNetAddr_Object = MibTableColumn
dodIPFilterSrcNetAddr = _DodIPFilterSrcNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 8, 1, 3),
    _DodIPFilterSrcNetAddr_Type()
)
dodIPFilterSrcNetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIPFilterSrcNetAddr.setStatus("mandatory")


class _DodIPFilterAllow_Type(Integer32):
    """Custom type dodIPFilterAllow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_DodIPFilterAllow_Type.__name__ = "Integer32"
_DodIPFilterAllow_Object = MibTableColumn
dodIPFilterAllow = _DodIPFilterAllow_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 8, 1, 4),
    _DodIPFilterAllow_Type()
)
dodIPFilterAllow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIPFilterAllow.setStatus("mandatory")
_DodIPXFilterTable_Object = MibTable
dodIPXFilterTable = _DodIPXFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 9)
)
if mibBuilder.loadTexts:
    dodIPXFilterTable.setStatus("mandatory")
_DodIPXFilterEntry_Object = MibTableRow
dodIPXFilterEntry = _DodIPXFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 9, 1)
)
dodIPXFilterEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dodDestinationName"),
    (0, "FLOWPOINT-MIB", "dodIPXFilterIndex"),
)
if mibBuilder.loadTexts:
    dodIPXFilterEntry.setStatus("mandatory")


class _DodIPXFilterIndex_Type(Integer32):
    """Custom type dodIPXFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_DodIPXFilterIndex_Type.__name__ = "Integer32"
_DodIPXFilterIndex_Object = MibTableColumn
dodIPXFilterIndex = _DodIPXFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 9, 1, 1),
    _DodIPXFilterIndex_Type()
)
dodIPXFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodIPXFilterIndex.setStatus("mandatory")
_DodIPXFilterDstNetAddr_Type = IpxNetAddress
_DodIPXFilterDstNetAddr_Object = MibTableColumn
dodIPXFilterDstNetAddr = _DodIPXFilterDstNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 9, 1, 2),
    _DodIPXFilterDstNetAddr_Type()
)
dodIPXFilterDstNetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIPXFilterDstNetAddr.setStatus("mandatory")
_DodIPXFilterDstNodeAddr_Type = MacAddress
_DodIPXFilterDstNodeAddr_Object = MibTableColumn
dodIPXFilterDstNodeAddr = _DodIPXFilterDstNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 9, 1, 3),
    _DodIPXFilterDstNodeAddr_Type()
)
dodIPXFilterDstNodeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIPXFilterDstNodeAddr.setStatus("mandatory")


class _DodIPXFilterDstSocket_Type(OctetString):
    """Custom type dodIPXFilterDstSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DodIPXFilterDstSocket_Type.__name__ = "OctetString"
_DodIPXFilterDstSocket_Object = MibTableColumn
dodIPXFilterDstSocket = _DodIPXFilterDstSocket_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 9, 1, 4),
    _DodIPXFilterDstSocket_Type()
)
dodIPXFilterDstSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIPXFilterDstSocket.setStatus("mandatory")
_DodIPXFilterSrcNetAddr_Type = IpxNetAddress
_DodIPXFilterSrcNetAddr_Object = MibTableColumn
dodIPXFilterSrcNetAddr = _DodIPXFilterSrcNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 9, 1, 5),
    _DodIPXFilterSrcNetAddr_Type()
)
dodIPXFilterSrcNetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIPXFilterSrcNetAddr.setStatus("mandatory")
_DodIPXFilterSrcNodeAddr_Type = MacAddress
_DodIPXFilterSrcNodeAddr_Object = MibTableColumn
dodIPXFilterSrcNodeAddr = _DodIPXFilterSrcNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 9, 1, 6),
    _DodIPXFilterSrcNodeAddr_Type()
)
dodIPXFilterSrcNodeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIPXFilterSrcNodeAddr.setStatus("mandatory")


class _DodIPXFilterSrcSocket_Type(OctetString):
    """Custom type dodIPXFilterSrcSocket based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DodIPXFilterSrcSocket_Type.__name__ = "OctetString"
_DodIPXFilterSrcSocket_Object = MibTableColumn
dodIPXFilterSrcSocket = _DodIPXFilterSrcSocket_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 9, 1, 7),
    _DodIPXFilterSrcSocket_Type()
)
dodIPXFilterSrcSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIPXFilterSrcSocket.setStatus("mandatory")


class _DodIPXFilterAllow_Type(Integer32):
    """Custom type dodIPXFilterAllow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_DodIPXFilterAllow_Type.__name__ = "Integer32"
_DodIPXFilterAllow_Object = MibTableColumn
dodIPXFilterAllow = _DodIPXFilterAllow_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 9, 1, 8),
    _DodIPXFilterAllow_Type()
)
dodIPXFilterAllow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIPXFilterAllow.setStatus("mandatory")


class _DodOperation_Type(Integer32):
    """Custom type dodOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("erase", 3),
          ("load", 2),
          ("save", 1))
    )


_DodOperation_Type.__name__ = "Integer32"
_DodOperation_Object = MibScalar
dodOperation = _DodOperation_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 10),
    _DodOperation_Type()
)
dodOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dodOperation.setStatus("mandatory")


class _DodRemoteMacDefault_Type(DisplayString):
    """Custom type dodRemoteMacDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DodRemoteMacDefault_Type.__name__ = "DisplayString"
_DodRemoteMacDefault_Object = MibScalar
dodRemoteMacDefault = _DodRemoteMacDefault_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 11),
    _DodRemoteMacDefault_Type()
)
dodRemoteMacDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodRemoteMacDefault.setStatus("mandatory")
_DodCallerTable_Object = MibTable
dodCallerTable = _DodCallerTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 12)
)
if mibBuilder.loadTexts:
    dodCallerTable.setStatus("mandatory")
_DodCallerEntry_Object = MibTableRow
dodCallerEntry = _DodCallerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 12, 1)
)
dodCallerEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dodDestinationName"),
    (0, "FLOWPOINT-MIB", "dodCallIDType"),
    (0, "FLOWPOINT-MIB", "dodCallerNumber"),
)
if mibBuilder.loadTexts:
    dodCallerEntry.setStatus("mandatory")


class _DodCallerNumber_Type(DisplayString):
    """Custom type dodCallerNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DodCallerNumber_Type.__name__ = "DisplayString"
_DodCallerNumber_Object = MibTableColumn
dodCallerNumber = _DodCallerNumber_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 12, 1, 1),
    _DodCallerNumber_Type()
)
dodCallerNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodCallerNumber.setStatus("mandatory")


class _DodCallerOperation_Type(Integer32):
    """Custom type dodCallerOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("remove", 2))
    )


_DodCallerOperation_Type.__name__ = "Integer32"
_DodCallerOperation_Object = MibTableColumn
dodCallerOperation = _DodCallerOperation_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 12, 1, 2),
    _DodCallerOperation_Type()
)
dodCallerOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dodCallerOperation.setStatus("mandatory")
_DodIPTranslationServerTable_Object = MibTable
dodIPTranslationServerTable = _DodIPTranslationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 13)
)
if mibBuilder.loadTexts:
    dodIPTranslationServerTable.setStatus("mandatory")
_DodIPTranslationServerEntry_Object = MibTableRow
dodIPTranslationServerEntry = _DodIPTranslationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 13, 1)
)
dodIPTranslationServerEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dodDestinationName"),
    (0, "FLOWPOINT-MIB", "dodIPTranslationServerIPAddress"),
    (0, "FLOWPOINT-MIB", "dodIPTranslationProtocol"),
    (0, "FLOWPOINT-MIB", "dodIPFirstTranslationPort"),
)
if mibBuilder.loadTexts:
    dodIPTranslationServerEntry.setStatus("mandatory")
_DodIPTranslationServerIPAddress_Type = IpAddress
_DodIPTranslationServerIPAddress_Object = MibTableColumn
dodIPTranslationServerIPAddress = _DodIPTranslationServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 13, 1, 1),
    _DodIPTranslationServerIPAddress_Type()
)
dodIPTranslationServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodIPTranslationServerIPAddress.setStatus("mandatory")


class _DodIPTranslationProtocol_Type(OctetString):
    """Custom type dodIPTranslationProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DodIPTranslationProtocol_Type.__name__ = "OctetString"
_DodIPTranslationProtocol_Object = MibTableColumn
dodIPTranslationProtocol = _DodIPTranslationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 13, 1, 2),
    _DodIPTranslationProtocol_Type()
)
dodIPTranslationProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodIPTranslationProtocol.setStatus("mandatory")


class _DodIPFirstTranslationPort_Type(OctetString):
    """Custom type dodIPFirstTranslationPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DodIPFirstTranslationPort_Type.__name__ = "OctetString"
_DodIPFirstTranslationPort_Object = MibTableColumn
dodIPFirstTranslationPort = _DodIPFirstTranslationPort_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 13, 1, 3),
    _DodIPFirstTranslationPort_Type()
)
dodIPFirstTranslationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodIPFirstTranslationPort.setStatus("mandatory")


class _DodIPLastTranslationPort_Type(OctetString):
    """Custom type dodIPLastTranslationPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DodIPLastTranslationPort_Type.__name__ = "OctetString"
_DodIPLastTranslationPort_Object = MibTableColumn
dodIPLastTranslationPort = _DodIPLastTranslationPort_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 13, 1, 4),
    _DodIPLastTranslationPort_Type()
)
dodIPLastTranslationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodIPLastTranslationPort.setStatus("mandatory")


class _DodIPFirstPrivatePort_Type(OctetString):
    """Custom type dodIPFirstPrivatePort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DodIPFirstPrivatePort_Type.__name__ = "OctetString"
_DodIPFirstPrivatePort_Object = MibTableColumn
dodIPFirstPrivatePort = _DodIPFirstPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 13, 1, 5),
    _DodIPFirstPrivatePort_Type()
)
dodIPFirstPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodIPFirstPrivatePort.setStatus("mandatory")
_DodIPTranslationStatus_Type = RowStatus
_DodIPTranslationStatus_Object = MibTableColumn
dodIPTranslationStatus = _DodIPTranslationStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 13, 1, 6),
    _DodIPTranslationStatus_Type()
)
dodIPTranslationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodIPTranslationStatus.setStatus("mandatory")
_DodNatHostMappingTable_Object = MibTable
dodNatHostMappingTable = _DodNatHostMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 14)
)
if mibBuilder.loadTexts:
    dodNatHostMappingTable.setStatus("mandatory")
_DodNatHostMappingEntry_Object = MibTableRow
dodNatHostMappingEntry = _DodNatHostMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 14, 1)
)
dodNatHostMappingEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dodDestinationName"),
    (0, "FLOWPOINT-MIB", "dodFirstPrivateIPAddress"),
    (0, "FLOWPOINT-MIB", "dodLastPrivateIPAddress"),
    (0, "FLOWPOINT-MIB", "dodFirstPublicIPAddress"),
)
if mibBuilder.loadTexts:
    dodNatHostMappingEntry.setStatus("mandatory")
_DodFirstPrivateIPAddress_Type = IpAddress
_DodFirstPrivateIPAddress_Object = MibTableColumn
dodFirstPrivateIPAddress = _DodFirstPrivateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 14, 1, 1),
    _DodFirstPrivateIPAddress_Type()
)
dodFirstPrivateIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodFirstPrivateIPAddress.setStatus("mandatory")
_DodLastPrivateIPAddress_Type = IpAddress
_DodLastPrivateIPAddress_Object = MibTableColumn
dodLastPrivateIPAddress = _DodLastPrivateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 14, 1, 2),
    _DodLastPrivateIPAddress_Type()
)
dodLastPrivateIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodLastPrivateIPAddress.setStatus("mandatory")
_DodFirstPublicIPAddress_Type = IpAddress
_DodFirstPublicIPAddress_Object = MibTableColumn
dodFirstPublicIPAddress = _DodFirstPublicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 14, 1, 3),
    _DodFirstPublicIPAddress_Type()
)
dodFirstPublicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dodFirstPublicIPAddress.setStatus("mandatory")
_DodNatHostMappingStatus_Type = RowStatus
_DodNatHostMappingStatus_Object = MibTableColumn
dodNatHostMappingStatus = _DodNatHostMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 1, 14, 1, 4),
    _DodNatHostMappingStatus_Type()
)
dodNatHostMappingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dodNatHostMappingStatus.setStatus("mandatory")
_Fpether_ObjectIdentity = ObjectIdentity
fpether = _Fpether_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1548, 2)
)
_FpEtherTable_Object = MibTable
fpEtherTable = _FpEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1)
)
if mibBuilder.loadTexts:
    fpEtherTable.setStatus("mandatory")
_FpEtherEntry_Object = MibTableRow
fpEtherEntry = _FpEtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1)
)
fpEtherEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "fpPortNum"),
)
if mibBuilder.loadTexts:
    fpEtherEntry.setStatus("mandatory")


class _FpPortNum_Type(Integer32):
    """Custom type fpPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FpPortNum_Type.__name__ = "Integer32"
_FpPortNum_Object = MibTableColumn
fpPortNum = _FpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 1),
    _FpPortNum_Type()
)
fpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPortNum.setStatus("mandatory")


class _FpBridgeState_Type(Integer32):
    """Custom type fpBridgeState based on Integer32"""
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


_FpBridgeState_Type.__name__ = "Integer32"
_FpBridgeState_Object = MibTableColumn
fpBridgeState = _FpBridgeState_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 2),
    _FpBridgeState_Type()
)
fpBridgeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpBridgeState.setStatus("mandatory")


class _FpIpState_Type(Integer32):
    """Custom type fpIpState based on Integer32"""
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


_FpIpState_Type.__name__ = "Integer32"
_FpIpState_Object = MibTableColumn
fpIpState = _FpIpState_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 3),
    _FpIpState_Type()
)
fpIpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIpState.setStatus("mandatory")


class _FpIpxState_Type(Integer32):
    """Custom type fpIpxState based on Integer32"""
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


_FpIpxState_Type.__name__ = "Integer32"
_FpIpxState_Object = MibTableColumn
fpIpxState = _FpIpxState_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 4),
    _FpIpxState_Type()
)
fpIpxState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIpxState.setStatus("mandatory")
_FpIpNetAddress_Type = IpAddress
_FpIpNetAddress_Object = MibTableColumn
fpIpNetAddress = _FpIpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 5),
    _FpIpNetAddress_Type()
)
fpIpNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIpNetAddress.setStatus("mandatory")
_FpIpNetMask_Type = IpAddress
_FpIpNetMask_Object = MibTableColumn
fpIpNetMask = _FpIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 6),
    _FpIpNetMask_Type()
)
fpIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIpNetMask.setStatus("mandatory")
_FpIpxNetAddress_Type = IpxNetAddress
_FpIpxNetAddress_Object = MibTableColumn
fpIpxNetAddress = _FpIpxNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 7),
    _FpIpxNetAddress_Type()
)
fpIpxNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIpxNetAddress.setStatus("mandatory")


class _FpIpxFrameType_Type(Integer32):
    """Custom type fpIpxFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("frame-8022", 1),
          ("frame-8023", 2),
          ("frame-dix", 3))
    )


_FpIpxFrameType_Type.__name__ = "Integer32"
_FpIpxFrameType_Object = MibTableColumn
fpIpxFrameType = _FpIpxFrameType_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 8),
    _FpIpxFrameType_Type()
)
fpIpxFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIpxFrameType.setStatus("mandatory")


class _FpEtherIpOptRecvRIP_Type(Integer32):
    """Custom type fpEtherIpOptRecvRIP based on Integer32"""
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


_FpEtherIpOptRecvRIP_Type.__name__ = "Integer32"
_FpEtherIpOptRecvRIP_Object = MibTableColumn
fpEtherIpOptRecvRIP = _FpEtherIpOptRecvRIP_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 9),
    _FpEtherIpOptRecvRIP_Type()
)
fpEtherIpOptRecvRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpEtherIpOptRecvRIP.setStatus("mandatory")


class _FpEtherIpOptSendRIP_Type(Integer32):
    """Custom type fpEtherIpOptSendRIP based on Integer32"""
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


_FpEtherIpOptSendRIP_Type.__name__ = "Integer32"
_FpEtherIpOptSendRIP_Object = MibTableColumn
fpEtherIpOptSendRIP = _FpEtherIpOptSendRIP_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 10),
    _FpEtherIpOptSendRIP_Type()
)
fpEtherIpOptSendRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpEtherIpOptSendRIP.setStatus("mandatory")


class _FpEtherIpOptRecvRIPDefault_Type(Integer32):
    """Custom type fpEtherIpOptRecvRIPDefault based on Integer32"""
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


_FpEtherIpOptRecvRIPDefault_Type.__name__ = "Integer32"
_FpEtherIpOptRecvRIPDefault_Object = MibTableColumn
fpEtherIpOptRecvRIPDefault = _FpEtherIpOptRecvRIPDefault_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 11),
    _FpEtherIpOptRecvRIPDefault_Type()
)
fpEtherIpOptRecvRIPDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpEtherIpOptRecvRIPDefault.setStatus("mandatory")


class _FpEtherIpOptSendRIPDefault_Type(Integer32):
    """Custom type fpEtherIpOptSendRIPDefault based on Integer32"""
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


_FpEtherIpOptSendRIPDefault_Type.__name__ = "Integer32"
_FpEtherIpOptSendRIPDefault_Object = MibTableColumn
fpEtherIpOptSendRIPDefault = _FpEtherIpOptSendRIPDefault_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 12),
    _FpEtherIpOptSendRIPDefault_Type()
)
fpEtherIpOptSendRIPDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpEtherIpOptSendRIPDefault.setStatus("mandatory")


class _FpIpxStrNetAddress_Type(DisplayString):
    """Custom type fpIpxStrNetAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_FpIpxStrNetAddress_Type.__name__ = "DisplayString"
_FpIpxStrNetAddress_Object = MibTableColumn
fpIpxStrNetAddress = _FpIpxStrNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 13),
    _FpIpxStrNetAddress_Type()
)
fpIpxStrNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIpxStrNetAddress.setStatus("mandatory")
_FpIpDefaultGateway_Type = IpAddress
_FpIpDefaultGateway_Object = MibTableColumn
fpIpDefaultGateway = _FpIpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 14),
    _FpIpDefaultGateway_Type()
)
fpIpDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIpDefaultGateway.setStatus("mandatory")


class _FpEtherIpOptRecvRIP1_Type(Integer32):
    """Custom type fpEtherIpOptRecvRIP1 based on Integer32"""
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


_FpEtherIpOptRecvRIP1_Type.__name__ = "Integer32"
_FpEtherIpOptRecvRIP1_Object = MibTableColumn
fpEtherIpOptRecvRIP1 = _FpEtherIpOptRecvRIP1_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 15),
    _FpEtherIpOptRecvRIP1_Type()
)
fpEtherIpOptRecvRIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpEtherIpOptRecvRIP1.setStatus("mandatory")


class _FpEtherIpOptSendRIP1_Type(Integer32):
    """Custom type fpEtherIpOptSendRIP1 based on Integer32"""
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


_FpEtherIpOptSendRIP1_Type.__name__ = "Integer32"
_FpEtherIpOptSendRIP1_Object = MibTableColumn
fpEtherIpOptSendRIP1 = _FpEtherIpOptSendRIP1_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 16),
    _FpEtherIpOptSendRIP1_Type()
)
fpEtherIpOptSendRIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpEtherIpOptSendRIP1.setStatus("mandatory")


class _FpEtherIpOptRecvRIP2_Type(Integer32):
    """Custom type fpEtherIpOptRecvRIP2 based on Integer32"""
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


_FpEtherIpOptRecvRIP2_Type.__name__ = "Integer32"
_FpEtherIpOptRecvRIP2_Object = MibTableColumn
fpEtherIpOptRecvRIP2 = _FpEtherIpOptRecvRIP2_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 17),
    _FpEtherIpOptRecvRIP2_Type()
)
fpEtherIpOptRecvRIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpEtherIpOptRecvRIP2.setStatus("mandatory")


class _FpEtherIpOptSendRIP2_Type(Integer32):
    """Custom type fpEtherIpOptSendRIP2 based on Integer32"""
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


_FpEtherIpOptSendRIP2_Type.__name__ = "Integer32"
_FpEtherIpOptSendRIP2_Object = MibTableColumn
fpEtherIpOptSendRIP2 = _FpEtherIpOptSendRIP2_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 18),
    _FpEtherIpOptSendRIP2_Type()
)
fpEtherIpOptSendRIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpEtherIpOptSendRIP2.setStatus("mandatory")
_FpIpRIPMulticastAddress_Type = IpAddress
_FpIpRIPMulticastAddress_Object = MibTableColumn
fpIpRIPMulticastAddress = _FpIpRIPMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 19),
    _FpIpRIPMulticastAddress_Type()
)
fpIpRIPMulticastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIpRIPMulticastAddress.setStatus("mandatory")


class _FpNATState_Type(Integer32):
    """Custom type fpNATState based on Integer32"""
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


_FpNATState_Type.__name__ = "Integer32"
_FpNATState_Object = MibTableColumn
fpNATState = _FpNATState_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 20),
    _FpNATState_Type()
)
fpNATState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpNATState.setStatus("mandatory")
_FpMtu_Type = Integer32
_FpMtu_Object = MibTableColumn
fpMtu = _FpMtu_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 1, 1, 21),
    _FpMtu_Type()
)
fpMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpMtu.setStatus("mandatory")


class _FpEtherOperation_Type(Integer32):
    """Custom type fpEtherOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("erase", 3),
          ("load", 2),
          ("save", 1))
    )


_FpEtherOperation_Type.__name__ = "Integer32"
_FpEtherOperation_Object = MibScalar
fpEtherOperation = _FpEtherOperation_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 2),
    _FpEtherOperation_Type()
)
fpEtherOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    fpEtherOperation.setStatus("mandatory")
_EtherNatHostMappingTable_Object = MibTable
etherNatHostMappingTable = _EtherNatHostMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 3)
)
if mibBuilder.loadTexts:
    etherNatHostMappingTable.setStatus("mandatory")
_EtherNatHostMappingEntry_Object = MibTableRow
etherNatHostMappingEntry = _EtherNatHostMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 3, 1)
)
etherNatHostMappingEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "fpPortNum"),
    (0, "FLOWPOINT-MIB", "etherFirstPrivateIPAddress"),
    (0, "FLOWPOINT-MIB", "etherLastPrivateIPAddress"),
    (0, "FLOWPOINT-MIB", "etherFirstPublicIPAddress"),
)
if mibBuilder.loadTexts:
    etherNatHostMappingEntry.setStatus("mandatory")
_EtherFirstPrivateIPAddress_Type = IpAddress
_EtherFirstPrivateIPAddress_Object = MibTableColumn
etherFirstPrivateIPAddress = _EtherFirstPrivateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 3, 1, 1),
    _EtherFirstPrivateIPAddress_Type()
)
etherFirstPrivateIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherFirstPrivateIPAddress.setStatus("mandatory")
_EtherLastPrivateIPAddress_Type = IpAddress
_EtherLastPrivateIPAddress_Object = MibTableColumn
etherLastPrivateIPAddress = _EtherLastPrivateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 3, 1, 2),
    _EtherLastPrivateIPAddress_Type()
)
etherLastPrivateIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherLastPrivateIPAddress.setStatus("mandatory")
_EtherFirstPublicIPAddress_Type = IpAddress
_EtherFirstPublicIPAddress_Object = MibTableColumn
etherFirstPublicIPAddress = _EtherFirstPublicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 3, 1, 3),
    _EtherFirstPublicIPAddress_Type()
)
etherFirstPublicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherFirstPublicIPAddress.setStatus("mandatory")
_EtherNatHostMappingStatus_Type = RowStatus
_EtherNatHostMappingStatus_Object = MibTableColumn
etherNatHostMappingStatus = _EtherNatHostMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 3, 1, 4),
    _EtherNatHostMappingStatus_Type()
)
etherNatHostMappingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherNatHostMappingStatus.setStatus("mandatory")
_EtherIPTranslationServerTable_Object = MibTable
etherIPTranslationServerTable = _EtherIPTranslationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 4)
)
if mibBuilder.loadTexts:
    etherIPTranslationServerTable.setStatus("mandatory")
_EtherIPTranslationServerEntry_Object = MibTableRow
etherIPTranslationServerEntry = _EtherIPTranslationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 4, 1)
)
etherIPTranslationServerEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "fpPortNum"),
    (0, "FLOWPOINT-MIB", "etherIPTranslationServerIPAddress"),
    (0, "FLOWPOINT-MIB", "etherIPTranslationProtocol"),
    (0, "FLOWPOINT-MIB", "etherIPFirstTranslationPort"),
)
if mibBuilder.loadTexts:
    etherIPTranslationServerEntry.setStatus("mandatory")
_EtherIPTranslationServerIPAddress_Type = IpAddress
_EtherIPTranslationServerIPAddress_Object = MibTableColumn
etherIPTranslationServerIPAddress = _EtherIPTranslationServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 4, 1, 1),
    _EtherIPTranslationServerIPAddress_Type()
)
etherIPTranslationServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIPTranslationServerIPAddress.setStatus("mandatory")


class _EtherIPTranslationProtocol_Type(OctetString):
    """Custom type etherIPTranslationProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_EtherIPTranslationProtocol_Type.__name__ = "OctetString"
_EtherIPTranslationProtocol_Object = MibTableColumn
etherIPTranslationProtocol = _EtherIPTranslationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 4, 1, 2),
    _EtherIPTranslationProtocol_Type()
)
etherIPTranslationProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIPTranslationProtocol.setStatus("mandatory")


class _EtherIPFirstTranslationPort_Type(OctetString):
    """Custom type etherIPFirstTranslationPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_EtherIPFirstTranslationPort_Type.__name__ = "OctetString"
_EtherIPFirstTranslationPort_Object = MibTableColumn
etherIPFirstTranslationPort = _EtherIPFirstTranslationPort_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 4, 1, 3),
    _EtherIPFirstTranslationPort_Type()
)
etherIPFirstTranslationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIPFirstTranslationPort.setStatus("mandatory")


class _EtherIPLastTranslationPort_Type(OctetString):
    """Custom type etherIPLastTranslationPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_EtherIPLastTranslationPort_Type.__name__ = "OctetString"
_EtherIPLastTranslationPort_Object = MibTableColumn
etherIPLastTranslationPort = _EtherIPLastTranslationPort_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 4, 1, 4),
    _EtherIPLastTranslationPort_Type()
)
etherIPLastTranslationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIPLastTranslationPort.setStatus("mandatory")


class _EtherIPFirstPrivatePort_Type(OctetString):
    """Custom type etherIPFirstPrivatePort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_EtherIPFirstPrivatePort_Type.__name__ = "OctetString"
_EtherIPFirstPrivatePort_Object = MibTableColumn
etherIPFirstPrivatePort = _EtherIPFirstPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 4, 1, 5),
    _EtherIPFirstPrivatePort_Type()
)
etherIPFirstPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIPFirstPrivatePort.setStatus("mandatory")
_EtherIPTranslationStatus_Type = RowStatus
_EtherIPTranslationStatus_Object = MibTableColumn
etherIPTranslationStatus = _EtherIPTranslationStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 2, 4, 1, 6),
    _EtherIPTranslationStatus_Type()
)
etherIPTranslationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherIPTranslationStatus.setStatus("mandatory")
_Fpisdn_ObjectIdentity = ObjectIdentity
fpisdn = _Fpisdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1548, 3)
)


class _FpIsdnCh1Spid_Type(DisplayString):
    """Custom type fpIsdnCh1Spid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_FpIsdnCh1Spid_Type.__name__ = "DisplayString"
_FpIsdnCh1Spid_Object = MibScalar
fpIsdnCh1Spid = _FpIsdnCh1Spid_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 1),
    _FpIsdnCh1Spid_Type()
)
fpIsdnCh1Spid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIsdnCh1Spid.setStatus("mandatory")


class _FpIsdnCh2Spid_Type(DisplayString):
    """Custom type fpIsdnCh2Spid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_FpIsdnCh2Spid_Type.__name__ = "DisplayString"
_FpIsdnCh2Spid_Object = MibScalar
fpIsdnCh2Spid = _FpIsdnCh2Spid_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 2),
    _FpIsdnCh2Spid_Type()
)
fpIsdnCh2Spid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIsdnCh2Spid.setStatus("mandatory")


class _FpIsdnCh1DirectoryNum_Type(DisplayString):
    """Custom type fpIsdnCh1DirectoryNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_FpIsdnCh1DirectoryNum_Type.__name__ = "DisplayString"
_FpIsdnCh1DirectoryNum_Object = MibScalar
fpIsdnCh1DirectoryNum = _FpIsdnCh1DirectoryNum_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 3),
    _FpIsdnCh1DirectoryNum_Type()
)
fpIsdnCh1DirectoryNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIsdnCh1DirectoryNum.setStatus("mandatory")


class _FpIsdnCh2DirectoryNum_Type(DisplayString):
    """Custom type fpIsdnCh2DirectoryNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_FpIsdnCh2DirectoryNum_Type.__name__ = "DisplayString"
_FpIsdnCh2DirectoryNum_Object = MibScalar
fpIsdnCh2DirectoryNum = _FpIsdnCh2DirectoryNum_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 4),
    _FpIsdnCh2DirectoryNum_Type()
)
fpIsdnCh2DirectoryNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIsdnCh2DirectoryNum.setStatus("mandatory")


class _FpIsdnSwitchType_Type(Integer32):
    """Custom type fpIsdnSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              7,
              8,
              9,
              10,
              12,
              14)
        )
    )
    namedValues = NamedValues(
        *(("att5ess", 2),
          ("auto", 14),
          ("dms100", 5),
          ("kdd", 7),
          ("net3", 8),
          ("net3swiss", 9),
          ("ni1", 10),
          ("ntt", 12))
    )


_FpIsdnSwitchType_Type.__name__ = "Integer32"
_FpIsdnSwitchType_Object = MibScalar
fpIsdnSwitchType = _FpIsdnSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 5),
    _FpIsdnSwitchType_Type()
)
fpIsdnSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIsdnSwitchType.setStatus("mandatory")


class _FpIsdnOperation_Type(Integer32):
    """Custom type fpIsdnOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("erase", 3),
          ("load", 2),
          ("save", 1))
    )


_FpIsdnOperation_Type.__name__ = "Integer32"
_FpIsdnOperation_Object = MibScalar
fpIsdnOperation = _FpIsdnOperation_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 6),
    _FpIsdnOperation_Type()
)
fpIsdnOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    fpIsdnOperation.setStatus("mandatory")


class _FpIsdnCh1Status_Type(Integer32):
    """Custom type fpIsdnCh1Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("alerting", 5),
          ("closing", 4),
          ("connected", 3),
          ("dialing", 6),
          ("idle", 1),
          ("in-use-by-pots", 8),
          ("opening", 2),
          ("out-of-service", 7))
    )


_FpIsdnCh1Status_Type.__name__ = "Integer32"
_FpIsdnCh1Status_Object = MibScalar
fpIsdnCh1Status = _FpIsdnCh1Status_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 7),
    _FpIsdnCh1Status_Type()
)
fpIsdnCh1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIsdnCh1Status.setStatus("mandatory")


class _FpIsdnCh2Status_Type(Integer32):
    """Custom type fpIsdnCh2Status based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("alerting", 5),
          ("closing", 4),
          ("connected", 3),
          ("dialing", 6),
          ("idle", 1),
          ("in-use-by-pots", 8),
          ("opening", 2),
          ("out-of-service", 7))
    )


_FpIsdnCh2Status_Type.__name__ = "Integer32"
_FpIsdnCh2Status_Object = MibScalar
fpIsdnCh2Status = _FpIsdnCh2Status_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 8),
    _FpIsdnCh2Status_Type()
)
fpIsdnCh2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIsdnCh2Status.setStatus("mandatory")
_FpIsdnCh1ClearCode_Type = Integer32
_FpIsdnCh1ClearCode_Object = MibScalar
fpIsdnCh1ClearCode = _FpIsdnCh1ClearCode_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 9),
    _FpIsdnCh1ClearCode_Type()
)
fpIsdnCh1ClearCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIsdnCh1ClearCode.setStatus("mandatory")
_FpIsdnCh2ClearCode_Type = Integer32
_FpIsdnCh2ClearCode_Object = MibScalar
fpIsdnCh2ClearCode = _FpIsdnCh2ClearCode_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 10),
    _FpIsdnCh2ClearCode_Type()
)
fpIsdnCh2ClearCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIsdnCh2ClearCode.setStatus("mandatory")
_FpIsdnCh1ClearReason_Type = DisplayString
_FpIsdnCh1ClearReason_Object = MibScalar
fpIsdnCh1ClearReason = _FpIsdnCh1ClearReason_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 11),
    _FpIsdnCh1ClearReason_Type()
)
fpIsdnCh1ClearReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIsdnCh1ClearReason.setStatus("mandatory")
_FpIsdnCh2ClearReason_Type = DisplayString
_FpIsdnCh2ClearReason_Object = MibScalar
fpIsdnCh2ClearReason = _FpIsdnCh2ClearReason_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 12),
    _FpIsdnCh2ClearReason_Type()
)
fpIsdnCh2ClearReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIsdnCh2ClearReason.setStatus("mandatory")


class _FpIsdnSpeed_Type(Integer32):
    """Custom type fpIsdnSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("speed-56k", 2))
    )


_FpIsdnSpeed_Type.__name__ = "Integer32"
_FpIsdnSpeed_Object = MibScalar
fpIsdnSpeed = _FpIsdnSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 13),
    _FpIsdnSpeed_Type()
)
fpIsdnSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIsdnSpeed.setStatus("mandatory")


class _FpIsdnDataCallsIn_Type(Integer32):
    """Custom type fpIsdnDataCallsIn based on Integer32"""
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


_FpIsdnDataCallsIn_Type.__name__ = "Integer32"
_FpIsdnDataCallsIn_Object = MibScalar
fpIsdnDataCallsIn = _FpIsdnDataCallsIn_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 14),
    _FpIsdnDataCallsIn_Type()
)
fpIsdnDataCallsIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIsdnDataCallsIn.setStatus("mandatory")


class _FpIsdnDataCallsOut_Type(Integer32):
    """Custom type fpIsdnDataCallsOut based on Integer32"""
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


_FpIsdnDataCallsOut_Type.__name__ = "Integer32"
_FpIsdnDataCallsOut_Object = MibScalar
fpIsdnDataCallsOut = _FpIsdnDataCallsOut_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 15),
    _FpIsdnDataCallsOut_Type()
)
fpIsdnDataCallsOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIsdnDataCallsOut.setStatus("mandatory")


class _FpIsdnLineStatus_Type(Integer32):
    """Custom type fpIsdnLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("deactivated", 2))
    )


_FpIsdnLineStatus_Type.__name__ = "Integer32"
_FpIsdnLineStatus_Object = MibScalar
fpIsdnLineStatus = _FpIsdnLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 16),
    _FpIsdnLineStatus_Type()
)
fpIsdnLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIsdnLineStatus.setStatus("mandatory")


class _FpIsdnStatus_Type(Integer32):
    """Custom type fpIsdnStatus based on Integer32"""
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
        *(("autoSpidActive", 5),
          ("inService", 1),
          ("notOperational", 2),
          ("qualifyingSpids", 7),
          ("startAutoSpid", 3),
          ("stopAutoSpid", 4),
          ("validatingSpids", 6))
    )


_FpIsdnStatus_Type.__name__ = "Integer32"
_FpIsdnStatus_Object = MibScalar
fpIsdnStatus = _FpIsdnStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 17),
    _FpIsdnStatus_Type()
)
fpIsdnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpIsdnStatus.setStatus("mandatory")
_FpIsdnAutoSpidCounter_Type = Integer32
_FpIsdnAutoSpidCounter_Object = MibScalar
fpIsdnAutoSpidCounter = _FpIsdnAutoSpidCounter_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 18),
    _FpIsdnAutoSpidCounter_Type()
)
fpIsdnAutoSpidCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIsdnAutoSpidCounter.setStatus("mandatory")
_FpIsdnSwitchTable_Object = MibTable
fpIsdnSwitchTable = _FpIsdnSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 19)
)
if mibBuilder.loadTexts:
    fpIsdnSwitchTable.setStatus("mandatory")
_FpIsdnSwitchEntry_Object = MibTableRow
fpIsdnSwitchEntry = _FpIsdnSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 19, 1)
)
fpIsdnSwitchEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "fpIsdnSwitchTypeIndex"),
)
if mibBuilder.loadTexts:
    fpIsdnSwitchEntry.setStatus("mandatory")


class _FpIsdnSwitchTypeIndex_Type(Integer32):
    """Custom type fpIsdnSwitchTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FpIsdnSwitchTypeIndex_Type.__name__ = "Integer32"
_FpIsdnSwitchTypeIndex_Object = MibTableColumn
fpIsdnSwitchTypeIndex = _FpIsdnSwitchTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1548, 3, 19, 1, 1),
    _FpIsdnSwitchTypeIndex_Type()
)
fpIsdnSwitchTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIsdnSwitchTypeIndex.setStatus("mandatory")
_Fpsys_ObjectIdentity = ObjectIdentity
fpsys = _Fpsys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1548, 4)
)


class _FpSysName_Type(DisplayString):
    """Custom type fpSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FpSysName_Type.__name__ = "DisplayString"
_FpSysName_Object = MibScalar
fpSysName = _FpSysName_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 1),
    _FpSysName_Type()
)
fpSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpSysName.setStatus("mandatory")


class _FpSysMessage_Type(DisplayString):
    """Custom type fpSysMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FpSysMessage_Type.__name__ = "DisplayString"
_FpSysMessage_Object = MibScalar
fpSysMessage = _FpSysMessage_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 2),
    _FpSysMessage_Type()
)
fpSysMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpSysMessage.setStatus("mandatory")


class _FpSysPassword_Type(DisplayString):
    """Custom type fpSysPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FpSysPassword_Type.__name__ = "DisplayString"
_FpSysPassword_Object = MibScalar
fpSysPassword = _FpSysPassword_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 3),
    _FpSysPassword_Type()
)
fpSysPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpSysPassword.setStatus("mandatory")
_FpSysAuthen_Type = AuthenProtoType
_FpSysAuthen_Object = MibScalar
fpSysAuthen = _FpSysAuthen_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 4),
    _FpSysAuthen_Type()
)
fpSysAuthen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpSysAuthen.setStatus("mandatory")


class _FpSysOperation_Type(Integer32):
    """Custom type fpSysOperation based on Integer32"""
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
        *(("erase", 3),
          ("load", 2),
          ("reboot", 4),
          ("reboot-like-factory", 6),
          ("reboot-like-new", 7),
          ("save", 1),
          ("set-clock", 5))
    )


_FpSysOperation_Type.__name__ = "Integer32"
_FpSysOperation_Object = MibScalar
fpSysOperation = _FpSysOperation_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 5),
    _FpSysOperation_Type()
)
fpSysOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    fpSysOperation.setStatus("mandatory")


class _FpSysSoftwareVer_Type(DisplayString):
    """Custom type fpSysSoftwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FpSysSoftwareVer_Type.__name__ = "DisplayString"
_FpSysSoftwareVer_Object = MibScalar
fpSysSoftwareVer = _FpSysSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 6),
    _FpSysSoftwareVer_Type()
)
fpSysSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpSysSoftwareVer.setStatus("mandatory")


class _FpSysHardwareVer_Type(DisplayString):
    """Custom type fpSysHardwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FpSysHardwareVer_Type.__name__ = "DisplayString"
_FpSysHardwareVer_Object = MibScalar
fpSysHardwareVer = _FpSysHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 7),
    _FpSysHardwareVer_Type()
)
fpSysHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpSysHardwareVer.setStatus("mandatory")


class _FpLoginPassword_Type(DisplayString):
    """Custom type fpLoginPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FpLoginPassword_Type.__name__ = "DisplayString"
_FpLoginPassword_Object = MibScalar
fpLoginPassword = _FpLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 8),
    _FpLoginPassword_Type()
)
fpLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpLoginPassword.setStatus("mandatory")


class _FpWriteTimeout_Type(Integer32):
    """Custom type fpWriteTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_FpWriteTimeout_Type.__name__ = "Integer32"
_FpWriteTimeout_Object = MibScalar
fpWriteTimeout = _FpWriteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 9),
    _FpWriteTimeout_Type()
)
fpWriteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpWriteTimeout.setStatus("mandatory")


class _FpWriteTimer_Type(Integer32):
    """Custom type fpWriteTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_FpWriteTimer_Type.__name__ = "Integer32"
_FpWriteTimer_Object = MibScalar
fpWriteTimer = _FpWriteTimer_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 10),
    _FpWriteTimer_Type()
)
fpWriteTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpWriteTimer.setStatus("mandatory")


class _FpCommunityName_Type(DisplayString):
    """Custom type fpCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FpCommunityName_Type.__name__ = "DisplayString"
_FpCommunityName_Object = MibScalar
fpCommunityName = _FpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 11),
    _FpCommunityName_Type()
)
fpCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpCommunityName.setStatus("mandatory")


class _FpInternetFireWall_Type(Integer32):
    """Custom type fpInternetFireWall based on Integer32"""
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


_FpInternetFireWall_Type.__name__ = "Integer32"
_FpInternetFireWall_Object = MibScalar
fpInternetFireWall = _FpInternetFireWall_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 12),
    _FpInternetFireWall_Type()
)
fpInternetFireWall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpInternetFireWall.setStatus("mandatory")
_FpSysLogout_Type = Integer32
_FpSysLogout_Object = MibScalar
fpSysLogout = _FpSysLogout_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 13),
    _FpSysLogout_Type()
)
fpSysLogout.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    fpSysLogout.setStatus("mandatory")


class _FpIpxSupported_Type(Integer32):
    """Custom type fpIpxSupported based on Integer32"""
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


_FpIpxSupported_Type.__name__ = "Integer32"
_FpIpxSupported_Object = MibScalar
fpIpxSupported = _FpIpxSupported_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 14),
    _FpIpxSupported_Type()
)
fpIpxSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpIpxSupported.setStatus("mandatory")
_FpSysCallerIdTable_Object = MibTable
fpSysCallerIdTable = _FpSysCallerIdTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 15)
)
if mibBuilder.loadTexts:
    fpSysCallerIdTable.setStatus("mandatory")
_FpSysCallerIdEntry_Object = MibTableRow
fpSysCallerIdEntry = _FpSysCallerIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 15, 1)
)
fpSysCallerIdEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dodCallIDType"),
)
if mibBuilder.loadTexts:
    fpSysCallerIdEntry.setStatus("mandatory")


class _FpCallerIdEnabled_Type(Integer32):
    """Custom type fpCallerIdEnabled based on Integer32"""
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


_FpCallerIdEnabled_Type.__name__ = "Integer32"
_FpCallerIdEnabled_Object = MibTableColumn
fpCallerIdEnabled = _FpCallerIdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 15, 1, 1),
    _FpCallerIdEnabled_Type()
)
fpCallerIdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpCallerIdEnabled.setStatus("mandatory")


class _FpMIBCompatibility_Type(Integer32):
    """Custom type fpMIBCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("new", 2),
          ("old", 1))
    )


_FpMIBCompatibility_Type.__name__ = "Integer32"
_FpMIBCompatibility_Object = MibScalar
fpMIBCompatibility = _FpMIBCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 16),
    _FpMIBCompatibility_Type()
)
fpMIBCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpMIBCompatibility.setStatus("mandatory")


class _FpPOTSInstalled_Type(Integer32):
    """Custom type fpPOTSInstalled based on Integer32"""
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


_FpPOTSInstalled_Type.__name__ = "Integer32"
_FpPOTSInstalled_Object = MibScalar
fpPOTSInstalled = _FpPOTSInstalled_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 17),
    _FpPOTSInstalled_Type()
)
fpPOTSInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpPOTSInstalled.setStatus("mandatory")


class _FpSysLastLogEvent_Type(DisplayString):
    """Custom type fpSysLastLogEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FpSysLastLogEvent_Type.__name__ = "DisplayString"
_FpSysLastLogEvent_Object = MibScalar
fpSysLastLogEvent = _FpSysLastLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 18),
    _FpSysLastLogEvent_Type()
)
fpSysLastLogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpSysLastLogEvent.setStatus("mandatory")
_FpSysSingleUser_Type = IpAddress
_FpSysSingleUser_Object = MibScalar
fpSysSingleUser = _FpSysSingleUser_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 19),
    _FpSysSingleUser_Type()
)
fpSysSingleUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpSysSingleUser.setStatus("mandatory")
_FpSysYear_Type = Integer32
_FpSysYear_Object = MibScalar
fpSysYear = _FpSysYear_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 20),
    _FpSysYear_Type()
)
fpSysYear.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    fpSysYear.setStatus("mandatory")


class _FpSysMonth_Type(Integer32):
    """Custom type fpSysMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_FpSysMonth_Type.__name__ = "Integer32"
_FpSysMonth_Object = MibScalar
fpSysMonth = _FpSysMonth_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 21),
    _FpSysMonth_Type()
)
fpSysMonth.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    fpSysMonth.setStatus("mandatory")


class _FpSysDay_Type(Integer32):
    """Custom type fpSysDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_FpSysDay_Type.__name__ = "Integer32"
_FpSysDay_Object = MibScalar
fpSysDay = _FpSysDay_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 22),
    _FpSysDay_Type()
)
fpSysDay.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    fpSysDay.setStatus("mandatory")


class _FpSysHour_Type(Integer32):
    """Custom type fpSysHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_FpSysHour_Type.__name__ = "Integer32"
_FpSysHour_Object = MibScalar
fpSysHour = _FpSysHour_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 23),
    _FpSysHour_Type()
)
fpSysHour.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    fpSysHour.setStatus("mandatory")


class _FpSysMinute_Type(Integer32):
    """Custom type fpSysMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_FpSysMinute_Type.__name__ = "Integer32"
_FpSysMinute_Object = MibScalar
fpSysMinute = _FpSysMinute_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 24),
    _FpSysMinute_Type()
)
fpSysMinute.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    fpSysMinute.setStatus("mandatory")


class _FpSysSecond_Type(Integer32):
    """Custom type fpSysSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_FpSysSecond_Type.__name__ = "Integer32"
_FpSysSecond_Object = MibScalar
fpSysSecond = _FpSysSecond_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 25),
    _FpSysSecond_Type()
)
fpSysSecond.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    fpSysSecond.setStatus("mandatory")
_FpSysDefaultSingleUser_Type = IpAddress
_FpSysDefaultSingleUser_Object = MibScalar
fpSysDefaultSingleUser = _FpSysDefaultSingleUser_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 26),
    _FpSysDefaultSingleUser_Type()
)
fpSysDefaultSingleUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpSysDefaultSingleUser.setStatus("mandatory")
_FpSysBootpRelay_Type = IpAddress
_FpSysBootpRelay_Object = MibScalar
fpSysBootpRelay = _FpSysBootpRelay_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 27),
    _FpSysBootpRelay_Type()
)
fpSysBootpRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpSysBootpRelay.setStatus("mandatory")
_FpSysKernelRevision_Type = Integer32
_FpSysKernelRevision_Object = MibScalar
fpSysKernelRevision = _FpSysKernelRevision_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 28),
    _FpSysKernelRevision_Type()
)
fpSysKernelRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpSysKernelRevision.setStatus("mandatory")


class _FpSysTelnetPort_Type(Integer32):
    """Custom type fpSysTelnetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FpSysTelnetPort_Type.__name__ = "Integer32"
_FpSysTelnetPort_Object = MibScalar
fpSysTelnetPort = _FpSysTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 29),
    _FpSysTelnetPort_Type()
)
fpSysTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpSysTelnetPort.setStatus("mandatory")


class _FpSysSNMPPort_Type(Integer32):
    """Custom type fpSysSNMPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FpSysSNMPPort_Type.__name__ = "Integer32"
_FpSysSNMPPort_Object = MibScalar
fpSysSNMPPort = _FpSysSNMPPort_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 30),
    _FpSysSNMPPort_Type()
)
fpSysSNMPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpSysSNMPPort.setStatus("mandatory")


class _FpWAN2WANForwarding_Type(Integer32):
    """Custom type fpWAN2WANForwarding based on Integer32"""
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


_FpWAN2WANForwarding_Type.__name__ = "Integer32"
_FpWAN2WANForwarding_Object = MibScalar
fpWAN2WANForwarding = _FpWAN2WANForwarding_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 31),
    _FpWAN2WANForwarding_Type()
)
fpWAN2WANForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpWAN2WANForwarding.setStatus("mandatory")
_FpUdpRelayTable_Object = MibTable
fpUdpRelayTable = _FpUdpRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 32)
)
if mibBuilder.loadTexts:
    fpUdpRelayTable.setStatus("mandatory")
_FpUdpRelayEntry_Object = MibTableRow
fpUdpRelayEntry = _FpUdpRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 32, 1)
)
fpUdpRelayEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "fpUdpRelayFirstPort"),
    (0, "FLOWPOINT-MIB", "fpUdpRelayLastPort"),
    (0, "FLOWPOINT-MIB", "fpUdpRelayIPAddress"),
)
if mibBuilder.loadTexts:
    fpUdpRelayEntry.setStatus("mandatory")


class _FpUdpRelayFirstPort_Type(OctetString):
    """Custom type fpUdpRelayFirstPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_FpUdpRelayFirstPort_Type.__name__ = "OctetString"
_FpUdpRelayFirstPort_Object = MibTableColumn
fpUdpRelayFirstPort = _FpUdpRelayFirstPort_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 32, 1, 1),
    _FpUdpRelayFirstPort_Type()
)
fpUdpRelayFirstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpUdpRelayFirstPort.setStatus("mandatory")


class _FpUdpRelayLastPort_Type(OctetString):
    """Custom type fpUdpRelayLastPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_FpUdpRelayLastPort_Type.__name__ = "OctetString"
_FpUdpRelayLastPort_Object = MibTableColumn
fpUdpRelayLastPort = _FpUdpRelayLastPort_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 32, 1, 2),
    _FpUdpRelayLastPort_Type()
)
fpUdpRelayLastPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpUdpRelayLastPort.setStatus("mandatory")
_FpUdpRelayIPAddress_Type = IpAddress
_FpUdpRelayIPAddress_Object = MibTableColumn
fpUdpRelayIPAddress = _FpUdpRelayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 32, 1, 3),
    _FpUdpRelayIPAddress_Type()
)
fpUdpRelayIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpUdpRelayIPAddress.setStatus("mandatory")
_FpUdpRelayStatus_Type = RowStatus
_FpUdpRelayStatus_Object = MibTableColumn
fpUdpRelayStatus = _FpUdpRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 32, 1, 4),
    _FpUdpRelayStatus_Type()
)
fpUdpRelayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpUdpRelayStatus.setStatus("mandatory")


class _FpOneWANConnection_Type(Integer32):
    """Custom type fpOneWANConnection based on Integer32"""
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


_FpOneWANConnection_Type.__name__ = "Integer32"
_FpOneWANConnection_Object = MibScalar
fpOneWANConnection = _FpOneWANConnection_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 33),
    _FpOneWANConnection_Type()
)
fpOneWANConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpOneWANConnection.setStatus("mandatory")


class _FpSysHTTPPort_Type(Integer32):
    """Custom type fpSysHTTPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FpSysHTTPPort_Type.__name__ = "Integer32"
_FpSysHTTPPort_Object = MibScalar
fpSysHTTPPort = _FpSysHTTPPort_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 34),
    _FpSysHTTPPort_Type()
)
fpSysHTTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpSysHTTPPort.setStatus("mandatory")


class _FpDirectedBroadcasts_Type(Integer32):
    """Custom type fpDirectedBroadcasts based on Integer32"""
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


_FpDirectedBroadcasts_Type.__name__ = "Integer32"
_FpDirectedBroadcasts_Object = MibScalar
fpDirectedBroadcasts = _FpDirectedBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 35),
    _FpDirectedBroadcasts_Type()
)
fpDirectedBroadcasts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpDirectedBroadcasts.setStatus("mandatory")


class _FpBlockNetBIOSDefault_Type(Integer32):
    """Custom type fpBlockNetBIOSDefault based on Integer32"""
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


_FpBlockNetBIOSDefault_Type.__name__ = "Integer32"
_FpBlockNetBIOSDefault_Object = MibScalar
fpBlockNetBIOSDefault = _FpBlockNetBIOSDefault_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 36),
    _FpBlockNetBIOSDefault_Type()
)
fpBlockNetBIOSDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpBlockNetBIOSDefault.setStatus("mandatory")
_FpSysFlashAvailable_Type = Integer32
_FpSysFlashAvailable_Object = MibScalar
fpSysFlashAvailable = _FpSysFlashAvailable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 37),
    _FpSysFlashAvailable_Type()
)
fpSysFlashAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpSysFlashAvailable.setStatus("mandatory")
_FpVoiceTable_Object = MibTable
fpVoiceTable = _FpVoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 38)
)
if mibBuilder.loadTexts:
    fpVoiceTable.setStatus("mandatory")
_FpVoiceEntry_Object = MibTableRow
fpVoiceEntry = _FpVoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 38, 1)
)
fpVoiceEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "fpVoiceIndex"),
)
if mibBuilder.loadTexts:
    fpVoiceEntry.setStatus("mandatory")


class _FpVoiceIndex_Type(Integer32):
    """Custom type fpVoiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FpVoiceIndex_Type.__name__ = "Integer32"
_FpVoiceIndex_Object = MibTableColumn
fpVoiceIndex = _FpVoiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 38, 1, 1),
    _FpVoiceIndex_Type()
)
fpVoiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpVoiceIndex.setStatus("mandatory")
_FpVoicePort_Type = DisplayString
_FpVoicePort_Object = MibTableColumn
fpVoicePort = _FpVoicePort_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 38, 1, 2),
    _FpVoicePort_Type()
)
fpVoicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpVoicePort.setStatus("mandatory")
_FpEchoTable_Object = MibTable
fpEchoTable = _FpEchoTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 39)
)
if mibBuilder.loadTexts:
    fpEchoTable.setStatus("deprecated")
_FpEchoEntry_Object = MibTableRow
fpEchoEntry = _FpEchoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 39, 1)
)
fpEchoEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "fpEchoIndex"),
)
if mibBuilder.loadTexts:
    fpEchoEntry.setStatus("deprecated")


class _FpEchoIndex_Type(Integer32):
    """Custom type fpEchoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FpEchoIndex_Type.__name__ = "Integer32"
_FpEchoIndex_Object = MibTableColumn
fpEchoIndex = _FpEchoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 39, 1, 1),
    _FpEchoIndex_Type()
)
fpEchoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpEchoIndex.setStatus("deprecated")
_FpEchoPort_Type = DisplayString
_FpEchoPort_Object = MibTableColumn
fpEchoPort = _FpEchoPort_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 39, 1, 2),
    _FpEchoPort_Type()
)
fpEchoPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpEchoPort.setStatus("deprecated")
_FpOptionTable_Object = MibTable
fpOptionTable = _FpOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 40)
)
if mibBuilder.loadTexts:
    fpOptionTable.setStatus("mandatory")
_FpOptionEntry_Object = MibTableRow
fpOptionEntry = _FpOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 40, 1)
)
fpOptionEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "fpOptionIndex"),
)
if mibBuilder.loadTexts:
    fpOptionEntry.setStatus("mandatory")
_FpOptionIndex_Type = Integer32
_FpOptionIndex_Object = MibTableColumn
fpOptionIndex = _FpOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 40, 1, 1),
    _FpOptionIndex_Type()
)
fpOptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpOptionIndex.setStatus("mandatory")
_FpOptionString_Type = DisplayString
_FpOptionString_Object = MibTableColumn
fpOptionString = _FpOptionString_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 40, 1, 2),
    _FpOptionString_Type()
)
fpOptionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpOptionString.setStatus("mandatory")


class _FpOptionAvailable_Type(Integer32):
    """Custom type fpOptionAvailable based on Integer32"""
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


_FpOptionAvailable_Type.__name__ = "Integer32"
_FpOptionAvailable_Object = MibTableColumn
fpOptionAvailable = _FpOptionAvailable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 4, 40, 1, 3),
    _FpOptionAvailable_Type()
)
fpOptionAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpOptionAvailable.setStatus("mandatory")
_Fplogin_ObjectIdentity = ObjectIdentity
fplogin = _Fplogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1548, 5)
)
_FpLoginTable_Object = MibTable
fpLoginTable = _FpLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 5, 1)
)
if mibBuilder.loadTexts:
    fpLoginTable.setStatus("mandatory")
_FpLoginEntry_Object = MibTableRow
fpLoginEntry = _FpLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 5, 1, 1)
)
fpLoginEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "fpLoginPassword"),
)
if mibBuilder.loadTexts:
    fpLoginEntry.setStatus("mandatory")


class _FpLoginAction_Type(Integer32):
    """Custom type fpLoginAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_FpLoginAction_Type.__name__ = "Integer32"
_FpLoginAction_Object = MibTableColumn
fpLoginAction = _FpLoginAction_Object(
    (1, 3, 6, 1, 4, 1, 1548, 5, 1, 1, 1),
    _FpLoginAction_Type()
)
fpLoginAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpLoginAction.setStatus("mandatory")
_FpWan_ObjectIdentity = ObjectIdentity
fpWan = _FpWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1548, 6)
)
_FpWanTable_Object = MibTable
fpWanTable = _FpWanTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 6, 1)
)
if mibBuilder.loadTexts:
    fpWanTable.setStatus("mandatory")
_FpWanEntry_Object = MibTableRow
fpWanEntry = _FpWanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 6, 1, 1)
)
fpWanEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "fpWanIndex"),
)
if mibBuilder.loadTexts:
    fpWanEntry.setStatus("mandatory")


class _FpWanIndex_Type(Integer32):
    """Custom type fpWanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FpWanIndex_Type.__name__ = "Integer32"
_FpWanIndex_Object = MibTableColumn
fpWanIndex = _FpWanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1548, 6, 1, 1, 1),
    _FpWanIndex_Type()
)
fpWanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpWanIndex.setStatus("mandatory")


class _FpWanInstantOutUtil_Type(Integer32):
    """Custom type fpWanInstantOutUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FpWanInstantOutUtil_Type.__name__ = "Integer32"
_FpWanInstantOutUtil_Object = MibTableColumn
fpWanInstantOutUtil = _FpWanInstantOutUtil_Object(
    (1, 3, 6, 1, 4, 1, 1548, 6, 1, 1, 2),
    _FpWanInstantOutUtil_Type()
)
fpWanInstantOutUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpWanInstantOutUtil.setStatus("mandatory")


class _FpWanInstantInUtil_Type(Integer32):
    """Custom type fpWanInstantInUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FpWanInstantInUtil_Type.__name__ = "Integer32"
_FpWanInstantInUtil_Object = MibTableColumn
fpWanInstantInUtil = _FpWanInstantInUtil_Object(
    (1, 3, 6, 1, 4, 1, 1548, 6, 1, 1, 3),
    _FpWanInstantInUtil_Type()
)
fpWanInstantInUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpWanInstantInUtil.setStatus("mandatory")


class _FpWanAvgOutUtil_Type(Integer32):
    """Custom type fpWanAvgOutUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FpWanAvgOutUtil_Type.__name__ = "Integer32"
_FpWanAvgOutUtil_Object = MibTableColumn
fpWanAvgOutUtil = _FpWanAvgOutUtil_Object(
    (1, 3, 6, 1, 4, 1, 1548, 6, 1, 1, 4),
    _FpWanAvgOutUtil_Type()
)
fpWanAvgOutUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpWanAvgOutUtil.setStatus("mandatory")


class _FpWanAvgInUtil_Type(Integer32):
    """Custom type fpWanAvgInUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FpWanAvgInUtil_Type.__name__ = "Integer32"
_FpWanAvgInUtil_Object = MibTableColumn
fpWanAvgInUtil = _FpWanAvgInUtil_Object(
    (1, 3, 6, 1, 4, 1, 1548, 6, 1, 1, 5),
    _FpWanAvgInUtil_Type()
)
fpWanAvgInUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpWanAvgInUtil.setStatus("mandatory")


class _FpWanRemoteName_Type(DisplayString):
    """Custom type fpWanRemoteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FpWanRemoteName_Type.__name__ = "DisplayString"
_FpWanRemoteName_Object = MibTableColumn
fpWanRemoteName = _FpWanRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 1548, 6, 1, 1, 6),
    _FpWanRemoteName_Type()
)
fpWanRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpWanRemoteName.setStatus("mandatory")
_FpWanRemoteTime_Type = Integer32
_FpWanRemoteTime_Object = MibTableColumn
fpWanRemoteTime = _FpWanRemoteTime_Object(
    (1, 3, 6, 1, 4, 1, 1548, 6, 1, 1, 7),
    _FpWanRemoteTime_Type()
)
fpWanRemoteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpWanRemoteTime.setStatus("mandatory")
_FpWanIfIndex_Type = Integer32
_FpWanIfIndex_Object = MibTableColumn
fpWanIfIndex = _FpWanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1548, 6, 1, 1, 8),
    _FpWanIfIndex_Type()
)
fpWanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpWanIfIndex.setStatus("mandatory")
_FpWanOutSpeed_Type = Gauge32
_FpWanOutSpeed_Object = MibTableColumn
fpWanOutSpeed = _FpWanOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1548, 6, 1, 1, 9),
    _FpWanOutSpeed_Type()
)
fpWanOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpWanOutSpeed.setStatus("mandatory")
_FpWanInSpeed_Type = Gauge32
_FpWanInSpeed_Object = MibTableColumn
fpWanInSpeed = _FpWanInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1548, 6, 1, 1, 10),
    _FpWanInSpeed_Type()
)
fpWanInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpWanInSpeed.setStatus("mandatory")
_Fppots_ObjectIdentity = ObjectIdentity
fppots = _Fppots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1548, 7)
)


class _PotsOperation_Type(Integer32):
    """Custom type potsOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("erase", 3),
          ("load", 2),
          ("save", 1))
    )


_PotsOperation_Type.__name__ = "Integer32"
_PotsOperation_Object = MibScalar
potsOperation = _PotsOperation_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 1),
    _PotsOperation_Type()
)
potsOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    potsOperation.setStatus("mandatory")
_PotsTable_Object = MibTable
potsTable = _PotsTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 2)
)
if mibBuilder.loadTexts:
    potsTable.setStatus("mandatory")
_PotsEntry_Object = MibTableRow
potsEntry = _PotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 2, 1)
)
potsEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "potsIndex"),
)
if mibBuilder.loadTexts:
    potsEntry.setStatus("mandatory")


class _PotsIndex_Type(Integer32):
    """Custom type potsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PotsIndex_Type.__name__ = "Integer32"
_PotsIndex_Object = MibTableColumn
potsIndex = _PotsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 2, 1, 1),
    _PotsIndex_Type()
)
potsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potsIndex.setStatus("mandatory")


class _PotsEnabled_Type(Integer32):
    """Custom type potsEnabled based on Integer32"""
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


_PotsEnabled_Type.__name__ = "Integer32"
_PotsEnabled_Object = MibTableColumn
potsEnabled = _PotsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 2, 1, 2),
    _PotsEnabled_Type()
)
potsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    potsEnabled.setStatus("mandatory")


class _PotsOpMode_Type(Integer32):
    """Custom type potsOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("answer", 2),
          ("both", 1),
          ("dial", 3))
    )


_PotsOpMode_Type.__name__ = "Integer32"
_PotsOpMode_Object = MibTableColumn
potsOpMode = _PotsOpMode_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 2, 1, 3),
    _PotsOpMode_Type()
)
potsOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    potsOpMode.setStatus("mandatory")


class _PotsPreemptMode_Type(Integer32):
    """Custom type potsPreemptMode based on Integer32"""
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
        *(("both", 1),
          ("in", 2),
          ("none", 4),
          ("out", 3))
    )


_PotsPreemptMode_Type.__name__ = "Integer32"
_PotsPreemptMode_Object = MibTableColumn
potsPreemptMode = _PotsPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 2, 1, 4),
    _PotsPreemptMode_Type()
)
potsPreemptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    potsPreemptMode.setStatus("mandatory")


class _PotsAutoMode_Type(Integer32):
    """Custom type potsAutoMode based on Integer32"""
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
        *(("both", 1),
          ("in", 2),
          ("none", 4),
          ("out", 3))
    )


_PotsAutoMode_Type.__name__ = "Integer32"
_PotsAutoMode_Object = MibTableColumn
potsAutoMode = _PotsAutoMode_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 2, 1, 5),
    _PotsAutoMode_Type()
)
potsAutoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    potsAutoMode.setStatus("mandatory")


class _PotsPhoneCnt_Type(Integer32):
    """Custom type potsPhoneCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PotsPhoneCnt_Type.__name__ = "Integer32"
_PotsPhoneCnt_Object = MibTableColumn
potsPhoneCnt = _PotsPhoneCnt_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 2, 1, 6),
    _PotsPhoneCnt_Type()
)
potsPhoneCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potsPhoneCnt.setStatus("mandatory")


class _PotsLocalNumber_Type(DisplayString):
    """Custom type potsLocalNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_PotsLocalNumber_Type.__name__ = "DisplayString"
_PotsLocalNumber_Object = MibTableColumn
potsLocalNumber = _PotsLocalNumber_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 2, 1, 7),
    _PotsLocalNumber_Type()
)
potsLocalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potsLocalNumber.setStatus("mandatory")


class _PotsRemoteNumber_Type(DisplayString):
    """Custom type potsRemoteNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_PotsRemoteNumber_Type.__name__ = "DisplayString"
_PotsRemoteNumber_Object = MibTableColumn
potsRemoteNumber = _PotsRemoteNumber_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 2, 1, 8),
    _PotsRemoteNumber_Type()
)
potsRemoteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potsRemoteNumber.setStatus("mandatory")


class _PotsState_Type(Integer32):
    """Custom type potsState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("connected-incoming", 8),
          ("connected-outgoing", 9),
          ("dialing", 6),
          ("disconnected", 10),
          ("entering-ip-addr", 11),
          ("held-call", 12),
          ("idle", 3),
          ("not-available", 2),
          ("other", 1),
          ("proceeding", 7),
          ("ringing", 5),
          ("wait-dialtone", 4))
    )


_PotsState_Type.__name__ = "Integer32"
_PotsState_Object = MibTableColumn
potsState = _PotsState_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 2, 1, 9),
    _PotsState_Type()
)
potsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potsState.setStatus("mandatory")


class _PotsIsdnChannel_Type(Integer32):
    """Custom type potsIsdnChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_PotsIsdnChannel_Type.__name__ = "Integer32"
_PotsIsdnChannel_Object = MibTableColumn
potsIsdnChannel = _PotsIsdnChannel_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 2, 1, 10),
    _PotsIsdnChannel_Type()
)
potsIsdnChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potsIsdnChannel.setStatus("mandatory")


class _PotsWanIndex_Type(Integer32):
    """Custom type potsWanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_PotsWanIndex_Type.__name__ = "Integer32"
_PotsWanIndex_Object = MibTableColumn
potsWanIndex = _PotsWanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 2, 1, 11),
    _PotsWanIndex_Type()
)
potsWanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potsWanIndex.setStatus("mandatory")
_PotsPhoneTable_Object = MibTable
potsPhoneTable = _PotsPhoneTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 3)
)
if mibBuilder.loadTexts:
    potsPhoneTable.setStatus("mandatory")
_PotsPhoneEntry_Object = MibTableRow
potsPhoneEntry = _PotsPhoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 3, 1)
)
potsPhoneEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "potsIndex"),
    (0, "FLOWPOINT-MIB", "potsPhoneNumber"),
)
if mibBuilder.loadTexts:
    potsPhoneEntry.setStatus("mandatory")


class _PotsPhoneNumber_Type(DisplayString):
    """Custom type potsPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_PotsPhoneNumber_Type.__name__ = "DisplayString"
_PotsPhoneNumber_Object = MibTableColumn
potsPhoneNumber = _PotsPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 3, 1, 1),
    _PotsPhoneNumber_Type()
)
potsPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    potsPhoneNumber.setStatus("mandatory")


class _PotsPhoneOperation_Type(Integer32):
    """Custom type potsPhoneOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("remove", 2))
    )


_PotsPhoneOperation_Type.__name__ = "Integer32"
_PotsPhoneOperation_Object = MibTableColumn
potsPhoneOperation = _PotsPhoneOperation_Object(
    (1, 3, 6, 1, 4, 1, 1548, 7, 3, 1, 2),
    _PotsPhoneOperation_Type()
)
potsPhoneOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    potsPhoneOperation.setStatus("mandatory")
_Fpdownload_ObjectIdentity = ObjectIdentity
fpdownload = _Fpdownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1548, 8)
)
_FpDLForceOnBoot_Type = Integer32
_FpDLForceOnBoot_Object = MibScalar
fpDLForceOnBoot = _FpDLForceOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 1),
    _FpDLForceOnBoot_Type()
)
fpDLForceOnBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpDLForceOnBoot.setStatus("mandatory")
_FpDLCommitRAMToFlash_Type = Integer32
_FpDLCommitRAMToFlash_Object = MibScalar
fpDLCommitRAMToFlash = _FpDLCommitRAMToFlash_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 2),
    _FpDLCommitRAMToFlash_Type()
)
fpDLCommitRAMToFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDLCommitRAMToFlash.setStatus("obsolete")
_FpDLInitiateColdBoot_Type = Integer32
_FpDLInitiateColdBoot_Object = MibScalar
fpDLInitiateColdBoot = _FpDLInitiateColdBoot_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 3),
    _FpDLInitiateColdBoot_Type()
)
fpDLInitiateColdBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpDLInitiateColdBoot.setStatus("mandatory")
_FpDLTFTPRequestHost_Type = IpAddress
_FpDLTFTPRequestHost_Object = MibScalar
fpDLTFTPRequestHost = _FpDLTFTPRequestHost_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 4),
    _FpDLTFTPRequestHost_Type()
)
fpDLTFTPRequestHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpDLTFTPRequestHost.setStatus("mandatory")
_FpDLTFTPRequest_Type = DisplayString
_FpDLTFTPRequest_Object = MibScalar
fpDLTFTPRequest = _FpDLTFTPRequest_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 5),
    _FpDLTFTPRequest_Type()
)
fpDLTFTPRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDLTFTPRequest.setStatus("mandatory")
_FpDLLastImageFilename_Type = DisplayString
_FpDLLastImageFilename_Object = MibScalar
fpDLLastImageFilename = _FpDLLastImageFilename_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 6),
    _FpDLLastImageFilename_Type()
)
fpDLLastImageFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDLLastImageFilename.setStatus("mandatory")
_FpDLLastServerIPAddress_Type = IpAddress
_FpDLLastServerIPAddress_Object = MibScalar
fpDLLastServerIPAddress = _FpDLLastServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 7),
    _FpDLLastServerIPAddress_Type()
)
fpDLLastServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDLLastServerIPAddress.setStatus("mandatory")
_FpDLFlashSize_Type = Integer32
_FpDLFlashSize_Object = MibScalar
fpDLFlashSize = _FpDLFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 8),
    _FpDLFlashSize_Type()
)
fpDLFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDLFlashSize.setStatus("mandatory")
_FpDLFlashCount_Type = Integer32
_FpDLFlashCount_Object = MibScalar
fpDLFlashCount = _FpDLFlashCount_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 9),
    _FpDLFlashCount_Type()
)
fpDLFlashCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDLFlashCount.setStatus("mandatory")
_FpDLFirmwareBase_Type = Integer32
_FpDLFirmwareBase_Object = MibScalar
fpDLFirmwareBase = _FpDLFirmwareBase_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 10),
    _FpDLFirmwareBase_Type()
)
fpDLFirmwareBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDLFirmwareBase.setStatus("mandatory")
_FpDLFirmwareTop_Type = Integer32
_FpDLFirmwareTop_Object = MibScalar
fpDLFirmwareTop = _FpDLFirmwareTop_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 11),
    _FpDLFirmwareTop_Type()
)
fpDLFirmwareTop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDLFirmwareTop.setStatus("mandatory")
_FpDLFirmwareStart_Type = Integer32
_FpDLFirmwareStart_Object = MibScalar
fpDLFirmwareStart = _FpDLFirmwareStart_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 12),
    _FpDLFirmwareStart_Type()
)
fpDLFirmwareStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDLFirmwareStart.setStatus("mandatory")


class _FpDLBootRev_Type(OctetString):
    """Custom type fpDLBootRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_FpDLBootRev_Type.__name__ = "OctetString"
_FpDLBootRev_Object = MibScalar
fpDLBootRev = _FpDLBootRev_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 13),
    _FpDLBootRev_Type()
)
fpDLBootRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDLBootRev.setStatus("mandatory")
_FpDLForceBootp_Type = Integer32
_FpDLForceBootp_Object = MibScalar
fpDLForceBootp = _FpDLForceBootp_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 14),
    _FpDLForceBootp_Type()
)
fpDLForceBootp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpDLForceBootp.setStatus("mandatory")
_FpDLServerName_Type = OctetString
_FpDLServerName_Object = MibScalar
fpDLServerName = _FpDLServerName_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 15),
    _FpDLServerName_Type()
)
fpDLServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpDLServerName.setStatus("mandatory")


class _FpDLOnLineDownLoad_Type(Integer32):
    """Custom type fpDLOnLineDownLoad based on Integer32"""
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
        *(("forceDownLoad", 2),
          ("forceDownLoadReset", 3),
          ("forceRemove", 5),
          ("forceUpLoad", 4),
          ("normalOperation", 1))
    )


_FpDLOnLineDownLoad_Type.__name__ = "Integer32"
_FpDLOnLineDownLoad_Object = MibScalar
fpDLOnLineDownLoad = _FpDLOnLineDownLoad_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 16),
    _FpDLOnLineDownLoad_Type()
)
fpDLOnLineDownLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpDLOnLineDownLoad.setStatus("mandatory")


class _FpDLOperStatus_Type(Integer32):
    """Custom type fpDLOperStatus based on Integer32"""
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
        *(("downLoadActive", 4),
          ("downLoadCompleteError", 5),
          ("normalOperation", 3),
          ("other", 1),
          ("removeActive", 8),
          ("removeCompleteError", 9),
          ("unknown", 2),
          ("upLoadActive", 6),
          ("upLoadCompleteError", 7))
    )


_FpDLOperStatus_Type.__name__ = "Integer32"
_FpDLOperStatus_Object = MibScalar
fpDLOperStatus = _FpDLOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 17),
    _FpDLOperStatus_Type()
)
fpDLOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDLOperStatus.setStatus("mandatory")
_FpDLNetAddress_Type = IpAddress
_FpDLNetAddress_Object = MibScalar
fpDLNetAddress = _FpDLNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 18),
    _FpDLNetAddress_Type()
)
fpDLNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpDLNetAddress.setStatus("mandatory")


class _FpDLFileName_Type(DisplayString):
    """Custom type fpDLFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_FpDLFileName_Type.__name__ = "DisplayString"
_FpDLFileName_Object = MibScalar
fpDLFileName = _FpDLFileName_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 19),
    _FpDLFileName_Type()
)
fpDLFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpDLFileName.setStatus("mandatory")
_FpDLErrorString_Type = DisplayString
_FpDLErrorString_Object = MibScalar
fpDLErrorString = _FpDLErrorString_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 20),
    _FpDLErrorString_Type()
)
fpDLErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDLErrorString.setStatus("mandatory")
_FpDLTftpServerGatewayIPAddress_Type = IpAddress
_FpDLTftpServerGatewayIPAddress_Object = MibScalar
fpDLTftpServerGatewayIPAddress = _FpDLTftpServerGatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 21),
    _FpDLTftpServerGatewayIPAddress_Type()
)
fpDLTftpServerGatewayIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpDLTftpServerGatewayIPAddress.setStatus("mandatory")
_FpDLBlockCount_Type = Integer32
_FpDLBlockCount_Object = MibScalar
fpDLBlockCount = _FpDLBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 22),
    _FpDLBlockCount_Type()
)
fpDLBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDLBlockCount.setStatus("mandatory")


class _FpDLBootPartitionStatus_Type(Integer32):
    """Custom type fpDLBootPartitionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1),
          ("inProgress", 3))
    )


_FpDLBootPartitionStatus_Type.__name__ = "Integer32"
_FpDLBootPartitionStatus_Object = MibScalar
fpDLBootPartitionStatus = _FpDLBootPartitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 23),
    _FpDLBootPartitionStatus_Type()
)
fpDLBootPartitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDLBootPartitionStatus.setStatus("mandatory")


class _FpDLLocalFileName_Type(DisplayString):
    """Custom type fpDLLocalFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_FpDLLocalFileName_Type.__name__ = "DisplayString"
_FpDLLocalFileName_Object = MibScalar
fpDLLocalFileName = _FpDLLocalFileName_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 24),
    _FpDLLocalFileName_Type()
)
fpDLLocalFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fpDLLocalFileName.setStatus("mandatory")


class _FpDLBootVersion_Type(DisplayString):
    """Custom type fpDLBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_FpDLBootVersion_Type.__name__ = "DisplayString"
_FpDLBootVersion_Object = MibScalar
fpDLBootVersion = _FpDLBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 25),
    _FpDLBootVersion_Type()
)
fpDLBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDLBootVersion.setStatus("mandatory")


class _FpDLBootReason_Type(Integer32):
    """Custom type fpDLBootReason based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("double-bus-fault", 5),
          ("hardware-watchdog", 6),
          ("loss-of-clock", 7),
          ("other", 1),
          ("power-up", 2),
          ("reset-switch", 3),
          ("software-reboot", 4),
          ("suicide", 8))
    )


_FpDLBootReason_Type.__name__ = "Integer32"
_FpDLBootReason_Object = MibScalar
fpDLBootReason = _FpDLBootReason_Object(
    (1, 3, 6, 1, 4, 1, 1548, 8, 26),
    _FpDLBootReason_Type()
)
fpDLBootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDLBootReason.setStatus("mandatory")
_Fpiptranslate_ObjectIdentity = ObjectIdentity
fpiptranslate = _Fpiptranslate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1548, 9)
)
_SysIPTranslationServerTable_Object = MibTable
sysIPTranslationServerTable = _SysIPTranslationServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 9, 1)
)
if mibBuilder.loadTexts:
    sysIPTranslationServerTable.setStatus("mandatory")
_SysIPTranslationServerEntry_Object = MibTableRow
sysIPTranslationServerEntry = _SysIPTranslationServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 9, 1, 1)
)
sysIPTranslationServerEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "sysIPTranslationServerIPAddress"),
    (0, "FLOWPOINT-MIB", "sysIPTranslationProtocol"),
    (0, "FLOWPOINT-MIB", "sysIPFirstTranslationPort"),
)
if mibBuilder.loadTexts:
    sysIPTranslationServerEntry.setStatus("mandatory")
_SysIPTranslationServerIPAddress_Type = IpAddress
_SysIPTranslationServerIPAddress_Object = MibTableColumn
sysIPTranslationServerIPAddress = _SysIPTranslationServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 9, 1, 1, 1),
    _SysIPTranslationServerIPAddress_Type()
)
sysIPTranslationServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIPTranslationServerIPAddress.setStatus("mandatory")


class _SysIPTranslationProtocol_Type(OctetString):
    """Custom type sysIPTranslationProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SysIPTranslationProtocol_Type.__name__ = "OctetString"
_SysIPTranslationProtocol_Object = MibTableColumn
sysIPTranslationProtocol = _SysIPTranslationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1548, 9, 1, 1, 2),
    _SysIPTranslationProtocol_Type()
)
sysIPTranslationProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIPTranslationProtocol.setStatus("mandatory")


class _SysIPFirstTranslationPort_Type(OctetString):
    """Custom type sysIPFirstTranslationPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SysIPFirstTranslationPort_Type.__name__ = "OctetString"
_SysIPFirstTranslationPort_Object = MibTableColumn
sysIPFirstTranslationPort = _SysIPFirstTranslationPort_Object(
    (1, 3, 6, 1, 4, 1, 1548, 9, 1, 1, 3),
    _SysIPFirstTranslationPort_Type()
)
sysIPFirstTranslationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIPFirstTranslationPort.setStatus("mandatory")


class _SysIPLastTranslationPort_Type(OctetString):
    """Custom type sysIPLastTranslationPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SysIPLastTranslationPort_Type.__name__ = "OctetString"
_SysIPLastTranslationPort_Object = MibTableColumn
sysIPLastTranslationPort = _SysIPLastTranslationPort_Object(
    (1, 3, 6, 1, 4, 1, 1548, 9, 1, 1, 4),
    _SysIPLastTranslationPort_Type()
)
sysIPLastTranslationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIPLastTranslationPort.setStatus("mandatory")


class _SysIPFirstPrivatePort_Type(OctetString):
    """Custom type sysIPFirstPrivatePort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SysIPFirstPrivatePort_Type.__name__ = "OctetString"
_SysIPFirstPrivatePort_Object = MibTableColumn
sysIPFirstPrivatePort = _SysIPFirstPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 1548, 9, 1, 1, 5),
    _SysIPFirstPrivatePort_Type()
)
sysIPFirstPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIPFirstPrivatePort.setStatus("mandatory")
_SysIPTranslationStatus_Type = RowStatus
_SysIPTranslationStatus_Object = MibTableColumn
sysIPTranslationStatus = _SysIPTranslationStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 9, 1, 1, 6),
    _SysIPTranslationStatus_Type()
)
sysIPTranslationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIPTranslationStatus.setStatus("mandatory")
_SysNatHostMappingTable_Object = MibTable
sysNatHostMappingTable = _SysNatHostMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 9, 2)
)
if mibBuilder.loadTexts:
    sysNatHostMappingTable.setStatus("mandatory")
_SysNatHostMappingEntry_Object = MibTableRow
sysNatHostMappingEntry = _SysNatHostMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 9, 2, 1)
)
sysNatHostMappingEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "sysFirstPrivateIPAddress"),
    (0, "FLOWPOINT-MIB", "sysLastPrivateIPAddress"),
    (0, "FLOWPOINT-MIB", "sysFirstPublicIPAddress"),
)
if mibBuilder.loadTexts:
    sysNatHostMappingEntry.setStatus("mandatory")
_SysFirstPrivateIPAddress_Type = IpAddress
_SysFirstPrivateIPAddress_Object = MibTableColumn
sysFirstPrivateIPAddress = _SysFirstPrivateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 9, 2, 1, 1),
    _SysFirstPrivateIPAddress_Type()
)
sysFirstPrivateIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFirstPrivateIPAddress.setStatus("mandatory")
_SysLastPrivateIPAddress_Type = IpAddress
_SysLastPrivateIPAddress_Object = MibTableColumn
sysLastPrivateIPAddress = _SysLastPrivateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 9, 2, 1, 2),
    _SysLastPrivateIPAddress_Type()
)
sysLastPrivateIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLastPrivateIPAddress.setStatus("mandatory")
_SysFirstPublicIPAddress_Type = IpAddress
_SysFirstPublicIPAddress_Object = MibTableColumn
sysFirstPublicIPAddress = _SysFirstPublicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 9, 2, 1, 3),
    _SysFirstPublicIPAddress_Type()
)
sysFirstPublicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFirstPublicIPAddress.setStatus("mandatory")
_SysNatHostMappingStatus_Type = RowStatus
_SysNatHostMappingStatus_Object = MibTableColumn
sysNatHostMappingStatus = _SysNatHostMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 9, 2, 1, 4),
    _SysNatHostMappingStatus_Type()
)
sysNatHostMappingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNatHostMappingStatus.setStatus("mandatory")
_Fpdhcp_ObjectIdentity = ObjectIdentity
fpdhcp = _Fpdhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1548, 10)
)


class _DhcpOperation_Type(Integer32):
    """Custom type dhcpOperation based on Integer32"""
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
        *(("dhcpdisable", 5),
          ("dhcpenable", 4),
          ("erase", 3),
          ("load", 2),
          ("save", 1))
    )


_DhcpOperation_Type.__name__ = "Integer32"
_DhcpOperation_Object = MibScalar
dhcpOperation = _DhcpOperation_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 1),
    _DhcpOperation_Type()
)
dhcpOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dhcpOperation.setStatus("mandatory")
_DhcpGlobalTftpServer_Type = IpAddress
_DhcpGlobalTftpServer_Object = MibScalar
dhcpGlobalTftpServer = _DhcpGlobalTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 2),
    _DhcpGlobalTftpServer_Type()
)
dhcpGlobalTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpGlobalTftpServer.setStatus("mandatory")


class _DhcpGlobalTftpFile_Type(DisplayString):
    """Custom type dhcpGlobalTftpFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpGlobalTftpFile_Type.__name__ = "DisplayString"
_DhcpGlobalTftpFile_Object = MibScalar
dhcpGlobalTftpFile = _DhcpGlobalTftpFile_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 3),
    _DhcpGlobalTftpFile_Type()
)
dhcpGlobalTftpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpGlobalTftpFile.setStatus("mandatory")
_DhcpGlobalLeaseTime_Type = Integer32
_DhcpGlobalLeaseTime_Object = MibScalar
dhcpGlobalLeaseTime = _DhcpGlobalLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 4),
    _DhcpGlobalLeaseTime_Type()
)
dhcpGlobalLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpGlobalLeaseTime.setStatus("mandatory")
_DhcpCodeTable_Object = MibTable
dhcpCodeTable = _DhcpCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 5)
)
if mibBuilder.loadTexts:
    dhcpCodeTable.setStatus("mandatory")
_DhcpCodeEntry_Object = MibTableRow
dhcpCodeEntry = _DhcpCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 5, 1)
)
dhcpCodeEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dhcpOptionCode"),
)
if mibBuilder.loadTexts:
    dhcpCodeEntry.setStatus("mandatory")


class _DhcpOptionCode_Type(Integer32):
    """Custom type dhcpOptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DhcpOptionCode_Type.__name__ = "Integer32"
_DhcpOptionCode_Object = MibTableColumn
dhcpOptionCode = _DhcpOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 5, 1, 1),
    _DhcpOptionCode_Type()
)
dhcpOptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpOptionCode.setStatus("mandatory")


class _DhcpMinCount_Type(Integer32):
    """Custom type dhcpMinCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DhcpMinCount_Type.__name__ = "Integer32"
_DhcpMinCount_Object = MibTableColumn
dhcpMinCount = _DhcpMinCount_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 5, 1, 2),
    _DhcpMinCount_Type()
)
dhcpMinCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpMinCount.setStatus("mandatory")


class _DhcpMaxCount_Type(Integer32):
    """Custom type dhcpMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DhcpMaxCount_Type.__name__ = "Integer32"
_DhcpMaxCount_Object = MibTableColumn
dhcpMaxCount = _DhcpMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 5, 1, 3),
    _DhcpMaxCount_Type()
)
dhcpMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpMaxCount.setStatus("mandatory")
_DhcpOptionType_Type = DhcpOptionType
_DhcpOptionType_Object = MibTableColumn
dhcpOptionType = _DhcpOptionType_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 5, 1, 4),
    _DhcpOptionType_Type()
)
dhcpOptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpOptionType.setStatus("mandatory")
_DhcpOptionCodeStatus_Type = RowStatus
_DhcpOptionCodeStatus_Object = MibTableColumn
dhcpOptionCodeStatus = _DhcpOptionCodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 5, 1, 5),
    _DhcpOptionCodeStatus_Type()
)
dhcpOptionCodeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOptionCodeStatus.setStatus("mandatory")
_DhcpGlobalValueTable_Object = MibTable
dhcpGlobalValueTable = _DhcpGlobalValueTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 6)
)
if mibBuilder.loadTexts:
    dhcpGlobalValueTable.setStatus("mandatory")
_DhcpGlobalValueEntry_Object = MibTableRow
dhcpGlobalValueEntry = _DhcpGlobalValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 6, 1)
)
dhcpGlobalValueEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dhcpGlobalValueCode"),
)
if mibBuilder.loadTexts:
    dhcpGlobalValueEntry.setStatus("mandatory")


class _DhcpGlobalValueCode_Type(Integer32):
    """Custom type dhcpGlobalValueCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DhcpGlobalValueCode_Type.__name__ = "Integer32"
_DhcpGlobalValueCode_Object = MibTableColumn
dhcpGlobalValueCode = _DhcpGlobalValueCode_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 6, 1, 1),
    _DhcpGlobalValueCode_Type()
)
dhcpGlobalValueCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpGlobalValueCode.setStatus("mandatory")
_DhcpGlobalValueType_Type = DhcpOptionType
_DhcpGlobalValueType_Object = MibTableColumn
dhcpGlobalValueType = _DhcpGlobalValueType_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 6, 1, 2),
    _DhcpGlobalValueType_Type()
)
dhcpGlobalValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpGlobalValueType.setStatus("mandatory")


class _DhcpGlobalValue_Type(OctetString):
    """Custom type dhcpGlobalValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpGlobalValue_Type.__name__ = "OctetString"
_DhcpGlobalValue_Object = MibTableColumn
dhcpGlobalValue = _DhcpGlobalValue_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 6, 1, 3),
    _DhcpGlobalValue_Type()
)
dhcpGlobalValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpGlobalValue.setStatus("mandatory")
_DhcpGlobalValueStatus_Type = RowStatus
_DhcpGlobalValueStatus_Object = MibTableColumn
dhcpGlobalValueStatus = _DhcpGlobalValueStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 6, 1, 4),
    _DhcpGlobalValueStatus_Type()
)
dhcpGlobalValueStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpGlobalValueStatus.setStatus("mandatory")
_DhcpSubnetTable_Object = MibTable
dhcpSubnetTable = _DhcpSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 7)
)
if mibBuilder.loadTexts:
    dhcpSubnetTable.setStatus("mandatory")
_DhcpSubnetEntry_Object = MibTableRow
dhcpSubnetEntry = _DhcpSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 7, 1)
)
dhcpSubnetEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dhcpSubnetAddress"),
)
if mibBuilder.loadTexts:
    dhcpSubnetEntry.setStatus("mandatory")
_DhcpSubnetAddress_Type = IpAddress
_DhcpSubnetAddress_Object = MibTableColumn
dhcpSubnetAddress = _DhcpSubnetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 7, 1, 1),
    _DhcpSubnetAddress_Type()
)
dhcpSubnetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSubnetAddress.setStatus("mandatory")
_DhcpSubnetMask_Type = IpAddress
_DhcpSubnetMask_Object = MibTableColumn
dhcpSubnetMask = _DhcpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 7, 1, 2),
    _DhcpSubnetMask_Type()
)
dhcpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetMask.setStatus("mandatory")
_DhcpSubnetFirstIpAddress_Type = IpAddress
_DhcpSubnetFirstIpAddress_Object = MibTableColumn
dhcpSubnetFirstIpAddress = _DhcpSubnetFirstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 7, 1, 3),
    _DhcpSubnetFirstIpAddress_Type()
)
dhcpSubnetFirstIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetFirstIpAddress.setStatus("mandatory")
_DhcpSubnetLastIpAddress_Type = IpAddress
_DhcpSubnetLastIpAddress_Object = MibTableColumn
dhcpSubnetLastIpAddress = _DhcpSubnetLastIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 7, 1, 4),
    _DhcpSubnetLastIpAddress_Type()
)
dhcpSubnetLastIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetLastIpAddress.setStatus("mandatory")
_DhcpSubnetTftpServer_Type = IpAddress
_DhcpSubnetTftpServer_Object = MibTableColumn
dhcpSubnetTftpServer = _DhcpSubnetTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 7, 1, 5),
    _DhcpSubnetTftpServer_Type()
)
dhcpSubnetTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetTftpServer.setStatus("mandatory")


class _DhcpSubnetTftpFile_Type(DisplayString):
    """Custom type dhcpSubnetTftpFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpSubnetTftpFile_Type.__name__ = "DisplayString"
_DhcpSubnetTftpFile_Object = MibTableColumn
dhcpSubnetTftpFile = _DhcpSubnetTftpFile_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 7, 1, 6),
    _DhcpSubnetTftpFile_Type()
)
dhcpSubnetTftpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetTftpFile.setStatus("mandatory")


class _DhcpSubnetBootp_Type(Integer32):
    """Custom type dhcpSubnetBootp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_DhcpSubnetBootp_Type.__name__ = "Integer32"
_DhcpSubnetBootp_Object = MibTableColumn
dhcpSubnetBootp = _DhcpSubnetBootp_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 7, 1, 7),
    _DhcpSubnetBootp_Type()
)
dhcpSubnetBootp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetBootp.setStatus("mandatory")
_DhcpSubnetLeaseTime_Type = Integer32
_DhcpSubnetLeaseTime_Object = MibTableColumn
dhcpSubnetLeaseTime = _DhcpSubnetLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 7, 1, 8),
    _DhcpSubnetLeaseTime_Type()
)
dhcpSubnetLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetLeaseTime.setStatus("mandatory")
_DhcpSubnetStatus_Type = RowStatus
_DhcpSubnetStatus_Object = MibTableColumn
dhcpSubnetStatus = _DhcpSubnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 7, 1, 9),
    _DhcpSubnetStatus_Type()
)
dhcpSubnetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetStatus.setStatus("mandatory")


class _DhcpSubnetConflictActions_Type(Integer32):
    """Custom type dhcpSubnetConflictActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("docontinue", 1),
          ("dostop", 2))
    )


_DhcpSubnetConflictActions_Type.__name__ = "Integer32"
_DhcpSubnetConflictActions_Object = MibTableColumn
dhcpSubnetConflictActions = _DhcpSubnetConflictActions_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 7, 1, 10),
    _DhcpSubnetConflictActions_Type()
)
dhcpSubnetConflictActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetConflictActions.setStatus("mandatory")
_DhcpSubnetValueTable_Object = MibTable
dhcpSubnetValueTable = _DhcpSubnetValueTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 8)
)
if mibBuilder.loadTexts:
    dhcpSubnetValueTable.setStatus("mandatory")
_DhcpSubnetValueEntry_Object = MibTableRow
dhcpSubnetValueEntry = _DhcpSubnetValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 8, 1)
)
dhcpSubnetValueEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dhcpSubnetAddress"),
    (0, "FLOWPOINT-MIB", "dhcpSubnetValueCode"),
)
if mibBuilder.loadTexts:
    dhcpSubnetValueEntry.setStatus("mandatory")


class _DhcpSubnetValueCode_Type(Integer32):
    """Custom type dhcpSubnetValueCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DhcpSubnetValueCode_Type.__name__ = "Integer32"
_DhcpSubnetValueCode_Object = MibTableColumn
dhcpSubnetValueCode = _DhcpSubnetValueCode_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 8, 1, 1),
    _DhcpSubnetValueCode_Type()
)
dhcpSubnetValueCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSubnetValueCode.setStatus("mandatory")
_DhcpSubnetValueType_Type = DhcpOptionType
_DhcpSubnetValueType_Object = MibTableColumn
dhcpSubnetValueType = _DhcpSubnetValueType_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 8, 1, 2),
    _DhcpSubnetValueType_Type()
)
dhcpSubnetValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSubnetValueType.setStatus("mandatory")


class _DhcpSubnetValue_Type(OctetString):
    """Custom type dhcpSubnetValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpSubnetValue_Type.__name__ = "OctetString"
_DhcpSubnetValue_Object = MibTableColumn
dhcpSubnetValue = _DhcpSubnetValue_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 8, 1, 3),
    _DhcpSubnetValue_Type()
)
dhcpSubnetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetValue.setStatus("mandatory")
_DhcpSubnetValueStatus_Type = RowStatus
_DhcpSubnetValueStatus_Object = MibTableColumn
dhcpSubnetValueStatus = _DhcpSubnetValueStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 8, 1, 4),
    _DhcpSubnetValueStatus_Type()
)
dhcpSubnetValueStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSubnetValueStatus.setStatus("mandatory")
_DhcpClientTable_Object = MibTable
dhcpClientTable = _DhcpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 9)
)
if mibBuilder.loadTexts:
    dhcpClientTable.setStatus("mandatory")
_DhcpClientEntry_Object = MibTableRow
dhcpClientEntry = _DhcpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 9, 1)
)
dhcpClientEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dhcpClientAddress"),
)
if mibBuilder.loadTexts:
    dhcpClientEntry.setStatus("mandatory")
_DhcpClientAddress_Type = IpAddress
_DhcpClientAddress_Object = MibTableColumn
dhcpClientAddress = _DhcpClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 9, 1, 1),
    _DhcpClientAddress_Type()
)
dhcpClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientAddress.setStatus("mandatory")
_DhcpClientTftpServer_Type = IpAddress
_DhcpClientTftpServer_Object = MibTableColumn
dhcpClientTftpServer = _DhcpClientTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 9, 1, 2),
    _DhcpClientTftpServer_Type()
)
dhcpClientTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientTftpServer.setStatus("mandatory")


class _DhcpClientTftpFile_Type(DisplayString):
    """Custom type dhcpClientTftpFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpClientTftpFile_Type.__name__ = "DisplayString"
_DhcpClientTftpFile_Object = MibTableColumn
dhcpClientTftpFile = _DhcpClientTftpFile_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 9, 1, 3),
    _DhcpClientTftpFile_Type()
)
dhcpClientTftpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientTftpFile.setStatus("mandatory")


class _DhcpClientBootp_Type(Integer32):
    """Custom type dhcpClientBootp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_DhcpClientBootp_Type.__name__ = "Integer32"
_DhcpClientBootp_Object = MibTableColumn
dhcpClientBootp = _DhcpClientBootp_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 9, 1, 4),
    _DhcpClientBootp_Type()
)
dhcpClientBootp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientBootp.setStatus("mandatory")
_DhcpClientLeaseTime_Type = Integer32
_DhcpClientLeaseTime_Object = MibTableColumn
dhcpClientLeaseTime = _DhcpClientLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 9, 1, 5),
    _DhcpClientLeaseTime_Type()
)
dhcpClientLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientLeaseTime.setStatus("mandatory")
_DhcpClientExpireTimeYear_Type = Integer32
_DhcpClientExpireTimeYear_Object = MibTableColumn
dhcpClientExpireTimeYear = _DhcpClientExpireTimeYear_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 9, 1, 6),
    _DhcpClientExpireTimeYear_Type()
)
dhcpClientExpireTimeYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientExpireTimeYear.setStatus("mandatory")


class _DhcpClientExpireTimeMonth_Type(Integer32):
    """Custom type dhcpClientExpireTimeMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DhcpClientExpireTimeMonth_Type.__name__ = "Integer32"
_DhcpClientExpireTimeMonth_Object = MibTableColumn
dhcpClientExpireTimeMonth = _DhcpClientExpireTimeMonth_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 9, 1, 7),
    _DhcpClientExpireTimeMonth_Type()
)
dhcpClientExpireTimeMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientExpireTimeMonth.setStatus("mandatory")


class _DhcpClientExpireTimeDay_Type(Integer32):
    """Custom type dhcpClientExpireTimeDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DhcpClientExpireTimeDay_Type.__name__ = "Integer32"
_DhcpClientExpireTimeDay_Object = MibTableColumn
dhcpClientExpireTimeDay = _DhcpClientExpireTimeDay_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 9, 1, 8),
    _DhcpClientExpireTimeDay_Type()
)
dhcpClientExpireTimeDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientExpireTimeDay.setStatus("mandatory")


class _DhcpClientExpireTimeHour_Type(Integer32):
    """Custom type dhcpClientExpireTimeHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DhcpClientExpireTimeHour_Type.__name__ = "Integer32"
_DhcpClientExpireTimeHour_Object = MibTableColumn
dhcpClientExpireTimeHour = _DhcpClientExpireTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 9, 1, 9),
    _DhcpClientExpireTimeHour_Type()
)
dhcpClientExpireTimeHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientExpireTimeHour.setStatus("mandatory")


class _DhcpClientExpireTimeMinute_Type(Integer32):
    """Custom type dhcpClientExpireTimeMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DhcpClientExpireTimeMinute_Type.__name__ = "Integer32"
_DhcpClientExpireTimeMinute_Object = MibTableColumn
dhcpClientExpireTimeMinute = _DhcpClientExpireTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 9, 1, 10),
    _DhcpClientExpireTimeMinute_Type()
)
dhcpClientExpireTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientExpireTimeMinute.setStatus("mandatory")


class _DhcpClientExpireTimeSecond_Type(Integer32):
    """Custom type dhcpClientExpireTimeSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DhcpClientExpireTimeSecond_Type.__name__ = "Integer32"
_DhcpClientExpireTimeSecond_Object = MibTableColumn
dhcpClientExpireTimeSecond = _DhcpClientExpireTimeSecond_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 9, 1, 11),
    _DhcpClientExpireTimeSecond_Type()
)
dhcpClientExpireTimeSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientExpireTimeSecond.setStatus("mandatory")
_DhcpClientStatus_Type = RowStatus
_DhcpClientStatus_Object = MibTableColumn
dhcpClientStatus = _DhcpClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 9, 1, 12),
    _DhcpClientStatus_Type()
)
dhcpClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientStatus.setStatus("mandatory")
_DhcpClientValueTable_Object = MibTable
dhcpClientValueTable = _DhcpClientValueTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 10)
)
if mibBuilder.loadTexts:
    dhcpClientValueTable.setStatus("mandatory")
_DhcpClientValueEntry_Object = MibTableRow
dhcpClientValueEntry = _DhcpClientValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 10, 1)
)
dhcpClientValueEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "dhcpClientAddress"),
    (0, "FLOWPOINT-MIB", "dhcpClientValueCode"),
)
if mibBuilder.loadTexts:
    dhcpClientValueEntry.setStatus("mandatory")


class _DhcpClientValueCode_Type(Integer32):
    """Custom type dhcpClientValueCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DhcpClientValueCode_Type.__name__ = "Integer32"
_DhcpClientValueCode_Object = MibTableColumn
dhcpClientValueCode = _DhcpClientValueCode_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 10, 1, 1),
    _DhcpClientValueCode_Type()
)
dhcpClientValueCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientValueCode.setStatus("mandatory")
_DhcpClientValueType_Type = DhcpOptionType
_DhcpClientValueType_Object = MibTableColumn
dhcpClientValueType = _DhcpClientValueType_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 10, 1, 2),
    _DhcpClientValueType_Type()
)
dhcpClientValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpClientValueType.setStatus("mandatory")


class _DhcpClientValue_Type(OctetString):
    """Custom type dhcpClientValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpClientValue_Type.__name__ = "OctetString"
_DhcpClientValue_Object = MibTableColumn
dhcpClientValue = _DhcpClientValue_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 10, 1, 3),
    _DhcpClientValue_Type()
)
dhcpClientValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientValue.setStatus("mandatory")
_DhcpClientValueStatus_Type = RowStatus
_DhcpClientValueStatus_Object = MibTableColumn
dhcpClientValueStatus = _DhcpClientValueStatus_Object(
    (1, 3, 6, 1, 4, 1, 1548, 10, 10, 1, 4),
    _DhcpClientValueStatus_Type()
)
dhcpClientValueStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpClientValueStatus.setStatus("mandatory")
_Fpdir_ObjectIdentity = ObjectIdentity
fpdir = _Fpdir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1548, 11)
)
_FpDirTable_Object = MibTable
fpDirTable = _FpDirTable_Object(
    (1, 3, 6, 1, 4, 1, 1548, 11, 1)
)
if mibBuilder.loadTexts:
    fpDirTable.setStatus("mandatory")
_FpDirEntry_Object = MibTableRow
fpDirEntry = _FpDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 1548, 11, 1, 1)
)
fpDirEntry.setIndexNames(
    (0, "FLOWPOINT-MIB", "fpDirIndex"),
)
if mibBuilder.loadTexts:
    fpDirEntry.setStatus("mandatory")


class _FpDirIndex_Type(Integer32):
    """Custom type fpDirIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_FpDirIndex_Type.__name__ = "Integer32"
_FpDirIndex_Object = MibTableColumn
fpDirIndex = _FpDirIndex_Object(
    (1, 3, 6, 1, 4, 1, 1548, 11, 1, 1, 1),
    _FpDirIndex_Type()
)
fpDirIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDirIndex.setStatus("mandatory")


class _FpDirName_Type(DisplayString):
    """Custom type fpDirName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_FpDirName_Type.__name__ = "DisplayString"
_FpDirName_Object = MibTableColumn
fpDirName = _FpDirName_Object(
    (1, 3, 6, 1, 4, 1, 1548, 11, 1, 1, 2),
    _FpDirName_Type()
)
fpDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDirName.setStatus("mandatory")
_FpDirSize_Type = Integer32
_FpDirSize_Object = MibTableColumn
fpDirSize = _FpDirSize_Object(
    (1, 3, 6, 1, 4, 1, 1548, 11, 1, 1, 3),
    _FpDirSize_Type()
)
fpDirSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fpDirSize.setStatus("mandatory")
_Fpatm_ObjectIdentity = ObjectIdentity
fpatm = _Fpatm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1548, 12)
)


class _AtmOperation_Type(Integer32):
    """Custom type atmOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("erase", 3),
          ("load", 2),
          ("save", 1))
    )


_AtmOperation_Type.__name__ = "Integer32"
_AtmOperation_Object = MibScalar
atmOperation = _AtmOperation_Object(
    (1, 3, 6, 1, 4, 1, 1548, 12, 1),
    _AtmOperation_Type()
)
atmOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    atmOperation.setStatus("mandatory")
_Fpfr_ObjectIdentity = ObjectIdentity
fpfr = _Fpfr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1548, 13)
)


class _FrOperation_Type(Integer32):
    """Custom type frOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("erase", 3),
          ("load", 2),
          ("save", 1))
    )


_FrOperation_Type.__name__ = "Integer32"
_FrOperation_Object = MibScalar
frOperation = _FrOperation_Object(
    (1, 3, 6, 1, 4, 1, 1548, 13, 1),
    _FrOperation_Type()
)
frOperation.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    frOperation.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FLOWPOINT-MIB",
    **{"IpxNetAddress": IpxNetAddress,
       "MacAddress": MacAddress,
       "ConnectionType": ConnectionType,
       "AuthenProtoType": AuthenProtoType,
       "RowStatus": RowStatus,
       "DhcpOptionType": DhcpOptionType,
       "flowpoint": flowpoint,
       "fpdod": fpdod,
       "dodTable": dodTable,
       "dodEntry": dodEntry,
       "dodTableID": dodTableID,
       "dodDestinationName": dodDestinationName,
       "dodPassword": dodPassword,
       "dodAuthenProtocol": dodAuthenProtocol,
       "dodMaxLinks": dodMaxLinks,
       "dodBWThreshold": dodBWThreshold,
       "dodPreferType": dodPreferType,
       "dodTearDownTimer": dodTearDownTimer,
       "dodSourceIPAddress": dodSourceIPAddress,
       "dodRemoteIPAddress": dodRemoteIPAddress,
       "dodSourceIPMask": dodSourceIPMask,
       "dodRemoteIPMask": dodRemoteIPMask,
       "dodIPXNetAddress": dodIPXNetAddress,
       "dodIPFilters": dodIPFilters,
       "dodIPXFilters": dodIPXFilters,
       "dodRemoteIPNets": dodRemoteIPNets,
       "dodRemoteIPXNets": dodRemoteIPXNets,
       "dodRemoteIPXSAPs": dodRemoteIPXSAPs,
       "dodRemoteMacState": dodRemoteMacState,
       "dodRemoteMacs": dodRemoteMacs,
       "dodLastActivityTime": dodLastActivityTime,
       "dodTableOperation": dodTableOperation,
       "dodMinLinks": dodMinLinks,
       "dodBODType": dodBODType,
       "dodIpOptRecvRIP": dodIpOptRecvRIP,
       "dodIpOptSendRIP": dodIpOptSendRIP,
       "dodIpOptRecvRIPDefault": dodIpOptRecvRIPDefault,
       "dodIpOptSendRIPDefault": dodIpOptSendRIPDefault,
       "dodIpOptKeepPrivate": dodIpOptKeepPrivate,
       "dodBrOptUseStp": dodBrOptUseStp,
       "dodPPPOptUseLCPEcho": dodPPPOptUseLCPEcho,
       "dodEntryIsDisabled": dodEntryIsDisabled,
       "dodCallbackOption": dodCallbackOption,
       "dodSendDataAsVoice": dodSendDataAsVoice,
       "dodIPXNetStrAddress": dodIPXNetStrAddress,
       "dodOurSystemName": dodOurSystemName,
       "dodOurPassword": dodOurPassword,
       "dodPPPCallbackOption": dodPPPCallbackOption,
       "dodPPPCallbackInfo": dodPPPCallbackInfo,
       "dodDontAuthenticate": dodDontAuthenticate,
       "dodIPAddressTranslation": dodIPAddressTranslation,
       "dodIpOptRecvRIP1": dodIpOptRecvRIP1,
       "dodIpOptSendRIP1": dodIpOptSendRIP1,
       "dodIpOptRecvRIP2": dodIpOptRecvRIP2,
       "dodIpOptSendRIP2": dodIpOptSendRIP2,
       "dodProtocol": dodProtocol,
       "dodCompression": dodCompression,
       "dodPasswordSpecified": dodPasswordSpecified,
       "dodOurPasswordSpecified": dodOurPasswordSpecified,
       "dodBlockNetBIOS": dodBlockNetBIOS,
       "dodMtu": dodMtu,
       "dodIpSlaveMode": dodIpSlaveMode,
       "dodReacquireIpAddr": dodReacquireIpAddr,
       "dodIpxOptRIPSAP": dodIpxOptRIPSAP,
       "dodCallIDTable": dodCallIDTable,
       "dodCallIDEntry": dodCallIDEntry,
       "dodCallIDType": dodCallIDType,
       "dodCallIDPhones": dodCallIDPhones,
       "dodPhoneTable": dodPhoneTable,
       "dodPhoneEntry": dodPhoneEntry,
       "dodPhoneIndex": dodPhoneIndex,
       "dodPhoneSpeed": dodPhoneSpeed,
       "dodPhoneNumber": dodPhoneNumber,
       "dodRemoteMacTable": dodRemoteMacTable,
       "dodRemoteMacEntry": dodRemoteMacEntry,
       "dodRemoteMacIndex": dodRemoteMacIndex,
       "dodRemoteMacAddress": dodRemoteMacAddress,
       "dodRemoteMacOperation": dodRemoteMacOperation,
       "dodRemoteIPNetTable": dodRemoteIPNetTable,
       "dodRemoteIPNetEntry": dodRemoteIPNetEntry,
       "dodRemoteIPNetIndex": dodRemoteIPNetIndex,
       "dodRemoteIPNetAddress": dodRemoteIPNetAddress,
       "dodRemoteIPNetMask": dodRemoteIPNetMask,
       "dodRemoteIPNetHops": dodRemoteIPNetHops,
       "dodRemoteIPNetOperation": dodRemoteIPNetOperation,
       "dodRemoteIPNetGateway": dodRemoteIPNetGateway,
       "dodRemoteIPXNetTable": dodRemoteIPXNetTable,
       "dodRemoteIPXNetEntry": dodRemoteIPXNetEntry,
       "dodRemoteIPXNetIndex": dodRemoteIPXNetIndex,
       "dodRemoteIPXNetAddress": dodRemoteIPXNetAddress,
       "dodRemoteIPXNetMetric": dodRemoteIPXNetMetric,
       "dodRemoteIPXNetTicks": dodRemoteIPXNetTicks,
       "dodRemoteIPXNetOperation": dodRemoteIPXNetOperation,
       "dodRemoteIPXNetStrAddress": dodRemoteIPXNetStrAddress,
       "dodRemoteIPXSAPTable": dodRemoteIPXSAPTable,
       "dodRemoteIPXSAPEntry": dodRemoteIPXSAPEntry,
       "dodRemoteIPXSAPIndex": dodRemoteIPXSAPIndex,
       "dodRemoteIPXSAPName": dodRemoteIPXSAPName,
       "dodRemoteIPXSAPNetAddress": dodRemoteIPXSAPNetAddress,
       "dodRemoteIPXSAPNodeAddress": dodRemoteIPXSAPNodeAddress,
       "dodRemoteIPXSAPSocket": dodRemoteIPXSAPSocket,
       "dodRemoteIPXSAPType": dodRemoteIPXSAPType,
       "dodRemoteIPXSAPHops": dodRemoteIPXSAPHops,
       "dodRemoteIPXSAPOperation": dodRemoteIPXSAPOperation,
       "dodRemoteIPXSAPStrNetAddress": dodRemoteIPXSAPStrNetAddress,
       "dodRemoteIPXSAPStrSocket": dodRemoteIPXSAPStrSocket,
       "dodRemoteIPXSAPStrType": dodRemoteIPXSAPStrType,
       "dodIPFilterTable": dodIPFilterTable,
       "dodIPFilterEntry": dodIPFilterEntry,
       "dodIPFilterIndex": dodIPFilterIndex,
       "dodIPFilterDstNetAddr": dodIPFilterDstNetAddr,
       "dodIPFilterSrcNetAddr": dodIPFilterSrcNetAddr,
       "dodIPFilterAllow": dodIPFilterAllow,
       "dodIPXFilterTable": dodIPXFilterTable,
       "dodIPXFilterEntry": dodIPXFilterEntry,
       "dodIPXFilterIndex": dodIPXFilterIndex,
       "dodIPXFilterDstNetAddr": dodIPXFilterDstNetAddr,
       "dodIPXFilterDstNodeAddr": dodIPXFilterDstNodeAddr,
       "dodIPXFilterDstSocket": dodIPXFilterDstSocket,
       "dodIPXFilterSrcNetAddr": dodIPXFilterSrcNetAddr,
       "dodIPXFilterSrcNodeAddr": dodIPXFilterSrcNodeAddr,
       "dodIPXFilterSrcSocket": dodIPXFilterSrcSocket,
       "dodIPXFilterAllow": dodIPXFilterAllow,
       "dodOperation": dodOperation,
       "dodRemoteMacDefault": dodRemoteMacDefault,
       "dodCallerTable": dodCallerTable,
       "dodCallerEntry": dodCallerEntry,
       "dodCallerNumber": dodCallerNumber,
       "dodCallerOperation": dodCallerOperation,
       "dodIPTranslationServerTable": dodIPTranslationServerTable,
       "dodIPTranslationServerEntry": dodIPTranslationServerEntry,
       "dodIPTranslationServerIPAddress": dodIPTranslationServerIPAddress,
       "dodIPTranslationProtocol": dodIPTranslationProtocol,
       "dodIPFirstTranslationPort": dodIPFirstTranslationPort,
       "dodIPLastTranslationPort": dodIPLastTranslationPort,
       "dodIPFirstPrivatePort": dodIPFirstPrivatePort,
       "dodIPTranslationStatus": dodIPTranslationStatus,
       "dodNatHostMappingTable": dodNatHostMappingTable,
       "dodNatHostMappingEntry": dodNatHostMappingEntry,
       "dodFirstPrivateIPAddress": dodFirstPrivateIPAddress,
       "dodLastPrivateIPAddress": dodLastPrivateIPAddress,
       "dodFirstPublicIPAddress": dodFirstPublicIPAddress,
       "dodNatHostMappingStatus": dodNatHostMappingStatus,
       "fpether": fpether,
       "fpEtherTable": fpEtherTable,
       "fpEtherEntry": fpEtherEntry,
       "fpPortNum": fpPortNum,
       "fpBridgeState": fpBridgeState,
       "fpIpState": fpIpState,
       "fpIpxState": fpIpxState,
       "fpIpNetAddress": fpIpNetAddress,
       "fpIpNetMask": fpIpNetMask,
       "fpIpxNetAddress": fpIpxNetAddress,
       "fpIpxFrameType": fpIpxFrameType,
       "fpEtherIpOptRecvRIP": fpEtherIpOptRecvRIP,
       "fpEtherIpOptSendRIP": fpEtherIpOptSendRIP,
       "fpEtherIpOptRecvRIPDefault": fpEtherIpOptRecvRIPDefault,
       "fpEtherIpOptSendRIPDefault": fpEtherIpOptSendRIPDefault,
       "fpIpxStrNetAddress": fpIpxStrNetAddress,
       "fpIpDefaultGateway": fpIpDefaultGateway,
       "fpEtherIpOptRecvRIP1": fpEtherIpOptRecvRIP1,
       "fpEtherIpOptSendRIP1": fpEtherIpOptSendRIP1,
       "fpEtherIpOptRecvRIP2": fpEtherIpOptRecvRIP2,
       "fpEtherIpOptSendRIP2": fpEtherIpOptSendRIP2,
       "fpIpRIPMulticastAddress": fpIpRIPMulticastAddress,
       "fpNATState": fpNATState,
       "fpMtu": fpMtu,
       "fpEtherOperation": fpEtherOperation,
       "etherNatHostMappingTable": etherNatHostMappingTable,
       "etherNatHostMappingEntry": etherNatHostMappingEntry,
       "etherFirstPrivateIPAddress": etherFirstPrivateIPAddress,
       "etherLastPrivateIPAddress": etherLastPrivateIPAddress,
       "etherFirstPublicIPAddress": etherFirstPublicIPAddress,
       "etherNatHostMappingStatus": etherNatHostMappingStatus,
       "etherIPTranslationServerTable": etherIPTranslationServerTable,
       "etherIPTranslationServerEntry": etherIPTranslationServerEntry,
       "etherIPTranslationServerIPAddress": etherIPTranslationServerIPAddress,
       "etherIPTranslationProtocol": etherIPTranslationProtocol,
       "etherIPFirstTranslationPort": etherIPFirstTranslationPort,
       "etherIPLastTranslationPort": etherIPLastTranslationPort,
       "etherIPFirstPrivatePort": etherIPFirstPrivatePort,
       "etherIPTranslationStatus": etherIPTranslationStatus,
       "fpisdn": fpisdn,
       "fpIsdnCh1Spid": fpIsdnCh1Spid,
       "fpIsdnCh2Spid": fpIsdnCh2Spid,
       "fpIsdnCh1DirectoryNum": fpIsdnCh1DirectoryNum,
       "fpIsdnCh2DirectoryNum": fpIsdnCh2DirectoryNum,
       "fpIsdnSwitchType": fpIsdnSwitchType,
       "fpIsdnOperation": fpIsdnOperation,
       "fpIsdnCh1Status": fpIsdnCh1Status,
       "fpIsdnCh2Status": fpIsdnCh2Status,
       "fpIsdnCh1ClearCode": fpIsdnCh1ClearCode,
       "fpIsdnCh2ClearCode": fpIsdnCh2ClearCode,
       "fpIsdnCh1ClearReason": fpIsdnCh1ClearReason,
       "fpIsdnCh2ClearReason": fpIsdnCh2ClearReason,
       "fpIsdnSpeed": fpIsdnSpeed,
       "fpIsdnDataCallsIn": fpIsdnDataCallsIn,
       "fpIsdnDataCallsOut": fpIsdnDataCallsOut,
       "fpIsdnLineStatus": fpIsdnLineStatus,
       "fpIsdnStatus": fpIsdnStatus,
       "fpIsdnAutoSpidCounter": fpIsdnAutoSpidCounter,
       "fpIsdnSwitchTable": fpIsdnSwitchTable,
       "fpIsdnSwitchEntry": fpIsdnSwitchEntry,
       "fpIsdnSwitchTypeIndex": fpIsdnSwitchTypeIndex,
       "fpsys": fpsys,
       "fpSysName": fpSysName,
       "fpSysMessage": fpSysMessage,
       "fpSysPassword": fpSysPassword,
       "fpSysAuthen": fpSysAuthen,
       "fpSysOperation": fpSysOperation,
       "fpSysSoftwareVer": fpSysSoftwareVer,
       "fpSysHardwareVer": fpSysHardwareVer,
       "fpLoginPassword": fpLoginPassword,
       "fpWriteTimeout": fpWriteTimeout,
       "fpWriteTimer": fpWriteTimer,
       "fpCommunityName": fpCommunityName,
       "fpInternetFireWall": fpInternetFireWall,
       "fpSysLogout": fpSysLogout,
       "fpIpxSupported": fpIpxSupported,
       "fpSysCallerIdTable": fpSysCallerIdTable,
       "fpSysCallerIdEntry": fpSysCallerIdEntry,
       "fpCallerIdEnabled": fpCallerIdEnabled,
       "fpMIBCompatibility": fpMIBCompatibility,
       "fpPOTSInstalled": fpPOTSInstalled,
       "fpSysLastLogEvent": fpSysLastLogEvent,
       "fpSysSingleUser": fpSysSingleUser,
       "fpSysYear": fpSysYear,
       "fpSysMonth": fpSysMonth,
       "fpSysDay": fpSysDay,
       "fpSysHour": fpSysHour,
       "fpSysMinute": fpSysMinute,
       "fpSysSecond": fpSysSecond,
       "fpSysDefaultSingleUser": fpSysDefaultSingleUser,
       "fpSysBootpRelay": fpSysBootpRelay,
       "fpSysKernelRevision": fpSysKernelRevision,
       "fpSysTelnetPort": fpSysTelnetPort,
       "fpSysSNMPPort": fpSysSNMPPort,
       "fpWAN2WANForwarding": fpWAN2WANForwarding,
       "fpUdpRelayTable": fpUdpRelayTable,
       "fpUdpRelayEntry": fpUdpRelayEntry,
       "fpUdpRelayFirstPort": fpUdpRelayFirstPort,
       "fpUdpRelayLastPort": fpUdpRelayLastPort,
       "fpUdpRelayIPAddress": fpUdpRelayIPAddress,
       "fpUdpRelayStatus": fpUdpRelayStatus,
       "fpOneWANConnection": fpOneWANConnection,
       "fpSysHTTPPort": fpSysHTTPPort,
       "fpDirectedBroadcasts": fpDirectedBroadcasts,
       "fpBlockNetBIOSDefault": fpBlockNetBIOSDefault,
       "fpSysFlashAvailable": fpSysFlashAvailable,
       "fpVoiceTable": fpVoiceTable,
       "fpVoiceEntry": fpVoiceEntry,
       "fpVoiceIndex": fpVoiceIndex,
       "fpVoicePort": fpVoicePort,
       "fpEchoTable": fpEchoTable,
       "fpEchoEntry": fpEchoEntry,
       "fpEchoIndex": fpEchoIndex,
       "fpEchoPort": fpEchoPort,
       "fpOptionTable": fpOptionTable,
       "fpOptionEntry": fpOptionEntry,
       "fpOptionIndex": fpOptionIndex,
       "fpOptionString": fpOptionString,
       "fpOptionAvailable": fpOptionAvailable,
       "fplogin": fplogin,
       "fpLoginTable": fpLoginTable,
       "fpLoginEntry": fpLoginEntry,
       "fpLoginAction": fpLoginAction,
       "fpWan": fpWan,
       "fpWanTable": fpWanTable,
       "fpWanEntry": fpWanEntry,
       "fpWanIndex": fpWanIndex,
       "fpWanInstantOutUtil": fpWanInstantOutUtil,
       "fpWanInstantInUtil": fpWanInstantInUtil,
       "fpWanAvgOutUtil": fpWanAvgOutUtil,
       "fpWanAvgInUtil": fpWanAvgInUtil,
       "fpWanRemoteName": fpWanRemoteName,
       "fpWanRemoteTime": fpWanRemoteTime,
       "fpWanIfIndex": fpWanIfIndex,
       "fpWanOutSpeed": fpWanOutSpeed,
       "fpWanInSpeed": fpWanInSpeed,
       "fppots": fppots,
       "potsOperation": potsOperation,
       "potsTable": potsTable,
       "potsEntry": potsEntry,
       "potsIndex": potsIndex,
       "potsEnabled": potsEnabled,
       "potsOpMode": potsOpMode,
       "potsPreemptMode": potsPreemptMode,
       "potsAutoMode": potsAutoMode,
       "potsPhoneCnt": potsPhoneCnt,
       "potsLocalNumber": potsLocalNumber,
       "potsRemoteNumber": potsRemoteNumber,
       "potsState": potsState,
       "potsIsdnChannel": potsIsdnChannel,
       "potsWanIndex": potsWanIndex,
       "potsPhoneTable": potsPhoneTable,
       "potsPhoneEntry": potsPhoneEntry,
       "potsPhoneNumber": potsPhoneNumber,
       "potsPhoneOperation": potsPhoneOperation,
       "fpdownload": fpdownload,
       "fpDLForceOnBoot": fpDLForceOnBoot,
       "fpDLCommitRAMToFlash": fpDLCommitRAMToFlash,
       "fpDLInitiateColdBoot": fpDLInitiateColdBoot,
       "fpDLTFTPRequestHost": fpDLTFTPRequestHost,
       "fpDLTFTPRequest": fpDLTFTPRequest,
       "fpDLLastImageFilename": fpDLLastImageFilename,
       "fpDLLastServerIPAddress": fpDLLastServerIPAddress,
       "fpDLFlashSize": fpDLFlashSize,
       "fpDLFlashCount": fpDLFlashCount,
       "fpDLFirmwareBase": fpDLFirmwareBase,
       "fpDLFirmwareTop": fpDLFirmwareTop,
       "fpDLFirmwareStart": fpDLFirmwareStart,
       "fpDLBootRev": fpDLBootRev,
       "fpDLForceBootp": fpDLForceBootp,
       "fpDLServerName": fpDLServerName,
       "fpDLOnLineDownLoad": fpDLOnLineDownLoad,
       "fpDLOperStatus": fpDLOperStatus,
       "fpDLNetAddress": fpDLNetAddress,
       "fpDLFileName": fpDLFileName,
       "fpDLErrorString": fpDLErrorString,
       "fpDLTftpServerGatewayIPAddress": fpDLTftpServerGatewayIPAddress,
       "fpDLBlockCount": fpDLBlockCount,
       "fpDLBootPartitionStatus": fpDLBootPartitionStatus,
       "fpDLLocalFileName": fpDLLocalFileName,
       "fpDLBootVersion": fpDLBootVersion,
       "fpDLBootReason": fpDLBootReason,
       "fpiptranslate": fpiptranslate,
       "sysIPTranslationServerTable": sysIPTranslationServerTable,
       "sysIPTranslationServerEntry": sysIPTranslationServerEntry,
       "sysIPTranslationServerIPAddress": sysIPTranslationServerIPAddress,
       "sysIPTranslationProtocol": sysIPTranslationProtocol,
       "sysIPFirstTranslationPort": sysIPFirstTranslationPort,
       "sysIPLastTranslationPort": sysIPLastTranslationPort,
       "sysIPFirstPrivatePort": sysIPFirstPrivatePort,
       "sysIPTranslationStatus": sysIPTranslationStatus,
       "sysNatHostMappingTable": sysNatHostMappingTable,
       "sysNatHostMappingEntry": sysNatHostMappingEntry,
       "sysFirstPrivateIPAddress": sysFirstPrivateIPAddress,
       "sysLastPrivateIPAddress": sysLastPrivateIPAddress,
       "sysFirstPublicIPAddress": sysFirstPublicIPAddress,
       "sysNatHostMappingStatus": sysNatHostMappingStatus,
       "fpdhcp": fpdhcp,
       "dhcpOperation": dhcpOperation,
       "dhcpGlobalTftpServer": dhcpGlobalTftpServer,
       "dhcpGlobalTftpFile": dhcpGlobalTftpFile,
       "dhcpGlobalLeaseTime": dhcpGlobalLeaseTime,
       "dhcpCodeTable": dhcpCodeTable,
       "dhcpCodeEntry": dhcpCodeEntry,
       "dhcpOptionCode": dhcpOptionCode,
       "dhcpMinCount": dhcpMinCount,
       "dhcpMaxCount": dhcpMaxCount,
       "dhcpOptionType": dhcpOptionType,
       "dhcpOptionCodeStatus": dhcpOptionCodeStatus,
       "dhcpGlobalValueTable": dhcpGlobalValueTable,
       "dhcpGlobalValueEntry": dhcpGlobalValueEntry,
       "dhcpGlobalValueCode": dhcpGlobalValueCode,
       "dhcpGlobalValueType": dhcpGlobalValueType,
       "dhcpGlobalValue": dhcpGlobalValue,
       "dhcpGlobalValueStatus": dhcpGlobalValueStatus,
       "dhcpSubnetTable": dhcpSubnetTable,
       "dhcpSubnetEntry": dhcpSubnetEntry,
       "dhcpSubnetAddress": dhcpSubnetAddress,
       "dhcpSubnetMask": dhcpSubnetMask,
       "dhcpSubnetFirstIpAddress": dhcpSubnetFirstIpAddress,
       "dhcpSubnetLastIpAddress": dhcpSubnetLastIpAddress,
       "dhcpSubnetTftpServer": dhcpSubnetTftpServer,
       "dhcpSubnetTftpFile": dhcpSubnetTftpFile,
       "dhcpSubnetBootp": dhcpSubnetBootp,
       "dhcpSubnetLeaseTime": dhcpSubnetLeaseTime,
       "dhcpSubnetStatus": dhcpSubnetStatus,
       "dhcpSubnetConflictActions": dhcpSubnetConflictActions,
       "dhcpSubnetValueTable": dhcpSubnetValueTable,
       "dhcpSubnetValueEntry": dhcpSubnetValueEntry,
       "dhcpSubnetValueCode": dhcpSubnetValueCode,
       "dhcpSubnetValueType": dhcpSubnetValueType,
       "dhcpSubnetValue": dhcpSubnetValue,
       "dhcpSubnetValueStatus": dhcpSubnetValueStatus,
       "dhcpClientTable": dhcpClientTable,
       "dhcpClientEntry": dhcpClientEntry,
       "dhcpClientAddress": dhcpClientAddress,
       "dhcpClientTftpServer": dhcpClientTftpServer,
       "dhcpClientTftpFile": dhcpClientTftpFile,
       "dhcpClientBootp": dhcpClientBootp,
       "dhcpClientLeaseTime": dhcpClientLeaseTime,
       "dhcpClientExpireTimeYear": dhcpClientExpireTimeYear,
       "dhcpClientExpireTimeMonth": dhcpClientExpireTimeMonth,
       "dhcpClientExpireTimeDay": dhcpClientExpireTimeDay,
       "dhcpClientExpireTimeHour": dhcpClientExpireTimeHour,
       "dhcpClientExpireTimeMinute": dhcpClientExpireTimeMinute,
       "dhcpClientExpireTimeSecond": dhcpClientExpireTimeSecond,
       "dhcpClientStatus": dhcpClientStatus,
       "dhcpClientValueTable": dhcpClientValueTable,
       "dhcpClientValueEntry": dhcpClientValueEntry,
       "dhcpClientValueCode": dhcpClientValueCode,
       "dhcpClientValueType": dhcpClientValueType,
       "dhcpClientValue": dhcpClientValue,
       "dhcpClientValueStatus": dhcpClientValueStatus,
       "fpdir": fpdir,
       "fpDirTable": fpDirTable,
       "fpDirEntry": fpDirEntry,
       "fpDirIndex": fpDirIndex,
       "fpDirName": fpDirName,
       "fpDirSize": fpDirSize,
       "fpatm": fpatm,
       "atmOperation": atmOperation,
       "fpfr": fpfr,
       "frOperation": frOperation}
)
