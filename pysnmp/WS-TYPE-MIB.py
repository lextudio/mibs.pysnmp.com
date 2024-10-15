# SNMP MIB module (WS-TYPE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WS-TYPE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:24 2024
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


# Types definitions



class DoActionNow(Integer32):
    """Custom type DoActionNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doActionRightNow", 1),
          ("idleState", 2))
    )





class Password(OctetString):
    """Custom type Password based on OctetString"""




class StaticRowEnable(Integer32):
    """Custom type StaticRowEnable based on Integer32"""
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





class PartsPer10k(Unsigned32):
    """Custom type PartsPer10k based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )





class AbbrevRowStatus(Integer32):
    """Custom type AbbrevRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("createAndGo", 4),
          ("destroy", 6))
    )





class ScaleBy100(Unsigned32):
    """Custom type ScaleBy100 based on Unsigned32"""




class DoActionShowProgress(Integer32):
    """Custom type DoActionShowProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doActionRightNow", 1),
          ("idleState", 2))
    )





class HexPassword(OctetString):
    """Custom type HexPassword based on OctetString"""




class TransmitRate(Bits):
    """Custom type TransmitRate based on Bits"""




class RadioType(Integer32):
    """Custom type RadioType based on Integer32"""
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
        *(("radio802dot11A", 1),
          ("radio802dot11B", 2),
          ("radio802dot11FH", 4),
          ("radio802dot11G", 3))
    )





class SinglePointer(Integer32):
    """Custom type SinglePointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class MultiPointer63(Bits):
    """Custom type MultiPointer63 based on Bits"""




class MultiPointer64(Bits):
    """Custom type MultiPointer64 based on Bits"""




class MultiPointer255(Bits):
    """Custom type MultiPointer255 based on Bits"""




class MultiPointer256(Bits):
    """Custom type MultiPointer256 based on Bits"""




class MultiPointer512(Bits):
    """Custom type MultiPointer512 based on Bits"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WS-TYPE-MIB",
    **{"DoActionNow": DoActionNow,
       "Password": Password,
       "StaticRowEnable": StaticRowEnable,
       "PartsPer10k": PartsPer10k,
       "AbbrevRowStatus": AbbrevRowStatus,
       "ScaleBy100": ScaleBy100,
       "DoActionShowProgress": DoActionShowProgress,
       "HexPassword": HexPassword,
       "TransmitRate": TransmitRate,
       "RadioType": RadioType,
       "SinglePointer": SinglePointer,
       "MultiPointer63": MultiPointer63,
       "MultiPointer64": MultiPointer64,
       "MultiPointer255": MultiPointer255,
       "MultiPointer256": MultiPointer256,
       "MultiPointer512": MultiPointer512}
)
