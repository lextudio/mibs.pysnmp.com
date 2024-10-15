# SNMP MIB module (ARMILLAIRE2000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARMILLAIRE2000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:30 2024
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



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              17,
              18,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createandwait", 5),
          ("destroy", 6),
          ("down", 23),
          ("modified", 17),
          ("notinservice", 2),
          ("notready", 3),
          ("outofservice", 18),
          ("up", 22))
    )





class LrnRowStatus(Integer32):
    """Custom type LrnRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              18)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createandwait", 5),
          ("destroy", 6),
          ("notinservice", 2),
          ("notready", 3),
          ("outofservice", 18))
    )





class CktRowStatus(Integer32):
    """Custom type CktRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              17,
              18,
              20,
              22,
              23,
              99)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("block", 20),
          ("createandwait", 5),
          ("destroy", 6),
          ("down", 23),
          ("modified", 17),
          ("modifytimer", 99),
          ("notinservice", 2),
          ("notready", 3),
          ("outofservice", 18),
          ("up", 22))
    )





class TmrRowStatus(Integer32):
    """Custom type TmrRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              17,
              18,
              22,
              23,
              99)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("down", 23),
          ("modified", 17),
          ("modifytimer", 99),
          ("notinservice", 2),
          ("notready", 3),
          ("outofservice", 18),
          ("up", 22))
    )





class UserLoginStatus(Integer32):
    """Custom type UserLoginStatus based on Integer32"""
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
        *(("adduser", 3),
          ("deleteuser", 4),
          ("login", 1),
          ("logininvalid", 2))
    )





class UserLoginPriority(Integer32):
    """Custom type UserLoginPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              8738)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("cts", 2),
          ("user", 8738))
    )





class ProcessStatus(Integer32):
    """Custom type ProcessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              34,
              51,
              170,
              172)
        )
    )
    namedValues = NamedValues(
        *(("active", 34),
          ("down", 1),
          ("outofservice", 170),
          ("standby", 51),
          ("switchingover", 3),
          ("unknown", 172))
    )





class IsdnPriority(Integer32):
    """Custom type IsdnPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bearing", 2),
          ("primary", 0),
          ("secondary", 1))
    )





class IsdnType(Integer32):
    """Custom type IsdnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fas", 0),
          ("nfas", 1))
    )





class OpStatus(Integer32):
    """Custom type OpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              23)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("down", 23))
    )





class LinkOpStatus(Integer32):
    """Custom type LinkOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              19,
              23)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("down", 23),
          ("inhibit", 19))
    )





class LinkSetOpStatus(Integer32):
    """Custom type LinkSetOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              23)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("deactive", 23))
    )





class CktOpStatus(Integer32):
    """Custom type CktOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              20,
              23)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("block", 20),
          ("down", 23))
    )





class IsdnTrnkOpStatus(Integer32):
    """Custom type IsdnTrnkOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              21,
              23)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("disable", 21),
          ("down", 23))
    )





class ModifyTmrStatus(Integer32):
    """Custom type ModifyTmrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              99)
        )
    )
    namedValues = NamedValues(
        *(("modifytimer", 99),
          ("noaction", 0))
    )





class IfType(Integer32):
    """Custom type IfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("interface-e1", 8),
          ("interface-hde1", 9),
          ("interface-oc3", 3),
          ("interface-oc3aps", 12),
          ("interface-oc3cp", 5),
          ("interface-stm", 11),
          ("interface-stm1aps", 13),
          ("interface-t1", 0),
          ("interface-t3", 1),
          ("interface-une3", 10),
          ("interface-ut3", 2),
          ("interface-ut3cp", 4))
    )





class AtmIfType(Integer32):
    """Custom type AtmIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8)
        )
    )
    namedValues = NamedValues(
        *(("interface-e1", 8),
          ("interface-t1", 0))
    )





class ConnectionType(Integer32):
    """Custom type ConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("e3", 10),
          ("t3", 1),
          ("ut3", 2))
    )





class EnableStatus(Integer32):
    """Custom type EnableStatus based on Integer32"""
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





class Ss7RouteType(Integer32):
    """Custom type Ss7RouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("load", 0)
    )





class AddrIdentifier(Integer32):
    """Custom type AddrIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nationalnumber", 3),
          ("unknown", 2))
    )





class AddrType(Integer32):
    """Custom type AddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("callpartynum", 1),
          ("transitnetwork", 2))
    )





class NumPlan(Integer32):
    """Custom type NumPlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("isdnnumplan", 1),
          ("nonumber", 0))
    )





class Direction(Integer32):
    """Custom type Direction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("in", 0),
          ("out", 1))
    )





class EnableOperation(Integer32):
    """Custom type EnableOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("disable", 17),
          ("enable", 16))
    )





class IsdnChnlMgtOperation(Integer32):
    """Custom type IsdnChnlMgtOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("disable", 12),
          ("enable", 11))
    )





class IsdnTrnkMgtOperation(Integer32):
    """Custom type IsdnTrnkMgtOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disable", 10),
          ("enable", 9))
    )





class BlockOperation(Integer32):
    """Custom type BlockOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("block", 5),
          ("noaction", 0),
          ("unblock", 6))
    )





class Level(Integer32):
    """Custom type Level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2))
    )





class ModemResetStatus(Integer32):
    """Custom type ModemResetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )





class ModemEnableStatus(Integer32):
    """Custom type ModemEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )





class MeasEnableStatus(Integer32):
    """Custom type MeasEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )





class EthernetConnStatus(Integer32):
    """Custom type EthernetConnStatus based on Integer32"""
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





class Standard(Integer32):
    """Custom type Standard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(65,
              73,
              84)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 65),
          ("itu", 73),
          ("telmex", 84))
    )





class TrunkType(Integer32):
    """Custom type TrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(17,
              34)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 17),
          ("ss7", 34))
    )





class RouteType(Integer32):
    """Custom type RouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isdnRouteType", 2),
          ("ss7RouteType", 1))
    )





class AuditType(Integer32):
    """Custom type AuditType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(65,
              73)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 65),
          ("itu", 73))
    )





class AuditOperation(Integer32):
    """Custom type AuditOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("audit", 1),
          ("noaction", 0))
    )





class Controlstatus(Integer32):
    """Custom type Controlstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              6,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("blockckt", 5),
          ("disablechnl", 12),
          ("enablechnl", 11),
          ("noaction", 0),
          ("unblock", 6))
    )





class LinkControlStatus(Integer32):
    """Custom type LinkControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inhibitlink", 1),
          ("noaction", 0),
          ("uninhibitlink", 2))
    )





class LinkSetControlStatus(Integer32):
    """Custom type LinkSetControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("activatelnkset", 3),
          ("deactivatelnkset", 4),
          ("noaction", 0))
    )





class CircuitControlStatus(Integer32):
    """Custom type CircuitControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7,
              8,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("blockcic", 7),
          ("noaction", 0),
          ("queryckt", 13),
          ("resetckt", 15),
          ("unblockcic", 8),
          ("validateckt", 14))
    )





class IsdnControlstatus(Integer32):
    """Custom type IsdnControlstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabletrnk", 10),
          ("enabletrnk", 9),
          ("noaction", 0))
    )





class MtpRteState(Integer32):
    """Custom type MtpRteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rteavail", 1),
          ("rteunaval", 0))
    )





class Bool(Integer32):
    """Custom type Bool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )





class LoadBalance(Integer32):
    """Custom type LoadBalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )





class TrnkGrpType(Integer32):
    """Custom type TrnkGrpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 33),
          ("ss7", 32))
    )





class ActiveAlarmAckStatus(Integer32):
    """Custom type ActiveAlarmAckStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("noaction", 1))
    )





class EventType(Integer32):
    """Custom type EventType based on Integer32"""
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
        *(("alarm", 1),
          ("audit", 3),
          ("diagnostics", 4),
          ("emergency", 2),
          ("maintenance", 6),
          ("security", 5))
    )





class AlarmEvent(Integer32):
    """Custom type AlarmEvent based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("cdr", 5),
          ("device", 2),
          ("faultTolerance", 9),
          ("general", 1),
          ("ig", 8),
          ("log", 7),
          ("measurement", 6),
          ("mfd", 4),
          ("nomainevent", 0),
          ("protocol", 3))
    )





class AlarmSubEvent(Integer32):
    """Custom type AlarmSubEvent based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("administration", 1),
          ("atm", 9),
          ("hub", 5),
          ("isdn", 8),
          ("mssc", 3),
          ("nosubevent", 0),
          ("operation", 2),
          ("ss7Br", 7),
          ("ss7lnk", 6),
          ("xconnect", 4))
    )





class AlarmSeverity(Integer32):
    """Custom type AlarmSeverity based on Integer32"""
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
        *(("critical", 1),
          ("informational", 4),
          ("major", 2),
          ("minor", 3))
    )





class RoffType(Integer32):
    """Custom type RoffType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("intlgateway", 3),
          ("le", 1),
          ("tandem", 2))
    )





class NameString(DisplayString):
    """Custom type NameString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )





class AddrString(DisplayString):
    """Custom type AddrString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )





class CdrFlag(Integer32):
    """Custom type CdrFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bi", 3),
          ("ic", 1),
          ("noCdr", 0),
          ("og", 2))
    )





class DSPCardType(Integer32):
    """Custom type DSPCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsp2B", 1),
          ("dsp2C", 2))
    )





class VoicePcm(Integer32):
    """Custom type VoicePcm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 101),
          ("ulaw", 102))
    )





class TGFeature(Integer32):
    """Custom type TGFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )





class FTswitchOver(Integer32):
    """Custom type FTswitchOver based on Integer32"""
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
        *(("fticc", 1),
          ("ftisdn", 2),
          ("ftlm", 4),
          ("ftsig", 0),
          ("ftsphr", 3))
    )





class LogFileAttr(Integer32):
    """Custom type LogFileAttr based on Integer32"""
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
        *(("alarmlog", 3),
          ("auditlog", 2),
          ("billlog", 8),
          ("diaglog", 1),
          ("emplog", 6),
          ("eventlog", 5),
          ("measlog", 7),
          ("scrtylog", 4))
    )





class LogFileEnDis(Integer32):
    """Custom type LogFileEnDis based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("alarmlog", 3),
          ("auditlog", 2),
          ("billlog", 8),
          ("diaglog", 1),
          ("emplog", 6),
          ("eventlog", 5),
          ("logall", 11),
          ("measlog", 7),
          ("noaction", 0),
          ("scrtylog", 4))
    )





class SwitchType(Integer32):
    """Custom type SwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("international", 1),
          ("national", 0))
    )





class LinkType(Integer32):
    """Custom type LinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("speed-56K", 53),
          ("speed-64K", 54))
    )





class LogType(Integer32):
    """Custom type LogType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(48,
              49)
        )
    )
    namedValues = NamedValues(
        *(("off", 48),
          ("on", 49))
    )





class EnableTrace(Integer32):
    """Custom type EnableTrace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )





class TrunkState(Integer32):
    """Custom type TrunkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cP-Busy", 1),
          ("idle", 0),
          ("maintainance-Busy", 2),
          ("unEquipped", 255))
    )





class MeasPurgeFlag(Integer32):
    """Custom type MeasPurgeFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("autoOff", 0),
          ("autoOn", 1))
    )





class E1MultiFrame(Integer32):
    """Custom type E1MultiFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cas", 1),
          ("ccs", 2))
    )





class E1CRC4(Integer32):
    """Custom type E1CRC4 based on Integer32"""
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





class TransClkSrc(Integer32):
    """Custom type TransClkSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("loopTiming", 1))
    )





class DS1LineType(Integer32):
    """Custom type DS1LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d4", 2),
          ("esF", 1))
    )





class DS1LineCoding(Integer32):
    """Custom type DS1LineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 2),
          ("b8zs", 1))
    )





class DS1LBO(Integer32):
    """Custom type DS1LBO based on Integer32"""
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
        *(("negative15Db", 7),
          ("negative22-5Db", 8),
          ("negative7-5Db", 6),
          ("upTo133Feet", 1),
          ("upTo266Feet", 2),
          ("upTo399Feet", 3),
          ("upTo533Feet", 4),
          ("upTo655Feet", 5))
    )





class DS3LineType(Integer32):
    """Custom type DS3LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbitParity", 1),
          ("clearChannel", 2))
    )





class DS3LBO(Integer32):
    """Custom type DS3LBO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )





class DS3ATMCellMap(Integer32):
    """Custom type DS3ATMCellMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("directMapping", 2),
          ("plcp", 1))
    )





class TimerType(Integer32):
    """Custom type TimerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 1),
          ("itu", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Armillaire_ObjectIdentity = ObjectIdentity
armillaire = _Armillaire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1)
)
_Armillaire2000_ObjectIdentity = ObjectIdentity
armillaire2000 = _Armillaire2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2)
)
_SwitchInfo_ObjectIdentity = ObjectIdentity
switchInfo = _SwitchInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1)
)
_SwitchGenInfoGrp_ObjectIdentity = ObjectIdentity
switchGenInfoGrp = _SwitchGenInfoGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 1)
)
_SwitchName_Type = NameString
_SwitchName_Object = MibScalar
switchName = _SwitchName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 1, 1),
    _SwitchName_Type()
)
switchName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchName.setStatus("mandatory")


class _SwitchDescr_Type(DisplayString):
    """Custom type switchDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwitchDescr_Type.__name__ = "DisplayString"
_SwitchDescr_Object = MibScalar
switchDescr = _SwitchDescr_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 1, 2),
    _SwitchDescr_Type()
)
switchDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchDescr.setStatus("mandatory")


class _SwitchLocation_Type(DisplayString):
    """Custom type switchLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwitchLocation_Type.__name__ = "DisplayString"
_SwitchLocation_Object = MibScalar
switchLocation = _SwitchLocation_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 1, 3),
    _SwitchLocation_Type()
)
switchLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchLocation.setStatus("mandatory")


class _SwitchContact_Type(DisplayString):
    """Custom type switchContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_SwitchContact_Type.__name__ = "DisplayString"
_SwitchContact_Object = MibScalar
switchContact = _SwitchContact_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 1, 4),
    _SwitchContact_Type()
)
switchContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchContact.setStatus("mandatory")
_SwitchIPAddr_Type = IpAddress
_SwitchIPAddr_Object = MibScalar
switchIPAddr = _SwitchIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 1, 5),
    _SwitchIPAddr_Type()
)
switchIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIPAddr.setStatus("mandatory")
_SwitchUpTime_Type = TimeTicks
_SwitchUpTime_Object = MibScalar
switchUpTime = _SwitchUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 1, 6),
    _SwitchUpTime_Type()
)
switchUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchUpTime.setStatus("mandatory")


class _SwitchVersion_Type(DisplayString):
    """Custom type switchVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_SwitchVersion_Type.__name__ = "DisplayString"
_SwitchVersion_Object = MibScalar
switchVersion = _SwitchVersion_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 1, 7),
    _SwitchVersion_Type()
)
switchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchVersion.setStatus("mandatory")


class _SwitchVerDescr_Type(DisplayString):
    """Custom type switchVerDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwitchVerDescr_Type.__name__ = "DisplayString"
_SwitchVerDescr_Object = MibScalar
switchVerDescr = _SwitchVerDescr_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 1, 8),
    _SwitchVerDescr_Type()
)
switchVerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchVerDescr.setStatus("mandatory")


class _SystemDescr_Type(DisplayString):
    """Custom type systemDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SystemDescr_Type.__name__ = "DisplayString"
_SystemDescr_Object = MibScalar
systemDescr = _SystemDescr_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 1, 9),
    _SystemDescr_Type()
)
systemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDescr.setStatus("mandatory")
_SwitchType_Type = SwitchType
_SwitchType_Object = MibScalar
switchType = _SwitchType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 1, 10),
    _SwitchType_Type()
)
switchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchType.setStatus("mandatory")
_SwitchNameStatus_Type = RowStatus
_SwitchNameStatus_Object = MibScalar
switchNameStatus = _SwitchNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 1, 11),
    _SwitchNameStatus_Type()
)
switchNameStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchNameStatus.setStatus("mandatory")
_SwitchPcInfo_ObjectIdentity = ObjectIdentity
switchPcInfo = _SwitchPcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 2)
)
_SwitchPcInfoTable_Object = MibTable
switchPcInfoTable = _SwitchPcInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    switchPcInfoTable.setStatus("mandatory")
_SwitchPcEntry_Object = MibTableRow
switchPcEntry = _SwitchPcEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 2, 1, 1)
)
switchPcEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "switchPc"),
)
if mibBuilder.loadTexts:
    switchPcEntry.setStatus("mandatory")


class _SwitchPc_Type(Integer32):
    """Custom type switchPc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_SwitchPc_Type.__name__ = "Integer32"
_SwitchPc_Object = MibTableColumn
switchPc = _SwitchPc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 2, 1, 1, 1),
    _SwitchPc_Type()
)
switchPc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchPc.setStatus("mandatory")
_SwitchPcMode_Type = Standard
_SwitchPcMode_Object = MibTableColumn
switchPcMode = _SwitchPcMode_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 2, 1, 1, 2),
    _SwitchPcMode_Type()
)
switchPcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchPcMode.setStatus("mandatory")
_SwitchPcStatus_Type = RowStatus
_SwitchPcStatus_Object = MibTableColumn
switchPcStatus = _SwitchPcStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 2, 1, 1, 3),
    _SwitchPcStatus_Type()
)
switchPcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchPcStatus.setStatus("mandatory")
_SwitchUsrInfo_ObjectIdentity = ObjectIdentity
switchUsrInfo = _SwitchUsrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 3)
)
_SwitchUserCfgTable_Object = MibTable
switchUserCfgTable = _SwitchUserCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    switchUserCfgTable.setStatus("mandatory")
_SwitchUserCfgEntry_Object = MibTableRow
switchUserCfgEntry = _SwitchUserCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 3, 1, 1)
)
switchUserCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "switchUserId"),
)
if mibBuilder.loadTexts:
    switchUserCfgEntry.setStatus("mandatory")
_SwitchUserId_Type = Integer32
_SwitchUserId_Object = MibTableColumn
switchUserId = _SwitchUserId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 3, 1, 1, 1),
    _SwitchUserId_Type()
)
switchUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchUserId.setStatus("mandatory")
_SwitchUserName_Type = NameString
_SwitchUserName_Object = MibTableColumn
switchUserName = _SwitchUserName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 3, 1, 1, 2),
    _SwitchUserName_Type()
)
switchUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchUserName.setStatus("mandatory")
_SwitchUserPassword_Type = NameString
_SwitchUserPassword_Object = MibTableColumn
switchUserPassword = _SwitchUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 3, 1, 1, 3),
    _SwitchUserPassword_Type()
)
switchUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchUserPassword.setStatus("mandatory")
_SwitchUserPriority_Type = UserLoginPriority
_SwitchUserPriority_Object = MibTableColumn
switchUserPriority = _SwitchUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 3, 1, 1, 4),
    _SwitchUserPriority_Type()
)
switchUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchUserPriority.setStatus("mandatory")
_SwitchUserStatus_Type = UserLoginStatus
_SwitchUserStatus_Object = MibTableColumn
switchUserStatus = _SwitchUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 3, 1, 1, 5),
    _SwitchUserStatus_Type()
)
switchUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchUserStatus.setStatus("mandatory")
_SwitchVersionGrp_ObjectIdentity = ObjectIdentity
switchVersionGrp = _SwitchVersionGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 4)
)
_SwitchVerLM_Type = DisplayString
_SwitchVerLM_Object = MibScalar
switchVerLM = _SwitchVerLM_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 4, 1),
    _SwitchVerLM_Type()
)
switchVerLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchVerLM.setStatus("mandatory")
_SwitchVerMTP2_Type = DisplayString
_SwitchVerMTP2_Object = MibScalar
switchVerMTP2 = _SwitchVerMTP2_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 4, 2),
    _SwitchVerMTP2_Type()
)
switchVerMTP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchVerMTP2.setStatus("mandatory")
_SwitchVerICC_Type = DisplayString
_SwitchVerICC_Object = MibScalar
switchVerICC = _SwitchVerICC_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 4, 3),
    _SwitchVerICC_Type()
)
switchVerICC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchVerICC.setStatus("mandatory")
_SwitchVerSIG_Type = DisplayString
_SwitchVerSIG_Object = MibScalar
switchVerSIG = _SwitchVerSIG_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 4, 4),
    _SwitchVerSIG_Type()
)
switchVerSIG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchVerSIG.setStatus("mandatory")
_SwitchVerISDN_Type = DisplayString
_SwitchVerISDN_Object = MibScalar
switchVerISDN = _SwitchVerISDN_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 4, 5),
    _SwitchVerISDN_Type()
)
switchVerISDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchVerISDN.setStatus("mandatory")
_SwitchVerSPHR_Type = DisplayString
_SwitchVerSPHR_Object = MibScalar
switchVerSPHR = _SwitchVerSPHR_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 1, 4, 6),
    _SwitchVerSPHR_Type()
)
switchVerSPHR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchVerSPHR.setStatus("mandatory")
_SwitchConfig_ObjectIdentity = ObjectIdentity
switchConfig = _SwitchConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2)
)
_Ss7_ObjectIdentity = ObjectIdentity
ss7 = _Ss7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1)
)
_Ss7Sig_ObjectIdentity = ObjectIdentity
ss7Sig = _Ss7Sig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1)
)
_Ss7LinkCfgTable_Object = MibTable
ss7LinkCfgTable = _Ss7LinkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ss7LinkCfgTable.setStatus("mandatory")
_Ss7LinkCfgEntry_Object = MibTableRow
ss7LinkCfgEntry = _Ss7LinkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 1, 1)
)
ss7LinkCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "ss7LinkName"),
)
if mibBuilder.loadTexts:
    ss7LinkCfgEntry.setStatus("mandatory")
_Ss7LinkName_Type = NameString
_Ss7LinkName_Object = MibTableColumn
ss7LinkName = _Ss7LinkName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 1, 1, 1),
    _Ss7LinkName_Type()
)
ss7LinkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7LinkName.setStatus("mandatory")


class _Ss7LinkId_Type(Integer32):
    """Custom type ss7LinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7LinkId_Type.__name__ = "Integer32"
_Ss7LinkId_Object = MibTableColumn
ss7LinkId = _Ss7LinkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 1, 1, 2),
    _Ss7LinkId_Type()
)
ss7LinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7LinkId.setStatus("mandatory")


class _Ss7LinkTrunkId_Type(Integer32):
    """Custom type ss7LinkTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7LinkTrunkId_Type.__name__ = "Integer32"
_Ss7LinkTrunkId_Object = MibTableColumn
ss7LinkTrunkId = _Ss7LinkTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 1, 1, 3),
    _Ss7LinkTrunkId_Type()
)
ss7LinkTrunkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7LinkTrunkId.setStatus("mandatory")


class _Ss7LinkChannel_Type(Integer32):
    """Custom type ss7LinkChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7LinkChannel_Type.__name__ = "Integer32"
_Ss7LinkChannel_Object = MibTableColumn
ss7LinkChannel = _Ss7LinkChannel_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 1, 1, 4),
    _Ss7LinkChannel_Type()
)
ss7LinkChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7LinkChannel.setStatus("mandatory")


class _Ss7LinkSlc_Type(Integer32):
    """Custom type ss7LinkSlc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Ss7LinkSlc_Type.__name__ = "Integer32"
_Ss7LinkSlc_Object = MibTableColumn
ss7LinkSlc = _Ss7LinkSlc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 1, 1, 5),
    _Ss7LinkSlc_Type()
)
ss7LinkSlc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7LinkSlc.setStatus("mandatory")
_Ss7LinkSpeed_Type = LinkType
_Ss7LinkSpeed_Object = MibTableColumn
ss7LinkSpeed = _Ss7LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 1, 1, 6),
    _Ss7LinkSpeed_Type()
)
ss7LinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7LinkSpeed.setStatus("mandatory")
_Ss7LinkMode_Type = Standard
_Ss7LinkMode_Object = MibTableColumn
ss7LinkMode = _Ss7LinkMode_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 1, 1, 7),
    _Ss7LinkMode_Type()
)
ss7LinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7LinkMode.setStatus("mandatory")
_Ss7LinkRowStatus_Type = RowStatus
_Ss7LinkRowStatus_Object = MibTableColumn
ss7LinkRowStatus = _Ss7LinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 1, 1, 8),
    _Ss7LinkRowStatus_Type()
)
ss7LinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7LinkRowStatus.setStatus("mandatory")
_Ss7LinkOpStatus_Type = LinkOpStatus
_Ss7LinkOpStatus_Object = MibTableColumn
ss7LinkOpStatus = _Ss7LinkOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 1, 1, 9),
    _Ss7LinkOpStatus_Type()
)
ss7LinkOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7LinkOpStatus.setStatus("mandatory")
_Ss7AtmLinkCfgTable_Object = MibTable
ss7AtmLinkCfgTable = _Ss7AtmLinkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ss7AtmLinkCfgTable.setStatus("mandatory")
_Ss7AtmLinkCfgEntry_Object = MibTableRow
ss7AtmLinkCfgEntry = _Ss7AtmLinkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 2, 1)
)
ss7AtmLinkCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "ss7AtmVpi"),
    (0, "ARMILLAIRE2000-MIB", "ss7AtmVci"),
)
if mibBuilder.loadTexts:
    ss7AtmLinkCfgEntry.setStatus("mandatory")


class _Ss7AtmVpi_Type(Integer32):
    """Custom type ss7AtmVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7AtmVpi_Type.__name__ = "Integer32"
_Ss7AtmVpi_Object = MibTableColumn
ss7AtmVpi = _Ss7AtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 2, 1, 1),
    _Ss7AtmVpi_Type()
)
ss7AtmVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7AtmVpi.setStatus("mandatory")


class _Ss7AtmVci_Type(Integer32):
    """Custom type ss7AtmVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7AtmVci_Type.__name__ = "Integer32"
_Ss7AtmVci_Object = MibTableColumn
ss7AtmVci = _Ss7AtmVci_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 2, 1, 2),
    _Ss7AtmVci_Type()
)
ss7AtmVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7AtmVci.setStatus("mandatory")


class _Ss7AtmLnkId_Type(Integer32):
    """Custom type ss7AtmLnkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7AtmLnkId_Type.__name__ = "Integer32"
_Ss7AtmLnkId_Object = MibTableColumn
ss7AtmLnkId = _Ss7AtmLnkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 2, 1, 3),
    _Ss7AtmLnkId_Type()
)
ss7AtmLnkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7AtmLnkId.setStatus("mandatory")


class _Ss7AtmXconnectId_Type(Integer32):
    """Custom type ss7AtmXconnectId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7AtmXconnectId_Type.__name__ = "Integer32"
_Ss7AtmXconnectId_Object = MibTableColumn
ss7AtmXconnectId = _Ss7AtmXconnectId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 2, 1, 4),
    _Ss7AtmXconnectId_Type()
)
ss7AtmXconnectId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7AtmXconnectId.setStatus("mandatory")


class _Ss7AtmSlotId_Type(Integer32):
    """Custom type ss7AtmSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7AtmSlotId_Type.__name__ = "Integer32"
_Ss7AtmSlotId_Object = MibTableColumn
ss7AtmSlotId = _Ss7AtmSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 2, 1, 5),
    _Ss7AtmSlotId_Type()
)
ss7AtmSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7AtmSlotId.setStatus("mandatory")


class _Ss7AtmPortId_Type(Integer32):
    """Custom type ss7AtmPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7AtmPortId_Type.__name__ = "Integer32"
_Ss7AtmPortId_Object = MibTableColumn
ss7AtmPortId = _Ss7AtmPortId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 2, 1, 6),
    _Ss7AtmPortId_Type()
)
ss7AtmPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7AtmPortId.setStatus("mandatory")


class _Ss7AtmChnlId_Type(Integer32):
    """Custom type ss7AtmChnlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7AtmChnlId_Type.__name__ = "Integer32"
_Ss7AtmChnlId_Object = MibTableColumn
ss7AtmChnlId = _Ss7AtmChnlId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 2, 1, 7),
    _Ss7AtmChnlId_Type()
)
ss7AtmChnlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7AtmChnlId.setStatus("mandatory")


class _Ss7AtmTrnkId_Type(Integer32):
    """Custom type ss7AtmTrnkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7AtmTrnkId_Type.__name__ = "Integer32"
_Ss7AtmTrnkId_Object = MibTableColumn
ss7AtmTrnkId = _Ss7AtmTrnkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 2, 1, 8),
    _Ss7AtmTrnkId_Type()
)
ss7AtmTrnkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7AtmTrnkId.setStatus("mandatory")
_Ss7AtmPhyType_Type = AtmIfType
_Ss7AtmPhyType_Object = MibTableColumn
ss7AtmPhyType = _Ss7AtmPhyType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 2, 1, 9),
    _Ss7AtmPhyType_Type()
)
ss7AtmPhyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7AtmPhyType.setStatus("mandatory")
_Ss7AtmLinkRowStatus_Type = RowStatus
_Ss7AtmLinkRowStatus_Object = MibTableColumn
ss7AtmLinkRowStatus = _Ss7AtmLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 2, 1, 10),
    _Ss7AtmLinkRowStatus_Type()
)
ss7AtmLinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7AtmLinkRowStatus.setStatus("mandatory")
_Ss7AtmLinkOpStatus_Type = LinkOpStatus
_Ss7AtmLinkOpStatus_Object = MibTableColumn
ss7AtmLinkOpStatus = _Ss7AtmLinkOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 2, 1, 11),
    _Ss7AtmLinkOpStatus_Type()
)
ss7AtmLinkOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7AtmLinkOpStatus.setStatus("mandatory")
_Ss7LinksetCfgTable_Object = MibTable
ss7LinksetCfgTable = _Ss7LinksetCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ss7LinksetCfgTable.setStatus("mandatory")
_Ss7LinksetCfgEntry_Object = MibTableRow
ss7LinksetCfgEntry = _Ss7LinksetCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 3, 1)
)
ss7LinksetCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "ss7LinksetLinkId"),
)
if mibBuilder.loadTexts:
    ss7LinksetCfgEntry.setStatus("mandatory")


class _Ss7LinksetLinkId_Type(Integer32):
    """Custom type ss7LinksetLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7LinksetLinkId_Type.__name__ = "Integer32"
_Ss7LinksetLinkId_Object = MibTableColumn
ss7LinksetLinkId = _Ss7LinksetLinkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 3, 1, 1),
    _Ss7LinksetLinkId_Type()
)
ss7LinksetLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7LinksetLinkId.setStatus("mandatory")


class _Ss7LinksetId_Type(Integer32):
    """Custom type ss7LinksetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Ss7LinksetId_Type.__name__ = "Integer32"
_Ss7LinksetId_Object = MibTableColumn
ss7LinksetId = _Ss7LinksetId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 3, 1, 2),
    _Ss7LinksetId_Type()
)
ss7LinksetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7LinksetId.setStatus("mandatory")
_Ss7LinksetName_Type = NameString
_Ss7LinksetName_Object = MibTableColumn
ss7LinksetName = _Ss7LinksetName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 3, 1, 3),
    _Ss7LinksetName_Type()
)
ss7LinksetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7LinksetName.setStatus("mandatory")


class _Ss7LinksetAdjDpc_Type(Integer32):
    """Custom type ss7LinksetAdjDpc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_Ss7LinksetAdjDpc_Type.__name__ = "Integer32"
_Ss7LinksetAdjDpc_Object = MibTableColumn
ss7LinksetAdjDpc = _Ss7LinksetAdjDpc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 3, 1, 4),
    _Ss7LinksetAdjDpc_Type()
)
ss7LinksetAdjDpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7LinksetAdjDpc.setStatus("mandatory")
_Ss7LinksetMode_Type = Standard
_Ss7LinksetMode_Object = MibTableColumn
ss7LinksetMode = _Ss7LinksetMode_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 3, 1, 5),
    _Ss7LinksetMode_Type()
)
ss7LinksetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7LinksetMode.setStatus("mandatory")
_Ss7LinksetRowStatus_Type = RowStatus
_Ss7LinksetRowStatus_Object = MibTableColumn
ss7LinksetRowStatus = _Ss7LinksetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 3, 1, 6),
    _Ss7LinksetRowStatus_Type()
)
ss7LinksetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7LinksetRowStatus.setStatus("mandatory")
_Ss7LinksetOpStatus_Type = LinkSetOpStatus
_Ss7LinksetOpStatus_Object = MibTableColumn
ss7LinksetOpStatus = _Ss7LinksetOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 3, 1, 7),
    _Ss7LinksetOpStatus_Type()
)
ss7LinksetOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7LinksetOpStatus.setStatus("mandatory")
_Ss7LinksetMgmtTable_Object = MibTable
ss7LinksetMgmtTable = _Ss7LinksetMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ss7LinksetMgmtTable.setStatus("mandatory")
_Ss7LinksetMgmtEntry_Object = MibTableRow
ss7LinksetMgmtEntry = _Ss7LinksetMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 4, 1)
)
ss7LinksetMgmtEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "linksetId"),
)
if mibBuilder.loadTexts:
    ss7LinksetMgmtEntry.setStatus("mandatory")
_LinksetId_Type = Integer32
_LinksetId_Object = MibTableColumn
linksetId = _LinksetId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 4, 1, 1),
    _LinksetId_Type()
)
linksetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linksetId.setStatus("mandatory")
_LinksetLevel_Type = Level
_LinksetLevel_Object = MibTableColumn
linksetLevel = _LinksetLevel_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 4, 1, 2),
    _LinksetLevel_Type()
)
linksetLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linksetLevel.setStatus("mandatory")
_LinksetMgmntCmd_Type = LinkSetControlStatus
_LinksetMgmntCmd_Object = MibTableColumn
linksetMgmntCmd = _LinksetMgmntCmd_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 4, 1, 3),
    _LinksetMgmntCmd_Type()
)
linksetMgmntCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linksetMgmntCmd.setStatus("mandatory")
_Ss7LinkMgmntTable_Object = MibTable
ss7LinkMgmntTable = _Ss7LinkMgmntTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ss7LinkMgmntTable.setStatus("mandatory")
_Ss7LinkMgmntEntry_Object = MibTableRow
ss7LinkMgmntEntry = _Ss7LinkMgmntEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 5, 1)
)
ss7LinkMgmntEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "linkName"),
)
if mibBuilder.loadTexts:
    ss7LinkMgmntEntry.setStatus("mandatory")
_LinkName_Type = NameString
_LinkName_Object = MibTableColumn
linkName = _LinkName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 5, 1, 1),
    _LinkName_Type()
)
linkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkName.setStatus("mandatory")
_LinkMgmntCmd_Type = LinkControlStatus
_LinkMgmntCmd_Object = MibTableColumn
linkMgmntCmd = _LinkMgmntCmd_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 1, 5, 1, 2),
    _LinkMgmntCmd_Type()
)
linkMgmntCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkMgmntCmd.setStatus("mandatory")
_Ss7Br_ObjectIdentity = ObjectIdentity
ss7Br = _Ss7Br_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2)
)
_Ss7TrunkCfgTable_Object = MibTable
ss7TrunkCfgTable = _Ss7TrunkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ss7TrunkCfgTable.setStatus("mandatory")
_Ss7TrunkCfgEntry_Object = MibTableRow
ss7TrunkCfgEntry = _Ss7TrunkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1)
)
ss7TrunkCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "ss7TrunkId"),
)
if mibBuilder.loadTexts:
    ss7TrunkCfgEntry.setStatus("mandatory")


class _Ss7TrunkId_Type(Integer32):
    """Custom type ss7TrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7TrunkId_Type.__name__ = "Integer32"
_Ss7TrunkId_Object = MibTableColumn
ss7TrunkId = _Ss7TrunkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 1),
    _Ss7TrunkId_Type()
)
ss7TrunkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkId.setStatus("mandatory")
_Ss7TrunkName_Type = NameString
_Ss7TrunkName_Object = MibTableColumn
ss7TrunkName = _Ss7TrunkName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 2),
    _Ss7TrunkName_Type()
)
ss7TrunkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkName.setStatus("mandatory")


class _Ss7TrunkGrpId_Type(Integer32):
    """Custom type ss7TrunkGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7TrunkGrpId_Type.__name__ = "Integer32"
_Ss7TrunkGrpId_Object = MibTableColumn
ss7TrunkGrpId = _Ss7TrunkGrpId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 3),
    _Ss7TrunkGrpId_Type()
)
ss7TrunkGrpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkGrpId.setStatus("mandatory")


class _Ss7TrunkXconnectId_Type(Integer32):
    """Custom type ss7TrunkXconnectId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7TrunkXconnectId_Type.__name__ = "Integer32"
_Ss7TrunkXconnectId_Object = MibTableColumn
ss7TrunkXconnectId = _Ss7TrunkXconnectId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 4),
    _Ss7TrunkXconnectId_Type()
)
ss7TrunkXconnectId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkXconnectId.setStatus("mandatory")


class _Ss7TrunkSlotId_Type(Integer32):
    """Custom type ss7TrunkSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7TrunkSlotId_Type.__name__ = "Integer32"
_Ss7TrunkSlotId_Object = MibTableColumn
ss7TrunkSlotId = _Ss7TrunkSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 5),
    _Ss7TrunkSlotId_Type()
)
ss7TrunkSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkSlotId.setStatus("mandatory")


class _Ss7TrunkPortId_Type(Integer32):
    """Custom type ss7TrunkPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7TrunkPortId_Type.__name__ = "Integer32"
_Ss7TrunkPortId_Object = MibTableColumn
ss7TrunkPortId = _Ss7TrunkPortId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 6),
    _Ss7TrunkPortId_Type()
)
ss7TrunkPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkPortId.setStatus("mandatory")


class _Ss7TrunkOpc_Type(Integer32):
    """Custom type ss7TrunkOpc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_Ss7TrunkOpc_Type.__name__ = "Integer32"
_Ss7TrunkOpc_Object = MibTableColumn
ss7TrunkOpc = _Ss7TrunkOpc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 7),
    _Ss7TrunkOpc_Type()
)
ss7TrunkOpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkOpc.setStatus("mandatory")


class _Ss7TrunkDpc_Type(Integer32):
    """Custom type ss7TrunkDpc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_Ss7TrunkDpc_Type.__name__ = "Integer32"
_Ss7TrunkDpc_Object = MibTableColumn
ss7TrunkDpc = _Ss7TrunkDpc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 8),
    _Ss7TrunkDpc_Type()
)
ss7TrunkDpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkDpc.setStatus("mandatory")
_Ss7TrunkPhyType_Type = IfType
_Ss7TrunkPhyType_Object = MibTableColumn
ss7TrunkPhyType = _Ss7TrunkPhyType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 9),
    _Ss7TrunkPhyType_Type()
)
ss7TrunkPhyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkPhyType.setStatus("mandatory")
_Ss7TrunkMode_Type = Standard
_Ss7TrunkMode_Object = MibTableColumn
ss7TrunkMode = _Ss7TrunkMode_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 10),
    _Ss7TrunkMode_Type()
)
ss7TrunkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkMode.setStatus("mandatory")
_Ss7TrunkE1MultiFrame_Type = E1MultiFrame
_Ss7TrunkE1MultiFrame_Object = MibTableColumn
ss7TrunkE1MultiFrame = _Ss7TrunkE1MultiFrame_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 11),
    _Ss7TrunkE1MultiFrame_Type()
)
ss7TrunkE1MultiFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkE1MultiFrame.setStatus("mandatory")
_Ss7TrunkE1CRC4_Type = E1CRC4
_Ss7TrunkE1CRC4_Object = MibTableColumn
ss7TrunkE1CRC4 = _Ss7TrunkE1CRC4_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 12),
    _Ss7TrunkE1CRC4_Type()
)
ss7TrunkE1CRC4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkE1CRC4.setStatus("mandatory")
_Ss7TrunkE1TransClk_Type = TransClkSrc
_Ss7TrunkE1TransClk_Object = MibTableColumn
ss7TrunkE1TransClk = _Ss7TrunkE1TransClk_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 13),
    _Ss7TrunkE1TransClk_Type()
)
ss7TrunkE1TransClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkE1TransClk.setStatus("mandatory")
_Ss7TrunkDS1LineType_Type = DS1LineType
_Ss7TrunkDS1LineType_Object = MibTableColumn
ss7TrunkDS1LineType = _Ss7TrunkDS1LineType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 14),
    _Ss7TrunkDS1LineType_Type()
)
ss7TrunkDS1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkDS1LineType.setStatus("mandatory")
_Ss7TrunkDS1LineCoding_Type = DS1LineCoding
_Ss7TrunkDS1LineCoding_Object = MibTableColumn
ss7TrunkDS1LineCoding = _Ss7TrunkDS1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 15),
    _Ss7TrunkDS1LineCoding_Type()
)
ss7TrunkDS1LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkDS1LineCoding.setStatus("mandatory")
_Ss7TrunkDS1TransClkSrc_Type = TransClkSrc
_Ss7TrunkDS1TransClkSrc_Object = MibTableColumn
ss7TrunkDS1TransClkSrc = _Ss7TrunkDS1TransClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 16),
    _Ss7TrunkDS1TransClkSrc_Type()
)
ss7TrunkDS1TransClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkDS1TransClkSrc.setStatus("mandatory")
_Ss7TrunkDS1LBO_Type = DS1LBO
_Ss7TrunkDS1LBO_Object = MibTableColumn
ss7TrunkDS1LBO = _Ss7TrunkDS1LBO_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 17),
    _Ss7TrunkDS1LBO_Type()
)
ss7TrunkDS1LBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkDS1LBO.setStatus("mandatory")
_Ss7TrunkDS3LineType_Type = DS3LineType
_Ss7TrunkDS3LineType_Object = MibTableColumn
ss7TrunkDS3LineType = _Ss7TrunkDS3LineType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 18),
    _Ss7TrunkDS3LineType_Type()
)
ss7TrunkDS3LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkDS3LineType.setStatus("mandatory")
_Ss7TrunkDS3TransClkSrc_Type = TransClkSrc
_Ss7TrunkDS3TransClkSrc_Object = MibTableColumn
ss7TrunkDS3TransClkSrc = _Ss7TrunkDS3TransClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 19),
    _Ss7TrunkDS3TransClkSrc_Type()
)
ss7TrunkDS3TransClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkDS3TransClkSrc.setStatus("mandatory")
_Ss7TrunkDS3LBO_Type = DS3LBO
_Ss7TrunkDS3LBO_Object = MibTableColumn
ss7TrunkDS3LBO = _Ss7TrunkDS3LBO_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 20),
    _Ss7TrunkDS3LBO_Type()
)
ss7TrunkDS3LBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkDS3LBO.setStatus("mandatory")
_Ss7TrunkDS3DS1LineType_Type = DS1LineType
_Ss7TrunkDS3DS1LineType_Object = MibTableColumn
ss7TrunkDS3DS1LineType = _Ss7TrunkDS3DS1LineType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 21),
    _Ss7TrunkDS3DS1LineType_Type()
)
ss7TrunkDS3DS1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkDS3DS1LineType.setStatus("mandatory")
_Ss7TrunkDS3DS1TransClkSrc_Type = TransClkSrc
_Ss7TrunkDS3DS1TransClkSrc_Object = MibTableColumn
ss7TrunkDS3DS1TransClkSrc = _Ss7TrunkDS3DS1TransClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 22),
    _Ss7TrunkDS3DS1TransClkSrc_Type()
)
ss7TrunkDS3DS1TransClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkDS3DS1TransClkSrc.setStatus("mandatory")
_Ss7TrunkOC3TransClkSrc_Type = TransClkSrc
_Ss7TrunkOC3TransClkSrc_Object = MibTableColumn
ss7TrunkOC3TransClkSrc = _Ss7TrunkOC3TransClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 23),
    _Ss7TrunkOC3TransClkSrc_Type()
)
ss7TrunkOC3TransClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkOC3TransClkSrc.setStatus("mandatory")
_Ss7TrunkUNCHE3TransClkSrc_Type = TransClkSrc
_Ss7TrunkUNCHE3TransClkSrc_Object = MibTableColumn
ss7TrunkUNCHE3TransClkSrc = _Ss7TrunkUNCHE3TransClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 24),
    _Ss7TrunkUNCHE3TransClkSrc_Type()
)
ss7TrunkUNCHE3TransClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkUNCHE3TransClkSrc.setStatus("mandatory")
_Ss7TrunkDS3ATMLineType_Type = DS3LineType
_Ss7TrunkDS3ATMLineType_Object = MibTableColumn
ss7TrunkDS3ATMLineType = _Ss7TrunkDS3ATMLineType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 25),
    _Ss7TrunkDS3ATMLineType_Type()
)
ss7TrunkDS3ATMLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkDS3ATMLineType.setStatus("mandatory")
_Ss7TrunkDS3ATMCellMap_Type = DS3ATMCellMap
_Ss7TrunkDS3ATMCellMap_Object = MibTableColumn
ss7TrunkDS3ATMCellMap = _Ss7TrunkDS3ATMCellMap_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 26),
    _Ss7TrunkDS3ATMCellMap_Type()
)
ss7TrunkDS3ATMCellMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkDS3ATMCellMap.setStatus("mandatory")
_Ss7TrunkDS3ATMTransClkSrc_Type = TransClkSrc
_Ss7TrunkDS3ATMTransClkSrc_Object = MibTableColumn
ss7TrunkDS3ATMTransClkSrc = _Ss7TrunkDS3ATMTransClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 27),
    _Ss7TrunkDS3ATMTransClkSrc_Type()
)
ss7TrunkDS3ATMTransClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkDS3ATMTransClkSrc.setStatus("mandatory")
_Ss7TrunkDS3ATMLBO_Type = DS3LBO
_Ss7TrunkDS3ATMLBO_Object = MibTableColumn
ss7TrunkDS3ATMLBO = _Ss7TrunkDS3ATMLBO_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 28),
    _Ss7TrunkDS3ATMLBO_Type()
)
ss7TrunkDS3ATMLBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkDS3ATMLBO.setStatus("mandatory")
_Ss7TrunkRowStatus_Type = RowStatus
_Ss7TrunkRowStatus_Object = MibTableColumn
ss7TrunkRowStatus = _Ss7TrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 29),
    _Ss7TrunkRowStatus_Type()
)
ss7TrunkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7TrunkRowStatus.setStatus("mandatory")
_Ss7TrunkOpStatus_Type = OpStatus
_Ss7TrunkOpStatus_Object = MibTableColumn
ss7TrunkOpStatus = _Ss7TrunkOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 1, 1, 30),
    _Ss7TrunkOpStatus_Type()
)
ss7TrunkOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7TrunkOpStatus.setStatus("mandatory")
_Ss7CktCfgTable_Object = MibTable
ss7CktCfgTable = _Ss7CktCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ss7CktCfgTable.setStatus("mandatory")
_Ss7CktCfgEntry_Object = MibTableRow
ss7CktCfgEntry = _Ss7CktCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1)
)
ss7CktCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "ss7CktTrunkId"),
    (0, "ARMILLAIRE2000-MIB", "ss7CktChnlId"),
)
if mibBuilder.loadTexts:
    ss7CktCfgEntry.setStatus("mandatory")


class _Ss7CktTrunkId_Type(Integer32):
    """Custom type ss7CktTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7CktTrunkId_Type.__name__ = "Integer32"
_Ss7CktTrunkId_Object = MibTableColumn
ss7CktTrunkId = _Ss7CktTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 1),
    _Ss7CktTrunkId_Type()
)
ss7CktTrunkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktTrunkId.setStatus("mandatory")


class _Ss7CktChnlId_Type(Integer32):
    """Custom type ss7CktChnlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7CktChnlId_Type.__name__ = "Integer32"
_Ss7CktChnlId_Object = MibTableColumn
ss7CktChnlId = _Ss7CktChnlId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 2),
    _Ss7CktChnlId_Type()
)
ss7CktChnlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktChnlId.setStatus("mandatory")


class _Ss7CktId_Type(Integer32):
    """Custom type ss7CktId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Ss7CktId_Type.__name__ = "Integer32"
_Ss7CktId_Object = MibTableColumn
ss7CktId = _Ss7CktId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 3),
    _Ss7CktId_Type()
)
ss7CktId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7CktId.setStatus("mandatory")


class _Ss7CktDpc_Type(Integer32):
    """Custom type ss7CktDpc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_Ss7CktDpc_Type.__name__ = "Integer32"
_Ss7CktDpc_Object = MibTableColumn
ss7CktDpc = _Ss7CktDpc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 4),
    _Ss7CktDpc_Type()
)
ss7CktDpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktDpc.setStatus("mandatory")


class _Ss7CktCic_Type(Integer32):
    """Custom type ss7CktCic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_Ss7CktCic_Type.__name__ = "Integer32"
_Ss7CktCic_Object = MibTableColumn
ss7CktCic = _Ss7CktCic_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 5),
    _Ss7CktCic_Type()
)
ss7CktCic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktCic.setStatus("mandatory")
_Ss7CktDir_Type = Direction
_Ss7CktDir_Object = MibTableColumn
ss7CktDir = _Ss7CktDir_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 6),
    _Ss7CktDir_Type()
)
ss7CktDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktDir.setStatus("mandatory")


class _Ss7CktPriority_Type(Integer32):
    """Custom type ss7CktPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7CktPriority_Type.__name__ = "Integer32"
_Ss7CktPriority_Object = MibTableColumn
ss7CktPriority = _Ss7CktPriority_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 7),
    _Ss7CktPriority_Type()
)
ss7CktPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktPriority.setStatus("mandatory")


class _Ss7CktT3_Type(Integer32):
    """Custom type ss7CktT3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_Ss7CktT3_Type.__name__ = "Integer32"
_Ss7CktT3_Object = MibTableColumn
ss7CktT3 = _Ss7CktT3_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 8),
    _Ss7CktT3_Type()
)
ss7CktT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktT3.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7CktT3.setUnits("sec")


class _Ss7CktT12_Type(Integer32):
    """Custom type ss7CktT12 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 60000),
    )


_Ss7CktT12_Type.__name__ = "Integer32"
_Ss7CktT12_Object = MibTableColumn
ss7CktT12 = _Ss7CktT12_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 9),
    _Ss7CktT12_Type()
)
ss7CktT12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktT12.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7CktT12.setUnits("ms")


class _Ss7CktT13_Type(Integer32):
    """Custom type ss7CktT13 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_Ss7CktT13_Type.__name__ = "Integer32"
_Ss7CktT13_Object = MibTableColumn
ss7CktT13 = _Ss7CktT13_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 10),
    _Ss7CktT13_Type()
)
ss7CktT13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktT13.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7CktT13.setUnits("sec")


class _Ss7CktT14_Type(Integer32):
    """Custom type ss7CktT14 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 60000),
    )


_Ss7CktT14_Type.__name__ = "Integer32"
_Ss7CktT14_Object = MibTableColumn
ss7CktT14 = _Ss7CktT14_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 11),
    _Ss7CktT14_Type()
)
ss7CktT14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktT14.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7CktT14.setUnits("ms")


class _Ss7CktT15_Type(Integer32):
    """Custom type ss7CktT15 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_Ss7CktT15_Type.__name__ = "Integer32"
_Ss7CktT15_Object = MibTableColumn
ss7CktT15 = _Ss7CktT15_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 12),
    _Ss7CktT15_Type()
)
ss7CktT15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktT15.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7CktT15.setUnits("sec")


class _Ss7CktT16_Type(Integer32):
    """Custom type ss7CktT16 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 60000),
    )


_Ss7CktT16_Type.__name__ = "Integer32"
_Ss7CktT16_Object = MibTableColumn
ss7CktT16 = _Ss7CktT16_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 13),
    _Ss7CktT16_Type()
)
ss7CktT16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktT16.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7CktT16.setUnits("ms")


class _Ss7CktT17_Type(Integer32):
    """Custom type ss7CktT17 based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_Ss7CktT17_Type.__name__ = "Integer32"
_Ss7CktT17_Object = MibTableColumn
ss7CktT17 = _Ss7CktT17_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 14),
    _Ss7CktT17_Type()
)
ss7CktT17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktT17.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7CktT17.setUnits("sec")


class _Ss7CktTVal_Type(Integer32):
    """Custom type ss7CktTVal based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 10000),
    )


_Ss7CktTVal_Type.__name__ = "Integer32"
_Ss7CktTVal_Object = MibTableColumn
ss7CktTVal = _Ss7CktTVal_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 15),
    _Ss7CktTVal_Type()
)
ss7CktTVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktTVal.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7CktTVal.setUnits("ms")
_Ss7CktRowStatus_Type = CktRowStatus
_Ss7CktRowStatus_Object = MibTableColumn
ss7CktRowStatus = _Ss7CktRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 16),
    _Ss7CktRowStatus_Type()
)
ss7CktRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktRowStatus.setStatus("mandatory")
_Ss7CktOpStatus_Type = CktOpStatus
_Ss7CktOpStatus_Object = MibTableColumn
ss7CktOpStatus = _Ss7CktOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 2, 1, 17),
    _Ss7CktOpStatus_Type()
)
ss7CktOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7CktOpStatus.setStatus("mandatory")
_Ss7CICTimerTable_Object = MibTable
ss7CICTimerTable = _Ss7CICTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ss7CICTimerTable.setStatus("mandatory")
_Ss7CicTmrEntry_Object = MibTableRow
ss7CicTmrEntry = _Ss7CicTmrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 3, 1)
)
ss7CicTmrEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "ss7CktTmrDpc"),
    (0, "ARMILLAIRE2000-MIB", "ss7CktTmrCic"),
)
if mibBuilder.loadTexts:
    ss7CicTmrEntry.setStatus("mandatory")


class _Ss7CktTmrDpc_Type(Integer32):
    """Custom type ss7CktTmrDpc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_Ss7CktTmrDpc_Type.__name__ = "Integer32"
_Ss7CktTmrDpc_Object = MibTableColumn
ss7CktTmrDpc = _Ss7CktTmrDpc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 3, 1, 1),
    _Ss7CktTmrDpc_Type()
)
ss7CktTmrDpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktTmrDpc.setStatus("mandatory")


class _Ss7CktTmrCic_Type(Integer32):
    """Custom type ss7CktTmrCic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7CktTmrCic_Type.__name__ = "Integer32"
_Ss7CktTmrCic_Object = MibTableColumn
ss7CktTmrCic = _Ss7CktTmrCic_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 3, 1, 2),
    _Ss7CktTmrCic_Type()
)
ss7CktTmrCic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktTmrCic.setStatus("mandatory")


class _Ss7CktTmrT3_Type(Integer32):
    """Custom type ss7CktTmrT3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7CktTmrT3_Type.__name__ = "Integer32"
_Ss7CktTmrT3_Object = MibTableColumn
ss7CktTmrT3 = _Ss7CktTmrT3_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 3, 1, 3),
    _Ss7CktTmrT3_Type()
)
ss7CktTmrT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktTmrT3.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7CktTmrT3.setUnits("ms")


class _Ss7CktTmrT12_Type(Integer32):
    """Custom type ss7CktTmrT12 based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7CktTmrT12_Type.__name__ = "Integer32"
_Ss7CktTmrT12_Object = MibTableColumn
ss7CktTmrT12 = _Ss7CktTmrT12_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 3, 1, 4),
    _Ss7CktTmrT12_Type()
)
ss7CktTmrT12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktTmrT12.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7CktTmrT12.setUnits("ms")


class _Ss7CktTmrT13_Type(Integer32):
    """Custom type ss7CktTmrT13 based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7CktTmrT13_Type.__name__ = "Integer32"
_Ss7CktTmrT13_Object = MibTableColumn
ss7CktTmrT13 = _Ss7CktTmrT13_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 3, 1, 5),
    _Ss7CktTmrT13_Type()
)
ss7CktTmrT13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktTmrT13.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7CktTmrT13.setUnits("ms")


class _Ss7CktTmrT14_Type(Integer32):
    """Custom type ss7CktTmrT14 based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7CktTmrT14_Type.__name__ = "Integer32"
_Ss7CktTmrT14_Object = MibTableColumn
ss7CktTmrT14 = _Ss7CktTmrT14_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 3, 1, 6),
    _Ss7CktTmrT14_Type()
)
ss7CktTmrT14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktTmrT14.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7CktTmrT14.setUnits("ms")


class _Ss7CktTmrT15_Type(Integer32):
    """Custom type ss7CktTmrT15 based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7CktTmrT15_Type.__name__ = "Integer32"
_Ss7CktTmrT15_Object = MibTableColumn
ss7CktTmrT15 = _Ss7CktTmrT15_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 3, 1, 7),
    _Ss7CktTmrT15_Type()
)
ss7CktTmrT15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktTmrT15.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7CktTmrT15.setUnits("ms")


class _Ss7CktTmrT16_Type(Integer32):
    """Custom type ss7CktTmrT16 based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7CktTmrT16_Type.__name__ = "Integer32"
_Ss7CktTmrT16_Object = MibTableColumn
ss7CktTmrT16 = _Ss7CktTmrT16_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 3, 1, 8),
    _Ss7CktTmrT16_Type()
)
ss7CktTmrT16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktTmrT16.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7CktTmrT16.setUnits("ms")


class _Ss7CktTmrT17_Type(Integer32):
    """Custom type ss7CktTmrT17 based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7CktTmrT17_Type.__name__ = "Integer32"
_Ss7CktTmrT17_Object = MibTableColumn
ss7CktTmrT17 = _Ss7CktTmrT17_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 3, 1, 9),
    _Ss7CktTmrT17_Type()
)
ss7CktTmrT17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktTmrT17.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7CktTmrT17.setUnits("ms")


class _Ss7CktTmrTVal_Type(Integer32):
    """Custom type ss7CktTmrTVal based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7CktTmrTVal_Type.__name__ = "Integer32"
_Ss7CktTmrTVal_Object = MibTableColumn
ss7CktTmrTVal = _Ss7CktTmrTVal_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 3, 1, 10),
    _Ss7CktTmrTVal_Type()
)
ss7CktTmrTVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktTmrTVal.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7CktTmrTVal.setUnits("ms")
_Ss7CktTmrRowStatus_Type = ModifyTmrStatus
_Ss7CktTmrRowStatus_Object = MibTableColumn
ss7CktTmrRowStatus = _Ss7CktTmrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 3, 1, 11),
    _Ss7CktTmrRowStatus_Type()
)
ss7CktTmrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktTmrRowStatus.setStatus("mandatory")
_Ss7BCktCfgTable_Object = MibTable
ss7BCktCfgTable = _Ss7BCktCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ss7BCktCfgTable.setStatus("mandatory")
_Ss7BCktCfgEntry_Object = MibTableRow
ss7BCktCfgEntry = _Ss7BCktCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1)
)
ss7BCktCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "ss7BCktVpi"),
    (0, "ARMILLAIRE2000-MIB", "ss7BCktVci"),
)
if mibBuilder.loadTexts:
    ss7BCktCfgEntry.setStatus("mandatory")


class _Ss7BCktVpi_Type(Integer32):
    """Custom type ss7BCktVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7BCktVpi_Type.__name__ = "Integer32"
_Ss7BCktVpi_Object = MibTableColumn
ss7BCktVpi = _Ss7BCktVpi_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 1),
    _Ss7BCktVpi_Type()
)
ss7BCktVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7BCktVpi.setStatus("mandatory")


class _Ss7BCktVci_Type(Integer32):
    """Custom type ss7BCktVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7BCktVci_Type.__name__ = "Integer32"
_Ss7BCktVci_Object = MibTableColumn
ss7BCktVci = _Ss7BCktVci_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 2),
    _Ss7BCktVci_Type()
)
ss7BCktVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7BCktVci.setStatus("mandatory")


class _Ss7BCktTrunkId_Type(Integer32):
    """Custom type ss7BCktTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7BCktTrunkId_Type.__name__ = "Integer32"
_Ss7BCktTrunkId_Object = MibTableColumn
ss7BCktTrunkId = _Ss7BCktTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 3),
    _Ss7BCktTrunkId_Type()
)
ss7BCktTrunkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7BCktTrunkId.setStatus("mandatory")


class _Ss7BCktDpc_Type(Integer32):
    """Custom type ss7BCktDpc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_Ss7BCktDpc_Type.__name__ = "Integer32"
_Ss7BCktDpc_Object = MibTableColumn
ss7BCktDpc = _Ss7BCktDpc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 4),
    _Ss7BCktDpc_Type()
)
ss7BCktDpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7BCktDpc.setStatus("mandatory")


class _Ss7BCktCic_Type(Integer32):
    """Custom type ss7BCktCic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_Ss7BCktCic_Type.__name__ = "Integer32"
_Ss7BCktCic_Object = MibTableColumn
ss7BCktCic = _Ss7BCktCic_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 5),
    _Ss7BCktCic_Type()
)
ss7BCktCic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7BCktCic.setStatus("mandatory")
_Ss7BCktDir_Type = Direction
_Ss7BCktDir_Object = MibTableColumn
ss7BCktDir = _Ss7BCktDir_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 6),
    _Ss7BCktDir_Type()
)
ss7BCktDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7BCktDir.setStatus("mandatory")


class _Ss7BCktPriority_Type(Integer32):
    """Custom type ss7BCktPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7BCktPriority_Type.__name__ = "Integer32"
_Ss7BCktPriority_Object = MibTableColumn
ss7BCktPriority = _Ss7BCktPriority_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 7),
    _Ss7BCktPriority_Type()
)
ss7BCktPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7BCktPriority.setStatus("mandatory")


class _Ss7BCktT3_Type(Integer32):
    """Custom type ss7BCktT3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7BCktT3_Type.__name__ = "Integer32"
_Ss7BCktT3_Object = MibTableColumn
ss7BCktT3 = _Ss7BCktT3_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 8),
    _Ss7BCktT3_Type()
)
ss7BCktT3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7BCktT3.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7BCktT3.setUnits("ms")


class _Ss7BCktT12_Type(Integer32):
    """Custom type ss7BCktT12 based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7BCktT12_Type.__name__ = "Integer32"
_Ss7BCktT12_Object = MibTableColumn
ss7BCktT12 = _Ss7BCktT12_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 9),
    _Ss7BCktT12_Type()
)
ss7BCktT12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7BCktT12.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7BCktT12.setUnits("ms")


class _Ss7BCktT13_Type(Integer32):
    """Custom type ss7BCktT13 based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7BCktT13_Type.__name__ = "Integer32"
_Ss7BCktT13_Object = MibTableColumn
ss7BCktT13 = _Ss7BCktT13_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 10),
    _Ss7BCktT13_Type()
)
ss7BCktT13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7BCktT13.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7BCktT13.setUnits("ms")


class _Ss7BCktT14_Type(Integer32):
    """Custom type ss7BCktT14 based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7BCktT14_Type.__name__ = "Integer32"
_Ss7BCktT14_Object = MibTableColumn
ss7BCktT14 = _Ss7BCktT14_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 11),
    _Ss7BCktT14_Type()
)
ss7BCktT14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7BCktT14.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7BCktT14.setUnits("ms")


class _Ss7BCktT15_Type(Integer32):
    """Custom type ss7BCktT15 based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7BCktT15_Type.__name__ = "Integer32"
_Ss7BCktT15_Object = MibTableColumn
ss7BCktT15 = _Ss7BCktT15_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 12),
    _Ss7BCktT15_Type()
)
ss7BCktT15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7BCktT15.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7BCktT15.setUnits("ms")


class _Ss7BCktT16_Type(Integer32):
    """Custom type ss7BCktT16 based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7BCktT16_Type.__name__ = "Integer32"
_Ss7BCktT16_Object = MibTableColumn
ss7BCktT16 = _Ss7BCktT16_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 13),
    _Ss7BCktT16_Type()
)
ss7BCktT16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7BCktT16.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7BCktT16.setUnits("ms")


class _Ss7BCktT17_Type(Integer32):
    """Custom type ss7BCktT17 based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7BCktT17_Type.__name__ = "Integer32"
_Ss7BCktT17_Object = MibTableColumn
ss7BCktT17 = _Ss7BCktT17_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 14),
    _Ss7BCktT17_Type()
)
ss7BCktT17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7BCktT17.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7BCktT17.setUnits("ms")


class _Ss7BCktTVal_Type(Integer32):
    """Custom type ss7BCktTVal based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7BCktTVal_Type.__name__ = "Integer32"
_Ss7BCktTVal_Object = MibTableColumn
ss7BCktTVal = _Ss7BCktTVal_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 15),
    _Ss7BCktTVal_Type()
)
ss7BCktTVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7BCktTVal.setStatus("mandatory")
if mibBuilder.loadTexts:
    ss7BCktTVal.setUnits("ms")
_Ss7BCktRowStatus_Type = CktRowStatus
_Ss7BCktRowStatus_Object = MibTableColumn
ss7BCktRowStatus = _Ss7BCktRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 16),
    _Ss7BCktRowStatus_Type()
)
ss7BCktRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7BCktRowStatus.setStatus("mandatory")
_Ss7BCktOpStatus_Type = CktOpStatus
_Ss7BCktOpStatus_Object = MibTableColumn
ss7BCktOpStatus = _Ss7BCktOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 4, 1, 17),
    _Ss7BCktOpStatus_Type()
)
ss7BCktOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7BCktOpStatus.setStatus("mandatory")
_Ss7CktMgmntGroup_ObjectIdentity = ObjectIdentity
ss7CktMgmntGroup = _Ss7CktMgmntGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 5)
)
_Ss7CktMgmntTable_Object = MibTable
ss7CktMgmntTable = _Ss7CktMgmntTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ss7CktMgmntTable.setStatus("mandatory")
_Ss7CktMgmntEntry_Object = MibTableRow
ss7CktMgmntEntry = _Ss7CktMgmntEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 5, 1, 1)
)
ss7CktMgmntEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "ss7CktMgmntTrnkId"),
    (0, "ARMILLAIRE2000-MIB", "ss7CktMgmntChnlId"),
)
if mibBuilder.loadTexts:
    ss7CktMgmntEntry.setStatus("mandatory")
_Ss7CktMgmntTrnkId_Type = Integer32
_Ss7CktMgmntTrnkId_Object = MibTableColumn
ss7CktMgmntTrnkId = _Ss7CktMgmntTrnkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 5, 1, 1, 1),
    _Ss7CktMgmntTrnkId_Type()
)
ss7CktMgmntTrnkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7CktMgmntTrnkId.setStatus("mandatory")
_Ss7CktMgmntChnlId_Type = Integer32
_Ss7CktMgmntChnlId_Object = MibTableColumn
ss7CktMgmntChnlId = _Ss7CktMgmntChnlId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 5, 1, 1, 2),
    _Ss7CktMgmntChnlId_Type()
)
ss7CktMgmntChnlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7CktMgmntChnlId.setStatus("mandatory")


class _Ss7CktMgmntRepNum_Type(Integer32):
    """Custom type ss7CktMgmntRepNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7CktMgmntRepNum_Type.__name__ = "Integer32"
_Ss7CktMgmntRepNum_Object = MibTableColumn
ss7CktMgmntRepNum = _Ss7CktMgmntRepNum_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 5, 1, 1, 3),
    _Ss7CktMgmntRepNum_Type()
)
ss7CktMgmntRepNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktMgmntRepNum.setStatus("mandatory")
_Ss7CktMgmntCmd_Type = BlockOperation
_Ss7CktMgmntCmd_Object = MibTableColumn
ss7CktMgmntCmd = _Ss7CktMgmntCmd_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 5, 1, 1, 4),
    _Ss7CktMgmntCmd_Type()
)
ss7CktMgmntCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktMgmntCmd.setStatus("mandatory")
_Ss7CICMgmntTable_Object = MibTable
ss7CICMgmntTable = _Ss7CICMgmntTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    ss7CICMgmntTable.setStatus("mandatory")
_Ss7CICMgmntEntry_Object = MibTableRow
ss7CICMgmntEntry = _Ss7CICMgmntEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 5, 2, 1)
)
ss7CICMgmntEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "ss7CktMgmtDPC"),
    (0, "ARMILLAIRE2000-MIB", "ss7CktMgmtCIC"),
)
if mibBuilder.loadTexts:
    ss7CICMgmntEntry.setStatus("mandatory")
_Ss7CktMgmtDPC_Type = Integer32
_Ss7CktMgmtDPC_Object = MibTableColumn
ss7CktMgmtDPC = _Ss7CktMgmtDPC_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 5, 2, 1, 1),
    _Ss7CktMgmtDPC_Type()
)
ss7CktMgmtDPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7CktMgmtDPC.setStatus("mandatory")
_Ss7CktMgmtCIC_Type = Integer32
_Ss7CktMgmtCIC_Object = MibTableColumn
ss7CktMgmtCIC = _Ss7CktMgmtCIC_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 5, 2, 1, 2),
    _Ss7CktMgmtCIC_Type()
)
ss7CktMgmtCIC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7CktMgmtCIC.setStatus("mandatory")


class _Ss7CktRepNum_Type(Integer32):
    """Custom type ss7CktRepNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7CktRepNum_Type.__name__ = "Integer32"
_Ss7CktRepNum_Object = MibTableColumn
ss7CktRepNum = _Ss7CktRepNum_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 5, 2, 1, 3),
    _Ss7CktRepNum_Type()
)
ss7CktRepNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CktRepNum.setStatus("mandatory")


class _Ss7CicRange_Type(Integer32):
    """Custom type ss7CicRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7CicRange_Type.__name__ = "Integer32"
_Ss7CicRange_Object = MibTableColumn
ss7CicRange = _Ss7CicRange_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 5, 2, 1, 4),
    _Ss7CicRange_Type()
)
ss7CicRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CicRange.setStatus("mandatory")
_Ss7CICMgmntCmd_Type = CircuitControlStatus
_Ss7CICMgmntCmd_Object = MibTableColumn
ss7CICMgmntCmd = _Ss7CICMgmntCmd_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 2, 5, 2, 1, 5),
    _Ss7CICMgmntCmd_Type()
)
ss7CICMgmntCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7CICMgmntCmd.setStatus("mandatory")
_Mtp2_ObjectIdentity = ObjectIdentity
mtp2 = _Mtp2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 3)
)
_Mtp2LinkTmrCfgTable_Object = MibTable
mtp2LinkTmrCfgTable = _Mtp2LinkTmrCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mtp2LinkTmrCfgTable.setStatus("mandatory")
_Mtp2LinkTmrCfgEntry_Object = MibTableRow
mtp2LinkTmrCfgEntry = _Mtp2LinkTmrCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 3, 1, 1)
)
mtp2LinkTmrCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "mtp2LinkId"),
)
if mibBuilder.loadTexts:
    mtp2LinkTmrCfgEntry.setStatus("mandatory")


class _Mtp2LinkId_Type(Integer32):
    """Custom type mtp2LinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Mtp2LinkId_Type.__name__ = "Integer32"
_Mtp2LinkId_Object = MibTableColumn
mtp2LinkId = _Mtp2LinkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 3, 1, 1, 1),
    _Mtp2LinkId_Type()
)
mtp2LinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp2LinkId.setStatus("mandatory")


class _Mtp2T1_Type(Integer32):
    """Custom type mtp2T1 based on Integer32"""
    defaultValue = 13000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(13000, 50000),
    )


_Mtp2T1_Type.__name__ = "Integer32"
_Mtp2T1_Object = MibTableColumn
mtp2T1 = _Mtp2T1_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 3, 1, 1, 2),
    _Mtp2T1_Type()
)
mtp2T1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp2T1.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp2T1.setUnits("ms")


class _Mtp2T2_Type(Integer32):
    """Custom type mtp2T2 based on Integer32"""
    defaultValue = 11500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 50000),
    )


_Mtp2T2_Type.__name__ = "Integer32"
_Mtp2T2_Object = MibTableColumn
mtp2T2 = _Mtp2T2_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 3, 1, 1, 3),
    _Mtp2T2_Type()
)
mtp2T2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp2T2.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp2T2.setUnits("ms")


class _Mtp2T3_Type(Integer32):
    """Custom type mtp2T3 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 15000),
    )


_Mtp2T3_Type.__name__ = "Integer32"
_Mtp2T3_Object = MibTableColumn
mtp2T3 = _Mtp2T3_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 3, 1, 1, 4),
    _Mtp2T3_Type()
)
mtp2T3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp2T3.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp2T3.setUnits("ms")


class _Mtp2T4n_Type(Integer32):
    """Custom type mtp2T4n based on Integer32"""
    defaultValue = 2070

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2070, 9500),
    )


_Mtp2T4n_Type.__name__ = "Integer32"
_Mtp2T4n_Object = MibTableColumn
mtp2T4n = _Mtp2T4n_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 3, 1, 1, 5),
    _Mtp2T4n_Type()
)
mtp2T4n.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp2T4n.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp2T4n.setUnits("ms")


class _Mtp2T4e_Type(Integer32):
    """Custom type mtp2T4e based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 600),
    )


_Mtp2T4e_Type.__name__ = "Integer32"
_Mtp2T4e_Object = MibTableColumn
mtp2T4e = _Mtp2T4e_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 3, 1, 1, 6),
    _Mtp2T4e_Type()
)
mtp2T4e.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp2T4e.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp2T4e.setUnits("ms")


class _Mtp2T5_Type(Integer32):
    """Custom type mtp2T5 based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 120),
    )


_Mtp2T5_Type.__name__ = "Integer32"
_Mtp2T5_Object = MibTableColumn
mtp2T5 = _Mtp2T5_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 3, 1, 1, 7),
    _Mtp2T5_Type()
)
mtp2T5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp2T5.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp2T5.setUnits("ms")


class _Mtp2T6_Type(Integer32):
    """Custom type mtp2T6 based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 6000),
    )


_Mtp2T6_Type.__name__ = "Integer32"
_Mtp2T6_Object = MibTableColumn
mtp2T6 = _Mtp2T6_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 3, 1, 1, 8),
    _Mtp2T6_Type()
)
mtp2T6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp2T6.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp2T6.setUnits("ms")


class _Mtp2T7_Type(Integer32):
    """Custom type mtp2T7 based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 2000),
    )


_Mtp2T7_Type.__name__ = "Integer32"
_Mtp2T7_Object = MibTableColumn
mtp2T7 = _Mtp2T7_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 3, 1, 1, 9),
    _Mtp2T7_Type()
)
mtp2T7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp2T7.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp2T7.setUnits("ms")
_Mtp2RowStatus_Type = TmrRowStatus
_Mtp2RowStatus_Object = MibTableColumn
mtp2RowStatus = _Mtp2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 3, 1, 1, 10),
    _Mtp2RowStatus_Type()
)
mtp2RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp2RowStatus.setStatus("mandatory")
_Mtp2OpStatus_Type = OpStatus
_Mtp2OpStatus_Object = MibTableColumn
mtp2OpStatus = _Mtp2OpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 3, 1, 1, 11),
    _Mtp2OpStatus_Type()
)
mtp2OpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtp2OpStatus.setStatus("mandatory")
_Mtp3_ObjectIdentity = ObjectIdentity
mtp3 = _Mtp3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4)
)
_Mtp3GenTmrCfgGroup_ObjectIdentity = ObjectIdentity
mtp3GenTmrCfgGroup = _Mtp3GenTmrCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 1)
)


class _Mtp3T15_Type(Integer32):
    """Custom type mtp3T15 based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 3000),
    )


_Mtp3T15_Type.__name__ = "Integer32"
_Mtp3T15_Object = MibScalar
mtp3T15 = _Mtp3T15_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 1, 1),
    _Mtp3T15_Type()
)
mtp3T15.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T15.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T15.setUnits("ms")


class _Mtp3T16_Type(Integer32):
    """Custom type mtp3T16 based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1400, 2000),
    )


_Mtp3T16_Type.__name__ = "Integer32"
_Mtp3T16_Object = MibScalar
mtp3T16 = _Mtp3T16_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 1, 2),
    _Mtp3T16_Type()
)
mtp3T16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T16.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T16.setUnits("ms")


class _Mtp3T18_Type(Integer32):
    """Custom type mtp3T18 based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Mtp3T18_Type.__name__ = "Integer32"
_Mtp3T18_Object = MibScalar
mtp3T18 = _Mtp3T18_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 1, 3),
    _Mtp3T18_Type()
)
mtp3T18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T18.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T18.setUnits("ms")


class _Mtp3T19_Type(Integer32):
    """Custom type mtp3T19 based on Integer32"""
    defaultValue = 67000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(67000, 69000),
    )


_Mtp3T19_Type.__name__ = "Integer32"
_Mtp3T19_Object = MibScalar
mtp3T19 = _Mtp3T19_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 1, 4),
    _Mtp3T19_Type()
)
mtp3T19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T19.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T19.setUnits("ms")


class _Mtp3T20_Type(Integer32):
    """Custom type mtp3T20 based on Integer32"""
    defaultValue = 590000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(59000, 61000),
    )


_Mtp3T20_Type.__name__ = "Integer32"
_Mtp3T20_Object = MibScalar
mtp3T20 = _Mtp3T20_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 1, 5),
    _Mtp3T20_Type()
)
mtp3T20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T20.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T20.setUnits("ms")


class _Mtp3T21_Type(Integer32):
    """Custom type mtp3T21 based on Integer32"""
    defaultValue = 63000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(63000, 65000),
    )


_Mtp3T21_Type.__name__ = "Integer32"
_Mtp3T21_Object = MibScalar
mtp3T21 = _Mtp3T21_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 1, 6),
    _Mtp3T21_Type()
)
mtp3T21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T21.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T21.setUnits("ms")


class _Mtp3T26_Type(Integer32):
    """Custom type mtp3T26 based on Integer32"""
    defaultValue = 12000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12000, 15000),
    )


_Mtp3T26_Type.__name__ = "Integer32"
_Mtp3T26_Object = MibScalar
mtp3T26 = _Mtp3T26_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 1, 7),
    _Mtp3T26_Type()
)
mtp3T26.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T26.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T26.setUnits("ms")


class _Mtp3T30_Type(Integer32):
    """Custom type mtp3T30 based on Integer32"""
    defaultValue = 30000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000, 35000),
    )


_Mtp3T30_Type.__name__ = "Integer32"
_Mtp3T30_Object = MibScalar
mtp3T30 = _Mtp3T30_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 1, 8),
    _Mtp3T30_Type()
)
mtp3T30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtp3T30.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T30.setUnits("ms")
_Mtp3GenTmrRowStatus_Type = ModifyTmrStatus
_Mtp3GenTmrRowStatus_Object = MibScalar
mtp3GenTmrRowStatus = _Mtp3GenTmrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 1, 9),
    _Mtp3GenTmrRowStatus_Type()
)
mtp3GenTmrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3GenTmrRowStatus.setStatus("mandatory")
_Mtp3LinkCfgTable_Object = MibTable
mtp3LinkCfgTable = _Mtp3LinkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    mtp3LinkCfgTable.setStatus("mandatory")
_Mtp3LinkCfgEntry_Object = MibTableRow
mtp3LinkCfgEntry = _Mtp3LinkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1)
)
mtp3LinkCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "mtp3LinkId"),
)
if mibBuilder.loadTexts:
    mtp3LinkCfgEntry.setStatus("mandatory")


class _Mtp3LinkId_Type(Integer32):
    """Custom type mtp3LinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Mtp3LinkId_Type.__name__ = "Integer32"
_Mtp3LinkId_Object = MibTableColumn
mtp3LinkId = _Mtp3LinkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 1),
    _Mtp3LinkId_Type()
)
mtp3LinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3LinkId.setStatus("mandatory")


class _Mtp3T1_Type(Integer32):
    """Custom type mtp3T1 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1200),
    )


_Mtp3T1_Type.__name__ = "Integer32"
_Mtp3T1_Object = MibTableColumn
mtp3T1 = _Mtp3T1_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 2),
    _Mtp3T1_Type()
)
mtp3T1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T1.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T1.setUnits("ms")


class _Mtp3T2_Type(Integer32):
    """Custom type mtp3T2 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(700, 2000),
    )


_Mtp3T2_Type.__name__ = "Integer32"
_Mtp3T2_Object = MibTableColumn
mtp3T2 = _Mtp3T2_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 3),
    _Mtp3T2_Type()
)
mtp3T2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T2.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T2.setUnits("ms")


class _Mtp3T3_Type(Integer32):
    """Custom type mtp3T3 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1200),
    )


_Mtp3T3_Type.__name__ = "Integer32"
_Mtp3T3_Object = MibTableColumn
mtp3T3 = _Mtp3T3_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 4),
    _Mtp3T3_Type()
)
mtp3T3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T3.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T3.setUnits("ms")


class _Mtp3T4_Type(Integer32):
    """Custom type mtp3T4 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1200),
    )


_Mtp3T4_Type.__name__ = "Integer32"
_Mtp3T4_Object = MibTableColumn
mtp3T4 = _Mtp3T4_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 5),
    _Mtp3T4_Type()
)
mtp3T4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T4.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T4.setUnits("ms")


class _Mtp3T5_Type(Integer32):
    """Custom type mtp3T5 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1200),
    )


_Mtp3T5_Type.__name__ = "Integer32"
_Mtp3T5_Object = MibTableColumn
mtp3T5 = _Mtp3T5_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 6),
    _Mtp3T5_Type()
)
mtp3T5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T5.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T5.setUnits("ms")


class _Mtp3T6_Type(Integer32):
    """Custom type mtp3T6 based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1200),
    )


_Mtp3T6_Type.__name__ = "Integer32"
_Mtp3T6_Object = MibTableColumn
mtp3T6 = _Mtp3T6_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 7),
    _Mtp3T6_Type()
)
mtp3T6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T6.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T6.setUnits("ms")


class _Mtp3T7_Type(Integer32):
    """Custom type mtp3T7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1200),
    )


_Mtp3T7_Type.__name__ = "Integer32"
_Mtp3T7_Object = MibTableColumn
mtp3T7 = _Mtp3T7_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 8),
    _Mtp3T7_Type()
)
mtp3T7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtp3T7.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T7.setUnits("ms")


class _Mtp3T12_Type(Integer32):
    """Custom type mtp3T12 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(800, 1500),
    )


_Mtp3T12_Type.__name__ = "Integer32"
_Mtp3T12_Object = MibTableColumn
mtp3T12 = _Mtp3T12_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 9),
    _Mtp3T12_Type()
)
mtp3T12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T12.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T12.setUnits("ms")


class _Mtp3T13_Type(Integer32):
    """Custom type mtp3T13 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(800, 1500),
    )


_Mtp3T13_Type.__name__ = "Integer32"
_Mtp3T13_Object = MibTableColumn
mtp3T13 = _Mtp3T13_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 10),
    _Mtp3T13_Type()
)
mtp3T13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T13.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T13.setUnits("ms")


class _Mtp3T14_Type(Integer32):
    """Custom type mtp3T14 based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 3000),
    )


_Mtp3T14_Type.__name__ = "Integer32"
_Mtp3T14_Object = MibTableColumn
mtp3T14 = _Mtp3T14_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 11),
    _Mtp3T14_Type()
)
mtp3T14.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T14.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T14.setUnits("ms")


class _Mtp3T17_Type(Integer32):
    """Custom type mtp3T17 based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(800, 1500),
    )


_Mtp3T17_Type.__name__ = "Integer32"
_Mtp3T17_Object = MibTableColumn
mtp3T17 = _Mtp3T17_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 12),
    _Mtp3T17_Type()
)
mtp3T17.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T17.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T17.setUnits("ms")


class _Mtp3T22_Type(Integer32):
    """Custom type mtp3T22 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 360),
    )


_Mtp3T22_Type.__name__ = "Integer32"
_Mtp3T22_Object = MibTableColumn
mtp3T22 = _Mtp3T22_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 13),
    _Mtp3T22_Type()
)
mtp3T22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T22.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T22.setUnits("sec")


class _Mtp3T23_Type(Integer32):
    """Custom type mtp3T23 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 360),
    )


_Mtp3T23_Type.__name__ = "Integer32"
_Mtp3T23_Object = MibTableColumn
mtp3T23 = _Mtp3T23_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 14),
    _Mtp3T23_Type()
)
mtp3T23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T23.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T23.setUnits("sec")


class _Mtp3T24_Type(Integer32):
    """Custom type mtp3T24 based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 5000),
    )


_Mtp3T24_Type.__name__ = "Integer32"
_Mtp3T24_Object = MibTableColumn
mtp3T24 = _Mtp3T24_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 15),
    _Mtp3T24_Type()
)
mtp3T24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtp3T24.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T24.setUnits("ms")


class _Mtp3T31_Type(Integer32):
    """Custom type mtp3T31 based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_Mtp3T31_Type.__name__ = "Integer32"
_Mtp3T31_Object = MibTableColumn
mtp3T31 = _Mtp3T31_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 16),
    _Mtp3T31_Type()
)
mtp3T31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T31.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T31.setUnits("sec")


class _Mtp3T32_Type(Integer32):
    """Custom type mtp3T32 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 12),
    )


_Mtp3T32_Type.__name__ = "Integer32"
_Mtp3T32_Object = MibTableColumn
mtp3T32 = _Mtp3T32_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 17),
    _Mtp3T32_Type()
)
mtp3T32.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T32.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T32.setUnits("sec")


class _Mtp3T33_Type(Integer32):
    """Custom type mtp3T33 based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_Mtp3T33_Type.__name__ = "Integer32"
_Mtp3T33_Object = MibTableColumn
mtp3T33 = _Mtp3T33_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 18),
    _Mtp3T33_Type()
)
mtp3T33.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T33.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T33.setUnits("sec")


class _Mtp3T34_Type(Integer32):
    """Custom type mtp3T34 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 90),
    )


_Mtp3T34_Type.__name__ = "Integer32"
_Mtp3T34_Object = MibTableColumn
mtp3T34 = _Mtp3T34_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 19),
    _Mtp3T34_Type()
)
mtp3T34.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T34.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T34.setUnits("sec")


class _Mtp3T35_Type(Integer32):
    """Custom type mtp3T35 based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_Mtp3T35_Type.__name__ = "Integer32"
_Mtp3T35_Object = MibTableColumn
mtp3T35 = _Mtp3T35_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 20),
    _Mtp3T35_Type()
)
mtp3T35.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T35.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T35.setUnits("sec")


class _Mtp3T36_Type(Integer32):
    """Custom type mtp3T36 based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_Mtp3T36_Type.__name__ = "Integer32"
_Mtp3T36_Object = MibTableColumn
mtp3T36 = _Mtp3T36_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 21),
    _Mtp3T36_Type()
)
mtp3T36.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T36.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T36.setUnits("sec")


class _Mtp3T37_Type(Integer32):
    """Custom type mtp3T37 based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_Mtp3T37_Type.__name__ = "Integer32"
_Mtp3T37_Object = MibTableColumn
mtp3T37 = _Mtp3T37_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 22),
    _Mtp3T37_Type()
)
mtp3T37.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3T37.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3T37.setUnits("sec")


class _Mtp3TFLC_Type(Integer32):
    """Custom type mtp3TFLC based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Mtp3TFLC_Type.__name__ = "Integer32"
_Mtp3TFLC_Object = MibTableColumn
mtp3TFLC = _Mtp3TFLC_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 23),
    _Mtp3TFLC_Type()
)
mtp3TFLC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3TFLC.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3TFLC.setUnits("ms")


class _Mtp3TBND_Type(Integer32):
    """Custom type mtp3TBND based on Integer32"""
    defaultValue = 20000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Mtp3TBND_Type.__name__ = "Integer32"
_Mtp3TBND_Object = MibTableColumn
mtp3TBND = _Mtp3TBND_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 24),
    _Mtp3TBND_Type()
)
mtp3TBND.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3TBND.setStatus("mandatory")
if mibBuilder.loadTexts:
    mtp3TBND.setUnits("ms")
_Mtp3RowStatus_Type = TmrRowStatus
_Mtp3RowStatus_Object = MibTableColumn
mtp3RowStatus = _Mtp3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 25),
    _Mtp3RowStatus_Type()
)
mtp3RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtp3RowStatus.setStatus("mandatory")
_Mtp3OpStatus_Type = OpStatus
_Mtp3OpStatus_Object = MibTableColumn
mtp3OpStatus = _Mtp3OpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 4, 2, 1, 26),
    _Mtp3OpStatus_Type()
)
mtp3OpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtp3OpStatus.setStatus("mandatory")
_Isup_ObjectIdentity = ObjectIdentity
isup = _Isup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5)
)
_IsupTimerCfgTable_Object = MibTable
isupTimerCfgTable = _IsupTimerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    isupTimerCfgTable.setStatus("mandatory")
_IsupTimerCfgEntry_Object = MibTableRow
isupTimerCfgEntry = _IsupTimerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1)
)
isupTimerCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "isupTimerType"),
)
if mibBuilder.loadTexts:
    isupTimerCfgEntry.setStatus("mandatory")


class _IsupTimerType_Type(TimerType):
    """Custom type isupTimerType based on TimerType"""
    subtypeSpec = TimerType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IsupTimerType_Type.__name__ = "TimerType"
_IsupTimerType_Object = MibTableColumn
isupTimerType = _IsupTimerType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 1),
    _IsupTimerType_Type()
)
isupTimerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTimerType.setStatus("mandatory")


class _IsupTmrT1_Type(Integer32):
    """Custom type isupTmrT1 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 60000),
    )


_IsupTmrT1_Type.__name__ = "Integer32"
_IsupTmrT1_Object = MibTableColumn
isupTmrT1 = _IsupTmrT1_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 2),
    _IsupTmrT1_Type()
)
isupTmrT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT1.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT1.setUnits("ms")


class _IsupTmrT2_Type(Integer32):
    """Custom type isupTmrT2 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_IsupTmrT2_Type.__name__ = "Integer32"
_IsupTmrT2_Object = MibTableColumn
isupTmrT2 = _IsupTmrT2_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 3),
    _IsupTmrT2_Type()
)
isupTmrT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT2.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT2.setUnits("sec")


class _IsupTmrT5_Type(Integer32):
    """Custom type isupTmrT5 based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_IsupTmrT5_Type.__name__ = "Integer32"
_IsupTmrT5_Object = MibTableColumn
isupTmrT5 = _IsupTmrT5_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 4),
    _IsupTmrT5_Type()
)
isupTmrT5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT5.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT5.setUnits("sec")


class _IsupTmrT6_Type(Integer32):
    """Custom type isupTmrT6 based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 32000),
    )


_IsupTmrT6_Type.__name__ = "Integer32"
_IsupTmrT6_Object = MibTableColumn
isupTmrT6 = _IsupTmrT6_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 5),
    _IsupTmrT6_Type()
)
isupTmrT6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT6.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT6.setUnits("ms")


class _IsupTmrT7_Type(Integer32):
    """Custom type isupTmrT7 based on Integer32"""
    defaultValue = 20000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20000, 30000),
    )


_IsupTmrT7_Type.__name__ = "Integer32"
_IsupTmrT7_Object = MibTableColumn
isupTmrT7 = _IsupTmrT7_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 6),
    _IsupTmrT7_Type()
)
isupTmrT7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT7.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT7.setUnits("ms")


class _IsupTmrT8_Type(Integer32):
    """Custom type isupTmrT8 based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 15000),
    )


_IsupTmrT8_Type.__name__ = "Integer32"
_IsupTmrT8_Object = MibTableColumn
isupTmrT8 = _IsupTmrT8_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 7),
    _IsupTmrT8_Type()
)
isupTmrT8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT8.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT8.setUnits("ms")


class _IsupTmrT9_Type(Integer32):
    """Custom type isupTmrT9 based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 240),
    )


_IsupTmrT9_Type.__name__ = "Integer32"
_IsupTmrT9_Object = MibTableColumn
isupTmrT9 = _IsupTmrT9_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 8),
    _IsupTmrT9_Type()
)
isupTmrT9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT9.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT9.setUnits("sec")


class _IsupTmrT18_Type(Integer32):
    """Custom type isupTmrT18 based on Integer32"""
    defaultValue = 15000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 60000),
    )


_IsupTmrT18_Type.__name__ = "Integer32"
_IsupTmrT18_Object = MibTableColumn
isupTmrT18 = _IsupTmrT18_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 9),
    _IsupTmrT18_Type()
)
isupTmrT18.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT18.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT18.setUnits("ms")


class _IsupTmrT19_Type(Integer32):
    """Custom type isupTmrT19 based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_IsupTmrT19_Type.__name__ = "Integer32"
_IsupTmrT19_Object = MibTableColumn
isupTmrT19 = _IsupTmrT19_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 10),
    _IsupTmrT19_Type()
)
isupTmrT19.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT19.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT19.setUnits("sec")


class _IsupTmrT20_Type(Integer32):
    """Custom type isupTmrT20 based on Integer32"""
    defaultValue = 15000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 60000),
    )


_IsupTmrT20_Type.__name__ = "Integer32"
_IsupTmrT20_Object = MibTableColumn
isupTmrT20 = _IsupTmrT20_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 11),
    _IsupTmrT20_Type()
)
isupTmrT20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT20.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT20.setUnits("ms")


class _IsupTmrT21_Type(Integer32):
    """Custom type isupTmrT21 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_IsupTmrT21_Type.__name__ = "Integer32"
_IsupTmrT21_Object = MibTableColumn
isupTmrT21 = _IsupTmrT21_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 12),
    _IsupTmrT21_Type()
)
isupTmrT21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT21.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT21.setUnits("sec")


class _IsupTmrT22_Type(Integer32):
    """Custom type isupTmrT22 based on Integer32"""
    defaultValue = 15000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 60000),
    )


_IsupTmrT22_Type.__name__ = "Integer32"
_IsupTmrT22_Object = MibTableColumn
isupTmrT22 = _IsupTmrT22_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 13),
    _IsupTmrT22_Type()
)
isupTmrT22.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT22.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT22.setUnits("ms")


class _IsupTmrT23_Type(Integer32):
    """Custom type isupTmrT23 based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 900),
    )


_IsupTmrT23_Type.__name__ = "Integer32"
_IsupTmrT23_Object = MibTableColumn
isupTmrT23 = _IsupTmrT23_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 14),
    _IsupTmrT23_Type()
)
isupTmrT23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT23.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT23.setUnits("sec")


class _IsupTmrT27_Type(Integer32):
    """Custom type isupTmrT27 based on Integer32"""
    defaultValue = 18

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18, 24),
    )


_IsupTmrT27_Type.__name__ = "Integer32"
_IsupTmrT27_Object = MibTableColumn
isupTmrT27 = _IsupTmrT27_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 15),
    _IsupTmrT27_Type()
)
isupTmrT27.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT27.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT27.setUnits("sec")


class _IsupTmrT28_Type(Integer32):
    """Custom type isupTmrT28 based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 10000),
    )


_IsupTmrT28_Type.__name__ = "Integer32"
_IsupTmrT28_Object = MibTableColumn
isupTmrT28 = _IsupTmrT28_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 16),
    _IsupTmrT28_Type()
)
isupTmrT28.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT28.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT28.setUnits("ms")


class _IsupTmrT31_Type(Integer32):
    """Custom type isupTmrT31 based on Integer32"""
    defaultValue = 360

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(360, 360),
    )


_IsupTmrT31_Type.__name__ = "Integer32"
_IsupTmrT31_Object = MibTableColumn
isupTmrT31 = _IsupTmrT31_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 17),
    _IsupTmrT31_Type()
)
isupTmrT31.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT31.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT31.setUnits("sec")


class _IsupTmrT33_Type(Integer32):
    """Custom type isupTmrT33 based on Integer32"""
    defaultValue = 12000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12000, 15000),
    )


_IsupTmrT33_Type.__name__ = "Integer32"
_IsupTmrT33_Object = MibTableColumn
isupTmrT33 = _IsupTmrT33_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 18),
    _IsupTmrT33_Type()
)
isupTmrT33.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT33.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT33.setUnits("ms")


class _IsupTmrT34_Type(Integer32):
    """Custom type isupTmrT34 based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 15000),
    )


_IsupTmrT34_Type.__name__ = "Integer32"
_IsupTmrT34_Object = MibTableColumn
isupTmrT34 = _IsupTmrT34_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 19),
    _IsupTmrT34_Type()
)
isupTmrT34.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT34.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT34.setUnits("ms")


class _IsupTmrT36_Type(Integer32):
    """Custom type isupTmrT36 based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 4000),
    )


_IsupTmrT36_Type.__name__ = "Integer32"
_IsupTmrT36_Object = MibTableColumn
isupTmrT36 = _IsupTmrT36_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 20),
    _IsupTmrT36_Type()
)
isupTmrT36.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrT36.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrT36.setUnits("ms")


class _IsupTmrTCCR_Type(Integer32):
    """Custom type isupTmrTCCR based on Integer32"""
    defaultValue = 20000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20000, 24000),
    )


_IsupTmrTCCR_Type.__name__ = "Integer32"
_IsupTmrTCCR_Object = MibTableColumn
isupTmrTCCR = _IsupTmrTCCR_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 21),
    _IsupTmrTCCR_Type()
)
isupTmrTCCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrTCCR.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrTCCR.setUnits("ms")


class _IsupTmrTEX_Type(Integer32):
    """Custom type isupTmrTEX based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsupTmrTEX_Type.__name__ = "Integer32"
_IsupTmrTEX_Object = MibTableColumn
isupTmrTEX = _IsupTmrTEX_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 22),
    _IsupTmrTEX_Type()
)
isupTmrTEX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isupTmrTEX.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrTEX.setUnits("ms")


class _IsupTmrTCRM_Type(Integer32):
    """Custom type isupTmrTCRM based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 4000),
    )


_IsupTmrTCRM_Type.__name__ = "Integer32"
_IsupTmrTCRM_Object = MibTableColumn
isupTmrTCRM = _IsupTmrTCRM_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 23),
    _IsupTmrTCRM_Type()
)
isupTmrTCRM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrTCRM.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrTCRM.setUnits("ms")


class _IsupTmrTCRA_Type(Integer32):
    """Custom type isupTmrTCRA based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_IsupTmrTCRA_Type.__name__ = "Integer32"
_IsupTmrTCRA_Object = MibTableColumn
isupTmrTCRA = _IsupTmrTCRA_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 24),
    _IsupTmrTCRA_Type()
)
isupTmrTCRA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrTCRA.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrTCRA.setUnits("ms")


class _IsupTmrTCCRt_Type(Integer32):
    """Custom type isupTmrTCCRt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_IsupTmrTCCRt_Type.__name__ = "Integer32"
_IsupTmrTCCRt_Object = MibTableColumn
isupTmrTCCRt = _IsupTmrTCCRt_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 25),
    _IsupTmrTCCRt_Type()
)
isupTmrTCCRt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrTCCRt.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrTCCRt.setUnits("ms")


class _IsupTmrTECt_Type(Integer32):
    """Custom type isupTmrTECt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsupTmrTECt_Type.__name__ = "Integer32"
_IsupTmrTECt_Object = MibTableColumn
isupTmrTECt = _IsupTmrTECt_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 26),
    _IsupTmrTECt_Type()
)
isupTmrTECt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isupTmrTECt.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrTECt.setUnits("ms")


class _IsupTmrTGTCHG_Type(Integer32):
    """Custom type isupTmrTGTCHG based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsupTmrTGTCHG_Type.__name__ = "Integer32"
_IsupTmrTGTCHG_Object = MibTableColumn
isupTmrTGTCHG = _IsupTmrTGTCHG_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 27),
    _IsupTmrTGTCHG_Type()
)
isupTmrTGTCHG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isupTmrTGTCHG.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrTGTCHG.setUnits("ms")


class _IsupTmrTGRES_Type(Integer32):
    """Custom type isupTmrTGRES based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 5000),
    )


_IsupTmrTGRES_Type.__name__ = "Integer32"
_IsupTmrTGRES_Object = MibTableColumn
isupTmrTGRES = _IsupTmrTGRES_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 28),
    _IsupTmrTGRES_Type()
)
isupTmrTGRES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTmrTGRES.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrTGRES.setUnits("ms")


class _IsupTmrTFGR_Type(Integer32):
    """Custom type isupTmrTFGR based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 120000),
    )


_IsupTmrTFGR_Type.__name__ = "Integer32"
_IsupTmrTFGR_Object = MibTableColumn
isupTmrTFGR = _IsupTmrTFGR_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 29),
    _IsupTmrTFGR_Type()
)
isupTmrTFGR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isupTmrTFGR.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrTFGR.setUnits("ms")


class _IsupTmrTRELRSP_Type(Integer32):
    """Custom type isupTmrTRELRSP based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsupTmrTRELRSP_Type.__name__ = "Integer32"
_IsupTmrTRELRSP_Object = MibTableColumn
isupTmrTRELRSP = _IsupTmrTRELRSP_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 30),
    _IsupTmrTRELRSP_Type()
)
isupTmrTRELRSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isupTmrTRELRSP.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrTRELRSP.setUnits("ms")


class _IsupTmrTFNLRELRS_Type(Integer32):
    """Custom type isupTmrTFNLRELRS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsupTmrTFNLRELRS_Type.__name__ = "Integer32"
_IsupTmrTFNLRELRS_Object = MibTableColumn
isupTmrTFNLRELRS = _IsupTmrTFNLRELRS_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 31),
    _IsupTmrTFNLRELRS_Type()
)
isupTmrTFNLRELRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isupTmrTFNLRELRS.setStatus("mandatory")
if mibBuilder.loadTexts:
    isupTmrTFNLRELRS.setUnits("ms")
_IsupTimerRowStatus_Type = ModifyTmrStatus
_IsupTimerRowStatus_Object = MibTableColumn
isupTimerRowStatus = _IsupTimerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 5, 1, 1, 32),
    _IsupTimerRowStatus_Type()
)
isupTimerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isupTimerRowStatus.setStatus("mandatory")
_Ss7Route_ObjectIdentity = ObjectIdentity
ss7Route = _Ss7Route_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 6)
)
_Ss7RtDpcTable_Object = MibTable
ss7RtDpcTable = _Ss7RtDpcTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ss7RtDpcTable.setStatus("mandatory")
_Ss7RtDpcEntry_Object = MibTableRow
ss7RtDpcEntry = _Ss7RtDpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 6, 1, 1)
)
ss7RtDpcEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "ss7RtDPC"),
)
if mibBuilder.loadTexts:
    ss7RtDpcEntry.setStatus("mandatory")


class _Ss7RtDPC_Type(Integer32):
    """Custom type ss7RtDPC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_Ss7RtDPC_Type.__name__ = "Integer32"
_Ss7RtDPC_Object = MibTableColumn
ss7RtDPC = _Ss7RtDPC_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 6, 1, 1, 1),
    _Ss7RtDPC_Type()
)
ss7RtDPC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7RtDPC.setStatus("mandatory")


class _Ss7RtCmbLinksetId_Type(Integer32):
    """Custom type ss7RtCmbLinksetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Ss7RtCmbLinksetId_Type.__name__ = "Integer32"
_Ss7RtCmbLinksetId_Object = MibTableColumn
ss7RtCmbLinksetId = _Ss7RtCmbLinksetId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 6, 1, 1, 2),
    _Ss7RtCmbLinksetId_Type()
)
ss7RtCmbLinksetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7RtCmbLinksetId.setStatus("mandatory")
_Ss7RtLoadShareType_Type = Standard
_Ss7RtLoadShareType_Object = MibTableColumn
ss7RtLoadShareType = _Ss7RtLoadShareType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 6, 1, 1, 3),
    _Ss7RtLoadShareType_Type()
)
ss7RtLoadShareType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7RtLoadShareType.setStatus("mandatory")
_Ss7RtRowStatus_Type = RowStatus
_Ss7RtRowStatus_Object = MibTableColumn
ss7RtRowStatus = _Ss7RtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 6, 1, 1, 4),
    _Ss7RtRowStatus_Type()
)
ss7RtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7RtRowStatus.setStatus("mandatory")
_Ss7RtOpStatus_Type = OpStatus
_Ss7RtOpStatus_Object = MibTableColumn
ss7RtOpStatus = _Ss7RtOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 1, 6, 1, 1, 5),
    _Ss7RtOpStatus_Type()
)
ss7RtOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7RtOpStatus.setStatus("mandatory")
_Isdn_ObjectIdentity = ObjectIdentity
isdn = _Isdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2)
)
_IsdnTmrCfgTable_Object = MibTable
isdnTmrCfgTable = _IsdnTmrCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    isdnTmrCfgTable.setStatus("mandatory")
_IsdnTmrCfgEntry_Object = MibTableRow
isdnTmrCfgEntry = _IsdnTmrCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1)
)
isdnTmrCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "isdnTnkId"),
)
if mibBuilder.loadTexts:
    isdnTmrCfgEntry.setStatus("mandatory")


class _IsdnTnkId_Type(Integer32):
    """Custom type isdnTnkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnTnkId_Type.__name__ = "Integer32"
_IsdnTnkId_Object = MibTableColumn
isdnTnkId = _IsdnTnkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 1),
    _IsdnTnkId_Type()
)
isdnTnkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTnkId.setStatus("mandatory")


class _IsdnTmrT301_Type(Integer32):
    """Custom type isdnTmrT301 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 420),
    )


_IsdnTmrT301_Type.__name__ = "Integer32"
_IsdnTmrT301_Object = MibTableColumn
isdnTmrT301 = _IsdnTmrT301_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 2),
    _IsdnTmrT301_Type()
)
isdnTmrT301.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT301.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT301.setUnits("sec")


class _IsdnTmrT302_Type(Integer32):
    """Custom type isdnTmrT302 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_IsdnTmrT302_Type.__name__ = "Integer32"
_IsdnTmrT302_Object = MibTableColumn
isdnTmrT302 = _IsdnTmrT302_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 3),
    _IsdnTmrT302_Type()
)
isdnTmrT302.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT302.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT302.setUnits("ms")


class _IsdnTmrT303_Type(Integer32):
    """Custom type isdnTmrT303 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 4000),
    )


_IsdnTmrT303_Type.__name__ = "Integer32"
_IsdnTmrT303_Object = MibTableColumn
isdnTmrT303 = _IsdnTmrT303_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 4),
    _IsdnTmrT303_Type()
)
isdnTmrT303.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT303.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT303.setUnits("ms")


class _IsdnTmrT304_Type(Integer32):
    """Custom type isdnTmrT304 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_IsdnTmrT304_Type.__name__ = "Integer32"
_IsdnTmrT304_Object = MibTableColumn
isdnTmrT304 = _IsdnTmrT304_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 5),
    _IsdnTmrT304_Type()
)
isdnTmrT304.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT304.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT304.setUnits("ms")


class _IsdnTmrT305_Type(Integer32):
    """Custom type isdnTmrT305 based on Integer32"""
    defaultValue = 30000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 60000),
    )


_IsdnTmrT305_Type.__name__ = "Integer32"
_IsdnTmrT305_Object = MibTableColumn
isdnTmrT305 = _IsdnTmrT305_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 6),
    _IsdnTmrT305_Type()
)
isdnTmrT305.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT305.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT305.setUnits("ms")


class _IsdnTmrT306_Type(Integer32):
    """Custom type isdnTmrT306 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 150),
    )


_IsdnTmrT306_Type.__name__ = "Integer32"
_IsdnTmrT306_Object = MibTableColumn
isdnTmrT306 = _IsdnTmrT306_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 7),
    _IsdnTmrT306_Type()
)
isdnTmrT306.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT306.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT306.setUnits("sec")


class _IsdnTmrT307_Type(Integer32):
    """Custom type isdnTmrT307 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_IsdnTmrT307_Type.__name__ = "Integer32"
_IsdnTmrT307_Object = MibTableColumn
isdnTmrT307 = _IsdnTmrT307_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 8),
    _IsdnTmrT307_Type()
)
isdnTmrT307.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT307.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT307.setUnits("sec")


class _IsdnTmrT308_Type(Integer32):
    """Custom type isdnTmrT308 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 10000),
    )


_IsdnTmrT308_Type.__name__ = "Integer32"
_IsdnTmrT308_Object = MibTableColumn
isdnTmrT308 = _IsdnTmrT308_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 9),
    _IsdnTmrT308_Type()
)
isdnTmrT308.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT308.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT308.setUnits("ms")


class _IsdnTmrT310_Type(Integer32):
    """Custom type isdnTmrT310 based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 10000),
    )


_IsdnTmrT310_Type.__name__ = "Integer32"
_IsdnTmrT310_Object = MibTableColumn
isdnTmrT310 = _IsdnTmrT310_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 10),
    _IsdnTmrT310_Type()
)
isdnTmrT310.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT310.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT310.setUnits("ms")


class _IsdnTmrT311_Type(Integer32):
    """Custom type isdnTmrT311 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsdnTmrT311_Type.__name__ = "Integer32"
_IsdnTmrT311_Object = MibTableColumn
isdnTmrT311 = _IsdnTmrT311_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 11),
    _IsdnTmrT311_Type()
)
isdnTmrT311.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnTmrT311.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT311.setUnits("ms")


class _IsdnTmrT312_Type(Integer32):
    """Custom type isdnTmrT312 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_IsdnTmrT312_Type.__name__ = "Integer32"
_IsdnTmrT312_Object = MibTableColumn
isdnTmrT312 = _IsdnTmrT312_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 12),
    _IsdnTmrT312_Type()
)
isdnTmrT312.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT312.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT312.setUnits("ms")


class _IsdnTmrT313_Type(Integer32):
    """Custom type isdnTmrT313 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsdnTmrT313_Type.__name__ = "Integer32"
_IsdnTmrT313_Object = MibTableColumn
isdnTmrT313 = _IsdnTmrT313_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 13),
    _IsdnTmrT313_Type()
)
isdnTmrT313.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT313.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT313.setUnits("ms")


class _IsdnTmrT316_Type(Integer32):
    """Custom type isdnTmrT316 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_IsdnTmrT316_Type.__name__ = "Integer32"
_IsdnTmrT316_Object = MibTableColumn
isdnTmrT316 = _IsdnTmrT316_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 14),
    _IsdnTmrT316_Type()
)
isdnTmrT316.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT316.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT316.setUnits("sec")


class _IsdnTmrT318_Type(Integer32):
    """Custom type isdnTmrT318 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsdnTmrT318_Type.__name__ = "Integer32"
_IsdnTmrT318_Object = MibTableColumn
isdnTmrT318 = _IsdnTmrT318_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 15),
    _IsdnTmrT318_Type()
)
isdnTmrT318.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT318.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT318.setUnits("ms")


class _IsdnTmrT319_Type(Integer32):
    """Custom type isdnTmrT319 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsdnTmrT319_Type.__name__ = "Integer32"
_IsdnTmrT319_Object = MibTableColumn
isdnTmrT319 = _IsdnTmrT319_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 16),
    _IsdnTmrT319_Type()
)
isdnTmrT319.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT319.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT319.setUnits("ms")


class _IsdnTmrT322_Type(Integer32):
    """Custom type isdnTmrT322 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 10000),
    )


_IsdnTmrT322_Type.__name__ = "Integer32"
_IsdnTmrT322_Object = MibTableColumn
isdnTmrT322 = _IsdnTmrT322_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 17),
    _IsdnTmrT322_Type()
)
isdnTmrT322.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT322.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT322.setUnits("ms")


class _IsdnTmrT316C_Type(Integer32):
    """Custom type isdnTmrT316C based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 120),
    )


_IsdnTmrT316C_Type.__name__ = "Integer32"
_IsdnTmrT316C_Object = MibTableColumn
isdnTmrT316C = _IsdnTmrT316C_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 18),
    _IsdnTmrT316C_Type()
)
isdnTmrT316C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnTmrT316C.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT316C.setUnits("sec")


class _IsdnTmrT330_Type(Integer32):
    """Custom type isdnTmrT330 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsdnTmrT330_Type.__name__ = "Integer32"
_IsdnTmrT330_Object = MibTableColumn
isdnTmrT330 = _IsdnTmrT330_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 19),
    _IsdnTmrT330_Type()
)
isdnTmrT330.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT330.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT330.setUnits("ms")


class _IsdnTmrT331_Type(Integer32):
    """Custom type isdnTmrT331 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsdnTmrT331_Type.__name__ = "Integer32"
_IsdnTmrT331_Object = MibTableColumn
isdnTmrT331 = _IsdnTmrT331_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 20),
    _IsdnTmrT331_Type()
)
isdnTmrT331.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT331.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT331.setUnits("ms")


class _IsdnTmrT332_Type(Integer32):
    """Custom type isdnTmrT332 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsdnTmrT332_Type.__name__ = "Integer32"
_IsdnTmrT332_Object = MibTableColumn
isdnTmrT332 = _IsdnTmrT332_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 21),
    _IsdnTmrT332_Type()
)
isdnTmrT332.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT332.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT332.setUnits("ms")


class _IsdnTmrTRST_Type(Integer32):
    """Custom type isdnTmrTRST based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )


_IsdnTmrTRST_Type.__name__ = "Integer32"
_IsdnTmrTRST_Object = MibTableColumn
isdnTmrTRST = _IsdnTmrTRST_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 22),
    _IsdnTmrTRST_Type()
)
isdnTmrTRST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnTmrTRST.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrTRST.setUnits("sec")


class _IsdnTmrTREST_Type(Integer32):
    """Custom type isdnTmrTREST based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 600),
    )


_IsdnTmrTREST_Type.__name__ = "Integer32"
_IsdnTmrTREST_Object = MibTableColumn
isdnTmrTREST = _IsdnTmrTREST_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 23),
    _IsdnTmrTREST_Type()
)
isdnTmrTREST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrTREST.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrTREST.setUnits("sec")


class _IsdnTmrTANS_Type(Integer32):
    """Custom type isdnTmrTANS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65553),
    )


_IsdnTmrTANS_Type.__name__ = "Integer32"
_IsdnTmrTANS_Object = MibTableColumn
isdnTmrTANS = _IsdnTmrTANS_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 24),
    _IsdnTmrTANS_Type()
)
isdnTmrTANS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnTmrTANS.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrTANS.setUnits("ms")


class _IsdnTmrT396_Type(Integer32):
    """Custom type isdnTmrT396 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsdnTmrT396_Type.__name__ = "Integer32"
_IsdnTmrT396_Object = MibTableColumn
isdnTmrT396 = _IsdnTmrT396_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 25),
    _IsdnTmrT396_Type()
)
isdnTmrT396.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT396.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT396.setUnits("ms")


class _IsdnTmrT397_Type(Integer32):
    """Custom type isdnTmrT397 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IsdnTmrT397_Type.__name__ = "Integer32"
_IsdnTmrT397_Object = MibTableColumn
isdnTmrT397 = _IsdnTmrT397_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 26),
    _IsdnTmrT397_Type()
)
isdnTmrT397.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTmrT397.setStatus("mandatory")
if mibBuilder.loadTexts:
    isdnTmrT397.setUnits("ms")
_IsdnTrnkTmrRowStatus_Type = TmrRowStatus
_IsdnTrnkTmrRowStatus_Object = MibTableColumn
isdnTrnkTmrRowStatus = _IsdnTrnkTmrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 27),
    _IsdnTrnkTmrRowStatus_Type()
)
isdnTrnkTmrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTrnkTmrRowStatus.setStatus("mandatory")
_IsdnTrnkTmrOpStatus_Type = OpStatus
_IsdnTrnkTmrOpStatus_Object = MibTableColumn
isdnTrnkTmrOpStatus = _IsdnTrnkTmrOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 1, 1, 28),
    _IsdnTrnkTmrOpStatus_Type()
)
isdnTrnkTmrOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnTrnkTmrOpStatus.setStatus("mandatory")
_IsdnTrunkCfgTable_Object = MibTable
isdnTrunkCfgTable = _IsdnTrunkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    isdnTrunkCfgTable.setStatus("mandatory")
_IsdnTrunkCfgEntry_Object = MibTableRow
isdnTrunkCfgEntry = _IsdnTrunkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1)
)
isdnTrunkCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "isdnTrunkId"),
)
if mibBuilder.loadTexts:
    isdnTrunkCfgEntry.setStatus("mandatory")


class _IsdnTrunkId_Type(Integer32):
    """Custom type isdnTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnTrunkId_Type.__name__ = "Integer32"
_IsdnTrunkId_Object = MibTableColumn
isdnTrunkId = _IsdnTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 1),
    _IsdnTrunkId_Type()
)
isdnTrunkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTrunkId.setStatus("mandatory")
_IsdnTrunkName_Type = NameString
_IsdnTrunkName_Object = MibTableColumn
isdnTrunkName = _IsdnTrunkName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 2),
    _IsdnTrunkName_Type()
)
isdnTrunkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTrunkName.setStatus("mandatory")


class _IsdnTrunkGrpId_Type(Integer32):
    """Custom type isdnTrunkGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnTrunkGrpId_Type.__name__ = "Integer32"
_IsdnTrunkGrpId_Object = MibTableColumn
isdnTrunkGrpId = _IsdnTrunkGrpId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 3),
    _IsdnTrunkGrpId_Type()
)
isdnTrunkGrpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTrunkGrpId.setStatus("mandatory")


class _IsdnDchnlId_Type(Integer32):
    """Custom type isdnDchnlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnDchnlId_Type.__name__ = "Integer32"
_IsdnDchnlId_Object = MibTableColumn
isdnDchnlId = _IsdnDchnlId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 4),
    _IsdnDchnlId_Type()
)
isdnDchnlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDchnlId.setStatus("mandatory")
_IsdnTrunkType_Type = IsdnType
_IsdnTrunkType_Object = MibTableColumn
isdnTrunkType = _IsdnTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 5),
    _IsdnTrunkType_Type()
)
isdnTrunkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTrunkType.setStatus("mandatory")


class _IsdnXconnectId_Type(Integer32):
    """Custom type isdnXconnectId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnXconnectId_Type.__name__ = "Integer32"
_IsdnXconnectId_Object = MibTableColumn
isdnXconnectId = _IsdnXconnectId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 6),
    _IsdnXconnectId_Type()
)
isdnXconnectId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnXconnectId.setStatus("mandatory")


class _IsdnSlotId_Type(Integer32):
    """Custom type isdnSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnSlotId_Type.__name__ = "Integer32"
_IsdnSlotId_Object = MibTableColumn
isdnSlotId = _IsdnSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 7),
    _IsdnSlotId_Type()
)
isdnSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnSlotId.setStatus("mandatory")


class _IsdnPortId_Type(Integer32):
    """Custom type isdnPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnPortId_Type.__name__ = "Integer32"
_IsdnPortId_Object = MibTableColumn
isdnPortId = _IsdnPortId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 8),
    _IsdnPortId_Type()
)
isdnPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnPortId.setStatus("mandatory")
_IsdnDirection_Type = Direction
_IsdnDirection_Object = MibTableColumn
isdnDirection = _IsdnDirection_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 9),
    _IsdnDirection_Type()
)
isdnDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDirection.setStatus("mandatory")
_IsdnPriority_Type = IsdnPriority
_IsdnPriority_Object = MibTableColumn
isdnPriority = _IsdnPriority_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 10),
    _IsdnPriority_Type()
)
isdnPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnPriority.setStatus("mandatory")


class _IsdnDurthreshold_Type(Integer32):
    """Custom type isdnDurthreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnDurthreshold_Type.__name__ = "Integer32"
_IsdnDurthreshold_Object = MibTableColumn
isdnDurthreshold = _IsdnDurthreshold_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 11),
    _IsdnDurthreshold_Type()
)
isdnDurthreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDurthreshold.setStatus("mandatory")


class _IsdnCntthreshold_Type(Integer32):
    """Custom type isdnCntthreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnCntthreshold_Type.__name__ = "Integer32"
_IsdnCntthreshold_Object = MibTableColumn
isdnCntthreshold = _IsdnCntthreshold_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 12),
    _IsdnCntthreshold_Type()
)
isdnCntthreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCntthreshold.setStatus("mandatory")
_IsdnPhyIntfType_Type = IfType
_IsdnPhyIntfType_Object = MibTableColumn
isdnPhyIntfType = _IsdnPhyIntfType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 13),
    _IsdnPhyIntfType_Type()
)
isdnPhyIntfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnPhyIntfType.setStatus("mandatory")


class _IsdnDchnlTimeSlot_Type(Integer32):
    """Custom type isdnDchnlTimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnDchnlTimeSlot_Type.__name__ = "Integer32"
_IsdnDchnlTimeSlot_Object = MibTableColumn
isdnDchnlTimeSlot = _IsdnDchnlTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 14),
    _IsdnDchnlTimeSlot_Type()
)
isdnDchnlTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDchnlTimeSlot.setStatus("mandatory")
_IsdnE1MultiFrame_Type = E1MultiFrame
_IsdnE1MultiFrame_Object = MibTableColumn
isdnE1MultiFrame = _IsdnE1MultiFrame_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 15),
    _IsdnE1MultiFrame_Type()
)
isdnE1MultiFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnE1MultiFrame.setStatus("mandatory")
_IsdnE1CRC4_Type = E1CRC4
_IsdnE1CRC4_Object = MibTableColumn
isdnE1CRC4 = _IsdnE1CRC4_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 16),
    _IsdnE1CRC4_Type()
)
isdnE1CRC4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnE1CRC4.setStatus("mandatory")
_IsdnE1TransClk_Type = TransClkSrc
_IsdnE1TransClk_Object = MibTableColumn
isdnE1TransClk = _IsdnE1TransClk_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 17),
    _IsdnE1TransClk_Type()
)
isdnE1TransClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnE1TransClk.setStatus("mandatory")
_IsdnDS1LineType_Type = DS1LineType
_IsdnDS1LineType_Object = MibTableColumn
isdnDS1LineType = _IsdnDS1LineType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 18),
    _IsdnDS1LineType_Type()
)
isdnDS1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDS1LineType.setStatus("mandatory")
_IsdnDS1LineCoding_Type = DS1LineCoding
_IsdnDS1LineCoding_Object = MibTableColumn
isdnDS1LineCoding = _IsdnDS1LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 19),
    _IsdnDS1LineCoding_Type()
)
isdnDS1LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDS1LineCoding.setStatus("mandatory")
_IsdnDS1TransClkSrc_Type = TransClkSrc
_IsdnDS1TransClkSrc_Object = MibTableColumn
isdnDS1TransClkSrc = _IsdnDS1TransClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 20),
    _IsdnDS1TransClkSrc_Type()
)
isdnDS1TransClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDS1TransClkSrc.setStatus("mandatory")
_IsdnDS1LBO_Type = DS1LBO
_IsdnDS1LBO_Object = MibTableColumn
isdnDS1LBO = _IsdnDS1LBO_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 21),
    _IsdnDS1LBO_Type()
)
isdnDS1LBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDS1LBO.setStatus("mandatory")
_IsdnDS3LineType_Type = DS3LineType
_IsdnDS3LineType_Object = MibTableColumn
isdnDS3LineType = _IsdnDS3LineType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 22),
    _IsdnDS3LineType_Type()
)
isdnDS3LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDS3LineType.setStatus("mandatory")
_IsdnDS3TransClkSrc_Type = TransClkSrc
_IsdnDS3TransClkSrc_Object = MibTableColumn
isdnDS3TransClkSrc = _IsdnDS3TransClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 23),
    _IsdnDS3TransClkSrc_Type()
)
isdnDS3TransClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDS3TransClkSrc.setStatus("mandatory")
_IsdnDS3LBO_Type = DS3LBO
_IsdnDS3LBO_Object = MibTableColumn
isdnDS3LBO = _IsdnDS3LBO_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 24),
    _IsdnDS3LBO_Type()
)
isdnDS3LBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDS3LBO.setStatus("mandatory")
_IsdnDS3DS1LineType_Type = DS1LineType
_IsdnDS3DS1LineType_Object = MibTableColumn
isdnDS3DS1LineType = _IsdnDS3DS1LineType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 25),
    _IsdnDS3DS1LineType_Type()
)
isdnDS3DS1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDS3DS1LineType.setStatus("mandatory")
_IsdnDS3DS1TransClkSrc_Type = TransClkSrc
_IsdnDS3DS1TransClkSrc_Object = MibTableColumn
isdnDS3DS1TransClkSrc = _IsdnDS3DS1TransClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 26),
    _IsdnDS3DS1TransClkSrc_Type()
)
isdnDS3DS1TransClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDS3DS1TransClkSrc.setStatus("mandatory")
_IsdnTrunkRowStatus_Type = RowStatus
_IsdnTrunkRowStatus_Object = MibTableColumn
isdnTrunkRowStatus = _IsdnTrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 27),
    _IsdnTrunkRowStatus_Type()
)
isdnTrunkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTrunkRowStatus.setStatus("mandatory")
_IsdnTrunkOpStatus_Type = IsdnTrnkOpStatus
_IsdnTrunkOpStatus_Object = MibTableColumn
isdnTrunkOpStatus = _IsdnTrunkOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 2, 1, 28),
    _IsdnTrunkOpStatus_Type()
)
isdnTrunkOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnTrunkOpStatus.setStatus("mandatory")
_IsdnChnlStatusTable_Object = MibTable
isdnChnlStatusTable = _IsdnChnlStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    isdnChnlStatusTable.setStatus("mandatory")
_IsdnChnlStatusCfgEntry_Object = MibTableRow
isdnChnlStatusCfgEntry = _IsdnChnlStatusCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 3, 1)
)
isdnChnlStatusCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "isdnStatusTrunkId"),
    (0, "ARMILLAIRE2000-MIB", "isdnStatusChnlId"),
)
if mibBuilder.loadTexts:
    isdnChnlStatusCfgEntry.setStatus("mandatory")


class _IsdnStatusTrunkId_Type(Integer32):
    """Custom type isdnStatusTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnStatusTrunkId_Type.__name__ = "Integer32"
_IsdnStatusTrunkId_Object = MibTableColumn
isdnStatusTrunkId = _IsdnStatusTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 3, 1, 1),
    _IsdnStatusTrunkId_Type()
)
isdnStatusTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnStatusTrunkId.setStatus("mandatory")


class _IsdnStatusChnlId_Type(Integer32):
    """Custom type isdnStatusChnlId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnStatusChnlId_Type.__name__ = "Integer32"
_IsdnStatusChnlId_Object = MibTableColumn
isdnStatusChnlId = _IsdnStatusChnlId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 3, 1, 2),
    _IsdnStatusChnlId_Type()
)
isdnStatusChnlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnStatusChnlId.setStatus("mandatory")
_IsdnStatusChnlState_Type = TrunkState
_IsdnStatusChnlState_Object = MibTableColumn
isdnStatusChnlState = _IsdnStatusChnlState_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 3, 1, 3),
    _IsdnStatusChnlState_Type()
)
isdnStatusChnlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnStatusChnlState.setStatus("mandatory")


class _IsdnStatusChnlAllocMeth_Type(Integer32):
    """Custom type isdnStatusChnlAllocMeth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnStatusChnlAllocMeth_Type.__name__ = "Integer32"
_IsdnStatusChnlAllocMeth_Object = MibTableColumn
isdnStatusChnlAllocMeth = _IsdnStatusChnlAllocMeth_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 3, 1, 4),
    _IsdnStatusChnlAllocMeth_Type()
)
isdnStatusChnlAllocMeth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnStatusChnlAllocMeth.setStatus("mandatory")


class _IsdnStatusChnlSuConnId_Type(Integer32):
    """Custom type isdnStatusChnlSuConnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnStatusChnlSuConnId_Type.__name__ = "Integer32"
_IsdnStatusChnlSuConnId_Object = MibTableColumn
isdnStatusChnlSuConnId = _IsdnStatusChnlSuConnId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 3, 1, 5),
    _IsdnStatusChnlSuConnId_Type()
)
isdnStatusChnlSuConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnStatusChnlSuConnId.setStatus("mandatory")
_IsdnMgmntGroup_ObjectIdentity = ObjectIdentity
isdnMgmntGroup = _IsdnMgmntGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 4)
)
_IsdnTrnkMgmntTable_Object = MibTable
isdnTrnkMgmntTable = _IsdnTrnkMgmntTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    isdnTrnkMgmntTable.setStatus("mandatory")
_IsdnTrnkMgmntEntry_Object = MibTableRow
isdnTrnkMgmntEntry = _IsdnTrnkMgmntEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 4, 1, 1)
)
isdnTrnkMgmntEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "isdnTrnkMgmntId"),
)
if mibBuilder.loadTexts:
    isdnTrnkMgmntEntry.setStatus("mandatory")
_IsdnTrnkMgmntId_Type = Integer32
_IsdnTrnkMgmntId_Object = MibTableColumn
isdnTrnkMgmntId = _IsdnTrnkMgmntId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 4, 1, 1, 1),
    _IsdnTrnkMgmntId_Type()
)
isdnTrnkMgmntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnTrnkMgmntId.setStatus("mandatory")
_IsdnTrnkMgmntCmd_Type = IsdnTrnkMgtOperation
_IsdnTrnkMgmntCmd_Object = MibTableColumn
isdnTrnkMgmntCmd = _IsdnTrnkMgmntCmd_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 4, 1, 1, 2),
    _IsdnTrnkMgmntCmd_Type()
)
isdnTrnkMgmntCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTrnkMgmntCmd.setStatus("mandatory")
_IsdnChnlMgmntTable_Object = MibTable
isdnChnlMgmntTable = _IsdnChnlMgmntTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    isdnChnlMgmntTable.setStatus("mandatory")
_IsdnChnlMgmntEntry_Object = MibTableRow
isdnChnlMgmntEntry = _IsdnChnlMgmntEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 4, 2, 1)
)
isdnChnlMgmntEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "isdnTrunkMgmntId"),
    (0, "ARMILLAIRE2000-MIB", "isdnChnlMgmntId"),
)
if mibBuilder.loadTexts:
    isdnChnlMgmntEntry.setStatus("mandatory")
_IsdnTrunkMgmntId_Type = Integer32
_IsdnTrunkMgmntId_Object = MibTableColumn
isdnTrunkMgmntId = _IsdnTrunkMgmntId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 4, 2, 1, 1),
    _IsdnTrunkMgmntId_Type()
)
isdnTrunkMgmntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnTrunkMgmntId.setStatus("mandatory")
_IsdnChnlMgmntId_Type = Integer32
_IsdnChnlMgmntId_Object = MibTableColumn
isdnChnlMgmntId = _IsdnChnlMgmntId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 4, 2, 1, 2),
    _IsdnChnlMgmntId_Type()
)
isdnChnlMgmntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnChnlMgmntId.setStatus("mandatory")
_IsdnChnlMgmntCmd_Type = IsdnChnlMgtOperation
_IsdnChnlMgmntCmd_Object = MibTableColumn
isdnChnlMgmntCmd = _IsdnChnlMgmntCmd_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 4, 2, 1, 3),
    _IsdnChnlMgmntCmd_Type()
)
isdnChnlMgmntCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnChnlMgmntCmd.setStatus("mandatory")
_MfdMgmntTable_Object = MibTable
mfdMgmntTable = _MfdMgmntTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    mfdMgmntTable.setStatus("mandatory")
_MfdMgmntEntry_Object = MibTableRow
mfdMgmntEntry = _MfdMgmntEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 4, 3, 1)
)
mfdMgmntEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "isdnTnkMgmntId"),
)
if mibBuilder.loadTexts:
    mfdMgmntEntry.setStatus("mandatory")
_IsdnTnkMgmntId_Type = Integer32
_IsdnTnkMgmntId_Object = MibTableColumn
isdnTnkMgmntId = _IsdnTnkMgmntId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 4, 3, 1, 1),
    _IsdnTnkMgmntId_Type()
)
isdnTnkMgmntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnTnkMgmntId.setStatus("mandatory")


class _IsdnDurThreshold_Type(Integer32):
    """Custom type isdnDurThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnDurThreshold_Type.__name__ = "Integer32"
_IsdnDurThreshold_Object = MibTableColumn
isdnDurThreshold = _IsdnDurThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 4, 3, 1, 2),
    _IsdnDurThreshold_Type()
)
isdnDurThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnDurThreshold.setStatus("mandatory")


class _IsdnCntThreshold_Type(Integer32):
    """Custom type isdnCntThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IsdnCntThreshold_Type.__name__ = "Integer32"
_IsdnCntThreshold_Object = MibTableColumn
isdnCntThreshold = _IsdnCntThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 4, 3, 1, 3),
    _IsdnCntThreshold_Type()
)
isdnCntThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnCntThreshold.setStatus("mandatory")
_MfdMgmntCmd_Type = EnableOperation
_MfdMgmntCmd_Object = MibTableColumn
mfdMgmntCmd = _MfdMgmntCmd_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 2, 4, 3, 1, 4),
    _MfdMgmntCmd_Type()
)
mfdMgmntCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfdMgmntCmd.setStatus("mandatory")
_TrnkGrp_ObjectIdentity = ObjectIdentity
trnkGrp = _TrnkGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 3)
)
_TrunkGrpCfgTable_Object = MibTable
trunkGrpCfgTable = _TrunkGrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    trunkGrpCfgTable.setStatus("mandatory")
_TrunkGrpCfgEntry_Object = MibTableRow
trunkGrpCfgEntry = _TrunkGrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 3, 1, 1)
)
trunkGrpCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "trunkGrpId"),
)
if mibBuilder.loadTexts:
    trunkGrpCfgEntry.setStatus("mandatory")


class _TrunkGrpId_Type(Integer32):
    """Custom type trunkGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrunkGrpId_Type.__name__ = "Integer32"
_TrunkGrpId_Object = MibTableColumn
trunkGrpId = _TrunkGrpId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 3, 1, 1, 1),
    _TrunkGrpId_Type()
)
trunkGrpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkGrpId.setStatus("mandatory")


class _TrunkGrpName_Type(DisplayString):
    """Custom type trunkGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_TrunkGrpName_Type.__name__ = "DisplayString"
_TrunkGrpName_Object = MibTableColumn
trunkGrpName = _TrunkGrpName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 3, 1, 1, 2),
    _TrunkGrpName_Type()
)
trunkGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkGrpName.setStatus("mandatory")


class _TrunkGrpCarrierId_Type(Integer32):
    """Custom type trunkGrpCarrierId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrunkGrpCarrierId_Type.__name__ = "Integer32"
_TrunkGrpCarrierId_Object = MibTableColumn
trunkGrpCarrierId = _TrunkGrpCarrierId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 3, 1, 1, 3),
    _TrunkGrpCarrierId_Type()
)
trunkGrpCarrierId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkGrpCarrierId.setStatus("mandatory")
_TrunkGrpType_Type = TrnkGrpType
_TrunkGrpType_Object = MibTableColumn
trunkGrpType = _TrunkGrpType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 3, 1, 1, 4),
    _TrunkGrpType_Type()
)
trunkGrpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkGrpType.setStatus("mandatory")
_TrunkGrpRoffName_Type = NameString
_TrunkGrpRoffName_Object = MibTableColumn
trunkGrpRoffName = _TrunkGrpRoffName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 3, 1, 1, 5),
    _TrunkGrpRoffName_Type()
)
trunkGrpRoffName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkGrpRoffName.setStatus("mandatory")
_TrunkGrpRoffType_Type = RoffType
_TrunkGrpRoffType_Object = MibTableColumn
trunkGrpRoffType = _TrunkGrpRoffType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 3, 1, 1, 6),
    _TrunkGrpRoffType_Type()
)
trunkGrpRoffType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkGrpRoffType.setStatus("mandatory")
_TrunkGrpCdrFlag_Type = CdrFlag
_TrunkGrpCdrFlag_Object = MibTableColumn
trunkGrpCdrFlag = _TrunkGrpCdrFlag_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 3, 1, 1, 7),
    _TrunkGrpCdrFlag_Type()
)
trunkGrpCdrFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkGrpCdrFlag.setStatus("mandatory")


class _TrunkGrpNoOfTrunks_Type(Integer32):
    """Custom type trunkGrpNoOfTrunks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrunkGrpNoOfTrunks_Type.__name__ = "Integer32"
_TrunkGrpNoOfTrunks_Object = MibTableColumn
trunkGrpNoOfTrunks = _TrunkGrpNoOfTrunks_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 3, 1, 1, 8),
    _TrunkGrpNoOfTrunks_Type()
)
trunkGrpNoOfTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGrpNoOfTrunks.setStatus("mandatory")
_TrunkGrpVoicePcm_Type = VoicePcm
_TrunkGrpVoicePcm_Object = MibTableColumn
trunkGrpVoicePcm = _TrunkGrpVoicePcm_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 3, 1, 1, 9),
    _TrunkGrpVoicePcm_Type()
)
trunkGrpVoicePcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkGrpVoicePcm.setStatus("mandatory")
_TrunkGrpRowStatus_Type = RowStatus
_TrunkGrpRowStatus_Object = MibTableColumn
trunkGrpRowStatus = _TrunkGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 3, 1, 1, 10),
    _TrunkGrpRowStatus_Type()
)
trunkGrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkGrpRowStatus.setStatus("mandatory")
_TrunkGrpOpStatus_Type = OpStatus
_TrunkGrpOpStatus_Object = MibTableColumn
trunkGrpOpStatus = _TrunkGrpOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 3, 1, 1, 11),
    _TrunkGrpOpStatus_Type()
)
trunkGrpOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkGrpOpStatus.setStatus("mandatory")
_Rt_ObjectIdentity = ObjectIdentity
rt = _Rt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4)
)
_RouteTable_Object = MibTable
routeTable = _RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    routeTable.setStatus("mandatory")
_RouteEntry_Object = MibTableRow
routeEntry = _RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 1, 1)
)
routeEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "routeId"),
)
if mibBuilder.loadTexts:
    routeEntry.setStatus("mandatory")


class _RouteId_Type(Integer32):
    """Custom type routeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RouteId_Type.__name__ = "Integer32"
_RouteId_Object = MibTableColumn
routeId = _RouteId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 1, 1, 1),
    _RouteId_Type()
)
routeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeId.setStatus("mandatory")
_RouteAddrType_Type = AddrType
_RouteAddrType_Object = MibTableColumn
routeAddrType = _RouteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 1, 1, 2),
    _RouteAddrType_Type()
)
routeAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeAddrType.setStatus("mandatory")
_RouteAdrId_Type = AddrIdentifier
_RouteAdrId_Object = MibTableColumn
routeAdrId = _RouteAdrId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 1, 1, 3),
    _RouteAdrId_Type()
)
routeAdrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeAdrId.setStatus("mandatory")
_RouteAddr_Type = AddrString
_RouteAddr_Object = MibTableColumn
routeAddr = _RouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 1, 1, 4),
    _RouteAddr_Type()
)
routeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeAddr.setStatus("mandatory")
_RouteNumPlan_Type = NumPlan
_RouteNumPlan_Object = MibTableColumn
routeNumPlan = _RouteNumPlan_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 1, 1, 5),
    _RouteNumPlan_Type()
)
routeNumPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeNumPlan.setStatus("mandatory")


class _RouteNumOfDigit_Type(Integer32):
    """Custom type routeNumOfDigit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RouteNumOfDigit_Type.__name__ = "Integer32"
_RouteNumOfDigit_Object = MibTableColumn
routeNumOfDigit = _RouteNumOfDigit_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 1, 1, 6),
    _RouteNumOfDigit_Type()
)
routeNumOfDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeNumOfDigit.setStatus("mandatory")
_RouteRouteName_Type = NameString
_RouteRouteName_Object = MibTableColumn
routeRouteName = _RouteRouteName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 1, 1, 7),
    _RouteRouteName_Type()
)
routeRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeRouteName.setStatus("mandatory")
_RouteRouteType_Type = RouteType
_RouteRouteType_Object = MibTableColumn
routeRouteType = _RouteRouteType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 1, 1, 8),
    _RouteRouteType_Type()
)
routeRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeRouteType.setStatus("mandatory")
_RouteRowStatus_Type = RowStatus
_RouteRowStatus_Object = MibTableColumn
routeRowStatus = _RouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 1, 1, 9),
    _RouteRowStatus_Type()
)
routeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeRowStatus.setStatus("mandatory")
_RouteOpStatus_Type = OpStatus
_RouteOpStatus_Object = MibTableColumn
routeOpStatus = _RouteOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 1, 1, 10),
    _RouteOpStatus_Type()
)
routeOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeOpStatus.setStatus("mandatory")
_RtEntryIsdnCfgTable_Object = MibTable
rtEntryIsdnCfgTable = _RtEntryIsdnCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    rtEntryIsdnCfgTable.setStatus("mandatory")
_RtEntryIsdnCfgEntry_Object = MibTableRow
rtEntryIsdnCfgEntry = _RtEntryIsdnCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 2, 1)
)
rtEntryIsdnCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "rtEntryIsdnGrpId"),
    (0, "ARMILLAIRE2000-MIB", "rtEntryIsdntrunkId"),
)
if mibBuilder.loadTexts:
    rtEntryIsdnCfgEntry.setStatus("mandatory")


class _RtEntryIsdnGrpId_Type(Integer32):
    """Custom type rtEntryIsdnGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RtEntryIsdnGrpId_Type.__name__ = "Integer32"
_RtEntryIsdnGrpId_Object = MibTableColumn
rtEntryIsdnGrpId = _RtEntryIsdnGrpId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 2, 1, 1),
    _RtEntryIsdnGrpId_Type()
)
rtEntryIsdnGrpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtEntryIsdnGrpId.setStatus("mandatory")


class _RtEntryIsdntrunkId_Type(Integer32):
    """Custom type rtEntryIsdntrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_RtEntryIsdntrunkId_Type.__name__ = "Integer32"
_RtEntryIsdntrunkId_Object = MibTableColumn
rtEntryIsdntrunkId = _RtEntryIsdntrunkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 2, 1, 2),
    _RtEntryIsdntrunkId_Type()
)
rtEntryIsdntrunkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtEntryIsdntrunkId.setStatus("mandatory")
_RtEntryIsdnRouteName_Type = NameString
_RtEntryIsdnRouteName_Object = MibTableColumn
rtEntryIsdnRouteName = _RtEntryIsdnRouteName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 2, 1, 3),
    _RtEntryIsdnRouteName_Type()
)
rtEntryIsdnRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtEntryIsdnRouteName.setStatus("mandatory")
_RtEntryIsdnRowStatus_Type = RowStatus
_RtEntryIsdnRowStatus_Object = MibTableColumn
rtEntryIsdnRowStatus = _RtEntryIsdnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 2, 1, 4),
    _RtEntryIsdnRowStatus_Type()
)
rtEntryIsdnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtEntryIsdnRowStatus.setStatus("mandatory")
_RtEntryIsdnOpStatus_Type = OpStatus
_RtEntryIsdnOpStatus_Object = MibTableColumn
rtEntryIsdnOpStatus = _RtEntryIsdnOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 2, 1, 5),
    _RtEntryIsdnOpStatus_Type()
)
rtEntryIsdnOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtEntryIsdnOpStatus.setStatus("mandatory")
_RtEntrySs7CfgTable_Object = MibTable
rtEntrySs7CfgTable = _RtEntrySs7CfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    rtEntrySs7CfgTable.setStatus("mandatory")
_RtEntrySs7CfgEntry_Object = MibTableRow
rtEntrySs7CfgEntry = _RtEntrySs7CfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 3, 1)
)
rtEntrySs7CfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "rtEntrySs7GrpId"),
    (0, "ARMILLAIRE2000-MIB", "rtEntrySs7CmbLinksetId"),
)
if mibBuilder.loadTexts:
    rtEntrySs7CfgEntry.setStatus("mandatory")


class _RtEntrySs7GrpId_Type(Integer32):
    """Custom type rtEntrySs7GrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RtEntrySs7GrpId_Type.__name__ = "Integer32"
_RtEntrySs7GrpId_Object = MibTableColumn
rtEntrySs7GrpId = _RtEntrySs7GrpId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 3, 1, 1),
    _RtEntrySs7GrpId_Type()
)
rtEntrySs7GrpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtEntrySs7GrpId.setStatus("mandatory")


class _RtEntrySs7CmbLinksetId_Type(Integer32):
    """Custom type rtEntrySs7CmbLinksetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RtEntrySs7CmbLinksetId_Type.__name__ = "Integer32"
_RtEntrySs7CmbLinksetId_Object = MibTableColumn
rtEntrySs7CmbLinksetId = _RtEntrySs7CmbLinksetId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 3, 1, 2),
    _RtEntrySs7CmbLinksetId_Type()
)
rtEntrySs7CmbLinksetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtEntrySs7CmbLinksetId.setStatus("mandatory")
_RtEntrySs7RouteName_Type = NameString
_RtEntrySs7RouteName_Object = MibTableColumn
rtEntrySs7RouteName = _RtEntrySs7RouteName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 3, 1, 3),
    _RtEntrySs7RouteName_Type()
)
rtEntrySs7RouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtEntrySs7RouteName.setStatus("mandatory")


class _RtEntrySs7Dpc_Type(Integer32):
    """Custom type rtEntrySs7Dpc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_RtEntrySs7Dpc_Type.__name__ = "Integer32"
_RtEntrySs7Dpc_Object = MibTableColumn
rtEntrySs7Dpc = _RtEntrySs7Dpc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 3, 1, 4),
    _RtEntrySs7Dpc_Type()
)
rtEntrySs7Dpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtEntrySs7Dpc.setStatus("mandatory")
_RtEntrySs7Mode_Type = Standard
_RtEntrySs7Mode_Object = MibTableColumn
rtEntrySs7Mode = _RtEntrySs7Mode_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 3, 1, 5),
    _RtEntrySs7Mode_Type()
)
rtEntrySs7Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtEntrySs7Mode.setStatus("mandatory")
_RtEntrySs7RowStatus_Type = RowStatus
_RtEntrySs7RowStatus_Object = MibTableColumn
rtEntrySs7RowStatus = _RtEntrySs7RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 3, 1, 6),
    _RtEntrySs7RowStatus_Type()
)
rtEntrySs7RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtEntrySs7RowStatus.setStatus("mandatory")
_RtEntrySs7OpStatus_Type = OpStatus
_RtEntrySs7OpStatus_Object = MibTableColumn
rtEntrySs7OpStatus = _RtEntrySs7OpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 3, 1, 7),
    _RtEntrySs7OpStatus_Type()
)
rtEntrySs7OpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtEntrySs7OpStatus.setStatus("mandatory")
_RouteMgmntCmdGroup_ObjectIdentity = ObjectIdentity
routeMgmntCmdGroup = _RouteMgmntCmdGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 4)
)
_DigitStripMgmntTable_Object = MibTable
digitStripMgmntTable = _DigitStripMgmntTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 4, 1)
)
if mibBuilder.loadTexts:
    digitStripMgmntTable.setStatus("mandatory")
_DigitStripMgmntEntry_Object = MibTableRow
digitStripMgmntEntry = _DigitStripMgmntEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 4, 1, 1)
)
digitStripMgmntEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "rtName"),
)
if mibBuilder.loadTexts:
    digitStripMgmntEntry.setStatus("mandatory")
_RtName_Type = NameString
_RtName_Object = MibTableColumn
rtName = _RtName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 4, 1, 1, 1),
    _RtName_Type()
)
rtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtName.setStatus("mandatory")
_RtAddrType_Type = AddrIdentifier
_RtAddrType_Object = MibTableColumn
rtAddrType = _RtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 4, 1, 1, 2),
    _RtAddrType_Type()
)
rtAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtAddrType.setStatus("mandatory")


class _RtNumOfDigit_Type(Integer32):
    """Custom type rtNumOfDigit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RtNumOfDigit_Type.__name__ = "Integer32"
_RtNumOfDigit_Object = MibTableColumn
rtNumOfDigit = _RtNumOfDigit_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 4, 1, 1, 3),
    _RtNumOfDigit_Type()
)
rtNumOfDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtNumOfDigit.setStatus("mandatory")
_RtMgmntCmd_Type = EnableOperation
_RtMgmntCmd_Object = MibTableColumn
rtMgmntCmd = _RtMgmntCmd_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 4, 1, 1, 4),
    _RtMgmntCmd_Type()
)
rtMgmntCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtMgmntCmd.setStatus("mandatory")
_IsdnLoadBalanceMgmntTable_Object = MibTable
isdnLoadBalanceMgmntTable = _IsdnLoadBalanceMgmntTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 4, 2)
)
if mibBuilder.loadTexts:
    isdnLoadBalanceMgmntTable.setStatus("mandatory")
_IsdnLoadBalanceMgmntEntry_Object = MibTableRow
isdnLoadBalanceMgmntEntry = _IsdnLoadBalanceMgmntEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 4, 2, 1)
)
isdnLoadBalanceMgmntEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "rteName"),
)
if mibBuilder.loadTexts:
    isdnLoadBalanceMgmntEntry.setStatus("mandatory")
_RteName_Type = NameString
_RteName_Object = MibTableColumn
rteName = _RteName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 4, 2, 1, 1),
    _RteName_Type()
)
rteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rteName.setStatus("mandatory")
_IlbMgmntCmd_Type = EnableOperation
_IlbMgmntCmd_Object = MibTableColumn
ilbMgmntCmd = _IlbMgmntCmd_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 4, 4, 2, 1, 2),
    _IlbMgmntCmd_Type()
)
ilbMgmntCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ilbMgmntCmd.setStatus("mandatory")
_Xconnect_ObjectIdentity = ObjectIdentity
xconnect = _Xconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5)
)
_XconnectCfgTable_Object = MibTable
xconnectCfgTable = _XconnectCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    xconnectCfgTable.setStatus("mandatory")
_XconnectCfgEntry_Object = MibTableRow
xconnectCfgEntry = _XconnectCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 1, 1)
)
xconnectCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "xconnectId"),
)
if mibBuilder.loadTexts:
    xconnectCfgEntry.setStatus("mandatory")


class _XconnectId_Type(Integer32):
    """Custom type xconnectId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XconnectId_Type.__name__ = "Integer32"
_XconnectId_Object = MibTableColumn
xconnectId = _XconnectId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 1, 1, 1),
    _XconnectId_Type()
)
xconnectId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xconnectId.setStatus("mandatory")
_XconnectName_Type = NameString
_XconnectName_Object = MibTableColumn
xconnectName = _XconnectName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 1, 1, 2),
    _XconnectName_Type()
)
xconnectName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xconnectName.setStatus("mandatory")
_XconnectIPAddr_Type = IpAddress
_XconnectIPAddr_Object = MibTableColumn
xconnectIPAddr = _XconnectIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 1, 1, 3),
    _XconnectIPAddr_Type()
)
xconnectIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xconnectIPAddr.setStatus("mandatory")


class _XconnectTCPPort_Type(Integer32):
    """Custom type xconnectTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XconnectTCPPort_Type.__name__ = "Integer32"
_XconnectTCPPort_Object = MibTableColumn
xconnectTCPPort = _XconnectTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 1, 1, 4),
    _XconnectTCPPort_Type()
)
xconnectTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xconnectTCPPort.setStatus("mandatory")
_XconnectRowStatus_Type = RowStatus
_XconnectRowStatus_Object = MibTableColumn
xconnectRowStatus = _XconnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 1, 1, 5),
    _XconnectRowStatus_Type()
)
xconnectRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xconnectRowStatus.setStatus("mandatory")
_XconnectOpStatus_Type = OpStatus
_XconnectOpStatus_Object = MibTableColumn
xconnectOpStatus = _XconnectOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 1, 1, 6),
    _XconnectOpStatus_Type()
)
xconnectOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xconnectOpStatus.setStatus("mandatory")
_XlinkCfgTable_Object = MibTable
xlinkCfgTable = _XlinkCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    xlinkCfgTable.setStatus("mandatory")
_XlinkCfgEntry_Object = MibTableRow
xlinkCfgEntry = _XlinkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 2, 1)
)
xlinkCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "xconnectIdEndA"),
    (0, "ARMILLAIRE2000-MIB", "slotIdEndA"),
    (0, "ARMILLAIRE2000-MIB", "portIdEndA"),
    (0, "ARMILLAIRE2000-MIB", "xconnectIdEndB"),
    (0, "ARMILLAIRE2000-MIB", "slotIdEndB"),
    (0, "ARMILLAIRE2000-MIB", "portIdEndB"),
)
if mibBuilder.loadTexts:
    xlinkCfgEntry.setStatus("mandatory")


class _XconnectIdEndA_Type(Integer32):
    """Custom type xconnectIdEndA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XconnectIdEndA_Type.__name__ = "Integer32"
_XconnectIdEndA_Object = MibTableColumn
xconnectIdEndA = _XconnectIdEndA_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 2, 1, 1),
    _XconnectIdEndA_Type()
)
xconnectIdEndA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xconnectIdEndA.setStatus("mandatory")


class _SlotIdEndA_Type(Integer32):
    """Custom type slotIdEndA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlotIdEndA_Type.__name__ = "Integer32"
_SlotIdEndA_Object = MibTableColumn
slotIdEndA = _SlotIdEndA_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 2, 1, 2),
    _SlotIdEndA_Type()
)
slotIdEndA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotIdEndA.setStatus("mandatory")


class _PortIdEndA_Type(Integer32):
    """Custom type portIdEndA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortIdEndA_Type.__name__ = "Integer32"
_PortIdEndA_Object = MibTableColumn
portIdEndA = _PortIdEndA_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 2, 1, 3),
    _PortIdEndA_Type()
)
portIdEndA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIdEndA.setStatus("mandatory")


class _XconnectIdEndB_Type(Integer32):
    """Custom type xconnectIdEndB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XconnectIdEndB_Type.__name__ = "Integer32"
_XconnectIdEndB_Object = MibTableColumn
xconnectIdEndB = _XconnectIdEndB_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 2, 1, 4),
    _XconnectIdEndB_Type()
)
xconnectIdEndB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xconnectIdEndB.setStatus("mandatory")


class _SlotIdEndB_Type(Integer32):
    """Custom type slotIdEndB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlotIdEndB_Type.__name__ = "Integer32"
_SlotIdEndB_Object = MibTableColumn
slotIdEndB = _SlotIdEndB_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 2, 1, 5),
    _SlotIdEndB_Type()
)
slotIdEndB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotIdEndB.setStatus("mandatory")


class _PortIdEndB_Type(Integer32):
    """Custom type portIdEndB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortIdEndB_Type.__name__ = "Integer32"
_PortIdEndB_Object = MibTableColumn
portIdEndB = _PortIdEndB_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 2, 1, 6),
    _PortIdEndB_Type()
)
portIdEndB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIdEndB.setStatus("mandatory")
_XlinkConnectionType_Type = ConnectionType
_XlinkConnectionType_Object = MibTableColumn
xlinkConnectionType = _XlinkConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 2, 1, 7),
    _XlinkConnectionType_Type()
)
xlinkConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xlinkConnectionType.setStatus("mandatory")
_XlinkRowStatus_Type = RowStatus
_XlinkRowStatus_Object = MibTableColumn
xlinkRowStatus = _XlinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 2, 1, 8),
    _XlinkRowStatus_Type()
)
xlinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xlinkRowStatus.setStatus("mandatory")
_XlinkOpStatus_Type = OpStatus
_XlinkOpStatus_Object = MibTableColumn
xlinkOpStatus = _XlinkOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 2, 1, 9),
    _XlinkOpStatus_Type()
)
xlinkOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xlinkOpStatus.setStatus("mandatory")
_XlinkMgmntTable_Object = MibTable
xlinkMgmntTable = _XlinkMgmntTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 3)
)
if mibBuilder.loadTexts:
    xlinkMgmntTable.setStatus("mandatory")
_XlinkMgmntEntry_Object = MibTableRow
xlinkMgmntEntry = _XlinkMgmntEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 3, 1)
)
xlinkMgmntEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "xconnIdEndA"),
    (0, "ARMILLAIRE2000-MIB", "xconnSlotIdEndA"),
    (0, "ARMILLAIRE2000-MIB", "xconnPortIdEndA"),
    (0, "ARMILLAIRE2000-MIB", "xconnIdEndB"),
    (0, "ARMILLAIRE2000-MIB", "xconnSlotIdEndB"),
    (0, "ARMILLAIRE2000-MIB", "xconnPortIdEndB"),
)
if mibBuilder.loadTexts:
    xlinkMgmntEntry.setStatus("mandatory")


class _XconnIdEndA_Type(Integer32):
    """Custom type xconnIdEndA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XconnIdEndA_Type.__name__ = "Integer32"
_XconnIdEndA_Object = MibTableColumn
xconnIdEndA = _XconnIdEndA_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 3, 1, 1),
    _XconnIdEndA_Type()
)
xconnIdEndA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xconnIdEndA.setStatus("mandatory")


class _XconnSlotIdEndA_Type(Integer32):
    """Custom type xconnSlotIdEndA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XconnSlotIdEndA_Type.__name__ = "Integer32"
_XconnSlotIdEndA_Object = MibTableColumn
xconnSlotIdEndA = _XconnSlotIdEndA_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 3, 1, 2),
    _XconnSlotIdEndA_Type()
)
xconnSlotIdEndA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xconnSlotIdEndA.setStatus("mandatory")


class _XconnPortIdEndA_Type(Integer32):
    """Custom type xconnPortIdEndA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XconnPortIdEndA_Type.__name__ = "Integer32"
_XconnPortIdEndA_Object = MibTableColumn
xconnPortIdEndA = _XconnPortIdEndA_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 3, 1, 3),
    _XconnPortIdEndA_Type()
)
xconnPortIdEndA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xconnPortIdEndA.setStatus("mandatory")


class _XconnIdEndB_Type(Integer32):
    """Custom type xconnIdEndB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XconnIdEndB_Type.__name__ = "Integer32"
_XconnIdEndB_Object = MibTableColumn
xconnIdEndB = _XconnIdEndB_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 3, 1, 4),
    _XconnIdEndB_Type()
)
xconnIdEndB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xconnIdEndB.setStatus("mandatory")


class _XconnSlotIdEndB_Type(Integer32):
    """Custom type xconnSlotIdEndB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XconnSlotIdEndB_Type.__name__ = "Integer32"
_XconnSlotIdEndB_Object = MibTableColumn
xconnSlotIdEndB = _XconnSlotIdEndB_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 3, 1, 5),
    _XconnSlotIdEndB_Type()
)
xconnSlotIdEndB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xconnSlotIdEndB.setStatus("mandatory")
_XconnPortIdEndB_Type = Integer32
_XconnPortIdEndB_Object = MibTableColumn
xconnPortIdEndB = _XconnPortIdEndB_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 3, 1, 6),
    _XconnPortIdEndB_Type()
)
xconnPortIdEndB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xconnPortIdEndB.setStatus("mandatory")
_XlinkMgmntCmd_Type = EnableOperation
_XlinkMgmntCmd_Object = MibTableColumn
xlinkMgmntCmd = _XlinkMgmntCmd_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 5, 3, 1, 7),
    _XlinkMgmntCmd_Type()
)
xlinkMgmntCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xlinkMgmntCmd.setStatus("mandatory")
_EnableGroup_ObjectIdentity = ObjectIdentity
enableGroup = _EnableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 6)
)
_EnableSwitch_Type = EnableStatus
_EnableSwitch_Object = MibScalar
enableSwitch = _EnableSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 6, 1),
    _EnableSwitch_Type()
)
enableSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSwitch.setStatus("mandatory")
_EnableSS7Route_Type = EnableStatus
_EnableSS7Route_Object = MibScalar
enableSS7Route = _EnableSS7Route_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 6, 2),
    _EnableSS7Route_Type()
)
enableSS7Route.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSS7Route.setStatus("mandatory")
_EnableSS7Ckt_Type = EnableStatus
_EnableSS7Ckt_Object = MibScalar
enableSS7Ckt = _EnableSS7Ckt_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 6, 3),
    _EnableSS7Ckt_Type()
)
enableSS7Ckt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSS7Ckt.setStatus("mandatory")
_EnableIsdntrunk_Type = EnableStatus
_EnableIsdntrunk_Object = MibScalar
enableIsdntrunk = _EnableIsdntrunk_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 6, 4),
    _EnableIsdntrunk_Type()
)
enableIsdntrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableIsdntrunk.setStatus("mandatory")
_EnableXconnect_Type = EnableStatus
_EnableXconnect_Object = MibScalar
enableXconnect = _EnableXconnect_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 6, 5),
    _EnableXconnect_Type()
)
enableXconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableXconnect.setStatus("mandatory")
_EnableRoute_Type = EnableStatus
_EnableRoute_Object = MibScalar
enableRoute = _EnableRoute_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 2, 6, 6),
    _EnableRoute_Type()
)
enableRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableRoute.setStatus("mandatory")
_SwitchMeas_ObjectIdentity = ObjectIdentity
switchMeas = _SwitchMeas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3)
)
_MeasFile_ObjectIdentity = ObjectIdentity
measFile = _MeasFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1)
)
_MeasFileInfo_ObjectIdentity = ObjectIdentity
measFileInfo = _MeasFileInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1, 1)
)


class _MeasFileAcknowledge_Type(DisplayString):
    """Custom type measFileAcknowledge based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MeasFileAcknowledge_Type.__name__ = "DisplayString"
_MeasFileAcknowledge_Object = MibScalar
measFileAcknowledge = _MeasFileAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1, 1, 1),
    _MeasFileAcknowledge_Type()
)
measFileAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    measFileAcknowledge.setStatus("mandatory")
_MeasFileConfig_ObjectIdentity = ObjectIdentity
measFileConfig = _MeasFileConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1, 2)
)


class _MeasFileCfgMeasInterval_Type(Integer32):
    """Custom type measFileCfgMeasInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_MeasFileCfgMeasInterval_Type.__name__ = "Integer32"
_MeasFileCfgMeasInterval_Object = MibScalar
measFileCfgMeasInterval = _MeasFileCfgMeasInterval_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1, 2, 1),
    _MeasFileCfgMeasInterval_Type()
)
measFileCfgMeasInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    measFileCfgMeasInterval.setStatus("mandatory")


class _MeasFileCfgUsagescanInterval_Type(Integer32):
    """Custom type measFileCfgUsagescanInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_MeasFileCfgUsagescanInterval_Type.__name__ = "Integer32"
_MeasFileCfgUsagescanInterval_Object = MibScalar
measFileCfgUsagescanInterval = _MeasFileCfgUsagescanInterval_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1, 2, 2),
    _MeasFileCfgUsagescanInterval_Type()
)
measFileCfgUsagescanInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    measFileCfgUsagescanInterval.setStatus("mandatory")


class _MeasFileCfgPurgeDay_Type(Integer32):
    """Custom type measFileCfgPurgeDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_MeasFileCfgPurgeDay_Type.__name__ = "Integer32"
_MeasFileCfgPurgeDay_Object = MibScalar
measFileCfgPurgeDay = _MeasFileCfgPurgeDay_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1, 2, 3),
    _MeasFileCfgPurgeDay_Type()
)
measFileCfgPurgeDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    measFileCfgPurgeDay.setStatus("mandatory")
_MeasFileCfgPurgeFlag_Type = MeasPurgeFlag
_MeasFileCfgPurgeFlag_Object = MibScalar
measFileCfgPurgeFlag = _MeasFileCfgPurgeFlag_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1, 2, 4),
    _MeasFileCfgPurgeFlag_Type()
)
measFileCfgPurgeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    measFileCfgPurgeFlag.setStatus("mandatory")
_MeasFileCfgPrimaryDir_Type = DisplayString
_MeasFileCfgPrimaryDir_Object = MibScalar
measFileCfgPrimaryDir = _MeasFileCfgPrimaryDir_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1, 2, 5),
    _MeasFileCfgPrimaryDir_Type()
)
measFileCfgPrimaryDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measFileCfgPrimaryDir.setStatus("mandatory")
_MeasFileCfgSecondaryDir_Type = DisplayString
_MeasFileCfgSecondaryDir_Object = MibScalar
measFileCfgSecondaryDir = _MeasFileCfgSecondaryDir_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1, 2, 6),
    _MeasFileCfgSecondaryDir_Type()
)
measFileCfgSecondaryDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measFileCfgSecondaryDir.setStatus("mandatory")
_MeasFileEnableGrp_ObjectIdentity = ObjectIdentity
measFileEnableGrp = _MeasFileEnableGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1, 3)
)
_MeasFileEnablePRITraffic_Type = MeasEnableStatus
_MeasFileEnablePRITraffic_Object = MibScalar
measFileEnablePRITraffic = _MeasFileEnablePRITraffic_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1, 3, 1),
    _MeasFileEnablePRITraffic_Type()
)
measFileEnablePRITraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    measFileEnablePRITraffic.setStatus("mandatory")
_MeasFileEnableISUPTraffic_Type = MeasEnableStatus
_MeasFileEnableISUPTraffic_Object = MibScalar
measFileEnableISUPTraffic = _MeasFileEnableISUPTraffic_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1, 3, 2),
    _MeasFileEnableISUPTraffic_Type()
)
measFileEnableISUPTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    measFileEnableISUPTraffic.setStatus("mandatory")
_MeasFileEnablePRIIneffectiveCall_Type = MeasEnableStatus
_MeasFileEnablePRIIneffectiveCall_Object = MibScalar
measFileEnablePRIIneffectiveCall = _MeasFileEnablePRIIneffectiveCall_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1, 3, 3),
    _MeasFileEnablePRIIneffectiveCall_Type()
)
measFileEnablePRIIneffectiveCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    measFileEnablePRIIneffectiveCall.setStatus("mandatory")
_MeasFileEnableISUPIneffectiveCall_Type = MeasEnableStatus
_MeasFileEnableISUPIneffectiveCall_Object = MibScalar
measFileEnableISUPIneffectiveCall = _MeasFileEnableISUPIneffectiveCall_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1, 3, 4),
    _MeasFileEnableISUPIneffectiveCall_Type()
)
measFileEnableISUPIneffectiveCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    measFileEnableISUPIneffectiveCall.setStatus("mandatory")
_MeasFileEnableTrunkGrp_Type = MeasEnableStatus
_MeasFileEnableTrunkGrp_Object = MibScalar
measFileEnableTrunkGrp = _MeasFileEnableTrunkGrp_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1, 3, 5),
    _MeasFileEnableTrunkGrp_Type()
)
measFileEnableTrunkGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    measFileEnableTrunkGrp.setStatus("mandatory")
_MeasFileEnableSS7LinkTraffic_Type = MeasEnableStatus
_MeasFileEnableSS7LinkTraffic_Object = MibScalar
measFileEnableSS7LinkTraffic = _MeasFileEnableSS7LinkTraffic_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 1, 3, 6),
    _MeasFileEnableSS7LinkTraffic_Type()
)
measFileEnableSS7LinkTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    measFileEnableSS7LinkTraffic.setStatus("mandatory")
_MeasSwitch_ObjectIdentity = ObjectIdentity
measSwitch = _MeasSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2)
)
_MeasSwitchIsupGrp_ObjectIdentity = ObjectIdentity
measSwitchIsupGrp = _MeasSwitchIsupGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 1)
)
_MeasSwitchIsupDataSuspect_Type = Counter32
_MeasSwitchIsupDataSuspect_Object = MibScalar
measSwitchIsupDataSuspect = _MeasSwitchIsupDataSuspect_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 1, 1),
    _MeasSwitchIsupDataSuspect_Type()
)
measSwitchIsupDataSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupDataSuspect.setStatus("mandatory")
_MeasSwitchIsupIncomingAnsiTrunkCallAttempts_Type = Counter32
_MeasSwitchIsupIncomingAnsiTrunkCallAttempts_Object = MibScalar
measSwitchIsupIncomingAnsiTrunkCallAttempts = _MeasSwitchIsupIncomingAnsiTrunkCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 1, 2),
    _MeasSwitchIsupIncomingAnsiTrunkCallAttempts_Type()
)
measSwitchIsupIncomingAnsiTrunkCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupIncomingAnsiTrunkCallAttempts.setStatus("mandatory")
_MeasSwitchIsupIncomingAnsiTrunkCallAnswered_Type = Counter32
_MeasSwitchIsupIncomingAnsiTrunkCallAnswered_Object = MibScalar
measSwitchIsupIncomingAnsiTrunkCallAnswered = _MeasSwitchIsupIncomingAnsiTrunkCallAnswered_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 1, 3),
    _MeasSwitchIsupIncomingAnsiTrunkCallAnswered_Type()
)
measSwitchIsupIncomingAnsiTrunkCallAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupIncomingAnsiTrunkCallAnswered.setStatus("mandatory")
_MeasSwitchIsupOutgoingAnsiTrunkCallAttempts_Type = Counter32
_MeasSwitchIsupOutgoingAnsiTrunkCallAttempts_Object = MibScalar
measSwitchIsupOutgoingAnsiTrunkCallAttempts = _MeasSwitchIsupOutgoingAnsiTrunkCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 1, 4),
    _MeasSwitchIsupOutgoingAnsiTrunkCallAttempts_Type()
)
measSwitchIsupOutgoingAnsiTrunkCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupOutgoingAnsiTrunkCallAttempts.setStatus("mandatory")
_MeasSwitchIsupOutgoingAnsiTrunkCallAnswered_Type = Counter32
_MeasSwitchIsupOutgoingAnsiTrunkCallAnswered_Object = MibScalar
measSwitchIsupOutgoingAnsiTrunkCallAnswered = _MeasSwitchIsupOutgoingAnsiTrunkCallAnswered_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 1, 5),
    _MeasSwitchIsupOutgoingAnsiTrunkCallAnswered_Type()
)
measSwitchIsupOutgoingAnsiTrunkCallAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupOutgoingAnsiTrunkCallAnswered.setStatus("mandatory")
_MeasSwitchIsupIncomingItutTrunkCallAttempts_Type = Counter32
_MeasSwitchIsupIncomingItutTrunkCallAttempts_Object = MibScalar
measSwitchIsupIncomingItutTrunkCallAttempts = _MeasSwitchIsupIncomingItutTrunkCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 1, 6),
    _MeasSwitchIsupIncomingItutTrunkCallAttempts_Type()
)
measSwitchIsupIncomingItutTrunkCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupIncomingItutTrunkCallAttempts.setStatus("mandatory")
_MeasSwitchIsupIncomingItutTrunkCallAnswered_Type = Counter32
_MeasSwitchIsupIncomingItutTrunkCallAnswered_Object = MibScalar
measSwitchIsupIncomingItutTrunkCallAnswered = _MeasSwitchIsupIncomingItutTrunkCallAnswered_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 1, 7),
    _MeasSwitchIsupIncomingItutTrunkCallAnswered_Type()
)
measSwitchIsupIncomingItutTrunkCallAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupIncomingItutTrunkCallAnswered.setStatus("mandatory")
_MeasSwitchIsupOutgoingItutTrunkCallAttempts_Type = Counter32
_MeasSwitchIsupOutgoingItutTrunkCallAttempts_Object = MibScalar
measSwitchIsupOutgoingItutTrunkCallAttempts = _MeasSwitchIsupOutgoingItutTrunkCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 1, 8),
    _MeasSwitchIsupOutgoingItutTrunkCallAttempts_Type()
)
measSwitchIsupOutgoingItutTrunkCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupOutgoingItutTrunkCallAttempts.setStatus("mandatory")
_MeasSwitchIsupOutgoingItutTrunkCallAnswered_Type = Counter32
_MeasSwitchIsupOutgoingItutTrunkCallAnswered_Object = MibScalar
measSwitchIsupOutgoingItutTrunkCallAnswered = _MeasSwitchIsupOutgoingItutTrunkCallAnswered_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 1, 9),
    _MeasSwitchIsupOutgoingItutTrunkCallAnswered_Type()
)
measSwitchIsupOutgoingItutTrunkCallAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupOutgoingItutTrunkCallAnswered.setStatus("mandatory")
_MeasSwitchIsupFailCallGrp_ObjectIdentity = ObjectIdentity
measSwitchIsupFailCallGrp = _MeasSwitchIsupFailCallGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 2)
)
_MeasSwitchIsupFailCallDataSuspect_Type = Counter32
_MeasSwitchIsupFailCallDataSuspect_Object = MibScalar
measSwitchIsupFailCallDataSuspect = _MeasSwitchIsupFailCallDataSuspect_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 2, 1),
    _MeasSwitchIsupFailCallDataSuspect_Type()
)
measSwitchIsupFailCallDataSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupFailCallDataSuspect.setStatus("mandatory")
_MeasSwitchIsupFailCallAnsiMatchingLoss_Type = Counter32
_MeasSwitchIsupFailCallAnsiMatchingLoss_Object = MibScalar
measSwitchIsupFailCallAnsiMatchingLoss = _MeasSwitchIsupFailCallAnsiMatchingLoss_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 2, 2),
    _MeasSwitchIsupFailCallAnsiMatchingLoss_Type()
)
measSwitchIsupFailCallAnsiMatchingLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupFailCallAnsiMatchingLoss.setStatus("mandatory")
_MeasSwitchIsupFailCallAnsiNoCircuit_Type = Counter32
_MeasSwitchIsupFailCallAnsiNoCircuit_Object = MibScalar
measSwitchIsupFailCallAnsiNoCircuit = _MeasSwitchIsupFailCallAnsiNoCircuit_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 2, 3),
    _MeasSwitchIsupFailCallAnsiNoCircuit_Type()
)
measSwitchIsupFailCallAnsiNoCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupFailCallAnsiNoCircuit.setStatus("mandatory")
_MeasSwitchIsupFailCallAnsiCalledPartyLineBusy_Type = Counter32
_MeasSwitchIsupFailCallAnsiCalledPartyLineBusy_Object = MibScalar
measSwitchIsupFailCallAnsiCalledPartyLineBusy = _MeasSwitchIsupFailCallAnsiCalledPartyLineBusy_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 2, 4),
    _MeasSwitchIsupFailCallAnsiCalledPartyLineBusy_Type()
)
measSwitchIsupFailCallAnsiCalledPartyLineBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupFailCallAnsiCalledPartyLineBusy.setStatus("mandatory")
_MeasSwitchIsupFailCallAnsiIneffectiveMachineAttempts_Type = Counter32
_MeasSwitchIsupFailCallAnsiIneffectiveMachineAttempts_Object = MibScalar
measSwitchIsupFailCallAnsiIneffectiveMachineAttempts = _MeasSwitchIsupFailCallAnsiIneffectiveMachineAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 2, 5),
    _MeasSwitchIsupFailCallAnsiIneffectiveMachineAttempts_Type()
)
measSwitchIsupFailCallAnsiIneffectiveMachineAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupFailCallAnsiIneffectiveMachineAttempts.setStatus("mandatory")
_MeasSwitchIsupFailCallItutMatchingLoss_Type = Counter32
_MeasSwitchIsupFailCallItutMatchingLoss_Object = MibScalar
measSwitchIsupFailCallItutMatchingLoss = _MeasSwitchIsupFailCallItutMatchingLoss_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 2, 6),
    _MeasSwitchIsupFailCallItutMatchingLoss_Type()
)
measSwitchIsupFailCallItutMatchingLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupFailCallItutMatchingLoss.setStatus("mandatory")
_MeasSwitchIsupFailCallItutNoCircuit_Type = Counter32
_MeasSwitchIsupFailCallItutNoCircuit_Object = MibScalar
measSwitchIsupFailCallItutNoCircuit = _MeasSwitchIsupFailCallItutNoCircuit_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 2, 7),
    _MeasSwitchIsupFailCallItutNoCircuit_Type()
)
measSwitchIsupFailCallItutNoCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupFailCallItutNoCircuit.setStatus("mandatory")
_MeasSwitchIsupFailCallItutCalledPartyLineBusy_Type = Counter32
_MeasSwitchIsupFailCallItutCalledPartyLineBusy_Object = MibScalar
measSwitchIsupFailCallItutCalledPartyLineBusy = _MeasSwitchIsupFailCallItutCalledPartyLineBusy_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 2, 8),
    _MeasSwitchIsupFailCallItutCalledPartyLineBusy_Type()
)
measSwitchIsupFailCallItutCalledPartyLineBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupFailCallItutCalledPartyLineBusy.setStatus("mandatory")
_MeasSwitchIsupFailCallItutIneffectiveMachineAttempts_Type = Counter32
_MeasSwitchIsupFailCallItutIneffectiveMachineAttempts_Object = MibScalar
measSwitchIsupFailCallItutIneffectiveMachineAttempts = _MeasSwitchIsupFailCallItutIneffectiveMachineAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 2, 9),
    _MeasSwitchIsupFailCallItutIneffectiveMachineAttempts_Type()
)
measSwitchIsupFailCallItutIneffectiveMachineAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchIsupFailCallItutIneffectiveMachineAttempts.setStatus("mandatory")
_MeasSwitchPriGrp_ObjectIdentity = ObjectIdentity
measSwitchPriGrp = _MeasSwitchPriGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 3)
)
_MeasSwitchPriDataSuspect_Type = Counter32
_MeasSwitchPriDataSuspect_Object = MibScalar
measSwitchPriDataSuspect = _MeasSwitchPriDataSuspect_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 3, 1),
    _MeasSwitchPriDataSuspect_Type()
)
measSwitchPriDataSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchPriDataSuspect.setStatus("mandatory")
_MeasSwitchPriIncomingIsdnPRICallAttempts_Type = Counter32
_MeasSwitchPriIncomingIsdnPRICallAttempts_Object = MibScalar
measSwitchPriIncomingIsdnPRICallAttempts = _MeasSwitchPriIncomingIsdnPRICallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 3, 2),
    _MeasSwitchPriIncomingIsdnPRICallAttempts_Type()
)
measSwitchPriIncomingIsdnPRICallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchPriIncomingIsdnPRICallAttempts.setStatus("mandatory")
_MeasSwitchPriIncomingIsdnPRICallAnswered_Type = Counter32
_MeasSwitchPriIncomingIsdnPRICallAnswered_Object = MibScalar
measSwitchPriIncomingIsdnPRICallAnswered = _MeasSwitchPriIncomingIsdnPRICallAnswered_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 3, 3),
    _MeasSwitchPriIncomingIsdnPRICallAnswered_Type()
)
measSwitchPriIncomingIsdnPRICallAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchPriIncomingIsdnPRICallAnswered.setStatus("mandatory")
_MeasSwitchPriFailCallGrp_ObjectIdentity = ObjectIdentity
measSwitchPriFailCallGrp = _MeasSwitchPriFailCallGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 4)
)
_MeasSwitchPriFailCallDataSuspect_Type = Counter32
_MeasSwitchPriFailCallDataSuspect_Object = MibScalar
measSwitchPriFailCallDataSuspect = _MeasSwitchPriFailCallDataSuspect_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 4, 1),
    _MeasSwitchPriFailCallDataSuspect_Type()
)
measSwitchPriFailCallDataSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchPriFailCallDataSuspect.setStatus("mandatory")
_MeasSwitchPriFailCallMatchingLoss_Type = Counter32
_MeasSwitchPriFailCallMatchingLoss_Object = MibScalar
measSwitchPriFailCallMatchingLoss = _MeasSwitchPriFailCallMatchingLoss_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 4, 2),
    _MeasSwitchPriFailCallMatchingLoss_Type()
)
measSwitchPriFailCallMatchingLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchPriFailCallMatchingLoss.setStatus("mandatory")
_MeasSwitchPriFailCallNoCircuit_Type = Counter32
_MeasSwitchPriFailCallNoCircuit_Object = MibScalar
measSwitchPriFailCallNoCircuit = _MeasSwitchPriFailCallNoCircuit_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 4, 3),
    _MeasSwitchPriFailCallNoCircuit_Type()
)
measSwitchPriFailCallNoCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchPriFailCallNoCircuit.setStatus("mandatory")
_MeasSwitchPriFailCallCalledPartyLineBusy_Type = Counter32
_MeasSwitchPriFailCallCalledPartyLineBusy_Object = MibScalar
measSwitchPriFailCallCalledPartyLineBusy = _MeasSwitchPriFailCallCalledPartyLineBusy_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 4, 4),
    _MeasSwitchPriFailCallCalledPartyLineBusy_Type()
)
measSwitchPriFailCallCalledPartyLineBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchPriFailCallCalledPartyLineBusy.setStatus("mandatory")
_MeasSwitchPriFailCallIneffectiveMachineAttempts_Type = Counter32
_MeasSwitchPriFailCallIneffectiveMachineAttempts_Object = MibScalar
measSwitchPriFailCallIneffectiveMachineAttempts = _MeasSwitchPriFailCallIneffectiveMachineAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 2, 4, 5),
    _MeasSwitchPriFailCallIneffectiveMachineAttempts_Type()
)
measSwitchPriFailCallIneffectiveMachineAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measSwitchPriFailCallIneffectiveMachineAttempts.setStatus("mandatory")
_MeasTrnkGrp_ObjectIdentity = ObjectIdentity
measTrnkGrp = _MeasTrnkGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 3)
)
_MeasTrnkGrpTrafficTable_Object = MibTable
measTrnkGrpTrafficTable = _MeasTrnkGrpTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    measTrnkGrpTrafficTable.setStatus("mandatory")
_MeasTrnkGrpTrafficEntry_Object = MibTableRow
measTrnkGrpTrafficEntry = _MeasTrnkGrpTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 3, 1, 1)
)
measTrnkGrpTrafficEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "measTrnkGrpName"),
)
if mibBuilder.loadTexts:
    measTrnkGrpTrafficEntry.setStatus("mandatory")
_MeasTrnkGrpName_Type = DisplayString
_MeasTrnkGrpName_Object = MibTableColumn
measTrnkGrpName = _MeasTrnkGrpName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 3, 1, 1, 1),
    _MeasTrnkGrpName_Type()
)
measTrnkGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measTrnkGrpName.setStatus("mandatory")
_MeasTrnkGrpDataSuspect_Type = Integer32
_MeasTrnkGrpDataSuspect_Object = MibTableColumn
measTrnkGrpDataSuspect = _MeasTrnkGrpDataSuspect_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 3, 1, 1, 2),
    _MeasTrnkGrpDataSuspect_Type()
)
measTrnkGrpDataSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measTrnkGrpDataSuspect.setStatus("mandatory")
_MeasTrnkGrpincomingUsage_Type = Integer32
_MeasTrnkGrpincomingUsage_Object = MibTableColumn
measTrnkGrpincomingUsage = _MeasTrnkGrpincomingUsage_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 3, 1, 1, 3),
    _MeasTrnkGrpincomingUsage_Type()
)
measTrnkGrpincomingUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measTrnkGrpincomingUsage.setStatus("mandatory")
_MeasTrnkGrpoutgoingUsage_Type = Integer32
_MeasTrnkGrpoutgoingUsage_Object = MibTableColumn
measTrnkGrpoutgoingUsage = _MeasTrnkGrpoutgoingUsage_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 3, 1, 1, 4),
    _MeasTrnkGrpoutgoingUsage_Type()
)
measTrnkGrpoutgoingUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measTrnkGrpoutgoingUsage.setStatus("mandatory")
_MeasTrnkGrpISCicsChnls_Type = Integer32
_MeasTrnkGrpISCicsChnls_Object = MibTableColumn
measTrnkGrpISCicsChnls = _MeasTrnkGrpISCicsChnls_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 3, 1, 1, 5),
    _MeasTrnkGrpISCicsChnls_Type()
)
measTrnkGrpISCicsChnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measTrnkGrpISCicsChnls.setStatus("mandatory")
_MeasTrnkGrpOOSCicsChnls_Type = Integer32
_MeasTrnkGrpOOSCicsChnls_Object = MibTableColumn
measTrnkGrpOOSCicsChnls = _MeasTrnkGrpOOSCicsChnls_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 3, 1, 1, 6),
    _MeasTrnkGrpOOSCicsChnls_Type()
)
measTrnkGrpOOSCicsChnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measTrnkGrpOOSCicsChnls.setStatus("mandatory")
_MeasTrnkGrptotalUsage_Type = Integer32
_MeasTrnkGrptotalUsage_Object = MibTableColumn
measTrnkGrptotalUsage = _MeasTrnkGrptotalUsage_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 3, 1, 1, 7),
    _MeasTrnkGrptotalUsage_Type()
)
measTrnkGrptotalUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measTrnkGrptotalUsage.setStatus("mandatory")
_MeasTrnkGrpmaintainanceUsage_Type = Integer32
_MeasTrnkGrpmaintainanceUsage_Object = MibTableColumn
measTrnkGrpmaintainanceUsage = _MeasTrnkGrpmaintainanceUsage_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 3, 1, 1, 8),
    _MeasTrnkGrpmaintainanceUsage_Type()
)
measTrnkGrpmaintainanceUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measTrnkGrpmaintainanceUsage.setStatus("mandatory")
_MeasLnk_ObjectIdentity = ObjectIdentity
measLnk = _MeasLnk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 4)
)
_MeasLinkTrafficTable_Object = MibTable
measLinkTrafficTable = _MeasLinkTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    measLinkTrafficTable.setStatus("mandatory")
_MeasLinkTrafficEntry_Object = MibTableRow
measLinkTrafficEntry = _MeasLinkTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 4, 1, 1)
)
measLinkTrafficEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "measLinkName"),
)
if mibBuilder.loadTexts:
    measLinkTrafficEntry.setStatus("mandatory")
_MeasLinkName_Type = NameString
_MeasLinkName_Object = MibTableColumn
measLinkName = _MeasLinkName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 4, 1, 1, 1),
    _MeasLinkName_Type()
)
measLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measLinkName.setStatus("mandatory")
_MeasLinkDataSuspect_Type = Integer32
_MeasLinkDataSuspect_Object = MibTableColumn
measLinkDataSuspect = _MeasLinkDataSuspect_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 4, 1, 1, 2),
    _MeasLinkDataSuspect_Type()
)
measLinkDataSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measLinkDataSuspect.setStatus("mandatory")
_MeasLinkUnavailableDuration_Type = Integer32
_MeasLinkUnavailableDuration_Object = MibTableColumn
measLinkUnavailableDuration = _MeasLinkUnavailableDuration_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 4, 1, 1, 3),
    _MeasLinkUnavailableDuration_Type()
)
measLinkUnavailableDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measLinkUnavailableDuration.setStatus("mandatory")
_MeasLinkInServiceDuration_Type = Integer32
_MeasLinkInServiceDuration_Object = MibTableColumn
measLinkInServiceDuration = _MeasLinkInServiceDuration_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 4, 1, 1, 4),
    _MeasLinkInServiceDuration_Type()
)
measLinkInServiceDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measLinkInServiceDuration.setStatus("mandatory")
_MeasLinkMSUsRetransmitted_Type = Integer32
_MeasLinkMSUsRetransmitted_Object = MibTableColumn
measLinkMSUsRetransmitted = _MeasLinkMSUsRetransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 4, 1, 1, 5),
    _MeasLinkMSUsRetransmitted_Type()
)
measLinkMSUsRetransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measLinkMSUsRetransmitted.setStatus("mandatory")
_MeasLinkOctetsReceived_Type = Integer32
_MeasLinkOctetsReceived_Object = MibTableColumn
measLinkOctetsReceived = _MeasLinkOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 4, 1, 1, 6),
    _MeasLinkOctetsReceived_Type()
)
measLinkOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measLinkOctetsReceived.setStatus("mandatory")
_MeasLinkOctectsTransmitted_Type = Integer32
_MeasLinkOctectsTransmitted_Object = MibTableColumn
measLinkOctectsTransmitted = _MeasLinkOctectsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 4, 1, 1, 7),
    _MeasLinkOctectsTransmitted_Type()
)
measLinkOctectsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measLinkOctectsTransmitted.setStatus("mandatory")
_MeasLinkLostMSUsBufferOverflow_Type = Integer32
_MeasLinkLostMSUsBufferOverflow_Object = MibTableColumn
measLinkLostMSUsBufferOverflow = _MeasLinkLostMSUsBufferOverflow_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 4, 1, 1, 8),
    _MeasLinkLostMSUsBufferOverflow_Type()
)
measLinkLostMSUsBufferOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measLinkLostMSUsBufferOverflow.setStatus("mandatory")
_MeasLinkMSUsDiscarded_Type = Integer32
_MeasLinkMSUsDiscarded_Object = MibTableColumn
measLinkMSUsDiscarded = _MeasLinkMSUsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 3, 4, 1, 1, 9),
    _MeasLinkMSUsDiscarded_Type()
)
measLinkMSUsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    measLinkMSUsDiscarded.setStatus("mandatory")
_SwitchCdr_ObjectIdentity = ObjectIdentity
switchCdr = _SwitchCdr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4)
)
_CdrConfig_ObjectIdentity = ObjectIdentity
cdrConfig = _CdrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 1)
)


class _CdrLongDurCallGenTime_Type(Integer32):
    """Custom type cdrLongDurCallGenTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2359),
    )


_CdrLongDurCallGenTime_Type.__name__ = "Integer32"
_CdrLongDurCallGenTime_Object = MibScalar
cdrLongDurCallGenTime = _CdrLongDurCallGenTime_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 1, 1),
    _CdrLongDurCallGenTime_Type()
)
cdrLongDurCallGenTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrLongDurCallGenTime.setStatus("mandatory")
_CdrBafConfig_ObjectIdentity = ObjectIdentity
cdrBafConfig = _CdrBafConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 2)
)
_CdrAppendModule801_Type = Bool
_CdrAppendModule801_Object = MibScalar
cdrAppendModule801 = _CdrAppendModule801_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 2, 1),
    _CdrAppendModule801_Type()
)
cdrAppendModule801.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrAppendModule801.setStatus("mandatory")


class _CdrSensorId_Type(Integer32):
    """Custom type cdrSensorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999998),
    )


_CdrSensorId_Type.__name__ = "Integer32"
_CdrSensorId_Object = MibScalar
cdrSensorId = _CdrSensorId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 2, 2),
    _CdrSensorId_Type()
)
cdrSensorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrSensorId.setStatus("mandatory")


class _CdrRecordingOfficeId_Type(Integer32):
    """Custom type cdrRecordingOfficeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999998),
    )


_CdrRecordingOfficeId_Type.__name__ = "Integer32"
_CdrRecordingOfficeId_Object = MibScalar
cdrRecordingOfficeId = _CdrRecordingOfficeId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 2, 3),
    _CdrRecordingOfficeId_Type()
)
cdrRecordingOfficeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrRecordingOfficeId.setStatus("mandatory")
_CdrFileConfig_ObjectIdentity = ObjectIdentity
cdrFileConfig = _CdrFileConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 3)
)


class _CdrFileInterval_Type(Integer32):
    """Custom type cdrFileInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_CdrFileInterval_Type.__name__ = "Integer32"
_CdrFileInterval_Object = MibScalar
cdrFileInterval = _CdrFileInterval_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 3, 1),
    _CdrFileInterval_Type()
)
cdrFileInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrFileInterval.setStatus("mandatory")


class _CdrFileRecLimit_Type(Integer32):
    """Custom type cdrFileRecLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_CdrFileRecLimit_Type.__name__ = "Integer32"
_CdrFileRecLimit_Object = MibScalar
cdrFileRecLimit = _CdrFileRecLimit_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 3, 2),
    _CdrFileRecLimit_Type()
)
cdrFileRecLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrFileRecLimit.setStatus("mandatory")


class _CdrFileSourceId_Type(Integer32):
    """Custom type cdrFileSourceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CdrFileSourceId_Type.__name__ = "Integer32"
_CdrFileSourceId_Object = MibScalar
cdrFileSourceId = _CdrFileSourceId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 3, 3),
    _CdrFileSourceId_Type()
)
cdrFileSourceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrFileSourceId.setStatus("mandatory")


class _CdrFileDestinationType_Type(Integer32):
    """Custom type cdrFileDestinationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CdrFileDestinationType_Type.__name__ = "Integer32"
_CdrFileDestinationType_Object = MibScalar
cdrFileDestinationType = _CdrFileDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 3, 4),
    _CdrFileDestinationType_Type()
)
cdrFileDestinationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrFileDestinationType.setStatus("mandatory")


class _CdrFileDestinationId_Type(Integer32):
    """Custom type cdrFileDestinationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CdrFileDestinationId_Type.__name__ = "Integer32"
_CdrFileDestinationId_Object = MibScalar
cdrFileDestinationId = _CdrFileDestinationId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 3, 5),
    _CdrFileDestinationId_Type()
)
cdrFileDestinationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrFileDestinationId.setStatus("mandatory")
_CdrFileInfo_ObjectIdentity = ObjectIdentity
cdrFileInfo = _CdrFileInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 4)
)
_CdrFileQuery_Type = Integer32
_CdrFileQuery_Object = MibScalar
cdrFileQuery = _CdrFileQuery_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 4, 1),
    _CdrFileQuery_Type()
)
cdrFileQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrFileQuery.setStatus("mandatory")


class _CdrFileName_Type(DisplayString):
    """Custom type cdrFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_CdrFileName_Type.__name__ = "DisplayString"
_CdrFileName_Object = MibScalar
cdrFileName = _CdrFileName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 4, 2),
    _CdrFileName_Type()
)
cdrFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrFileName.setStatus("mandatory")
_CdrFileStatus_Type = Integer32
_CdrFileStatus_Object = MibScalar
cdrFileStatus = _CdrFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 4, 3),
    _CdrFileStatus_Type()
)
cdrFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrFileStatus.setStatus("mandatory")


class _CdrFileCreateDate_Type(DisplayString):
    """Custom type cdrFileCreateDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CdrFileCreateDate_Type.__name__ = "DisplayString"
_CdrFileCreateDate_Object = MibScalar
cdrFileCreateDate = _CdrFileCreateDate_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 4, 4),
    _CdrFileCreateDate_Type()
)
cdrFileCreateDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrFileCreateDate.setStatus("mandatory")


class _CdrFileCreateTime_Type(DisplayString):
    """Custom type cdrFileCreateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CdrFileCreateTime_Type.__name__ = "DisplayString"
_CdrFileCreateTime_Object = MibScalar
cdrFileCreateTime = _CdrFileCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 4, 5),
    _CdrFileCreateTime_Type()
)
cdrFileCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrFileCreateTime.setStatus("mandatory")
_CdrFileRecordNum_Type = Integer32
_CdrFileRecordNum_Object = MibScalar
cdrFileRecordNum = _CdrFileRecordNum_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 4, 6),
    _CdrFileRecordNum_Type()
)
cdrFileRecordNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrFileRecordNum.setStatus("mandatory")


class _CdrFileAcknowledge_Type(DisplayString):
    """Custom type cdrFileAcknowledge based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CdrFileAcknowledge_Type.__name__ = "DisplayString"
_CdrFileAcknowledge_Object = MibScalar
cdrFileAcknowledge = _CdrFileAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 4, 7),
    _CdrFileAcknowledge_Type()
)
cdrFileAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrFileAcknowledge.setStatus("mandatory")
_CdrMgmntCmdGroup_ObjectIdentity = ObjectIdentity
cdrMgmntCmdGroup = _CdrMgmntCmdGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 5)
)
_CdrGenMgmntCmd_Type = EnableOperation
_CdrGenMgmntCmd_Object = MibScalar
cdrGenMgmntCmd = _CdrGenMgmntCmd_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 5, 1),
    _CdrGenMgmntCmd_Type()
)
cdrGenMgmntCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrGenMgmntCmd.setStatus("mandatory")
_CdrMngmtTrnkGrpTable_Object = MibTable
cdrMngmtTrnkGrpTable = _CdrMngmtTrnkGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 5, 2)
)
if mibBuilder.loadTexts:
    cdrMngmtTrnkGrpTable.setStatus("mandatory")
_CdrMngmtTrnkGrpEntry_Object = MibTableRow
cdrMngmtTrnkGrpEntry = _CdrMngmtTrnkGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 5, 2, 1)
)
cdrMngmtTrnkGrpEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "cdrTrnkGrpId"),
)
if mibBuilder.loadTexts:
    cdrMngmtTrnkGrpEntry.setStatus("mandatory")


class _CdrTrnkGrpId_Type(Integer32):
    """Custom type cdrTrnkGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CdrTrnkGrpId_Type.__name__ = "Integer32"
_CdrTrnkGrpId_Object = MibTableColumn
cdrTrnkGrpId = _CdrTrnkGrpId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 5, 2, 1, 1),
    _CdrTrnkGrpId_Type()
)
cdrTrnkGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdrTrnkGrpId.setStatus("mandatory")
_CdrTrnkGrpdirection_Type = CdrFlag
_CdrTrnkGrpdirection_Object = MibTableColumn
cdrTrnkGrpdirection = _CdrTrnkGrpdirection_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 5, 2, 1, 2),
    _CdrTrnkGrpdirection_Type()
)
cdrTrnkGrpdirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrTrnkGrpdirection.setStatus("mandatory")
_CdrTrnkGrpMgmntCmd_Type = EnableOperation
_CdrTrnkGrpMgmntCmd_Object = MibTableColumn
cdrTrnkGrpMgmntCmd = _CdrTrnkGrpMgmntCmd_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 4, 5, 2, 1, 3),
    _CdrTrnkGrpMgmntCmd_Type()
)
cdrTrnkGrpMgmntCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdrTrnkGrpMgmntCmd.setStatus("mandatory")
_SwitchFeature_ObjectIdentity = ObjectIdentity
switchFeature = _SwitchFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5)
)
_ModemFaultDetection_ObjectIdentity = ObjectIdentity
modemFaultDetection = _ModemFaultDetection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 1)
)
_ModemStatusTable_Object = MibTable
modemStatusTable = _ModemStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    modemStatusTable.setStatus("mandatory")
_ModemStatusEntry_Object = MibTableRow
modemStatusEntry = _ModemStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 1, 1, 1)
)
modemStatusEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "faultModemTrnkId"),
    (0, "ARMILLAIRE2000-MIB", "faultModemChnlId"),
)
if mibBuilder.loadTexts:
    modemStatusEntry.setStatus("mandatory")
_FaultModemTrnkId_Type = Integer32
_FaultModemTrnkId_Object = MibTableColumn
faultModemTrnkId = _FaultModemTrnkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 1, 1, 1, 1),
    _FaultModemTrnkId_Type()
)
faultModemTrnkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultModemTrnkId.setStatus("mandatory")
_FaultModemChnlId_Type = Integer32
_FaultModemChnlId_Object = MibTableColumn
faultModemChnlId = _FaultModemChnlId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 1, 1, 1, 2),
    _FaultModemChnlId_Type()
)
faultModemChnlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultModemChnlId.setStatus("mandatory")
_FaultModemRepnum_Type = Integer32
_FaultModemRepnum_Object = MibTableColumn
faultModemRepnum = _FaultModemRepnum_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 1, 1, 1, 3),
    _FaultModemRepnum_Type()
)
faultModemRepnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultModemRepnum.setStatus("mandatory")
_FaultModemReset_Type = ModemResetStatus
_FaultModemReset_Object = MibTableColumn
faultModemReset = _FaultModemReset_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 1, 1, 1, 4),
    _FaultModemReset_Type()
)
faultModemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultModemReset.setStatus("mandatory")
_Lnp_ObjectIdentity = ObjectIdentity
lnp = _Lnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 2)
)
_LrnTable_Object = MibTable
lrnTable = _LrnTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    lrnTable.setStatus("mandatory")
_LrnEntry_Object = MibTableRow
lrnEntry = _LrnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 2, 1, 1)
)
lrnEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "lrnNum"),
)
if mibBuilder.loadTexts:
    lrnEntry.setStatus("mandatory")


class _LrnNum_Type(DisplayString):
    """Custom type lrnNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_LrnNum_Type.__name__ = "DisplayString"
_LrnNum_Object = MibTableColumn
lrnNum = _LrnNum_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 2, 1, 1, 1),
    _LrnNum_Type()
)
lrnNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lrnNum.setStatus("mandatory")
_LrnRowStatus_Type = LrnRowStatus
_LrnRowStatus_Object = MibTableColumn
lrnRowStatus = _LrnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 2, 1, 1, 2),
    _LrnRowStatus_Type()
)
lrnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lrnRowStatus.setStatus("mandatory")
_SwitchDSP_ObjectIdentity = ObjectIdentity
switchDSP = _SwitchDSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 3)
)
_SwitchDSPCfgTable_Object = MibTable
switchDSPCfgTable = _SwitchDSPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 3, 1)
)
if mibBuilder.loadTexts:
    switchDSPCfgTable.setStatus("mandatory")
_SwitchDSPCfgEntry_Object = MibTableRow
switchDSPCfgEntry = _SwitchDSPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 3, 1, 1)
)
switchDSPCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "switchDSPXconnId"),
    (0, "ARMILLAIRE2000-MIB", "switchDSPSlotId"),
)
if mibBuilder.loadTexts:
    switchDSPCfgEntry.setStatus("mandatory")


class _SwitchDSPXconnId_Type(Integer32):
    """Custom type switchDSPXconnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwitchDSPXconnId_Type.__name__ = "Integer32"
_SwitchDSPXconnId_Object = MibTableColumn
switchDSPXconnId = _SwitchDSPXconnId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 3, 1, 1, 1),
    _SwitchDSPXconnId_Type()
)
switchDSPXconnId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchDSPXconnId.setStatus("mandatory")


class _SwitchDSPSlotId_Type(Integer32):
    """Custom type switchDSPSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwitchDSPSlotId_Type.__name__ = "Integer32"
_SwitchDSPSlotId_Object = MibTableColumn
switchDSPSlotId = _SwitchDSPSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 3, 1, 1, 2),
    _SwitchDSPSlotId_Type()
)
switchDSPSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchDSPSlotId.setStatus("mandatory")
_SwitchDSPCardType_Type = DSPCardType
_SwitchDSPCardType_Object = MibTableColumn
switchDSPCardType = _SwitchDSPCardType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 3, 1, 1, 3),
    _SwitchDSPCardType_Type()
)
switchDSPCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchDSPCardType.setStatus("mandatory")
_SwitchDSPCfgRowStatus_Type = RowStatus
_SwitchDSPCfgRowStatus_Object = MibTableColumn
switchDSPCfgRowStatus = _SwitchDSPCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 3, 1, 1, 4),
    _SwitchDSPCfgRowStatus_Type()
)
switchDSPCfgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchDSPCfgRowStatus.setStatus("mandatory")
_SwitchDSPCfgOpStatus_Type = OpStatus
_SwitchDSPCfgOpStatus_Object = MibTableColumn
switchDSPCfgOpStatus = _SwitchDSPCfgOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 3, 1, 1, 5),
    _SwitchDSPCfgOpStatus_Type()
)
switchDSPCfgOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDSPCfgOpStatus.setStatus("mandatory")
_SwitchTGFeature_ObjectIdentity = ObjectIdentity
switchTGFeature = _SwitchTGFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 4)
)
_SwitchFeatureTGCfgTable_Object = MibTable
switchFeatureTGCfgTable = _SwitchFeatureTGCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 4, 1)
)
if mibBuilder.loadTexts:
    switchFeatureTGCfgTable.setStatus("mandatory")
_SwitchTGGrpCfgEntry_Object = MibTableRow
switchTGGrpCfgEntry = _SwitchTGGrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 4, 1, 1)
)
switchTGGrpCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "switchFeatureTGId"),
)
if mibBuilder.loadTexts:
    switchTGGrpCfgEntry.setStatus("mandatory")
_SwitchFeatureTGId_Type = Integer32
_SwitchFeatureTGId_Object = MibTableColumn
switchFeatureTGId = _SwitchFeatureTGId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 4, 1, 1, 1),
    _SwitchFeatureTGId_Type()
)
switchFeatureTGId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchFeatureTGId.setStatus("mandatory")
_SwitchFeatureTGName_Type = NameString
_SwitchFeatureTGName_Object = MibTableColumn
switchFeatureTGName = _SwitchFeatureTGName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 4, 1, 1, 2),
    _SwitchFeatureTGName_Type()
)
switchFeatureTGName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchFeatureTGName.setStatus("mandatory")
_SwitchFeatureTGType_Type = TrnkGrpType
_SwitchFeatureTGType_Object = MibTableColumn
switchFeatureTGType = _SwitchFeatureTGType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 4, 1, 1, 3),
    _SwitchFeatureTGType_Type()
)
switchFeatureTGType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchFeatureTGType.setStatus("mandatory")
_SwitchFeatureTGFeatureEC_Type = TGFeature
_SwitchFeatureTGFeatureEC_Object = MibTableColumn
switchFeatureTGFeatureEC = _SwitchFeatureTGFeatureEC_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 4, 1, 1, 4),
    _SwitchFeatureTGFeatureEC_Type()
)
switchFeatureTGFeatureEC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchFeatureTGFeatureEC.setStatus("mandatory")
_SwitchFeatureTGFeatureCOMPRESS_Type = TGFeature
_SwitchFeatureTGFeatureCOMPRESS_Object = MibTableColumn
switchFeatureTGFeatureCOMPRESS = _SwitchFeatureTGFeatureCOMPRESS_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 4, 1, 1, 5),
    _SwitchFeatureTGFeatureCOMPRESS_Type()
)
switchFeatureTGFeatureCOMPRESS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchFeatureTGFeatureCOMPRESS.setStatus("mandatory")
_SwitchFeatureTGFeatureSS_Type = TGFeature
_SwitchFeatureTGFeatureSS_Object = MibTableColumn
switchFeatureTGFeatureSS = _SwitchFeatureTGFeatureSS_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 4, 1, 1, 6),
    _SwitchFeatureTGFeatureSS_Type()
)
switchFeatureTGFeatureSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchFeatureTGFeatureSS.setStatus("mandatory")
_SwitchFeatureTGFeatureCNIS_Type = TGFeature
_SwitchFeatureTGFeatureCNIS_Object = MibTableColumn
switchFeatureTGFeatureCNIS = _SwitchFeatureTGFeatureCNIS_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 5, 4, 1, 1, 7),
    _SwitchFeatureTGFeatureCNIS_Type()
)
switchFeatureTGFeatureCNIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchFeatureTGFeatureCNIS.setStatus("mandatory")
_SwitchMaintenance_ObjectIdentity = ObjectIdentity
switchMaintenance = _SwitchMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6)
)
_Ft_ObjectIdentity = ObjectIdentity
ft = _Ft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 1)
)
_FtSwitchOverInfo_ObjectIdentity = ObjectIdentity
ftSwitchOverInfo = _FtSwitchOverInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 1, 1)
)
_SwitchOver_Type = FTswitchOver
_SwitchOver_Object = MibScalar
switchOver = _SwitchOver_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 1, 1, 1),
    _SwitchOver_Type()
)
switchOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchOver.setStatus("mandatory")
_Log_ObjectIdentity = ObjectIdentity
log = _Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 2)
)
_LogFileInfo_ObjectIdentity = ObjectIdentity
logFileInfo = _LogFileInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 2, 1)
)


class _LogGenTime_Type(Integer32):
    """Custom type logGenTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_LogGenTime_Type.__name__ = "Integer32"
_LogGenTime_Object = MibScalar
logGenTime = _LogGenTime_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 2, 1, 1),
    _LogGenTime_Type()
)
logGenTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logGenTime.setStatus("mandatory")


class _LogPurgeTime_Type(Integer32):
    """Custom type logPurgeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_LogPurgeTime_Type.__name__ = "Integer32"
_LogPurgeTime_Object = MibScalar
logPurgeTime = _LogPurgeTime_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 2, 1, 2),
    _LogPurgeTime_Type()
)
logPurgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logPurgeTime.setStatus("mandatory")
_LogFileGenEnable_ObjectIdentity = ObjectIdentity
logFileGenEnable = _LogFileGenEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 2, 2)
)
_EnablelogGen_Type = LogFileEnDis
_EnablelogGen_Object = MibScalar
enablelogGen = _EnablelogGen_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 2, 2, 1),
    _EnablelogGen_Type()
)
enablelogGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablelogGen.setStatus("mandatory")
_DisableLogGen_Type = LogFileEnDis
_DisableLogGen_Object = MibScalar
disableLogGen = _DisableLogGen_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 2, 2, 2),
    _DisableLogGen_Type()
)
disableLogGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disableLogGen.setStatus("mandatory")
_LogFileAttribute_ObjectIdentity = ObjectIdentity
logFileAttribute = _LogFileAttribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 2, 3)
)
_LogAttribute_Type = LogFileAttr
_LogAttribute_Object = MibScalar
logAttribute = _LogAttribute_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 2, 3, 1),
    _LogAttribute_Type()
)
logAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logAttribute.setStatus("mandatory")
_LogFileSize_Type = Integer32
_LogFileSize_Object = MibScalar
logFileSize = _LogFileSize_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 2, 3, 2),
    _LogFileSize_Type()
)
logFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFileSize.setStatus("mandatory")
_LogFileDuration_Type = Integer32
_LogFileDuration_Object = MibScalar
logFileDuration = _LogFileDuration_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 2, 3, 3),
    _LogFileDuration_Type()
)
logFileDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFileDuration.setStatus("mandatory")
_LogFileStatus_Type = Integer32
_LogFileStatus_Object = MibScalar
logFileStatus = _LogFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 2, 3, 4),
    _LogFileStatus_Type()
)
logFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFileStatus.setStatus("mandatory")
_Trace_ObjectIdentity = ObjectIdentity
trace = _Trace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3)
)
_Ss7LnkTrace_ObjectIdentity = ObjectIdentity
ss7LnkTrace = _Ss7LnkTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 1)
)
_Ss7LnkTraceTable_Object = MibTable
ss7LnkTraceTable = _Ss7LnkTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ss7LnkTraceTable.setStatus("mandatory")
_Ss7LnkTraceEntry_Object = MibTableRow
ss7LnkTraceEntry = _Ss7LnkTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 1, 1, 1)
)
ss7LnkTraceEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "ss7LnkId"),
)
if mibBuilder.loadTexts:
    ss7LnkTraceEntry.setStatus("mandatory")
_Ss7LnkId_Type = Integer32
_Ss7LnkId_Object = MibTableColumn
ss7LnkId = _Ss7LnkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 1, 1, 1, 1),
    _Ss7LnkId_Type()
)
ss7LnkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7LnkId.setStatus("mandatory")
_Ss7LnkLog_Type = LogType
_Ss7LnkLog_Object = MibTableColumn
ss7LnkLog = _Ss7LnkLog_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 1, 1, 1, 2),
    _Ss7LnkLog_Type()
)
ss7LnkLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7LnkLog.setStatus("mandatory")
_Ss7LnkEnable_Type = EnableTrace
_Ss7LnkEnable_Object = MibTableColumn
ss7LnkEnable = _Ss7LnkEnable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 1, 1, 1, 3),
    _Ss7LnkEnable_Type()
)
ss7LnkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7LnkEnable.setStatus("mandatory")
_Ss7RouteTrace_ObjectIdentity = ObjectIdentity
ss7RouteTrace = _Ss7RouteTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 2)
)
_Ss7RouteTraceTable_Object = MibTable
ss7RouteTraceTable = _Ss7RouteTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ss7RouteTraceTable.setStatus("mandatory")
_Ss7RouteTraceEntry_Object = MibTableRow
ss7RouteTraceEntry = _Ss7RouteTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 2, 1, 1)
)
ss7RouteTraceEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "ss7RouteDpc"),
)
if mibBuilder.loadTexts:
    ss7RouteTraceEntry.setStatus("mandatory")
_Ss7RouteDpc_Type = Integer32
_Ss7RouteDpc_Object = MibTableColumn
ss7RouteDpc = _Ss7RouteDpc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 2, 1, 1, 1),
    _Ss7RouteDpc_Type()
)
ss7RouteDpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7RouteDpc.setStatus("mandatory")
_Ss7RouteLog_Type = LogType
_Ss7RouteLog_Object = MibTableColumn
ss7RouteLog = _Ss7RouteLog_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 2, 1, 1, 2),
    _Ss7RouteLog_Type()
)
ss7RouteLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ss7RouteLog.setStatus("mandatory")
_Ss7RouteEnable_Type = EnableTrace
_Ss7RouteEnable_Object = MibTableColumn
ss7RouteEnable = _Ss7RouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 2, 1, 1, 3),
    _Ss7RouteEnable_Type()
)
ss7RouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ss7RouteEnable.setStatus("mandatory")
_IsdnTrnkTrace_ObjectIdentity = ObjectIdentity
isdnTrnkTrace = _IsdnTrnkTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 3)
)
_IsdnTrunkTraceTable_Object = MibTable
isdnTrunkTraceTable = _IsdnTrunkTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 3, 1)
)
if mibBuilder.loadTexts:
    isdnTrunkTraceTable.setStatus("mandatory")
_IsdnTrunkTraceEntry_Object = MibTableRow
isdnTrunkTraceEntry = _IsdnTrunkTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 3, 1, 1)
)
isdnTrunkTraceEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "isdnTrnkId"),
)
if mibBuilder.loadTexts:
    isdnTrunkTraceEntry.setStatus("mandatory")
_IsdnTrnkId_Type = Integer32
_IsdnTrnkId_Object = MibTableColumn
isdnTrnkId = _IsdnTrnkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 3, 1, 1, 1),
    _IsdnTrnkId_Type()
)
isdnTrnkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnTrnkId.setStatus("mandatory")
_IsdnTrunkLog_Type = LogType
_IsdnTrunkLog_Object = MibTableColumn
isdnTrunkLog = _IsdnTrunkLog_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 3, 1, 1, 2),
    _IsdnTrunkLog_Type()
)
isdnTrunkLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdnTrunkLog.setStatus("mandatory")
_IsdnTrunkEnable_Type = EnableTrace
_IsdnTrunkEnable_Object = MibTableColumn
isdnTrunkEnable = _IsdnTrunkEnable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 3, 3, 1, 1, 3),
    _IsdnTrunkEnable_Type()
)
isdnTrunkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isdnTrunkEnable.setStatus("mandatory")
_ProcessStatus_ObjectIdentity = ObjectIdentity
processStatus = _ProcessStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 4)
)
_ProcessStatusInfo_ObjectIdentity = ObjectIdentity
processStatusInfo = _ProcessStatusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 4, 1)
)
_StatusLM1ProcId_Type = ProcessStatus
_StatusLM1ProcId_Object = MibScalar
statusLM1ProcId = _StatusLM1ProcId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 4, 1, 1),
    _StatusLM1ProcId_Type()
)
statusLM1ProcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusLM1ProcId.setStatus("mandatory")
_StatusLM2ProcID_Type = ProcessStatus
_StatusLM2ProcID_Object = MibScalar
statusLM2ProcID = _StatusLM2ProcID_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 4, 1, 2),
    _StatusLM2ProcID_Type()
)
statusLM2ProcID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusLM2ProcID.setStatus("mandatory")
_StatusICC1ProcId_Type = ProcessStatus
_StatusICC1ProcId_Object = MibScalar
statusICC1ProcId = _StatusICC1ProcId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 4, 1, 3),
    _StatusICC1ProcId_Type()
)
statusICC1ProcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusICC1ProcId.setStatus("mandatory")
_StatusICC2ProcId_Type = ProcessStatus
_StatusICC2ProcId_Object = MibScalar
statusICC2ProcId = _StatusICC2ProcId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 4, 1, 4),
    _StatusICC2ProcId_Type()
)
statusICC2ProcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusICC2ProcId.setStatus("mandatory")
_StatusISDN1ProcId_Type = ProcessStatus
_StatusISDN1ProcId_Object = MibScalar
statusISDN1ProcId = _StatusISDN1ProcId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 4, 1, 5),
    _StatusISDN1ProcId_Type()
)
statusISDN1ProcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusISDN1ProcId.setStatus("mandatory")
_StatusISDN2ProcId_Type = ProcessStatus
_StatusISDN2ProcId_Object = MibScalar
statusISDN2ProcId = _StatusISDN2ProcId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 4, 1, 6),
    _StatusISDN2ProcId_Type()
)
statusISDN2ProcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusISDN2ProcId.setStatus("mandatory")
_StatusSPHR1ProcId_Type = ProcessStatus
_StatusSPHR1ProcId_Object = MibScalar
statusSPHR1ProcId = _StatusSPHR1ProcId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 4, 1, 7),
    _StatusSPHR1ProcId_Type()
)
statusSPHR1ProcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSPHR1ProcId.setStatus("mandatory")
_StatusSPHR2ProcId_Type = ProcessStatus
_StatusSPHR2ProcId_Object = MibScalar
statusSPHR2ProcId = _StatusSPHR2ProcId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 4, 1, 8),
    _StatusSPHR2ProcId_Type()
)
statusSPHR2ProcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSPHR2ProcId.setStatus("mandatory")
_StatusSIG1ProcId_Type = ProcessStatus
_StatusSIG1ProcId_Object = MibScalar
statusSIG1ProcId = _StatusSIG1ProcId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 4, 1, 9),
    _StatusSIG1ProcId_Type()
)
statusSIG1ProcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSIG1ProcId.setStatus("mandatory")
_StatusSIG2ProcId_Type = ProcessStatus
_StatusSIG2ProcId_Object = MibScalar
statusSIG2ProcId = _StatusSIG2ProcId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 4, 1, 10),
    _StatusSIG2ProcId_Type()
)
statusSIG2ProcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSIG2ProcId.setStatus("mandatory")
_StatusMTP21ProcId_Type = ProcessStatus
_StatusMTP21ProcId_Object = MibScalar
statusMTP21ProcId = _StatusMTP21ProcId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 4, 1, 11),
    _StatusMTP21ProcId_Type()
)
statusMTP21ProcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMTP21ProcId.setStatus("mandatory")
_StatusMTP22ProcId_Type = ProcessStatus
_StatusMTP22ProcId_Object = MibScalar
statusMTP22ProcId = _StatusMTP22ProcId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 4, 1, 12),
    _StatusMTP22ProcId_Type()
)
statusMTP22ProcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMTP22ProcId.setStatus("mandatory")
_StatusMTP23ProcId_Type = ProcessStatus
_StatusMTP23ProcId_Object = MibScalar
statusMTP23ProcId = _StatusMTP23ProcId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 4, 1, 13),
    _StatusMTP23ProcId_Type()
)
statusMTP23ProcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMTP23ProcId.setStatus("mandatory")
_StatusMTP24ProcId_Type = ProcessStatus
_StatusMTP24ProcId_Object = MibScalar
statusMTP24ProcId = _StatusMTP24ProcId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 4, 1, 14),
    _StatusMTP24ProcId_Type()
)
statusMTP24ProcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusMTP24ProcId.setStatus("mandatory")
_EthernetConnStatusInfo_ObjectIdentity = ObjectIdentity
ethernetConnStatusInfo = _EthernetConnStatusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 5)
)
_EthernetConnStatus_Type = EthernetConnStatus
_EthernetConnStatus_Object = MibScalar
ethernetConnStatus = _EthernetConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 5, 1),
    _EthernetConnStatus_Type()
)
ethernetConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetConnStatus.setStatus("mandatory")
_Audit_ObjectIdentity = ObjectIdentity
audit = _Audit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 6)
)
_AuditInfo_ObjectIdentity = ObjectIdentity
auditInfo = _AuditInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 6, 1)
)
_AuditISDNTrnkTable_Object = MibTable
auditISDNTrnkTable = _AuditISDNTrnkTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 6, 1, 1)
)
if mibBuilder.loadTexts:
    auditISDNTrnkTable.setStatus("mandatory")
_AuditISDNTrnkCfgEntry_Object = MibTableRow
auditISDNTrnkCfgEntry = _AuditISDNTrnkCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 6, 1, 1, 1)
)
auditISDNTrnkCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "auditTrnkId"),
)
if mibBuilder.loadTexts:
    auditISDNTrnkCfgEntry.setStatus("mandatory")
_AuditTrnkId_Type = Integer32
_AuditTrnkId_Object = MibTableColumn
auditTrnkId = _AuditTrnkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 6, 1, 1, 1, 1),
    _AuditTrnkId_Type()
)
auditTrnkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditTrnkId.setStatus("mandatory")
_AuditISDNTrnk_Type = AuditOperation
_AuditISDNTrnk_Object = MibTableColumn
auditISDNTrnk = _AuditISDNTrnk_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 6, 1, 1, 1, 2),
    _AuditISDNTrnk_Type()
)
auditISDNTrnk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditISDNTrnk.setStatus("mandatory")
_AuditXLink_Type = AuditOperation
_AuditXLink_Object = MibScalar
auditXLink = _AuditXLink_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 6, 1, 2),
    _AuditXLink_Type()
)
auditXLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditXLink.setStatus("mandatory")
_AuditDPCTable_Object = MibTable
auditDPCTable = _AuditDPCTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 6, 1, 3)
)
if mibBuilder.loadTexts:
    auditDPCTable.setStatus("mandatory")
_AuditDPCCfgEntry_Object = MibTableRow
auditDPCCfgEntry = _AuditDPCCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 6, 1, 3, 1)
)
auditDPCCfgEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "auditPointCode"),
)
if mibBuilder.loadTexts:
    auditDPCCfgEntry.setStatus("mandatory")
_AuditPointCode_Type = Integer32
_AuditPointCode_Object = MibTableColumn
auditPointCode = _AuditPointCode_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 6, 1, 3, 1, 1),
    _AuditPointCode_Type()
)
auditPointCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditPointCode.setStatus("mandatory")
_AuditPointCodeType_Type = AuditType
_AuditPointCodeType_Object = MibTableColumn
auditPointCodeType = _AuditPointCodeType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 6, 1, 3, 1, 2),
    _AuditPointCodeType_Type()
)
auditPointCodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditPointCodeType.setStatus("mandatory")
_AuditDPC_Type = AuditOperation
_AuditDPC_Object = MibTableColumn
auditDPC = _AuditDPC_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 6, 1, 3, 1, 3),
    _AuditDPC_Type()
)
auditDPC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditDPC.setStatus("mandatory")
_AuditPeriodGrp_ObjectIdentity = ObjectIdentity
auditPeriodGrp = _AuditPeriodGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 6, 1, 4)
)


class _AuditTimePeriod_Type(Integer32):
    """Custom type auditTimePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AuditTimePeriod_Type.__name__ = "Integer32"
_AuditTimePeriod_Object = MibScalar
auditTimePeriod = _AuditTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 6, 1, 4, 1),
    _AuditTimePeriod_Type()
)
auditTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditTimePeriod.setStatus("mandatory")
_AuditPeriod_Type = AuditOperation
_AuditPeriod_Object = MibScalar
auditPeriod = _AuditPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 6, 6, 1, 4, 2),
    _AuditPeriod_Type()
)
auditPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditPeriod.setStatus("mandatory")
_SwitchTrap_ObjectIdentity = ObjectIdentity
switchTrap = _SwitchTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7)
)
_TrapObjects_ObjectIdentity = ObjectIdentity
trapObjects = _TrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1)
)


class _TrapOpc_Type(Integer32):
    """Custom type trapOpc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_TrapOpc_Type.__name__ = "Integer32"
_TrapOpc_Object = MibScalar
trapOpc = _TrapOpc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 1),
    _TrapOpc_Type()
)
trapOpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapOpc.setStatus("mandatory")
_TrapXconnectId_Type = Integer32
_TrapXconnectId_Object = MibScalar
trapXconnectId = _TrapXconnectId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 2),
    _TrapXconnectId_Type()
)
trapXconnectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapXconnectId.setStatus("mandatory")
_TrapLinkId_Type = Integer32
_TrapLinkId_Object = MibScalar
trapLinkId = _TrapLinkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 3),
    _TrapLinkId_Type()
)
trapLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLinkId.setStatus("mandatory")
_TrapSlotId_Type = Integer32
_TrapSlotId_Object = MibScalar
trapSlotId = _TrapSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 4),
    _TrapSlotId_Type()
)
trapSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSlotId.setStatus("mandatory")
_TrapPortId_Type = Integer32
_TrapPortId_Object = MibScalar
trapPortId = _TrapPortId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 5),
    _TrapPortId_Type()
)
trapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPortId.setStatus("mandatory")
_TrapTrunkId_Type = Integer32
_TrapTrunkId_Object = MibScalar
trapTrunkId = _TrapTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 6),
    _TrapTrunkId_Type()
)
trapTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTrunkId.setStatus("mandatory")
_TrapInterfaceId_Type = Integer32
_TrapInterfaceId_Object = MibScalar
trapInterfaceId = _TrapInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 7),
    _TrapInterfaceId_Type()
)
trapInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapInterfaceId.setStatus("mandatory")
_TrapChnlId_Type = Integer32
_TrapChnlId_Object = MibScalar
trapChnlId = _TrapChnlId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 8),
    _TrapChnlId_Type()
)
trapChnlId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapChnlId.setStatus("mandatory")
_TrapDbId_Type = Integer32
_TrapDbId_Object = MibScalar
trapDbId = _TrapDbId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 9),
    _TrapDbId_Type()
)
trapDbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDbId.setStatus("mandatory")
_TrapLinkName_Type = NameString
_TrapLinkName_Object = MibScalar
trapLinkName = _TrapLinkName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 10),
    _TrapLinkName_Type()
)
trapLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLinkName.setStatus("mandatory")
_TrapSwitchName_Type = DisplayString
_TrapSwitchName_Object = MibScalar
trapSwitchName = _TrapSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 11),
    _TrapSwitchName_Type()
)
trapSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSwitchName.setStatus("mandatory")
_TrapCicvalue_Type = Integer32
_TrapCicvalue_Object = MibScalar
trapCicvalue = _TrapCicvalue_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 12),
    _TrapCicvalue_Type()
)
trapCicvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCicvalue.setStatus("mandatory")
_TrapCicrange_Type = Integer32
_TrapCicrange_Object = MibScalar
trapCicrange = _TrapCicrange_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 13),
    _TrapCicrange_Type()
)
trapCicrange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCicrange.setStatus("mandatory")


class _TrapCause_Type(DisplayString):
    """Custom type trapCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 33),
    )


_TrapCause_Type.__name__ = "DisplayString"
_TrapCause_Object = MibScalar
trapCause = _TrapCause_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 14),
    _TrapCause_Type()
)
trapCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCause.setStatus("mandatory")


class _TrapDpc_Type(Integer32):
    """Custom type trapDpc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_TrapDpc_Type.__name__ = "Integer32"
_TrapDpc_Object = MibScalar
trapDpc = _TrapDpc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 15),
    _TrapDpc_Type()
)
trapDpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDpc.setStatus("mandatory")
_TrapCdrFileSeqNum_Type = Integer32
_TrapCdrFileSeqNum_Object = MibScalar
trapCdrFileSeqNum = _TrapCdrFileSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 16),
    _TrapCdrFileSeqNum_Type()
)
trapCdrFileSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCdrFileSeqNum.setStatus("mandatory")


class _TrapCdrFileName_Type(DisplayString):
    """Custom type trapCdrFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TrapCdrFileName_Type.__name__ = "DisplayString"
_TrapCdrFileName_Object = MibScalar
trapCdrFileName = _TrapCdrFileName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 17),
    _TrapCdrFileName_Type()
)
trapCdrFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCdrFileName.setStatus("mandatory")
_TrapMeasErrCause_Type = Integer32
_TrapMeasErrCause_Object = MibScalar
trapMeasErrCause = _TrapMeasErrCause_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 18),
    _TrapMeasErrCause_Type()
)
trapMeasErrCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapMeasErrCause.setStatus("mandatory")
_TrapMeasErrNum_Type = Integer32
_TrapMeasErrNum_Object = MibScalar
trapMeasErrNum = _TrapMeasErrNum_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 19),
    _TrapMeasErrNum_Type()
)
trapMeasErrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapMeasErrNum.setStatus("mandatory")
_TrapRepeatNum_Type = Integer32
_TrapRepeatNum_Object = MibScalar
trapRepeatNum = _TrapRepeatNum_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 20),
    _TrapRepeatNum_Type()
)
trapRepeatNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapRepeatNum.setStatus("mandatory")
_TrapSeverity_Type = DisplayString
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 21),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("mandatory")
_TrapProcessId_Type = Integer32
_TrapProcessId_Object = MibScalar
trapProcessId = _TrapProcessId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 22),
    _TrapProcessId_Type()
)
trapProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapProcessId.setStatus("mandatory")
_TrapBucketSize_Type = Integer32
_TrapBucketSize_Object = MibScalar
trapBucketSize = _TrapBucketSize_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 23),
    _TrapBucketSize_Type()
)
trapBucketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapBucketSize.setStatus("mandatory")
_TrapNode1Id_Type = Integer32
_TrapNode1Id_Object = MibScalar
trapNode1Id = _TrapNode1Id_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 24),
    _TrapNode1Id_Type()
)
trapNode1Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNode1Id.setStatus("mandatory")
_TrapNode2Id_Type = Integer32
_TrapNode2Id_Object = MibScalar
trapNode2Id = _TrapNode2Id_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 25),
    _TrapNode2Id_Type()
)
trapNode2Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapNode2Id.setStatus("mandatory")
_TrapRoutename_Type = DisplayString
_TrapRoutename_Object = MibScalar
trapRoutename = _TrapRoutename_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 26),
    _TrapRoutename_Type()
)
trapRoutename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapRoutename.setStatus("mandatory")


class _TrapMeasFileName_Type(DisplayString):
    """Custom type trapMeasFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TrapMeasFileName_Type.__name__ = "DisplayString"
_TrapMeasFileName_Object = MibScalar
trapMeasFileName = _TrapMeasFileName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 27),
    _TrapMeasFileName_Type()
)
trapMeasFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapMeasFileName.setStatus("mandatory")
_TrapDirectory_Type = DisplayString
_TrapDirectory_Object = MibScalar
trapDirectory = _TrapDirectory_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 28),
    _TrapDirectory_Type()
)
trapDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDirectory.setStatus("mandatory")
_TrapProcessorId_Type = Integer32
_TrapProcessorId_Object = MibScalar
trapProcessorId = _TrapProcessorId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 29),
    _TrapProcessorId_Type()
)
trapProcessorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapProcessorId.setStatus("mandatory")


class _TrapLogFileName_Type(DisplayString):
    """Custom type trapLogFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TrapLogFileName_Type.__name__ = "DisplayString"
_TrapLogFileName_Object = MibScalar
trapLogFileName = _TrapLogFileName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 30),
    _TrapLogFileName_Type()
)
trapLogFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogFileName.setStatus("mandatory")


class _TrapLogErrcause_Type(DisplayString):
    """Custom type trapLogErrcause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TrapLogErrcause_Type.__name__ = "DisplayString"
_TrapLogErrcause_Object = MibScalar
trapLogErrcause = _TrapLogErrcause_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 31),
    _TrapLogErrcause_Type()
)
trapLogErrcause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogErrcause.setStatus("mandatory")
_TrapLogErrNo_Type = Integer32
_TrapLogErrNo_Object = MibScalar
trapLogErrNo = _TrapLogErrNo_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 32),
    _TrapLogErrNo_Type()
)
trapLogErrNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLogErrNo.setStatus("mandatory")
_TrapPsuNo_Type = Integer32
_TrapPsuNo_Object = MibScalar
trapPsuNo = _TrapPsuNo_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 33),
    _TrapPsuNo_Type()
)
trapPsuNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPsuNo.setStatus("mandatory")
_TrapIntId_Type = Integer32
_TrapIntId_Object = MibScalar
trapIntId = _TrapIntId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 34),
    _TrapIntId_Type()
)
trapIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIntId.setStatus("mandatory")
_TrapIntfcId_Type = Integer32
_TrapIntfcId_Object = MibScalar
trapIntfcId = _TrapIntfcId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 35),
    _TrapIntfcId_Type()
)
trapIntfcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIntfcId.setStatus("mandatory")
_TrapLanId_Type = Integer32
_TrapLanId_Object = MibScalar
trapLanId = _TrapLanId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 36),
    _TrapLanId_Type()
)
trapLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapLanId.setStatus("mandatory")
_TrapnumXlinks_Type = Integer32
_TrapnumXlinks_Object = MibScalar
trapnumXlinks = _TrapnumXlinks_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 37),
    _TrapnumXlinks_Type()
)
trapnumXlinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapnumXlinks.setStatus("mandatory")
_TrapSwitchId1_Type = Integer32
_TrapSwitchId1_Object = MibScalar
trapSwitchId1 = _TrapSwitchId1_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 38),
    _TrapSwitchId1_Type()
)
trapSwitchId1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSwitchId1.setStatus("mandatory")
_TrapSwitchId2_Type = Integer32
_TrapSwitchId2_Object = MibScalar
trapSwitchId2 = _TrapSwitchId2_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 39),
    _TrapSwitchId2_Type()
)
trapSwitchId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSwitchId2.setStatus("mandatory")
_TrapProcInstNo_Type = Integer32
_TrapProcInstNo_Object = MibScalar
trapProcInstNo = _TrapProcInstNo_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 40),
    _TrapProcInstNo_Type()
)
trapProcInstNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapProcInstNo.setStatus("mandatory")


class _TrapProcName_Type(DisplayString):
    """Custom type trapProcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TrapProcName_Type.__name__ = "DisplayString"
_TrapProcName_Object = MibScalar
trapProcName = _TrapProcName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 41),
    _TrapProcName_Type()
)
trapProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapProcName.setStatus("mandatory")
_TrapFanNo_Type = Integer32
_TrapFanNo_Object = MibScalar
trapFanNo = _TrapFanNo_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 42),
    _TrapFanNo_Type()
)
trapFanNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapFanNo.setStatus("mandatory")
_TrapUserName_Type = NameString
_TrapUserName_Object = MibScalar
trapUserName = _TrapUserName_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 43),
    _TrapUserName_Type()
)
trapUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapUserName.setStatus("mandatory")


class _TrapBitMapStatus_Type(DisplayString):
    """Custom type trapBitMapStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 33),
    )


_TrapBitMapStatus_Type.__name__ = "DisplayString"
_TrapBitMapStatus_Object = MibScalar
trapBitMapStatus = _TrapBitMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 1, 44),
    _TrapBitMapStatus_Type()
)
trapBitMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapBitMapStatus.setStatus("mandatory")
_AlarmGrp_ObjectIdentity = ObjectIdentity
alarmGrp = _AlarmGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2)
)
_AlarmTraps_ObjectIdentity = ObjectIdentity
alarmTraps = _AlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1)
)
_SwitchActiveAlarmTable_Object = MibTable
switchActiveAlarmTable = _SwitchActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 2)
)
if mibBuilder.loadTexts:
    switchActiveAlarmTable.setStatus("mandatory")
_SwitchActiveAlarmEntry_Object = MibTableRow
switchActiveAlarmEntry = _SwitchActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 2, 1)
)
switchActiveAlarmEntry.setIndexNames(
    (0, "ARMILLAIRE2000-MIB", "switchAlarmMsgId"),
    (0, "ARMILLAIRE2000-MIB", "switchAlarmInstNo"),
)
if mibBuilder.loadTexts:
    switchActiveAlarmEntry.setStatus("mandatory")


class _SwitchAlarmMsgId_Type(Integer32):
    """Custom type switchAlarmMsgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwitchAlarmMsgId_Type.__name__ = "Integer32"
_SwitchAlarmMsgId_Object = MibTableColumn
switchAlarmMsgId = _SwitchAlarmMsgId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 2, 1, 1),
    _SwitchAlarmMsgId_Type()
)
switchAlarmMsgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchAlarmMsgId.setStatus("mandatory")


class _SwitchAlarmInstNo_Type(Integer32):
    """Custom type switchAlarmInstNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwitchAlarmInstNo_Type.__name__ = "Integer32"
_SwitchAlarmInstNo_Object = MibTableColumn
switchAlarmInstNo = _SwitchAlarmInstNo_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 2, 1, 2),
    _SwitchAlarmInstNo_Type()
)
switchAlarmInstNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchAlarmInstNo.setStatus("mandatory")
_SwitchAlarmTime_Type = DisplayString
_SwitchAlarmTime_Object = MibTableColumn
switchAlarmTime = _SwitchAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 2, 1, 3),
    _SwitchAlarmTime_Type()
)
switchAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchAlarmTime.setStatus("mandatory")
_SwitchAlarmType_Type = EventType
_SwitchAlarmType_Object = MibTableColumn
switchAlarmType = _SwitchAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 2, 1, 4),
    _SwitchAlarmType_Type()
)
switchAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchAlarmType.setStatus("mandatory")
_SwitchAlarmMainEvent_Type = AlarmEvent
_SwitchAlarmMainEvent_Object = MibTableColumn
switchAlarmMainEvent = _SwitchAlarmMainEvent_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 2, 1, 5),
    _SwitchAlarmMainEvent_Type()
)
switchAlarmMainEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchAlarmMainEvent.setStatus("mandatory")
_SwitchAlarmSubEvent_Type = AlarmSubEvent
_SwitchAlarmSubEvent_Object = MibTableColumn
switchAlarmSubEvent = _SwitchAlarmSubEvent_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 2, 1, 6),
    _SwitchAlarmSubEvent_Type()
)
switchAlarmSubEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchAlarmSubEvent.setStatus("mandatory")
_SwitchAlarmId_Type = Integer32
_SwitchAlarmId_Object = MibTableColumn
switchAlarmId = _SwitchAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 2, 1, 7),
    _SwitchAlarmId_Type()
)
switchAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchAlarmId.setStatus("mandatory")
_SwitchAlarmSeverity_Type = AlarmSeverity
_SwitchAlarmSeverity_Object = MibTableColumn
switchAlarmSeverity = _SwitchAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 2, 1, 8),
    _SwitchAlarmSeverity_Type()
)
switchAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchAlarmSeverity.setStatus("mandatory")
_SwitchAlarmDesc_Type = DisplayString
_SwitchAlarmDesc_Object = MibTableColumn
switchAlarmDesc = _SwitchAlarmDesc_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 2, 1, 9),
    _SwitchAlarmDesc_Type()
)
switchAlarmDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchAlarmDesc.setStatus("mandatory")
_SwitchAlarmAck_Type = ActiveAlarmAckStatus
_SwitchAlarmAck_Object = MibTableColumn
switchAlarmAck = _SwitchAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 2, 1, 10),
    _SwitchAlarmAck_Type()
)
switchAlarmAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchAlarmAck.setStatus("mandatory")


class _SwitchAlarmRepeatTime_Type(Integer32):
    """Custom type switchAlarmRepeatTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SwitchAlarmRepeatTime_Type.__name__ = "Integer32"
_SwitchAlarmRepeatTime_Object = MibTableColumn
switchAlarmRepeatTime = _SwitchAlarmRepeatTime_Object(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 2, 1, 11),
    _SwitchAlarmRepeatTime_Type()
)
switchAlarmRepeatTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchAlarmRepeatTime.setStatus("mandatory")
_Services_ObjectIdentity = ObjectIdentity
services = _Services_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4618, 2)
)

# Managed Objects groups


# Notification objects

genswitchSnmpAgentReadyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 1)
)
genswitchSnmpAgentReadyNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"))
)
if mibBuilder.loadTexts:
    genswitchSnmpAgentReadyNotify.setStatus(
        ""
    )

genConsoleLoginNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 2)
)
genConsoleLoginNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapUserName"))
)
if mibBuilder.loadTexts:
    genConsoleLoginNotify.setStatus(
        ""
    )

genConsoleLogoutNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 3)
)
genConsoleLogoutNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapUserName"))
)
if mibBuilder.loadTexts:
    genConsoleLogoutNotify.setStatus(
        ""
    )

genProcessBufOverflowNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 4)
)
genProcessBufOverflowNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapProcName"),
        ("ARMILLAIRE2000-MIB", "trapProcInstNo"),
        ("ARMILLAIRE2000-MIB", "trapBucketSize"))
)
if mibBuilder.loadTexts:
    genProcessBufOverflowNotify.setStatus(
        ""
    )

genProcessBufOverflowRecoverNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 5)
)
genProcessBufOverflowRecoverNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapProcName"),
        ("ARMILLAIRE2000-MIB", "trapProcInstNo"),
        ("ARMILLAIRE2000-MIB", "trapBucketSize"))
)
if mibBuilder.loadTexts:
    genProcessBufOverflowRecoverNotify.setStatus(
        ""
    )

genProcessHeapOverFlowNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 6)
)
genProcessHeapOverFlowNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapProcName"),
        ("ARMILLAIRE2000-MIB", "trapProcInstNo"))
)
if mibBuilder.loadTexts:
    genProcessHeapOverFlowNotify.setStatus(
        ""
    )

genProcessHeapOverFlowRecoverNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 7)
)
genProcessHeapOverFlowRecoverNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapProcName"),
        ("ARMILLAIRE2000-MIB", "trapProcInstNo"))
)
if mibBuilder.loadTexts:
    genProcessHeapOverFlowRecoverNotify.setStatus(
        ""
    )

xconnectUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 8)
)
xconnectUpNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectUpNotify.setStatus(
        ""
    )

xconnectDnNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 9)
)
xconnectDnNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectDnNotify.setStatus(
        ""
    )

xconnectClkClearNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 10)
)
xconnectClkClearNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectClkClearNotify.setStatus(
        ""
    )

xconnectClkFailNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 11)
)
xconnectClkFailNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectClkFailNotify.setStatus(
        ""
    )

xconnectBkplaneRefClkClearNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 12)
)
xconnectBkplaneRefClkClearNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectBkplaneRefClkClearNotify.setStatus(
        ""
    )

xconnectBkplaneRefClkFailNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 13)
)
xconnectBkplaneRefClkFailNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectBkplaneRefClkFailNotify.setStatus(
        ""
    )

xconnectInterfaceInServiceNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 14)
)
xconnectInterfaceInServiceNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectInterfaceInServiceNotify.setStatus(
        ""
    )

xconnectInterfaceOutOfServiceNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 15)
)
xconnectInterfaceOutOfServiceNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectInterfaceOutOfServiceNotify.setStatus(
        ""
    )

xconnectCardInsertionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 16)
)
xconnectCardInsertionNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectCardInsertionNotify.setStatus(
        ""
    )

xconnectCardRemovalNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 17)
)
xconnectCardRemovalNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectCardRemovalNotify.setStatus(
        ""
    )

xconnectIllegalCardTypeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 18)
)
xconnectIllegalCardTypeNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectIllegalCardTypeNotify.setStatus(
        ""
    )

xconnectIntfFarEndLOFNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 19)
)
xconnectIntfFarEndLOFNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectIntfFarEndLOFNotify.setStatus(
        ""
    )

xconnectIntfFarEndAISNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 20)
)
xconnectIntfFarEndAISNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectIntfFarEndAISNotify.setStatus(
        ""
    )

xconnectIntfNearEndLOFNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 21)
)
xconnectIntfNearEndLOFNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectIntfNearEndLOFNotify.setStatus(
        ""
    )

xconnectIntfNearEndLOSNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 22)
)
xconnectIntfNearEndLOSNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectIntfNearEndLOSNotify.setStatus(
        ""
    )

xconnectIntfCreateNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 23)
)
xconnectIntfCreateNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectIntfCreateNotify.setStatus(
        ""
    )

xconnectIntfDeleteNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 24)
)
xconnectIntfDeleteNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectIntfDeleteNotify.setStatus(
        ""
    )

xconnectXlinkAdjConClrNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 25)
)
xconnectXlinkAdjConClrNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapNode1Id"),
        ("ARMILLAIRE2000-MIB", "trapNode2Id"),
        ("ARMILLAIRE2000-MIB", "trapnumXlinks"))
)
if mibBuilder.loadTexts:
    xconnectXlinkAdjConClrNotify.setStatus(
        ""
    )

xconnectXlinkAdjConNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 26)
)
xconnectXlinkAdjConNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapNode1Id"),
        ("ARMILLAIRE2000-MIB", "trapNode2Id"),
        ("ARMILLAIRE2000-MIB", "trapnumXlinks"))
)
if mibBuilder.loadTexts:
    xconnectXlinkAdjConNotify.setStatus(
        ""
    )

xconnectXlinkRouteFailNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 27)
)
xconnectXlinkRouteFailNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapNode1Id"),
        ("ARMILLAIRE2000-MIB", "trapNode2Id"))
)
if mibBuilder.loadTexts:
    xconnectXlinkRouteFailNotify.setStatus(
        ""
    )

xconnectPortUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 28)
)
xconnectPortUpNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectPortUpNotify.setStatus(
        ""
    )

xconnectCPUSwitchOverNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 29)
)
xconnectCPUSwitchOverNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    xconnectCPUSwitchOverNotify.setStatus(
        ""
    )

atmRAINotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 30)
)
atmRAINotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    atmRAINotify.setStatus(
        ""
    )

atmAISNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 31)
)
atmAISNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    atmAISNotify.setStatus(
        ""
    )

atmLOFNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 32)
)
atmLOFNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    atmLOFNotify.setStatus(
        ""
    )

atmLOSNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 33)
)
atmLOSNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"))
)
if mibBuilder.loadTexts:
    atmLOSNotify.setStatus(
        ""
    )

mfdClearNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 34)
)
mfdClearNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapTrunkId"),
        ("ARMILLAIRE2000-MIB", "trapChnlId"))
)
if mibBuilder.loadTexts:
    mfdClearNotify.setStatus(
        ""
    )

mfdDetectionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 35)
)
mfdDetectionNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapRepeatNum"),
        ("ARMILLAIRE2000-MIB", "trapTrunkId"),
        ("ARMILLAIRE2000-MIB", "trapChnlId"))
)
if mibBuilder.loadTexts:
    mfdDetectionNotify.setStatus(
        ""
    )

measFileReadyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 36)
)
measFileReadyNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapMeasFileName"))
)
if mibBuilder.loadTexts:
    measFileReadyNotify.setStatus(
        ""
    )

measDiskOverCrtclThresholdNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 37)
)
measDiskOverCrtclThresholdNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapMeasErrCause"),
        ("ARMILLAIRE2000-MIB", "trapMeasErrNum"))
)
if mibBuilder.loadTexts:
    measDiskOverCrtclThresholdNotify.setStatus(
        ""
    )

measFileMoveNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 38)
)
measFileMoveNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapMeasFileName"))
)
if mibBuilder.loadTexts:
    measFileMoveNotify.setStatus(
        ""
    )

measFileMoveErrNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 39)
)
measFileMoveErrNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapMeasFileName"))
)
if mibBuilder.loadTexts:
    measFileMoveErrNotify.setStatus(
        ""
    )

measFileOpenErrNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 40)
)
measFileOpenErrNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapMeasFileName"))
)
if mibBuilder.loadTexts:
    measFileOpenErrNotify.setStatus(
        ""
    )

measFileDeleteNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 41)
)
measFileDeleteNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapMeasFileName"))
)
if mibBuilder.loadTexts:
    measFileDeleteNotify.setStatus(
        ""
    )

measFileDeleteErrNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 42)
)
measFileDeleteErrNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapMeasFileName"))
)
if mibBuilder.loadTexts:
    measFileDeleteErrNotify.setStatus(
        ""
    )

cdrFileReadyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 43)
)
cdrFileReadyNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapCdrFileName"))
)
if mibBuilder.loadTexts:
    cdrFileReadyNotify.setStatus(
        ""
    )

cdrDiskFullNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 44)
)
cdrDiskFullNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapDirectory"))
)
if mibBuilder.loadTexts:
    cdrDiskFullNotify.setStatus(
        ""
    )

cdrFileOpenErrNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 45)
)
cdrFileOpenErrNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapCdrFileName"))
)
if mibBuilder.loadTexts:
    cdrFileOpenErrNotify.setStatus(
        ""
    )

cdrFileMoveErrNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 46)
)
cdrFileMoveErrNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapCdrFileName"))
)
if mibBuilder.loadTexts:
    cdrFileMoveErrNotify.setStatus(
        ""
    )

cdrDeleteErrNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 47)
)
cdrDeleteErrNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapCdrFileName"))
)
if mibBuilder.loadTexts:
    cdrDeleteErrNotify.setStatus(
        ""
    )

cdrWriteHeaderErrNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 48)
)
cdrWriteHeaderErrNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapCdrFileName"))
)
if mibBuilder.loadTexts:
    cdrWriteHeaderErrNotify.setStatus(
        ""
    )

cdrWriteRecErrNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 49)
)
cdrWriteRecErrNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapCdrFileName"))
)
if mibBuilder.loadTexts:
    cdrWriteRecErrNotify.setStatus(
        ""
    )

cdrErrFileLocErrNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 50)
)
cdrErrFileLocErrNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapCdrFileName"))
)
if mibBuilder.loadTexts:
    cdrErrFileLocErrNotify.setStatus(
        ""
    )

cdrErrTempFileLocErrNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 51)
)
cdrErrTempFileLocErrNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapCdrFileName"))
)
if mibBuilder.loadTexts:
    cdrErrTempFileLocErrNotify.setStatus(
        ""
    )

cdrFileSysErrNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 52)
)
cdrFileSysErrNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapCdrFileName"))
)
if mibBuilder.loadTexts:
    cdrFileSysErrNotify.setStatus(
        ""
    )

cdrFileCloseErrNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 53)
)
cdrFileCloseErrNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapCdrFileName"))
)
if mibBuilder.loadTexts:
    cdrFileCloseErrNotify.setStatus(
        ""
    )

cdrFileDelete5DaysNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 54)
)
cdrFileDelete5DaysNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapCdrFileName"))
)
if mibBuilder.loadTexts:
    cdrFileDelete5DaysNotify.setStatus(
        ""
    )

ss7LinkUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 55)
)
ss7LinkUpNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    ss7LinkUpNotify.setStatus(
        ""
    )

ss7LinkDnNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 56)
)
ss7LinkDnNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    ss7LinkDnNotify.setStatus(
        ""
    )

ss7Mtp2LinkUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 57)
)
ss7Mtp2LinkUpNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    ss7Mtp2LinkUpNotify.setStatus(
        ""
    )

ss7Mtp2LinkDnNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 58)
)
ss7Mtp2LinkDnNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    ss7Mtp2LinkDnNotify.setStatus(
        ""
    )

ss7LinkEnterCongestionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 59)
)
ss7LinkEnterCongestionNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    ss7LinkEnterCongestionNotify.setStatus(
        ""
    )

ss7LinkExitCongestionNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 60)
)
ss7LinkExitCongestionNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    ss7LinkExitCongestionNotify.setStatus(
        ""
    )

ss7InvalidSLCNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 61)
)
ss7InvalidSLCNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapDpc"))
)
if mibBuilder.loadTexts:
    ss7InvalidSLCNotify.setStatus(
        ""
    )

ss7ConcernedDpcPauseNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 62)
)
ss7ConcernedDpcPauseNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapDpc"))
)
if mibBuilder.loadTexts:
    ss7ConcernedDpcPauseNotify.setStatus(
        ""
    )

ss7ConcernedDpcResumeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 63)
)
ss7ConcernedDpcResumeNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapDpc"))
)
if mibBuilder.loadTexts:
    ss7ConcernedDpcResumeNotify.setStatus(
        ""
    )

ss7ConcernedDpcRemUnAvailNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 64)
)
ss7ConcernedDpcRemUnAvailNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapDpc"))
)
if mibBuilder.loadTexts:
    ss7ConcernedDpcRemUnAvailNotify.setStatus(
        ""
    )

ss7LinkRemInhNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 65)
)
ss7LinkRemInhNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    ss7LinkRemInhNotify.setStatus(
        ""
    )

ss7LinkRemUnInhNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 66)
)
ss7LinkRemUnInhNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    ss7LinkRemUnInhNotify.setStatus(
        ""
    )

ss7LinkLocInhNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 67)
)
ss7LinkLocInhNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    ss7LinkLocInhNotify.setStatus(
        ""
    )

ss7LinkLocUnInhNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 68)
)
ss7LinkLocUnInhNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    ss7LinkLocUnInhNotify.setStatus(
        ""
    )

ss7LinkLOPBlkNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 69)
)
ss7LinkLOPBlkNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    ss7LinkLOPBlkNotify.setStatus(
        ""
    )

ss7LinkLPRNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 70)
)
ss7LinkLPRNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    ss7LinkLPRNotify.setStatus(
        ""
    )

ss7LinkRPONotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 71)
)
ss7LinkRPONotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    ss7LinkRPONotify.setStatus(
        ""
    )

ss7LinkRPRNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 72)
)
ss7LinkRPRNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    ss7LinkRPRNotify.setStatus(
        ""
    )

ss7IsupCicLocNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 73)
)
ss7IsupCicLocNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapDpc"),
        ("ARMILLAIRE2000-MIB", "trapCicvalue"),
        ("ARMILLAIRE2000-MIB", "trapCicrange"),
        ("ARMILLAIRE2000-MIB", "trapCause"))
)
if mibBuilder.loadTexts:
    ss7IsupCicLocNotify.setStatus(
        ""
    )

ss7IsupCicRemNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 74)
)
ss7IsupCicRemNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapDpc"),
        ("ARMILLAIRE2000-MIB", "trapCicvalue"),
        ("ARMILLAIRE2000-MIB", "trapCicrange"),
        ("ARMILLAIRE2000-MIB", "trapCause"))
)
if mibBuilder.loadTexts:
    ss7IsupCicRemNotify.setStatus(
        ""
    )

ss7IsupCongLvl1Notify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 75)
)
ss7IsupCongLvl1Notify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapDpc"))
)
if mibBuilder.loadTexts:
    ss7IsupCongLvl1Notify.setStatus(
        ""
    )

ss7IsupCongLvl2Notify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 76)
)
ss7IsupCongLvl2Notify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapDpc"))
)
if mibBuilder.loadTexts:
    ss7IsupCongLvl2Notify.setStatus(
        ""
    )

isdnDChnlUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 77)
)
isdnDChnlUpNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"))
)
if mibBuilder.loadTexts:
    isdnDChnlUpNotify.setStatus(
        ""
    )

isdnDChnlDnNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 78)
)
isdnDChnlDnNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapXconnectId"),
        ("ARMILLAIRE2000-MIB", "trapSlotId"),
        ("ARMILLAIRE2000-MIB", "trapPortId"))
)
if mibBuilder.loadTexts:
    isdnDChnlDnNotify.setStatus(
        ""
    )

logFileReadyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 79)
)
logFileReadyNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLogFileName"))
)
if mibBuilder.loadTexts:
    logFileReadyNotify.setStatus(
        ""
    )

logDiskFull60PercentNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 80)
)
logDiskFull60PercentNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLogErrcause"),
        ("ARMILLAIRE2000-MIB", "trapLogErrNo"))
)
if mibBuilder.loadTexts:
    logDiskFull60PercentNotify.setStatus(
        ""
    )

logDiskFull70PercentNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 81)
)
logDiskFull70PercentNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLogErrcause"),
        ("ARMILLAIRE2000-MIB", "trapLogErrNo"))
)
if mibBuilder.loadTexts:
    logDiskFull70PercentNotify.setStatus(
        ""
    )

logDiskFull80PercentNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 82)
)
logDiskFull80PercentNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLogErrcause"),
        ("ARMILLAIRE2000-MIB", "trapLogErrNo"))
)
if mibBuilder.loadTexts:
    logDiskFull80PercentNotify.setStatus(
        ""
    )

logErrFileOpenNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 83)
)
logErrFileOpenNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLogFileName"))
)
if mibBuilder.loadTexts:
    logErrFileOpenNotify.setStatus(
        ""
    )

logErrFileCloseNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 84)
)
logErrFileCloseNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLogFileName"))
)
if mibBuilder.loadTexts:
    logErrFileCloseNotify.setStatus(
        ""
    )

logErrFileDeleteNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 85)
)
logErrFileDeleteNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLogFileName"))
)
if mibBuilder.loadTexts:
    logErrFileDeleteNotify.setStatus(
        ""
    )

logErrFileWriteNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 86)
)
logErrFileWriteNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLogFileName"))
)
if mibBuilder.loadTexts:
    logErrFileWriteNotify.setStatus(
        ""
    )

msscPriDedicatedLinkUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 87)
)
msscPriDedicatedLinkUpNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    msscPriDedicatedLinkUpNotify.setStatus(
        ""
    )

msscPriDedicatedLinkDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 88)
)
msscPriDedicatedLinkDownNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    msscPriDedicatedLinkDownNotify.setStatus(
        ""
    )

msscSecDedicatedLinkUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 89)
)
msscSecDedicatedLinkUpNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    msscSecDedicatedLinkUpNotify.setStatus(
        ""
    )

msscSecDedicatedLinkDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 90)
)
msscSecDedicatedLinkDownNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLinkId"))
)
if mibBuilder.loadTexts:
    msscSecDedicatedLinkDownNotify.setStatus(
        ""
    )

msscPriPsuUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 91)
)
msscPriPsuUpNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapPsuNo"))
)
if mibBuilder.loadTexts:
    msscPriPsuUpNotify.setStatus(
        ""
    )

msscPriPsuDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 92)
)
msscPriPsuDownNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapPsuNo"))
)
if mibBuilder.loadTexts:
    msscPriPsuDownNotify.setStatus(
        ""
    )

msscBakPsuUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 93)
)
msscBakPsuUpNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapPsuNo"))
)
if mibBuilder.loadTexts:
    msscBakPsuUpNotify.setStatus(
        ""
    )

msscBakPsuDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 94)
)
msscBakPsuDownNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapPsuNo"))
)
if mibBuilder.loadTexts:
    msscBakPsuDownNotify.setStatus(
        ""
    )

msscPriLanPhyIntfUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 95)
)
msscPriLanPhyIntfUpNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLanId"))
)
if mibBuilder.loadTexts:
    msscPriLanPhyIntfUpNotify.setStatus(
        ""
    )

msscPriLanPhyIntfDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 96)
)
msscPriLanPhyIntfDownNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLanId"))
)
if mibBuilder.loadTexts:
    msscPriLanPhyIntfDownNotify.setStatus(
        ""
    )

msscSecLanPhyIntfUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 97)
)
msscSecLanPhyIntfUpNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLanId"))
)
if mibBuilder.loadTexts:
    msscSecLanPhyIntfUpNotify.setStatus(
        ""
    )

msscSecLanPhyIntfDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 98)
)
msscSecLanPhyIntfDownNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLanId"))
)
if mibBuilder.loadTexts:
    msscSecLanPhyIntfDownNotify.setStatus(
        ""
    )

msscPriHostFanUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 99)
)
msscPriHostFanUpNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapFanNo"))
)
if mibBuilder.loadTexts:
    msscPriHostFanUpNotify.setStatus(
        ""
    )

msscPriHostFanDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 100)
)
msscPriHostFanDownNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapFanNo"))
)
if mibBuilder.loadTexts:
    msscPriHostFanDownNotify.setStatus(
        ""
    )

msscBckHostFanUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 101)
)
msscBckHostFanUpNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapFanNo"))
)
if mibBuilder.loadTexts:
    msscBckHostFanUpNotify.setStatus(
        ""
    )

msscBckHostFanDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 102)
)
msscBckHostFanDownNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapFanNo"))
)
if mibBuilder.loadTexts:
    msscBckHostFanDownNotify.setStatus(
        ""
    )

hubPriIntfUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 103)
)
hubPriIntfUpNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLanId"))
)
if mibBuilder.loadTexts:
    hubPriIntfUpNotify.setStatus(
        ""
    )

hubPriIntfDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 104)
)
hubPriIntfDownNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLanId"))
)
if mibBuilder.loadTexts:
    hubPriIntfDownNotify.setStatus(
        ""
    )

hubSecIntfUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 105)
)
hubSecIntfUpNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLanId"))
)
if mibBuilder.loadTexts:
    hubSecIntfUpNotify.setStatus(
        ""
    )

hubSecIntfDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 106)
)
hubSecIntfDownNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapLanId"))
)
if mibBuilder.loadTexts:
    hubSecIntfDownNotify.setStatus(
        ""
    )

ftProcessAbnormalTerminationNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 107)
)
ftProcessAbnormalTerminationNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapProcName"),
        ("ARMILLAIRE2000-MIB", "trapProcInstNo"))
)
if mibBuilder.loadTexts:
    ftProcessAbnormalTerminationNotify.setStatus(
        ""
    )

ftProcessRestartConfigSucceededNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 108)
)
ftProcessRestartConfigSucceededNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapProcName"),
        ("ARMILLAIRE2000-MIB", "trapProcInstNo"))
)
if mibBuilder.loadTexts:
    ftProcessRestartConfigSucceededNotify.setStatus(
        ""
    )

ftProcessRestartConfigFailedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 109)
)
ftProcessRestartConfigFailedNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapProcName"),
        ("ARMILLAIRE2000-MIB", "trapProcInstNo"))
)
if mibBuilder.loadTexts:
    ftProcessRestartConfigFailedNotify.setStatus(
        ""
    )

ftMsscFtmupNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 110)
)
ftMsscFtmupNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"))
)
if mibBuilder.loadTexts:
    ftMsscFtmupNotify.setStatus(
        ""
    )

ftControlSwitchOverSucceededNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 111)
)
ftControlSwitchOverSucceededNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapProcName"))
)
if mibBuilder.loadTexts:
    ftControlSwitchOverSucceededNotify.setStatus(
        ""
    )

ftControlSwitchOverFailedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 112)
)
ftControlSwitchOverFailedNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapProcName"))
)
if mibBuilder.loadTexts:
    ftControlSwitchOverFailedNotify.setStatus(
        ""
    )

ftForcedSwitchOverSucceededNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 113)
)
ftForcedSwitchOverSucceededNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapProcName"))
)
if mibBuilder.loadTexts:
    ftForcedSwitchOverSucceededNotify.setStatus(
        ""
    )

ftForcedSwitchOverFailedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 114)
)
ftForcedSwitchOverFailedNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapProcName"))
)
if mibBuilder.loadTexts:
    ftForcedSwitchOverFailedNotify.setStatus(
        ""
    )

ftProcessRestartDisableNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 115)
)
ftProcessRestartDisableNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapProcName"),
        ("ARMILLAIRE2000-MIB", "trapProcInstNo"))
)
if mibBuilder.loadTexts:
    ftProcessRestartDisableNotify.setStatus(
        ""
    )

updateDBAuditOpStatNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 116)
)
updateDBAuditOpStatNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"))
)
if mibBuilder.loadTexts:
    updateDBAuditOpStatNotify.setStatus(
        ""
    )

isupIccAuditNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 117)
)
isupIccAuditNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"))
)
if mibBuilder.loadTexts:
    isupIccAuditNotify.setStatus(
        ""
    )

cdrDiskFullMinorNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 118)
)
cdrDiskFullMinorNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapDirectory"))
)
if mibBuilder.loadTexts:
    cdrDiskFullMinorNotify.setStatus(
        ""
    )

cdrDiskFullMajorNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 119)
)
cdrDiskFullMajorNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapDirectory"))
)
if mibBuilder.loadTexts:
    cdrDiskFullMajorNotify.setStatus(
        ""
    )

cdrErrMoveCdrNackNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 120)
)
cdrErrMoveCdrNackNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapCdrFileName"))
)
if mibBuilder.loadTexts:
    cdrErrMoveCdrNackNotify.setStatus(
        ""
    )

cdrFileMoveCdrNackNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 121)
)
cdrFileMoveCdrNackNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapCdrFileName"))
)
if mibBuilder.loadTexts:
    cdrFileMoveCdrNackNotify.setStatus(
        ""
    )

ss7CktValidationNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 4618, 1, 2, 7, 2, 1, 0, 122)
)
ss7CktValidationNotify.setObjects(
      *(("ARMILLAIRE2000-MIB", "trapSeverity"),
        ("ARMILLAIRE2000-MIB", "trapOpc"),
        ("ARMILLAIRE2000-MIB", "trapSwitchName"),
        ("ARMILLAIRE2000-MIB", "trapDpc"),
        ("ARMILLAIRE2000-MIB", "trapCicvalue"),
        ("ARMILLAIRE2000-MIB", "trapCause"))
)
if mibBuilder.loadTexts:
    ss7CktValidationNotify.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARMILLAIRE2000-MIB",
    **{"RowStatus": RowStatus,
       "LrnRowStatus": LrnRowStatus,
       "CktRowStatus": CktRowStatus,
       "TmrRowStatus": TmrRowStatus,
       "UserLoginStatus": UserLoginStatus,
       "UserLoginPriority": UserLoginPriority,
       "ProcessStatus": ProcessStatus,
       "IsdnPriority": IsdnPriority,
       "IsdnType": IsdnType,
       "OpStatus": OpStatus,
       "LinkOpStatus": LinkOpStatus,
       "LinkSetOpStatus": LinkSetOpStatus,
       "CktOpStatus": CktOpStatus,
       "IsdnTrnkOpStatus": IsdnTrnkOpStatus,
       "ModifyTmrStatus": ModifyTmrStatus,
       "IfType": IfType,
       "AtmIfType": AtmIfType,
       "ConnectionType": ConnectionType,
       "EnableStatus": EnableStatus,
       "Ss7RouteType": Ss7RouteType,
       "AddrIdentifier": AddrIdentifier,
       "AddrType": AddrType,
       "NumPlan": NumPlan,
       "Direction": Direction,
       "EnableOperation": EnableOperation,
       "IsdnChnlMgtOperation": IsdnChnlMgtOperation,
       "IsdnTrnkMgtOperation": IsdnTrnkMgtOperation,
       "BlockOperation": BlockOperation,
       "Level": Level,
       "ModemResetStatus": ModemResetStatus,
       "ModemEnableStatus": ModemEnableStatus,
       "MeasEnableStatus": MeasEnableStatus,
       "EthernetConnStatus": EthernetConnStatus,
       "Standard": Standard,
       "TrunkType": TrunkType,
       "RouteType": RouteType,
       "AuditType": AuditType,
       "AuditOperation": AuditOperation,
       "Controlstatus": Controlstatus,
       "LinkControlStatus": LinkControlStatus,
       "LinkSetControlStatus": LinkSetControlStatus,
       "CircuitControlStatus": CircuitControlStatus,
       "IsdnControlstatus": IsdnControlstatus,
       "MtpRteState": MtpRteState,
       "Bool": Bool,
       "LoadBalance": LoadBalance,
       "TrnkGrpType": TrnkGrpType,
       "ActiveAlarmAckStatus": ActiveAlarmAckStatus,
       "EventType": EventType,
       "AlarmEvent": AlarmEvent,
       "AlarmSubEvent": AlarmSubEvent,
       "AlarmSeverity": AlarmSeverity,
       "RoffType": RoffType,
       "NameString": NameString,
       "AddrString": AddrString,
       "CdrFlag": CdrFlag,
       "DSPCardType": DSPCardType,
       "VoicePcm": VoicePcm,
       "TGFeature": TGFeature,
       "FTswitchOver": FTswitchOver,
       "LogFileAttr": LogFileAttr,
       "LogFileEnDis": LogFileEnDis,
       "SwitchType": SwitchType,
       "LinkType": LinkType,
       "LogType": LogType,
       "EnableTrace": EnableTrace,
       "TrunkState": TrunkState,
       "MeasPurgeFlag": MeasPurgeFlag,
       "E1MultiFrame": E1MultiFrame,
       "E1CRC4": E1CRC4,
       "TransClkSrc": TransClkSrc,
       "DS1LineType": DS1LineType,
       "DS1LineCoding": DS1LineCoding,
       "DS1LBO": DS1LBO,
       "DS3LineType": DS3LineType,
       "DS3LBO": DS3LBO,
       "DS3ATMCellMap": DS3ATMCellMap,
       "TimerType": TimerType,
       "armillaire": armillaire,
       "products": products,
       "armillaire2000": armillaire2000,
       "switchInfo": switchInfo,
       "switchGenInfoGrp": switchGenInfoGrp,
       "switchName": switchName,
       "switchDescr": switchDescr,
       "switchLocation": switchLocation,
       "switchContact": switchContact,
       "switchIPAddr": switchIPAddr,
       "switchUpTime": switchUpTime,
       "switchVersion": switchVersion,
       "switchVerDescr": switchVerDescr,
       "systemDescr": systemDescr,
       "switchType": switchType,
       "switchNameStatus": switchNameStatus,
       "switchPcInfo": switchPcInfo,
       "switchPcInfoTable": switchPcInfoTable,
       "switchPcEntry": switchPcEntry,
       "switchPc": switchPc,
       "switchPcMode": switchPcMode,
       "switchPcStatus": switchPcStatus,
       "switchUsrInfo": switchUsrInfo,
       "switchUserCfgTable": switchUserCfgTable,
       "switchUserCfgEntry": switchUserCfgEntry,
       "switchUserId": switchUserId,
       "switchUserName": switchUserName,
       "switchUserPassword": switchUserPassword,
       "switchUserPriority": switchUserPriority,
       "switchUserStatus": switchUserStatus,
       "switchVersionGrp": switchVersionGrp,
       "switchVerLM": switchVerLM,
       "switchVerMTP2": switchVerMTP2,
       "switchVerICC": switchVerICC,
       "switchVerSIG": switchVerSIG,
       "switchVerISDN": switchVerISDN,
       "switchVerSPHR": switchVerSPHR,
       "switchConfig": switchConfig,
       "ss7": ss7,
       "ss7Sig": ss7Sig,
       "ss7LinkCfgTable": ss7LinkCfgTable,
       "ss7LinkCfgEntry": ss7LinkCfgEntry,
       "ss7LinkName": ss7LinkName,
       "ss7LinkId": ss7LinkId,
       "ss7LinkTrunkId": ss7LinkTrunkId,
       "ss7LinkChannel": ss7LinkChannel,
       "ss7LinkSlc": ss7LinkSlc,
       "ss7LinkSpeed": ss7LinkSpeed,
       "ss7LinkMode": ss7LinkMode,
       "ss7LinkRowStatus": ss7LinkRowStatus,
       "ss7LinkOpStatus": ss7LinkOpStatus,
       "ss7AtmLinkCfgTable": ss7AtmLinkCfgTable,
       "ss7AtmLinkCfgEntry": ss7AtmLinkCfgEntry,
       "ss7AtmVpi": ss7AtmVpi,
       "ss7AtmVci": ss7AtmVci,
       "ss7AtmLnkId": ss7AtmLnkId,
       "ss7AtmXconnectId": ss7AtmXconnectId,
       "ss7AtmSlotId": ss7AtmSlotId,
       "ss7AtmPortId": ss7AtmPortId,
       "ss7AtmChnlId": ss7AtmChnlId,
       "ss7AtmTrnkId": ss7AtmTrnkId,
       "ss7AtmPhyType": ss7AtmPhyType,
       "ss7AtmLinkRowStatus": ss7AtmLinkRowStatus,
       "ss7AtmLinkOpStatus": ss7AtmLinkOpStatus,
       "ss7LinksetCfgTable": ss7LinksetCfgTable,
       "ss7LinksetCfgEntry": ss7LinksetCfgEntry,
       "ss7LinksetLinkId": ss7LinksetLinkId,
       "ss7LinksetId": ss7LinksetId,
       "ss7LinksetName": ss7LinksetName,
       "ss7LinksetAdjDpc": ss7LinksetAdjDpc,
       "ss7LinksetMode": ss7LinksetMode,
       "ss7LinksetRowStatus": ss7LinksetRowStatus,
       "ss7LinksetOpStatus": ss7LinksetOpStatus,
       "ss7LinksetMgmtTable": ss7LinksetMgmtTable,
       "ss7LinksetMgmtEntry": ss7LinksetMgmtEntry,
       "linksetId": linksetId,
       "linksetLevel": linksetLevel,
       "linksetMgmntCmd": linksetMgmntCmd,
       "ss7LinkMgmntTable": ss7LinkMgmntTable,
       "ss7LinkMgmntEntry": ss7LinkMgmntEntry,
       "linkName": linkName,
       "linkMgmntCmd": linkMgmntCmd,
       "ss7Br": ss7Br,
       "ss7TrunkCfgTable": ss7TrunkCfgTable,
       "ss7TrunkCfgEntry": ss7TrunkCfgEntry,
       "ss7TrunkId": ss7TrunkId,
       "ss7TrunkName": ss7TrunkName,
       "ss7TrunkGrpId": ss7TrunkGrpId,
       "ss7TrunkXconnectId": ss7TrunkXconnectId,
       "ss7TrunkSlotId": ss7TrunkSlotId,
       "ss7TrunkPortId": ss7TrunkPortId,
       "ss7TrunkOpc": ss7TrunkOpc,
       "ss7TrunkDpc": ss7TrunkDpc,
       "ss7TrunkPhyType": ss7TrunkPhyType,
       "ss7TrunkMode": ss7TrunkMode,
       "ss7TrunkE1MultiFrame": ss7TrunkE1MultiFrame,
       "ss7TrunkE1CRC4": ss7TrunkE1CRC4,
       "ss7TrunkE1TransClk": ss7TrunkE1TransClk,
       "ss7TrunkDS1LineType": ss7TrunkDS1LineType,
       "ss7TrunkDS1LineCoding": ss7TrunkDS1LineCoding,
       "ss7TrunkDS1TransClkSrc": ss7TrunkDS1TransClkSrc,
       "ss7TrunkDS1LBO": ss7TrunkDS1LBO,
       "ss7TrunkDS3LineType": ss7TrunkDS3LineType,
       "ss7TrunkDS3TransClkSrc": ss7TrunkDS3TransClkSrc,
       "ss7TrunkDS3LBO": ss7TrunkDS3LBO,
       "ss7TrunkDS3DS1LineType": ss7TrunkDS3DS1LineType,
       "ss7TrunkDS3DS1TransClkSrc": ss7TrunkDS3DS1TransClkSrc,
       "ss7TrunkOC3TransClkSrc": ss7TrunkOC3TransClkSrc,
       "ss7TrunkUNCHE3TransClkSrc": ss7TrunkUNCHE3TransClkSrc,
       "ss7TrunkDS3ATMLineType": ss7TrunkDS3ATMLineType,
       "ss7TrunkDS3ATMCellMap": ss7TrunkDS3ATMCellMap,
       "ss7TrunkDS3ATMTransClkSrc": ss7TrunkDS3ATMTransClkSrc,
       "ss7TrunkDS3ATMLBO": ss7TrunkDS3ATMLBO,
       "ss7TrunkRowStatus": ss7TrunkRowStatus,
       "ss7TrunkOpStatus": ss7TrunkOpStatus,
       "ss7CktCfgTable": ss7CktCfgTable,
       "ss7CktCfgEntry": ss7CktCfgEntry,
       "ss7CktTrunkId": ss7CktTrunkId,
       "ss7CktChnlId": ss7CktChnlId,
       "ss7CktId": ss7CktId,
       "ss7CktDpc": ss7CktDpc,
       "ss7CktCic": ss7CktCic,
       "ss7CktDir": ss7CktDir,
       "ss7CktPriority": ss7CktPriority,
       "ss7CktT3": ss7CktT3,
       "ss7CktT12": ss7CktT12,
       "ss7CktT13": ss7CktT13,
       "ss7CktT14": ss7CktT14,
       "ss7CktT15": ss7CktT15,
       "ss7CktT16": ss7CktT16,
       "ss7CktT17": ss7CktT17,
       "ss7CktTVal": ss7CktTVal,
       "ss7CktRowStatus": ss7CktRowStatus,
       "ss7CktOpStatus": ss7CktOpStatus,
       "ss7CICTimerTable": ss7CICTimerTable,
       "ss7CicTmrEntry": ss7CicTmrEntry,
       "ss7CktTmrDpc": ss7CktTmrDpc,
       "ss7CktTmrCic": ss7CktTmrCic,
       "ss7CktTmrT3": ss7CktTmrT3,
       "ss7CktTmrT12": ss7CktTmrT12,
       "ss7CktTmrT13": ss7CktTmrT13,
       "ss7CktTmrT14": ss7CktTmrT14,
       "ss7CktTmrT15": ss7CktTmrT15,
       "ss7CktTmrT16": ss7CktTmrT16,
       "ss7CktTmrT17": ss7CktTmrT17,
       "ss7CktTmrTVal": ss7CktTmrTVal,
       "ss7CktTmrRowStatus": ss7CktTmrRowStatus,
       "ss7BCktCfgTable": ss7BCktCfgTable,
       "ss7BCktCfgEntry": ss7BCktCfgEntry,
       "ss7BCktVpi": ss7BCktVpi,
       "ss7BCktVci": ss7BCktVci,
       "ss7BCktTrunkId": ss7BCktTrunkId,
       "ss7BCktDpc": ss7BCktDpc,
       "ss7BCktCic": ss7BCktCic,
       "ss7BCktDir": ss7BCktDir,
       "ss7BCktPriority": ss7BCktPriority,
       "ss7BCktT3": ss7BCktT3,
       "ss7BCktT12": ss7BCktT12,
       "ss7BCktT13": ss7BCktT13,
       "ss7BCktT14": ss7BCktT14,
       "ss7BCktT15": ss7BCktT15,
       "ss7BCktT16": ss7BCktT16,
       "ss7BCktT17": ss7BCktT17,
       "ss7BCktTVal": ss7BCktTVal,
       "ss7BCktRowStatus": ss7BCktRowStatus,
       "ss7BCktOpStatus": ss7BCktOpStatus,
       "ss7CktMgmntGroup": ss7CktMgmntGroup,
       "ss7CktMgmntTable": ss7CktMgmntTable,
       "ss7CktMgmntEntry": ss7CktMgmntEntry,
       "ss7CktMgmntTrnkId": ss7CktMgmntTrnkId,
       "ss7CktMgmntChnlId": ss7CktMgmntChnlId,
       "ss7CktMgmntRepNum": ss7CktMgmntRepNum,
       "ss7CktMgmntCmd": ss7CktMgmntCmd,
       "ss7CICMgmntTable": ss7CICMgmntTable,
       "ss7CICMgmntEntry": ss7CICMgmntEntry,
       "ss7CktMgmtDPC": ss7CktMgmtDPC,
       "ss7CktMgmtCIC": ss7CktMgmtCIC,
       "ss7CktRepNum": ss7CktRepNum,
       "ss7CicRange": ss7CicRange,
       "ss7CICMgmntCmd": ss7CICMgmntCmd,
       "mtp2": mtp2,
       "mtp2LinkTmrCfgTable": mtp2LinkTmrCfgTable,
       "mtp2LinkTmrCfgEntry": mtp2LinkTmrCfgEntry,
       "mtp2LinkId": mtp2LinkId,
       "mtp2T1": mtp2T1,
       "mtp2T2": mtp2T2,
       "mtp2T3": mtp2T3,
       "mtp2T4n": mtp2T4n,
       "mtp2T4e": mtp2T4e,
       "mtp2T5": mtp2T5,
       "mtp2T6": mtp2T6,
       "mtp2T7": mtp2T7,
       "mtp2RowStatus": mtp2RowStatus,
       "mtp2OpStatus": mtp2OpStatus,
       "mtp3": mtp3,
       "mtp3GenTmrCfgGroup": mtp3GenTmrCfgGroup,
       "mtp3T15": mtp3T15,
       "mtp3T16": mtp3T16,
       "mtp3T18": mtp3T18,
       "mtp3T19": mtp3T19,
       "mtp3T20": mtp3T20,
       "mtp3T21": mtp3T21,
       "mtp3T26": mtp3T26,
       "mtp3T30": mtp3T30,
       "mtp3GenTmrRowStatus": mtp3GenTmrRowStatus,
       "mtp3LinkCfgTable": mtp3LinkCfgTable,
       "mtp3LinkCfgEntry": mtp3LinkCfgEntry,
       "mtp3LinkId": mtp3LinkId,
       "mtp3T1": mtp3T1,
       "mtp3T2": mtp3T2,
       "mtp3T3": mtp3T3,
       "mtp3T4": mtp3T4,
       "mtp3T5": mtp3T5,
       "mtp3T6": mtp3T6,
       "mtp3T7": mtp3T7,
       "mtp3T12": mtp3T12,
       "mtp3T13": mtp3T13,
       "mtp3T14": mtp3T14,
       "mtp3T17": mtp3T17,
       "mtp3T22": mtp3T22,
       "mtp3T23": mtp3T23,
       "mtp3T24": mtp3T24,
       "mtp3T31": mtp3T31,
       "mtp3T32": mtp3T32,
       "mtp3T33": mtp3T33,
       "mtp3T34": mtp3T34,
       "mtp3T35": mtp3T35,
       "mtp3T36": mtp3T36,
       "mtp3T37": mtp3T37,
       "mtp3TFLC": mtp3TFLC,
       "mtp3TBND": mtp3TBND,
       "mtp3RowStatus": mtp3RowStatus,
       "mtp3OpStatus": mtp3OpStatus,
       "isup": isup,
       "isupTimerCfgTable": isupTimerCfgTable,
       "isupTimerCfgEntry": isupTimerCfgEntry,
       "isupTimerType": isupTimerType,
       "isupTmrT1": isupTmrT1,
       "isupTmrT2": isupTmrT2,
       "isupTmrT5": isupTmrT5,
       "isupTmrT6": isupTmrT6,
       "isupTmrT7": isupTmrT7,
       "isupTmrT8": isupTmrT8,
       "isupTmrT9": isupTmrT9,
       "isupTmrT18": isupTmrT18,
       "isupTmrT19": isupTmrT19,
       "isupTmrT20": isupTmrT20,
       "isupTmrT21": isupTmrT21,
       "isupTmrT22": isupTmrT22,
       "isupTmrT23": isupTmrT23,
       "isupTmrT27": isupTmrT27,
       "isupTmrT28": isupTmrT28,
       "isupTmrT31": isupTmrT31,
       "isupTmrT33": isupTmrT33,
       "isupTmrT34": isupTmrT34,
       "isupTmrT36": isupTmrT36,
       "isupTmrTCCR": isupTmrTCCR,
       "isupTmrTEX": isupTmrTEX,
       "isupTmrTCRM": isupTmrTCRM,
       "isupTmrTCRA": isupTmrTCRA,
       "isupTmrTCCRt": isupTmrTCCRt,
       "isupTmrTECt": isupTmrTECt,
       "isupTmrTGTCHG": isupTmrTGTCHG,
       "isupTmrTGRES": isupTmrTGRES,
       "isupTmrTFGR": isupTmrTFGR,
       "isupTmrTRELRSP": isupTmrTRELRSP,
       "isupTmrTFNLRELRS": isupTmrTFNLRELRS,
       "isupTimerRowStatus": isupTimerRowStatus,
       "ss7Route": ss7Route,
       "ss7RtDpcTable": ss7RtDpcTable,
       "ss7RtDpcEntry": ss7RtDpcEntry,
       "ss7RtDPC": ss7RtDPC,
       "ss7RtCmbLinksetId": ss7RtCmbLinksetId,
       "ss7RtLoadShareType": ss7RtLoadShareType,
       "ss7RtRowStatus": ss7RtRowStatus,
       "ss7RtOpStatus": ss7RtOpStatus,
       "isdn": isdn,
       "isdnTmrCfgTable": isdnTmrCfgTable,
       "isdnTmrCfgEntry": isdnTmrCfgEntry,
       "isdnTnkId": isdnTnkId,
       "isdnTmrT301": isdnTmrT301,
       "isdnTmrT302": isdnTmrT302,
       "isdnTmrT303": isdnTmrT303,
       "isdnTmrT304": isdnTmrT304,
       "isdnTmrT305": isdnTmrT305,
       "isdnTmrT306": isdnTmrT306,
       "isdnTmrT307": isdnTmrT307,
       "isdnTmrT308": isdnTmrT308,
       "isdnTmrT310": isdnTmrT310,
       "isdnTmrT311": isdnTmrT311,
       "isdnTmrT312": isdnTmrT312,
       "isdnTmrT313": isdnTmrT313,
       "isdnTmrT316": isdnTmrT316,
       "isdnTmrT318": isdnTmrT318,
       "isdnTmrT319": isdnTmrT319,
       "isdnTmrT322": isdnTmrT322,
       "isdnTmrT316C": isdnTmrT316C,
       "isdnTmrT330": isdnTmrT330,
       "isdnTmrT331": isdnTmrT331,
       "isdnTmrT332": isdnTmrT332,
       "isdnTmrTRST": isdnTmrTRST,
       "isdnTmrTREST": isdnTmrTREST,
       "isdnTmrTANS": isdnTmrTANS,
       "isdnTmrT396": isdnTmrT396,
       "isdnTmrT397": isdnTmrT397,
       "isdnTrnkTmrRowStatus": isdnTrnkTmrRowStatus,
       "isdnTrnkTmrOpStatus": isdnTrnkTmrOpStatus,
       "isdnTrunkCfgTable": isdnTrunkCfgTable,
       "isdnTrunkCfgEntry": isdnTrunkCfgEntry,
       "isdnTrunkId": isdnTrunkId,
       "isdnTrunkName": isdnTrunkName,
       "isdnTrunkGrpId": isdnTrunkGrpId,
       "isdnDchnlId": isdnDchnlId,
       "isdnTrunkType": isdnTrunkType,
       "isdnXconnectId": isdnXconnectId,
       "isdnSlotId": isdnSlotId,
       "isdnPortId": isdnPortId,
       "isdnDirection": isdnDirection,
       "isdnPriority": isdnPriority,
       "isdnDurthreshold": isdnDurthreshold,
       "isdnCntthreshold": isdnCntthreshold,
       "isdnPhyIntfType": isdnPhyIntfType,
       "isdnDchnlTimeSlot": isdnDchnlTimeSlot,
       "isdnE1MultiFrame": isdnE1MultiFrame,
       "isdnE1CRC4": isdnE1CRC4,
       "isdnE1TransClk": isdnE1TransClk,
       "isdnDS1LineType": isdnDS1LineType,
       "isdnDS1LineCoding": isdnDS1LineCoding,
       "isdnDS1TransClkSrc": isdnDS1TransClkSrc,
       "isdnDS1LBO": isdnDS1LBO,
       "isdnDS3LineType": isdnDS3LineType,
       "isdnDS3TransClkSrc": isdnDS3TransClkSrc,
       "isdnDS3LBO": isdnDS3LBO,
       "isdnDS3DS1LineType": isdnDS3DS1LineType,
       "isdnDS3DS1TransClkSrc": isdnDS3DS1TransClkSrc,
       "isdnTrunkRowStatus": isdnTrunkRowStatus,
       "isdnTrunkOpStatus": isdnTrunkOpStatus,
       "isdnChnlStatusTable": isdnChnlStatusTable,
       "isdnChnlStatusCfgEntry": isdnChnlStatusCfgEntry,
       "isdnStatusTrunkId": isdnStatusTrunkId,
       "isdnStatusChnlId": isdnStatusChnlId,
       "isdnStatusChnlState": isdnStatusChnlState,
       "isdnStatusChnlAllocMeth": isdnStatusChnlAllocMeth,
       "isdnStatusChnlSuConnId": isdnStatusChnlSuConnId,
       "isdnMgmntGroup": isdnMgmntGroup,
       "isdnTrnkMgmntTable": isdnTrnkMgmntTable,
       "isdnTrnkMgmntEntry": isdnTrnkMgmntEntry,
       "isdnTrnkMgmntId": isdnTrnkMgmntId,
       "isdnTrnkMgmntCmd": isdnTrnkMgmntCmd,
       "isdnChnlMgmntTable": isdnChnlMgmntTable,
       "isdnChnlMgmntEntry": isdnChnlMgmntEntry,
       "isdnTrunkMgmntId": isdnTrunkMgmntId,
       "isdnChnlMgmntId": isdnChnlMgmntId,
       "isdnChnlMgmntCmd": isdnChnlMgmntCmd,
       "mfdMgmntTable": mfdMgmntTable,
       "mfdMgmntEntry": mfdMgmntEntry,
       "isdnTnkMgmntId": isdnTnkMgmntId,
       "isdnDurThreshold": isdnDurThreshold,
       "isdnCntThreshold": isdnCntThreshold,
       "mfdMgmntCmd": mfdMgmntCmd,
       "trnkGrp": trnkGrp,
       "trunkGrpCfgTable": trunkGrpCfgTable,
       "trunkGrpCfgEntry": trunkGrpCfgEntry,
       "trunkGrpId": trunkGrpId,
       "trunkGrpName": trunkGrpName,
       "trunkGrpCarrierId": trunkGrpCarrierId,
       "trunkGrpType": trunkGrpType,
       "trunkGrpRoffName": trunkGrpRoffName,
       "trunkGrpRoffType": trunkGrpRoffType,
       "trunkGrpCdrFlag": trunkGrpCdrFlag,
       "trunkGrpNoOfTrunks": trunkGrpNoOfTrunks,
       "trunkGrpVoicePcm": trunkGrpVoicePcm,
       "trunkGrpRowStatus": trunkGrpRowStatus,
       "trunkGrpOpStatus": trunkGrpOpStatus,
       "rt": rt,
       "routeTable": routeTable,
       "routeEntry": routeEntry,
       "routeId": routeId,
       "routeAddrType": routeAddrType,
       "routeAdrId": routeAdrId,
       "routeAddr": routeAddr,
       "routeNumPlan": routeNumPlan,
       "routeNumOfDigit": routeNumOfDigit,
       "routeRouteName": routeRouteName,
       "routeRouteType": routeRouteType,
       "routeRowStatus": routeRowStatus,
       "routeOpStatus": routeOpStatus,
       "rtEntryIsdnCfgTable": rtEntryIsdnCfgTable,
       "rtEntryIsdnCfgEntry": rtEntryIsdnCfgEntry,
       "rtEntryIsdnGrpId": rtEntryIsdnGrpId,
       "rtEntryIsdntrunkId": rtEntryIsdntrunkId,
       "rtEntryIsdnRouteName": rtEntryIsdnRouteName,
       "rtEntryIsdnRowStatus": rtEntryIsdnRowStatus,
       "rtEntryIsdnOpStatus": rtEntryIsdnOpStatus,
       "rtEntrySs7CfgTable": rtEntrySs7CfgTable,
       "rtEntrySs7CfgEntry": rtEntrySs7CfgEntry,
       "rtEntrySs7GrpId": rtEntrySs7GrpId,
       "rtEntrySs7CmbLinksetId": rtEntrySs7CmbLinksetId,
       "rtEntrySs7RouteName": rtEntrySs7RouteName,
       "rtEntrySs7Dpc": rtEntrySs7Dpc,
       "rtEntrySs7Mode": rtEntrySs7Mode,
       "rtEntrySs7RowStatus": rtEntrySs7RowStatus,
       "rtEntrySs7OpStatus": rtEntrySs7OpStatus,
       "routeMgmntCmdGroup": routeMgmntCmdGroup,
       "digitStripMgmntTable": digitStripMgmntTable,
       "digitStripMgmntEntry": digitStripMgmntEntry,
       "rtName": rtName,
       "rtAddrType": rtAddrType,
       "rtNumOfDigit": rtNumOfDigit,
       "rtMgmntCmd": rtMgmntCmd,
       "isdnLoadBalanceMgmntTable": isdnLoadBalanceMgmntTable,
       "isdnLoadBalanceMgmntEntry": isdnLoadBalanceMgmntEntry,
       "rteName": rteName,
       "ilbMgmntCmd": ilbMgmntCmd,
       "xconnect": xconnect,
       "xconnectCfgTable": xconnectCfgTable,
       "xconnectCfgEntry": xconnectCfgEntry,
       "xconnectId": xconnectId,
       "xconnectName": xconnectName,
       "xconnectIPAddr": xconnectIPAddr,
       "xconnectTCPPort": xconnectTCPPort,
       "xconnectRowStatus": xconnectRowStatus,
       "xconnectOpStatus": xconnectOpStatus,
       "xlinkCfgTable": xlinkCfgTable,
       "xlinkCfgEntry": xlinkCfgEntry,
       "xconnectIdEndA": xconnectIdEndA,
       "slotIdEndA": slotIdEndA,
       "portIdEndA": portIdEndA,
       "xconnectIdEndB": xconnectIdEndB,
       "slotIdEndB": slotIdEndB,
       "portIdEndB": portIdEndB,
       "xlinkConnectionType": xlinkConnectionType,
       "xlinkRowStatus": xlinkRowStatus,
       "xlinkOpStatus": xlinkOpStatus,
       "xlinkMgmntTable": xlinkMgmntTable,
       "xlinkMgmntEntry": xlinkMgmntEntry,
       "xconnIdEndA": xconnIdEndA,
       "xconnSlotIdEndA": xconnSlotIdEndA,
       "xconnPortIdEndA": xconnPortIdEndA,
       "xconnIdEndB": xconnIdEndB,
       "xconnSlotIdEndB": xconnSlotIdEndB,
       "xconnPortIdEndB": xconnPortIdEndB,
       "xlinkMgmntCmd": xlinkMgmntCmd,
       "enableGroup": enableGroup,
       "enableSwitch": enableSwitch,
       "enableSS7Route": enableSS7Route,
       "enableSS7Ckt": enableSS7Ckt,
       "enableIsdntrunk": enableIsdntrunk,
       "enableXconnect": enableXconnect,
       "enableRoute": enableRoute,
       "switchMeas": switchMeas,
       "measFile": measFile,
       "measFileInfo": measFileInfo,
       "measFileAcknowledge": measFileAcknowledge,
       "measFileConfig": measFileConfig,
       "measFileCfgMeasInterval": measFileCfgMeasInterval,
       "measFileCfgUsagescanInterval": measFileCfgUsagescanInterval,
       "measFileCfgPurgeDay": measFileCfgPurgeDay,
       "measFileCfgPurgeFlag": measFileCfgPurgeFlag,
       "measFileCfgPrimaryDir": measFileCfgPrimaryDir,
       "measFileCfgSecondaryDir": measFileCfgSecondaryDir,
       "measFileEnableGrp": measFileEnableGrp,
       "measFileEnablePRITraffic": measFileEnablePRITraffic,
       "measFileEnableISUPTraffic": measFileEnableISUPTraffic,
       "measFileEnablePRIIneffectiveCall": measFileEnablePRIIneffectiveCall,
       "measFileEnableISUPIneffectiveCall": measFileEnableISUPIneffectiveCall,
       "measFileEnableTrunkGrp": measFileEnableTrunkGrp,
       "measFileEnableSS7LinkTraffic": measFileEnableSS7LinkTraffic,
       "measSwitch": measSwitch,
       "measSwitchIsupGrp": measSwitchIsupGrp,
       "measSwitchIsupDataSuspect": measSwitchIsupDataSuspect,
       "measSwitchIsupIncomingAnsiTrunkCallAttempts": measSwitchIsupIncomingAnsiTrunkCallAttempts,
       "measSwitchIsupIncomingAnsiTrunkCallAnswered": measSwitchIsupIncomingAnsiTrunkCallAnswered,
       "measSwitchIsupOutgoingAnsiTrunkCallAttempts": measSwitchIsupOutgoingAnsiTrunkCallAttempts,
       "measSwitchIsupOutgoingAnsiTrunkCallAnswered": measSwitchIsupOutgoingAnsiTrunkCallAnswered,
       "measSwitchIsupIncomingItutTrunkCallAttempts": measSwitchIsupIncomingItutTrunkCallAttempts,
       "measSwitchIsupIncomingItutTrunkCallAnswered": measSwitchIsupIncomingItutTrunkCallAnswered,
       "measSwitchIsupOutgoingItutTrunkCallAttempts": measSwitchIsupOutgoingItutTrunkCallAttempts,
       "measSwitchIsupOutgoingItutTrunkCallAnswered": measSwitchIsupOutgoingItutTrunkCallAnswered,
       "measSwitchIsupFailCallGrp": measSwitchIsupFailCallGrp,
       "measSwitchIsupFailCallDataSuspect": measSwitchIsupFailCallDataSuspect,
       "measSwitchIsupFailCallAnsiMatchingLoss": measSwitchIsupFailCallAnsiMatchingLoss,
       "measSwitchIsupFailCallAnsiNoCircuit": measSwitchIsupFailCallAnsiNoCircuit,
       "measSwitchIsupFailCallAnsiCalledPartyLineBusy": measSwitchIsupFailCallAnsiCalledPartyLineBusy,
       "measSwitchIsupFailCallAnsiIneffectiveMachineAttempts": measSwitchIsupFailCallAnsiIneffectiveMachineAttempts,
       "measSwitchIsupFailCallItutMatchingLoss": measSwitchIsupFailCallItutMatchingLoss,
       "measSwitchIsupFailCallItutNoCircuit": measSwitchIsupFailCallItutNoCircuit,
       "measSwitchIsupFailCallItutCalledPartyLineBusy": measSwitchIsupFailCallItutCalledPartyLineBusy,
       "measSwitchIsupFailCallItutIneffectiveMachineAttempts": measSwitchIsupFailCallItutIneffectiveMachineAttempts,
       "measSwitchPriGrp": measSwitchPriGrp,
       "measSwitchPriDataSuspect": measSwitchPriDataSuspect,
       "measSwitchPriIncomingIsdnPRICallAttempts": measSwitchPriIncomingIsdnPRICallAttempts,
       "measSwitchPriIncomingIsdnPRICallAnswered": measSwitchPriIncomingIsdnPRICallAnswered,
       "measSwitchPriFailCallGrp": measSwitchPriFailCallGrp,
       "measSwitchPriFailCallDataSuspect": measSwitchPriFailCallDataSuspect,
       "measSwitchPriFailCallMatchingLoss": measSwitchPriFailCallMatchingLoss,
       "measSwitchPriFailCallNoCircuit": measSwitchPriFailCallNoCircuit,
       "measSwitchPriFailCallCalledPartyLineBusy": measSwitchPriFailCallCalledPartyLineBusy,
       "measSwitchPriFailCallIneffectiveMachineAttempts": measSwitchPriFailCallIneffectiveMachineAttempts,
       "measTrnkGrp": measTrnkGrp,
       "measTrnkGrpTrafficTable": measTrnkGrpTrafficTable,
       "measTrnkGrpTrafficEntry": measTrnkGrpTrafficEntry,
       "measTrnkGrpName": measTrnkGrpName,
       "measTrnkGrpDataSuspect": measTrnkGrpDataSuspect,
       "measTrnkGrpincomingUsage": measTrnkGrpincomingUsage,
       "measTrnkGrpoutgoingUsage": measTrnkGrpoutgoingUsage,
       "measTrnkGrpISCicsChnls": measTrnkGrpISCicsChnls,
       "measTrnkGrpOOSCicsChnls": measTrnkGrpOOSCicsChnls,
       "measTrnkGrptotalUsage": measTrnkGrptotalUsage,
       "measTrnkGrpmaintainanceUsage": measTrnkGrpmaintainanceUsage,
       "measLnk": measLnk,
       "measLinkTrafficTable": measLinkTrafficTable,
       "measLinkTrafficEntry": measLinkTrafficEntry,
       "measLinkName": measLinkName,
       "measLinkDataSuspect": measLinkDataSuspect,
       "measLinkUnavailableDuration": measLinkUnavailableDuration,
       "measLinkInServiceDuration": measLinkInServiceDuration,
       "measLinkMSUsRetransmitted": measLinkMSUsRetransmitted,
       "measLinkOctetsReceived": measLinkOctetsReceived,
       "measLinkOctectsTransmitted": measLinkOctectsTransmitted,
       "measLinkLostMSUsBufferOverflow": measLinkLostMSUsBufferOverflow,
       "measLinkMSUsDiscarded": measLinkMSUsDiscarded,
       "switchCdr": switchCdr,
       "cdrConfig": cdrConfig,
       "cdrLongDurCallGenTime": cdrLongDurCallGenTime,
       "cdrBafConfig": cdrBafConfig,
       "cdrAppendModule801": cdrAppendModule801,
       "cdrSensorId": cdrSensorId,
       "cdrRecordingOfficeId": cdrRecordingOfficeId,
       "cdrFileConfig": cdrFileConfig,
       "cdrFileInterval": cdrFileInterval,
       "cdrFileRecLimit": cdrFileRecLimit,
       "cdrFileSourceId": cdrFileSourceId,
       "cdrFileDestinationType": cdrFileDestinationType,
       "cdrFileDestinationId": cdrFileDestinationId,
       "cdrFileInfo": cdrFileInfo,
       "cdrFileQuery": cdrFileQuery,
       "cdrFileName": cdrFileName,
       "cdrFileStatus": cdrFileStatus,
       "cdrFileCreateDate": cdrFileCreateDate,
       "cdrFileCreateTime": cdrFileCreateTime,
       "cdrFileRecordNum": cdrFileRecordNum,
       "cdrFileAcknowledge": cdrFileAcknowledge,
       "cdrMgmntCmdGroup": cdrMgmntCmdGroup,
       "cdrGenMgmntCmd": cdrGenMgmntCmd,
       "cdrMngmtTrnkGrpTable": cdrMngmtTrnkGrpTable,
       "cdrMngmtTrnkGrpEntry": cdrMngmtTrnkGrpEntry,
       "cdrTrnkGrpId": cdrTrnkGrpId,
       "cdrTrnkGrpdirection": cdrTrnkGrpdirection,
       "cdrTrnkGrpMgmntCmd": cdrTrnkGrpMgmntCmd,
       "switchFeature": switchFeature,
       "modemFaultDetection": modemFaultDetection,
       "modemStatusTable": modemStatusTable,
       "modemStatusEntry": modemStatusEntry,
       "faultModemTrnkId": faultModemTrnkId,
       "faultModemChnlId": faultModemChnlId,
       "faultModemRepnum": faultModemRepnum,
       "faultModemReset": faultModemReset,
       "lnp": lnp,
       "lrnTable": lrnTable,
       "lrnEntry": lrnEntry,
       "lrnNum": lrnNum,
       "lrnRowStatus": lrnRowStatus,
       "switchDSP": switchDSP,
       "switchDSPCfgTable": switchDSPCfgTable,
       "switchDSPCfgEntry": switchDSPCfgEntry,
       "switchDSPXconnId": switchDSPXconnId,
       "switchDSPSlotId": switchDSPSlotId,
       "switchDSPCardType": switchDSPCardType,
       "switchDSPCfgRowStatus": switchDSPCfgRowStatus,
       "switchDSPCfgOpStatus": switchDSPCfgOpStatus,
       "switchTGFeature": switchTGFeature,
       "switchFeatureTGCfgTable": switchFeatureTGCfgTable,
       "switchTGGrpCfgEntry": switchTGGrpCfgEntry,
       "switchFeatureTGId": switchFeatureTGId,
       "switchFeatureTGName": switchFeatureTGName,
       "switchFeatureTGType": switchFeatureTGType,
       "switchFeatureTGFeatureEC": switchFeatureTGFeatureEC,
       "switchFeatureTGFeatureCOMPRESS": switchFeatureTGFeatureCOMPRESS,
       "switchFeatureTGFeatureSS": switchFeatureTGFeatureSS,
       "switchFeatureTGFeatureCNIS": switchFeatureTGFeatureCNIS,
       "switchMaintenance": switchMaintenance,
       "ft": ft,
       "ftSwitchOverInfo": ftSwitchOverInfo,
       "switchOver": switchOver,
       "log": log,
       "logFileInfo": logFileInfo,
       "logGenTime": logGenTime,
       "logPurgeTime": logPurgeTime,
       "logFileGenEnable": logFileGenEnable,
       "enablelogGen": enablelogGen,
       "disableLogGen": disableLogGen,
       "logFileAttribute": logFileAttribute,
       "logAttribute": logAttribute,
       "logFileSize": logFileSize,
       "logFileDuration": logFileDuration,
       "logFileStatus": logFileStatus,
       "trace": trace,
       "ss7LnkTrace": ss7LnkTrace,
       "ss7LnkTraceTable": ss7LnkTraceTable,
       "ss7LnkTraceEntry": ss7LnkTraceEntry,
       "ss7LnkId": ss7LnkId,
       "ss7LnkLog": ss7LnkLog,
       "ss7LnkEnable": ss7LnkEnable,
       "ss7RouteTrace": ss7RouteTrace,
       "ss7RouteTraceTable": ss7RouteTraceTable,
       "ss7RouteTraceEntry": ss7RouteTraceEntry,
       "ss7RouteDpc": ss7RouteDpc,
       "ss7RouteLog": ss7RouteLog,
       "ss7RouteEnable": ss7RouteEnable,
       "isdnTrnkTrace": isdnTrnkTrace,
       "isdnTrunkTraceTable": isdnTrunkTraceTable,
       "isdnTrunkTraceEntry": isdnTrunkTraceEntry,
       "isdnTrnkId": isdnTrnkId,
       "isdnTrunkLog": isdnTrunkLog,
       "isdnTrunkEnable": isdnTrunkEnable,
       "processStatus": processStatus,
       "processStatusInfo": processStatusInfo,
       "statusLM1ProcId": statusLM1ProcId,
       "statusLM2ProcID": statusLM2ProcID,
       "statusICC1ProcId": statusICC1ProcId,
       "statusICC2ProcId": statusICC2ProcId,
       "statusISDN1ProcId": statusISDN1ProcId,
       "statusISDN2ProcId": statusISDN2ProcId,
       "statusSPHR1ProcId": statusSPHR1ProcId,
       "statusSPHR2ProcId": statusSPHR2ProcId,
       "statusSIG1ProcId": statusSIG1ProcId,
       "statusSIG2ProcId": statusSIG2ProcId,
       "statusMTP21ProcId": statusMTP21ProcId,
       "statusMTP22ProcId": statusMTP22ProcId,
       "statusMTP23ProcId": statusMTP23ProcId,
       "statusMTP24ProcId": statusMTP24ProcId,
       "ethernetConnStatusInfo": ethernetConnStatusInfo,
       "ethernetConnStatus": ethernetConnStatus,
       "audit": audit,
       "auditInfo": auditInfo,
       "auditISDNTrnkTable": auditISDNTrnkTable,
       "auditISDNTrnkCfgEntry": auditISDNTrnkCfgEntry,
       "auditTrnkId": auditTrnkId,
       "auditISDNTrnk": auditISDNTrnk,
       "auditXLink": auditXLink,
       "auditDPCTable": auditDPCTable,
       "auditDPCCfgEntry": auditDPCCfgEntry,
       "auditPointCode": auditPointCode,
       "auditPointCodeType": auditPointCodeType,
       "auditDPC": auditDPC,
       "auditPeriodGrp": auditPeriodGrp,
       "auditTimePeriod": auditTimePeriod,
       "auditPeriod": auditPeriod,
       "switchTrap": switchTrap,
       "trapObjects": trapObjects,
       "trapOpc": trapOpc,
       "trapXconnectId": trapXconnectId,
       "trapLinkId": trapLinkId,
       "trapSlotId": trapSlotId,
       "trapPortId": trapPortId,
       "trapTrunkId": trapTrunkId,
       "trapInterfaceId": trapInterfaceId,
       "trapChnlId": trapChnlId,
       "trapDbId": trapDbId,
       "trapLinkName": trapLinkName,
       "trapSwitchName": trapSwitchName,
       "trapCicvalue": trapCicvalue,
       "trapCicrange": trapCicrange,
       "trapCause": trapCause,
       "trapDpc": trapDpc,
       "trapCdrFileSeqNum": trapCdrFileSeqNum,
       "trapCdrFileName": trapCdrFileName,
       "trapMeasErrCause": trapMeasErrCause,
       "trapMeasErrNum": trapMeasErrNum,
       "trapRepeatNum": trapRepeatNum,
       "trapSeverity": trapSeverity,
       "trapProcessId": trapProcessId,
       "trapBucketSize": trapBucketSize,
       "trapNode1Id": trapNode1Id,
       "trapNode2Id": trapNode2Id,
       "trapRoutename": trapRoutename,
       "trapMeasFileName": trapMeasFileName,
       "trapDirectory": trapDirectory,
       "trapProcessorId": trapProcessorId,
       "trapLogFileName": trapLogFileName,
       "trapLogErrcause": trapLogErrcause,
       "trapLogErrNo": trapLogErrNo,
       "trapPsuNo": trapPsuNo,
       "trapIntId": trapIntId,
       "trapIntfcId": trapIntfcId,
       "trapLanId": trapLanId,
       "trapnumXlinks": trapnumXlinks,
       "trapSwitchId1": trapSwitchId1,
       "trapSwitchId2": trapSwitchId2,
       "trapProcInstNo": trapProcInstNo,
       "trapProcName": trapProcName,
       "trapFanNo": trapFanNo,
       "trapUserName": trapUserName,
       "trapBitMapStatus": trapBitMapStatus,
       "alarmGrp": alarmGrp,
       "alarmTraps": alarmTraps,
       "genswitchSnmpAgentReadyNotify": genswitchSnmpAgentReadyNotify,
       "genConsoleLoginNotify": genConsoleLoginNotify,
       "genConsoleLogoutNotify": genConsoleLogoutNotify,
       "genProcessBufOverflowNotify": genProcessBufOverflowNotify,
       "genProcessBufOverflowRecoverNotify": genProcessBufOverflowRecoverNotify,
       "genProcessHeapOverFlowNotify": genProcessHeapOverFlowNotify,
       "genProcessHeapOverFlowRecoverNotify": genProcessHeapOverFlowRecoverNotify,
       "xconnectUpNotify": xconnectUpNotify,
       "xconnectDnNotify": xconnectDnNotify,
       "xconnectClkClearNotify": xconnectClkClearNotify,
       "xconnectClkFailNotify": xconnectClkFailNotify,
       "xconnectBkplaneRefClkClearNotify": xconnectBkplaneRefClkClearNotify,
       "xconnectBkplaneRefClkFailNotify": xconnectBkplaneRefClkFailNotify,
       "xconnectInterfaceInServiceNotify": xconnectInterfaceInServiceNotify,
       "xconnectInterfaceOutOfServiceNotify": xconnectInterfaceOutOfServiceNotify,
       "xconnectCardInsertionNotify": xconnectCardInsertionNotify,
       "xconnectCardRemovalNotify": xconnectCardRemovalNotify,
       "xconnectIllegalCardTypeNotify": xconnectIllegalCardTypeNotify,
       "xconnectIntfFarEndLOFNotify": xconnectIntfFarEndLOFNotify,
       "xconnectIntfFarEndAISNotify": xconnectIntfFarEndAISNotify,
       "xconnectIntfNearEndLOFNotify": xconnectIntfNearEndLOFNotify,
       "xconnectIntfNearEndLOSNotify": xconnectIntfNearEndLOSNotify,
       "xconnectIntfCreateNotify": xconnectIntfCreateNotify,
       "xconnectIntfDeleteNotify": xconnectIntfDeleteNotify,
       "xconnectXlinkAdjConClrNotify": xconnectXlinkAdjConClrNotify,
       "xconnectXlinkAdjConNotify": xconnectXlinkAdjConNotify,
       "xconnectXlinkRouteFailNotify": xconnectXlinkRouteFailNotify,
       "xconnectPortUpNotify": xconnectPortUpNotify,
       "xconnectCPUSwitchOverNotify": xconnectCPUSwitchOverNotify,
       "atmRAINotify": atmRAINotify,
       "atmAISNotify": atmAISNotify,
       "atmLOFNotify": atmLOFNotify,
       "atmLOSNotify": atmLOSNotify,
       "mfdClearNotify": mfdClearNotify,
       "mfdDetectionNotify": mfdDetectionNotify,
       "measFileReadyNotify": measFileReadyNotify,
       "measDiskOverCrtclThresholdNotify": measDiskOverCrtclThresholdNotify,
       "measFileMoveNotify": measFileMoveNotify,
       "measFileMoveErrNotify": measFileMoveErrNotify,
       "measFileOpenErrNotify": measFileOpenErrNotify,
       "measFileDeleteNotify": measFileDeleteNotify,
       "measFileDeleteErrNotify": measFileDeleteErrNotify,
       "cdrFileReadyNotify": cdrFileReadyNotify,
       "cdrDiskFullNotify": cdrDiskFullNotify,
       "cdrFileOpenErrNotify": cdrFileOpenErrNotify,
       "cdrFileMoveErrNotify": cdrFileMoveErrNotify,
       "cdrDeleteErrNotify": cdrDeleteErrNotify,
       "cdrWriteHeaderErrNotify": cdrWriteHeaderErrNotify,
       "cdrWriteRecErrNotify": cdrWriteRecErrNotify,
       "cdrErrFileLocErrNotify": cdrErrFileLocErrNotify,
       "cdrErrTempFileLocErrNotify": cdrErrTempFileLocErrNotify,
       "cdrFileSysErrNotify": cdrFileSysErrNotify,
       "cdrFileCloseErrNotify": cdrFileCloseErrNotify,
       "cdrFileDelete5DaysNotify": cdrFileDelete5DaysNotify,
       "ss7LinkUpNotify": ss7LinkUpNotify,
       "ss7LinkDnNotify": ss7LinkDnNotify,
       "ss7Mtp2LinkUpNotify": ss7Mtp2LinkUpNotify,
       "ss7Mtp2LinkDnNotify": ss7Mtp2LinkDnNotify,
       "ss7LinkEnterCongestionNotify": ss7LinkEnterCongestionNotify,
       "ss7LinkExitCongestionNotify": ss7LinkExitCongestionNotify,
       "ss7InvalidSLCNotify": ss7InvalidSLCNotify,
       "ss7ConcernedDpcPauseNotify": ss7ConcernedDpcPauseNotify,
       "ss7ConcernedDpcResumeNotify": ss7ConcernedDpcResumeNotify,
       "ss7ConcernedDpcRemUnAvailNotify": ss7ConcernedDpcRemUnAvailNotify,
       "ss7LinkRemInhNotify": ss7LinkRemInhNotify,
       "ss7LinkRemUnInhNotify": ss7LinkRemUnInhNotify,
       "ss7LinkLocInhNotify": ss7LinkLocInhNotify,
       "ss7LinkLocUnInhNotify": ss7LinkLocUnInhNotify,
       "ss7LinkLOPBlkNotify": ss7LinkLOPBlkNotify,
       "ss7LinkLPRNotify": ss7LinkLPRNotify,
       "ss7LinkRPONotify": ss7LinkRPONotify,
       "ss7LinkRPRNotify": ss7LinkRPRNotify,
       "ss7IsupCicLocNotify": ss7IsupCicLocNotify,
       "ss7IsupCicRemNotify": ss7IsupCicRemNotify,
       "ss7IsupCongLvl1Notify": ss7IsupCongLvl1Notify,
       "ss7IsupCongLvl2Notify": ss7IsupCongLvl2Notify,
       "isdnDChnlUpNotify": isdnDChnlUpNotify,
       "isdnDChnlDnNotify": isdnDChnlDnNotify,
       "logFileReadyNotify": logFileReadyNotify,
       "logDiskFull60PercentNotify": logDiskFull60PercentNotify,
       "logDiskFull70PercentNotify": logDiskFull70PercentNotify,
       "logDiskFull80PercentNotify": logDiskFull80PercentNotify,
       "logErrFileOpenNotify": logErrFileOpenNotify,
       "logErrFileCloseNotify": logErrFileCloseNotify,
       "logErrFileDeleteNotify": logErrFileDeleteNotify,
       "logErrFileWriteNotify": logErrFileWriteNotify,
       "msscPriDedicatedLinkUpNotify": msscPriDedicatedLinkUpNotify,
       "msscPriDedicatedLinkDownNotify": msscPriDedicatedLinkDownNotify,
       "msscSecDedicatedLinkUpNotify": msscSecDedicatedLinkUpNotify,
       "msscSecDedicatedLinkDownNotify": msscSecDedicatedLinkDownNotify,
       "msscPriPsuUpNotify": msscPriPsuUpNotify,
       "msscPriPsuDownNotify": msscPriPsuDownNotify,
       "msscBakPsuUpNotify": msscBakPsuUpNotify,
       "msscBakPsuDownNotify": msscBakPsuDownNotify,
       "msscPriLanPhyIntfUpNotify": msscPriLanPhyIntfUpNotify,
       "msscPriLanPhyIntfDownNotify": msscPriLanPhyIntfDownNotify,
       "msscSecLanPhyIntfUpNotify": msscSecLanPhyIntfUpNotify,
       "msscSecLanPhyIntfDownNotify": msscSecLanPhyIntfDownNotify,
       "msscPriHostFanUpNotify": msscPriHostFanUpNotify,
       "msscPriHostFanDownNotify": msscPriHostFanDownNotify,
       "msscBckHostFanUpNotify": msscBckHostFanUpNotify,
       "msscBckHostFanDownNotify": msscBckHostFanDownNotify,
       "hubPriIntfUpNotify": hubPriIntfUpNotify,
       "hubPriIntfDownNotify": hubPriIntfDownNotify,
       "hubSecIntfUpNotify": hubSecIntfUpNotify,
       "hubSecIntfDownNotify": hubSecIntfDownNotify,
       "ftProcessAbnormalTerminationNotify": ftProcessAbnormalTerminationNotify,
       "ftProcessRestartConfigSucceededNotify": ftProcessRestartConfigSucceededNotify,
       "ftProcessRestartConfigFailedNotify": ftProcessRestartConfigFailedNotify,
       "ftMsscFtmupNotify": ftMsscFtmupNotify,
       "ftControlSwitchOverSucceededNotify": ftControlSwitchOverSucceededNotify,
       "ftControlSwitchOverFailedNotify": ftControlSwitchOverFailedNotify,
       "ftForcedSwitchOverSucceededNotify": ftForcedSwitchOverSucceededNotify,
       "ftForcedSwitchOverFailedNotify": ftForcedSwitchOverFailedNotify,
       "ftProcessRestartDisableNotify": ftProcessRestartDisableNotify,
       "updateDBAuditOpStatNotify": updateDBAuditOpStatNotify,
       "isupIccAuditNotify": isupIccAuditNotify,
       "cdrDiskFullMinorNotify": cdrDiskFullMinorNotify,
       "cdrDiskFullMajorNotify": cdrDiskFullMajorNotify,
       "cdrErrMoveCdrNackNotify": cdrErrMoveCdrNackNotify,
       "cdrFileMoveCdrNackNotify": cdrFileMoveCdrNackNotify,
       "ss7CktValidationNotify": ss7CktValidationNotify,
       "switchActiveAlarmTable": switchActiveAlarmTable,
       "switchActiveAlarmEntry": switchActiveAlarmEntry,
       "switchAlarmMsgId": switchAlarmMsgId,
       "switchAlarmInstNo": switchAlarmInstNo,
       "switchAlarmTime": switchAlarmTime,
       "switchAlarmType": switchAlarmType,
       "switchAlarmMainEvent": switchAlarmMainEvent,
       "switchAlarmSubEvent": switchAlarmSubEvent,
       "switchAlarmId": switchAlarmId,
       "switchAlarmSeverity": switchAlarmSeverity,
       "switchAlarmDesc": switchAlarmDesc,
       "switchAlarmAck": switchAlarmAck,
       "switchAlarmRepeatTime": switchAlarmRepeatTime,
       "services": services}
)
