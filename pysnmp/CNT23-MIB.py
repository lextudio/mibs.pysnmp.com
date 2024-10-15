# SNMP MIB module (CNT23-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CNT23-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:55 2024
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

(cnt2Snmp,) = mibBuilder.importSymbols(
    "CNT2-MIB",
    "cnt2Snmp")

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

_Cnt2SubAgent_ObjectIdentity = ObjectIdentity
cnt2SubAgent = _Cnt2SubAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 333, 2, 3, 1)
)
_Cnt2RegistrationNum_Type = Integer32
_Cnt2RegistrationNum_Object = MibScalar
cnt2RegistrationNum = _Cnt2RegistrationNum_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 1),
    _Cnt2RegistrationNum_Type()
)
cnt2RegistrationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2RegistrationNum.setStatus("mandatory")
_Cnt2RegistrationTable_Object = MibTable
cnt2RegistrationTable = _Cnt2RegistrationTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cnt2RegistrationTable.setStatus("mandatory")
_Cnt2RegistrationEntry_Object = MibTableRow
cnt2RegistrationEntry = _Cnt2RegistrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1)
)
cnt2RegistrationEntry.setIndexNames(
    (0, "CNT23-MIB", "cnt2RegisterIndex"),
)
if mibBuilder.loadTexts:
    cnt2RegistrationEntry.setStatus("mandatory")
_Cnt2RegisterIndex_Type = Integer32
_Cnt2RegisterIndex_Object = MibTableColumn
cnt2RegisterIndex = _Cnt2RegisterIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 1),
    _Cnt2RegisterIndex_Type()
)
cnt2RegisterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2RegisterIndex.setStatus("mandatory")
_Cnt2RegisterSlot_Type = Integer32
_Cnt2RegisterSlot_Object = MibTableColumn
cnt2RegisterSlot = _Cnt2RegisterSlot_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 2),
    _Cnt2RegisterSlot_Type()
)
cnt2RegisterSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2RegisterSlot.setStatus("mandatory")


class _Cnt2RegisterProtocol_Type(Integer32):
    """Custom type cnt2RegisterProtocol based on Integer32"""
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
        *(("dpiv2", 2),
          ("local", 4),
          ("none", 1),
          ("smux", 3))
    )


_Cnt2RegisterProtocol_Type.__name__ = "Integer32"
_Cnt2RegisterProtocol_Object = MibTableColumn
cnt2RegisterProtocol = _Cnt2RegisterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 3),
    _Cnt2RegisterProtocol_Type()
)
cnt2RegisterProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2RegisterProtocol.setStatus("mandatory")


class _Cnt2RegisterTransport_Type(Integer32):
    """Custom type cnt2RegisterTransport based on Integer32"""
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
        *(("direct", 6),
          ("fl", 5),
          ("memory", 4),
          ("switch", 1),
          ("tcp", 2),
          ("udp", 3))
    )


_Cnt2RegisterTransport_Type.__name__ = "Integer32"
_Cnt2RegisterTransport_Object = MibTableColumn
cnt2RegisterTransport = _Cnt2RegisterTransport_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 4),
    _Cnt2RegisterTransport_Type()
)
cnt2RegisterTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2RegisterTransport.setStatus("mandatory")


class _Cnt2RegisterAgentDescr_Type(DisplayString):
    """Custom type cnt2RegisterAgentDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cnt2RegisterAgentDescr_Type.__name__ = "DisplayString"
_Cnt2RegisterAgentDescr_Object = MibTableColumn
cnt2RegisterAgentDescr = _Cnt2RegisterAgentDescr_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 5),
    _Cnt2RegisterAgentDescr_Type()
)
cnt2RegisterAgentDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2RegisterAgentDescr.setStatus("mandatory")
_Cnt2RegisterGroup_Type = ObjectIdentifier
_Cnt2RegisterGroup_Object = MibTableColumn
cnt2RegisterGroup = _Cnt2RegisterGroup_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 6),
    _Cnt2RegisterGroup_Type()
)
cnt2RegisterGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2RegisterGroup.setStatus("mandatory")


class _Cnt2RegisterMibVersion_Type(DisplayString):
    """Custom type cnt2RegisterMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cnt2RegisterMibVersion_Type.__name__ = "DisplayString"
_Cnt2RegisterMibVersion_Object = MibTableColumn
cnt2RegisterMibVersion = _Cnt2RegisterMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 7),
    _Cnt2RegisterMibVersion_Type()
)
cnt2RegisterMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2RegisterMibVersion.setStatus("mandatory")
_Cnt2RegisterUpTime_Type = TimeTicks
_Cnt2RegisterUpTime_Object = MibTableColumn
cnt2RegisterUpTime = _Cnt2RegisterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 8),
    _Cnt2RegisterUpTime_Type()
)
cnt2RegisterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2RegisterUpTime.setStatus("mandatory")


class _Cnt2RegisterRowInstance_Type(DisplayString):
    """Custom type cnt2RegisterRowInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cnt2RegisterRowInstance_Type.__name__ = "DisplayString"
_Cnt2RegisterRowInstance_Object = MibTableColumn
cnt2RegisterRowInstance = _Cnt2RegisterRowInstance_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 3, 1, 2, 1, 9),
    _Cnt2RegisterRowInstance_Type()
)
cnt2RegisterRowInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2RegisterRowInstance.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CNT23-MIB",
    **{"cnt2SubAgent": cnt2SubAgent,
       "cnt2RegistrationNum": cnt2RegistrationNum,
       "cnt2RegistrationTable": cnt2RegistrationTable,
       "cnt2RegistrationEntry": cnt2RegistrationEntry,
       "cnt2RegisterIndex": cnt2RegisterIndex,
       "cnt2RegisterSlot": cnt2RegisterSlot,
       "cnt2RegisterProtocol": cnt2RegisterProtocol,
       "cnt2RegisterTransport": cnt2RegisterTransport,
       "cnt2RegisterAgentDescr": cnt2RegisterAgentDescr,
       "cnt2RegisterGroup": cnt2RegisterGroup,
       "cnt2RegisterMibVersion": cnt2RegisterMibVersion,
       "cnt2RegisterUpTime": cnt2RegisterUpTime,
       "cnt2RegisterRowInstance": cnt2RegisterRowInstance}
)
