# SNMP MIB module (COM21-HCX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COM21-HCX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:33 2024
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



class FrequencyKhz(Integer32):
    """Custom type FrequencyKhz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 800000),
    )





class UpstrmFreqKhz(Integer32):
    """Custom type UpstrmFreqKhz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 40000),
    )





class Gain(Integer32):
    """Custom type Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class StuGain(Integer32):
    """Custom type StuGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18, 58),
    )





class EpochTime(Integer32):
    """Custom type EpochTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class PrimServiceState(Integer32):
    """Custom type PrimServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oos", 2))
    )





class Offset(Integer32):
    """Custom type Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )





class AlarmSeverity(Integer32):
    """Custom type AlarmSeverity based on Integer32"""
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
        *(("clear", 1),
          ("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("warning", 2))
    )





class Com21RowStatus(Integer32):
    """Custom type Com21RowStatus based on Integer32"""
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
        *(("active", 1),
          ("create", 2),
          ("deactive", 4),
          ("destroy", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Com21_ObjectIdentity = ObjectIdentity
com21 = _Com21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141)
)
_Com21Hcx_ObjectIdentity = ObjectIdentity
com21Hcx = _Com21Hcx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2)
)
_Com21Stu_ObjectIdentity = ObjectIdentity
com21Stu = _Com21Stu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 3)
)
_Com21Traps_ObjectIdentity = ObjectIdentity
com21Traps = _Com21Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 4)
)
_Com21Nmaps_ObjectIdentity = ObjectIdentity
com21Nmaps = _Com21Nmaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 5)
)
_Com21Reg_ObjectIdentity = ObjectIdentity
com21Reg = _Com21Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COM21-HCX-MIB",
    **{"FrequencyKhz": FrequencyKhz,
       "UpstrmFreqKhz": UpstrmFreqKhz,
       "Gain": Gain,
       "StuGain": StuGain,
       "EpochTime": EpochTime,
       "PrimServiceState": PrimServiceState,
       "Offset": Offset,
       "AlarmSeverity": AlarmSeverity,
       "Com21RowStatus": Com21RowStatus,
       "com21": com21,
       "com21Hcx": com21Hcx,
       "com21Stu": com21Stu,
       "com21Traps": com21Traps,
       "com21Nmaps": com21Nmaps,
       "com21Reg": com21Reg}
)
