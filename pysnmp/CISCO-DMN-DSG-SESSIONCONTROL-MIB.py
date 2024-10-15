# SNMP MIB module (CISCO-DMN-DSG-SESSIONCONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-SESSIONCONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:33 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ciscoDSGSessionControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6)
)
ciscoDSGSessionControl.setRevisions(
        ("2010-08-30 11:00",
         "2009-11-22 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SessionControlOpen_Type(Integer32):
    """Custom type sessionControlOpen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("writeOnly", 2))
    )


_SessionControlOpen_Type.__name__ = "Integer32"
_SessionControlOpen_Object = MibScalar
sessionControlOpen = _SessionControlOpen_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 1),
    _SessionControlOpen_Type()
)
sessionControlOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionControlOpen.setStatus("current")


class _SessionControlClose_Type(Integer32):
    """Custom type sessionControlClose based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignoreAndClose", 2),
          ("saveAndClose", 1),
          ("writeOnly", 3))
    )


_SessionControlClose_Type.__name__ = "Integer32"
_SessionControlClose_Object = MibScalar
sessionControlClose = _SessionControlClose_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 2),
    _SessionControlClose_Type()
)
sessionControlClose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionControlClose.setStatus("current")


class _SessionControlStatus_Type(Integer32):
    """Custom type sessionControlStatus based on Integer32"""
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
        *(("closed", 2),
          ("expired", 3),
          ("open", 1),
          ("openWithInvalidConfig", 4))
    )


_SessionControlStatus_Type.__name__ = "Integer32"
_SessionControlStatus_Object = MibScalar
sessionControlStatus = _SessionControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 3),
    _SessionControlStatus_Type()
)
sessionControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionControlStatus.setStatus("current")


class _SessionControlValidateStatus_Type(DisplayString):
    """Custom type sessionControlValidateStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_SessionControlValidateStatus_Type.__name__ = "DisplayString"
_SessionControlValidateStatus_Object = MibScalar
sessionControlValidateStatus = _SessionControlValidateStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 6, 4),
    _SessionControlValidateStatus_Type()
)
sessionControlValidateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionControlValidateStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-SESSIONCONTROL-MIB",
    **{"ciscoDSGSessionControl": ciscoDSGSessionControl,
       "sessionControlOpen": sessionControlOpen,
       "sessionControlClose": sessionControlClose,
       "sessionControlStatus": sessionControlStatus,
       "sessionControlValidateStatus": sessionControlValidateStatus}
)
