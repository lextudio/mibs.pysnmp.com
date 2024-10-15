# SNMP MIB module (HPNSAASR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPNSAASR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:18 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaASR_ObjectIdentity = ObjectIdentity
hpnsaASR = _HpnsaASR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 25)
)
_HpnsaASRMibRev_ObjectIdentity = ObjectIdentity
hpnsaASRMibRev = _HpnsaASRMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 1)
)


class _HpnsaASRMibRevMajor_Type(Integer32):
    """Custom type hpnsaASRMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaASRMibRevMajor_Type.__name__ = "Integer32"
_HpnsaASRMibRevMajor_Object = MibScalar
hpnsaASRMibRevMajor = _HpnsaASRMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 1, 1),
    _HpnsaASRMibRevMajor_Type()
)
hpnsaASRMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaASRMibRevMajor.setStatus("mandatory")


class _HpnsaASRMibRevMinor_Type(Integer32):
    """Custom type hpnsaASRMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaASRMibRevMinor_Type.__name__ = "Integer32"
_HpnsaASRMibRevMinor_Object = MibScalar
hpnsaASRMibRevMinor = _HpnsaASRMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 1, 2),
    _HpnsaASRMibRevMinor_Type()
)
hpnsaASRMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaASRMibRevMinor.setStatus("mandatory")
_HpnsaASRParms_ObjectIdentity = ObjectIdentity
hpnsaASRParms = _HpnsaASRParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 2)
)


class _HpnsaASRMaxConsecutiveASR_Type(Integer32):
    """Custom type hpnsaASRMaxConsecutiveASR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HpnsaASRMaxConsecutiveASR_Type.__name__ = "Integer32"
_HpnsaASRMaxConsecutiveASR_Object = MibScalar
hpnsaASRMaxConsecutiveASR = _HpnsaASRMaxConsecutiveASR_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 2, 1),
    _HpnsaASRMaxConsecutiveASR_Type()
)
hpnsaASRMaxConsecutiveASR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaASRMaxConsecutiveASR.setStatus("mandatory")
_HpnsaASRCurrentConsecutiveASR_Type = Integer32
_HpnsaASRCurrentConsecutiveASR_Object = MibScalar
hpnsaASRCurrentConsecutiveASR = _HpnsaASRCurrentConsecutiveASR_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 2, 2),
    _HpnsaASRCurrentConsecutiveASR_Type()
)
hpnsaASRCurrentConsecutiveASR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaASRCurrentConsecutiveASR.setStatus("mandatory")
_HpnsaASRTimeOutInterval_Type = Integer32
_HpnsaASRTimeOutInterval_Object = MibScalar
hpnsaASRTimeOutInterval = _HpnsaASRTimeOutInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 2, 3),
    _HpnsaASRTimeOutInterval_Type()
)
hpnsaASRTimeOutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaASRTimeOutInterval.setStatus("mandatory")
_HpnsaASRKickInterval_Type = Integer32
_HpnsaASRKickInterval_Object = MibScalar
hpnsaASRKickInterval = _HpnsaASRKickInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 2, 4),
    _HpnsaASRKickInterval_Type()
)
hpnsaASRKickInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaASRKickInterval.setStatus("mandatory")
_HpnsaASRTimeoutAction_Type = DisplayString
_HpnsaASRTimeoutAction_Object = MibScalar
hpnsaASRTimeoutAction = _HpnsaASRTimeoutAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 25, 2, 5),
    _HpnsaASRTimeoutAction_Type()
)
hpnsaASRTimeoutAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaASRTimeoutAction.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSAASR-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaASR": hpnsaASR,
       "hpnsaASRMibRev": hpnsaASRMibRev,
       "hpnsaASRMibRevMajor": hpnsaASRMibRevMajor,
       "hpnsaASRMibRevMinor": hpnsaASRMibRevMinor,
       "hpnsaASRParms": hpnsaASRParms,
       "hpnsaASRMaxConsecutiveASR": hpnsaASRMaxConsecutiveASR,
       "hpnsaASRCurrentConsecutiveASR": hpnsaASRCurrentConsecutiveASR,
       "hpnsaASRTimeOutInterval": hpnsaASRTimeOutInterval,
       "hpnsaASRKickInterval": hpnsaASRKickInterval,
       "hpnsaASRTimeoutAction": hpnsaASRTimeoutAction}
)
