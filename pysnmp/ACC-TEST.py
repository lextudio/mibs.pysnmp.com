# SNMP MIB module (ACC-TEST) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-TEST
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:05 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccTest_ObjectIdentity = ObjectIdentity
accTest = _AccTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 49)
)
_AccDialTest_ObjectIdentity = ObjectIdentity
accDialTest = _AccDialTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 49, 1)
)


class _AccDialTestAction_Type(Integer32):
    """Custom type accDialTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("loopback", 1)
    )


_AccDialTestAction_Type.__name__ = "Integer32"
_AccDialTestAction_Object = MibScalar
accDialTestAction = _AccDialTestAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 49, 1, 1),
    _AccDialTestAction_Type()
)
accDialTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialTestAction.setStatus("mandatory")
_AccDialTestDialAddress_Type = OctetString
_AccDialTestDialAddress_Object = MibScalar
accDialTestDialAddress = _AccDialTestDialAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 49, 1, 2),
    _AccDialTestDialAddress_Type()
)
accDialTestDialAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialTestDialAddress.setStatus("mandatory")
_AccDialTestPort_Type = Integer32
_AccDialTestPort_Object = MibScalar
accDialTestPort = _AccDialTestPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 49, 1, 3),
    _AccDialTestPort_Type()
)
accDialTestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialTestPort.setStatus("mandatory")


class _AccDialTestMessageLevel_Type(Integer32):
    """Custom type accDialTestMessageLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccDialTestMessageLevel_Type.__name__ = "Integer32"
_AccDialTestMessageLevel_Object = MibScalar
accDialTestMessageLevel = _AccDialTestMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 49, 1, 4),
    _AccDialTestMessageLevel_Type()
)
accDialTestMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialTestMessageLevel.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-TEST",
    **{"accTest": accTest,
       "accDialTest": accDialTest,
       "accDialTestAction": accDialTestAction,
       "accDialTestDialAddress": accDialTestDialAddress,
       "accDialTestPort": accDialTestPort,
       "accDialTestMessageLevel": accDialTestMessageLevel}
)
