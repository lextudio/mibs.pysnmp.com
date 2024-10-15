# SNMP MIB module (EICON-DIALER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EICON-DIALER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:43 2024
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



class PortRef(Integer32):
    """Custom type PortRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )





class ActionState(Integer32):
    """Custom type ActionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("done", 1),
          ("failed", 2),
          ("in-progress", 3))
    )





class DataEncoding(Integer32):
    """Custom type DataEncoding based on Integer32"""
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
        *(("fm0", 3),
          ("fm1", 4),
          ("nrz", 1),
          ("nrzi", 2))
    )





class ClockType(Integer32):
    """Custom type ClockType based on Integer32"""
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
        *(("ext-dpll", 3),
          ("external", 1),
          ("int-dpll", 4),
          ("internal", 2))
    )





class OnOff(Integer32):
    """Custom type OnOff based on Integer32"""
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





class FalseTrue(Integer32):
    """Custom type FalseTrue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )





class DisEnable(Integer32):
    """Custom type DisEnable based on Integer32"""
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





class PrimBitRate(Integer32):
    """Custom type PrimBitRate based on Integer32"""
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
        *(("not-supported", 8),
          ("speed1200", 1),
          ("speed12000", 6),
          ("speed14400", 7),
          ("speed2400", 2),
          ("speed4800", 3),
          ("speed7200", 4),
          ("speed9600", 5))
    )





class PrimCfg(Integer32):
    """Custom type PrimCfg based on Integer32"""
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
        *(("not-supported", 5),
          ("v22bis", 1),
          ("v32", 2),
          ("v32bis", 4),
          ("v32tcm", 3))
    )





class IsdnSpidStatus(Integer32):
    """Custom type IsdnSpidStatus based on Integer32"""
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
        *(("blocked", 3),
          ("illegal", 4),
          ("init", 2),
          ("uninit", 1))
    )





class IsdnDnType(Integer32):
    """Custom type IsdnDnType based on Integer32"""
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
        *(("abbreviated", 6),
          ("illegal", 7),
          ("international", 2),
          ("national", 3),
          ("net-specific", 4),
          ("subscriber", 5),
          ("unknown", 1))
    )





class IsdnDnPlan(Integer32):
    """Custom type IsdnDnPlan based on Integer32"""
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
        *(("data-numbering", 3),
          ("illegal", 7),
          ("isdn-numbering", 2),
          ("nat-numbering", 6),
          ("private-net", 4),
          ("telex-numbering", 5),
          ("unknown", 1))
    )





class IsdnSubType(Integer32):
    """Custom type IsdnSubType based on Integer32"""
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
        *(("illegal", 4),
          ("nsap", 1),
          ("osi", 3),
          ("user-specified", 2))
    )





class IsdnTnsNetId(Integer32):
    """Custom type IsdnTnsNetId based on Integer32"""
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
        *(("illegal", 4),
          ("international", 3),
          ("national", 2),
          ("user-specified", 1))
    )





class IsdnTnsIdPlan(Integer32):
    """Custom type IsdnTnsIdPlan based on Integer32"""
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
        *(("data", 3),
          ("illegal", 4),
          ("interlata", 2),
          ("unknown", 1))
    )





class IsdnCallType(Integer32):
    """Custom type IsdnCallType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("btx", 7),
          ("circuit-spv", 4),
          ("circuit-switched", 1),
          ("fax-3", 5),
          ("fax-4", 6),
          ("illegal", 10),
          ("nailed-packet", 3),
          ("packet-switched", 2),
          ("teletex", 8),
          ("videotex", 9))
    )





class IsdnCallSpeed(Integer32):
    """Custom type IsdnCallSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed-56k", 1),
          ("speed-64k", 2),
          ("speed-illegal", 3))
    )





class IsdnBChannels(Integer32):
    """Custom type IsdnBChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b1-channel", 1),
          ("b2-channel", 2),
          ("illegal", 3))
    )





class IsdnAnsEnable(Integer32):
    """Custom type IsdnAnsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("enabled-illegal", 3))
    )





class IsdnScrStatus(Integer32):
    """Custom type IsdnScrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("illegal", 3))
    )





class IsdnCallOpt(Integer32):
    """Custom type IsdnCallOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("call-opt", 3),
          ("opt", 1),
          ("option", 2))
    )





class IsdnStoDefined(Integer32):
    """Custom type IsdnStoDefined based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("stored", 1)
    )





class IsdnTeiStatus(Integer32):
    """Custom type IsdnTeiStatus based on Integer32"""
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
        *(("assigned", 3),
          ("illegal", 4),
          ("outstanding", 2),
          ("unassigned", 1))
    )





class IsdnL2State(Integer32):
    """Custom type IsdnL2State based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("assign-awaiting-tei", 3),
          ("awaiting-established", 6),
          ("awaiting-release", 7),
          ("establish-awaiting-tei", 4),
          ("illegal", 10),
          ("mutiple-frame-established", 8),
          ("null-state", 1),
          ("tei-assigned", 5),
          ("tei-unassigned", 2),
          ("timer-recovery", 9))
    )





class IsdnL3State(Integer32):
    """Custom type IsdnL3State based on Integer32"""
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
              31,
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("asai-tr1-state", 29),
          ("broadcast-state", 36),
          ("call-active", 11),
          ("call-delivered", 5),
          ("call-init", 2),
          ("call-passive", 15),
          ("call-present", 7),
          ("call-received", 8),
          ("cancel-request", 22),
          ("connect-request", 9),
          ("disconnect-ind", 13),
          ("disconnect-request", 12),
          ("establish-wait", 28),
          ("idle-state", 27),
          ("illegal", 37),
          ("in-call-proc", 10),
          ("null-state", 1),
          ("out-call-proc", 4),
          ("overlap-receive", 26),
          ("overlap-sending", 3),
          ("register-request", 21),
          ("release-request", 20),
          ("resume-request", 18),
          ("suspend-request", 16),
          ("u10-awaiting-disc", 34),
          ("u10-call-on-hold", 35),
          ("u10-conference-request", 32),
          ("u10-hold-request", 30),
          ("u10-reconnect-request", 33),
          ("u10-transfer-request", 31),
          ("undefined-state-13", 14),
          ("undefined-state-16", 17),
          ("undefined-state-18", 19),
          ("undefined-state-22", 23),
          ("undefined-state-23", 24),
          ("undefined-state-24", 25),
          ("undefined-state-5", 6))
    )





class IsdnP3State(Integer32):
    """Custom type IsdnP3State based on Integer32"""
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
        *(("activated", 6),
          ("closed", 1),
          ("closing", 8),
          ("deactivated", 7),
          ("illegal", 9),
          ("opened", 3),
          ("opening", 2),
          ("sw-activation", 5),
          ("tei-establishment", 4))
    )





class IsdnActState(Integer32):
    """Custom type IsdnActState based on Integer32"""
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
        *(("activ-failed", 5),
          ("activating", 2),
          ("active", 3),
          ("call-failed", 4),
          ("deactivated", 1),
          ("illegal", 6))
    )





class IsdnNI1BCcState(Integer32):
    """Custom type IsdnNI1BCcState based on Integer32"""
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
        *(("call-queued", 11),
          ("connected", 4),
          ("dialing", 5),
          ("idle", 2),
          ("illegal", 12),
          ("lockout", 6),
          ("null-state", 1),
          ("offhook-releasing", 7),
          ("onhook-releasing", 8),
          ("originate", 9),
          ("ringing", 3),
          ("routing", 10))
    )





class IsdnTR6BCcState(Integer32):
    """Custom type IsdnTR6BCcState based on Integer32"""
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
        *(("call-queued", 11),
          ("connected", 5),
          ("connecting", 4),
          ("idle", 2),
          ("illegal", 12),
          ("lockout", 6),
          ("null-state", 1),
          ("offhook-releasing", 7),
          ("onhook-releasing", 8),
          ("originate", 9),
          ("ringing", 3),
          ("routing", 10))
    )





class IsdnVN3BCcState(Integer32):
    """Custom type IsdnVN3BCcState based on Integer32"""
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
        *(("call-queued", 11),
          ("connected", 5),
          ("connecting", 4),
          ("idle", 2),
          ("illegal", 12),
          ("lockout", 6),
          ("null-state", 1),
          ("offhook-releasing", 7),
          ("onhook-releasing", 8),
          ("originate", 9),
          ("ringing", 3),
          ("routing", 10))
    )





class IsdnNET3BCcState(Integer32):
    """Custom type IsdnNET3BCcState based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("bell-releasing", 12),
          ("call-queued", 11),
          ("connected", 5),
          ("connecting", 4),
          ("idle", 2),
          ("illegal", 13),
          ("lockout", 6),
          ("null-state", 1),
          ("offhook-releasing", 7),
          ("onhook-releasing", 8),
          ("originate", 9),
          ("ringing", 3),
          ("routingout", 10))
    )





class IsdnTPHBCcState(Integer32):
    """Custom type IsdnTPHBCcState based on Integer32"""
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
        *(("call-queued", 11),
          ("connected", 4),
          ("dialing", 5),
          ("idle", 2),
          ("illegal", 12),
          ("lockout", 6),
          ("null-state", 1),
          ("offhook-releasing", 7),
          ("onhook-releasing", 8),
          ("originate", 9),
          ("ringing", 3),
          ("routing", 10))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Eicon_ObjectIdentity = ObjectIdentity
eicon = _Eicon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434)
)
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2)
)
_Mibv2_ObjectIdentity = ObjectIdentity
mibv2 = _Mibv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2)
)
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4)
)
_Dialer_ObjectIdentity = ObjectIdentity
dialer = _Dialer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16)
)
_DialerInfoTable_Object = MibTable
dialerInfoTable = _DialerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 1)
)
if mibBuilder.loadTexts:
    dialerInfoTable.setStatus("mandatory")
_DialerInfoEntry_Object = MibTableRow
dialerInfoEntry = _DialerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 1, 1)
)
dialerInfoEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerInfoPortRef"),
)
if mibBuilder.loadTexts:
    dialerInfoEntry.setStatus("mandatory")
_DialerInfoPortRef_Type = PortRef
_DialerInfoPortRef_Object = MibTableColumn
dialerInfoPortRef = _DialerInfoPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 1, 1, 1),
    _DialerInfoPortRef_Type()
)
dialerInfoPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerInfoPortRef.setStatus("mandatory")


class _DialerInfoType_Type(Integer32):
    """Custom type dialerInfoType based on Integer32"""
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
        *(("at-cmd", 4),
          ("direct", 1),
          ("isdn-stat", 5),
          ("none", 7),
          ("other", 8),
          ("v22bis", 3),
          ("v25bis", 2),
          ("v32bis", 6))
    )


_DialerInfoType_Type.__name__ = "Integer32"
_DialerInfoType_Object = MibTableColumn
dialerInfoType = _DialerInfoType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 1, 1, 2),
    _DialerInfoType_Type()
)
dialerInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerInfoType.setStatus("mandatory")
_DialerInfoTimeStart_Type = TimeTicks
_DialerInfoTimeStart_Object = MibTableColumn
dialerInfoTimeStart = _DialerInfoTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 1, 1, 3),
    _DialerInfoTimeStart_Type()
)
dialerInfoTimeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerInfoTimeStart.setStatus("mandatory")
_DialerInfoTimeConnect_Type = TimeTicks
_DialerInfoTimeConnect_Object = MibTableColumn
dialerInfoTimeConnect = _DialerInfoTimeConnect_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 1, 1, 4),
    _DialerInfoTimeConnect_Type()
)
dialerInfoTimeConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerInfoTimeConnect.setStatus("mandatory")


class _DialerInfoLineSpeed_Type(Integer32):
    """Custom type dialerInfoLineSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_DialerInfoLineSpeed_Type.__name__ = "Integer32"
_DialerInfoLineSpeed_Object = MibTableColumn
dialerInfoLineSpeed = _DialerInfoLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 1, 1, 5),
    _DialerInfoLineSpeed_Type()
)
dialerInfoLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerInfoLineSpeed.setStatus("mandatory")
_DialerInfoDataEncoding_Type = DataEncoding
_DialerInfoDataEncoding_Object = MibTableColumn
dialerInfoDataEncoding = _DialerInfoDataEncoding_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 1, 1, 6),
    _DialerInfoDataEncoding_Type()
)
dialerInfoDataEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerInfoDataEncoding.setStatus("mandatory")
_DialerInfoClockType_Type = ClockType
_DialerInfoClockType_Object = MibTableColumn
dialerInfoClockType = _DialerInfoClockType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 1, 1, 7),
    _DialerInfoClockType_Type()
)
dialerInfoClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerInfoClockType.setStatus("mandatory")
_DialerDirectInfoTable_Object = MibTable
dialerDirectInfoTable = _DialerDirectInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 2)
)
if mibBuilder.loadTexts:
    dialerDirectInfoTable.setStatus("mandatory")
_DialerDirectInfoEntry_Object = MibTableRow
dialerDirectInfoEntry = _DialerDirectInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 2, 1)
)
dialerDirectInfoEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerDirectPortRef"),
)
if mibBuilder.loadTexts:
    dialerDirectInfoEntry.setStatus("mandatory")
_DialerDirectPortRef_Type = PortRef
_DialerDirectPortRef_Object = MibTableColumn
dialerDirectPortRef = _DialerDirectPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 2, 1, 1),
    _DialerDirectPortRef_Type()
)
dialerDirectPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerDirectPortRef.setStatus("mandatory")


class _DialerDirectIfType_Type(Integer32):
    """Custom type dialerDirectIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 1),
          ("v35", 2),
          ("x21", 3))
    )


_DialerDirectIfType_Type.__name__ = "Integer32"
_DialerDirectIfType_Object = MibTableColumn
dialerDirectIfType = _DialerDirectIfType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 2, 1, 2),
    _DialerDirectIfType_Type()
)
dialerDirectIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerDirectIfType.setStatus("mandatory")


class _DialerDirectMode_Type(Integer32):
    """Custom type dialerDirectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dial", 2),
          ("leased", 1))
    )


_DialerDirectMode_Type.__name__ = "Integer32"
_DialerDirectMode_Object = MibTableColumn
dialerDirectMode = _DialerDirectMode_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 2, 1, 3),
    _DialerDirectMode_Type()
)
dialerDirectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerDirectMode.setStatus("mandatory")
_DialerDirectConnDelay_Type = Integer32
_DialerDirectConnDelay_Object = MibTableColumn
dialerDirectConnDelay = _DialerDirectConnDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 2, 1, 4),
    _DialerDirectConnDelay_Type()
)
dialerDirectConnDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerDirectConnDelay.setStatus("mandatory")
_DialerDirectRtsDelay_Type = Integer32
_DialerDirectRtsDelay_Object = MibTableColumn
dialerDirectRtsDelay = _DialerDirectRtsDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 2, 1, 5),
    _DialerDirectRtsDelay_Type()
)
dialerDirectRtsDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerDirectRtsDelay.setStatus("mandatory")


class _DialerDirectState_Type(Integer32):
    """Custom type dialerDirectState based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("answer-wait", 8),
          ("answering", 3),
          ("closed", 1),
          ("closing", 6),
          ("connect-delay", 11),
          ("connect-req", 16),
          ("connected", 12),
          ("connecting", 10),
          ("delaying", 4),
          ("disconnecting", 13),
          ("incomming-call", 17),
          ("local-disc", 15),
          ("opened", 5),
          ("opening", 2),
          ("originating", 9),
          ("outgoing-call", 18),
          ("outgoing-delay", 19),
          ("remote-disc", 14),
          ("ringing", 7))
    )


_DialerDirectState_Type.__name__ = "Integer32"
_DialerDirectState_Object = MibTableColumn
dialerDirectState = _DialerDirectState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 2, 1, 6),
    _DialerDirectState_Type()
)
dialerDirectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerDirectState.setStatus("mandatory")
_DialerDirectRs232InfoTable_Object = MibTable
dialerDirectRs232InfoTable = _DialerDirectRs232InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 3)
)
if mibBuilder.loadTexts:
    dialerDirectRs232InfoTable.setStatus("mandatory")
_DialerDirectRs232InfoEntry_Object = MibTableRow
dialerDirectRs232InfoEntry = _DialerDirectRs232InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 3, 1)
)
dialerDirectRs232InfoEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerDirectRs232PortRef"),
)
if mibBuilder.loadTexts:
    dialerDirectRs232InfoEntry.setStatus("mandatory")
_DialerDirectRs232PortRef_Type = PortRef
_DialerDirectRs232PortRef_Object = MibTableColumn
dialerDirectRs232PortRef = _DialerDirectRs232PortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 3, 1, 1),
    _DialerDirectRs232PortRef_Type()
)
dialerDirectRs232PortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerDirectRs232PortRef.setStatus("mandatory")
_DialerDirectRs232DbounceDelay_Type = Integer32
_DialerDirectRs232DbounceDelay_Object = MibTableColumn
dialerDirectRs232DbounceDelay = _DialerDirectRs232DbounceDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 3, 1, 2),
    _DialerDirectRs232DbounceDelay_Type()
)
dialerDirectRs232DbounceDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerDirectRs232DbounceDelay.setStatus("mandatory")
_DialerDirectRs232DtrSignal_Type = OnOff
_DialerDirectRs232DtrSignal_Object = MibTableColumn
dialerDirectRs232DtrSignal = _DialerDirectRs232DtrSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 3, 1, 3),
    _DialerDirectRs232DtrSignal_Type()
)
dialerDirectRs232DtrSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerDirectRs232DtrSignal.setStatus("mandatory")
_DialerDirectRs232DsrSignal_Type = OnOff
_DialerDirectRs232DsrSignal_Object = MibTableColumn
dialerDirectRs232DsrSignal = _DialerDirectRs232DsrSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 3, 1, 4),
    _DialerDirectRs232DsrSignal_Type()
)
dialerDirectRs232DsrSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerDirectRs232DsrSignal.setStatus("mandatory")
_DialerDirectRs232RiSignal_Type = OnOff
_DialerDirectRs232RiSignal_Object = MibTableColumn
dialerDirectRs232RiSignal = _DialerDirectRs232RiSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 3, 1, 5),
    _DialerDirectRs232RiSignal_Type()
)
dialerDirectRs232RiSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerDirectRs232RiSignal.setStatus("mandatory")
_DialerDirectX21InfoTable_Object = MibTable
dialerDirectX21InfoTable = _DialerDirectX21InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 4)
)
if mibBuilder.loadTexts:
    dialerDirectX21InfoTable.setStatus("mandatory")
_DialerDirectX21InfoEntry_Object = MibTableRow
dialerDirectX21InfoEntry = _DialerDirectX21InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 4, 1)
)
dialerDirectX21InfoEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerDirectX21PortRef"),
)
if mibBuilder.loadTexts:
    dialerDirectX21InfoEntry.setStatus("mandatory")
_DialerDirectX21PortRef_Type = PortRef
_DialerDirectX21PortRef_Object = MibTableColumn
dialerDirectX21PortRef = _DialerDirectX21PortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 4, 1, 1),
    _DialerDirectX21PortRef_Type()
)
dialerDirectX21PortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerDirectX21PortRef.setStatus("mandatory")
_DialerDirectX21CtrlSignal_Type = OnOff
_DialerDirectX21CtrlSignal_Object = MibTableColumn
dialerDirectX21CtrlSignal = _DialerDirectX21CtrlSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 4, 1, 2),
    _DialerDirectX21CtrlSignal_Type()
)
dialerDirectX21CtrlSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerDirectX21CtrlSignal.setStatus("mandatory")
_DialerDirectX21IndicSignal_Type = OnOff
_DialerDirectX21IndicSignal_Object = MibTableColumn
dialerDirectX21IndicSignal = _DialerDirectX21IndicSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 4, 1, 3),
    _DialerDirectX21IndicSignal_Type()
)
dialerDirectX21IndicSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerDirectX21IndicSignal.setStatus("mandatory")
_DialerV25bisInfoTable_Object = MibTable
dialerV25bisInfoTable = _DialerV25bisInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5)
)
if mibBuilder.loadTexts:
    dialerV25bisInfoTable.setStatus("mandatory")
_DialerV25bisInfoEntry_Object = MibTableRow
dialerV25bisInfoEntry = _DialerV25bisInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1)
)
dialerV25bisInfoEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerV25bisPortRef"),
)
if mibBuilder.loadTexts:
    dialerV25bisInfoEntry.setStatus("mandatory")
_DialerV25bisPortRef_Type = PortRef
_DialerV25bisPortRef_Object = MibTableColumn
dialerV25bisPortRef = _DialerV25bisPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 1),
    _DialerV25bisPortRef_Type()
)
dialerV25bisPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisPortRef.setStatus("mandatory")


class _DialerV25bisPrimaryNum_Type(DisplayString):
    """Custom type dialerV25bisPrimaryNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DialerV25bisPrimaryNum_Type.__name__ = "DisplayString"
_DialerV25bisPrimaryNum_Object = MibTableColumn
dialerV25bisPrimaryNum = _DialerV25bisPrimaryNum_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 2),
    _DialerV25bisPrimaryNum_Type()
)
dialerV25bisPrimaryNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerV25bisPrimaryNum.setStatus("mandatory")


class _DialerV25bisSecondaryNum_Type(DisplayString):
    """Custom type dialerV25bisSecondaryNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DialerV25bisSecondaryNum_Type.__name__ = "DisplayString"
_DialerV25bisSecondaryNum_Object = MibTableColumn
dialerV25bisSecondaryNum = _DialerV25bisSecondaryNum_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 3),
    _DialerV25bisSecondaryNum_Type()
)
dialerV25bisSecondaryNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerV25bisSecondaryNum.setStatus("mandatory")
_DialerV25bisAnsEnable_Type = FalseTrue
_DialerV25bisAnsEnable_Object = MibTableColumn
dialerV25bisAnsEnable = _DialerV25bisAnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 4),
    _DialerV25bisAnsEnable_Type()
)
dialerV25bisAnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerV25bisAnsEnable.setStatus("mandatory")
_DialerV25bisRetryAllowed_Type = FalseTrue
_DialerV25bisRetryAllowed_Object = MibTableColumn
dialerV25bisRetryAllowed = _DialerV25bisRetryAllowed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 5),
    _DialerV25bisRetryAllowed_Type()
)
dialerV25bisRetryAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisRetryAllowed.setStatus("mandatory")
_DialerV25bisMaxRetries_Type = Integer32
_DialerV25bisMaxRetries_Object = MibTableColumn
dialerV25bisMaxRetries = _DialerV25bisMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 6),
    _DialerV25bisMaxRetries_Type()
)
dialerV25bisMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisMaxRetries.setStatus("mandatory")
_DialerV25bisRetryDelay_Type = Integer32
_DialerV25bisRetryDelay_Object = MibTableColumn
dialerV25bisRetryDelay = _DialerV25bisRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 7),
    _DialerV25bisRetryDelay_Type()
)
dialerV25bisRetryDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisRetryDelay.setStatus("mandatory")
_DialerV25bisConnDelay_Type = Integer32
_DialerV25bisConnDelay_Object = MibTableColumn
dialerV25bisConnDelay = _DialerV25bisConnDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 8),
    _DialerV25bisConnDelay_Type()
)
dialerV25bisConnDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisConnDelay.setStatus("mandatory")
_DialerV25bisOnOffDelay_Type = Integer32
_DialerV25bisOnOffDelay_Object = MibTableColumn
dialerV25bisOnOffDelay = _DialerV25bisOnOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 9),
    _DialerV25bisOnOffDelay_Type()
)
dialerV25bisOnOffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisOnOffDelay.setStatus("mandatory")
_DialerV25bisLossDelay_Type = Integer32
_DialerV25bisLossDelay_Object = MibTableColumn
dialerV25bisLossDelay = _DialerV25bisLossDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 10),
    _DialerV25bisLossDelay_Type()
)
dialerV25bisLossDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisLossDelay.setStatus("mandatory")
_DialerV25bisMinDsrOnDelay_Type = Integer32
_DialerV25bisMinDsrOnDelay_Object = MibTableColumn
dialerV25bisMinDsrOnDelay = _DialerV25bisMinDsrOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 11),
    _DialerV25bisMinDsrOnDelay_Type()
)
dialerV25bisMinDsrOnDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisMinDsrOnDelay.setStatus("mandatory")
_DialerV25bisRiDtrDelay_Type = Integer32
_DialerV25bisRiDtrDelay_Object = MibTableColumn
dialerV25bisRiDtrDelay = _DialerV25bisRiDtrDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 12),
    _DialerV25bisRiDtrDelay_Type()
)
dialerV25bisRiDtrDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisRiDtrDelay.setStatus("mandatory")
_DialerV25bisHangupDelay_Type = Integer32
_DialerV25bisHangupDelay_Object = MibTableColumn
dialerV25bisHangupDelay = _DialerV25bisHangupDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 13),
    _DialerV25bisHangupDelay_Type()
)
dialerV25bisHangupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisHangupDelay.setStatus("mandatory")
_DialerV25bisDeltaRiDelay_Type = Integer32
_DialerV25bisDeltaRiDelay_Object = MibTableColumn
dialerV25bisDeltaRiDelay = _DialerV25bisDeltaRiDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 14),
    _DialerV25bisDeltaRiDelay_Type()
)
dialerV25bisDeltaRiDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisDeltaRiDelay.setStatus("mandatory")
_DialerV25bisCtsOnDelay_Type = Integer32
_DialerV25bisCtsOnDelay_Object = MibTableColumn
dialerV25bisCtsOnDelay = _DialerV25bisCtsOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 15),
    _DialerV25bisCtsOnDelay_Type()
)
dialerV25bisCtsOnDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisCtsOnDelay.setStatus("mandatory")
_DialerV25bisDtrSignal_Type = OnOff
_DialerV25bisDtrSignal_Object = MibTableColumn
dialerV25bisDtrSignal = _DialerV25bisDtrSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 16),
    _DialerV25bisDtrSignal_Type()
)
dialerV25bisDtrSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisDtrSignal.setStatus("mandatory")
_DialerV25bisDsrSignal_Type = OnOff
_DialerV25bisDsrSignal_Object = MibTableColumn
dialerV25bisDsrSignal = _DialerV25bisDsrSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 17),
    _DialerV25bisDsrSignal_Type()
)
dialerV25bisDsrSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisDsrSignal.setStatus("mandatory")
_DialerV25bisCtsSignal_Type = OnOff
_DialerV25bisCtsSignal_Object = MibTableColumn
dialerV25bisCtsSignal = _DialerV25bisCtsSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 18),
    _DialerV25bisCtsSignal_Type()
)
dialerV25bisCtsSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisCtsSignal.setStatus("mandatory")
_DialerV25bisRiSignal_Type = OnOff
_DialerV25bisRiSignal_Object = MibTableColumn
dialerV25bisRiSignal = _DialerV25bisRiSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 19),
    _DialerV25bisRiSignal_Type()
)
dialerV25bisRiSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisRiSignal.setStatus("mandatory")


class _DialerV25bisState_Type(Integer32):
    """Custom type dialerV25bisState based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("ans-accepting", 13),
          ("ans-cplt", 9),
          ("ans-start", 8),
          ("collision", 12),
          ("connect", 4),
          ("data-tran", 5),
          ("dialing", 3),
          ("hanging-up", 10),
          ("ignore-ring", 11),
          ("on-hook", 1),
          ("prog-not-rdy", 17),
          ("prog-rdy", 14),
          ("prog-ring", 16),
          ("program", 15),
          ("ready", 2),
          ("retrying", 6),
          ("ringing", 7))
    )


_DialerV25bisState_Type.__name__ = "Integer32"
_DialerV25bisState_Object = MibTableColumn
dialerV25bisState = _DialerV25bisState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 5, 1, 20),
    _DialerV25bisState_Type()
)
dialerV25bisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV25bisState.setStatus("mandatory")
_DialerAtCmdInfoTable_Object = MibTable
dialerAtCmdInfoTable = _DialerAtCmdInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6)
)
if mibBuilder.loadTexts:
    dialerAtCmdInfoTable.setStatus("mandatory")
_DialerAtCmdInfoEntry_Object = MibTableRow
dialerAtCmdInfoEntry = _DialerAtCmdInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1)
)
dialerAtCmdInfoEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerAtCmdPortRef"),
)
if mibBuilder.loadTexts:
    dialerAtCmdInfoEntry.setStatus("mandatory")
_DialerAtCmdPortRef_Type = PortRef
_DialerAtCmdPortRef_Object = MibTableColumn
dialerAtCmdPortRef = _DialerAtCmdPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 1),
    _DialerAtCmdPortRef_Type()
)
dialerAtCmdPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdPortRef.setStatus("mandatory")


class _DialerAtCmdPrimaryNum_Type(DisplayString):
    """Custom type dialerAtCmdPrimaryNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DialerAtCmdPrimaryNum_Type.__name__ = "DisplayString"
_DialerAtCmdPrimaryNum_Object = MibTableColumn
dialerAtCmdPrimaryNum = _DialerAtCmdPrimaryNum_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 2),
    _DialerAtCmdPrimaryNum_Type()
)
dialerAtCmdPrimaryNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerAtCmdPrimaryNum.setStatus("mandatory")


class _DialerAtCmdSecondaryNum_Type(DisplayString):
    """Custom type dialerAtCmdSecondaryNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DialerAtCmdSecondaryNum_Type.__name__ = "DisplayString"
_DialerAtCmdSecondaryNum_Object = MibTableColumn
dialerAtCmdSecondaryNum = _DialerAtCmdSecondaryNum_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 3),
    _DialerAtCmdSecondaryNum_Type()
)
dialerAtCmdSecondaryNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerAtCmdSecondaryNum.setStatus("mandatory")
_DialerAtCmdAnsEnable_Type = FalseTrue
_DialerAtCmdAnsEnable_Object = MibTableColumn
dialerAtCmdAnsEnable = _DialerAtCmdAnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 4),
    _DialerAtCmdAnsEnable_Type()
)
dialerAtCmdAnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerAtCmdAnsEnable.setStatus("mandatory")
_DialerAtCmdRetryAllowed_Type = FalseTrue
_DialerAtCmdRetryAllowed_Object = MibTableColumn
dialerAtCmdRetryAllowed = _DialerAtCmdRetryAllowed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 5),
    _DialerAtCmdRetryAllowed_Type()
)
dialerAtCmdRetryAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdRetryAllowed.setStatus("mandatory")
_DialerAtCmdMaxRetries_Type = Integer32
_DialerAtCmdMaxRetries_Object = MibTableColumn
dialerAtCmdMaxRetries = _DialerAtCmdMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 6),
    _DialerAtCmdMaxRetries_Type()
)
dialerAtCmdMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdMaxRetries.setStatus("mandatory")
_DialerAtCmdRetryDelay_Type = Integer32
_DialerAtCmdRetryDelay_Object = MibTableColumn
dialerAtCmdRetryDelay = _DialerAtCmdRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 7),
    _DialerAtCmdRetryDelay_Type()
)
dialerAtCmdRetryDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdRetryDelay.setStatus("mandatory")
_DialerAtCmdConnDelay_Type = Integer32
_DialerAtCmdConnDelay_Object = MibTableColumn
dialerAtCmdConnDelay = _DialerAtCmdConnDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 8),
    _DialerAtCmdConnDelay_Type()
)
dialerAtCmdConnDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdConnDelay.setStatus("mandatory")
_DialerAtCmdOnOffDelay_Type = Integer32
_DialerAtCmdOnOffDelay_Object = MibTableColumn
dialerAtCmdOnOffDelay = _DialerAtCmdOnOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 9),
    _DialerAtCmdOnOffDelay_Type()
)
dialerAtCmdOnOffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdOnOffDelay.setStatus("mandatory")
_DialerAtCmdLossDelay_Type = Integer32
_DialerAtCmdLossDelay_Object = MibTableColumn
dialerAtCmdLossDelay = _DialerAtCmdLossDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 10),
    _DialerAtCmdLossDelay_Type()
)
dialerAtCmdLossDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdLossDelay.setStatus("mandatory")
_DialerAtCmdMinDsrOnDelay_Type = Integer32
_DialerAtCmdMinDsrOnDelay_Object = MibTableColumn
dialerAtCmdMinDsrOnDelay = _DialerAtCmdMinDsrOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 11),
    _DialerAtCmdMinDsrOnDelay_Type()
)
dialerAtCmdMinDsrOnDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdMinDsrOnDelay.setStatus("mandatory")
_DialerAtCmdRiDtrDelay_Type = Integer32
_DialerAtCmdRiDtrDelay_Object = MibTableColumn
dialerAtCmdRiDtrDelay = _DialerAtCmdRiDtrDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 12),
    _DialerAtCmdRiDtrDelay_Type()
)
dialerAtCmdRiDtrDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdRiDtrDelay.setStatus("mandatory")
_DialerAtCmdHangupDelay_Type = Integer32
_DialerAtCmdHangupDelay_Object = MibTableColumn
dialerAtCmdHangupDelay = _DialerAtCmdHangupDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 13),
    _DialerAtCmdHangupDelay_Type()
)
dialerAtCmdHangupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdHangupDelay.setStatus("mandatory")
_DialerAtCmdDeltaRiDelay_Type = Integer32
_DialerAtCmdDeltaRiDelay_Object = MibTableColumn
dialerAtCmdDeltaRiDelay = _DialerAtCmdDeltaRiDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 14),
    _DialerAtCmdDeltaRiDelay_Type()
)
dialerAtCmdDeltaRiDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdDeltaRiDelay.setStatus("mandatory")


class _DialerAtCmdParity_Type(Integer32):
    """Custom type dialerAtCmdParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_DialerAtCmdParity_Type.__name__ = "Integer32"
_DialerAtCmdParity_Object = MibTableColumn
dialerAtCmdParity = _DialerAtCmdParity_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 15),
    _DialerAtCmdParity_Type()
)
dialerAtCmdParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdParity.setStatus("mandatory")


class _DialerAtCmdBitsPerByte_Type(Integer32):
    """Custom type dialerAtCmdBitsPerByte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data7", 1),
          ("data8", 2))
    )


_DialerAtCmdBitsPerByte_Type.__name__ = "Integer32"
_DialerAtCmdBitsPerByte_Object = MibTableColumn
dialerAtCmdBitsPerByte = _DialerAtCmdBitsPerByte_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 16),
    _DialerAtCmdBitsPerByte_Type()
)
dialerAtCmdBitsPerByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdBitsPerByte.setStatus("mandatory")
_DialerAtCmdModemSpeed_Type = Integer32
_DialerAtCmdModemSpeed_Object = MibTableColumn
dialerAtCmdModemSpeed = _DialerAtCmdModemSpeed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 17),
    _DialerAtCmdModemSpeed_Type()
)
dialerAtCmdModemSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdModemSpeed.setStatus("mandatory")
_DialerAtCmdDtrSignal_Type = OnOff
_DialerAtCmdDtrSignal_Object = MibTableColumn
dialerAtCmdDtrSignal = _DialerAtCmdDtrSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 18),
    _DialerAtCmdDtrSignal_Type()
)
dialerAtCmdDtrSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdDtrSignal.setStatus("mandatory")
_DialerAtCmdDsrSignal_Type = OnOff
_DialerAtCmdDsrSignal_Object = MibTableColumn
dialerAtCmdDsrSignal = _DialerAtCmdDsrSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 19),
    _DialerAtCmdDsrSignal_Type()
)
dialerAtCmdDsrSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdDsrSignal.setStatus("mandatory")
_DialerAtCmdRiSignal_Type = OnOff
_DialerAtCmdRiSignal_Object = MibTableColumn
dialerAtCmdRiSignal = _DialerAtCmdRiSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 20),
    _DialerAtCmdRiSignal_Type()
)
dialerAtCmdRiSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdRiSignal.setStatus("mandatory")


class _DialerAtCmdState_Type(Integer32):
    """Custom type dialerAtCmdState based on Integer32"""
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
        *(("answering", 3),
          ("dialing", 2),
          ("hanging-up", 7),
          ("off-hook", 6),
          ("on-hook", 1),
          ("retrying", 5),
          ("ringing", 4))
    )


_DialerAtCmdState_Type.__name__ = "Integer32"
_DialerAtCmdState_Object = MibTableColumn
dialerAtCmdState = _DialerAtCmdState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 6, 1, 21),
    _DialerAtCmdState_Type()
)
dialerAtCmdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerAtCmdState.setStatus("mandatory")
_DialerV22BisDnaInfoTable_Object = MibTable
dialerV22BisDnaInfoTable = _DialerV22BisDnaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7)
)
if mibBuilder.loadTexts:
    dialerV22BisDnaInfoTable.setStatus("mandatory")
_DialerV22BisDnaInfoEntry_Object = MibTableRow
dialerV22BisDnaInfoEntry = _DialerV22BisDnaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1)
)
dialerV22BisDnaInfoEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerV22BisDnaPortRef"),
)
if mibBuilder.loadTexts:
    dialerV22BisDnaInfoEntry.setStatus("mandatory")
_DialerV22BisDnaPortRef_Type = PortRef
_DialerV22BisDnaPortRef_Object = MibTableColumn
dialerV22BisDnaPortRef = _DialerV22BisDnaPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 1),
    _DialerV22BisDnaPortRef_Type()
)
dialerV22BisDnaPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaPortRef.setStatus("mandatory")


class _DialerV22BisDnaPrimaryNum_Type(DisplayString):
    """Custom type dialerV22BisDnaPrimaryNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DialerV22BisDnaPrimaryNum_Type.__name__ = "DisplayString"
_DialerV22BisDnaPrimaryNum_Object = MibTableColumn
dialerV22BisDnaPrimaryNum = _DialerV22BisDnaPrimaryNum_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 2),
    _DialerV22BisDnaPrimaryNum_Type()
)
dialerV22BisDnaPrimaryNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerV22BisDnaPrimaryNum.setStatus("mandatory")


class _DialerV22BisDnaSecondaryNum_Type(DisplayString):
    """Custom type dialerV22BisDnaSecondaryNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DialerV22BisDnaSecondaryNum_Type.__name__ = "DisplayString"
_DialerV22BisDnaSecondaryNum_Object = MibTableColumn
dialerV22BisDnaSecondaryNum = _DialerV22BisDnaSecondaryNum_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 3),
    _DialerV22BisDnaSecondaryNum_Type()
)
dialerV22BisDnaSecondaryNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerV22BisDnaSecondaryNum.setStatus("mandatory")
_DialerV22BisDnaAnsEnable_Type = FalseTrue
_DialerV22BisDnaAnsEnable_Object = MibTableColumn
dialerV22BisDnaAnsEnable = _DialerV22BisDnaAnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 4),
    _DialerV22BisDnaAnsEnable_Type()
)
dialerV22BisDnaAnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerV22BisDnaAnsEnable.setStatus("mandatory")
_DialerV22BisDnaRetryAllowed_Type = FalseTrue
_DialerV22BisDnaRetryAllowed_Object = MibTableColumn
dialerV22BisDnaRetryAllowed = _DialerV22BisDnaRetryAllowed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 5),
    _DialerV22BisDnaRetryAllowed_Type()
)
dialerV22BisDnaRetryAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaRetryAllowed.setStatus("mandatory")
_DialerV22BisDnaMaxRetries_Type = Integer32
_DialerV22BisDnaMaxRetries_Object = MibTableColumn
dialerV22BisDnaMaxRetries = _DialerV22BisDnaMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 6),
    _DialerV22BisDnaMaxRetries_Type()
)
dialerV22BisDnaMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaMaxRetries.setStatus("mandatory")
_DialerV22BisDnaCallProgress_Type = FalseTrue
_DialerV22BisDnaCallProgress_Object = MibTableColumn
dialerV22BisDnaCallProgress = _DialerV22BisDnaCallProgress_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 7),
    _DialerV22BisDnaCallProgress_Type()
)
dialerV22BisDnaCallProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaCallProgress.setStatus("mandatory")
_DialerV22BisDnaDecadic_Type = FalseTrue
_DialerV22BisDnaDecadic_Object = MibTableColumn
dialerV22BisDnaDecadic = _DialerV22BisDnaDecadic_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 8),
    _DialerV22BisDnaDecadic_Type()
)
dialerV22BisDnaDecadic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaDecadic.setStatus("mandatory")
_DialerV22BisDnaMakeBreakRatio_Type = Integer32
_DialerV22BisDnaMakeBreakRatio_Object = MibTableColumn
dialerV22BisDnaMakeBreakRatio = _DialerV22BisDnaMakeBreakRatio_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 9),
    _DialerV22BisDnaMakeBreakRatio_Type()
)
dialerV22BisDnaMakeBreakRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaMakeBreakRatio.setStatus("mandatory")
_DialerV22BisDnaRetryDelay_Type = Integer32
_DialerV22BisDnaRetryDelay_Object = MibTableColumn
dialerV22BisDnaRetryDelay = _DialerV22BisDnaRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 10),
    _DialerV22BisDnaRetryDelay_Type()
)
dialerV22BisDnaRetryDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaRetryDelay.setStatus("mandatory")
_DialerV22BisDnaMinDialDelay_Type = Integer32
_DialerV22BisDnaMinDialDelay_Object = MibTableColumn
dialerV22BisDnaMinDialDelay = _DialerV22BisDnaMinDialDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 11),
    _DialerV22BisDnaMinDialDelay_Type()
)
dialerV22BisDnaMinDialDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaMinDialDelay.setStatus("mandatory")
_DialerV22BisDnaWaitDialTone_Type = Integer32
_DialerV22BisDnaWaitDialTone_Object = MibTableColumn
dialerV22BisDnaWaitDialTone = _DialerV22BisDnaWaitDialTone_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 12),
    _DialerV22BisDnaWaitDialTone_Type()
)
dialerV22BisDnaWaitDialTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaWaitDialTone.setStatus("mandatory")
_DialerV22BisDnaWaitCarrier_Type = Integer32
_DialerV22BisDnaWaitCarrier_Object = MibTableColumn
dialerV22BisDnaWaitCarrier = _DialerV22BisDnaWaitCarrier_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 13),
    _DialerV22BisDnaWaitCarrier_Type()
)
dialerV22BisDnaWaitCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaWaitCarrier.setStatus("mandatory")
_DialerV22BisDnaHndshkAbortTimer_Type = Integer32
_DialerV22BisDnaHndshkAbortTimer_Object = MibTableColumn
dialerV22BisDnaHndshkAbortTimer = _DialerV22BisDnaHndshkAbortTimer_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 14),
    _DialerV22BisDnaHndshkAbortTimer_Type()
)
dialerV22BisDnaHndshkAbortTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaHndshkAbortTimer.setStatus("mandatory")
_DialerV22BisDnaGuardTone_Type = Integer32
_DialerV22BisDnaGuardTone_Object = MibTableColumn
dialerV22BisDnaGuardTone = _DialerV22BisDnaGuardTone_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 15),
    _DialerV22BisDnaGuardTone_Type()
)
dialerV22BisDnaGuardTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaGuardTone.setStatus("mandatory")
_DialerV22BisDnaPulseDelay_Type = Integer32
_DialerV22BisDnaPulseDelay_Object = MibTableColumn
dialerV22BisDnaPulseDelay = _DialerV22BisDnaPulseDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 16),
    _DialerV22BisDnaPulseDelay_Type()
)
dialerV22BisDnaPulseDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaPulseDelay.setStatus("mandatory")
_DialerV22BisDnaDTMFDuration_Type = Integer32
_DialerV22BisDnaDTMFDuration_Object = MibTableColumn
dialerV22BisDnaDTMFDuration = _DialerV22BisDnaDTMFDuration_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 17),
    _DialerV22BisDnaDTMFDuration_Type()
)
dialerV22BisDnaDTMFDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaDTMFDuration.setStatus("mandatory")
_DialerV22BisDnaDTMFDelay_Type = Integer32
_DialerV22BisDnaDTMFDelay_Object = MibTableColumn
dialerV22BisDnaDTMFDelay = _DialerV22BisDnaDTMFDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 18),
    _DialerV22BisDnaDTMFDelay_Type()
)
dialerV22BisDnaDTMFDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaDTMFDelay.setStatus("mandatory")
_DialerV22BisDnaDTMFLevel_Type = Integer32
_DialerV22BisDnaDTMFLevel_Object = MibTableColumn
dialerV22BisDnaDTMFLevel = _DialerV22BisDnaDTMFLevel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 19),
    _DialerV22BisDnaDTMFLevel_Type()
)
dialerV22BisDnaDTMFLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaDTMFLevel.setStatus("mandatory")
_DialerV22BisDnaTxLevel_Type = Integer32
_DialerV22BisDnaTxLevel_Object = MibTableColumn
dialerV22BisDnaTxLevel = _DialerV22BisDnaTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 20),
    _DialerV22BisDnaTxLevel_Type()
)
dialerV22BisDnaTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaTxLevel.setStatus("mandatory")
_DialerV22BisDnaRxLevel_Type = FalseTrue
_DialerV22BisDnaRxLevel_Object = MibTableColumn
dialerV22BisDnaRxLevel = _DialerV22BisDnaRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 21),
    _DialerV22BisDnaRxLevel_Type()
)
dialerV22BisDnaRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaRxLevel.setStatus("mandatory")
_DialerV22BisDnaRiNbr_Type = Integer32
_DialerV22BisDnaRiNbr_Object = MibTableColumn
dialerV22BisDnaRiNbr = _DialerV22BisDnaRiNbr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 22),
    _DialerV22BisDnaRiNbr_Type()
)
dialerV22BisDnaRiNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaRiNbr.setStatus("mandatory")
_DialerV22BisDnaDeltaRiDelay_Type = Integer32
_DialerV22BisDnaDeltaRiDelay_Object = MibTableColumn
dialerV22BisDnaDeltaRiDelay = _DialerV22BisDnaDeltaRiDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 23),
    _DialerV22BisDnaDeltaRiDelay_Type()
)
dialerV22BisDnaDeltaRiDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaDeltaRiDelay.setStatus("mandatory")
_DialerV22BisDnaRiDtrDelay_Type = Integer32
_DialerV22BisDnaRiDtrDelay_Object = MibTableColumn
dialerV22BisDnaRiDtrDelay = _DialerV22BisDnaRiDtrDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 24),
    _DialerV22BisDnaRiDtrDelay_Type()
)
dialerV22BisDnaRiDtrDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaRiDtrDelay.setStatus("mandatory")
_DialerV22BisDnaDsrRtsDelay_Type = Integer32
_DialerV22BisDnaDsrRtsDelay_Object = MibTableColumn
dialerV22BisDnaDsrRtsDelay = _DialerV22BisDnaDsrRtsDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 25),
    _DialerV22BisDnaDsrRtsDelay_Type()
)
dialerV22BisDnaDsrRtsDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaDsrRtsDelay.setStatus("mandatory")
_DialerV22BisDnaModemSpeed_Type = Integer32
_DialerV22BisDnaModemSpeed_Object = MibTableColumn
dialerV22BisDnaModemSpeed = _DialerV22BisDnaModemSpeed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 26),
    _DialerV22BisDnaModemSpeed_Type()
)
dialerV22BisDnaModemSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaModemSpeed.setStatus("mandatory")
_DialerV22BisDnaDtrSignal_Type = OnOff
_DialerV22BisDnaDtrSignal_Object = MibTableColumn
dialerV22BisDnaDtrSignal = _DialerV22BisDnaDtrSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 27),
    _DialerV22BisDnaDtrSignal_Type()
)
dialerV22BisDnaDtrSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaDtrSignal.setStatus("mandatory")
_DialerV22BisDnaDsrSignal_Type = OnOff
_DialerV22BisDnaDsrSignal_Object = MibTableColumn
dialerV22BisDnaDsrSignal = _DialerV22BisDnaDsrSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 28),
    _DialerV22BisDnaDsrSignal_Type()
)
dialerV22BisDnaDsrSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaDsrSignal.setStatus("mandatory")
_DialerV22BisDnaRiSignal_Type = OnOff
_DialerV22BisDnaRiSignal_Object = MibTableColumn
dialerV22BisDnaRiSignal = _DialerV22BisDnaRiSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 29),
    _DialerV22BisDnaRiSignal_Type()
)
dialerV22BisDnaRiSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaRiSignal.setStatus("mandatory")
_DialerV22BisDnaCdSignal_Type = OnOff
_DialerV22BisDnaCdSignal_Object = MibTableColumn
dialerV22BisDnaCdSignal = _DialerV22BisDnaCdSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 30),
    _DialerV22BisDnaCdSignal_Type()
)
dialerV22BisDnaCdSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaCdSignal.setStatus("mandatory")
_DialerV22BisDnaToneInd_Type = OnOff
_DialerV22BisDnaToneInd_Object = MibTableColumn
dialerV22BisDnaToneInd = _DialerV22BisDnaToneInd_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 31),
    _DialerV22BisDnaToneInd_Type()
)
dialerV22BisDnaToneInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaToneInd.setStatus("mandatory")
_DialerV22BisDnaDloInd_Type = OnOff
_DialerV22BisDnaDloInd_Object = MibTableColumn
dialerV22BisDnaDloInd = _DialerV22BisDnaDloInd_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 32),
    _DialerV22BisDnaDloInd_Type()
)
dialerV22BisDnaDloInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaDloInd.setStatus("mandatory")


class _DialerV22BisDnaState_Type(Integer32):
    """Custom type dialerV22BisDnaState based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("answering", 8),
          ("delaying", 9),
          ("dialing-mdm", 2),
          ("dialing-phone", 1),
          ("handshaking", 11),
          ("initialising", 13),
          ("line-busy", 5),
          ("off-hook", 6),
          ("on-hook", 7),
          ("retrying", 3),
          ("ringing", 4),
          ("voice-com", 10),
          ("wait-ringback", 12))
    )


_DialerV22BisDnaState_Type.__name__ = "Integer32"
_DialerV22BisDnaState_Object = MibTableColumn
dialerV22BisDnaState = _DialerV22BisDnaState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 7, 1, 33),
    _DialerV22BisDnaState_Type()
)
dialerV22BisDnaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisDnaState.setStatus("mandatory")
_DialerV22BisImcInfoTable_Object = MibTable
dialerV22BisImcInfoTable = _DialerV22BisImcInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8)
)
if mibBuilder.loadTexts:
    dialerV22BisImcInfoTable.setStatus("mandatory")
_DialerV22BisImcInfoEntry_Object = MibTableRow
dialerV22BisImcInfoEntry = _DialerV22BisImcInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1)
)
dialerV22BisImcInfoEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerV22BisImcPortRef"),
)
if mibBuilder.loadTexts:
    dialerV22BisImcInfoEntry.setStatus("mandatory")
_DialerV22BisImcPortRef_Type = PortRef
_DialerV22BisImcPortRef_Object = MibTableColumn
dialerV22BisImcPortRef = _DialerV22BisImcPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 1),
    _DialerV22BisImcPortRef_Type()
)
dialerV22BisImcPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcPortRef.setStatus("mandatory")


class _DialerV22BisImcPrimaryNum_Type(DisplayString):
    """Custom type dialerV22BisImcPrimaryNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DialerV22BisImcPrimaryNum_Type.__name__ = "DisplayString"
_DialerV22BisImcPrimaryNum_Object = MibTableColumn
dialerV22BisImcPrimaryNum = _DialerV22BisImcPrimaryNum_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 2),
    _DialerV22BisImcPrimaryNum_Type()
)
dialerV22BisImcPrimaryNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerV22BisImcPrimaryNum.setStatus("mandatory")


class _DialerV22BisImcSecondaryNum_Type(DisplayString):
    """Custom type dialerV22BisImcSecondaryNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DialerV22BisImcSecondaryNum_Type.__name__ = "DisplayString"
_DialerV22BisImcSecondaryNum_Object = MibTableColumn
dialerV22BisImcSecondaryNum = _DialerV22BisImcSecondaryNum_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 3),
    _DialerV22BisImcSecondaryNum_Type()
)
dialerV22BisImcSecondaryNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerV22BisImcSecondaryNum.setStatus("mandatory")
_DialerV22BisImcAnsEnable_Type = FalseTrue
_DialerV22BisImcAnsEnable_Object = MibTableColumn
dialerV22BisImcAnsEnable = _DialerV22BisImcAnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 4),
    _DialerV22BisImcAnsEnable_Type()
)
dialerV22BisImcAnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerV22BisImcAnsEnable.setStatus("mandatory")
_DialerV22BisImcRetryAllowed_Type = FalseTrue
_DialerV22BisImcRetryAllowed_Object = MibTableColumn
dialerV22BisImcRetryAllowed = _DialerV22BisImcRetryAllowed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 5),
    _DialerV22BisImcRetryAllowed_Type()
)
dialerV22BisImcRetryAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcRetryAllowed.setStatus("mandatory")
_DialerV22BisImcMaxRetries_Type = Integer32
_DialerV22BisImcMaxRetries_Object = MibTableColumn
dialerV22BisImcMaxRetries = _DialerV22BisImcMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 6),
    _DialerV22BisImcMaxRetries_Type()
)
dialerV22BisImcMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcMaxRetries.setStatus("mandatory")
_DialerV22BisImcCallProgress_Type = FalseTrue
_DialerV22BisImcCallProgress_Object = MibTableColumn
dialerV22BisImcCallProgress = _DialerV22BisImcCallProgress_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 7),
    _DialerV22BisImcCallProgress_Type()
)
dialerV22BisImcCallProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcCallProgress.setStatus("mandatory")
_DialerV22BisImcDecadic_Type = FalseTrue
_DialerV22BisImcDecadic_Object = MibTableColumn
dialerV22BisImcDecadic = _DialerV22BisImcDecadic_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 8),
    _DialerV22BisImcDecadic_Type()
)
dialerV22BisImcDecadic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcDecadic.setStatus("mandatory")
_DialerV22BisImcMakeBreakRatio_Type = Integer32
_DialerV22BisImcMakeBreakRatio_Object = MibTableColumn
dialerV22BisImcMakeBreakRatio = _DialerV22BisImcMakeBreakRatio_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 9),
    _DialerV22BisImcMakeBreakRatio_Type()
)
dialerV22BisImcMakeBreakRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcMakeBreakRatio.setStatus("mandatory")
_DialerV22BisImcRetryDelay_Type = Integer32
_DialerV22BisImcRetryDelay_Object = MibTableColumn
dialerV22BisImcRetryDelay = _DialerV22BisImcRetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 10),
    _DialerV22BisImcRetryDelay_Type()
)
dialerV22BisImcRetryDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcRetryDelay.setStatus("mandatory")
_DialerV22BisImcMinDialDelay_Type = Integer32
_DialerV22BisImcMinDialDelay_Object = MibTableColumn
dialerV22BisImcMinDialDelay = _DialerV22BisImcMinDialDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 11),
    _DialerV22BisImcMinDialDelay_Type()
)
dialerV22BisImcMinDialDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcMinDialDelay.setStatus("mandatory")
_DialerV22BisImcWaitDialTone_Type = Integer32
_DialerV22BisImcWaitDialTone_Object = MibTableColumn
dialerV22BisImcWaitDialTone = _DialerV22BisImcWaitDialTone_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 12),
    _DialerV22BisImcWaitDialTone_Type()
)
dialerV22BisImcWaitDialTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcWaitDialTone.setStatus("mandatory")
_DialerV22BisImcWaitCarrier_Type = Integer32
_DialerV22BisImcWaitCarrier_Object = MibTableColumn
dialerV22BisImcWaitCarrier = _DialerV22BisImcWaitCarrier_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 13),
    _DialerV22BisImcWaitCarrier_Type()
)
dialerV22BisImcWaitCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcWaitCarrier.setStatus("mandatory")
_DialerV22BisImcHndshkAbortTimer_Type = Integer32
_DialerV22BisImcHndshkAbortTimer_Object = MibTableColumn
dialerV22BisImcHndshkAbortTimer = _DialerV22BisImcHndshkAbortTimer_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 14),
    _DialerV22BisImcHndshkAbortTimer_Type()
)
dialerV22BisImcHndshkAbortTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcHndshkAbortTimer.setStatus("mandatory")
_DialerV22BisImcGuardTone_Type = Integer32
_DialerV22BisImcGuardTone_Object = MibTableColumn
dialerV22BisImcGuardTone = _DialerV22BisImcGuardTone_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 15),
    _DialerV22BisImcGuardTone_Type()
)
dialerV22BisImcGuardTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcGuardTone.setStatus("mandatory")
_DialerV22BisImcPulseDelay_Type = Integer32
_DialerV22BisImcPulseDelay_Object = MibTableColumn
dialerV22BisImcPulseDelay = _DialerV22BisImcPulseDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 16),
    _DialerV22BisImcPulseDelay_Type()
)
dialerV22BisImcPulseDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcPulseDelay.setStatus("mandatory")
_DialerV22BisImcDTMFDuration_Type = Integer32
_DialerV22BisImcDTMFDuration_Object = MibTableColumn
dialerV22BisImcDTMFDuration = _DialerV22BisImcDTMFDuration_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 17),
    _DialerV22BisImcDTMFDuration_Type()
)
dialerV22BisImcDTMFDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcDTMFDuration.setStatus("mandatory")
_DialerV22BisImcDTMFDelay_Type = Integer32
_DialerV22BisImcDTMFDelay_Object = MibTableColumn
dialerV22BisImcDTMFDelay = _DialerV22BisImcDTMFDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 18),
    _DialerV22BisImcDTMFDelay_Type()
)
dialerV22BisImcDTMFDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcDTMFDelay.setStatus("mandatory")
_DialerV22BisImcDTMFLevel_Type = Integer32
_DialerV22BisImcDTMFLevel_Object = MibTableColumn
dialerV22BisImcDTMFLevel = _DialerV22BisImcDTMFLevel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 19),
    _DialerV22BisImcDTMFLevel_Type()
)
dialerV22BisImcDTMFLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcDTMFLevel.setStatus("mandatory")
_DialerV22BisImcTxLevel_Type = Integer32
_DialerV22BisImcTxLevel_Object = MibTableColumn
dialerV22BisImcTxLevel = _DialerV22BisImcTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 20),
    _DialerV22BisImcTxLevel_Type()
)
dialerV22BisImcTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcTxLevel.setStatus("mandatory")
_DialerV22BisImcRxLevel_Type = Integer32
_DialerV22BisImcRxLevel_Object = MibTableColumn
dialerV22BisImcRxLevel = _DialerV22BisImcRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 21),
    _DialerV22BisImcRxLevel_Type()
)
dialerV22BisImcRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcRxLevel.setStatus("mandatory")
_DialerV22BisImcRiNbr_Type = Integer32
_DialerV22BisImcRiNbr_Object = MibTableColumn
dialerV22BisImcRiNbr = _DialerV22BisImcRiNbr_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 22),
    _DialerV22BisImcRiNbr_Type()
)
dialerV22BisImcRiNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcRiNbr.setStatus("mandatory")
_DialerV22BisImcDeltaRiDelay_Type = Integer32
_DialerV22BisImcDeltaRiDelay_Object = MibTableColumn
dialerV22BisImcDeltaRiDelay = _DialerV22BisImcDeltaRiDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 23),
    _DialerV22BisImcDeltaRiDelay_Type()
)
dialerV22BisImcDeltaRiDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcDeltaRiDelay.setStatus("mandatory")
_DialerV22BisImcRiDtrDelay_Type = Integer32
_DialerV22BisImcRiDtrDelay_Object = MibTableColumn
dialerV22BisImcRiDtrDelay = _DialerV22BisImcRiDtrDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 24),
    _DialerV22BisImcRiDtrDelay_Type()
)
dialerV22BisImcRiDtrDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcRiDtrDelay.setStatus("mandatory")
_DialerV22BisImcDsrRtsDelay_Type = Integer32
_DialerV22BisImcDsrRtsDelay_Object = MibTableColumn
dialerV22BisImcDsrRtsDelay = _DialerV22BisImcDsrRtsDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 25),
    _DialerV22BisImcDsrRtsDelay_Type()
)
dialerV22BisImcDsrRtsDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcDsrRtsDelay.setStatus("mandatory")
_DialerV22BisImcModemSpeed_Type = Integer32
_DialerV22BisImcModemSpeed_Object = MibTableColumn
dialerV22BisImcModemSpeed = _DialerV22BisImcModemSpeed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 26),
    _DialerV22BisImcModemSpeed_Type()
)
dialerV22BisImcModemSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcModemSpeed.setStatus("mandatory")
_DialerV22BisImcDtrSignal_Type = OnOff
_DialerV22BisImcDtrSignal_Object = MibTableColumn
dialerV22BisImcDtrSignal = _DialerV22BisImcDtrSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 27),
    _DialerV22BisImcDtrSignal_Type()
)
dialerV22BisImcDtrSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcDtrSignal.setStatus("mandatory")
_DialerV22BisImcDsrSignal_Type = OnOff
_DialerV22BisImcDsrSignal_Object = MibTableColumn
dialerV22BisImcDsrSignal = _DialerV22BisImcDsrSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 28),
    _DialerV22BisImcDsrSignal_Type()
)
dialerV22BisImcDsrSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcDsrSignal.setStatus("mandatory")
_DialerV22BisImcRiSignal_Type = OnOff
_DialerV22BisImcRiSignal_Object = MibTableColumn
dialerV22BisImcRiSignal = _DialerV22BisImcRiSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 29),
    _DialerV22BisImcRiSignal_Type()
)
dialerV22BisImcRiSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcRiSignal.setStatus("mandatory")
_DialerV22BisImcCdSignal_Type = OnOff
_DialerV22BisImcCdSignal_Object = MibTableColumn
dialerV22BisImcCdSignal = _DialerV22BisImcCdSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 30),
    _DialerV22BisImcCdSignal_Type()
)
dialerV22BisImcCdSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcCdSignal.setStatus("mandatory")
_DialerV22BisImcToneInd_Type = OnOff
_DialerV22BisImcToneInd_Object = MibTableColumn
dialerV22BisImcToneInd = _DialerV22BisImcToneInd_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 31),
    _DialerV22BisImcToneInd_Type()
)
dialerV22BisImcToneInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcToneInd.setStatus("mandatory")
_DialerV22BisImcDloInd_Type = OnOff
_DialerV22BisImcDloInd_Object = MibTableColumn
dialerV22BisImcDloInd = _DialerV22BisImcDloInd_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 32),
    _DialerV22BisImcDloInd_Type()
)
dialerV22BisImcDloInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcDloInd.setStatus("mandatory")


class _DialerV22BisImcLineType_Type(Integer32):
    """Custom type dialerV22BisImcLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dial", 1),
          ("leased", 2))
    )


_DialerV22BisImcLineType_Type.__name__ = "Integer32"
_DialerV22BisImcLineType_Object = MibTableColumn
dialerV22BisImcLineType = _DialerV22BisImcLineType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 33),
    _DialerV22BisImcLineType_Type()
)
dialerV22BisImcLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcLineType.setStatus("mandatory")


class _DialerV22BisImcLeasedOpertn_Type(Integer32):
    """Custom type dialerV22BisImcLeasedOpertn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 1),
          ("originate", 2))
    )


_DialerV22BisImcLeasedOpertn_Type.__name__ = "Integer32"
_DialerV22BisImcLeasedOpertn_Object = MibTableColumn
dialerV22BisImcLeasedOpertn = _DialerV22BisImcLeasedOpertn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 34),
    _DialerV22BisImcLeasedOpertn_Type()
)
dialerV22BisImcLeasedOpertn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcLeasedOpertn.setStatus("mandatory")


class _DialerV22BisImcSpeakerLevel_Type(Integer32):
    """Custom type dialerV22BisImcSpeakerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_DialerV22BisImcSpeakerLevel_Type.__name__ = "Integer32"
_DialerV22BisImcSpeakerLevel_Object = MibTableColumn
dialerV22BisImcSpeakerLevel = _DialerV22BisImcSpeakerLevel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 35),
    _DialerV22BisImcSpeakerLevel_Type()
)
dialerV22BisImcSpeakerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcSpeakerLevel.setStatus("mandatory")


class _DialerV22BisImcState_Type(Integer32):
    """Custom type dialerV22BisImcState based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("answering", 8),
          ("delaying", 9),
          ("dialing-mdm", 2),
          ("dialing-phone", 1),
          ("handshaking", 11),
          ("initialising", 13),
          ("line-busy", 5),
          ("off-hook", 6),
          ("on-hook", 7),
          ("retrying", 3),
          ("ringing", 4),
          ("voice-com", 10),
          ("wait-ringback", 12))
    )


_DialerV22BisImcState_Type.__name__ = "Integer32"
_DialerV22BisImcState_Object = MibTableColumn
dialerV22BisImcState = _DialerV22BisImcState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 8, 1, 36),
    _DialerV22BisImcState_Type()
)
dialerV22BisImcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV22BisImcState.setStatus("mandatory")
_DialerV32BisInfoTable_Object = MibTable
dialerV32BisInfoTable = _DialerV32BisInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9)
)
if mibBuilder.loadTexts:
    dialerV32BisInfoTable.setStatus("mandatory")
_DialerV32BisInfoEntry_Object = MibTableRow
dialerV32BisInfoEntry = _DialerV32BisInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1)
)
dialerV32BisInfoEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerV32BisPortRef"),
)
if mibBuilder.loadTexts:
    dialerV32BisInfoEntry.setStatus("mandatory")
_DialerV32BisPortRef_Type = PortRef
_DialerV32BisPortRef_Object = MibTableColumn
dialerV32BisPortRef = _DialerV32BisPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 1),
    _DialerV32BisPortRef_Type()
)
dialerV32BisPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisPortRef.setStatus("mandatory")


class _DialerV32BisPrimNum_Type(DisplayString):
    """Custom type dialerV32BisPrimNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DialerV32BisPrimNum_Type.__name__ = "DisplayString"
_DialerV32BisPrimNum_Object = MibTableColumn
dialerV32BisPrimNum = _DialerV32BisPrimNum_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 2),
    _DialerV32BisPrimNum_Type()
)
dialerV32BisPrimNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerV32BisPrimNum.setStatus("mandatory")


class _DialerV32BisSecNum_Type(DisplayString):
    """Custom type dialerV32BisSecNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DialerV32BisSecNum_Type.__name__ = "DisplayString"
_DialerV32BisSecNum_Object = MibTableColumn
dialerV32BisSecNum = _DialerV32BisSecNum_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 3),
    _DialerV32BisSecNum_Type()
)
dialerV32BisSecNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerV32BisSecNum.setStatus("mandatory")


class _DialerV32BisOverrNum_Type(DisplayString):
    """Custom type dialerV32BisOverrNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DialerV32BisOverrNum_Type.__name__ = "DisplayString"
_DialerV32BisOverrNum_Object = MibTableColumn
dialerV32BisOverrNum = _DialerV32BisOverrNum_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 4),
    _DialerV32BisOverrNum_Type()
)
dialerV32BisOverrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisOverrNum.setStatus("mandatory")


class _DialerV32BisCurrNum_Type(DisplayString):
    """Custom type dialerV32BisCurrNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DialerV32BisCurrNum_Type.__name__ = "DisplayString"
_DialerV32BisCurrNum_Object = MibTableColumn
dialerV32BisCurrNum = _DialerV32BisCurrNum_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 5),
    _DialerV32BisCurrNum_Type()
)
dialerV32BisCurrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisCurrNum.setStatus("mandatory")
_DialerV32BisPrimBitRate_Type = PrimBitRate
_DialerV32BisPrimBitRate_Object = MibTableColumn
dialerV32BisPrimBitRate = _DialerV32BisPrimBitRate_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 6),
    _DialerV32BisPrimBitRate_Type()
)
dialerV32BisPrimBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisPrimBitRate.setStatus("mandatory")
_DialerV32BisSecBitRate_Type = PrimBitRate
_DialerV32BisSecBitRate_Object = MibTableColumn
dialerV32BisSecBitRate = _DialerV32BisSecBitRate_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 7),
    _DialerV32BisSecBitRate_Type()
)
dialerV32BisSecBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisSecBitRate.setStatus("mandatory")
_DialerV32BisOverrBitRate_Type = PrimBitRate
_DialerV32BisOverrBitRate_Object = MibTableColumn
dialerV32BisOverrBitRate = _DialerV32BisOverrBitRate_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 8),
    _DialerV32BisOverrBitRate_Type()
)
dialerV32BisOverrBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisOverrBitRate.setStatus("mandatory")
_DialerV32BisCurrBitRate_Type = PrimBitRate
_DialerV32BisCurrBitRate_Object = MibTableColumn
dialerV32BisCurrBitRate = _DialerV32BisCurrBitRate_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 9),
    _DialerV32BisCurrBitRate_Type()
)
dialerV32BisCurrBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisCurrBitRate.setStatus("mandatory")
_DialerV32BisPrimConfig_Type = PrimCfg
_DialerV32BisPrimConfig_Object = MibTableColumn
dialerV32BisPrimConfig = _DialerV32BisPrimConfig_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 10),
    _DialerV32BisPrimConfig_Type()
)
dialerV32BisPrimConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisPrimConfig.setStatus("mandatory")
_DialerV32BisSecConfig_Type = PrimCfg
_DialerV32BisSecConfig_Object = MibTableColumn
dialerV32BisSecConfig = _DialerV32BisSecConfig_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 11),
    _DialerV32BisSecConfig_Type()
)
dialerV32BisSecConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisSecConfig.setStatus("mandatory")
_DialerV32BisOverrConfig_Type = PrimCfg
_DialerV32BisOverrConfig_Object = MibTableColumn
dialerV32BisOverrConfig = _DialerV32BisOverrConfig_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 12),
    _DialerV32BisOverrConfig_Type()
)
dialerV32BisOverrConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisOverrConfig.setStatus("mandatory")
_DialerV32BisCurrConfig_Type = PrimCfg
_DialerV32BisCurrConfig_Object = MibTableColumn
dialerV32BisCurrConfig = _DialerV32BisCurrConfig_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 13),
    _DialerV32BisCurrConfig_Type()
)
dialerV32BisCurrConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisCurrConfig.setStatus("mandatory")
_DialerV32BisCurrRetry_Type = Integer32
_DialerV32BisCurrRetry_Object = MibTableColumn
dialerV32BisCurrRetry = _DialerV32BisCurrRetry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 14),
    _DialerV32BisCurrRetry_Type()
)
dialerV32BisCurrRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisCurrRetry.setStatus("mandatory")
_DialerV32BisRingCount_Type = Integer32
_DialerV32BisRingCount_Object = MibTableColumn
dialerV32BisRingCount = _DialerV32BisRingCount_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 15),
    _DialerV32BisRingCount_Type()
)
dialerV32BisRingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisRingCount.setStatus("mandatory")
_DialerV32BisAnsEnable_Type = FalseTrue
_DialerV32BisAnsEnable_Object = MibTableColumn
dialerV32BisAnsEnable = _DialerV32BisAnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 16),
    _DialerV32BisAnsEnable_Type()
)
dialerV32BisAnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerV32BisAnsEnable.setStatus("mandatory")


class _DialerV32BisDialMethod_Type(Integer32):
    """Custom type dialerV32BisDialMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtmf", 1),
          ("pulse", 2))
    )


_DialerV32BisDialMethod_Type.__name__ = "Integer32"
_DialerV32BisDialMethod_Object = MibTableColumn
dialerV32BisDialMethod = _DialerV32BisDialMethod_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 17),
    _DialerV32BisDialMethod_Type()
)
dialerV32BisDialMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisDialMethod.setStatus("mandatory")
_DialerV32BisRetry_Type = FalseTrue
_DialerV32BisRetry_Object = MibTableColumn
dialerV32BisRetry = _DialerV32BisRetry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 18),
    _DialerV32BisRetry_Type()
)
dialerV32BisRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisRetry.setStatus("mandatory")
_DialerV32BisCallFailure_Type = Integer32
_DialerV32BisCallFailure_Object = MibTableColumn
dialerV32BisCallFailure = _DialerV32BisCallFailure_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 19),
    _DialerV32BisCallFailure_Type()
)
dialerV32BisCallFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisCallFailure.setStatus("mandatory")
_DialerV32BisCarrierDetect_Type = Integer32
_DialerV32BisCarrierDetect_Object = MibTableColumn
dialerV32BisCarrierDetect = _DialerV32BisCarrierDetect_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 20),
    _DialerV32BisCarrierDetect_Type()
)
dialerV32BisCarrierDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisCarrierDetect.setStatus("mandatory")
_DialerV32BisCarrierWait_Type = Integer32
_DialerV32BisCarrierWait_Object = MibTableColumn
dialerV32BisCarrierWait = _DialerV32BisCarrierWait_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 21),
    _DialerV32BisCarrierWait_Type()
)
dialerV32BisCarrierWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisCarrierWait.setStatus("mandatory")
_DialerV32BisHangupVerify_Type = Integer32
_DialerV32BisHangupVerify_Object = MibTableColumn
dialerV32BisHangupVerify = _DialerV32BisHangupVerify_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 22),
    _DialerV32BisHangupVerify_Type()
)
dialerV32BisHangupVerify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisHangupVerify.setStatus("mandatory")
_DialerV32BisHangupSignal_Type = DisEnable
_DialerV32BisHangupSignal_Object = MibTableColumn
dialerV32BisHangupSignal = _DialerV32BisHangupSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 23),
    _DialerV32BisHangupSignal_Type()
)
dialerV32BisHangupSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisHangupSignal.setStatus("mandatory")
_DialerV32BisTxLevel_Type = Integer32
_DialerV32BisTxLevel_Object = MibTableColumn
dialerV32BisTxLevel = _DialerV32BisTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 24),
    _DialerV32BisTxLevel_Type()
)
dialerV32BisTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisTxLevel.setStatus("mandatory")
_DialerV32BisRxLevel_Type = Integer32
_DialerV32BisRxLevel_Object = MibTableColumn
dialerV32BisRxLevel = _DialerV32BisRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 25),
    _DialerV32BisRxLevel_Type()
)
dialerV32BisRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisRxLevel.setStatus("mandatory")
_DialerV32BisGuardTone_Type = Integer32
_DialerV32BisGuardTone_Object = MibTableColumn
dialerV32BisGuardTone = _DialerV32BisGuardTone_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 26),
    _DialerV32BisGuardTone_Type()
)
dialerV32BisGuardTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisGuardTone.setStatus("mandatory")


class _DialerV32BisLeasedLine_Type(Integer32):
    """Custom type dialerV32BisLeasedLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("four-w-ll", 2),
          ("two-w-ll", 1))
    )


_DialerV32BisLeasedLine_Type.__name__ = "Integer32"
_DialerV32BisLeasedLine_Object = MibTableColumn
dialerV32BisLeasedLine = _DialerV32BisLeasedLine_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 27),
    _DialerV32BisLeasedLine_Type()
)
dialerV32BisLeasedLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisLeasedLine.setStatus("mandatory")


class _DialerV32BisLeaseMode_Type(Integer32):
    """Custom type dialerV32BisLeaseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("answer", 1),
          ("originate", 2))
    )


_DialerV32BisLeaseMode_Type.__name__ = "Integer32"
_DialerV32BisLeaseMode_Object = MibTableColumn
dialerV32BisLeaseMode = _DialerV32BisLeaseMode_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 28),
    _DialerV32BisLeaseMode_Type()
)
dialerV32BisLeaseMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisLeaseMode.setStatus("mandatory")
_DialerV32BisLLTxLevel_Type = Integer32
_DialerV32BisLLTxLevel_Object = MibTableColumn
dialerV32BisLLTxLevel = _DialerV32BisLLTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 29),
    _DialerV32BisLLTxLevel_Type()
)
dialerV32BisLLTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisLLTxLevel.setStatus("mandatory")
_DialerV32BisLLConfig_Type = PrimCfg
_DialerV32BisLLConfig_Object = MibTableColumn
dialerV32BisLLConfig = _DialerV32BisLLConfig_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 30),
    _DialerV32BisLLConfig_Type()
)
dialerV32BisLLConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisLLConfig.setStatus("mandatory")
_DialerV32BisLLBitRate_Type = PrimBitRate
_DialerV32BisLLBitRate_Object = MibTableColumn
dialerV32BisLLBitRate = _DialerV32BisLLBitRate_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 31),
    _DialerV32BisLLBitRate_Type()
)
dialerV32BisLLBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisLLBitRate.setStatus("mandatory")
_DialerV32BisCallingTone_Type = DisEnable
_DialerV32BisCallingTone_Object = MibTableColumn
dialerV32BisCallingTone = _DialerV32BisCallingTone_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 32),
    _DialerV32BisCallingTone_Type()
)
dialerV32BisCallingTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisCallingTone.setStatus("mandatory")
_DialerV32BisAutoMode_Type = DisEnable
_DialerV32BisAutoMode_Object = MibTableColumn
dialerV32BisAutoMode = _DialerV32BisAutoMode_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 33),
    _DialerV32BisAutoMode_Type()
)
dialerV32BisAutoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisAutoMode.setStatus("mandatory")
_DialerV32BisRetryAllowed_Type = DisEnable
_DialerV32BisRetryAllowed_Object = MibTableColumn
dialerV32BisRetryAllowed = _DialerV32BisRetryAllowed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 34),
    _DialerV32BisRetryAllowed_Type()
)
dialerV32BisRetryAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisRetryAllowed.setStatus("mandatory")
_DialerV32BisMaxRetry_Type = Integer32
_DialerV32BisMaxRetry_Object = MibTableColumn
dialerV32BisMaxRetry = _DialerV32BisMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 35),
    _DialerV32BisMaxRetry_Type()
)
dialerV32BisMaxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisMaxRetry.setStatus("mandatory")
_DialerV32BisDialTone_Type = DisEnable
_DialerV32BisDialTone_Object = MibTableColumn
dialerV32BisDialTone = _DialerV32BisDialTone_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 36),
    _DialerV32BisDialTone_Type()
)
dialerV32BisDialTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisDialTone.setStatus("mandatory")
_DialerV32BisDialToneWait_Type = Integer32
_DialerV32BisDialToneWait_Object = MibTableColumn
dialerV32BisDialToneWait = _DialerV32BisDialToneWait_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 37),
    _DialerV32BisDialToneWait_Type()
)
dialerV32BisDialToneWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisDialToneWait.setStatus("mandatory")
_DialerV32BisRetryWait_Type = Integer32
_DialerV32BisRetryWait_Object = MibTableColumn
dialerV32BisRetryWait = _DialerV32BisRetryWait_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 38),
    _DialerV32BisRetryWait_Type()
)
dialerV32BisRetryWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisRetryWait.setStatus("mandatory")
_DialerV32BisHangupWait_Type = Integer32
_DialerV32BisHangupWait_Object = MibTableColumn
dialerV32BisHangupWait = _DialerV32BisHangupWait_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 39),
    _DialerV32BisHangupWait_Type()
)
dialerV32BisHangupWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisHangupWait.setStatus("mandatory")
_DialerV32BisDialPauseWait_Type = Integer32
_DialerV32BisDialPauseWait_Object = MibTableColumn
dialerV32BisDialPauseWait = _DialerV32BisDialPauseWait_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 40),
    _DialerV32BisDialPauseWait_Type()
)
dialerV32BisDialPauseWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisDialPauseWait.setStatus("mandatory")
_DialerV32BisDeltaRiWait_Type = Integer32
_DialerV32BisDeltaRiWait_Object = MibTableColumn
dialerV32BisDeltaRiWait = _DialerV32BisDeltaRiWait_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 41),
    _DialerV32BisDeltaRiWait_Type()
)
dialerV32BisDeltaRiWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisDeltaRiWait.setStatus("mandatory")
_DialerV32BisDTMFDuration_Type = Integer32
_DialerV32BisDTMFDuration_Object = MibTableColumn
dialerV32BisDTMFDuration = _DialerV32BisDTMFDuration_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 42),
    _DialerV32BisDTMFDuration_Type()
)
dialerV32BisDTMFDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisDTMFDuration.setStatus("mandatory")
_DialerV32BisDTMFDelay_Type = Integer32
_DialerV32BisDTMFDelay_Object = MibTableColumn
dialerV32BisDTMFDelay = _DialerV32BisDTMFDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 43),
    _DialerV32BisDTMFDelay_Type()
)
dialerV32BisDTMFDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisDTMFDelay.setStatus("mandatory")
_DialerV32BisDTMFFreq1Level_Type = Integer32
_DialerV32BisDTMFFreq1Level_Object = MibTableColumn
dialerV32BisDTMFFreq1Level = _DialerV32BisDTMFFreq1Level_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 44),
    _DialerV32BisDTMFFreq1Level_Type()
)
dialerV32BisDTMFFreq1Level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisDTMFFreq1Level.setStatus("mandatory")
_DialerV32BisDTMFFreq2Level_Type = Integer32
_DialerV32BisDTMFFreq2Level_Object = MibTableColumn
dialerV32BisDTMFFreq2Level = _DialerV32BisDTMFFreq2Level_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 45),
    _DialerV32BisDTMFFreq2Level_Type()
)
dialerV32BisDTMFFreq2Level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisDTMFFreq2Level.setStatus("mandatory")
_DialerV32BisPulseMakeTime_Type = Integer32
_DialerV32BisPulseMakeTime_Object = MibTableColumn
dialerV32BisPulseMakeTime = _DialerV32BisPulseMakeTime_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 46),
    _DialerV32BisPulseMakeTime_Type()
)
dialerV32BisPulseMakeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisPulseMakeTime.setStatus("mandatory")
_DialerV32BisPulseBreakTime_Type = Integer32
_DialerV32BisPulseBreakTime_Object = MibTableColumn
dialerV32BisPulseBreakTime = _DialerV32BisPulseBreakTime_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 47),
    _DialerV32BisPulseBreakTime_Type()
)
dialerV32BisPulseBreakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisPulseBreakTime.setStatus("mandatory")
_DialerV32BisPulseDelay_Type = Integer32
_DialerV32BisPulseDelay_Object = MibTableColumn
dialerV32BisPulseDelay = _DialerV32BisPulseDelay_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 48),
    _DialerV32BisPulseDelay_Type()
)
dialerV32BisPulseDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisPulseDelay.setStatus("mandatory")


class _DialerV32BisSpeakerLevel_Type(Integer32):
    """Custom type dialerV32BisSpeakerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_DialerV32BisSpeakerLevel_Type.__name__ = "Integer32"
_DialerV32BisSpeakerLevel_Object = MibTableColumn
dialerV32BisSpeakerLevel = _DialerV32BisSpeakerLevel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 49),
    _DialerV32BisSpeakerLevel_Type()
)
dialerV32BisSpeakerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisSpeakerLevel.setStatus("mandatory")
_DialerV32BisRiToAnswer_Type = Integer32
_DialerV32BisRiToAnswer_Object = MibTableColumn
dialerV32BisRiToAnswer = _DialerV32BisRiToAnswer_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 50),
    _DialerV32BisRiToAnswer_Type()
)
dialerV32BisRiToAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisRiToAnswer.setStatus("mandatory")
_DialerV32BisAnswerBitRate_Type = PrimBitRate
_DialerV32BisAnswerBitRate_Object = MibTableColumn
dialerV32BisAnswerBitRate = _DialerV32BisAnswerBitRate_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 51),
    _DialerV32BisAnswerBitRate_Type()
)
dialerV32BisAnswerBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisAnswerBitRate.setStatus("mandatory")
_DialerV32BisAnswerConfig_Type = PrimCfg
_DialerV32BisAnswerConfig_Object = MibTableColumn
dialerV32BisAnswerConfig = _DialerV32BisAnswerConfig_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 52),
    _DialerV32BisAnswerConfig_Type()
)
dialerV32BisAnswerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisAnswerConfig.setStatus("mandatory")
_DialerV32BisRetrain_Type = OnOff
_DialerV32BisRetrain_Object = MibTableColumn
dialerV32BisRetrain = _DialerV32BisRetrain_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 53),
    _DialerV32BisRetrain_Type()
)
dialerV32BisRetrain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisRetrain.setStatus("mandatory")


class _DialerV32BisEqmLevel_Type(Integer32):
    """Custom type dialerV32BisEqmLevel based on Integer32"""
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
        *(("disable", 1),
          ("high-quality", 4),
          ("low-quality", 2),
          ("medium-quality", 3))
    )


_DialerV32BisEqmLevel_Type.__name__ = "Integer32"
_DialerV32BisEqmLevel_Object = MibTableColumn
dialerV32BisEqmLevel = _DialerV32BisEqmLevel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 54),
    _DialerV32BisEqmLevel_Type()
)
dialerV32BisEqmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisEqmLevel.setStatus("mandatory")
_DialerV32BisRiOnOffDetect_Type = OnOff
_DialerV32BisRiOnOffDetect_Object = MibTableColumn
dialerV32BisRiOnOffDetect = _DialerV32BisRiOnOffDetect_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 55),
    _DialerV32BisRiOnOffDetect_Type()
)
dialerV32BisRiOnOffDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisRiOnOffDetect.setStatus("mandatory")
_DialerV32BisCdDetect_Type = OnOff
_DialerV32BisCdDetect_Object = MibTableColumn
dialerV32BisCdDetect = _DialerV32BisCdDetect_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 56),
    _DialerV32BisCdDetect_Type()
)
dialerV32BisCdDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisCdDetect.setStatus("mandatory")
_DialerV32BisRingbackDetect_Type = OnOff
_DialerV32BisRingbackDetect_Object = MibTableColumn
dialerV32BisRingbackDetect = _DialerV32BisRingbackDetect_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 57),
    _DialerV32BisRingbackDetect_Type()
)
dialerV32BisRingbackDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisRingbackDetect.setStatus("mandatory")
_DialerV32BisAnswerDetect_Type = OnOff
_DialerV32BisAnswerDetect_Object = MibTableColumn
dialerV32BisAnswerDetect = _DialerV32BisAnswerDetect_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 58),
    _DialerV32BisAnswerDetect_Type()
)
dialerV32BisAnswerDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisAnswerDetect.setStatus("mandatory")
_DialerV32BisBusyDetect_Type = OnOff
_DialerV32BisBusyDetect_Object = MibTableColumn
dialerV32BisBusyDetect = _DialerV32BisBusyDetect_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 59),
    _DialerV32BisBusyDetect_Type()
)
dialerV32BisBusyDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisBusyDetect.setStatus("mandatory")
_DialerV32BisDiscDetect_Type = OnOff
_DialerV32BisDiscDetect_Object = MibTableColumn
dialerV32BisDiscDetect = _DialerV32BisDiscDetect_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 60),
    _DialerV32BisDiscDetect_Type()
)
dialerV32BisDiscDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisDiscDetect.setStatus("mandatory")
_DialerV32BisCdSignal_Type = OnOff
_DialerV32BisCdSignal_Object = MibTableColumn
dialerV32BisCdSignal = _DialerV32BisCdSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 61),
    _DialerV32BisCdSignal_Type()
)
dialerV32BisCdSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisCdSignal.setStatus("mandatory")
_DialerV32BisDsrSignal_Type = OnOff
_DialerV32BisDsrSignal_Object = MibTableColumn
dialerV32BisDsrSignal = _DialerV32BisDsrSignal_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 62),
    _DialerV32BisDsrSignal_Type()
)
dialerV32BisDsrSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisDsrSignal.setStatus("mandatory")


class _DialerV32BisState_Type(Integer32):
    """Custom type dialerV32BisState based on Integer32"""
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
        *(("m-answering", 6),
          ("m-closed", 1),
          ("m-closing", 15),
          ("m-connected", 9),
          ("m-dialing", 5),
          ("m-hangup-idle", 14),
          ("m-local-disc", 13),
          ("m-local-test", 3),
          ("m-offhook-idle", 16),
          ("m-opened", 2),
          ("m-originating", 7),
          ("m-remote-disc", 12),
          ("m-remote-test", 11),
          ("m-retraining", 10),
          ("m-retrying", 8),
          ("m-ringing", 4))
    )


_DialerV32BisState_Type.__name__ = "Integer32"
_DialerV32BisState_Object = MibTableColumn
dialerV32BisState = _DialerV32BisState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 9, 1, 63),
    _DialerV32BisState_Type()
)
dialerV32BisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerV32BisState.setStatus("mandatory")
_DialerControlTable_Object = MibTable
dialerControlTable = _DialerControlTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10)
)
if mibBuilder.loadTexts:
    dialerControlTable.setStatus("mandatory")
_DialerControlEntry_Object = MibTableRow
dialerControlEntry = _DialerControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1)
)
dialerControlEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerCtrlPortRef"),
)
if mibBuilder.loadTexts:
    dialerControlEntry.setStatus("mandatory")
_DialerCtrlPortRef_Type = PortRef
_DialerCtrlPortRef_Object = MibTableColumn
dialerCtrlPortRef = _DialerCtrlPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 1),
    _DialerCtrlPortRef_Type()
)
dialerCtrlPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerCtrlPortRef.setStatus("mandatory")


class _DialerCtrlAction_Type(Integer32):
    """Custom type dialerCtrlAction based on Integer32"""
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
        *(("dial", 2),
          ("exec", 1),
          ("hangup", 3),
          ("idle", 5),
          ("other", 7),
          ("start", 4),
          ("store", 6))
    )


_DialerCtrlAction_Type.__name__ = "Integer32"
_DialerCtrlAction_Object = MibTableColumn
dialerCtrlAction = _DialerCtrlAction_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 2),
    _DialerCtrlAction_Type()
)
dialerCtrlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerCtrlAction.setStatus("mandatory")
_DialerCtrlAnsEnable_Type = FalseTrue
_DialerCtrlAnsEnable_Object = MibTableColumn
dialerCtrlAnsEnable = _DialerCtrlAnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 3),
    _DialerCtrlAnsEnable_Type()
)
dialerCtrlAnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerCtrlAnsEnable.setStatus("mandatory")
_DialerCtrlDirectDSROnOff_Type = OnOff
_DialerCtrlDirectDSROnOff_Object = MibTableColumn
dialerCtrlDirectDSROnOff = _DialerCtrlDirectDSROnOff_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 4),
    _DialerCtrlDirectDSROnOff_Type()
)
dialerCtrlDirectDSROnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerCtrlDirectDSROnOff.setStatus("mandatory")


class _DialerCtrlNumber_Type(DisplayString):
    """Custom type dialerCtrlNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DialerCtrlNumber_Type.__name__ = "DisplayString"
_DialerCtrlNumber_Object = MibTableColumn
dialerCtrlNumber = _DialerCtrlNumber_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 5),
    _DialerCtrlNumber_Type()
)
dialerCtrlNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerCtrlNumber.setStatus("mandatory")


class _DialerCtrlScriptFile_Type(DisplayString):
    """Custom type dialerCtrlScriptFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DialerCtrlScriptFile_Type.__name__ = "DisplayString"
_DialerCtrlScriptFile_Object = MibTableColumn
dialerCtrlScriptFile = _DialerCtrlScriptFile_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 6),
    _DialerCtrlScriptFile_Type()
)
dialerCtrlScriptFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerCtrlScriptFile.setStatus("mandatory")
_DialerCtrlActionState_Type = ActionState
_DialerCtrlActionState_Object = MibTableColumn
dialerCtrlActionState = _DialerCtrlActionState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 7),
    _DialerCtrlActionState_Type()
)
dialerCtrlActionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerCtrlActionState.setStatus("mandatory")
_DialerCtrlActionError_Type = Integer32
_DialerCtrlActionError_Object = MibTableColumn
dialerCtrlActionError = _DialerCtrlActionError_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 8),
    _DialerCtrlActionError_Type()
)
dialerCtrlActionError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerCtrlActionError.setStatus("mandatory")
_DialerCtrlConfig_Type = PrimCfg
_DialerCtrlConfig_Object = MibTableColumn
dialerCtrlConfig = _DialerCtrlConfig_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 9),
    _DialerCtrlConfig_Type()
)
dialerCtrlConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerCtrlConfig.setStatus("mandatory")
_DialerCtrlBitRate_Type = PrimBitRate
_DialerCtrlBitRate_Object = MibTableColumn
dialerCtrlBitRate = _DialerCtrlBitRate_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 10),
    _DialerCtrlBitRate_Type()
)
dialerCtrlBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerCtrlBitRate.setStatus("mandatory")
_DialerCtrlType_Type = IsdnDnType
_DialerCtrlType_Object = MibTableColumn
dialerCtrlType = _DialerCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 11),
    _DialerCtrlType_Type()
)
dialerCtrlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerCtrlType.setStatus("mandatory")
_DialerCtrlPlan_Type = IsdnDnPlan
_DialerCtrlPlan_Object = MibTableColumn
dialerCtrlPlan = _DialerCtrlPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 12),
    _DialerCtrlPlan_Type()
)
dialerCtrlPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerCtrlPlan.setStatus("mandatory")


class _DialerCtrlSub_Type(DisplayString):
    """Custom type dialerCtrlSub based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerCtrlSub_Type.__name__ = "DisplayString"
_DialerCtrlSub_Object = MibTableColumn
dialerCtrlSub = _DialerCtrlSub_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 13),
    _DialerCtrlSub_Type()
)
dialerCtrlSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerCtrlSub.setStatus("mandatory")
_DialerCtrlSubType_Type = IsdnSubType
_DialerCtrlSubType_Object = MibTableColumn
dialerCtrlSubType = _DialerCtrlSubType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 14),
    _DialerCtrlSubType_Type()
)
dialerCtrlSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerCtrlSubType.setStatus("mandatory")


class _DialerCtrlTns_Type(DisplayString):
    """Custom type dialerCtrlTns based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DialerCtrlTns_Type.__name__ = "DisplayString"
_DialerCtrlTns_Object = MibTableColumn
dialerCtrlTns = _DialerCtrlTns_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 15),
    _DialerCtrlTns_Type()
)
dialerCtrlTns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerCtrlTns.setStatus("mandatory")


class _DialerCtrlNumberTemp_Type(DisplayString):
    """Custom type dialerCtrlNumberTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_DialerCtrlNumberTemp_Type.__name__ = "DisplayString"
_DialerCtrlNumberTemp_Object = MibTableColumn
dialerCtrlNumberTemp = _DialerCtrlNumberTemp_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 16),
    _DialerCtrlNumberTemp_Type()
)
dialerCtrlNumberTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerCtrlNumberTemp.setStatus("mandatory")
_DialerCtrlDialMask_Type = Integer32
_DialerCtrlDialMask_Object = MibTableColumn
dialerCtrlDialMask = _DialerCtrlDialMask_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 17),
    _DialerCtrlDialMask_Type()
)
dialerCtrlDialMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerCtrlDialMask.setStatus("mandatory")
_DialerCtrlCallSpeed_Type = Integer32
_DialerCtrlCallSpeed_Object = MibTableColumn
dialerCtrlCallSpeed = _DialerCtrlCallSpeed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 10, 1, 18),
    _DialerCtrlCallSpeed_Type()
)
dialerCtrlCallSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerCtrlCallSpeed.setStatus("mandatory")
_DialerIsdnStatusTable_Object = MibTable
dialerIsdnStatusTable = _DialerIsdnStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 11)
)
if mibBuilder.loadTexts:
    dialerIsdnStatusTable.setStatus("mandatory")
_DialerIsdnStatusEntry_Object = MibTableRow
dialerIsdnStatusEntry = _DialerIsdnStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 11, 1)
)
dialerIsdnStatusEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerIsdnStatusPortRef"),
)
if mibBuilder.loadTexts:
    dialerIsdnStatusEntry.setStatus("mandatory")
_DialerIsdnStatusPortRef_Type = PortRef
_DialerIsdnStatusPortRef_Object = MibTableColumn
dialerIsdnStatusPortRef = _DialerIsdnStatusPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 11, 1, 1),
    _DialerIsdnStatusPortRef_Type()
)
dialerIsdnStatusPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnStatusPortRef.setStatus("mandatory")


class _DialerIsdnStatusSwitchType_Type(Integer32):
    """Custom type dialerIsdnStatusSwitchType based on Integer32"""
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
        *(("att", 3),
          ("illegal", 8),
          ("net3", 6),
          ("ni1", 1),
          ("nt", 2),
          ("tph", 7),
          ("tr6", 4),
          ("vn3", 5))
    )


_DialerIsdnStatusSwitchType_Type.__name__ = "Integer32"
_DialerIsdnStatusSwitchType_Object = MibTableColumn
dialerIsdnStatusSwitchType = _DialerIsdnStatusSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 11, 1, 2),
    _DialerIsdnStatusSwitchType_Type()
)
dialerIsdnStatusSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnStatusSwitchType.setStatus("mandatory")


class _DialerIsdnStatusChType_Type(Integer32):
    """Custom type dialerIsdnStatusChType based on Integer32"""
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
        *(("b-channel", 1),
          ("d-channel", 2),
          ("illegal", 3),
          ("unused", 4))
    )


_DialerIsdnStatusChType_Type.__name__ = "Integer32"
_DialerIsdnStatusChType_Object = MibTableColumn
dialerIsdnStatusChType = _DialerIsdnStatusChType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 11, 1, 3),
    _DialerIsdnStatusChType_Type()
)
dialerIsdnStatusChType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnStatusChType.setStatus("mandatory")


class _DialerIsdnStatusL1State_Type(Integer32):
    """Custom type dialerIsdnStatusL1State based on Integer32"""
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
        *(("activate", 4),
          ("await-info2", 2),
          ("await-info4", 3),
          ("deactivated", 1),
          ("illegal", 5))
    )


_DialerIsdnStatusL1State_Type.__name__ = "Integer32"
_DialerIsdnStatusL1State_Object = MibTableColumn
dialerIsdnStatusL1State = _DialerIsdnStatusL1State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 11, 1, 4),
    _DialerIsdnStatusL1State_Type()
)
dialerIsdnStatusL1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnStatusL1State.setStatus("mandatory")


class _DialerIsdnStatusState_Type(Integer32):
    """Custom type dialerIsdnStatusState based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("isdn-closed", 7),
          ("isdn-closing", 13),
          ("isdn-connected", 10),
          ("isdn-connecting", 9),
          ("isdn-deact-closed", 1),
          ("isdn-deact-opened", 2),
          ("isdn-disconnecting", 12),
          ("isdn-illegal", 19),
          ("isdn-linking-act", 16),
          ("isdn-linking-deact", 15),
          ("isdn-linking-ring", 18),
          ("isdn-loopback", 14),
          ("isdn-opened", 8),
          ("isdn-release-closed", 5),
          ("isdn-release-opened", 6),
          ("isdn-ringing", 11),
          ("isdn-test", 17),
          ("isdn-wait-act-closed", 3),
          ("isdn-wait-act-opened", 4))
    )


_DialerIsdnStatusState_Type.__name__ = "Integer32"
_DialerIsdnStatusState_Object = MibTableColumn
dialerIsdnStatusState = _DialerIsdnStatusState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 11, 1, 5),
    _DialerIsdnStatusState_Type()
)
dialerIsdnStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnStatusState.setStatus("mandatory")
_DialerIsdnNI1BChTable_Object = MibTable
dialerIsdnNI1BChTable = _DialerIsdnNI1BChTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12)
)
if mibBuilder.loadTexts:
    dialerIsdnNI1BChTable.setStatus("mandatory")
_DialerIsdnNI1BChEntry_Object = MibTableRow
dialerIsdnNI1BChEntry = _DialerIsdnNI1BChEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1)
)
dialerIsdnNI1BChEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerIsdnNI1BChPortRef"),
)
if mibBuilder.loadTexts:
    dialerIsdnNI1BChEntry.setStatus("mandatory")
_DialerIsdnNI1BChPortRef_Type = PortRef
_DialerIsdnNI1BChPortRef_Object = MibTableColumn
dialerIsdnNI1BChPortRef = _DialerIsdnNI1BChPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 1),
    _DialerIsdnNI1BChPortRef_Type()
)
dialerIsdnNI1BChPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChPortRef.setStatus("mandatory")


class _DialerIsdnNI1BChSpid_Type(DisplayString):
    """Custom type dialerIsdnNI1BChSpid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnNI1BChSpid_Type.__name__ = "DisplayString"
_DialerIsdnNI1BChSpid_Object = MibTableColumn
dialerIsdnNI1BChSpid = _DialerIsdnNI1BChSpid_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 2),
    _DialerIsdnNI1BChSpid_Type()
)
dialerIsdnNI1BChSpid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChSpid.setStatus("mandatory")
_DialerIsdnNI1BChSpidStatus_Type = IsdnSpidStatus
_DialerIsdnNI1BChSpidStatus_Object = MibTableColumn
dialerIsdnNI1BChSpidStatus = _DialerIsdnNI1BChSpidStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 3),
    _DialerIsdnNI1BChSpidStatus_Type()
)
dialerIsdnNI1BChSpidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChSpidStatus.setStatus("mandatory")


class _DialerIsdnNI1BChLocalDn_Type(DisplayString):
    """Custom type dialerIsdnNI1BChLocalDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnNI1BChLocalDn_Type.__name__ = "DisplayString"
_DialerIsdnNI1BChLocalDn_Object = MibTableColumn
dialerIsdnNI1BChLocalDn = _DialerIsdnNI1BChLocalDn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 4),
    _DialerIsdnNI1BChLocalDn_Type()
)
dialerIsdnNI1BChLocalDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChLocalDn.setStatus("mandatory")


class _DialerIsdnNI1BChLocalSub_Type(DisplayString):
    """Custom type dialerIsdnNI1BChLocalSub based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnNI1BChLocalSub_Type.__name__ = "DisplayString"
_DialerIsdnNI1BChLocalSub_Object = MibTableColumn
dialerIsdnNI1BChLocalSub = _DialerIsdnNI1BChLocalSub_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 5),
    _DialerIsdnNI1BChLocalSub_Type()
)
dialerIsdnNI1BChLocalSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChLocalSub.setStatus("mandatory")


class _DialerIsdnNI1BChTnsDigs_Type(DisplayString):
    """Custom type dialerIsdnNI1BChTnsDigs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DialerIsdnNI1BChTnsDigs_Type.__name__ = "DisplayString"
_DialerIsdnNI1BChTnsDigs_Object = MibTableColumn
dialerIsdnNI1BChTnsDigs = _DialerIsdnNI1BChTnsDigs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 6),
    _DialerIsdnNI1BChTnsDigs_Type()
)
dialerIsdnNI1BChTnsDigs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChTnsDigs.setStatus("mandatory")


class _DialerIsdnNI1BChRemoteDn_Type(DisplayString):
    """Custom type dialerIsdnNI1BChRemoteDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnNI1BChRemoteDn_Type.__name__ = "DisplayString"
_DialerIsdnNI1BChRemoteDn_Object = MibTableColumn
dialerIsdnNI1BChRemoteDn = _DialerIsdnNI1BChRemoteDn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 7),
    _DialerIsdnNI1BChRemoteDn_Type()
)
dialerIsdnNI1BChRemoteDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChRemoteDn.setStatus("mandatory")


class _DialerIsdnNI1BChRemoteSub_Type(DisplayString):
    """Custom type dialerIsdnNI1BChRemoteSub based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnNI1BChRemoteSub_Type.__name__ = "DisplayString"
_DialerIsdnNI1BChRemoteSub_Object = MibTableColumn
dialerIsdnNI1BChRemoteSub = _DialerIsdnNI1BChRemoteSub_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 8),
    _DialerIsdnNI1BChRemoteSub_Type()
)
dialerIsdnNI1BChRemoteSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChRemoteSub.setStatus("mandatory")
_DialerIsdnNI1BChCallType_Type = IsdnCallType
_DialerIsdnNI1BChCallType_Object = MibTableColumn
dialerIsdnNI1BChCallType = _DialerIsdnNI1BChCallType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 9),
    _DialerIsdnNI1BChCallType_Type()
)
dialerIsdnNI1BChCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChCallType.setStatus("mandatory")
_DialerIsdnNI1BChCallSpeed_Type = IsdnCallSpeed
_DialerIsdnNI1BChCallSpeed_Object = MibTableColumn
dialerIsdnNI1BChCallSpeed = _DialerIsdnNI1BChCallSpeed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 10),
    _DialerIsdnNI1BChCallSpeed_Type()
)
dialerIsdnNI1BChCallSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChCallSpeed.setStatus("mandatory")
_DialerIsdnNI1BChBChannel_Type = IsdnBChannels
_DialerIsdnNI1BChBChannel_Object = MibTableColumn
dialerIsdnNI1BChBChannel = _DialerIsdnNI1BChBChannel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 11),
    _DialerIsdnNI1BChBChannel_Type()
)
dialerIsdnNI1BChBChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChBChannel.setStatus("mandatory")
_DialerIsdnNI1BChAnsEnable_Type = IsdnAnsEnable
_DialerIsdnNI1BChAnsEnable_Object = MibTableColumn
dialerIsdnNI1BChAnsEnable = _DialerIsdnNI1BChAnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 12),
    _DialerIsdnNI1BChAnsEnable_Type()
)
dialerIsdnNI1BChAnsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChAnsEnable.setStatus("mandatory")
_DialerIsdnNI1BChCcState_Type = IsdnNI1BCcState
_DialerIsdnNI1BChCcState_Object = MibTableColumn
dialerIsdnNI1BChCcState = _DialerIsdnNI1BChCcState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 13),
    _DialerIsdnNI1BChCcState_Type()
)
dialerIsdnNI1BChCcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChCcState.setStatus("mandatory")
_DialerIsdnNI1BChCcNbCause_Type = Integer32
_DialerIsdnNI1BChCcNbCause_Object = MibTableColumn
dialerIsdnNI1BChCcNbCause = _DialerIsdnNI1BChCcNbCause_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 14),
    _DialerIsdnNI1BChCcNbCause_Type()
)
dialerIsdnNI1BChCcNbCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChCcNbCause.setStatus("mandatory")


class _DialerIsdnNI1BChCcCause_Type(OctetString):
    """Custom type dialerIsdnNI1BChCcCause based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DialerIsdnNI1BChCcCause_Type.__name__ = "OctetString"
_DialerIsdnNI1BChCcCause_Object = MibTableColumn
dialerIsdnNI1BChCcCause = _DialerIsdnNI1BChCcCause_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 15),
    _DialerIsdnNI1BChCcCause_Type()
)
dialerIsdnNI1BChCcCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChCcCause.setStatus("mandatory")
_DialerIsdnNI1BChL3State_Type = IsdnL3State
_DialerIsdnNI1BChL3State_Object = MibTableColumn
dialerIsdnNI1BChL3State = _DialerIsdnNI1BChL3State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 16),
    _DialerIsdnNI1BChL3State_Type()
)
dialerIsdnNI1BChL3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChL3State.setStatus("mandatory")
_DialerIsdnNI1BChL2State_Type = IsdnL2State
_DialerIsdnNI1BChL2State_Object = MibTableColumn
dialerIsdnNI1BChL2State = _DialerIsdnNI1BChL2State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 17),
    _DialerIsdnNI1BChL2State_Type()
)
dialerIsdnNI1BChL2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChL2State.setStatus("mandatory")
_DialerIsdnNI1BChTeiValue_Type = Integer32
_DialerIsdnNI1BChTeiValue_Object = MibTableColumn
dialerIsdnNI1BChTeiValue = _DialerIsdnNI1BChTeiValue_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 18),
    _DialerIsdnNI1BChTeiValue_Type()
)
dialerIsdnNI1BChTeiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChTeiValue.setStatus("mandatory")
_DialerIsdnNI1BChTeiStatus_Type = IsdnTeiStatus
_DialerIsdnNI1BChTeiStatus_Object = MibTableColumn
dialerIsdnNI1BChTeiStatus = _DialerIsdnNI1BChTeiStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 19),
    _DialerIsdnNI1BChTeiStatus_Type()
)
dialerIsdnNI1BChTeiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChTeiStatus.setStatus("mandatory")
_DialerIsdnNI1BChLocalDnType_Type = IsdnDnType
_DialerIsdnNI1BChLocalDnType_Object = MibTableColumn
dialerIsdnNI1BChLocalDnType = _DialerIsdnNI1BChLocalDnType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 20),
    _DialerIsdnNI1BChLocalDnType_Type()
)
dialerIsdnNI1BChLocalDnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChLocalDnType.setStatus("mandatory")
_DialerIsdnNI1BChLocalDnPlan_Type = IsdnDnPlan
_DialerIsdnNI1BChLocalDnPlan_Object = MibTableColumn
dialerIsdnNI1BChLocalDnPlan = _DialerIsdnNI1BChLocalDnPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 21),
    _DialerIsdnNI1BChLocalDnPlan_Type()
)
dialerIsdnNI1BChLocalDnPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChLocalDnPlan.setStatus("mandatory")
_DialerIsdnNI1BChLocalSubType_Type = IsdnSubType
_DialerIsdnNI1BChLocalSubType_Object = MibTableColumn
dialerIsdnNI1BChLocalSubType = _DialerIsdnNI1BChLocalSubType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 22),
    _DialerIsdnNI1BChLocalSubType_Type()
)
dialerIsdnNI1BChLocalSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChLocalSubType.setStatus("mandatory")
_DialerIsdnNI1BChTnsNetId_Type = IsdnTnsNetId
_DialerIsdnNI1BChTnsNetId_Object = MibTableColumn
dialerIsdnNI1BChTnsNetId = _DialerIsdnNI1BChTnsNetId_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 23),
    _DialerIsdnNI1BChTnsNetId_Type()
)
dialerIsdnNI1BChTnsNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChTnsNetId.setStatus("mandatory")
_DialerIsdnNI1BChTnsIdPlan_Type = IsdnTnsIdPlan
_DialerIsdnNI1BChTnsIdPlan_Object = MibTableColumn
dialerIsdnNI1BChTnsIdPlan = _DialerIsdnNI1BChTnsIdPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 24),
    _DialerIsdnNI1BChTnsIdPlan_Type()
)
dialerIsdnNI1BChTnsIdPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChTnsIdPlan.setStatus("mandatory")
_DialerIsdnNI1BChRemoteDnType_Type = IsdnDnType
_DialerIsdnNI1BChRemoteDnType_Object = MibTableColumn
dialerIsdnNI1BChRemoteDnType = _DialerIsdnNI1BChRemoteDnType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 25),
    _DialerIsdnNI1BChRemoteDnType_Type()
)
dialerIsdnNI1BChRemoteDnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChRemoteDnType.setStatus("mandatory")
_DialerIsdnNI1BChRemoteDnPlan_Type = IsdnDnPlan
_DialerIsdnNI1BChRemoteDnPlan_Object = MibTableColumn
dialerIsdnNI1BChRemoteDnPlan = _DialerIsdnNI1BChRemoteDnPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 26),
    _DialerIsdnNI1BChRemoteDnPlan_Type()
)
dialerIsdnNI1BChRemoteDnPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChRemoteDnPlan.setStatus("mandatory")
_DialerIsdnNI1BChRemoteSubType_Type = IsdnSubType
_DialerIsdnNI1BChRemoteSubType_Object = MibTableColumn
dialerIsdnNI1BChRemoteSubType = _DialerIsdnNI1BChRemoteSubType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 27),
    _DialerIsdnNI1BChRemoteSubType_Type()
)
dialerIsdnNI1BChRemoteSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChRemoteSubType.setStatus("mandatory")
_DialerIsdnNI1BChScrStatus_Type = IsdnScrStatus
_DialerIsdnNI1BChScrStatus_Object = MibTableColumn
dialerIsdnNI1BChScrStatus = _DialerIsdnNI1BChScrStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 28),
    _DialerIsdnNI1BChScrStatus_Type()
)
dialerIsdnNI1BChScrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChScrStatus.setStatus("mandatory")
_DialerIsdnNI1BChCallOpt_Type = IsdnCallOpt
_DialerIsdnNI1BChCallOpt_Object = MibTableColumn
dialerIsdnNI1BChCallOpt = _DialerIsdnNI1BChCallOpt_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 29),
    _DialerIsdnNI1BChCallOpt_Type()
)
dialerIsdnNI1BChCallOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChCallOpt.setStatus("mandatory")
_DialerIsdnNI1BChStoDefined_Type = IsdnStoDefined
_DialerIsdnNI1BChStoDefined_Object = MibTableColumn
dialerIsdnNI1BChStoDefined = _DialerIsdnNI1BChStoDefined_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 30),
    _DialerIsdnNI1BChStoDefined_Type()
)
dialerIsdnNI1BChStoDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChStoDefined.setStatus("mandatory")
_DialerIsdnNI1BChStoDnType_Type = Integer32
_DialerIsdnNI1BChStoDnType_Object = MibTableColumn
dialerIsdnNI1BChStoDnType = _DialerIsdnNI1BChStoDnType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 31),
    _DialerIsdnNI1BChStoDnType_Type()
)
dialerIsdnNI1BChStoDnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChStoDnType.setStatus("mandatory")
_DialerIsdnNI1BChStoDnPlan_Type = Integer32
_DialerIsdnNI1BChStoDnPlan_Object = MibTableColumn
dialerIsdnNI1BChStoDnPlan = _DialerIsdnNI1BChStoDnPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 32),
    _DialerIsdnNI1BChStoDnPlan_Type()
)
dialerIsdnNI1BChStoDnPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChStoDnPlan.setStatus("mandatory")


class _DialerIsdnNI1BChStoDn_Type(DisplayString):
    """Custom type dialerIsdnNI1BChStoDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnNI1BChStoDn_Type.__name__ = "DisplayString"
_DialerIsdnNI1BChStoDn_Object = MibTableColumn
dialerIsdnNI1BChStoDn = _DialerIsdnNI1BChStoDn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 33),
    _DialerIsdnNI1BChStoDn_Type()
)
dialerIsdnNI1BChStoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChStoDn.setStatus("mandatory")
_DialerIsdnNI1BChStoSubType_Type = Integer32
_DialerIsdnNI1BChStoSubType_Object = MibTableColumn
dialerIsdnNI1BChStoSubType = _DialerIsdnNI1BChStoSubType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 34),
    _DialerIsdnNI1BChStoSubType_Type()
)
dialerIsdnNI1BChStoSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChStoSubType.setStatus("mandatory")


class _DialerIsdnNI1BChStoSub_Type(DisplayString):
    """Custom type dialerIsdnNI1BChStoSub based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnNI1BChStoSub_Type.__name__ = "DisplayString"
_DialerIsdnNI1BChStoSub_Object = MibTableColumn
dialerIsdnNI1BChStoSub = _DialerIsdnNI1BChStoSub_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 35),
    _DialerIsdnNI1BChStoSub_Type()
)
dialerIsdnNI1BChStoSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChStoSub.setStatus("mandatory")
_DialerIsdnNI1BChStoTnsNetId_Type = Integer32
_DialerIsdnNI1BChStoTnsNetId_Object = MibTableColumn
dialerIsdnNI1BChStoTnsNetId = _DialerIsdnNI1BChStoTnsNetId_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 36),
    _DialerIsdnNI1BChStoTnsNetId_Type()
)
dialerIsdnNI1BChStoTnsNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChStoTnsNetId.setStatus("mandatory")
_DialerIsdnNI1BChStoTnsPlan_Type = Integer32
_DialerIsdnNI1BChStoTnsPlan_Object = MibTableColumn
dialerIsdnNI1BChStoTnsPlan = _DialerIsdnNI1BChStoTnsPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 37),
    _DialerIsdnNI1BChStoTnsPlan_Type()
)
dialerIsdnNI1BChStoTnsPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChStoTnsPlan.setStatus("mandatory")


class _DialerIsdnNI1BChStoDigs_Type(DisplayString):
    """Custom type dialerIsdnNI1BChStoDigs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DialerIsdnNI1BChStoDigs_Type.__name__ = "DisplayString"
_DialerIsdnNI1BChStoDigs_Object = MibTableColumn
dialerIsdnNI1BChStoDigs = _DialerIsdnNI1BChStoDigs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 38),
    _DialerIsdnNI1BChStoDigs_Type()
)
dialerIsdnNI1BChStoDigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChStoDigs.setStatus("mandatory")
_DialerIsdnNI1BChStoBcType_Type = Integer32
_DialerIsdnNI1BChStoBcType_Object = MibTableColumn
dialerIsdnNI1BChStoBcType = _DialerIsdnNI1BChStoBcType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 39),
    _DialerIsdnNI1BChStoBcType_Type()
)
dialerIsdnNI1BChStoBcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChStoBcType.setStatus("mandatory")
_DialerIsdnNI1BChStoBcOpt_Type = Integer32
_DialerIsdnNI1BChStoBcOpt_Object = MibTableColumn
dialerIsdnNI1BChStoBcOpt = _DialerIsdnNI1BChStoBcOpt_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 12, 1, 40),
    _DialerIsdnNI1BChStoBcOpt_Type()
)
dialerIsdnNI1BChStoBcOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1BChStoBcOpt.setStatus("mandatory")
_DialerIsdnNI1DChTable_Object = MibTable
dialerIsdnNI1DChTable = _DialerIsdnNI1DChTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 13)
)
if mibBuilder.loadTexts:
    dialerIsdnNI1DChTable.setStatus("mandatory")
_DialerIsdnNI1DChEntry_Object = MibTableRow
dialerIsdnNI1DChEntry = _DialerIsdnNI1DChEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 13, 1)
)
dialerIsdnNI1DChEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerIsdnNI1DChPortRef"),
)
if mibBuilder.loadTexts:
    dialerIsdnNI1DChEntry.setStatus("mandatory")
_DialerIsdnNI1DChPortRef_Type = PortRef
_DialerIsdnNI1DChPortRef_Object = MibTableColumn
dialerIsdnNI1DChPortRef = _DialerIsdnNI1DChPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 13, 1, 1),
    _DialerIsdnNI1DChPortRef_Type()
)
dialerIsdnNI1DChPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1DChPortRef.setStatus("mandatory")
_DialerIsdnNI1DChTeiValue_Type = Integer32
_DialerIsdnNI1DChTeiValue_Object = MibTableColumn
dialerIsdnNI1DChTeiValue = _DialerIsdnNI1DChTeiValue_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 13, 1, 2),
    _DialerIsdnNI1DChTeiValue_Type()
)
dialerIsdnNI1DChTeiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1DChTeiValue.setStatus("mandatory")
_DialerIsdnNI1DChTeiStatus_Type = IsdnTeiStatus
_DialerIsdnNI1DChTeiStatus_Object = MibTableColumn
dialerIsdnNI1DChTeiStatus = _DialerIsdnNI1DChTeiStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 13, 1, 3),
    _DialerIsdnNI1DChTeiStatus_Type()
)
dialerIsdnNI1DChTeiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1DChTeiStatus.setStatus("mandatory")
_DialerIsdnNI1DChL2State_Type = IsdnL2State
_DialerIsdnNI1DChL2State_Object = MibTableColumn
dialerIsdnNI1DChL2State = _DialerIsdnNI1DChL2State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 13, 1, 4),
    _DialerIsdnNI1DChL2State_Type()
)
dialerIsdnNI1DChL2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1DChL2State.setStatus("mandatory")
_DialerIsdnNI1DChP3State_Type = IsdnP3State
_DialerIsdnNI1DChP3State_Object = MibTableColumn
dialerIsdnNI1DChP3State = _DialerIsdnNI1DChP3State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 13, 1, 5),
    _DialerIsdnNI1DChP3State_Type()
)
dialerIsdnNI1DChP3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1DChP3State.setStatus("mandatory")
_DialerIsdnNI1DChActState_Type = IsdnActState
_DialerIsdnNI1DChActState_Object = MibTableColumn
dialerIsdnNI1DChActState = _DialerIsdnNI1DChActState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 13, 1, 6),
    _DialerIsdnNI1DChActState_Type()
)
dialerIsdnNI1DChActState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNI1DChActState.setStatus("mandatory")
_DialerIsdnTR6BChTable_Object = MibTable
dialerIsdnTR6BChTable = _DialerIsdnTR6BChTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14)
)
if mibBuilder.loadTexts:
    dialerIsdnTR6BChTable.setStatus("mandatory")
_DialerIsdnTR6BChEntry_Object = MibTableRow
dialerIsdnTR6BChEntry = _DialerIsdnTR6BChEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1)
)
dialerIsdnTR6BChEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerIsdnTR6BChPortRef"),
)
if mibBuilder.loadTexts:
    dialerIsdnTR6BChEntry.setStatus("mandatory")
_DialerIsdnTR6BChPortRef_Type = PortRef
_DialerIsdnTR6BChPortRef_Object = MibTableColumn
dialerIsdnTR6BChPortRef = _DialerIsdnTR6BChPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 1),
    _DialerIsdnTR6BChPortRef_Type()
)
dialerIsdnTR6BChPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChPortRef.setStatus("mandatory")


class _DialerIsdnTR6BChLocalDn_Type(DisplayString):
    """Custom type dialerIsdnTR6BChLocalDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnTR6BChLocalDn_Type.__name__ = "DisplayString"
_DialerIsdnTR6BChLocalDn_Object = MibTableColumn
dialerIsdnTR6BChLocalDn = _DialerIsdnTR6BChLocalDn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 2),
    _DialerIsdnTR6BChLocalDn_Type()
)
dialerIsdnTR6BChLocalDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChLocalDn.setStatus("mandatory")


class _DialerIsdnTR6BChRemoteDn_Type(DisplayString):
    """Custom type dialerIsdnTR6BChRemoteDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnTR6BChRemoteDn_Type.__name__ = "DisplayString"
_DialerIsdnTR6BChRemoteDn_Object = MibTableColumn
dialerIsdnTR6BChRemoteDn = _DialerIsdnTR6BChRemoteDn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 3),
    _DialerIsdnTR6BChRemoteDn_Type()
)
dialerIsdnTR6BChRemoteDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChRemoteDn.setStatus("mandatory")
_DialerIsdnTR6BChCallType_Type = IsdnCallType
_DialerIsdnTR6BChCallType_Object = MibTableColumn
dialerIsdnTR6BChCallType = _DialerIsdnTR6BChCallType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 4),
    _DialerIsdnTR6BChCallType_Type()
)
dialerIsdnTR6BChCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChCallType.setStatus("mandatory")
_DialerIsdnTR6BChCallSpeed_Type = IsdnCallSpeed
_DialerIsdnTR6BChCallSpeed_Object = MibTableColumn
dialerIsdnTR6BChCallSpeed = _DialerIsdnTR6BChCallSpeed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 5),
    _DialerIsdnTR6BChCallSpeed_Type()
)
dialerIsdnTR6BChCallSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChCallSpeed.setStatus("mandatory")
_DialerIsdnTR6BChBChannel_Type = IsdnBChannels
_DialerIsdnTR6BChBChannel_Object = MibTableColumn
dialerIsdnTR6BChBChannel = _DialerIsdnTR6BChBChannel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 6),
    _DialerIsdnTR6BChBChannel_Type()
)
dialerIsdnTR6BChBChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChBChannel.setStatus("mandatory")
_DialerIsdnTR6BChAnsEnable_Type = IsdnAnsEnable
_DialerIsdnTR6BChAnsEnable_Object = MibTableColumn
dialerIsdnTR6BChAnsEnable = _DialerIsdnTR6BChAnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 7),
    _DialerIsdnTR6BChAnsEnable_Type()
)
dialerIsdnTR6BChAnsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChAnsEnable.setStatus("mandatory")
_DialerIsdnTR6BChCcState_Type = IsdnTR6BCcState
_DialerIsdnTR6BChCcState_Object = MibTableColumn
dialerIsdnTR6BChCcState = _DialerIsdnTR6BChCcState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 8),
    _DialerIsdnTR6BChCcState_Type()
)
dialerIsdnTR6BChCcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChCcState.setStatus("mandatory")
_DialerIsdnTR6BChCcNbCause_Type = Integer32
_DialerIsdnTR6BChCcNbCause_Object = MibTableColumn
dialerIsdnTR6BChCcNbCause = _DialerIsdnTR6BChCcNbCause_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 9),
    _DialerIsdnTR6BChCcNbCause_Type()
)
dialerIsdnTR6BChCcNbCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChCcNbCause.setStatus("mandatory")


class _DialerIsdnTR6BChCcCause_Type(OctetString):
    """Custom type dialerIsdnTR6BChCcCause based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DialerIsdnTR6BChCcCause_Type.__name__ = "OctetString"
_DialerIsdnTR6BChCcCause_Object = MibTableColumn
dialerIsdnTR6BChCcCause = _DialerIsdnTR6BChCcCause_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 10),
    _DialerIsdnTR6BChCcCause_Type()
)
dialerIsdnTR6BChCcCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChCcCause.setStatus("mandatory")
_DialerIsdnTR6BChL3State_Type = IsdnL3State
_DialerIsdnTR6BChL3State_Object = MibTableColumn
dialerIsdnTR6BChL3State = _DialerIsdnTR6BChL3State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 11),
    _DialerIsdnTR6BChL3State_Type()
)
dialerIsdnTR6BChL3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChL3State.setStatus("mandatory")
_DialerIsdnTR6BChL2State_Type = IsdnL2State
_DialerIsdnTR6BChL2State_Object = MibTableColumn
dialerIsdnTR6BChL2State = _DialerIsdnTR6BChL2State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 12),
    _DialerIsdnTR6BChL2State_Type()
)
dialerIsdnTR6BChL2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChL2State.setStatus("mandatory")
_DialerIsdnTR6BChLocalDnType_Type = IsdnDnType
_DialerIsdnTR6BChLocalDnType_Object = MibTableColumn
dialerIsdnTR6BChLocalDnType = _DialerIsdnTR6BChLocalDnType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 13),
    _DialerIsdnTR6BChLocalDnType_Type()
)
dialerIsdnTR6BChLocalDnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChLocalDnType.setStatus("mandatory")
_DialerIsdnTR6BChLocalDnPlan_Type = IsdnDnPlan
_DialerIsdnTR6BChLocalDnPlan_Object = MibTableColumn
dialerIsdnTR6BChLocalDnPlan = _DialerIsdnTR6BChLocalDnPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 14),
    _DialerIsdnTR6BChLocalDnPlan_Type()
)
dialerIsdnTR6BChLocalDnPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChLocalDnPlan.setStatus("mandatory")
_DialerIsdnTR6BChRemoteDnType_Type = IsdnDnType
_DialerIsdnTR6BChRemoteDnType_Object = MibTableColumn
dialerIsdnTR6BChRemoteDnType = _DialerIsdnTR6BChRemoteDnType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 15),
    _DialerIsdnTR6BChRemoteDnType_Type()
)
dialerIsdnTR6BChRemoteDnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChRemoteDnType.setStatus("mandatory")
_DialerIsdnTR6BChRemoteDnPlan_Type = IsdnDnPlan
_DialerIsdnTR6BChRemoteDnPlan_Object = MibTableColumn
dialerIsdnTR6BChRemoteDnPlan = _DialerIsdnTR6BChRemoteDnPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 16),
    _DialerIsdnTR6BChRemoteDnPlan_Type()
)
dialerIsdnTR6BChRemoteDnPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChRemoteDnPlan.setStatus("mandatory")
_DialerIsdnTR6BChScrStatus_Type = IsdnScrStatus
_DialerIsdnTR6BChScrStatus_Object = MibTableColumn
dialerIsdnTR6BChScrStatus = _DialerIsdnTR6BChScrStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 17),
    _DialerIsdnTR6BChScrStatus_Type()
)
dialerIsdnTR6BChScrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChScrStatus.setStatus("mandatory")
_DialerIsdnTR6BChCallOpt_Type = IsdnCallOpt
_DialerIsdnTR6BChCallOpt_Object = MibTableColumn
dialerIsdnTR6BChCallOpt = _DialerIsdnTR6BChCallOpt_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 18),
    _DialerIsdnTR6BChCallOpt_Type()
)
dialerIsdnTR6BChCallOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChCallOpt.setStatus("mandatory")
_DialerIsdnTR6BChTeiValue_Type = Integer32
_DialerIsdnTR6BChTeiValue_Object = MibTableColumn
dialerIsdnTR6BChTeiValue = _DialerIsdnTR6BChTeiValue_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 19),
    _DialerIsdnTR6BChTeiValue_Type()
)
dialerIsdnTR6BChTeiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChTeiValue.setStatus("mandatory")
_DialerIsdnTR6BChTeiStatus_Type = IsdnTeiStatus
_DialerIsdnTR6BChTeiStatus_Object = MibTableColumn
dialerIsdnTR6BChTeiStatus = _DialerIsdnTR6BChTeiStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 20),
    _DialerIsdnTR6BChTeiStatus_Type()
)
dialerIsdnTR6BChTeiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChTeiStatus.setStatus("mandatory")
_DialerIsdnTR6BChStoDefined_Type = IsdnStoDefined
_DialerIsdnTR6BChStoDefined_Object = MibTableColumn
dialerIsdnTR6BChStoDefined = _DialerIsdnTR6BChStoDefined_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 21),
    _DialerIsdnTR6BChStoDefined_Type()
)
dialerIsdnTR6BChStoDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChStoDefined.setStatus("mandatory")
_DialerIsdnTR6BChStoDnType_Type = Integer32
_DialerIsdnTR6BChStoDnType_Object = MibTableColumn
dialerIsdnTR6BChStoDnType = _DialerIsdnTR6BChStoDnType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 22),
    _DialerIsdnTR6BChStoDnType_Type()
)
dialerIsdnTR6BChStoDnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChStoDnType.setStatus("mandatory")
_DialerIsdnTR6BChStoDnPlan_Type = Integer32
_DialerIsdnTR6BChStoDnPlan_Object = MibTableColumn
dialerIsdnTR6BChStoDnPlan = _DialerIsdnTR6BChStoDnPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 23),
    _DialerIsdnTR6BChStoDnPlan_Type()
)
dialerIsdnTR6BChStoDnPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChStoDnPlan.setStatus("mandatory")


class _DialerIsdnTR6BChStoDn_Type(DisplayString):
    """Custom type dialerIsdnTR6BChStoDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnTR6BChStoDn_Type.__name__ = "DisplayString"
_DialerIsdnTR6BChStoDn_Object = MibTableColumn
dialerIsdnTR6BChStoDn = _DialerIsdnTR6BChStoDn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 24),
    _DialerIsdnTR6BChStoDn_Type()
)
dialerIsdnTR6BChStoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChStoDn.setStatus("mandatory")
_DialerIsdnTR6BChStoBcType_Type = Integer32
_DialerIsdnTR6BChStoBcType_Object = MibTableColumn
dialerIsdnTR6BChStoBcType = _DialerIsdnTR6BChStoBcType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 25),
    _DialerIsdnTR6BChStoBcType_Type()
)
dialerIsdnTR6BChStoBcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChStoBcType.setStatus("mandatory")
_DialerIsdnTR6BChStoBcOpt_Type = Integer32
_DialerIsdnTR6BChStoBcOpt_Object = MibTableColumn
dialerIsdnTR6BChStoBcOpt = _DialerIsdnTR6BChStoBcOpt_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 14, 1, 26),
    _DialerIsdnTR6BChStoBcOpt_Type()
)
dialerIsdnTR6BChStoBcOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTR6BChStoBcOpt.setStatus("mandatory")
_DialerIsdnVN3BChTable_Object = MibTable
dialerIsdnVN3BChTable = _DialerIsdnVN3BChTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15)
)
if mibBuilder.loadTexts:
    dialerIsdnVN3BChTable.setStatus("mandatory")
_DialerIsdnVN3BChEntry_Object = MibTableRow
dialerIsdnVN3BChEntry = _DialerIsdnVN3BChEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1)
)
dialerIsdnVN3BChEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerIsdnVN3BChPortRef"),
)
if mibBuilder.loadTexts:
    dialerIsdnVN3BChEntry.setStatus("mandatory")
_DialerIsdnVN3BChPortRef_Type = PortRef
_DialerIsdnVN3BChPortRef_Object = MibTableColumn
dialerIsdnVN3BChPortRef = _DialerIsdnVN3BChPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 1),
    _DialerIsdnVN3BChPortRef_Type()
)
dialerIsdnVN3BChPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChPortRef.setStatus("mandatory")
_DialerIsdnVN3BChLocalDnType_Type = IsdnDnType
_DialerIsdnVN3BChLocalDnType_Object = MibTableColumn
dialerIsdnVN3BChLocalDnType = _DialerIsdnVN3BChLocalDnType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 2),
    _DialerIsdnVN3BChLocalDnType_Type()
)
dialerIsdnVN3BChLocalDnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChLocalDnType.setStatus("mandatory")
_DialerIsdnVN3BChLocalDnPlan_Type = IsdnDnPlan
_DialerIsdnVN3BChLocalDnPlan_Object = MibTableColumn
dialerIsdnVN3BChLocalDnPlan = _DialerIsdnVN3BChLocalDnPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 3),
    _DialerIsdnVN3BChLocalDnPlan_Type()
)
dialerIsdnVN3BChLocalDnPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChLocalDnPlan.setStatus("mandatory")


class _DialerIsdnVN3BChLocalDn_Type(DisplayString):
    """Custom type dialerIsdnVN3BChLocalDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnVN3BChLocalDn_Type.__name__ = "DisplayString"
_DialerIsdnVN3BChLocalDn_Object = MibTableColumn
dialerIsdnVN3BChLocalDn = _DialerIsdnVN3BChLocalDn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 4),
    _DialerIsdnVN3BChLocalDn_Type()
)
dialerIsdnVN3BChLocalDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChLocalDn.setStatus("mandatory")
_DialerIsdnVN3BChLocalSubType_Type = IsdnSubType
_DialerIsdnVN3BChLocalSubType_Object = MibTableColumn
dialerIsdnVN3BChLocalSubType = _DialerIsdnVN3BChLocalSubType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 5),
    _DialerIsdnVN3BChLocalSubType_Type()
)
dialerIsdnVN3BChLocalSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChLocalSubType.setStatus("mandatory")


class _DialerIsdnVN3BChLocalSub_Type(DisplayString):
    """Custom type dialerIsdnVN3BChLocalSub based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnVN3BChLocalSub_Type.__name__ = "DisplayString"
_DialerIsdnVN3BChLocalSub_Object = MibTableColumn
dialerIsdnVN3BChLocalSub = _DialerIsdnVN3BChLocalSub_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 6),
    _DialerIsdnVN3BChLocalSub_Type()
)
dialerIsdnVN3BChLocalSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChLocalSub.setStatus("mandatory")
_DialerIsdnVN3BChRemoteDnType_Type = IsdnDnType
_DialerIsdnVN3BChRemoteDnType_Object = MibTableColumn
dialerIsdnVN3BChRemoteDnType = _DialerIsdnVN3BChRemoteDnType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 7),
    _DialerIsdnVN3BChRemoteDnType_Type()
)
dialerIsdnVN3BChRemoteDnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChRemoteDnType.setStatus("mandatory")
_DialerIsdnVN3BChRemoteDnPlan_Type = IsdnDnPlan
_DialerIsdnVN3BChRemoteDnPlan_Object = MibTableColumn
dialerIsdnVN3BChRemoteDnPlan = _DialerIsdnVN3BChRemoteDnPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 8),
    _DialerIsdnVN3BChRemoteDnPlan_Type()
)
dialerIsdnVN3BChRemoteDnPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChRemoteDnPlan.setStatus("mandatory")


class _DialerIsdnVN3BChRemoteDn_Type(DisplayString):
    """Custom type dialerIsdnVN3BChRemoteDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnVN3BChRemoteDn_Type.__name__ = "DisplayString"
_DialerIsdnVN3BChRemoteDn_Object = MibTableColumn
dialerIsdnVN3BChRemoteDn = _DialerIsdnVN3BChRemoteDn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 9),
    _DialerIsdnVN3BChRemoteDn_Type()
)
dialerIsdnVN3BChRemoteDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChRemoteDn.setStatus("mandatory")
_DialerIsdnVN3BChRemoteSubType_Type = IsdnSubType
_DialerIsdnVN3BChRemoteSubType_Object = MibTableColumn
dialerIsdnVN3BChRemoteSubType = _DialerIsdnVN3BChRemoteSubType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 10),
    _DialerIsdnVN3BChRemoteSubType_Type()
)
dialerIsdnVN3BChRemoteSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChRemoteSubType.setStatus("mandatory")


class _DialerIsdnVN3BChRemoteSub_Type(DisplayString):
    """Custom type dialerIsdnVN3BChRemoteSub based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnVN3BChRemoteSub_Type.__name__ = "DisplayString"
_DialerIsdnVN3BChRemoteSub_Object = MibTableColumn
dialerIsdnVN3BChRemoteSub = _DialerIsdnVN3BChRemoteSub_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 11),
    _DialerIsdnVN3BChRemoteSub_Type()
)
dialerIsdnVN3BChRemoteSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChRemoteSub.setStatus("mandatory")
_DialerIsdnVN3BChCallType_Type = IsdnCallType
_DialerIsdnVN3BChCallType_Object = MibTableColumn
dialerIsdnVN3BChCallType = _DialerIsdnVN3BChCallType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 12),
    _DialerIsdnVN3BChCallType_Type()
)
dialerIsdnVN3BChCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChCallType.setStatus("mandatory")
_DialerIsdnVN3BChCallSpeed_Type = IsdnCallSpeed
_DialerIsdnVN3BChCallSpeed_Object = MibTableColumn
dialerIsdnVN3BChCallSpeed = _DialerIsdnVN3BChCallSpeed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 13),
    _DialerIsdnVN3BChCallSpeed_Type()
)
dialerIsdnVN3BChCallSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChCallSpeed.setStatus("mandatory")
_DialerIsdnVN3BChBChannel_Type = IsdnBChannels
_DialerIsdnVN3BChBChannel_Object = MibTableColumn
dialerIsdnVN3BChBChannel = _DialerIsdnVN3BChBChannel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 14),
    _DialerIsdnVN3BChBChannel_Type()
)
dialerIsdnVN3BChBChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChBChannel.setStatus("mandatory")
_DialerIsdnVN3BChAnsEnable_Type = IsdnAnsEnable
_DialerIsdnVN3BChAnsEnable_Object = MibTableColumn
dialerIsdnVN3BChAnsEnable = _DialerIsdnVN3BChAnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 15),
    _DialerIsdnVN3BChAnsEnable_Type()
)
dialerIsdnVN3BChAnsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChAnsEnable.setStatus("mandatory")
_DialerIsdnVN3BChScrStatus_Type = IsdnScrStatus
_DialerIsdnVN3BChScrStatus_Object = MibTableColumn
dialerIsdnVN3BChScrStatus = _DialerIsdnVN3BChScrStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 16),
    _DialerIsdnVN3BChScrStatus_Type()
)
dialerIsdnVN3BChScrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChScrStatus.setStatus("mandatory")
_DialerIsdnVN3BChCallOpt_Type = IsdnCallOpt
_DialerIsdnVN3BChCallOpt_Object = MibTableColumn
dialerIsdnVN3BChCallOpt = _DialerIsdnVN3BChCallOpt_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 17),
    _DialerIsdnVN3BChCallOpt_Type()
)
dialerIsdnVN3BChCallOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChCallOpt.setStatus("mandatory")
_DialerIsdnVN3BChCcState_Type = IsdnVN3BCcState
_DialerIsdnVN3BChCcState_Object = MibTableColumn
dialerIsdnVN3BChCcState = _DialerIsdnVN3BChCcState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 18),
    _DialerIsdnVN3BChCcState_Type()
)
dialerIsdnVN3BChCcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChCcState.setStatus("mandatory")
_DialerIsdnVN3BChCcNbCause_Type = Integer32
_DialerIsdnVN3BChCcNbCause_Object = MibTableColumn
dialerIsdnVN3BChCcNbCause = _DialerIsdnVN3BChCcNbCause_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 19),
    _DialerIsdnVN3BChCcNbCause_Type()
)
dialerIsdnVN3BChCcNbCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChCcNbCause.setStatus("mandatory")


class _DialerIsdnVN3BChCcCause_Type(OctetString):
    """Custom type dialerIsdnVN3BChCcCause based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DialerIsdnVN3BChCcCause_Type.__name__ = "OctetString"
_DialerIsdnVN3BChCcCause_Object = MibTableColumn
dialerIsdnVN3BChCcCause = _DialerIsdnVN3BChCcCause_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 20),
    _DialerIsdnVN3BChCcCause_Type()
)
dialerIsdnVN3BChCcCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChCcCause.setStatus("mandatory")
_DialerIsdnVN3BChL3State_Type = IsdnL3State
_DialerIsdnVN3BChL3State_Object = MibTableColumn
dialerIsdnVN3BChL3State = _DialerIsdnVN3BChL3State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 21),
    _DialerIsdnVN3BChL3State_Type()
)
dialerIsdnVN3BChL3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChL3State.setStatus("mandatory")
_DialerIsdnVN3BChL2State_Type = IsdnL2State
_DialerIsdnVN3BChL2State_Object = MibTableColumn
dialerIsdnVN3BChL2State = _DialerIsdnVN3BChL2State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 22),
    _DialerIsdnVN3BChL2State_Type()
)
dialerIsdnVN3BChL2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChL2State.setStatus("mandatory")
_DialerIsdnVN3BChTeiValue_Type = Integer32
_DialerIsdnVN3BChTeiValue_Object = MibTableColumn
dialerIsdnVN3BChTeiValue = _DialerIsdnVN3BChTeiValue_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 23),
    _DialerIsdnVN3BChTeiValue_Type()
)
dialerIsdnVN3BChTeiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChTeiValue.setStatus("mandatory")
_DialerIsdnVN3BChTeiStatus_Type = IsdnTeiStatus
_DialerIsdnVN3BChTeiStatus_Object = MibTableColumn
dialerIsdnVN3BChTeiStatus = _DialerIsdnVN3BChTeiStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 24),
    _DialerIsdnVN3BChTeiStatus_Type()
)
dialerIsdnVN3BChTeiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChTeiStatus.setStatus("mandatory")
_DialerIsdnVN3BChStoDefined_Type = IsdnStoDefined
_DialerIsdnVN3BChStoDefined_Object = MibTableColumn
dialerIsdnVN3BChStoDefined = _DialerIsdnVN3BChStoDefined_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 25),
    _DialerIsdnVN3BChStoDefined_Type()
)
dialerIsdnVN3BChStoDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChStoDefined.setStatus("mandatory")
_DialerIsdnVN3BChStoDnType_Type = Integer32
_DialerIsdnVN3BChStoDnType_Object = MibTableColumn
dialerIsdnVN3BChStoDnType = _DialerIsdnVN3BChStoDnType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 26),
    _DialerIsdnVN3BChStoDnType_Type()
)
dialerIsdnVN3BChStoDnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChStoDnType.setStatus("mandatory")
_DialerIsdnVN3BChStoDnPlan_Type = Integer32
_DialerIsdnVN3BChStoDnPlan_Object = MibTableColumn
dialerIsdnVN3BChStoDnPlan = _DialerIsdnVN3BChStoDnPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 27),
    _DialerIsdnVN3BChStoDnPlan_Type()
)
dialerIsdnVN3BChStoDnPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChStoDnPlan.setStatus("mandatory")


class _DialerIsdnVN3BChStoDn_Type(DisplayString):
    """Custom type dialerIsdnVN3BChStoDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnVN3BChStoDn_Type.__name__ = "DisplayString"
_DialerIsdnVN3BChStoDn_Object = MibTableColumn
dialerIsdnVN3BChStoDn = _DialerIsdnVN3BChStoDn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 28),
    _DialerIsdnVN3BChStoDn_Type()
)
dialerIsdnVN3BChStoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChStoDn.setStatus("mandatory")
_DialerIsdnVN3BChStoSubType_Type = Integer32
_DialerIsdnVN3BChStoSubType_Object = MibTableColumn
dialerIsdnVN3BChStoSubType = _DialerIsdnVN3BChStoSubType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 29),
    _DialerIsdnVN3BChStoSubType_Type()
)
dialerIsdnVN3BChStoSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChStoSubType.setStatus("mandatory")


class _DialerIsdnVN3BChStoSub_Type(DisplayString):
    """Custom type dialerIsdnVN3BChStoSub based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnVN3BChStoSub_Type.__name__ = "DisplayString"
_DialerIsdnVN3BChStoSub_Object = MibTableColumn
dialerIsdnVN3BChStoSub = _DialerIsdnVN3BChStoSub_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 30),
    _DialerIsdnVN3BChStoSub_Type()
)
dialerIsdnVN3BChStoSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChStoSub.setStatus("mandatory")
_DialerIsdnVN3BChStoBcType_Type = Integer32
_DialerIsdnVN3BChStoBcType_Object = MibTableColumn
dialerIsdnVN3BChStoBcType = _DialerIsdnVN3BChStoBcType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 31),
    _DialerIsdnVN3BChStoBcType_Type()
)
dialerIsdnVN3BChStoBcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChStoBcType.setStatus("mandatory")
_DialerIsdnVN3BChStoBcOpt_Type = Integer32
_DialerIsdnVN3BChStoBcOpt_Object = MibTableColumn
dialerIsdnVN3BChStoBcOpt = _DialerIsdnVN3BChStoBcOpt_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 15, 1, 32),
    _DialerIsdnVN3BChStoBcOpt_Type()
)
dialerIsdnVN3BChStoBcOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3BChStoBcOpt.setStatus("mandatory")
_DialerIsdnVN3DChTable_Object = MibTable
dialerIsdnVN3DChTable = _DialerIsdnVN3DChTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 16)
)
if mibBuilder.loadTexts:
    dialerIsdnVN3DChTable.setStatus("mandatory")
_DialerIsdnVN3DChEntry_Object = MibTableRow
dialerIsdnVN3DChEntry = _DialerIsdnVN3DChEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 16, 1)
)
dialerIsdnVN3DChEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerIsdnVN3DChPortRef"),
)
if mibBuilder.loadTexts:
    dialerIsdnVN3DChEntry.setStatus("mandatory")
_DialerIsdnVN3DChPortRef_Type = PortRef
_DialerIsdnVN3DChPortRef_Object = MibTableColumn
dialerIsdnVN3DChPortRef = _DialerIsdnVN3DChPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 16, 1, 1),
    _DialerIsdnVN3DChPortRef_Type()
)
dialerIsdnVN3DChPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3DChPortRef.setStatus("mandatory")
_DialerIsdnVN3DChTeiValue_Type = Integer32
_DialerIsdnVN3DChTeiValue_Object = MibTableColumn
dialerIsdnVN3DChTeiValue = _DialerIsdnVN3DChTeiValue_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 16, 1, 2),
    _DialerIsdnVN3DChTeiValue_Type()
)
dialerIsdnVN3DChTeiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3DChTeiValue.setStatus("mandatory")
_DialerIsdnVN3DChTeiStatus_Type = IsdnTeiStatus
_DialerIsdnVN3DChTeiStatus_Object = MibTableColumn
dialerIsdnVN3DChTeiStatus = _DialerIsdnVN3DChTeiStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 16, 1, 3),
    _DialerIsdnVN3DChTeiStatus_Type()
)
dialerIsdnVN3DChTeiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3DChTeiStatus.setStatus("mandatory")
_DialerIsdnVN3DChL2State_Type = IsdnL2State
_DialerIsdnVN3DChL2State_Object = MibTableColumn
dialerIsdnVN3DChL2State = _DialerIsdnVN3DChL2State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 16, 1, 4),
    _DialerIsdnVN3DChL2State_Type()
)
dialerIsdnVN3DChL2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3DChL2State.setStatus("mandatory")
_DialerIsdnVN3DChP3State_Type = IsdnP3State
_DialerIsdnVN3DChP3State_Object = MibTableColumn
dialerIsdnVN3DChP3State = _DialerIsdnVN3DChP3State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 16, 1, 5),
    _DialerIsdnVN3DChP3State_Type()
)
dialerIsdnVN3DChP3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnVN3DChP3State.setStatus("mandatory")
_DialerIsdnNET3BChTable_Object = MibTable
dialerIsdnNET3BChTable = _DialerIsdnNET3BChTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17)
)
if mibBuilder.loadTexts:
    dialerIsdnNET3BChTable.setStatus("mandatory")
_DialerIsdnNET3BChEntry_Object = MibTableRow
dialerIsdnNET3BChEntry = _DialerIsdnNET3BChEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1)
)
dialerIsdnNET3BChEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerIsdnNET3BChPortRef"),
)
if mibBuilder.loadTexts:
    dialerIsdnNET3BChEntry.setStatus("mandatory")
_DialerIsdnNET3BChPortRef_Type = PortRef
_DialerIsdnNET3BChPortRef_Object = MibTableColumn
dialerIsdnNET3BChPortRef = _DialerIsdnNET3BChPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 1),
    _DialerIsdnNET3BChPortRef_Type()
)
dialerIsdnNET3BChPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChPortRef.setStatus("mandatory")
_DialerIsdnNET3BChLocalDnType_Type = IsdnDnType
_DialerIsdnNET3BChLocalDnType_Object = MibTableColumn
dialerIsdnNET3BChLocalDnType = _DialerIsdnNET3BChLocalDnType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 2),
    _DialerIsdnNET3BChLocalDnType_Type()
)
dialerIsdnNET3BChLocalDnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChLocalDnType.setStatus("mandatory")
_DialerIsdnNET3BChLocalDnPlan_Type = IsdnDnPlan
_DialerIsdnNET3BChLocalDnPlan_Object = MibTableColumn
dialerIsdnNET3BChLocalDnPlan = _DialerIsdnNET3BChLocalDnPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 3),
    _DialerIsdnNET3BChLocalDnPlan_Type()
)
dialerIsdnNET3BChLocalDnPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChLocalDnPlan.setStatus("mandatory")


class _DialerIsdnNET3BChLocalDn_Type(DisplayString):
    """Custom type dialerIsdnNET3BChLocalDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnNET3BChLocalDn_Type.__name__ = "DisplayString"
_DialerIsdnNET3BChLocalDn_Object = MibTableColumn
dialerIsdnNET3BChLocalDn = _DialerIsdnNET3BChLocalDn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 4),
    _DialerIsdnNET3BChLocalDn_Type()
)
dialerIsdnNET3BChLocalDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChLocalDn.setStatus("mandatory")
_DialerIsdnNET3BChLocalSubType_Type = IsdnSubType
_DialerIsdnNET3BChLocalSubType_Object = MibTableColumn
dialerIsdnNET3BChLocalSubType = _DialerIsdnNET3BChLocalSubType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 5),
    _DialerIsdnNET3BChLocalSubType_Type()
)
dialerIsdnNET3BChLocalSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChLocalSubType.setStatus("mandatory")


class _DialerIsdnNET3BChLocalSub_Type(DisplayString):
    """Custom type dialerIsdnNET3BChLocalSub based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnNET3BChLocalSub_Type.__name__ = "DisplayString"
_DialerIsdnNET3BChLocalSub_Object = MibTableColumn
dialerIsdnNET3BChLocalSub = _DialerIsdnNET3BChLocalSub_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 6),
    _DialerIsdnNET3BChLocalSub_Type()
)
dialerIsdnNET3BChLocalSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChLocalSub.setStatus("mandatory")
_DialerIsdnNET3BChRemoteDnType_Type = IsdnDnType
_DialerIsdnNET3BChRemoteDnType_Object = MibTableColumn
dialerIsdnNET3BChRemoteDnType = _DialerIsdnNET3BChRemoteDnType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 7),
    _DialerIsdnNET3BChRemoteDnType_Type()
)
dialerIsdnNET3BChRemoteDnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChRemoteDnType.setStatus("mandatory")
_DialerIsdnNET3BChRemoteDnPlan_Type = IsdnDnPlan
_DialerIsdnNET3BChRemoteDnPlan_Object = MibTableColumn
dialerIsdnNET3BChRemoteDnPlan = _DialerIsdnNET3BChRemoteDnPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 8),
    _DialerIsdnNET3BChRemoteDnPlan_Type()
)
dialerIsdnNET3BChRemoteDnPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChRemoteDnPlan.setStatus("mandatory")


class _DialerIsdnNET3BChRemoteDn_Type(DisplayString):
    """Custom type dialerIsdnNET3BChRemoteDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnNET3BChRemoteDn_Type.__name__ = "DisplayString"
_DialerIsdnNET3BChRemoteDn_Object = MibTableColumn
dialerIsdnNET3BChRemoteDn = _DialerIsdnNET3BChRemoteDn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 9),
    _DialerIsdnNET3BChRemoteDn_Type()
)
dialerIsdnNET3BChRemoteDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChRemoteDn.setStatus("mandatory")
_DialerIsdnNET3BChRemoteSubType_Type = IsdnSubType
_DialerIsdnNET3BChRemoteSubType_Object = MibTableColumn
dialerIsdnNET3BChRemoteSubType = _DialerIsdnNET3BChRemoteSubType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 10),
    _DialerIsdnNET3BChRemoteSubType_Type()
)
dialerIsdnNET3BChRemoteSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChRemoteSubType.setStatus("mandatory")


class _DialerIsdnNET3BChRemoteSub_Type(DisplayString):
    """Custom type dialerIsdnNET3BChRemoteSub based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnNET3BChRemoteSub_Type.__name__ = "DisplayString"
_DialerIsdnNET3BChRemoteSub_Object = MibTableColumn
dialerIsdnNET3BChRemoteSub = _DialerIsdnNET3BChRemoteSub_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 11),
    _DialerIsdnNET3BChRemoteSub_Type()
)
dialerIsdnNET3BChRemoteSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChRemoteSub.setStatus("mandatory")
_DialerIsdnNET3BChCallType_Type = IsdnCallType
_DialerIsdnNET3BChCallType_Object = MibTableColumn
dialerIsdnNET3BChCallType = _DialerIsdnNET3BChCallType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 12),
    _DialerIsdnNET3BChCallType_Type()
)
dialerIsdnNET3BChCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChCallType.setStatus("mandatory")
_DialerIsdnNET3BChCallSpeed_Type = IsdnCallSpeed
_DialerIsdnNET3BChCallSpeed_Object = MibTableColumn
dialerIsdnNET3BChCallSpeed = _DialerIsdnNET3BChCallSpeed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 13),
    _DialerIsdnNET3BChCallSpeed_Type()
)
dialerIsdnNET3BChCallSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChCallSpeed.setStatus("mandatory")
_DialerIsdnNET3BChBChannel_Type = IsdnBChannels
_DialerIsdnNET3BChBChannel_Object = MibTableColumn
dialerIsdnNET3BChBChannel = _DialerIsdnNET3BChBChannel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 14),
    _DialerIsdnNET3BChBChannel_Type()
)
dialerIsdnNET3BChBChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChBChannel.setStatus("mandatory")
_DialerIsdnNET3BChAnsEnable_Type = IsdnAnsEnable
_DialerIsdnNET3BChAnsEnable_Object = MibTableColumn
dialerIsdnNET3BChAnsEnable = _DialerIsdnNET3BChAnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 15),
    _DialerIsdnNET3BChAnsEnable_Type()
)
dialerIsdnNET3BChAnsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChAnsEnable.setStatus("mandatory")
_DialerIsdnNET3BChTnsNetId_Type = IsdnTnsNetId
_DialerIsdnNET3BChTnsNetId_Object = MibTableColumn
dialerIsdnNET3BChTnsNetId = _DialerIsdnNET3BChTnsNetId_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 16),
    _DialerIsdnNET3BChTnsNetId_Type()
)
dialerIsdnNET3BChTnsNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChTnsNetId.setStatus("mandatory")
_DialerIsdnNET3BChTnsIdPlan_Type = IsdnTnsIdPlan
_DialerIsdnNET3BChTnsIdPlan_Object = MibTableColumn
dialerIsdnNET3BChTnsIdPlan = _DialerIsdnNET3BChTnsIdPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 17),
    _DialerIsdnNET3BChTnsIdPlan_Type()
)
dialerIsdnNET3BChTnsIdPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChTnsIdPlan.setStatus("mandatory")


class _DialerIsdnNET3BChTnsDigs_Type(DisplayString):
    """Custom type dialerIsdnNET3BChTnsDigs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DialerIsdnNET3BChTnsDigs_Type.__name__ = "DisplayString"
_DialerIsdnNET3BChTnsDigs_Object = MibTableColumn
dialerIsdnNET3BChTnsDigs = _DialerIsdnNET3BChTnsDigs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 18),
    _DialerIsdnNET3BChTnsDigs_Type()
)
dialerIsdnNET3BChTnsDigs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChTnsDigs.setStatus("mandatory")
_DialerIsdnNET3BChScrStatus_Type = IsdnScrStatus
_DialerIsdnNET3BChScrStatus_Object = MibTableColumn
dialerIsdnNET3BChScrStatus = _DialerIsdnNET3BChScrStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 19),
    _DialerIsdnNET3BChScrStatus_Type()
)
dialerIsdnNET3BChScrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChScrStatus.setStatus("mandatory")
_DialerIsdnNET3BChCallOpt_Type = IsdnCallOpt
_DialerIsdnNET3BChCallOpt_Object = MibTableColumn
dialerIsdnNET3BChCallOpt = _DialerIsdnNET3BChCallOpt_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 20),
    _DialerIsdnNET3BChCallOpt_Type()
)
dialerIsdnNET3BChCallOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChCallOpt.setStatus("mandatory")
_DialerIsdnNET3BChCcState_Type = IsdnNET3BCcState
_DialerIsdnNET3BChCcState_Object = MibTableColumn
dialerIsdnNET3BChCcState = _DialerIsdnNET3BChCcState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 21),
    _DialerIsdnNET3BChCcState_Type()
)
dialerIsdnNET3BChCcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChCcState.setStatus("mandatory")
_DialerIsdnNET3BChCcNbCause_Type = Integer32
_DialerIsdnNET3BChCcNbCause_Object = MibTableColumn
dialerIsdnNET3BChCcNbCause = _DialerIsdnNET3BChCcNbCause_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 22),
    _DialerIsdnNET3BChCcNbCause_Type()
)
dialerIsdnNET3BChCcNbCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChCcNbCause.setStatus("mandatory")


class _DialerIsdnNET3BChCcCause_Type(OctetString):
    """Custom type dialerIsdnNET3BChCcCause based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DialerIsdnNET3BChCcCause_Type.__name__ = "OctetString"
_DialerIsdnNET3BChCcCause_Object = MibTableColumn
dialerIsdnNET3BChCcCause = _DialerIsdnNET3BChCcCause_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 23),
    _DialerIsdnNET3BChCcCause_Type()
)
dialerIsdnNET3BChCcCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChCcCause.setStatus("mandatory")
_DialerIsdnNET3BChL3State_Type = IsdnL3State
_DialerIsdnNET3BChL3State_Object = MibTableColumn
dialerIsdnNET3BChL3State = _DialerIsdnNET3BChL3State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 24),
    _DialerIsdnNET3BChL3State_Type()
)
dialerIsdnNET3BChL3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChL3State.setStatus("mandatory")
_DialerIsdnNET3BChL2State_Type = IsdnL2State
_DialerIsdnNET3BChL2State_Object = MibTableColumn
dialerIsdnNET3BChL2State = _DialerIsdnNET3BChL2State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 25),
    _DialerIsdnNET3BChL2State_Type()
)
dialerIsdnNET3BChL2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChL2State.setStatus("mandatory")
_DialerIsdnNET3BChTeiValue_Type = Integer32
_DialerIsdnNET3BChTeiValue_Object = MibTableColumn
dialerIsdnNET3BChTeiValue = _DialerIsdnNET3BChTeiValue_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 26),
    _DialerIsdnNET3BChTeiValue_Type()
)
dialerIsdnNET3BChTeiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChTeiValue.setStatus("mandatory")
_DialerIsdnNET3BChTeiStatus_Type = IsdnTeiStatus
_DialerIsdnNET3BChTeiStatus_Object = MibTableColumn
dialerIsdnNET3BChTeiStatus = _DialerIsdnNET3BChTeiStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 27),
    _DialerIsdnNET3BChTeiStatus_Type()
)
dialerIsdnNET3BChTeiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChTeiStatus.setStatus("mandatory")
_DialerIsdnNET3BChStoDefined_Type = IsdnStoDefined
_DialerIsdnNET3BChStoDefined_Object = MibTableColumn
dialerIsdnNET3BChStoDefined = _DialerIsdnNET3BChStoDefined_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 28),
    _DialerIsdnNET3BChStoDefined_Type()
)
dialerIsdnNET3BChStoDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChStoDefined.setStatus("mandatory")
_DialerIsdnNET3BChStoDnType_Type = Integer32
_DialerIsdnNET3BChStoDnType_Object = MibTableColumn
dialerIsdnNET3BChStoDnType = _DialerIsdnNET3BChStoDnType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 29),
    _DialerIsdnNET3BChStoDnType_Type()
)
dialerIsdnNET3BChStoDnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChStoDnType.setStatus("mandatory")
_DialerIsdnNET3BChStoDnPlan_Type = Integer32
_DialerIsdnNET3BChStoDnPlan_Object = MibTableColumn
dialerIsdnNET3BChStoDnPlan = _DialerIsdnNET3BChStoDnPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 30),
    _DialerIsdnNET3BChStoDnPlan_Type()
)
dialerIsdnNET3BChStoDnPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChStoDnPlan.setStatus("mandatory")


class _DialerIsdnNET3BChStoDn_Type(DisplayString):
    """Custom type dialerIsdnNET3BChStoDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnNET3BChStoDn_Type.__name__ = "DisplayString"
_DialerIsdnNET3BChStoDn_Object = MibTableColumn
dialerIsdnNET3BChStoDn = _DialerIsdnNET3BChStoDn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 31),
    _DialerIsdnNET3BChStoDn_Type()
)
dialerIsdnNET3BChStoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChStoDn.setStatus("mandatory")
_DialerIsdnNET3BChStoSubType_Type = Integer32
_DialerIsdnNET3BChStoSubType_Object = MibTableColumn
dialerIsdnNET3BChStoSubType = _DialerIsdnNET3BChStoSubType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 32),
    _DialerIsdnNET3BChStoSubType_Type()
)
dialerIsdnNET3BChStoSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChStoSubType.setStatus("mandatory")


class _DialerIsdnNET3BChStoSub_Type(DisplayString):
    """Custom type dialerIsdnNET3BChStoSub based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnNET3BChStoSub_Type.__name__ = "DisplayString"
_DialerIsdnNET3BChStoSub_Object = MibTableColumn
dialerIsdnNET3BChStoSub = _DialerIsdnNET3BChStoSub_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 33),
    _DialerIsdnNET3BChStoSub_Type()
)
dialerIsdnNET3BChStoSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChStoSub.setStatus("mandatory")
_DialerIsdnNET3BChStoTnsNetId_Type = Integer32
_DialerIsdnNET3BChStoTnsNetId_Object = MibTableColumn
dialerIsdnNET3BChStoTnsNetId = _DialerIsdnNET3BChStoTnsNetId_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 34),
    _DialerIsdnNET3BChStoTnsNetId_Type()
)
dialerIsdnNET3BChStoTnsNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChStoTnsNetId.setStatus("mandatory")
_DialerIsdnNET3BChStoTnsPlan_Type = Integer32
_DialerIsdnNET3BChStoTnsPlan_Object = MibTableColumn
dialerIsdnNET3BChStoTnsPlan = _DialerIsdnNET3BChStoTnsPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 35),
    _DialerIsdnNET3BChStoTnsPlan_Type()
)
dialerIsdnNET3BChStoTnsPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChStoTnsPlan.setStatus("mandatory")


class _DialerIsdnNET3BChStoDigs_Type(DisplayString):
    """Custom type dialerIsdnNET3BChStoDigs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DialerIsdnNET3BChStoDigs_Type.__name__ = "DisplayString"
_DialerIsdnNET3BChStoDigs_Object = MibTableColumn
dialerIsdnNET3BChStoDigs = _DialerIsdnNET3BChStoDigs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 36),
    _DialerIsdnNET3BChStoDigs_Type()
)
dialerIsdnNET3BChStoDigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChStoDigs.setStatus("mandatory")
_DialerIsdnNET3BChStoBcType_Type = Integer32
_DialerIsdnNET3BChStoBcType_Object = MibTableColumn
dialerIsdnNET3BChStoBcType = _DialerIsdnNET3BChStoBcType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 37),
    _DialerIsdnNET3BChStoBcType_Type()
)
dialerIsdnNET3BChStoBcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChStoBcType.setStatus("mandatory")
_DialerIsdnNET3BChStoBcOpt_Type = Integer32
_DialerIsdnNET3BChStoBcOpt_Object = MibTableColumn
dialerIsdnNET3BChStoBcOpt = _DialerIsdnNET3BChStoBcOpt_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 17, 1, 38),
    _DialerIsdnNET3BChStoBcOpt_Type()
)
dialerIsdnNET3BChStoBcOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnNET3BChStoBcOpt.setStatus("mandatory")
_DialerIsdnTPHBChTable_Object = MibTable
dialerIsdnTPHBChTable = _DialerIsdnTPHBChTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18)
)
if mibBuilder.loadTexts:
    dialerIsdnTPHBChTable.setStatus("mandatory")
_DialerIsdnTPHBChEntry_Object = MibTableRow
dialerIsdnTPHBChEntry = _DialerIsdnTPHBChEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1)
)
dialerIsdnTPHBChEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerIsdnTPHBChPortRef"),
)
if mibBuilder.loadTexts:
    dialerIsdnTPHBChEntry.setStatus("mandatory")
_DialerIsdnTPHBChPortRef_Type = PortRef
_DialerIsdnTPHBChPortRef_Object = MibTableColumn
dialerIsdnTPHBChPortRef = _DialerIsdnTPHBChPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 1),
    _DialerIsdnTPHBChPortRef_Type()
)
dialerIsdnTPHBChPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChPortRef.setStatus("mandatory")
_DialerIsdnTPHBChLocalDnType_Type = IsdnDnType
_DialerIsdnTPHBChLocalDnType_Object = MibTableColumn
dialerIsdnTPHBChLocalDnType = _DialerIsdnTPHBChLocalDnType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 2),
    _DialerIsdnTPHBChLocalDnType_Type()
)
dialerIsdnTPHBChLocalDnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChLocalDnType.setStatus("mandatory")
_DialerIsdnTPHBChLocalDnPlan_Type = IsdnDnPlan
_DialerIsdnTPHBChLocalDnPlan_Object = MibTableColumn
dialerIsdnTPHBChLocalDnPlan = _DialerIsdnTPHBChLocalDnPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 3),
    _DialerIsdnTPHBChLocalDnPlan_Type()
)
dialerIsdnTPHBChLocalDnPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChLocalDnPlan.setStatus("mandatory")


class _DialerIsdnTPHBChLocalDn_Type(DisplayString):
    """Custom type dialerIsdnTPHBChLocalDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnTPHBChLocalDn_Type.__name__ = "DisplayString"
_DialerIsdnTPHBChLocalDn_Object = MibTableColumn
dialerIsdnTPHBChLocalDn = _DialerIsdnTPHBChLocalDn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 4),
    _DialerIsdnTPHBChLocalDn_Type()
)
dialerIsdnTPHBChLocalDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChLocalDn.setStatus("mandatory")
_DialerIsdnTPHBChLocalSubType_Type = IsdnSubType
_DialerIsdnTPHBChLocalSubType_Object = MibTableColumn
dialerIsdnTPHBChLocalSubType = _DialerIsdnTPHBChLocalSubType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 5),
    _DialerIsdnTPHBChLocalSubType_Type()
)
dialerIsdnTPHBChLocalSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChLocalSubType.setStatus("mandatory")


class _DialerIsdnTPHBChLocalSub_Type(DisplayString):
    """Custom type dialerIsdnTPHBChLocalSub based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnTPHBChLocalSub_Type.__name__ = "DisplayString"
_DialerIsdnTPHBChLocalSub_Object = MibTableColumn
dialerIsdnTPHBChLocalSub = _DialerIsdnTPHBChLocalSub_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 6),
    _DialerIsdnTPHBChLocalSub_Type()
)
dialerIsdnTPHBChLocalSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChLocalSub.setStatus("mandatory")
_DialerIsdnTPHBChRemoteDnType_Type = IsdnDnType
_DialerIsdnTPHBChRemoteDnType_Object = MibTableColumn
dialerIsdnTPHBChRemoteDnType = _DialerIsdnTPHBChRemoteDnType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 7),
    _DialerIsdnTPHBChRemoteDnType_Type()
)
dialerIsdnTPHBChRemoteDnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChRemoteDnType.setStatus("mandatory")
_DialerIsdnTPHBChRemoteDnPlan_Type = IsdnDnPlan
_DialerIsdnTPHBChRemoteDnPlan_Object = MibTableColumn
dialerIsdnTPHBChRemoteDnPlan = _DialerIsdnTPHBChRemoteDnPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 8),
    _DialerIsdnTPHBChRemoteDnPlan_Type()
)
dialerIsdnTPHBChRemoteDnPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChRemoteDnPlan.setStatus("mandatory")


class _DialerIsdnTPHBChRemoteDn_Type(DisplayString):
    """Custom type dialerIsdnTPHBChRemoteDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnTPHBChRemoteDn_Type.__name__ = "DisplayString"
_DialerIsdnTPHBChRemoteDn_Object = MibTableColumn
dialerIsdnTPHBChRemoteDn = _DialerIsdnTPHBChRemoteDn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 9),
    _DialerIsdnTPHBChRemoteDn_Type()
)
dialerIsdnTPHBChRemoteDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChRemoteDn.setStatus("mandatory")
_DialerIsdnTPHBChRemoteSubType_Type = IsdnSubType
_DialerIsdnTPHBChRemoteSubType_Object = MibTableColumn
dialerIsdnTPHBChRemoteSubType = _DialerIsdnTPHBChRemoteSubType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 10),
    _DialerIsdnTPHBChRemoteSubType_Type()
)
dialerIsdnTPHBChRemoteSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChRemoteSubType.setStatus("mandatory")


class _DialerIsdnTPHBChRemoteSub_Type(DisplayString):
    """Custom type dialerIsdnTPHBChRemoteSub based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnTPHBChRemoteSub_Type.__name__ = "DisplayString"
_DialerIsdnTPHBChRemoteSub_Object = MibTableColumn
dialerIsdnTPHBChRemoteSub = _DialerIsdnTPHBChRemoteSub_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 11),
    _DialerIsdnTPHBChRemoteSub_Type()
)
dialerIsdnTPHBChRemoteSub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChRemoteSub.setStatus("mandatory")
_DialerIsdnTPHBChCallType_Type = IsdnCallType
_DialerIsdnTPHBChCallType_Object = MibTableColumn
dialerIsdnTPHBChCallType = _DialerIsdnTPHBChCallType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 12),
    _DialerIsdnTPHBChCallType_Type()
)
dialerIsdnTPHBChCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChCallType.setStatus("mandatory")
_DialerIsdnTPHBChCallSpeed_Type = IsdnCallSpeed
_DialerIsdnTPHBChCallSpeed_Object = MibTableColumn
dialerIsdnTPHBChCallSpeed = _DialerIsdnTPHBChCallSpeed_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 13),
    _DialerIsdnTPHBChCallSpeed_Type()
)
dialerIsdnTPHBChCallSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChCallSpeed.setStatus("mandatory")
_DialerIsdnTPHBChBChannel_Type = IsdnBChannels
_DialerIsdnTPHBChBChannel_Object = MibTableColumn
dialerIsdnTPHBChBChannel = _DialerIsdnTPHBChBChannel_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 14),
    _DialerIsdnTPHBChBChannel_Type()
)
dialerIsdnTPHBChBChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChBChannel.setStatus("mandatory")
_DialerIsdnTPHBChAnsEnable_Type = IsdnAnsEnable
_DialerIsdnTPHBChAnsEnable_Object = MibTableColumn
dialerIsdnTPHBChAnsEnable = _DialerIsdnTPHBChAnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 15),
    _DialerIsdnTPHBChAnsEnable_Type()
)
dialerIsdnTPHBChAnsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChAnsEnable.setStatus("mandatory")
_DialerIsdnTPHBChScrStatus_Type = IsdnScrStatus
_DialerIsdnTPHBChScrStatus_Object = MibTableColumn
dialerIsdnTPHBChScrStatus = _DialerIsdnTPHBChScrStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 16),
    _DialerIsdnTPHBChScrStatus_Type()
)
dialerIsdnTPHBChScrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChScrStatus.setStatus("mandatory")
_DialerIsdnTPHBChCallOpt_Type = IsdnCallOpt
_DialerIsdnTPHBChCallOpt_Object = MibTableColumn
dialerIsdnTPHBChCallOpt = _DialerIsdnTPHBChCallOpt_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 17),
    _DialerIsdnTPHBChCallOpt_Type()
)
dialerIsdnTPHBChCallOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChCallOpt.setStatus("mandatory")
_DialerIsdnTPHBChCcState_Type = IsdnTPHBCcState
_DialerIsdnTPHBChCcState_Object = MibTableColumn
dialerIsdnTPHBChCcState = _DialerIsdnTPHBChCcState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 18),
    _DialerIsdnTPHBChCcState_Type()
)
dialerIsdnTPHBChCcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChCcState.setStatus("mandatory")
_DialerIsdnTPHBChCcNbCause_Type = Integer32
_DialerIsdnTPHBChCcNbCause_Object = MibTableColumn
dialerIsdnTPHBChCcNbCause = _DialerIsdnTPHBChCcNbCause_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 19),
    _DialerIsdnTPHBChCcNbCause_Type()
)
dialerIsdnTPHBChCcNbCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChCcNbCause.setStatus("mandatory")


class _DialerIsdnTPHBChCcCause_Type(OctetString):
    """Custom type dialerIsdnTPHBChCcCause based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DialerIsdnTPHBChCcCause_Type.__name__ = "OctetString"
_DialerIsdnTPHBChCcCause_Object = MibTableColumn
dialerIsdnTPHBChCcCause = _DialerIsdnTPHBChCcCause_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 20),
    _DialerIsdnTPHBChCcCause_Type()
)
dialerIsdnTPHBChCcCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChCcCause.setStatus("mandatory")
_DialerIsdnTPHBChL3State_Type = IsdnL3State
_DialerIsdnTPHBChL3State_Object = MibTableColumn
dialerIsdnTPHBChL3State = _DialerIsdnTPHBChL3State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 21),
    _DialerIsdnTPHBChL3State_Type()
)
dialerIsdnTPHBChL3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChL3State.setStatus("mandatory")
_DialerIsdnTPHBChL2State_Type = IsdnL2State
_DialerIsdnTPHBChL2State_Object = MibTableColumn
dialerIsdnTPHBChL2State = _DialerIsdnTPHBChL2State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 22),
    _DialerIsdnTPHBChL2State_Type()
)
dialerIsdnTPHBChL2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChL2State.setStatus("mandatory")
_DialerIsdnTPHBChTeiValue_Type = Integer32
_DialerIsdnTPHBChTeiValue_Object = MibTableColumn
dialerIsdnTPHBChTeiValue = _DialerIsdnTPHBChTeiValue_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 23),
    _DialerIsdnTPHBChTeiValue_Type()
)
dialerIsdnTPHBChTeiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChTeiValue.setStatus("mandatory")
_DialerIsdnTPHBChTeiStatus_Type = IsdnTeiStatus
_DialerIsdnTPHBChTeiStatus_Object = MibTableColumn
dialerIsdnTPHBChTeiStatus = _DialerIsdnTPHBChTeiStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 24),
    _DialerIsdnTPHBChTeiStatus_Type()
)
dialerIsdnTPHBChTeiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChTeiStatus.setStatus("mandatory")
_DialerIsdnTPHBChStoDefined_Type = IsdnStoDefined
_DialerIsdnTPHBChStoDefined_Object = MibTableColumn
dialerIsdnTPHBChStoDefined = _DialerIsdnTPHBChStoDefined_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 25),
    _DialerIsdnTPHBChStoDefined_Type()
)
dialerIsdnTPHBChStoDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChStoDefined.setStatus("mandatory")
_DialerIsdnTPHBChStoDnType_Type = Integer32
_DialerIsdnTPHBChStoDnType_Object = MibTableColumn
dialerIsdnTPHBChStoDnType = _DialerIsdnTPHBChStoDnType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 26),
    _DialerIsdnTPHBChStoDnType_Type()
)
dialerIsdnTPHBChStoDnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChStoDnType.setStatus("mandatory")
_DialerIsdnTPHBChStoDnPlan_Type = Integer32
_DialerIsdnTPHBChStoDnPlan_Object = MibTableColumn
dialerIsdnTPHBChStoDnPlan = _DialerIsdnTPHBChStoDnPlan_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 27),
    _DialerIsdnTPHBChStoDnPlan_Type()
)
dialerIsdnTPHBChStoDnPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChStoDnPlan.setStatus("mandatory")


class _DialerIsdnTPHBChStoDn_Type(DisplayString):
    """Custom type dialerIsdnTPHBChStoDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnTPHBChStoDn_Type.__name__ = "DisplayString"
_DialerIsdnTPHBChStoDn_Object = MibTableColumn
dialerIsdnTPHBChStoDn = _DialerIsdnTPHBChStoDn_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 28),
    _DialerIsdnTPHBChStoDn_Type()
)
dialerIsdnTPHBChStoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChStoDn.setStatus("mandatory")
_DialerIsdnTPHBChStoSubType_Type = Integer32
_DialerIsdnTPHBChStoSubType_Object = MibTableColumn
dialerIsdnTPHBChStoSubType = _DialerIsdnTPHBChStoSubType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 29),
    _DialerIsdnTPHBChStoSubType_Type()
)
dialerIsdnTPHBChStoSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChStoSubType.setStatus("mandatory")


class _DialerIsdnTPHBChStoSub_Type(DisplayString):
    """Custom type dialerIsdnTPHBChStoSub based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_DialerIsdnTPHBChStoSub_Type.__name__ = "DisplayString"
_DialerIsdnTPHBChStoSub_Object = MibTableColumn
dialerIsdnTPHBChStoSub = _DialerIsdnTPHBChStoSub_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 30),
    _DialerIsdnTPHBChStoSub_Type()
)
dialerIsdnTPHBChStoSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChStoSub.setStatus("mandatory")
_DialerIsdnTPHBChStoBcType_Type = Integer32
_DialerIsdnTPHBChStoBcType_Object = MibTableColumn
dialerIsdnTPHBChStoBcType = _DialerIsdnTPHBChStoBcType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 31),
    _DialerIsdnTPHBChStoBcType_Type()
)
dialerIsdnTPHBChStoBcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChStoBcType.setStatus("mandatory")
_DialerIsdnTPHBChStoBcOpt_Type = Integer32
_DialerIsdnTPHBChStoBcOpt_Object = MibTableColumn
dialerIsdnTPHBChStoBcOpt = _DialerIsdnTPHBChStoBcOpt_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 18, 1, 32),
    _DialerIsdnTPHBChStoBcOpt_Type()
)
dialerIsdnTPHBChStoBcOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHBChStoBcOpt.setStatus("mandatory")
_DialerIsdnTPHDChTable_Object = MibTable
dialerIsdnTPHDChTable = _DialerIsdnTPHDChTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 19)
)
if mibBuilder.loadTexts:
    dialerIsdnTPHDChTable.setStatus("mandatory")
_DialerIsdnTPHDChEntry_Object = MibTableRow
dialerIsdnTPHDChEntry = _DialerIsdnTPHDChEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 19, 1)
)
dialerIsdnTPHDChEntry.setIndexNames(
    (0, "EICON-DIALER-MIB", "dialerIsdnTPHDChPortRef"),
)
if mibBuilder.loadTexts:
    dialerIsdnTPHDChEntry.setStatus("mandatory")
_DialerIsdnTPHDChPortRef_Type = PortRef
_DialerIsdnTPHDChPortRef_Object = MibTableColumn
dialerIsdnTPHDChPortRef = _DialerIsdnTPHDChPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 19, 1, 1),
    _DialerIsdnTPHDChPortRef_Type()
)
dialerIsdnTPHDChPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHDChPortRef.setStatus("mandatory")
_DialerIsdnTPHDChTeiValue_Type = Integer32
_DialerIsdnTPHDChTeiValue_Object = MibTableColumn
dialerIsdnTPHDChTeiValue = _DialerIsdnTPHDChTeiValue_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 19, 1, 2),
    _DialerIsdnTPHDChTeiValue_Type()
)
dialerIsdnTPHDChTeiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHDChTeiValue.setStatus("mandatory")
_DialerIsdnTPHDChTeiStatus_Type = IsdnTeiStatus
_DialerIsdnTPHDChTeiStatus_Object = MibTableColumn
dialerIsdnTPHDChTeiStatus = _DialerIsdnTPHDChTeiStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 19, 1, 3),
    _DialerIsdnTPHDChTeiStatus_Type()
)
dialerIsdnTPHDChTeiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHDChTeiStatus.setStatus("mandatory")
_DialerIsdnTPHDChL2State_Type = IsdnL2State
_DialerIsdnTPHDChL2State_Object = MibTableColumn
dialerIsdnTPHDChL2State = _DialerIsdnTPHDChL2State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 19, 1, 4),
    _DialerIsdnTPHDChL2State_Type()
)
dialerIsdnTPHDChL2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHDChL2State.setStatus("mandatory")
_DialerIsdnTPHDChP3State_Type = IsdnP3State
_DialerIsdnTPHDChP3State_Object = MibTableColumn
dialerIsdnTPHDChP3State = _DialerIsdnTPHDChP3State_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 16, 19, 1, 5),
    _DialerIsdnTPHDChP3State_Type()
)
dialerIsdnTPHDChP3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialerIsdnTPHDChP3State.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EICON-DIALER-MIB",
    **{"PortRef": PortRef,
       "ActionState": ActionState,
       "DataEncoding": DataEncoding,
       "ClockType": ClockType,
       "OnOff": OnOff,
       "FalseTrue": FalseTrue,
       "DisEnable": DisEnable,
       "PrimBitRate": PrimBitRate,
       "PrimCfg": PrimCfg,
       "IsdnSpidStatus": IsdnSpidStatus,
       "IsdnDnType": IsdnDnType,
       "IsdnDnPlan": IsdnDnPlan,
       "IsdnSubType": IsdnSubType,
       "IsdnTnsNetId": IsdnTnsNetId,
       "IsdnTnsIdPlan": IsdnTnsIdPlan,
       "IsdnCallType": IsdnCallType,
       "IsdnCallSpeed": IsdnCallSpeed,
       "IsdnBChannels": IsdnBChannels,
       "IsdnAnsEnable": IsdnAnsEnable,
       "IsdnScrStatus": IsdnScrStatus,
       "IsdnCallOpt": IsdnCallOpt,
       "IsdnStoDefined": IsdnStoDefined,
       "IsdnTeiStatus": IsdnTeiStatus,
       "IsdnL2State": IsdnL2State,
       "IsdnL3State": IsdnL3State,
       "IsdnP3State": IsdnP3State,
       "IsdnActState": IsdnActState,
       "IsdnNI1BCcState": IsdnNI1BCcState,
       "IsdnTR6BCcState": IsdnTR6BCcState,
       "IsdnVN3BCcState": IsdnVN3BCcState,
       "IsdnNET3BCcState": IsdnNET3BCcState,
       "IsdnTPHBCcState": IsdnTPHBCcState,
       "eicon": eicon,
       "management": management,
       "mibv2": mibv2,
       "module": module,
       "dialer": dialer,
       "dialerInfoTable": dialerInfoTable,
       "dialerInfoEntry": dialerInfoEntry,
       "dialerInfoPortRef": dialerInfoPortRef,
       "dialerInfoType": dialerInfoType,
       "dialerInfoTimeStart": dialerInfoTimeStart,
       "dialerInfoTimeConnect": dialerInfoTimeConnect,
       "dialerInfoLineSpeed": dialerInfoLineSpeed,
       "dialerInfoDataEncoding": dialerInfoDataEncoding,
       "dialerInfoClockType": dialerInfoClockType,
       "dialerDirectInfoTable": dialerDirectInfoTable,
       "dialerDirectInfoEntry": dialerDirectInfoEntry,
       "dialerDirectPortRef": dialerDirectPortRef,
       "dialerDirectIfType": dialerDirectIfType,
       "dialerDirectMode": dialerDirectMode,
       "dialerDirectConnDelay": dialerDirectConnDelay,
       "dialerDirectRtsDelay": dialerDirectRtsDelay,
       "dialerDirectState": dialerDirectState,
       "dialerDirectRs232InfoTable": dialerDirectRs232InfoTable,
       "dialerDirectRs232InfoEntry": dialerDirectRs232InfoEntry,
       "dialerDirectRs232PortRef": dialerDirectRs232PortRef,
       "dialerDirectRs232DbounceDelay": dialerDirectRs232DbounceDelay,
       "dialerDirectRs232DtrSignal": dialerDirectRs232DtrSignal,
       "dialerDirectRs232DsrSignal": dialerDirectRs232DsrSignal,
       "dialerDirectRs232RiSignal": dialerDirectRs232RiSignal,
       "dialerDirectX21InfoTable": dialerDirectX21InfoTable,
       "dialerDirectX21InfoEntry": dialerDirectX21InfoEntry,
       "dialerDirectX21PortRef": dialerDirectX21PortRef,
       "dialerDirectX21CtrlSignal": dialerDirectX21CtrlSignal,
       "dialerDirectX21IndicSignal": dialerDirectX21IndicSignal,
       "dialerV25bisInfoTable": dialerV25bisInfoTable,
       "dialerV25bisInfoEntry": dialerV25bisInfoEntry,
       "dialerV25bisPortRef": dialerV25bisPortRef,
       "dialerV25bisPrimaryNum": dialerV25bisPrimaryNum,
       "dialerV25bisSecondaryNum": dialerV25bisSecondaryNum,
       "dialerV25bisAnsEnable": dialerV25bisAnsEnable,
       "dialerV25bisRetryAllowed": dialerV25bisRetryAllowed,
       "dialerV25bisMaxRetries": dialerV25bisMaxRetries,
       "dialerV25bisRetryDelay": dialerV25bisRetryDelay,
       "dialerV25bisConnDelay": dialerV25bisConnDelay,
       "dialerV25bisOnOffDelay": dialerV25bisOnOffDelay,
       "dialerV25bisLossDelay": dialerV25bisLossDelay,
       "dialerV25bisMinDsrOnDelay": dialerV25bisMinDsrOnDelay,
       "dialerV25bisRiDtrDelay": dialerV25bisRiDtrDelay,
       "dialerV25bisHangupDelay": dialerV25bisHangupDelay,
       "dialerV25bisDeltaRiDelay": dialerV25bisDeltaRiDelay,
       "dialerV25bisCtsOnDelay": dialerV25bisCtsOnDelay,
       "dialerV25bisDtrSignal": dialerV25bisDtrSignal,
       "dialerV25bisDsrSignal": dialerV25bisDsrSignal,
       "dialerV25bisCtsSignal": dialerV25bisCtsSignal,
       "dialerV25bisRiSignal": dialerV25bisRiSignal,
       "dialerV25bisState": dialerV25bisState,
       "dialerAtCmdInfoTable": dialerAtCmdInfoTable,
       "dialerAtCmdInfoEntry": dialerAtCmdInfoEntry,
       "dialerAtCmdPortRef": dialerAtCmdPortRef,
       "dialerAtCmdPrimaryNum": dialerAtCmdPrimaryNum,
       "dialerAtCmdSecondaryNum": dialerAtCmdSecondaryNum,
       "dialerAtCmdAnsEnable": dialerAtCmdAnsEnable,
       "dialerAtCmdRetryAllowed": dialerAtCmdRetryAllowed,
       "dialerAtCmdMaxRetries": dialerAtCmdMaxRetries,
       "dialerAtCmdRetryDelay": dialerAtCmdRetryDelay,
       "dialerAtCmdConnDelay": dialerAtCmdConnDelay,
       "dialerAtCmdOnOffDelay": dialerAtCmdOnOffDelay,
       "dialerAtCmdLossDelay": dialerAtCmdLossDelay,
       "dialerAtCmdMinDsrOnDelay": dialerAtCmdMinDsrOnDelay,
       "dialerAtCmdRiDtrDelay": dialerAtCmdRiDtrDelay,
       "dialerAtCmdHangupDelay": dialerAtCmdHangupDelay,
       "dialerAtCmdDeltaRiDelay": dialerAtCmdDeltaRiDelay,
       "dialerAtCmdParity": dialerAtCmdParity,
       "dialerAtCmdBitsPerByte": dialerAtCmdBitsPerByte,
       "dialerAtCmdModemSpeed": dialerAtCmdModemSpeed,
       "dialerAtCmdDtrSignal": dialerAtCmdDtrSignal,
       "dialerAtCmdDsrSignal": dialerAtCmdDsrSignal,
       "dialerAtCmdRiSignal": dialerAtCmdRiSignal,
       "dialerAtCmdState": dialerAtCmdState,
       "dialerV22BisDnaInfoTable": dialerV22BisDnaInfoTable,
       "dialerV22BisDnaInfoEntry": dialerV22BisDnaInfoEntry,
       "dialerV22BisDnaPortRef": dialerV22BisDnaPortRef,
       "dialerV22BisDnaPrimaryNum": dialerV22BisDnaPrimaryNum,
       "dialerV22BisDnaSecondaryNum": dialerV22BisDnaSecondaryNum,
       "dialerV22BisDnaAnsEnable": dialerV22BisDnaAnsEnable,
       "dialerV22BisDnaRetryAllowed": dialerV22BisDnaRetryAllowed,
       "dialerV22BisDnaMaxRetries": dialerV22BisDnaMaxRetries,
       "dialerV22BisDnaCallProgress": dialerV22BisDnaCallProgress,
       "dialerV22BisDnaDecadic": dialerV22BisDnaDecadic,
       "dialerV22BisDnaMakeBreakRatio": dialerV22BisDnaMakeBreakRatio,
       "dialerV22BisDnaRetryDelay": dialerV22BisDnaRetryDelay,
       "dialerV22BisDnaMinDialDelay": dialerV22BisDnaMinDialDelay,
       "dialerV22BisDnaWaitDialTone": dialerV22BisDnaWaitDialTone,
       "dialerV22BisDnaWaitCarrier": dialerV22BisDnaWaitCarrier,
       "dialerV22BisDnaHndshkAbortTimer": dialerV22BisDnaHndshkAbortTimer,
       "dialerV22BisDnaGuardTone": dialerV22BisDnaGuardTone,
       "dialerV22BisDnaPulseDelay": dialerV22BisDnaPulseDelay,
       "dialerV22BisDnaDTMFDuration": dialerV22BisDnaDTMFDuration,
       "dialerV22BisDnaDTMFDelay": dialerV22BisDnaDTMFDelay,
       "dialerV22BisDnaDTMFLevel": dialerV22BisDnaDTMFLevel,
       "dialerV22BisDnaTxLevel": dialerV22BisDnaTxLevel,
       "dialerV22BisDnaRxLevel": dialerV22BisDnaRxLevel,
       "dialerV22BisDnaRiNbr": dialerV22BisDnaRiNbr,
       "dialerV22BisDnaDeltaRiDelay": dialerV22BisDnaDeltaRiDelay,
       "dialerV22BisDnaRiDtrDelay": dialerV22BisDnaRiDtrDelay,
       "dialerV22BisDnaDsrRtsDelay": dialerV22BisDnaDsrRtsDelay,
       "dialerV22BisDnaModemSpeed": dialerV22BisDnaModemSpeed,
       "dialerV22BisDnaDtrSignal": dialerV22BisDnaDtrSignal,
       "dialerV22BisDnaDsrSignal": dialerV22BisDnaDsrSignal,
       "dialerV22BisDnaRiSignal": dialerV22BisDnaRiSignal,
       "dialerV22BisDnaCdSignal": dialerV22BisDnaCdSignal,
       "dialerV22BisDnaToneInd": dialerV22BisDnaToneInd,
       "dialerV22BisDnaDloInd": dialerV22BisDnaDloInd,
       "dialerV22BisDnaState": dialerV22BisDnaState,
       "dialerV22BisImcInfoTable": dialerV22BisImcInfoTable,
       "dialerV22BisImcInfoEntry": dialerV22BisImcInfoEntry,
       "dialerV22BisImcPortRef": dialerV22BisImcPortRef,
       "dialerV22BisImcPrimaryNum": dialerV22BisImcPrimaryNum,
       "dialerV22BisImcSecondaryNum": dialerV22BisImcSecondaryNum,
       "dialerV22BisImcAnsEnable": dialerV22BisImcAnsEnable,
       "dialerV22BisImcRetryAllowed": dialerV22BisImcRetryAllowed,
       "dialerV22BisImcMaxRetries": dialerV22BisImcMaxRetries,
       "dialerV22BisImcCallProgress": dialerV22BisImcCallProgress,
       "dialerV22BisImcDecadic": dialerV22BisImcDecadic,
       "dialerV22BisImcMakeBreakRatio": dialerV22BisImcMakeBreakRatio,
       "dialerV22BisImcRetryDelay": dialerV22BisImcRetryDelay,
       "dialerV22BisImcMinDialDelay": dialerV22BisImcMinDialDelay,
       "dialerV22BisImcWaitDialTone": dialerV22BisImcWaitDialTone,
       "dialerV22BisImcWaitCarrier": dialerV22BisImcWaitCarrier,
       "dialerV22BisImcHndshkAbortTimer": dialerV22BisImcHndshkAbortTimer,
       "dialerV22BisImcGuardTone": dialerV22BisImcGuardTone,
       "dialerV22BisImcPulseDelay": dialerV22BisImcPulseDelay,
       "dialerV22BisImcDTMFDuration": dialerV22BisImcDTMFDuration,
       "dialerV22BisImcDTMFDelay": dialerV22BisImcDTMFDelay,
       "dialerV22BisImcDTMFLevel": dialerV22BisImcDTMFLevel,
       "dialerV22BisImcTxLevel": dialerV22BisImcTxLevel,
       "dialerV22BisImcRxLevel": dialerV22BisImcRxLevel,
       "dialerV22BisImcRiNbr": dialerV22BisImcRiNbr,
       "dialerV22BisImcDeltaRiDelay": dialerV22BisImcDeltaRiDelay,
       "dialerV22BisImcRiDtrDelay": dialerV22BisImcRiDtrDelay,
       "dialerV22BisImcDsrRtsDelay": dialerV22BisImcDsrRtsDelay,
       "dialerV22BisImcModemSpeed": dialerV22BisImcModemSpeed,
       "dialerV22BisImcDtrSignal": dialerV22BisImcDtrSignal,
       "dialerV22BisImcDsrSignal": dialerV22BisImcDsrSignal,
       "dialerV22BisImcRiSignal": dialerV22BisImcRiSignal,
       "dialerV22BisImcCdSignal": dialerV22BisImcCdSignal,
       "dialerV22BisImcToneInd": dialerV22BisImcToneInd,
       "dialerV22BisImcDloInd": dialerV22BisImcDloInd,
       "dialerV22BisImcLineType": dialerV22BisImcLineType,
       "dialerV22BisImcLeasedOpertn": dialerV22BisImcLeasedOpertn,
       "dialerV22BisImcSpeakerLevel": dialerV22BisImcSpeakerLevel,
       "dialerV22BisImcState": dialerV22BisImcState,
       "dialerV32BisInfoTable": dialerV32BisInfoTable,
       "dialerV32BisInfoEntry": dialerV32BisInfoEntry,
       "dialerV32BisPortRef": dialerV32BisPortRef,
       "dialerV32BisPrimNum": dialerV32BisPrimNum,
       "dialerV32BisSecNum": dialerV32BisSecNum,
       "dialerV32BisOverrNum": dialerV32BisOverrNum,
       "dialerV32BisCurrNum": dialerV32BisCurrNum,
       "dialerV32BisPrimBitRate": dialerV32BisPrimBitRate,
       "dialerV32BisSecBitRate": dialerV32BisSecBitRate,
       "dialerV32BisOverrBitRate": dialerV32BisOverrBitRate,
       "dialerV32BisCurrBitRate": dialerV32BisCurrBitRate,
       "dialerV32BisPrimConfig": dialerV32BisPrimConfig,
       "dialerV32BisSecConfig": dialerV32BisSecConfig,
       "dialerV32BisOverrConfig": dialerV32BisOverrConfig,
       "dialerV32BisCurrConfig": dialerV32BisCurrConfig,
       "dialerV32BisCurrRetry": dialerV32BisCurrRetry,
       "dialerV32BisRingCount": dialerV32BisRingCount,
       "dialerV32BisAnsEnable": dialerV32BisAnsEnable,
       "dialerV32BisDialMethod": dialerV32BisDialMethod,
       "dialerV32BisRetry": dialerV32BisRetry,
       "dialerV32BisCallFailure": dialerV32BisCallFailure,
       "dialerV32BisCarrierDetect": dialerV32BisCarrierDetect,
       "dialerV32BisCarrierWait": dialerV32BisCarrierWait,
       "dialerV32BisHangupVerify": dialerV32BisHangupVerify,
       "dialerV32BisHangupSignal": dialerV32BisHangupSignal,
       "dialerV32BisTxLevel": dialerV32BisTxLevel,
       "dialerV32BisRxLevel": dialerV32BisRxLevel,
       "dialerV32BisGuardTone": dialerV32BisGuardTone,
       "dialerV32BisLeasedLine": dialerV32BisLeasedLine,
       "dialerV32BisLeaseMode": dialerV32BisLeaseMode,
       "dialerV32BisLLTxLevel": dialerV32BisLLTxLevel,
       "dialerV32BisLLConfig": dialerV32BisLLConfig,
       "dialerV32BisLLBitRate": dialerV32BisLLBitRate,
       "dialerV32BisCallingTone": dialerV32BisCallingTone,
       "dialerV32BisAutoMode": dialerV32BisAutoMode,
       "dialerV32BisRetryAllowed": dialerV32BisRetryAllowed,
       "dialerV32BisMaxRetry": dialerV32BisMaxRetry,
       "dialerV32BisDialTone": dialerV32BisDialTone,
       "dialerV32BisDialToneWait": dialerV32BisDialToneWait,
       "dialerV32BisRetryWait": dialerV32BisRetryWait,
       "dialerV32BisHangupWait": dialerV32BisHangupWait,
       "dialerV32BisDialPauseWait": dialerV32BisDialPauseWait,
       "dialerV32BisDeltaRiWait": dialerV32BisDeltaRiWait,
       "dialerV32BisDTMFDuration": dialerV32BisDTMFDuration,
       "dialerV32BisDTMFDelay": dialerV32BisDTMFDelay,
       "dialerV32BisDTMFFreq1Level": dialerV32BisDTMFFreq1Level,
       "dialerV32BisDTMFFreq2Level": dialerV32BisDTMFFreq2Level,
       "dialerV32BisPulseMakeTime": dialerV32BisPulseMakeTime,
       "dialerV32BisPulseBreakTime": dialerV32BisPulseBreakTime,
       "dialerV32BisPulseDelay": dialerV32BisPulseDelay,
       "dialerV32BisSpeakerLevel": dialerV32BisSpeakerLevel,
       "dialerV32BisRiToAnswer": dialerV32BisRiToAnswer,
       "dialerV32BisAnswerBitRate": dialerV32BisAnswerBitRate,
       "dialerV32BisAnswerConfig": dialerV32BisAnswerConfig,
       "dialerV32BisRetrain": dialerV32BisRetrain,
       "dialerV32BisEqmLevel": dialerV32BisEqmLevel,
       "dialerV32BisRiOnOffDetect": dialerV32BisRiOnOffDetect,
       "dialerV32BisCdDetect": dialerV32BisCdDetect,
       "dialerV32BisRingbackDetect": dialerV32BisRingbackDetect,
       "dialerV32BisAnswerDetect": dialerV32BisAnswerDetect,
       "dialerV32BisBusyDetect": dialerV32BisBusyDetect,
       "dialerV32BisDiscDetect": dialerV32BisDiscDetect,
       "dialerV32BisCdSignal": dialerV32BisCdSignal,
       "dialerV32BisDsrSignal": dialerV32BisDsrSignal,
       "dialerV32BisState": dialerV32BisState,
       "dialerControlTable": dialerControlTable,
       "dialerControlEntry": dialerControlEntry,
       "dialerCtrlPortRef": dialerCtrlPortRef,
       "dialerCtrlAction": dialerCtrlAction,
       "dialerCtrlAnsEnable": dialerCtrlAnsEnable,
       "dialerCtrlDirectDSROnOff": dialerCtrlDirectDSROnOff,
       "dialerCtrlNumber": dialerCtrlNumber,
       "dialerCtrlScriptFile": dialerCtrlScriptFile,
       "dialerCtrlActionState": dialerCtrlActionState,
       "dialerCtrlActionError": dialerCtrlActionError,
       "dialerCtrlConfig": dialerCtrlConfig,
       "dialerCtrlBitRate": dialerCtrlBitRate,
       "dialerCtrlType": dialerCtrlType,
       "dialerCtrlPlan": dialerCtrlPlan,
       "dialerCtrlSub": dialerCtrlSub,
       "dialerCtrlSubType": dialerCtrlSubType,
       "dialerCtrlTns": dialerCtrlTns,
       "dialerCtrlNumberTemp": dialerCtrlNumberTemp,
       "dialerCtrlDialMask": dialerCtrlDialMask,
       "dialerCtrlCallSpeed": dialerCtrlCallSpeed,
       "dialerIsdnStatusTable": dialerIsdnStatusTable,
       "dialerIsdnStatusEntry": dialerIsdnStatusEntry,
       "dialerIsdnStatusPortRef": dialerIsdnStatusPortRef,
       "dialerIsdnStatusSwitchType": dialerIsdnStatusSwitchType,
       "dialerIsdnStatusChType": dialerIsdnStatusChType,
       "dialerIsdnStatusL1State": dialerIsdnStatusL1State,
       "dialerIsdnStatusState": dialerIsdnStatusState,
       "dialerIsdnNI1BChTable": dialerIsdnNI1BChTable,
       "dialerIsdnNI1BChEntry": dialerIsdnNI1BChEntry,
       "dialerIsdnNI1BChPortRef": dialerIsdnNI1BChPortRef,
       "dialerIsdnNI1BChSpid": dialerIsdnNI1BChSpid,
       "dialerIsdnNI1BChSpidStatus": dialerIsdnNI1BChSpidStatus,
       "dialerIsdnNI1BChLocalDn": dialerIsdnNI1BChLocalDn,
       "dialerIsdnNI1BChLocalSub": dialerIsdnNI1BChLocalSub,
       "dialerIsdnNI1BChTnsDigs": dialerIsdnNI1BChTnsDigs,
       "dialerIsdnNI1BChRemoteDn": dialerIsdnNI1BChRemoteDn,
       "dialerIsdnNI1BChRemoteSub": dialerIsdnNI1BChRemoteSub,
       "dialerIsdnNI1BChCallType": dialerIsdnNI1BChCallType,
       "dialerIsdnNI1BChCallSpeed": dialerIsdnNI1BChCallSpeed,
       "dialerIsdnNI1BChBChannel": dialerIsdnNI1BChBChannel,
       "dialerIsdnNI1BChAnsEnable": dialerIsdnNI1BChAnsEnable,
       "dialerIsdnNI1BChCcState": dialerIsdnNI1BChCcState,
       "dialerIsdnNI1BChCcNbCause": dialerIsdnNI1BChCcNbCause,
       "dialerIsdnNI1BChCcCause": dialerIsdnNI1BChCcCause,
       "dialerIsdnNI1BChL3State": dialerIsdnNI1BChL3State,
       "dialerIsdnNI1BChL2State": dialerIsdnNI1BChL2State,
       "dialerIsdnNI1BChTeiValue": dialerIsdnNI1BChTeiValue,
       "dialerIsdnNI1BChTeiStatus": dialerIsdnNI1BChTeiStatus,
       "dialerIsdnNI1BChLocalDnType": dialerIsdnNI1BChLocalDnType,
       "dialerIsdnNI1BChLocalDnPlan": dialerIsdnNI1BChLocalDnPlan,
       "dialerIsdnNI1BChLocalSubType": dialerIsdnNI1BChLocalSubType,
       "dialerIsdnNI1BChTnsNetId": dialerIsdnNI1BChTnsNetId,
       "dialerIsdnNI1BChTnsIdPlan": dialerIsdnNI1BChTnsIdPlan,
       "dialerIsdnNI1BChRemoteDnType": dialerIsdnNI1BChRemoteDnType,
       "dialerIsdnNI1BChRemoteDnPlan": dialerIsdnNI1BChRemoteDnPlan,
       "dialerIsdnNI1BChRemoteSubType": dialerIsdnNI1BChRemoteSubType,
       "dialerIsdnNI1BChScrStatus": dialerIsdnNI1BChScrStatus,
       "dialerIsdnNI1BChCallOpt": dialerIsdnNI1BChCallOpt,
       "dialerIsdnNI1BChStoDefined": dialerIsdnNI1BChStoDefined,
       "dialerIsdnNI1BChStoDnType": dialerIsdnNI1BChStoDnType,
       "dialerIsdnNI1BChStoDnPlan": dialerIsdnNI1BChStoDnPlan,
       "dialerIsdnNI1BChStoDn": dialerIsdnNI1BChStoDn,
       "dialerIsdnNI1BChStoSubType": dialerIsdnNI1BChStoSubType,
       "dialerIsdnNI1BChStoSub": dialerIsdnNI1BChStoSub,
       "dialerIsdnNI1BChStoTnsNetId": dialerIsdnNI1BChStoTnsNetId,
       "dialerIsdnNI1BChStoTnsPlan": dialerIsdnNI1BChStoTnsPlan,
       "dialerIsdnNI1BChStoDigs": dialerIsdnNI1BChStoDigs,
       "dialerIsdnNI1BChStoBcType": dialerIsdnNI1BChStoBcType,
       "dialerIsdnNI1BChStoBcOpt": dialerIsdnNI1BChStoBcOpt,
       "dialerIsdnNI1DChTable": dialerIsdnNI1DChTable,
       "dialerIsdnNI1DChEntry": dialerIsdnNI1DChEntry,
       "dialerIsdnNI1DChPortRef": dialerIsdnNI1DChPortRef,
       "dialerIsdnNI1DChTeiValue": dialerIsdnNI1DChTeiValue,
       "dialerIsdnNI1DChTeiStatus": dialerIsdnNI1DChTeiStatus,
       "dialerIsdnNI1DChL2State": dialerIsdnNI1DChL2State,
       "dialerIsdnNI1DChP3State": dialerIsdnNI1DChP3State,
       "dialerIsdnNI1DChActState": dialerIsdnNI1DChActState,
       "dialerIsdnTR6BChTable": dialerIsdnTR6BChTable,
       "dialerIsdnTR6BChEntry": dialerIsdnTR6BChEntry,
       "dialerIsdnTR6BChPortRef": dialerIsdnTR6BChPortRef,
       "dialerIsdnTR6BChLocalDn": dialerIsdnTR6BChLocalDn,
       "dialerIsdnTR6BChRemoteDn": dialerIsdnTR6BChRemoteDn,
       "dialerIsdnTR6BChCallType": dialerIsdnTR6BChCallType,
       "dialerIsdnTR6BChCallSpeed": dialerIsdnTR6BChCallSpeed,
       "dialerIsdnTR6BChBChannel": dialerIsdnTR6BChBChannel,
       "dialerIsdnTR6BChAnsEnable": dialerIsdnTR6BChAnsEnable,
       "dialerIsdnTR6BChCcState": dialerIsdnTR6BChCcState,
       "dialerIsdnTR6BChCcNbCause": dialerIsdnTR6BChCcNbCause,
       "dialerIsdnTR6BChCcCause": dialerIsdnTR6BChCcCause,
       "dialerIsdnTR6BChL3State": dialerIsdnTR6BChL3State,
       "dialerIsdnTR6BChL2State": dialerIsdnTR6BChL2State,
       "dialerIsdnTR6BChLocalDnType": dialerIsdnTR6BChLocalDnType,
       "dialerIsdnTR6BChLocalDnPlan": dialerIsdnTR6BChLocalDnPlan,
       "dialerIsdnTR6BChRemoteDnType": dialerIsdnTR6BChRemoteDnType,
       "dialerIsdnTR6BChRemoteDnPlan": dialerIsdnTR6BChRemoteDnPlan,
       "dialerIsdnTR6BChScrStatus": dialerIsdnTR6BChScrStatus,
       "dialerIsdnTR6BChCallOpt": dialerIsdnTR6BChCallOpt,
       "dialerIsdnTR6BChTeiValue": dialerIsdnTR6BChTeiValue,
       "dialerIsdnTR6BChTeiStatus": dialerIsdnTR6BChTeiStatus,
       "dialerIsdnTR6BChStoDefined": dialerIsdnTR6BChStoDefined,
       "dialerIsdnTR6BChStoDnType": dialerIsdnTR6BChStoDnType,
       "dialerIsdnTR6BChStoDnPlan": dialerIsdnTR6BChStoDnPlan,
       "dialerIsdnTR6BChStoDn": dialerIsdnTR6BChStoDn,
       "dialerIsdnTR6BChStoBcType": dialerIsdnTR6BChStoBcType,
       "dialerIsdnTR6BChStoBcOpt": dialerIsdnTR6BChStoBcOpt,
       "dialerIsdnVN3BChTable": dialerIsdnVN3BChTable,
       "dialerIsdnVN3BChEntry": dialerIsdnVN3BChEntry,
       "dialerIsdnVN3BChPortRef": dialerIsdnVN3BChPortRef,
       "dialerIsdnVN3BChLocalDnType": dialerIsdnVN3BChLocalDnType,
       "dialerIsdnVN3BChLocalDnPlan": dialerIsdnVN3BChLocalDnPlan,
       "dialerIsdnVN3BChLocalDn": dialerIsdnVN3BChLocalDn,
       "dialerIsdnVN3BChLocalSubType": dialerIsdnVN3BChLocalSubType,
       "dialerIsdnVN3BChLocalSub": dialerIsdnVN3BChLocalSub,
       "dialerIsdnVN3BChRemoteDnType": dialerIsdnVN3BChRemoteDnType,
       "dialerIsdnVN3BChRemoteDnPlan": dialerIsdnVN3BChRemoteDnPlan,
       "dialerIsdnVN3BChRemoteDn": dialerIsdnVN3BChRemoteDn,
       "dialerIsdnVN3BChRemoteSubType": dialerIsdnVN3BChRemoteSubType,
       "dialerIsdnVN3BChRemoteSub": dialerIsdnVN3BChRemoteSub,
       "dialerIsdnVN3BChCallType": dialerIsdnVN3BChCallType,
       "dialerIsdnVN3BChCallSpeed": dialerIsdnVN3BChCallSpeed,
       "dialerIsdnVN3BChBChannel": dialerIsdnVN3BChBChannel,
       "dialerIsdnVN3BChAnsEnable": dialerIsdnVN3BChAnsEnable,
       "dialerIsdnVN3BChScrStatus": dialerIsdnVN3BChScrStatus,
       "dialerIsdnVN3BChCallOpt": dialerIsdnVN3BChCallOpt,
       "dialerIsdnVN3BChCcState": dialerIsdnVN3BChCcState,
       "dialerIsdnVN3BChCcNbCause": dialerIsdnVN3BChCcNbCause,
       "dialerIsdnVN3BChCcCause": dialerIsdnVN3BChCcCause,
       "dialerIsdnVN3BChL3State": dialerIsdnVN3BChL3State,
       "dialerIsdnVN3BChL2State": dialerIsdnVN3BChL2State,
       "dialerIsdnVN3BChTeiValue": dialerIsdnVN3BChTeiValue,
       "dialerIsdnVN3BChTeiStatus": dialerIsdnVN3BChTeiStatus,
       "dialerIsdnVN3BChStoDefined": dialerIsdnVN3BChStoDefined,
       "dialerIsdnVN3BChStoDnType": dialerIsdnVN3BChStoDnType,
       "dialerIsdnVN3BChStoDnPlan": dialerIsdnVN3BChStoDnPlan,
       "dialerIsdnVN3BChStoDn": dialerIsdnVN3BChStoDn,
       "dialerIsdnVN3BChStoSubType": dialerIsdnVN3BChStoSubType,
       "dialerIsdnVN3BChStoSub": dialerIsdnVN3BChStoSub,
       "dialerIsdnVN3BChStoBcType": dialerIsdnVN3BChStoBcType,
       "dialerIsdnVN3BChStoBcOpt": dialerIsdnVN3BChStoBcOpt,
       "dialerIsdnVN3DChTable": dialerIsdnVN3DChTable,
       "dialerIsdnVN3DChEntry": dialerIsdnVN3DChEntry,
       "dialerIsdnVN3DChPortRef": dialerIsdnVN3DChPortRef,
       "dialerIsdnVN3DChTeiValue": dialerIsdnVN3DChTeiValue,
       "dialerIsdnVN3DChTeiStatus": dialerIsdnVN3DChTeiStatus,
       "dialerIsdnVN3DChL2State": dialerIsdnVN3DChL2State,
       "dialerIsdnVN3DChP3State": dialerIsdnVN3DChP3State,
       "dialerIsdnNET3BChTable": dialerIsdnNET3BChTable,
       "dialerIsdnNET3BChEntry": dialerIsdnNET3BChEntry,
       "dialerIsdnNET3BChPortRef": dialerIsdnNET3BChPortRef,
       "dialerIsdnNET3BChLocalDnType": dialerIsdnNET3BChLocalDnType,
       "dialerIsdnNET3BChLocalDnPlan": dialerIsdnNET3BChLocalDnPlan,
       "dialerIsdnNET3BChLocalDn": dialerIsdnNET3BChLocalDn,
       "dialerIsdnNET3BChLocalSubType": dialerIsdnNET3BChLocalSubType,
       "dialerIsdnNET3BChLocalSub": dialerIsdnNET3BChLocalSub,
       "dialerIsdnNET3BChRemoteDnType": dialerIsdnNET3BChRemoteDnType,
       "dialerIsdnNET3BChRemoteDnPlan": dialerIsdnNET3BChRemoteDnPlan,
       "dialerIsdnNET3BChRemoteDn": dialerIsdnNET3BChRemoteDn,
       "dialerIsdnNET3BChRemoteSubType": dialerIsdnNET3BChRemoteSubType,
       "dialerIsdnNET3BChRemoteSub": dialerIsdnNET3BChRemoteSub,
       "dialerIsdnNET3BChCallType": dialerIsdnNET3BChCallType,
       "dialerIsdnNET3BChCallSpeed": dialerIsdnNET3BChCallSpeed,
       "dialerIsdnNET3BChBChannel": dialerIsdnNET3BChBChannel,
       "dialerIsdnNET3BChAnsEnable": dialerIsdnNET3BChAnsEnable,
       "dialerIsdnNET3BChTnsNetId": dialerIsdnNET3BChTnsNetId,
       "dialerIsdnNET3BChTnsIdPlan": dialerIsdnNET3BChTnsIdPlan,
       "dialerIsdnNET3BChTnsDigs": dialerIsdnNET3BChTnsDigs,
       "dialerIsdnNET3BChScrStatus": dialerIsdnNET3BChScrStatus,
       "dialerIsdnNET3BChCallOpt": dialerIsdnNET3BChCallOpt,
       "dialerIsdnNET3BChCcState": dialerIsdnNET3BChCcState,
       "dialerIsdnNET3BChCcNbCause": dialerIsdnNET3BChCcNbCause,
       "dialerIsdnNET3BChCcCause": dialerIsdnNET3BChCcCause,
       "dialerIsdnNET3BChL3State": dialerIsdnNET3BChL3State,
       "dialerIsdnNET3BChL2State": dialerIsdnNET3BChL2State,
       "dialerIsdnNET3BChTeiValue": dialerIsdnNET3BChTeiValue,
       "dialerIsdnNET3BChTeiStatus": dialerIsdnNET3BChTeiStatus,
       "dialerIsdnNET3BChStoDefined": dialerIsdnNET3BChStoDefined,
       "dialerIsdnNET3BChStoDnType": dialerIsdnNET3BChStoDnType,
       "dialerIsdnNET3BChStoDnPlan": dialerIsdnNET3BChStoDnPlan,
       "dialerIsdnNET3BChStoDn": dialerIsdnNET3BChStoDn,
       "dialerIsdnNET3BChStoSubType": dialerIsdnNET3BChStoSubType,
       "dialerIsdnNET3BChStoSub": dialerIsdnNET3BChStoSub,
       "dialerIsdnNET3BChStoTnsNetId": dialerIsdnNET3BChStoTnsNetId,
       "dialerIsdnNET3BChStoTnsPlan": dialerIsdnNET3BChStoTnsPlan,
       "dialerIsdnNET3BChStoDigs": dialerIsdnNET3BChStoDigs,
       "dialerIsdnNET3BChStoBcType": dialerIsdnNET3BChStoBcType,
       "dialerIsdnNET3BChStoBcOpt": dialerIsdnNET3BChStoBcOpt,
       "dialerIsdnTPHBChTable": dialerIsdnTPHBChTable,
       "dialerIsdnTPHBChEntry": dialerIsdnTPHBChEntry,
       "dialerIsdnTPHBChPortRef": dialerIsdnTPHBChPortRef,
       "dialerIsdnTPHBChLocalDnType": dialerIsdnTPHBChLocalDnType,
       "dialerIsdnTPHBChLocalDnPlan": dialerIsdnTPHBChLocalDnPlan,
       "dialerIsdnTPHBChLocalDn": dialerIsdnTPHBChLocalDn,
       "dialerIsdnTPHBChLocalSubType": dialerIsdnTPHBChLocalSubType,
       "dialerIsdnTPHBChLocalSub": dialerIsdnTPHBChLocalSub,
       "dialerIsdnTPHBChRemoteDnType": dialerIsdnTPHBChRemoteDnType,
       "dialerIsdnTPHBChRemoteDnPlan": dialerIsdnTPHBChRemoteDnPlan,
       "dialerIsdnTPHBChRemoteDn": dialerIsdnTPHBChRemoteDn,
       "dialerIsdnTPHBChRemoteSubType": dialerIsdnTPHBChRemoteSubType,
       "dialerIsdnTPHBChRemoteSub": dialerIsdnTPHBChRemoteSub,
       "dialerIsdnTPHBChCallType": dialerIsdnTPHBChCallType,
       "dialerIsdnTPHBChCallSpeed": dialerIsdnTPHBChCallSpeed,
       "dialerIsdnTPHBChBChannel": dialerIsdnTPHBChBChannel,
       "dialerIsdnTPHBChAnsEnable": dialerIsdnTPHBChAnsEnable,
       "dialerIsdnTPHBChScrStatus": dialerIsdnTPHBChScrStatus,
       "dialerIsdnTPHBChCallOpt": dialerIsdnTPHBChCallOpt,
       "dialerIsdnTPHBChCcState": dialerIsdnTPHBChCcState,
       "dialerIsdnTPHBChCcNbCause": dialerIsdnTPHBChCcNbCause,
       "dialerIsdnTPHBChCcCause": dialerIsdnTPHBChCcCause,
       "dialerIsdnTPHBChL3State": dialerIsdnTPHBChL3State,
       "dialerIsdnTPHBChL2State": dialerIsdnTPHBChL2State,
       "dialerIsdnTPHBChTeiValue": dialerIsdnTPHBChTeiValue,
       "dialerIsdnTPHBChTeiStatus": dialerIsdnTPHBChTeiStatus,
       "dialerIsdnTPHBChStoDefined": dialerIsdnTPHBChStoDefined,
       "dialerIsdnTPHBChStoDnType": dialerIsdnTPHBChStoDnType,
       "dialerIsdnTPHBChStoDnPlan": dialerIsdnTPHBChStoDnPlan,
       "dialerIsdnTPHBChStoDn": dialerIsdnTPHBChStoDn,
       "dialerIsdnTPHBChStoSubType": dialerIsdnTPHBChStoSubType,
       "dialerIsdnTPHBChStoSub": dialerIsdnTPHBChStoSub,
       "dialerIsdnTPHBChStoBcType": dialerIsdnTPHBChStoBcType,
       "dialerIsdnTPHBChStoBcOpt": dialerIsdnTPHBChStoBcOpt,
       "dialerIsdnTPHDChTable": dialerIsdnTPHDChTable,
       "dialerIsdnTPHDChEntry": dialerIsdnTPHDChEntry,
       "dialerIsdnTPHDChPortRef": dialerIsdnTPHDChPortRef,
       "dialerIsdnTPHDChTeiValue": dialerIsdnTPHDChTeiValue,
       "dialerIsdnTPHDChTeiStatus": dialerIsdnTPHDChTeiStatus,
       "dialerIsdnTPHDChL2State": dialerIsdnTPHDChL2State,
       "dialerIsdnTPHDChP3State": dialerIsdnTPHDChP3State}
)
