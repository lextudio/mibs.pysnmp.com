# SNMP MIB module (PW-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PW-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:22 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pwTCMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 8888, 1)
)
pwTCMIB.setRevisions(
        ("2003-07-28 12:00",
         "2003-05-01 12:00",
         "1902-05-28 12:00",
         "1902-01-30 12:00",
         "2001-12-20 12:00",
         "2001-07-12 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PwGroupID(Unsigned32, TextualConvention):
    status = "current"


class PwVcIDType(Unsigned32, TextualConvention):
    status = "current"


class PwVcIndexType(Unsigned32, TextualConvention):
    status = "current"


class PwVcVlanCfg(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )



class PwOperStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )



class PwVcType(Integer32, TextualConvention):
    status = "current"
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
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("atmAal5PduVcc", 14),
          ("atmAal5SduVcc", 2),
          ("atmCell1to1Vcc", 12),
          ("atmCell1to1Vpc", 13),
          ("atmCellNto1Vcc", 9),
          ("atmCellNto1Vpc", 10),
          ("atmTransparent", 3),
          ("cem", 8),
          ("cep", 16),
          ("ethernet", 5),
          ("ethernetTagged", 4),
          ("frameRelayDlci", 1),
          ("frameRelayPortMode", 15),
          ("hdlc", 6),
          ("ipLayer2Transport", 11),
          ("other", 0),
          ("ppp", 7))
    )



class PwVcAttachmentIdentifierType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class PwVcCw(TruthValue, TextualConvention):
    status = "current"


class PwVcRemoteCwStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("illegalRecievedBit", 4),
          ("notApplicable", 0),
          ("notYetKnown", 6),
          ("rxWithdrawWithWrongBitErrorCode", 3),
          ("sameAsSent", 5),
          ("sentWrongBitErrorCode", 2),
          ("waitingForNextMsg", 1))
    )



class PwVcCapabilities(Bits, TextualConvention):
    status = "current"


class PwVcStatus(Bits, TextualConvention):
    status = "current"


class PwVcFragSize(Unsigned32, TextualConvention):
    status = "current"


class PwVcFragStatus(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_PwMIB_ObjectIdentity = ObjectIdentity
pwMIB = _PwMIB_ObjectIdentity(
    (1, 3, 6, 1, 3, 8888)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PW-TC-MIB",
    **{"PwGroupID": PwGroupID,
       "PwVcIDType": PwVcIDType,
       "PwVcIndexType": PwVcIndexType,
       "PwVcVlanCfg": PwVcVlanCfg,
       "PwOperStatus": PwOperStatus,
       "PwVcType": PwVcType,
       "PwVcAttachmentIdentifierType": PwVcAttachmentIdentifierType,
       "PwVcCw": PwVcCw,
       "PwVcRemoteCwStatus": PwVcRemoteCwStatus,
       "PwVcCapabilities": PwVcCapabilities,
       "PwVcStatus": PwVcStatus,
       "PwVcFragSize": PwVcFragSize,
       "PwVcFragStatus": PwVcFragStatus,
       "pwMIB": pwMIB,
       "pwTCMIB": pwTCMIB}
)
